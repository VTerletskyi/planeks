from .serializers import ColumnSerializer
from .models import Schema
from typing import List


def create_columns(data_list: List, schema: Schema):
    for data in data_list:
        data['lower_bound'] = data['lower_bound'] if data['lower_bound'] else None
        data['upper_bound'] = data['upper_bound'] if data['upper_bound'] else None
        data['sentence_count'] = data['sentence_count'] if data['sentence_count'] else None
        data['schema'] = schema.id
        field_serializer = ColumnSerializer(data=data)
        field_serializer.is_valid(raise_exception=True)
        field_serializer.save()
