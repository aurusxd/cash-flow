from django.db import models
from django.utils import timezone


class Status(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

    def __str__(self):
        return self.name


class OperationType(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")

    class Meta:
        verbose_name = "Тип операции"
        verbose_name_plural = "Типы операций"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    operation_type = models.ForeignKey(
        OperationType,
        on_delete=models.CASCADE,
        related_name="categories",
        verbose_name="Тип операции",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        unique_together = ("name", "operation_type")

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="subcategories",
        verbose_name="Категория",
    )

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
        unique_together = ("name", "category")

    def __str__(self):
        return self.name


class Record(models.Model):
    date = models.DateField(default=timezone.now, verbose_name="Дата")
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name="records",
        verbose_name="Статус",
    )
    operation_type = models.ForeignKey(
        OperationType,
        on_delete=models.PROTECT,
        related_name="records",
        verbose_name="Тип",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="records",
        verbose_name="Категория",
    )
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.PROTECT,
        related_name="records",
        verbose_name="Подкатегория",
    )
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name="Сумма",
    )
    comment = models.TextField(
        blank=True,
        null=True,
        verbose_name="Комментарий",
    )

    class Meta:
        verbose_name = "Запись ДДС"
        verbose_name_plural = "Записи ДДС"
        ordering = ["-date"]  # noqa: RUF012

    def __str__(self):
        return f"{self.date} — {self.amount} ₽"
