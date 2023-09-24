from django.contrib import admin
from .models import (
    Restaurant,
    Menu,
    MenuItem,
    Allergen,
)

admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(Allergen)
