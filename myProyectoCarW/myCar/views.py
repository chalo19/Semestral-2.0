from django.shortcuts import render
from .models import SliderIndex,MisionyVision,Galeria1,Insumos

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,logout, login as login_aut

from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.
def inicio(request):
    autos = SliderIndex.objects.all()
    return render(request,'index.html',{'autos':autos})

def galeria(request):
    gale = Galeria1.objects.all()
    return render(request,'galeria.html',{'gale':gale})

def formulario(request):
    if request.POST:
        nombre = request.POST.get("txtNombre")
        apellido = request.POST.get("txtApellido")
        email = request.POST.get("txtEmail")
        usuario = request.POST.get("txtUser")
        contra = request.POST.get("txtPass")
        contraR = request.POST.get("txtPassRepetir")

        if contra!=contraR:
            return render(request,'formulario.html',{'msg':'Contraseña Incorrecta'})

        try:
            usu = User.objects.get(username=usuario)
            return render(request,'formulario.html',{'msg':'Usuario Existente'})
        except:        
            usu = User()
            usu.first_name = nombre
            usu.last_name = apellido
            usu.email = email
            usu.username = usuario
            usu.set_password(contra)
            usu.save()

            us = authenticate(request, username=usuario, password=contra)
            login_aut(request,us)

            autos = SliderIndex.objects.all()
            return render(request,'index.html',{'autos':autos})

    return render(request,'formulario.html')

@login_required(login_url='/login/')
@permission_required('myCar.view_insumos',login_url='/login/')
@permission_required('myCar.change_insumos',login_url='/login/')
def modificar(request):
    msg=''
    if request.POST.get:
        nombre = request.POST.get("nombreinsumo")
        precio = request.POST.get("precioinsumo")
        descripcion = request.POST.get("descripcioninsumo")
        stock = request.POST.get("stock")
        
        try:
            insumo = Insumos.objects.get(nombre=nombre)
            precio = precio,
            descripcion = descripcion,
            stock = stock
            insumo.save()
            msg='Modifico'
        except:
            msg='No Modifico'

    insumos = Insumos.objects.all()
    return render(request,'admin_productos.html',{'lista_insumos': insumos,'msg':msg})  

@login_required(login_url='/login/')
@permission_required('myCar.view_insumos',login_url='/login/')
def busqueda_mod(request,id):
    try:
        insumo = Insumos.objects.get(nombre=id)
        return render(request,'modificar.html',{'insumo':insumo})
    except:
        msg='INSUMO NO ENCONTRADO'
    insumos = Insumos.objects.all()
    return render(request,'admin_productos.html',{'lista_insumos': insumos,'msg':msg})

@login_required(login_url='/login/')
@permission_required('myCar.delete_insumos',login_url='/login/')
def eliminar(request,id):
    try:
        insumo = Insumos.objects.get(nombre=id)
        insumo.delete()
        msg='INSUMO ELIMINADO CORRECTAMENTE'
    except:
        msg='INSUMO NO EXISTE'
    insumos = Insumos.objects.all()
    return render(request,'admin_productos.html',{'lista_insumos': insumos,'msg':msg})

@login_required(login_url='/login/')
@permission_required('myCar.view_insumos',login_url='/login/')
def lista_insumos(request):
    insumos = Insumos.objects.all()
    return render(request,'admin_productos.html',{'lista_insumos': insumos})

@login_required(login_url='/login/')
@permission_required('myCar.add_insumos',login_url='/login/')
def formulario2(request):
    if request.POST:
        nombre = request.POST.get("nombreinsumo")
        precio = request.POST.get("precioinsumo")
        descripcion = request.POST.get("descripcioninsumo")
        stock = request.POST.get("stock")
        insumo = Insumos(
            nombre = nombre,
            precio = precio,
            descripcion = descripcion,
            stock = stock
        )
        insumo.save()

        return render(request,'formulario 2.html',{'msg':'INSUMO GRABADO'})  

    return render(request,'formulario 2.html')

def quienes_somos(request):
    myv = MisionyVision.objects.all()
    return render(request,'quienes_somos.html',{'myv':myv})

def cerrar_sesion(request):
    logout(request)
    autos = SliderIndex.objects.all()
    return render(request,'index.html',{'autos':autos})

def login(request):
    if request.POST:
        usuario = request.POST.get("txtNombre")
        password = request.POST.get("txtContra")
        us = authenticate(request, username=usuario, password=password)
        if us is not None and us.is_active:
            login_aut(request,us)
            autos = SliderIndex.objects.all()
            return render(request,'index.html',{'autos':autos})
        else:
            return render(request,'login.html',{'msg':'NO EXISTE EL USUARIO'})
    return render(request,'login.html')