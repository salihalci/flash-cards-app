from django.contrib import admin
from .models import Question

class CardApp(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Question, CardApp)