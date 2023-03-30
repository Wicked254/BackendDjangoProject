from rest_framework import serializers
from .models import Question, Answer
//defining serializer for question model
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
//defining serializer for answers model
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
class QuestionSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'body', 'username', 'created_at', 'updated_at']
//to know specific users
class AnswerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Answer
        fields = ['id', 'question', 'body', 'username', 'created_at', 'updated_at']
