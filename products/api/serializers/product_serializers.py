from rest_framework import serializers

from products.models import Product
from products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer


class ProductSerializer(serializers.ModelSerializer):
    #measure_unit = serializers.StringRelatedField()
    #category_product = serializers.StringRelatedField()

    class Meta:
        model = Product
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name':instance.name,
            'description': instance.description,
            'image': instance.image if instance.image != '' else '' or 'null',
            'measure_unit': instance.measure_unit.description if instance.measure_unit is not None else '',
            'categort_product': instance.category_product.description if instance.category_product is not None else ''
        }