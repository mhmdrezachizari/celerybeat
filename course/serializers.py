from rest_framework import serializers
from persiantools.jdatetime import JalaliDate
from .models import Course
from teacher.models import Teacher
from students.models import Enrollment  # اضافه شده


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name_last', 'name_first']


class CourseSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True, read_only=True)
    date_start_jalali = serializers.SerializerMethodField()
    date_end_jalali = serializers.SerializerMethodField()
    course_link = serializers.SerializerMethodField()  # اضافه شد

    class Meta:
        model = Course
        fields = [
            'id', 'name', 'price',
            'date_start', 'date_start_jalali',
            'date_end', 'date_end_jalali',
            'teachers', 'image',
            'course_link'  # اضافه شد
        ]

    def get_date_start_jalali(self, obj):
        if obj.date_start:
            return JalaliDate(obj.date_start).strftime('%Y/%m/%d')
        return None

    def get_date_end_jalali(self, obj):
        if obj.date_end:
            return JalaliDate(obj.date_end).strftime('%Y/%m/%d')
        return None

    def get_course_link(self, obj):
        request = self.context.get('request')
        user = request.user if request else None

        if user is None or not user.is_authenticated:
            return None

        try:
            student = user.student
        except Exception:
            return None

        enrollment = Enrollment.objects.filter(student=student, course=obj, is_paid=True).first()
        if enrollment:
            return obj.course_link
        return None
