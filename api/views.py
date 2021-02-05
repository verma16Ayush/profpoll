from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import *
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from django.contrib.auth import login, logout, authenticate
# Create your views here.


@api_view(['GET'])
@permission_classes([AllowAny])
def api_overview(request):
    data = {
        'api/':'api end-points overview',
        'api/list/':'list all professors',
        'api/list_dept/<str:dept>/':'list all professors of dept department',
        'rate_prof/<str:pk>/':'rate professor with pk primary key',
        'prof_id/<str:pk>/':'get a professor\'s data, including ratings but not comments',
        'prof_comment_id/<str:pk>/':'get comments on a professor',
        'review/<str:pk>/':'write a review/comment for a professor',
        'register/':'register a new user',
        'login_user/':'login an existing user',
        'logout_user/':'log out an already logged-in user'
    }
    return Response(data=data)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_prof_list(request):
    profs = Professor.objects.all()
    profs_slz = ProfSerializer(profs, many=True)
    return Response(profs_slz.data)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_prof_list_by_dept(request, dept):
    profs = Professor.objects.filter(dept=dept)
    profs_slz = ProfSerializer(profs, many=True)
    return Response(profs_slz.data)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_prof_id(request, pk):
    prof = Professor.objects.get(id=pk)
    prof_slz = ProfSerializer(prof, many=False)
    return Response(prof_slz.data)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_prof_comments(request, pk):
    comments = Comment.objects.filter(prof=pk)
    comments_slz = CommentSerializer(comments, many=True)
    return Response(comments_slz.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_prof(request, pk):
    serializer = CommentSerializer()
    if(request.method == 'POST'):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def rate_prof(request, pk):
    serializer = RatingSerializer()
    if request.method == 'POST':
        if Ratings.objects.get(user_id=request.user.id) is not None:
            data = {
                'details':'User has already rated this professor'
            }
            return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

        request.data['user_id'] = request.user.id
        request.data['prof_id'] = pk
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def register(request):
    if request.user.is_authenticated:
        return Response(status=status.HTTP_307_TEMPORARY_REDIRECT)
    serializer = UserSerializer()
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_user(request):
    if request.user.is_authenticated:
        return Response(status=status.HTTP_307_TEMPORARY_REDIRECT)
    username = request.data['username']
    password = request.data['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    


