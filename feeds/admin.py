from django.contrib import admin
from .models import PersonalInformation, About, Skill, Project, Contact

# Register your models here.


class PersonalInformationAdmin(admin.ModelAdmin):
    list_display = ('name_complete', 'address')
    search_fields = ["name_complete"]


admin.site.register(PersonalInformation, PersonalInformationAdmin)
admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Contact)
