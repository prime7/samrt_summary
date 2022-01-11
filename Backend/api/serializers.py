from rest_framework import serializers
from api.models import Summary, RATING_CHOICES
from api.algorithm import run
from django.shortcuts import get_object_or_404


class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = '__all__'
    
    def validate(self, attrs):
        if 'src_link' in attrs or 'content' in attrs:
            return attrs
        raise serializers.ValidationError('Atleast one of the field between src_link or content is needed')

    def create(self, validated_data):
        summary = Summary.objects.create(**validated_data)
        if 'src_link' in validated_data:
            summary.summary = run(validated_data['src_link'],None)
        elif 'content' in validated_data:
            summary.summary = run(None,validated_data['content'])
        return summary


class RateSummarySerializer(serializers.Serializer):
    summary_id = serializers.CharField()
    rate = serializers.IntegerField()