from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status, mixins
from rest_framework.response import Response

from .models import *
from .serializers import *


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer

    def list(self, request):
        queryset = Categories.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        data = serializer.data
        return Response(data)


class SubCategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = SubCategories.objects.all()
    serializer_class = SubCategorySerializer

    def list(self, request):
        queryset = SubCategories.objects.all()
        serializer = SubCategorySerializer(queryset, many=True)
        data = serializer.data
        return Response(data)

    def get_category_data(self, request=None):
        if request:
            get_category = request.GET.get('q')
            if get_category:
                category = Categories.objects.filter(category_name=get_category).first()
                if category:
                    querset = SubCategories.objects.filter(category=category.id)
                    querset = SubCategorySerializer(querset, many=True)
                    return Response(querset.data, status=status.HTTP_200_OK)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)


class ProductViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    def list(self, request):
        queryset = Products.objects.all()
        serializer = ProductsSerializer(queryset, many=True)
        data = serializer.data
        return Response(data)

    def create(self, request, td_id=None):
        document_data = request.data.copy()
        category = Categories.objects.filter(id=document_data['category']).first()
        sub_category = SubCategories.objects.filter(id=document_data['sub_category']).first()
        final_dict = dict()

        final_dict['category'] = category.pk
        final_dict['sub_category'] = sub_category.pk
        final_dict['product_name'] = document_data['product_name']
        serializer = ProductsAllSerializer(data=final_dict)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        headers.update({'Cache-Control': 'no-cache, max-age=0, must-revalidate'})
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_products(self, request=None):
        if request:
            get_category = request.GET.get('q')
            get_sub_category = request.GET.get('s')
            category_data = sub_category_data = querset = None
            if get_category:
                category_data = Categories.objects.filter(id=int(get_category)).first()
            if get_sub_category:
                sub_category_data = SubCategories.objects.filter(id=int(get_sub_category)).first()
            if category_data and sub_category_data:
                querset = Products.objects.filter(category=int(category_data.id),
                                                  sub_category=int(sub_category_data.id))
            elif category_data and not sub_category_data:
                querset = Products.objects.filter(category=int(category_data.id))
            elif sub_category_data and not category_data:
                querset = Products.objects.filter(sub_category=int(sub_category_data.id))
            if querset:
                querset = ProductsSerializer(querset, many=True)
                return Response(querset.data, status=status.HTTP_200_OK)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
