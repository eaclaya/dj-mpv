from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    expired = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ['name', 'domain', 'due_date', 'contact', 'email', 'expired']

    def get_expired(self, obj):
        from datetime import date
        return obj.due_date is not None and obj.due_date < date.today()

