from rest_framework import serializers
from .models import CategoryBlog, Blog


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryBlog
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    def create(self, validated_data):
        if 'category' in self.initial_data:
            validated_data['category_id'] = self.initial_data['category']
        obj = super(BlogSerializer, self).create(validated_data)
        return obj

    def update(self, instance, validated_data):
        instance = super(BlogSerializer, self).update(instance, validated_data)
        if 'category' in self.initial_data:
            instance.category_id = self.initial_data['category']

        return super(BlogSerializer, self).update(instance, validated_data)

    class Meta:
        model = Blog
        exclude = []

