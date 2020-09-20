from django.contrib import admin
from .models import *

admin.site.register(StandardUser)
admin.site.register(University)
admin.site.register(City)
admin.site.register(Address)
admin.site.register(Subject)
admin.site.register(Discipline)
admin.site.register(Question)
admin.site.register(Book)
# admin.site.register(UserPermition)