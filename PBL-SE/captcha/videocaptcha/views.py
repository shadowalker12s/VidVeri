from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate,login
from .users import RegisteredUser
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Video, CaptchaQuestion
import random

def play_video(request):
    # Retrieve a random video from the database
    video = Video.objects.order_by('?').first()
    questions = CaptchaQuestion.objects.filter(video=video)
    context = {
        'video': video,
        'questions': questions
    }
    return render(request, 'videocaptcha/play_video.html', context)

def verify_captcha(request):
    if request.method == 'POST':
        video_id = request.POST.get('video_id')
        answers = request.POST.getlist('answers[]')
        # Fetch questions and answers from the database
        questions = CaptchaQuestion.objects.filter(video_id=video_id)
        correct_answers = [question.answer for question in questions]
        # Verify answers
        if answers == correct_answers:
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})
    return JsonResponse({'error': 'Invalid request method'})
def captcha_view(request):
    random_video = random.choice(Video.objects.all())

    # Get the questions related to the random video
    questions = CaptchaQuestion.objects.filter(video=random_video)

    context = {
        'random_video': random_video,
        'questions': questions,
    }
    return render(request, 'videocaptcha/captcha.html',context)
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user=User.objects.get(email=email)
        except:
            print("Username does not exist")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('captcha')  # Redirect to a protected page after successful login
        else:
            # Authentication failed
            return render(request, 'videocaptcha/login.html', {'error': 'Invalid email or password'})
    else:
        return render(request, 'videocaptcha/login.html')
    
def register_view(request):
     return render(request, 'videocaptcha/register.html')