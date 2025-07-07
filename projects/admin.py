from django.contrib import admin
from .models import Project, Rating


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'average_rating', 'total_ratings', 'created_at')
    ordering = ('-average_rating',)
    search_fields = ('title',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Rating)