

from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
        ("siuu", {"fields": ["siuu"]}),
        ("hmmmm", {"fields": ["testi"]}),
        ("greating", {"fields": ["greating"]})

    ]
    list_display = ["question_text","testi", "siuu", "pub_date"]
    inlines = [ChoiceInline]
    list_filter = ["question_text","testi", "siuu", "pub_date"]
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)














