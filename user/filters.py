import django_filters
from .models import Survivor
from django_filters import rest_framework as drf_filters

class SurvivirsFilterApiFilter(drf_filters.FilterSet):
    class Meta:
        model = Survivor
        fields = ['is_infected']

