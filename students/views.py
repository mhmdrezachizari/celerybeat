from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Enrollment, Student
from .serializers import EnrollmentSerializer, StudentSerializer, CourseWithLinkSerializer
from course.models import Course
from rest_framework.generics import RetrieveAPIView
from rest_framework.exceptions import NotFound


class EnrollmentCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        try:
            student = Student.objects.get(student=request.user)
        except Student.DoesNotExist:
            return Response(
                {"detail": "Student profile not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        data = request.data.copy()
        data["student"] = student.id

        serializer = EnrollmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "detail": "Enrollment request submitted. Please wait for admin confirmation."
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetDataForStudent(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = StudentSerializer

    def get_object(self):
        try:
            return Student.objects.get(student=self.request.user)
        except Student.DoesNotExist:
            raise NotFound("Student not found")



class PaidCoursesView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # گرفتن Student مربوط به کاربر
        student = request.user.student
        print(request)
        # پیدا کردن دوره‌هایی که پرداخت شده‌اند
        enrollments = Enrollment.objects.filter(student=student, is_paid=True)
        courses = [en.course for en in enrollments]
        # Serialize
        serializer = CourseWithLinkSerializer(courses, many=True)
        return Response(serializer.data)