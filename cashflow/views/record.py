from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from cashflow.forms import RecordForm
from cashflow.models import Record
from cashflow.selectors.record import get_records_queryset


class RecordListView(ListView):
    model = Record

    template_name = "record_list.html"

    context_object_name = "records"

    queryset = get_records_queryset()


class RecordCreateView(CreateView):
    model = Record
    form_class = RecordForm

    template_name = "record_form.html"

    success_url = reverse_lazy("record_list")
