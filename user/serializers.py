from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Survivor,SurvivorStatistics


infected_CHOICES =( 
        	(0, "not infected"),
        	(1, "infected")
        	)
class SurvivorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survivor

        #fields=('name','age','gender','username','last_location')
        exclude = ('report_count','date_created', )
        # fields = ('__all__')

class SurvivorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survivor

        fields = ('__all__')

class SurvivorUpdLocSerializer(serializers.ModelSerializer):
	is_infected =serializers.ChoiceField(choices = infected_CHOICES)
	class Meta:
		model = Survivor

		fields = ('last_location','water','ammunition','medication','is_infected')


class StatSerializer(serializers.Serializer):
	total_survivors = serializers.FloatField()
	number_infected = serializers.FloatField()
	number_non_infected = serializers.FloatField()
	perc_infected = serializers.FloatField()
	perc_non_infected = serializers.FloatField()
































    # def validate(self, attrs):
    #     email = attrs.get('email', '')
    #     if Survivor.objects.filter(email=email).exists():
    #         raise serializers.ValidationError(
    #             {'email': ('Email is already in use')})
    #     return super().validate(attrs)
