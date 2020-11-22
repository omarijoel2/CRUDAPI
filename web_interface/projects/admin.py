from django.contrib import admin
from .models import Projects,Country, Office, Readiness

# Register your models here.
admin.site.register(Projects)

admin.site.register(Country)

admin.site.register(Office)
admin.site.register(Readiness)
