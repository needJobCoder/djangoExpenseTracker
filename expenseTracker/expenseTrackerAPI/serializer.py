from rest_framework import serializers
from .models import Users, Purchases


class UserSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class PurchaseSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Purchases
        fields = "__all__"
