from django.urls import path

from products.api.views.general_views import MeasureUnitListApiView, IndicatorListApiView, CategoryProductListApiView
from products.api.views.product_views import (ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView)

urlpatterns = [
    path('measure_unit/', MeasureUnitListApiView.as_view(), name='measure_unit'),
    path('indicator/', IndicatorListApiView.as_view(), name='indicator'),
    path('category_product', CategoryProductListApiView.as_view(), name='category_product'),
    path('product/', ProductListCreateAPIView.as_view(), name='product_create'),
    path('product/retrieve-update-destroy/<pk>', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product_retrieve_update_destroy'),

]