
from .serializers import ProjectSerializer
from projects.models import Projects
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist







@api_view(['GET'])
def ProjectList(request):
    projdata = Projects.objects.all()
    serializer =  ProjectSerializer(projdata, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def ProjectCreate(request):
    serializer = ProjectSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['GET'])
def ProjectByStatus(request):
        proj_info = Projects.objects.filter(Status='Completed')
        serializer = ProjectSerializer(proj_info, many=True)
        return Response(serializer.data)
@api_view(['GET'])
def ByCountry(request):
    ken_pro = Projects.objects.filter(Country=4)
    serializer = ProjectSerializer(ken_pro, many=True)
    return Response(serializer.data)
