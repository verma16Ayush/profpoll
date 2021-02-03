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
    profs = Professor.objects.all()
    profs_slz = ProfSerializer(profs, many=True)
    return Response(profs_slz.data)

@api_view(['GET'])
def profs_by_dept(requst, dept):
    profs = Professor.objects.filter(dept=dept)
    profs_slz = ProfSerializer(profs, many=True)
    return Response(profs_slz.data)

@api_view(['GET'])
def prof_rating(request, pk):
    prof = Professor.objects.get(id=pk)
    prof_slz = ProfSerializer(prof, many=False)
    return Response(prof_slz.data)

@api_view(['GET'])
def prof_comments(request, pk):
    comment = Comment.objects.filter(prof=pk)
    comment_slz = CommentSerializer(comment, many=True)
    return Response(comment_slz.data)

