"""Маршруты веб-приложения ДДС."""

from django.contrib import admin
from django.urls import path

from cashflow.views.record import (
    RecordCreateView,
    RecordDeleteSelectedView,
    RecordDeleteView,
    RecordListView,
    RecordUpdateView,
    get_categories,
    get_subcategories,
)
from cashflow.views.reference import (
    ReferenceCreateView,
    ReferenceDeleteView,
    ReferenceListView,
    ReferenceUpdateView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RecordListView.as_view(), name="record_list"),
    path("records/create/", RecordCreateView.as_view(), name="record_create"),
    path(
        "records/delete/",
        RecordDeleteSelectedView.as_view(),
        name="record_delete_selected",
    ),
    path(
        "records/<int:pk>/delete/",
        RecordDeleteView.as_view(),
        name="record_delete",
    ),
    path(
        "records/<int:pk>/update/",
        RecordUpdateView.as_view(),
        name="record_update",
    ),
    path(
        "references/<str:reference_slug>/",
        ReferenceListView.as_view(),
        name="reference_list",
    ),
    path(
        "references/<str:reference_slug>/create/",
        ReferenceCreateView.as_view(),
        name="reference_create",
    ),
    path(
        "references/<str:reference_slug>/<int:pk>/update/",
        ReferenceUpdateView.as_view(),
        name="reference_update",
    ),
    path(
        "references/<str:reference_slug>/<int:pk>/delete/",
        ReferenceDeleteView.as_view(),
        name="reference_delete",
    ),
    path("ajax/categories/", get_categories, name="ajax_categories"),
    path("ajax/subcategories/", get_subcategories, name="ajax_subcategories"),
]
