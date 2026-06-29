from django.core.management.base import BaseCommand

from cashflow.models import Category, OperationType, Status, Subcategory


class Command(BaseCommand):
    help = "Create default cash flow dictionaries."

    def handle(self, *_args, **_options):
        statuses = ("Бизнес", "Личное", "Налог")
        operation_types = ("Пополнение", "Списание")
        categories = {
            "Пополнение": {
                "Доходы": ("Продажи", "Возвраты"),
            },
            "Списание": {
                "Инфраструктура": ("VPS", "Proxy"),
                "Маркетинг": ("Farpost", "Avito"),
            },
        }

        created_count = 0

        for status_name in statuses:
            _, created = Status.objects.get_or_create(name=status_name)
            created_count += int(created)

        operation_type_by_name = {}
        for operation_type_name in operation_types:
            operation_type, created = OperationType.objects.get_or_create(
                name=operation_type_name
            )
            operation_type_by_name[operation_type_name] = operation_type
            created_count += int(created)

        for operation_type_name, category_items in categories.items():
            operation_type = operation_type_by_name[operation_type_name]

            for category_name, subcategory_names in category_items.items():
                category, created = Category.objects.get_or_create(
                    name=category_name,
                    operation_type=operation_type,
                )
                created_count += int(created)

                for subcategory_name in subcategory_names:
                    _, created = Subcategory.objects.get_or_create(
                        name=subcategory_name,
                        category=category,
                    )
                    created_count += int(created)

        self.stdout.write(
            self.style.SUCCESS(
                f"Default dictionaries are ready. Created objects: {created_count}."
            )
        )
