from django.contrib import admin
from Calendar.models import EventLog, ApplicationUser, Comments, ImportEvents
# Register your models here.
admin.site.register(EventLog)
admin.site.register(ApplicationUser)
admin.site.register(Comments)
admin.site.register(ImportEvents)
