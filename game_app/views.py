from django.shortcuts import render, get_object_or_404
from .models import Quiz, Question, Answer
# Create your views here.

def play_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = Question.objects.filter(quiz=quiz)

    if request.method == 'POST':
        score = 0
        for question in questions:
            selected_answers_id = request.POST.get(f'question_{question.id}')
            if selected_answers_id:
                selected_answers = Answer.objects.get(pk=selected_answers_id)
                if selected_answers.is_correct:
                    score += 1
        return render(request, 'game_app/result.html', {'score': score, 'total_questions': len(questions)})
    
    return render(request, 'game_app/play_quiz.html', {'quiz': quiz, 'questions': questions}
                  )