from django.shortcuts import render
from rest_framework import generics,permissions,status
from .serializes import * 
from .models import * 
from rest_framework.exceptions import ValidationError 
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
# for validation + registration ,login
# -----------------------------------------------------
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# -----------------------------------------------------

# Create your views here.
from rest_framework.authtoken.models import Token

class PostList(generics.ListCreateAPIView):
    queryset =Post.objects.all()
    serializer_class = PostSerializer
    permission_classes =[permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self,serializer):
        serializer.save(poster = self.request.user)

class getPost(generics.RetrieveDestroyAPIView):
    queryset =Post.objects.all()
    serializer_class = PostSerializer
    permission_classes =[permissions.IsAuthenticatedOrReadOnly]

    def delete(self,request,*args,**kwargs):
        post = Post.objects.filter(pk = self.kwargs['pk'],poster = self.request.user)
        if post.exists():
            return self.destroy(request,*args,**kwargs)
        else:
            raise ValidationError("you are not authorized to delete this this post")

# queryset  serializer_class   permission_classes are predefined u cannot change them 

class CreateVote(generics.CreateAPIView):
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        post = Post.objects.get(pk = self.kwargs['pk'])
        return Vote.objects.filter(voter = user,post = post)
    
    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('you have already voted for this post')
        serializer.save(voter=self.request.user,post= Post.objects.get(pk=self.kwargs['pk']))



    def delete(self,request,*args,**kwargs):
        if self.get_queryset().exists():
                self.get_queryset().delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError("you haven't voted ")


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(username=data['username'],password = data['password'])
            user.save()
            token = Token.objects.create(user= user)
            return JsonResponse({'token':str(token)},status=200)
        except IntegrityError:
            return JsonResponse({'error':'username already exits'},status= 400)
@csrf_exempt
def login(request):
    if request.method == 'POST':
            data = JSONParser().parse(request)
            user = authenticate(username = data['username'],password = data['password'])
            if user is None:
                return JsonResponse({'error':'invalid credentials'},status=400)
            else:
                try:
                    token = Token.objects.get(user= user)
                except:
                    token = Token.objects.create(user = user)
                    return JsonResponse({'token':str(token)},status=200)

        

