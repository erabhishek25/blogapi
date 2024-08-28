from rest_framework import serializers


from .models import Post, Comment, Category, Tag
from account.models import User

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['id', 'name']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'content']


class PostSerialzier(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    category = CategorySerializer(many=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'status', 'category', 'tags', 'created', 'comments']
        read_only_fields = ['author']

    def get_comments(self, obj):
        comments = obj.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return serializer.data 


    def create(self, validated_data):
        print(validated_data)
        categories = validated_data.pop('category')
        tags = validated_data.pop('tags')
        post = Post.objects.create(**validated_data)

        # to handle category data if not presernt in db, create
        for category in categories:
            obj, created = Category.objects.get_or_create(**category)
            post.category.add(obj)
        
        # to handle tags data if not preset in db, create
        for tag in tags:
            print(tag)
            obj, created = Tag.objects.get_or_create(**tag)
            post.tags.add(obj)
        
        return post

       

    def update(self, instance, validated_data):
        
        categories_data = validated_data.pop('category')
        tags_data = validated_data.pop('tags')

        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        #clear all the category
        instance.category.clear()
        for category in categories_data:
            obj, created = Category.objects.get_or_create(**category)
            instance.category.add(obj)
        
        # clear all the previous tags
        instance.tags.clear()
        for tag in tags_data:
            obj, created = Tag.objects.get_or_create(**tag)
            instance.tags.add(obj)
        
        return instance

    def validate(self, data):
        return data
