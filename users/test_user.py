"""
TestUserSerializer - Creados como exemplos en las clases para prueba
                     las ediciones en el serializer


"""
from rest_framework import serializers
from users.models import User

class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()

    def validate_name(self, value):
        # custom validation
        if 'daniel' in value:
            raise serializers.ValidationError('Error! No puede existir un usuario con ese nombre')
        return value

    def validate_email(self, value):
        if value == '':
            raise serializers.ValidationError('Tiene que indicar un correo')
        return value

    def validate(self, data):
        #if data['name'] in data['email']:
            #raise serializers.ValidationError('El email no puede contener nombre')
        return data

    def create(self, validated_data):
        print(validated_data)
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance