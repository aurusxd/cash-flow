"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

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
