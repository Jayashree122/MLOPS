from rest_framework import serializers
from .models import React

class UserInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['id', 'Overall_rank', 'Score', 'Social_support', 'Healthy_life_expectancy', 'Freedom_to_make_life_choices', 'Generosity', 'Perceptions_of_corruption']
