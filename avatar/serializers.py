from rest_framework import serializers
from .models import Avatar


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = ("id", "gender", "skin_tone", "hair_style", "clothing", "accessories")
        read_only_fields = ("id",)

    def validate_clothing(self, value):
        required_fields = ["top", "bottom", "shoes"]
        if not all(field in value for field in required_fields):
            raise serializers.ValidationError(
                f"Clothing must contain all required fields: {', '.join(required_fields)}"
            )
        return value
