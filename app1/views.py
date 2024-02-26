from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
from .models import Score

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        score, created = Score.objects.get_or_create(user=request.user)
        points = score.points
    else:
        points = '로그인이 필요합니다.'  # 사용자가 로그인하지 않았을 경우의 메시지

    return render(request, 'index.html', {'points': points})

@login_required
def add_score(request):
    score, created = Score.objects.get_or_create(user=request.user)
    score.points += 5
    score.save()
    return redirect('app1:index')  # 점수 추가 후 리다이렉트할 페이지의 이름