from django.urls import path

from .views import EnrollmentCreateView, GetDataForStudent, PaidCoursesView

urlpatterns = [
   path('sendimage/' , EnrollmentCreateView.as_view()),
   path('studentinfo/' , GetDataForStudent.as_view()),
   path('studentcourse/' , PaidCoursesView.as_view()),
]