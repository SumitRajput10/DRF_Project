from rest_framework import serializers
from .models import Todo, TimingsTodo
import re
from django.template.defaultfilters import slugify

class TodoSerializer(serializers.ModelSerializer):

    # If we want key slug using (-) Example: My First / Answer: slug = My-First
    slug = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        # fields = '__all__'
        fields = ['uid', 'user', 'todo_title', 'slug', 'todo_description', 'is_done']
        # exclude = ['created_at', 'updated_at']

    def get_slug(self, obj):

        return slugify(obj.todo_title)

    # For validating specific fields
    def validate_todo_title(self, data):
        if data:
            todo_title = data
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

            if len(todo_title) < 5:
                raise serializers.ValidationError('Title should be at least 5 characters long')

            if not regex.search(todo_title) == None:
                raise serializers.ValidationError('Invalid title cannot contain special characters')

        return data

    # For validating all fields
    def validate(self, validated_data):

        if validated_data.get('todo_description'):
            todo_description = validated_data['todo_description']
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

            if len(todo_description) < 5:
                raise serializers.ValidationError('Descriptions should be at least 5 characters long')

            if not regex.search(todo_description) == None:
                raise serializers.ValidationError('Invalid description cannot contain special characters')

        return validated_data

class TimingTodoSerializer(serializers.ModelSerializer):
    todo = TodoSerializer() # For specific fields which you are already using in TodoSerializer
    class Meta:
        model = TimingsTodo
        exclude = ['created_at', 'updated_at']
        # depth = 1 # For showing foreign key data