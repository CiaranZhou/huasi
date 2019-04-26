from django.db import models


# Create your models here.
class Interest(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=10, verbose_name="兴趣类型")


class Question(models.Model):
    def __str__(self):
        return self.text

    text = models.CharField(max_length=100, verbose_name="题目")
    choice = models.BooleanField(verbose_name="选项")
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)


class Category(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=5, verbose_name="学科门类")


class SubCategory(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=15, verbose_name="子类")
    subject_code = models.CharField(max_length=5, verbose_name="学科代码")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class PsyCode(models.Model):
    def __str__(self):
        return self.code

    code = models.CharField(max_length=3, verbose_name="心理代码")


class EducationLevel(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=3, verbose_name="学历层次")


class Recommend(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=15, verbose_name="专业名称")
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True)
    profession_code = models.CharField(max_length=10, verbose_name="专业代码")
    psy_code = models.ManyToManyField(PsyCode, blank=True)
    education_level = models.ManyToManyField(EducationLevel, verbose_name="学历层次", blank=True)
    core_course = models.CharField(max_length=300, verbose_name="专业核心课程")
    high_school_curriculum = models.CharField(max_length=30, verbose_name="对应高中课程")
    career_direction = models.CharField(max_length=350, verbose_name="对应职业方向")
