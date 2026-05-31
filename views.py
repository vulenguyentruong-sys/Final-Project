from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Lesson, Question, Choice, Submission

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        # Logic chấm điểm sẽ được thực hiện ở đây
        # Sau khi submit, redirect sang trang kết quả
        return redirect('show_exam_result', course_id=course.id)
    return render(request, 'exam_template.html', {'course': course})

def show_exam_result(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    # Context giả định để pass bài, trong thực tế bạn sẽ lấy dữ liệu từ DB
    context = {
        'course': course,
        'score': 85,
        'passed': True,
        'message': 'Congratulations! You have passed the exam.'
    }
    return render(request, 'exam_result.html', context)
