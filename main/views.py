# views.py
from django.shortcuts import render, redirect
from .models import Comment, Profile

def home(request):
    comments = Comment.objects.all().order_by('-created_at')
    profile = Profile.objects.first()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment_text = request.POST.get('comment')
        if name and email and comment_text:
            Comment.objects.create(name=name, email=email, comment=comment_text)
            return redirect('home')

    return render(request, 'main/home.html', {
        'comments': comments,
        'profile': profile
    })

from django.http import JsonResponse
from .models import Comment  # Your Comment model

def submit_comment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment_text = request.POST.get('comment')

        comment = Comment.objects.create(
            name=name,
            email=email,
            comment=comment_text
        )

        return JsonResponse({
            'success': True,
            'name': comment.name,
            'comment': comment.comment,
            'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M')
        })
    return JsonResponse({'success': False}, status=400)
