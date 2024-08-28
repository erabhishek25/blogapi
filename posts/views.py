from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


from .models import Post, Comment 
from .serializers import PostSerialzier, CommentSerializer



class PostApi(viewsets.ViewSet):

    def list(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerialzier(posts, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = PostSerialzier(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def retrieve(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerialzier(post)
        return Response(serializer.data)
    
    def update(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerialzier(instance=post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def destroy(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response({'message': "Resource deleted successfully"})

    @action(detail=True, methods=['POST'])
    def add_comment(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post, author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)
    
    @action(detail=True, methods=['POST'])
    def publish(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.status = 'publish'
        post.save() 
        return Response({'message': 'Post published'})
    
    @action(detail=True, methods=['POST'])
    def pending(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.status = 'pending'
        post.save()
        return Response({'message': 'Post status Pending'})
    


