from djpwb.pwb.models import Poll
from djpwb.pwb.models import Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

    
class PollAdmin(admin.ModelAdmin):
    #fields = ('question','publication_date')
    fieldsets = [ 
		 ('Question',	{'fields': ['question']}),
		 ('Date Information',	{'fields': ['publication_date'], 'classes': ['collapse']}),
		]
    inlines = [ChoiceInline]
    list_filter = ['publication_date']
    list_display = ['question','publication_date']
    search_fields = ['question'] 		

admin.site.register(Poll, PollAdmin)




