from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'interest', 'choice')
    search_fields = ('text',)

    # queryset 是默认的结果，search_term 是在后台搜索的关键词
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(QuestionAdmin, self).get_search_results(request, queryset, search_term)
        try:
            search_term_as_int = int(search_term)
            queryset |= self.model.objects.filter(age=search_term_as_int)
        except:
            pass
        return queryset, use_distinct


@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'category',
        'name',
        'subject_code',
    )
    list_per_page = 20


@admin.register(PsyCode)
class PsyCodeAdmin(admin.ModelAdmin):
    list_display = ('code',)
    search_fields = ('code',)


@admin.register(EducationLevel)
class EducationLevelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Recommend)
class RecommendAdmin(admin.ModelAdmin):
    # queryset 是默认的结果，search_term 是在后台搜索的关键词
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(RecommendAdmin, self).get_search_results(request, queryset, search_term)
        try:
            search_term_as_int = int(search_term)
            queryset |= self.model.objects.filter(age=search_term_as_int)
        except:
            pass
        return queryset, use_distinct

    def education_level(self, obj):
        return obj.education_level.name

    list_display = (
        'profession_code',
        'name',
        'core_course',
        'high_school_curriculum',
        'career_direction',
    )
    search_fields = (
        'profession_code',
        'name',
        'core_course',
        'high_school_curriculum',
        'career_direction',
    )
    list_per_page = 30
