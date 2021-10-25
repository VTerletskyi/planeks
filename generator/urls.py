from django.urls import path
from .views import (
    SchemaCreateApiView,
    SchemaListApiView,
    SchemaDeleteApiView,
    DatasetGenerateApiView,
    DatasetDownloadApiView,
    DatasetListApiView
)

urlpatterns = [
    path('create-schema/', SchemaCreateApiView.as_view()),
    path('schemas/', SchemaListApiView.as_view()),
    path('delete/<str:schema_id>/', SchemaDeleteApiView.as_view()),
    path('run/', DatasetGenerateApiView.as_view()),
    path('download/<str:filename>/', DatasetDownloadApiView.as_view()),
    path('datasets/', DatasetListApiView.as_view()),
]
