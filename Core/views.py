from django.shortcuts import render
from Core.logic.logic import build_home_context
from django.forms import BaseForm, modelform_factory, modelformset_factory
from Core.models import Employee

from django.views.generic import ListView, DetailView

from django.contrib.contenttypes.models import ContentType


# Create your views here.
def home(request, **kwargs):
    context = build_home_context({})

    return render(request, template_name='home/welcome.html', context=context)


class ModelListView(ListView):
    template_name = 'home/model_list.html'
    context_object_name = 'model_list'

    def get_queryset(self):
        model_class = ContentType.objects.get(model=self.kwargs['model'].lower()).model_class()

        print(model_class.objects.all())
        return model_class.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context = build_home_context(context)

        context['model'] = self.kwargs['model']
        context['model_fields'] = [field.name for field in ContentType.objects.get(
            model=self.kwargs['model'].lower()).model_class()._meta.fields]
        return context


def model_list(request, model, **kwargs):
    context = build_home_context({})
    context['model'] = model

    model_class = ContentType.objects.get(model=model.lower()).model_class()
    print(model_class)
    print(Employee)

    factory = modelformset_factory(model_class, fields='__all__', extra=0)
    formset = factory()

    context = {'formset_table': [form.as_table() for form in formset]}

    return render(request, template_name='home/model_list.html', context=context)


def model_detail(request, model, **kwargs):
    context = build_home_context({})
    context['model'] = model

    return render(request, template_name='home/model.html', context=context)


def model_add(request, model):

    print("mode", model)

    model_class = ContentType.objects.get(model=model.lower()).model_class()

    factoried_model = modelform_factory(model_class, fields='__all__')

    form = factoried_model()

    if request.method == "POST":
        form = factoried_model(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'home/model_add.html', {'form': form})

def graph(request):
    return render(request, 'home/graph.html')