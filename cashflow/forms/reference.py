from django import forms

from cashflow.models import Category, OperationType, Status, Subcategory


class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            css_class = (
                "form-select" if field.widget.input_type == "select" else "form-control"
            )
            field.widget.attrs.setdefault("class", css_class)


class StatusForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Status
        fields = ("name",)


class OperationTypeForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = OperationType
        fields = ("name",)


class CategoryForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Category
        fields = ("name", "operation_type")


class SubcategoryForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ("name", "category")
