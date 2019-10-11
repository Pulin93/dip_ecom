from django.shortcuts import render
from .models import FeedbackData
from .forms import FeedbackFrom
from django.http.response import HttpResponse
import datetime
date = datetime.datetime.now()

def main_page(request):
    return render(request,'base.html')

def home_page(request):
    return render(request,'home_page.html')

def contact_page(request):
    return render(request,'contact_page.html')

def courses_page(request):
    return render(request,'courses_page.html')

def feedback_page(request):
    if request.method=="POST":
        fform = FeedbackFrom(request.POST)
        if fform.is_valid():
            name = request.POST.get('name')
            rating = request.POST.get('rating')
            feedback = request.POST.get('feedback')
            data = FeedbackData(
                name=name,
                rating=rating,
                feedback=feedback,

            )
            data.save()
            fform=FeedbackFrom()
            fdata = FeedbackData.objects.all()
            return render(request,'feedback_page.html',{'fform':fform,'fdata':fdata})
        else:
            return HttpResponse("Invalid Form")


    else:
        fform=FeedbackFrom()
        fdata = FeedbackData.objects.all()
        return render(request,'feedback_page.html',{'fform':fform,'fdata':fdata})

def team_page(request):
    return render(request,'team_page.html')

def gellery_page(request):
    return render(request,'gellery_page.html')

def git_repo(request):
    pass
