from django.urls import path
from . import views

urlpatterns = [
    # Các URL khác của bạn...
    path('<int:course_id>/submit/', views.submit, name='submit'),
    path('<int:course_id>/exam_result/', views.show_exam_result, name='show_exam_result'),
]
