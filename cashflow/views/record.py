from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from cashflow.forms import RecordForm
from cashflow.models import Category, OperationType, Record, Status, Subcategory
from cashflow.selectors.record import get_records_queryset


class RecordListView(ListView):
    model = Record

    template_name = "record_list.html"

    context_object_name = "records"

    def get_queryset(self):
        queryset = get_records_queryset()

        if date_from := self.request.GET.get("date_from"):
            queryset = queryset.filter(date__gte=date_from)

        if date_to := self.request.GET.get("date_to"):
            queryset = queryset.filter(date__lte=date_to)

        if status := self.request.GET.get("status"):
            queryset = queryset.filter(status_id=status)

        if operation_type := self.request.GET.get("operation_type"):
            queryset = queryset.filter(operation_type_id=operation_type)

        if category := self.request.GET.get("category"):
            queryset = queryset.filter(category_id=category)

        if subcategory := self.request.GET.get("subcategory"):
            queryset = queryset.filter(subcategory_id=subcategory)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        selected_operation_type = self.request.GET.get("operation_type", "")
        selected_category = self.request.GET.get("category", "")

        # Списки фильтров должны учитывать выбранные родительские справочники.
        categories = Category.objects.select_related("operation_type")
        if selected_operation_type:
            categories = categories.filter(operation_type_id=selected_operation_type)

        subcategories = Subcategory.objects.select_related("category")
        if selected_category:
            subcategories = subcategories.filter(category_id=selected_category)

        context.update(
            {
                "statuses": Status.objects.all(),
                "operation_types": OperationType.objects.all(),
                "categories": categories,
                "subcategories": subcategories,
                "selected_filters": {
                    "date_from": self.request.GET.get("date_from", ""),
                    "date_to": self.request.GET.get("date_to", ""),
                    "status": self.request.GET.get("status", ""),
                    "operation_type": selected_operation_type,
                    "category": selected_category,
                    "subcategory": self.request.GET.get("subcategory", ""),
                },
            }
        )

        return context


class RecordCreateView(CreateView):
    model = Record
    form_class = RecordForm
    template_name = "record_form.html"
    success_url = reverse_lazy("record_list")

    def form_valid(self, form):
        messages.success(self.request, "Запись успешно создана.")
        return super().form_valid(form)


class RecordDeleteView(DeleteView):
    model = Record
    template_name = "record_delete.html"
    success_url = reverse_lazy("record_list")

    def form_valid(self, form):
        messages.success(self.request, "Запись успешно удалена.")
        return super().form_valid(form)


class RecordDeleteSelectedView(View):
    def post(self, request):
        selected_record_ids = request.POST.getlist("selected_records")

        if not selected_record_ids:
            messages.warning(request, "Выберите хотя бы одну запись.")
            return redirect("record_list")

        deleted_count, _ = Record.objects.filter(id__in=selected_record_ids).delete()

        messages.success(request, f"Удалено записей: {deleted_count}.")
        return redirect("record_list")


class RecordUpdateView(UpdateView):
    model = Record
    form_class = RecordForm
    template_name = "record_update.html"
    success_url = reverse_lazy("record_list")

    def form_valid(self, form):
        messages.success(self.request, "Запись успешно обновлена.")
        return super().form_valid(form)


def get_categories(request):
    operation_type_id = request.GET.get("operation_type_id")

    categories = Category.objects.filter(operation_type_id=operation_type_id).values(
        "id", "name"
    )

    return JsonResponse(list(categories), safe=False)


def get_subcategories(request):
    category_id = request.GET.get("category_id")

    subcategories = Subcategory.objects.filter(category_id=category_id).values(
        "id", "name"
    )

    return JsonResponse(list(subcategories), safe=False)
