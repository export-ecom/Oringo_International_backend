from rest_framework import serializers
from .models import Inquiry

class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = ("id","user","name","email","subject","message","status","created_at")
        read_only_fields = ("id","user","status","created_at")

    def create(self, validated_data):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            validated_data["user"] = request.user
            if not validated_data.get("email"):
                validated_data["email"] = request.user.email
            if not validated_data.get("name"):
                validated_data["name"] = request.user.get_full_name() or request.user.username
        return super().create(validated_data)
