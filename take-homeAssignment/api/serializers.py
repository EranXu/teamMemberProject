from rest_framework.serializers import ModelSerializer
from .models import TeamMember

class TeamsSerializer(ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'