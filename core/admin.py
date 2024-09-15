from django.contrib import admin
from .models import TODO, Note, Profile, StudyMaterials

@admin.register(TODO)
class TODOAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'user', 'date', 'priority', 'due_date')
    search_fields = ('title', 'description')

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'modified_at')
    search_fields = ('title', 'content')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'image')
    search_fields = ('user__username',)

@admin.register(StudyMaterials)
class StudyMaterialsAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'date_posted', 'pdf_file')
    search_fields = ('title', 'subject')
    list_filter = ('subject',)