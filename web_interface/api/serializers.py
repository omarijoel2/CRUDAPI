from rest_framework import serializers
from projects.models import Projects

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['ProjectRef',
                  'ProjectTitle',
                  'Country',
                  'ImplementingOffice',
                  'DateFromGcf',
                  'StartDate',
                  'EndDate',
                  'Disbursement',
                  'GrantAmount',
                  'Status',
                  ]
