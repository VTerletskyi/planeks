# from django.views.generic import UpdateView
# from django.forms import ModelForm, TextInput, DateTimeInput
from .models import Schema, Column, Dataset
from rest_framework import serializers


class SchemaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schema
        fields = (
            'id', 'name', 'separator', 'string_character'
        )
        success_url = '/'


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = (
            'name', 'schema', 'field_type',
            'lower_bound', 'upper_bound', 'sentence_count'
        )


class SchemaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schema
        fields = (
            'id', 'name', 'pretty_updated_at',
        )


class DatasetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = (
            'schema', 'status', 'download_url'
        )


class DatasetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = (
            'id', 'pretty_created_at', 'status', 'download_url'
        )


class SchemaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schema
        fields = (
            'id', 'name', 'separator', 'string_ch aracter',
        )


# class PostForm(ModelForm):
#     class Meta:
#         model = Schema
#         fields = ['name']
#
#         widgets = {
#             "name": TextInput(attrs={
#                 "class": "form-control",
#                 "placeholder": "name"
#             })}
#
#
# class SchemaUpdateApiView(UpdateView):
#     model = Schema
#     template_name = "schemas.html"
#
#     form_class = PostForm
