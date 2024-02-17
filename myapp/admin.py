from django.contrib import admin

from myapp import models

# Register your models here.
admin.site.register(models.Cliente)
admin.site.register(models.Inmobile)

admin.site.register(models.InmobileImage)
admin.site.register(models.RegisterLocations)



