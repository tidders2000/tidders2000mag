from django.shortcuts import render, reverse,get_object_or_404
from .models import Category,Advert
from .forms import advert_form
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView

@login_required()
def advert(request):
   
    
    if request.method=="POST":
          user=request.user
          advert = advert_form(request.POST, request.FILES)
          cat= request.POST.get('q')
          if advert.is_valid():
              ad=advert.save(commit=True)
              ad.user=user
              ad.category=cat
              ad.save()
              messages.error(request, "Advert Added")
              
              category = Category.objects.values('category_name').distinct()
              advertForm=advert_form()
              return render(request, "advert.html", {'advertForm':advertForm, 'category':category})
    
        
    else:  
        category = Category.objects.values('category_name').distinct()
        advertForm=advert_form()
        return render(request, "advert.html", {'advertForm':advertForm, 'category':category})

def SearchResultsView(request):
    
    query = request.GET.get('search')
    
    adverts = Advert.objects.filter(category__icontains=query)
    return render(request, 'search_results.html',{"adverts":adverts, 'query':query})
 
 
def advertview(request, id):
    
    business = Advert.objects.get(pk=id)
    id=id
   
    return render(request,'advert_view.html',{"business":business,"id":id})

def error(request):
    return render(request, 'error.html')