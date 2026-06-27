from cashflow.models import Record


def get_records_queryset():
    return Record.objects.select_related(
        "status",
        "operation_type",
        "category",
        "subcategory",
    )
