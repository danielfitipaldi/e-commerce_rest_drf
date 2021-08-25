from django.urls import path

from products.api.views.general_views import MeasureUnitListApiView, IndicatorListApiView, CategoryProductListApiView

urlpatterns = [
    path('measure_unit/', MeasureUnitListApiView.as_view(), name='measure_unit'),
    path('indicator/', IndicatorListApiView.as_view(), name='indicator'),

]