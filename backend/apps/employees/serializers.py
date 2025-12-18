from rest_framework import serializers
from .models import Employee
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("user",)


class EmployeeSerializer(serializers.ModelSerializer):
    user_info = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = "__all__"

    def get_user_info(self, obj):
        user = obj.user  # now this resolves correctly
        if user is None:
            return None
        return {
            "id": user.id,
            "email": user.email,
        }
