# Create your views here.
from django.shortcuts import render
from .models import Record, Status, OperationType, Category, Subcategory


def record_list(request):
    records = Record.objects.select_related(
        "status",
        "operation_type",
        "category",
        "subcategory",
    ).all()

    date_from = request.GET.get("date_from")
    date_to = request.GET.get("date_to")
    status = request.GET.get("status")
    operation_type = request.GET.get("operation_type")
    category = request.GET.get("category")
    subcategory = request.GET.get("subcategory")

    if date_from:
        records = records.filter(date__gte=date_from)

    if date_to:
        records = records.filter(date__lte=date_to)

    if status:
        records = records.filter(status_id=status)

    if operation_type:
        records = records.filter(operation_type_id=operation_type)

    if category:
        records = records.filter(category_id=category)

    if subcategory:
        records = records.filter(subcategory_id=subcategory)

    context = {
        "records": records,
        "statuses": Status.objects.all(),
        "operation_types": OperationType.objects.all(),
        "categories": Category.objects.all(),
        "subcategories": Subcategory.objects.all(),
    }

    return render(request, "record_list.html", context)