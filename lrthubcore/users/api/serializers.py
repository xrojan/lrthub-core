# Created by Joshua de Guzman on 09/07/2018
# @email code@jmdg.io

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from .. import models
from ..models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        validated_data['email'],
                                        validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name',)
        model = models.Gender


class EmploymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name',)
        model = models.EmploymentType


class NationalitySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name',)
        model = models.Nationality


class MaritalStatusSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name',)
        model = models.MaritalStatus


class DisabilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name',)
        model = models.Disabilities


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(source='user_id', many=False, read_only=True)
    gender = GenderSerializer(source='gender_id', many=False, read_only=True)
    nationality = NationalitySerializer(source='nationality_id', many=False, read_only=True)
    marital_status = MaritalStatusSerializer(source='marital_status_id', many=False, read_only=True)
    employment_status = EmploymentTypeSerializer(source='employment_status_id', many=False, read_only=True)
    disabilities = MaritalStatusSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = (
        'id', 'user_id', 'user', 'profile_image', 'mobile_no', 'birth_date', 'address', 'children_count', 'salary',
        'no_of_cars',
        'gender_id', 'gender', 'nationality_id', 'nationality', 'marital_status_id', 'marital_status',
        'employment_status_id', 'employment_status', 'disabilities')
