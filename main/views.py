from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    #로그인한 사용자 정보
    user = request.user

    #관리자 여부 확인
    context = {
        'username': user.username,
        'is_staff': user.is_staff,
        'is_superuser': user.is_superuser,
    }

    return render(request, 'main/home.html', context)