from rest_framework import serializers
from .models import DataPoint

class DataPointSerializer(serializers.ModelSerializer):
    # Define fields with special handling for empty strings
    intensity = serializers.SerializerMethodField()
    impact = serializers.SerializerMethodField()
    likelihood = serializers.SerializerMethodField()
    relevance = serializers.SerializerMethodField()
    end_year = serializers.SerializerMethodField()
    start_year = serializers.SerializerMethodField()

    class Meta:
        model = DataPoint
        fields = '__all__'

    def get_int(self, obj, field_name):
        field_value = getattr(obj, field_name)
        return int(field_value) if field_value != '' else None

    def get_intensity(self, obj):
        return self.get_int(obj, 'intensity')

    def get_impact(self, obj):
        return self.get_int(obj, 'impact')

    def get_likelihood(self, obj):
        return self.get_int(obj, 'likelihood')

    def get_relevance(self, obj):
        return self.get_int(obj, 'relevance')

    def get_end_year(self, obj):
        return self.get_int(obj, 'end_year')

    def get_start_year(self, obj):
        return self.get_int(obj, 'start_year')
