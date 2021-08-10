from django.urls import path

from products.api.views.general_views import MeasureUnitListApiView, IndicatorListApiView, CategoryProductListApiView
from products.api.views.product_views import (ProductListAPIView, ProductCreateAPIView, ProductRetrieveAPIView,
                                              ProductDestroyAPIView, ProductUpdateAPIView)

urlpatterns = [
    path('measure_unit/', MeasureUnitListApiView.as_view(), name='measure_unit'),
    path('indicator/', IndicatorListApiView.as_view(), name='indicator'),
    path('category_product', CategoryProductListApiView.as_view(), name='category_product'),
    path('product/list', ProductListAPIView.as_view(), name='product_list'),
    path('product/create', ProductCreateAPIView.as_view(), name='product_create'),
    path('product/retrieve/<pk>', ProductRetrieveAPIView.as_view(), name='product_retrieve'),
    path('product/destroy/<pk>', ProductDestroyAPIView.as_view(), name='product_destroy'),
    path('product/update/<pk>', ProductUpdateAPIView.as_view(), name='product_update'),

]