from django.shortcuts import render, HttpResponse, redirect
from .forms import CreacionCliente, InscripcionCarrera
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Cliente, Inscripcion
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError


def registro(request):

    if request.method == 'POST':
        form = CreacionCliente(request.POST)

        if form.is_valid():
    
            form.save()
            return redirect('inicio_sesion')
        else:
            for i in form.error_messages:
                messages.error(request, form.error_messages[i])
                return render (request, 'registro.html', {'form':form})
    
    form = CreacionCliente()

    return render(request, 'registro.html', {'form':form})


def inicio_sesion(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)

        if form.is_valid():
            id = form.cleaned_data['username']
            contrasena = form.cleaned_data['password']
            user  = authenticate(request, username= id, password = contrasena)
            
            if user is not None:
                login(request, user)
                return redirect ('inicio')
        else: 
            messages.error(request, 'Identificacion o contraseña incorrectos')
        
    form = AuthenticationForm()
    return render(request,'inicio_sesion.html',{'form':form})


@login_required
def inicio(request):
    
    return render(request,'inicio.html',{})


def cerrar_sesion(request):
    logout(request)
    request.session.flush()
    return redirect('inicio_sesion') 


@login_required
def inscribir_carrera(request):

        if request.method == 'POST':
            form = InscripcionCarrera(request.POST)
            
            if form.is_valid():

                inscripcion = Inscripcion(
                    categoria=form.cleaned_data['categoria'],
                    nivel=form.cleaned_data['nivel'],
                    usuario=request.user.num_identificacion, 
                )
                inscripcion.save()
                return redirect('inscribir_carrera')
        
        form = InscripcionCarrera()
        existe = Inscripcion.objects.filter(usuario=request.user.num_identificacion).exists()
           
        if existe:
            carreras = Inscripcion.objects.get(usuario=request.user.num_identificacion)
            return render(request, 'registro_carrera.html', {'carreras': carreras})

        carreras = Inscripcion.objects.filter(usuario=request.user.num_identificacion)
        return render(request, 'registro_carrera.html', {'form': form, 'carreras': carreras})