from django.db import models
from django.contrib.auth.models import User

# Model for storing video URLs
class Video(models.Model):
    video_file = models.FileField(upload_to='videos/', default='') # URL field to store video URL
    title = models.CharField(max_length=255)  # Title of the video

    def __str__(self):
        return self.title

# Model for storing captcha questions and answers
class CaptchaQuestion(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)  # ForeignKey to associate with a video
    question = models.CharField(max_length=255)  # Question to display for the captcha
    answer = models.CharField(max_length=255)  # Correct answer for the captcha question

    def __str__(self):
        return f"{self.video.title} - {self.question}"
objects=models.Manager()