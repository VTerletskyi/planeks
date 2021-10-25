from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from .models import Schema, Dataset
from .serializers import SchemaCreateSerializer, SchemaListSerializer, DatasetListSerializer, DatasetCreateSerializer, SchemaDetailSerializer
from .services import create_columns
from .tasks import generate_csv
import mimetypes
from django.http import HttpResponse


class SchemaCreateApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        schema_data = request.data
        fields_data = schema_data.pop('data')
        serializer = SchemaCreateSerializer(data=schema_data)
        serializer.is_valid(raise_exception=True)
        schema = serializer.save()
        create_columns(data_list=fields_data, schema=schema)

        return Response(status=status.HTTP_201_CREATED)


class SchemaListApiView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        queryset = Schema.objects.all()
        serializer = SchemaListSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class SchemaDeleteApiView(APIView):
    permission_classes = (IsAuthenticated, )

    def delete(self, request, schema_id):
        Schema.objects.get(id=schema_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DatasetGenerateApiView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        data = request.data
        qty = int(data['qty']) if data['qty'] else 0
        schemas = Schema.objects.all()
        for schema in schemas:
            filename = f"{schema.name}.csv"
            dataset_data = {
                'schema': schema.id,
                'download_url': filename
            }
            serializer = DatasetCreateSerializer(data=dataset_data)
            serializer.is_valid(raise_exception=True)
            dataset = serializer.save()
            dataset = DatasetListSerializer(dataset)
            schema_serializer = SchemaDetailSerializer(schema)
            generate_csv.apply_async((int(qty), schema_serializer.data, dataset.data), countdown=5)
        return Response(status=status.HTTP_201_CREATED)


class DatasetDownloadApiView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, filename):
        fl_path = f'/src/media/{filename}'
        fl = open(fl_path, 'r')
        mime_type, _ = mimetypes.guess_type(fl_path)
        response = HttpResponse(fl, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response


class DatasetListApiView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        qs = Dataset.objects.all()
        serializer = DatasetListSerializer(qs, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
