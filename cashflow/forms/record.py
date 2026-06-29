from django import forms

from cashflow.models import Category, Record, Subcategory


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record

        fields = (
            "date",
            "status",
            "operation_type",
            "category",
            "subcategory",
            "amount",
            "comment",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["date"].widget = forms.DateInput(
            attrs={
                "type": "date",
                "class": "form-control",
            }
        )

        self.fields["status"].widget.attrs.update(
            {
                "class": "form-select",
            }
        )

        self.fields["operation_type"].widget.attrs.update(
            {
                "class": "form-select",
            }
        )

        self.fields["category"].widget.attrs.update(
            {
                "class": "form-select",
            }
        )

        self.fields["subcategory"].widget.attrs.update(
            {
                "class": "form-select",
            }
        )

        self.fields["amount"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите сумму",
                "min": "0",
                "step": "1",
            }
        )

        self.fields["comment"].widget.attrs.update(
            {
                "class": "form-control",
                "rows": 4,
                "placeholder": "Комментарий (необязательно)",
            }
        )

        self.fields["comment"].required = False

        self.fields["category"].queryset = Category.objects.none()
        self.fields["subcategory"].queryset = Subcategory.objects.none()

        operation_type_id = self.data.get("operation_type")
        category_id = self.data.get("category")

        if operation_type_id:
            self.fields["category"].queryset = Category.objects.filter(
                operation_type_id=operation_type_id
            )

        if category_id:
            self.fields["subcategory"].queryset = Subcategory.objects.filter(
                category_id=category_id
            )

        if self.instance.pk:
            self.fields["category"].queryset = Category.objects.filter(
                operation_type=self.instance.operation_type
            )
            self.fields["subcategory"].queryset = Subcategory.objects.filter(
                category=self.instance.category
            )

    def clean(self):
        cleaned_data = super().clean()

        operation_type = cleaned_data.get("operation_type")
        category = cleaned_data.get("category")
        subcategory = cleaned_data.get("subcategory")

        if (
            category
            and operation_type
            and category.operation_type_id != operation_type.id
        ):
            self.add_error(
                "category",
                "Категория не относится к выбранному типу.",
            )

        if subcategory and category and subcategory.category_id != category.id:
            self.add_error(
                "subcategory",
                "Подкатегория не относится к выбранной категории.",
            )

        return cleaned_data
