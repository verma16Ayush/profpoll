from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
# Create your views here.


@api_view(['GET'])
def api_overview(request):
    return Response('Soon')


@api_view(['GET'])
def prof_list(request):
    profs = Professor.objects.all().order_by('-rating')
    profs_serialized = ProfSerializer(profs, many=True)
    return Response(profs_serialized.data)

@api_view(['GET'])
def get_prof(request, pk):
    prof = Professor.objects.get(id=pk)
    prof_serialized = ProfSerializer(prof, many=False)
    return Response(prof_serialized.data)

@api_view(['GET'])
def prof_comment(request, pk):
    comments = Comment.objects.filter(prof=pk).order_by('-votes')
    comments_serialized = CommentSerializer(comments, many=True)
    return Response(comments_serialized.data)


@api_view(['POST'])
def post_rating(request, pk):
    return Response('Soon')


@api_view(['POST'])
def post_comment(request, pk):
    return Response('Soon')


@api_view(['POST'])
def edit_comment(request, pk):
    return Response('Soon')

@api_view(['DELETE'])
def delete_comment(request, pk):
    return Response('Soon')

@api_view(['POST'])
def upvote_comment(request, pk):
    return Response('Soon')