from django.shortcuts import render
#render=html을 보여주는 역할


def first_view(request):
    return render(request, 'index.html')