from rest_framework import serializers

from movies.models import Gostos, GostosDoPaciente, GostosDoPsico


class GostosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gostos
        fields = ['id', 'gosto']


class GostosDoPacienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = GostosDoPacient
        fields = ['id', 'gosto']

class GostosDoPsicoSerializer(serializers.ModelSerializer):

    class Meta:
        model = GostosDoPsico
        fields = ['id', 'gosto']