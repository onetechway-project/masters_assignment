from rest_framework import routers
from django.urls import path
from django.conf.urls import url, include

from . import views

app_name = 'category'

router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet)
router.register(r'sub-category', views.SubCategoryViewSet)
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    url(r'api/', include(router.urls)),
    url("api/filter-sub-category/", views.SubCategoryViewSet.as_view({"get": 'get_category_data'}), name="get_category_data"),
    url("api/filter-products/", views.ProductViewSet.as_view({"get": 'get_products'}), name="get_products"),
]