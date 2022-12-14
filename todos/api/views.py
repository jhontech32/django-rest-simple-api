from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list',
        'Detail View': '/task-detail/<str:pk>',
        'Create': '/task-create',
        'Update': '/task-update/<str:pk>',
        'Delete': '/task-delete/<str:pk>'
    }

    return Response(api_urls)