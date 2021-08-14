from tasks.models import Task
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields = ['id', 'username', 'email', ]


class TaskSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only = True)
    estimated_finish_time = serializers.DateTimeField(format="%d-%m-%Y %H:%M", input_formats=["%d-%m-%Y %H:%M"])
    created_datetime=serializers.DateTimeField(format="%d-%m-%Y %H:%M")

    class Meta:
        model = Task
        fields = ['id', 'creator', 'body', 'estimated_finish_time', 'created_datetime', 'is_completed', ]
        read_only_fields = ['created_datetime', 'is_completed',]