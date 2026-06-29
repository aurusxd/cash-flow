from dataclasses import dataclass

from django.contrib import messages
from django.db.models import ProtectedError
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from cashflow.forms import CategoryForm, OperationTypeForm, StatusForm, SubcategoryForm
from cashflow.models import Category, OperationType, Status, Subcategory


@dataclass(frozen=True)
class ReferenceConfig:
    slug: str
    title: str
    model: type
    form_class: type
    columns: tuple[tuple[str, str], ...]
    queryset_relations: tuple[str, ...] = ()


REFERENCES = {
    "statuses": ReferenceConfig(
        slug="statuses",
        title="Статусы",
        model=Status,
        form_class=StatusForm,
        columns=(("name", "Название"),),
    ),
    "operation-types": ReferenceConfig(
        slug="operation-types",
        title="Типы операций",
        model=OperationType,
        form_class=OperationTypeForm,
        columns=(("name", "Название"),),
    ),
    "categories": ReferenceConfig(
        slug="categories",
        title="Категории",
        model=Category,
        form_class=CategoryForm,
        columns=(("name", "Название"), ("operation_type", "Тип операции")),
        queryset_relations=("operation_type",),
    ),
    "subcategories": ReferenceConfig(
        slug="subcategories",
        title="Подкатегории",
        model=Subcategory,
        form_class=SubcategoryForm,
        columns=(("name", "Название"), ("category", "Категория")),
        queryset_relations=("category", "category__operation_type"),
    ),
}


class ReferenceMixin:
    reference: ReferenceConfig

    def dispatch(self, request, *args, **kwargs):
        try:
            self.reference = REFERENCES[kwargs["reference_slug"]]
        except KeyError as exc:
            msg = "Справочник не найден."
            raise Http404(msg) from exc

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = self.reference.model.objects.all()
        if self.reference.queryset_relations:
            queryset = queryset.select_related(*self.reference.queryset_relations)
        return queryset

    def get_success_url(self):
        return reverse(
            "reference_list",
            kwargs={"reference_slug": self.reference.slug},
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reference"] = self.reference
        context["references"] = REFERENCES.values()
        return context


class ReferenceListView(ReferenceMixin, ListView):
    template_name = "reference_list.html"
    context_object_name = "items"


class ReferenceCreateView(ReferenceMixin, CreateView):
    template_name = "reference_form.html"

    def get_form_class(self):
        return self.reference.form_class

    def form_valid(self, form):
        messages.success(self.request, "Элемент справочника создан.")
        return super().form_valid(form)


class ReferenceUpdateView(ReferenceMixin, UpdateView):
    template_name = "reference_form.html"

    def get_form_class(self):
        return self.reference.form_class

    def form_valid(self, form):
        messages.success(self.request, "Элемент справочника обновлен.")
        return super().form_valid(form)


class ReferenceDeleteView(ReferenceMixin, DeleteView):
    template_name = "reference_confirm_delete.html"

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
        except ProtectedError:
            messages.error(
                self.request,
                (
                    "Нельзя удалить элемент справочника, "
                    "который используется в записях ДДС."
                ),
            )
            return redirect(self.get_success_url())

        messages.success(self.request, "Элемент справочника удален.")
        return response
