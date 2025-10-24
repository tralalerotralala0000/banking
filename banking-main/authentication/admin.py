from django.contrib import admin
from.models import Country,Department, City, User

#Register your models here.

#admin.site.register(Country)
#admin.site.register(Department)
#admin.site.register(City)
#admin.site.register(User)

@admin.register(Country)
class CountrysAdmin(admin.ModelAdmin):
    display_data = ('name', 'abrev','get_status')

    def get_status(self, obj):
        return "Activate" if obj.status else "Inactive"
    get_status.short_description = 'Status' #Table label

