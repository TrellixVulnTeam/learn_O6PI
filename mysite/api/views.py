from datetime import datetime
import requests
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Snippet
from .models import Member, Card
from .serializers import UserSerializer, SnippetSerializer, MemberSerializer, CardSerializer

@csrf_exempt
@api_view(['GET', 'POST'])
def get_image(request, type):
    print(type)
    card = Card.objects.filter(type=type)
    serializer = CardSerializer(card, many=True)
    return Response(serializer.data)

@csrf_exempt
@api_view(['GET', 'POST'])
def member_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        member = Member.objects.all()
        serializer = MemberSerializer(member, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print("Post Request Call : ")
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            print("serializer is valid ")
            serializer.save()
            print("Model Save Succesfully !")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def member_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        member = Member.objects.get(pk=pk)
    except Member.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MemberSerializer(member)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MemberSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        print("******************Delete*******************")
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
def snippet_list_d(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
# @api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail_d(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MyRegisterView(View):
    template_name = 'member.html'
    form_class = MemberSerializer

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            print("Date Data :")
            data = {
                "name": form.cleaned_data["name"],
                "date": form.cleaned_data["date"].strftime("%d/%m/%Y"),
                "age": form.cleaned_data["age"],
                "mobile_no": form.cleaned_data["mobile_no"]
            }
            response = requests.post('http://127.0.0.1:8000/api/memberview', data=data)
            if response:
                form = self.form_class()
                return render(request, self.template_name, {'form': form, 'submit': 'Record Add '})

            else:
                print("Erro :", response.json())
                return render(request, self.template_name, {'form': form})
        else:
            return render(request, self.template_name, {'form': form})

def grid_view(request):
    return render(request, "grid.html")
