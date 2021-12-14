from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Core.logic.logic import build_home_context
from django.forms import BaseForm, modelform_factory, modelformset_factory

from .decorators import unauthenticated_user, allowed_user

from django.views.generic import ListView

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from .models import Auctioned_item


# Here are main functions, representing the CRUD system. The main function item create represents the
# UC001 List an item, which means adding an item to the e-auction system and listing it for the users to see.

# CREATE
# @login_required(login_url='/accounts/login/')
def item_create(request, model):
    context = build_home_context({})
    context['model'] = model

    model_class = ContentType.objects.get(model=model.lower()).model_class()

    factoried_model = modelform_factory(model_class, fields='__all__')

    form = factoried_model()
    context['form'] = form

    if request.method == "POST":
        form = factoried_model(request.POST)
        if form.is_valid():
            form.save()

        return redirect('model_list', model=model)

    return render(request, template_name='home/model_add.html', context=context, )


# Deletion of the item is working fine, but it has no button on the frontend, item is deleted by the URL endpoint
def item_delete(request,object_id):
    instance = Auctioned_item.objects.get(id=object_id)
    instance.delete()

    return redirect('/')


def model_detail(request, model, **kwargs):
    context = build_home_context({})
    context['model'] = model

    return render(request, template_name='home/model.html', context=context)





# admin creation for general usage
def create_admin(request):
    admin_user = User.objects.create_superuser(
        username='admin',
        email='admin@gmail.com',
        password='admin',
    )

    return HttpResponse(f'Admin created')



# Home page
#@login_required(login_url='/accounts/login/')
def home(request, **kwargs):
    context = build_home_context({}) # this builds the context with classes we want to use in our app

    return render(request, template_name='home/welcome.html', context=context)

# This class specifies the models that can be added into our pages
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