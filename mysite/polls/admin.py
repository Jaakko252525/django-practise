

from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.StackedInline):
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
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)














