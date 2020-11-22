from django import forms
from projects.models import Projects
from django_countries.fields import CountryField
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = "__all__"

        OPTIONS = (
                ("UnderImplementation","Under Implementation"),("Completed","Completed"),
                )
        Status = forms.ChoiceField(required=True, choices=OPTIONS)

        Readiness=(("NationalAdaptationPlans","NationalAdaptationPlans"),("Readiness","Readiness"),)
        States = forms.ChoiceField(required=True, choices=Readiness)
        country = CountryField().formfield()
