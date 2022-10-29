from django.shortcuts import render
from django.shortcuts import get_object_or_404,redirect
from django.urls import reverse



from .models import *
from .forms import SubmissionForm

def index(request):
    context ={'Status':'working'}
    return render(request, "index.html", context)

def homepage(request):
    users = User.objects.filter(participant = True)
    events = Event.objects.all()
    context = {'users':users , 'events':events}
    return render(request, "homepage.html" , context)   

def eventpage(request, pk):
    event =  get_object_or_404(Event , pk=pk)
    # we want to know if the user is registered or not
    registered = False
    myevents = Event.objects.filter(participants = request.user.id)
    if event in myevents:
        registered = True
    # registered= request.user.events.filter(id=event.id).exists() #better check if anon user breaks
    
    context = {'event':event , 'registered':registered}
    return render(request, "event.html",context)


def registration_confirmation(request, pk):
    event =  get_object_or_404(Event , pk=pk)
    context = {'event':event}
    if request.method == 'POST':
        event.participants.add(request.user)
        return redirect(reverse('event_page', pk = event.pk))
    return render(request, "event_confirmation.html", context)

def profile(request, pk):
    user = get_object_or_404(User , pk=pk)
    context = {'user': user}
    return render(request, "profile.html", context)


def account(request):
    user = request.user
    # participated_in = Event.objects.filter(participants = user.id)
    # + many = True
    #   added related name to Event model and modified template {% for event in user.events.all %} =)
    context = {'user': user}
    return render(request, "account.html", context)

def project_submission(request,pk):
    event = get_object_or_404(Event, pk=pk)
    form = SubmissionForm()
    
    if request.method == 'POST':
        form = SubmissionForm(request.POST) #initial={'event':event, 'participant':request.user} dosnt get sent to server =(
        if form.is_valid():
            submission = form.save(commit=False)
            submission.participant=request.user
            submission.event=event
            form.save()
            return redirect('account')
    context = {'event': event, 'form': form}
    return render(request, "submit_form.html", context)    