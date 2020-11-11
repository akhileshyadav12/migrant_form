from django.db.models import Count
from django.views import generic
from django.views.generic import CreateView, UpdateView
from django.shortcuts import get_object_or_404, render
from .forms import PersonForm
from .models import  Person


class IndexView(generic.ListView):
    template_name = 'registration/index.html'
    context_object_name = 'latest_person_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Person.objects.order_by('-name')[:5]


class DetailView(generic.DetailView):
    model = Person

  
    #template_name = 'registration/detail.html'



def index(request):
    latest_question_list = Person.objects#.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'registration/index.html', context)





def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'registration/results.html', {'question': question})

def data(request):
    person=Person.objects.all()
    a=person.values('job','home').annotate(dcount=Count('job'))
    return render(request,'registration/data.html',{"data":a,"error":"message"})





class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm#('name', 'email', 'job_title', 'bio')
    template_name='registration/person_form.html'
    success_url='/'
    
class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'registration/person_form.html'
   