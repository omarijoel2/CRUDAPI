from rest_framework import viewsets
from .serializers import ProjectSerializer
from projects.models import Projects
import json
from django.core.exceptions import ObjectDoesNotExist


@api_view(["GET"])



def get_projects(viewsets.ModelViewSet):
    queryset= Projects.objects.all()
    serializer = ProjectSerializer(Projects, many=True)
    return JsonResponse({'Projects': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])


def add_project(request):

    try:

        Projects = Projects.objects.create(
                      ProjectRef='ProjectRef',
                      ProjectTitle='ProjectTitle',
                      Country='Country',
                      ImplementingOffice='ImplementingOffice',
                      DateFromGcf='DateFromGcf',
                      StartDate='StartDate',
                      EndDate='EndDate',
                      Disbursement='Disbursement',
                      GrantAmount='GrantAmount',
                      Status='Status',
        )
        serializer = ProjectSerializer(Projects)
        return JsonResponse({'Projects': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def getProjectByStatus(request):
        try:

            Projects = Projects.objects.filter(Status='Completed')
            serializer = ProjectSerializer(Projects)
            return JsonResponse({'Projects': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist as e:
            return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def getByCountry(request):
    try:

        Projects = Projects.objects.filter(Country='Kenya')
        serializer = ProjectSerializer(Projects)
        return JsonResponse({'Projects': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
