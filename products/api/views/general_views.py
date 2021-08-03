from products.api.serializers.general_serializers import MeasureUnitSerializer, IndicatorSerializer, \
    CategoryProductSerializer

from base.api import GeneralListApiView


class MeasureUnitListApiView(GeneralListApiView):
    serializer_class = MeasureUnitSerializer


class IndicatorListApiView(GeneralListApiView):
    serializer_class = IndicatorSerializer


class CategoryProductListApiView(GeneralListApiView):
    serializer_class = CategoryProductSerializer



