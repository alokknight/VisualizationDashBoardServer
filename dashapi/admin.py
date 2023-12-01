from django.contrib import admin
from .models import DataPoint
# Register your models here.

class DataPointAdmin(admin.ModelAdmin):
    list_display = ['end_year','intensity','sector','topic','insight','url','region',
    'start_year','impact','added','published','country','relevance',
    'pestle','source','likelihood']
    list_filter = ['end_year','intensity','sector','topic','region',
    'start_year','impact','added','published','country','relevance',
    'pestle','source','likelihood']
    search_fields = ['end_year','intensity','sector','insight','url','region',
    'start_year','impact','added','published','country','relevance',
    'pestle','source','likelihood']

admin.site.register(DataPoint, DataPointAdmin)