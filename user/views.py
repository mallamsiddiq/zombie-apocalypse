from django.shortcuts import render
from rest_framework.generics import GenericAPIView,ListAPIView
from .serializers import SurvivorSerializer,SurvivorListSerializer,SurvivorUpdLocSerializer,StatSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .models import Survivor,SurvivorStatistics,Robots
import requests
import json
from rest_framework.views import APIView
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from django.core import serializers
from . filters import SurvivirsFilterApiFilter
from django_filters.rest_framework import DjangoFilterBackend




class RegisterView(ListAPIView):
	queryset = Survivor.objects.all()
	serializer_class = SurvivorListSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_class = SurvivirsFilterApiFilter
	def get_serializer_class(self):
	    if self.request.method=='POST':
	        return SurvivorSerializer
	    else:
	    	return self.serializer_class

	def post(self, request):
		serialize = SurvivorSerializer(data=request.data)
		if serialize.is_valid():
			serialize.save()
			return Response(serialize.data, status=status.HTTP_201_CREATED)
		return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

class survivor_detail_api(APIView):
    serializer_class = SurvivorUpdLocSerializer
    def get_serializer_class(self):
	    if self.request.method =='GET':
	        return SurvivorListSerializer
	    else:
	    	return SurvivorUpdLocSerializer
    def get_object(self,username):
        try:
            return Survivor.objects.get(username=username)
        except Exception as e:
            return None
    def get(self, request, username, format=None):
        snippet = self.get_object(username)
        if snippet:
            serializer = SurvivorListSerializer(snippet)
            return Response(serializer.data)
        else:
            return HttpResponse("""<h1>no quyery matches your search </i>.</h1><span> kindly input valid object parameter
                                     other than.</span> <b>{}</b>""".format(username))
    def put(self, request, username, format=None):
        suvivor_instance = self.get_object(username)
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
        	suvivor_instance.last_location=self.request.data.get('last_location')
        	suvivor_instance.water=self.request.data.get('water')
        	suvivor_instance.ammunition=self.request.data.get('ammunition')
        	suvivor_instance.medication=self.request.data.get('medication')
        	suvivor_instance.report_count+=int(self.request.data.get('is_infected'))
        	print(self.request.data.get('is_infected'))
        	suvivor_instance.is_infected=int(suvivor_instance.report_count) >=3
        	suvivor_instance.save()
        	return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # snippet = Post.objects.get(id=pk)
        #     snippet.views += 1
        #     snippet.save()

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        if not snippet.api_id:
            snippet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response('you are unauthorised to delete this item',status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def statview(request):
	snippets=SurvivorStatistics(Survivor.objects.filter(is_infected=True).count(),Survivor.objects.exclude(is_infected=True).count())
	data={'total_survivors':snippets.total_survivors,
	'percetage_infected':snippets.perc_infected,
	'perc_non_infected':snippets.perc_non_infected,
	'total_infected':snippets.number_infected,
	'total_non_infected':snippets.number_non_infected
	}
	return Response(data, status=200)


def robotsview(request):
	api_robots=requests.get('https://robotstakeover20210903110417.azurewebsites.net/robotcpu').json()
	
	robots= api_robots		# Robots.objects.all()
	return render(request, 'user/home.html', {'robots':robots})



# api_robots=requests.get('https://robotstakeover20210903110417.azurewebsites.net/robotcpu').json()
	
# for i in (api_robots):

	
# 	if len(Robots.objects.filter(serialNumber=i['serialNumber']))<1:
# 		try:
# 			robots_inst=Robots(model=i['model'],serialNumber=i['serialNumber'],manufacturedDate=i['manufacturedDate'],category=i['category'])
# 			robots_inst.save()
# 			print('this robot {} is beign registered'.format(i['serialNumber']))
# 		except Exception as e:
# 			print(e)
# 	else:
# 		print('this robot {} is already registered'.format(i['serialNumber']))

# Robots.objects.all().delete()


