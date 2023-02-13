from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from . models import Branch,District
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# from  django.core.paginator import Paginator,EmptyPage,InvalidPage


# Create your views here.

def alldiscat(request,c_slug=None):
    c_page=None
    districts_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Branch,slug=c_slug)
        districts_list=District.objects.all().filter(branch=c_page,available=True)
    else:
        districts_list=District.objects.all().filter(available=True)
    paginator=Paginator(districts_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        districts=paginator.page(page)
    except (EmptyPage,InvalidPage):
        districts=paginator.page(paginator.num_pages)
    return render(request, 'branch.html', {'branch': c_page, 'districts': districts})
def pdtdetail(request,c_slug,district_slug):
    try:
        district=District.objects.get(branch__slug=c_slug,slug=district_slug)
    except Exception as e:
        raise e
    return render(request,'district.html',{'district':district})