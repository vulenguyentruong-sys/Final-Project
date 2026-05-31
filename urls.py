from django.urls import path
from . import views

app_name = 'onlinecourse' # Thay bằng tên app của bạn nếu khác

urlpatterns = [
    # ... Các đường dẫn khác của bạn (như route, lesson, v.v.) ...
    
    # Đảm bảo 2 dòng dưới đây được viết chính xác từng chữ:
    path('<int:course_id>/submit/', views.submit, name='submit'),
    path('<int:course_id>/exam_result/', views.show_exam_result, name='show_exam_result'),
]
