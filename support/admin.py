from django.contrib import admin
from .models import Faq,Answer
# Register your models here.

class CommentInline(admin.TabularInline):
    model = Answer
@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('category','author','subject','create_date','updated_at')
    inlines=[CommentInline]
    
#admin.site.register(Faq)
#admin.site.register(Question)
#admin.site.register(Answer)

