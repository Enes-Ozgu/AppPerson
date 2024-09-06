from django.contrib import admin

from .models import Person

@admin.register(Person)


class PersonAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone_number")

    list_display_links = ["first_name", "last_name", "phone_number" ]
    
    search_fields = ["first_name"]
    class Meta:
        model = Person