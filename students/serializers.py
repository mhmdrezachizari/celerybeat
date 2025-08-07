from rest_framework import serializers
from .models import Enrollment, Student
from course.models import Course

class CourseWithLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'course_link']



class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = [
            "id",
            "student",
            "course",
            "is_paid",
            "registered_at",
            "receipt_image",
        ]
        read_only_fields = ["is_paid", "registered_at"]


class StudentSerializer(serializers.ModelSerializer):
    student = serializers.CharField(source='student.phone_number', read_only=True)
    class Meta:
        model = Student
        fields = "__all__"
