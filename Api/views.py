from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import StudentDetail
from .serializer import StudentDetailSerializer,DummySerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
# Create your views here.

'''we learn APIVIEWS, CreateAPIView,GenericView'''

# ListAPIViw for get request
class StudentDetailsPagination(LimitOffsetPagination):
	default_limit = 2
	max_limit = 6



class StudentDetails(generics.ListAPIView):
	# accept the query set
	queryset = StudentDetail.objects.all()
	# serializer class
	serializer_class = StudentDetailSerializer
	#add filter to this page
	filter_backends = (DjangoFilterBackend,SearchFilter)
	#add filter fields
	filter_fields = ('id','name')
	#add pagination
	pagination_class = StudentDetailsPagination




# post request APIView
class ShowDetails(APIView):
	def post(self,request):
		try:
			serializer = StudentDetailSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data,status=status.HTTP_200_OK)
			else:
				return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
		except Exception as e:
			return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




# create api view
class AddMoreDetails(generics.CreateAPIView):
	serializer_class = StudentDetailSerializer

	def create(self,request,*args,**kwargs):
		try:
			name = request.data.get('name',None)
			stream = request.data.get('stream',None)
			year = request.data.get('year',None)
			project = request.data.get('project',None)
			email = request.data.get('email',None)
			phone = request.data.get('phone',None)	
			return super().create(request,*args,**kwargs)
		except Exception as e:
			return Response({"MESSAGE":"YOU FAIL"})



#we use RetrieveUpdateDestroyAPIView to update and delete the data

class StudentDetailsRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
	queryset = StudentDetail.objects.all()
	lookup_field = 'id'
	serializer_class = StudentDetailSerializer
	def delete(self,request,*args,**kwargs):
		try:
			id = request.data.get('id',None)
			response = super().delete(request,*args,**kwargs)
			if response.status_code == 204:
				from django.core.cache import cache
				cache.delete(id)
				return response
		except Exception as e:
			return Response({'MESSAGE':'YOU FAIL'})
	def update(self,request,*args,**kwargs):
		response = super().update(request,*args,**kwargs)
		if response.status_code == 200:
			mydata = request.data
			from django.core.cache import cache
			cache.set(f"{mydata.get('id',None)}",{
				'name':mydata['name'],
				'stream':mydata['stream'],
				'year':mydata['year'],
				'project':mydata['project'],
				'email':mydata['email'],
				'phone':mydata['phone']
				})
			return response

#generic view is used to display the static data

class StaticView(generics.GenericAPIView):
	serializer_class = DummySerializer
	def get(self,request):
		message = {'data':'this is generic view'}

		serializer = DummySerializer({'data':message})
		return Response(serializer.data)

