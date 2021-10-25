from .models import Schema, Column, Dataset
from . import column_types
import os
from django.conf import settings
from test_planeks.celery import app


@app.task
def generate_csv(qty: int, schema: Schema, dataset):
    try:
        filename = f"{schema['name']}.csv"
        filename_path = os.path.join(settings.MEDIA_ROOT, filename)
        with open(filename_path, 'w') as file:
            columns = Column.objects.filter(schema=schema['id'])
            separator = schema['separator']
            string_char = schema['string_character']
            header = ''
            for column in columns:
                header += f'{column.name}{separator}'
            file.write(header+'\n')
            for j in range(qty):
                row = ''
                for column in columns:
                    field_type = column.field_type
                    upper = column.upper_bound
                    lower = column.lower_bound
                    sentence_count = column.sentence_count
                    generator = column_types[field_type]
                    if field_type == 7:
                        row += f'{generator(qty=sentence_count, string_char=string_char, separator=separator)}'
                    elif field_type == 8:
                        row += f'{generator(lower=lower, upper=upper)}'
                    else:
                        row += generator().replace(separator, '')
                    row += separator
                file.write(row+'\n')
        dataset = Dataset.objects.get(id=dataset['id'])
        dataset.status = "SUCCESS"
        dataset.save()
    except:
        dataset = Dataset.objects.get(id=dataset['id'])
        dataset.status = "FAILURE"
        dataset.save()
    return dataset.status
