from django.db import models

from teacher.models import Teacher


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    date_start = models.DateField()
    date_end = models.DateField()
    teachers = models.ManyToManyField(Teacher)
    image = models.ImageField(upload_to='course/images')
    course_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "کلاس ها"
