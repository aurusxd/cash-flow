from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from cashflow.forms import RecordForm
from cashflow.models import Record
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


class RecordCreateView(CreateView):
    model = Record
    form_class = RecordForm
    template_name = "record_form.html"
    success_url = reverse_lazy("record_list")

    def form_valid(self, form):
        messages.success(self.request, "Запись успешно создана.")
        return super().form_valid(form)
