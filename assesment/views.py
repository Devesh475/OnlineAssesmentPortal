from re import template
from django.http.response import Http404, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect
from .models import *
from .forms import questionPaperForm, questionForm
from user.models import userprofile, questionPaperAttended

# Create your views here.
def home(request):
    return render(request, "home.html")

def addquestion(request):
    form = questionForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = questionForm()

    context = {'form':form}
    template_name = 'addquestion.html'
    return render(request, template_name, context)

def createexam(request):
    form = questionPaperForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')

    template_name = "createexam.html"
    context = {'form':form}
    return render(request, template_name, context)

def pendingexam(request):
    user = User.objects.get(id=request.user.id)
    exams = questionPaper.objects.all()
    examlst = []
    for x in exams:
        if user in x.users.all() and x.examOverStatus == False and user not in x.submittedby.all():
            examlst.append(x)
    context = {'exams':examlst}
    template_name = 'pendingexams.html'
    return render(request, template_name, context)

def attendexam(request, pk):
    paper = questionPaper.objects.get(id=pk)
    userP = userprofile.objects.get(user=request.user)
    if request.method == "POST":
        marks = 0
        q = paper.questionList.all()
        for x in q:
            if request.POST.get(x.Question) == x.answer:
                marks += x.marks
        
        p = questionPaperAttended()
        p.user = request.user
        p.quest = paper
        p.marksobtained = marks
        p.save()
        userP.questionPapersAttended.add(p)
        
        paper.submittedby.add(request.user)
        return redirect('/pendingexams')

    context = {'paper':paper}
    template_name = "attendpaper.html"
    return render(request, template_name, context)

def ongoingexam(request):
    exams = questionPaper.objects.filter(examOverStatus=False)
    template_name = "ongoingexams.html"
    context = {'exams':exams}
    return render(request, template_name, context)

def previousexam(request):
    examsbystud = userprofile.objects.get(user=request.user)
    lst = examsbystud.questionPapersAttended.all()
    template_name = "previousexams.html"
    context = {'examsbystud':lst}
    return render(request, template_name, context)

def finishexam(request, pk):
    qs = questionPaper.objects.get(id=pk)
    qs.examOverStatus = True
    qs.save()
    return redirect('/ongoingexams')

def allcompletedexams(request):
    qs = questionPaper.objects.filter(examOverStatus=True)
    lst = {}
    for q in qs:
        print(q.title)
        ex = questionPaperAttended.objects.filter(quest=q)
        # for x in ex:
        #     print(x.user, x.marksbotained)
        # newlst = []
        # for x in ex:
        #     print(x.user, x.marksobtained)
        lst[q] = ex

    print(lst)  
    # for x,y in lst:
    #     print(x,'\n')
    #     for z in y:
    #         print(z, '\n')
    template_name = "completed.html"
    context = {'lst':lst}
    return render(request, template_name, context)