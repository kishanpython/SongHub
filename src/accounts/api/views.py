from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView


from rest_framework.generics import (
	CreateAPIView,
	ListAPIView,
	)

from rest_framework.permissions import (
	AllowAny,
	IsAdminUser,
	IsAuthenticated,
	IsAuthenticatedOrReadOnly,
	)

from .serializers import UserCreateSL,UserNameSL


User = get_user_model()

class UserCreateAPIViews(CreateAPIView):
	serializer_class =  UserCreateSL
	queryset = User.objects.all()



# class UserLoginAPIViews(APIView):
# 	permission_classes = [AllowAny]
# 	serializer_class = UserLoginSL

# 	def post(self,request,*args,**kwargs):
# 		data = request.data
# 		#print(data)
# 		serializer = UserLoginSL(data=data)
		
# 		#print(new_data)
# 		if serializer.is_valid():
# 			print("hello")
# 			new_data = serializer.data
			
# 			return Response(new_data, status = HTTP_200_OK)
# 		return 	Response(serializer.errors, status = HTTP_400_BAD_REQUEST)


class UserNameGetterAPIView(ListAPIView):
	permission_classes = [AllowAny]
	serializer_class = UserNameSL

	def get_queryset(self, *args, **kwargs):
		queryset = User.objects.filter(username=self.request.user)
		return queryset


