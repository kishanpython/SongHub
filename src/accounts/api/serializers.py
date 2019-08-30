from rest_framework.serializers import (
	CharField,
	ModelSerializer,
	ValidationError,
	)


from django.contrib.auth import get_user_model
from accounts.models import Accounts
User  = get_user_model()

class UserCreateSL(ModelSerializer):
	conf_password = CharField(label="Confirm password")
	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'password',
			'conf_password',
		]
		extra_kwargs = {"password":{"write_only":True}}

	def validate(self, data):
		username = data['username']
		user_chk = User.objects.filter(username = username)
		if user_chk.exists():
			raise ValidationError("User Already register with this username")
		return data	


	def validate_conf_password(self, value):
		data = self.get_initial()
		password = data.get("password")
		conf_password  = data.get("conf_password")
		if password != conf_password:
			raise ValidationError("Password and Confirm Password Not match")
		return value	



	def create(self, validated_data):
		username = validated_data['username']
		email = validated_data['email']
		password = validated_data['password']
		user_obj = User(
				username = username,
				password = password,
			)
		user_obj.set_password(password)
		user_obj.save()
		return validated_data


class UserNameSL(ModelSerializer):
	#token = CharField(allow_blank=True,read_only=True)
	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'password',
			
		]
		extra_kwargs = {"password":{"write_only":True}}

