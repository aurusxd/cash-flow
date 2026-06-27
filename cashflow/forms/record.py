from django import forms

from cashflow.models import Record


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
                "step": "0.01",
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
