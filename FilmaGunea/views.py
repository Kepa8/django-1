from typing import Any
from django import http
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template import loader
from django.shortcuts import render, redirect  
from django.db import models
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.contrib import messages
##from .forms import CustomUserCreationForm  


def hasiera(request):
    if request.user.is_authenticated:
            erab = request.user
            context = {'user': erab.username}
    else:
            nouser = "Ez zaude logeatuta"
            context = {'user': nouser}
    return render(request, 'FilmaGunea/hasiera.html',context)


def sartuta(request):
    erab = request.user
    context = {'user': erab.username}
    return render(request, 'FilmaGunea/sartuta.html', context)

class LoginForm(LoginView):
    template_name = 'FilmaGunea/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('sartuta')  
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Saioa Hasi'
        return context

def register(request):   
    if request.method == 'POST':  
        form = UserCreationForm(request.POST)  ##ez bada jartzen request.POST ez da gordetzen
        if form.is_valid():  
            form.save()
            return redirect('login')
    
    else:  
        form = UserCreationForm()  
    context = {  
        'form':form  
    }  
    return render(request, 'FilmaGunea/register.html', context)   

from .models import filmak_filma

def datuBase(request):
    f1 = filmak_filma(izenburua="Earthlings", zuzendaria="Shaun Monson", urtea="2005", generoa="DO", sipnosia="Using hidden cameras and never-before-seen footage, Earthlings chronicles the day-to-day practices of the largest industries in the world, all of which rely entirely on animals for profit.", bozkak="0")
    f2 = filmak_filma(izenburua="The Herd", zuzendaria="Melanie Light", urtea="2014", generoa="TH", sipnosia="Imprisoned within inhuman squalor with other women. Paula's existence and human function is abused as a resource by her captors. Escape, on any level, is hopeless as the women are condemned to a life of enforced servitude at the whims of their imprisoners for one reason only - their milk.", bozkak="0")
    f3 = filmak_filma(izenburua="Dominion", zuzendaria="Chris Delforce", urtea="2018", generoa="DO", sipnosia="Dominion uses drones, hidden and handheld cameras to expose the dark underbelly of modern animal agriculture, questioning the morality and validity of humankind's dominion over the animal kingdom. ", bozkak="0")
    f4 = filmak_filma(izenburua="Matadero: lo que la industria cárnica esconde", zuzendaria="Aitor Garmendia", urtea="2017", generoa="DO", sipnosia="El trabajo que se presenta a continuación tiene como objetivo hacer visible la explotación y violencia sistemática que padecen los animales en mataderos, la cual es mantenida oculta de forma deliberada por la industria cárnica. Con esta investigación se aporta información relevante al actual debate social y político antiespecista promovido por el movimiento de derechos animales que exige la abolición de toda explotación animal. ", bozkak="0")
    f5 = filmak_filma(izenburua="Gurean: animalien erabilera Euskal Herriko festetan", zuzendaria="LinasKorta", urtea="2018", generoa="DO", sipnosia="Askekintzak Euskal Herriko festetako animalien erabileraren inguruan inoiz egin den dokumentazio lan handiena bildu du. Gurean, 4 urteetan zehar (2014-2017) aktibista desberdinek ezkutuan jasotako irudiekin osatutako dokumentala da.", bozkak="0")
    f6 = filmak_filma(izenburua="Hiltegiak Euskal Herrian", zuzendaria="Nor", urtea="2018", generoa="DO",sipnosia="Azken minutua: Heriotza eta erresistentzia. 3 urteetan zehar Euskal Herriko edo inguruetako hiltegietan grabatutako irudiak dira honakoak.", bozkak="0")
    f7 = filmak_filma(izenburua="Cowspiracy: The Sustainability Secret", zuzendaria="Kip Andersen eta Keegan Kuhn", urtea="2014", generoa="DO", sipnosia="Follow the shocking, yet humorous, journey of an aspiring environmentalist, as he daringly seeks to find the real solution to the most pressing environmental issues and true path to sustainability.", bozkak="0")
    f8 = filmak_filma(izenburua="Munich 1962: isildu egia", zuzendaria="Larraitz Ariznabarreta eta Naroa Anabitarte", urtea="2014", generoa="DO", sipnosia="Kezka batetik sortutako proiektua da Munich 1962: isildu egia. Ordu hartan Munichen egon zirenen hitzak jaso dituzte Orreaga Taldeko kideek. Dokumental historikoa izateaz harago doa, ikus-entzulea hausnarketara gonbidatu nahi du. 'Iruditzen zaigu oraindik ere orduan gertatutakoak gaurkotasun handia duela; oraindik berdin jarraitzen dugu, garai hartan egin ziren akats berberak errepikatzen dira gaur egun', Naroa Anabitarte (Tolosa, 1979) Orreaga Taldeko kide eta dokumentalaren egilearen esanetan. Ez du ikusten politikarien aldetik akats berak ez errepikatzeko nahirik, 'ematen du dinamika beretan jarraitu nahi dela, aldez aurretik galduak diren bideak erabiliz'.", bozkak="0")
    f1.save()
    f2.save()
    f3.save()
    f4.save()
    f5.save()
    f6.save()
    f7.save()
    f8.save()
    return redirect('login')

objects = ['john', 'paul', 'george', 'ringo']


def filmak_ikusi(request):
    filmak = filmak_filma.objects.all()
    paginator = Paginator(filmak,5)
    page_number = request.GET.get('page')
    try:
         page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj=paginator.get_page(1)
    except EmptyPage:
        page_obj= paginator.page(paginator.num_pages)
   

    return render (request, 'FilmaGunea/katalogoa.html', {'filmak':page_obj})

def zaleak_ikusi(request):
    if request.method == 'POST':
        filma_id = request.POST.get('filma_id')
        filma = filmak_filma.objects.get(id=filma_id)
        bozkatzailea = filma.bozkatzaileak.all()
        return render(request, 'FilmaGunea/zaleak.html', {'filmak': filmak_filma.objects.all(), 'bozkatzailea': bozkatzailea})
    
    return render(request, 'FilmaGunea/zaleak.html', {'filmak': filmak_filma.objects.all()})



from .models import filmak_bozkatzailea

def bozkatu(request):
    filmak = filmak_filma.objects.all()

    if request.method=='POST':
        filma_id = request.POST.get('filma_id')
        erab = request.user
        filma = filmak_filma.objects.get(id=filma_id)
        bozkatzile_guztiak = filmak_bozkatzailea.objects.all()
        temp2 = bozkatzile_guztiak.filter(erabiltzailea=erab)
        if len(temp2)==0:
          bozkatzailea = filmak_bozkatzailea(erabiltzailea=erab)
          bozkatzailea.save()
          filma.bozkatzaileak.add(bozkatzailea)
          filma.bozkak += 1
          filma.save()
          messages.success(request, 'Milesker.')
          return redirect('bozkatu')
        else:
            bozka= filmak_bozkatzailea.objects.get(erabiltzailea=erab)
            temp= bozka.filmak_filma_set.filter(id=filma_id)
            if len(temp)==0:
                filma.bozkatzaileak.add(bozka)
                filma.bozkak += 1
                filma.save()
                messages.success(request, 'Milesker.')
                return redirect('bozkatu')
            else:
                messages.error(request, 'Jada botoa eman duzu pelikula honetan')
                return redirect('bozkatu')

    return render(request, 'FilmaGunea/bozkatu.html', {'filmak': filmak})


def ezabatuDena(request):
    filmak_filma.objects.all().delete()
    filmak_bozkatzailea.objects.all().delete()