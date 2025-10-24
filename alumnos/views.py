from django.shortcuts import render, get_object_or_404, redirect
from .models import Alumno
from .forms import AlumnoForm

def lista_alumnos(request):
      alumnos = Alumno.objects.all().order_by('id')
      busqueda = request.GET.get('q')
            
      if busqueda:
            # Filtra por nombre o apellido o id (sin usar Q)
            alumnos = Alumno.objects.filter(nombre__icontains=busqueda) | Alumno.objects.filter(apellido__icontains=busqueda)
            try:
                  # si lo que escribió el usuario es un número, buscamos por id también
                  busqueda_id = int(busqueda)
                  alumnos = alumnos | Alumno.objects.filter(id=busqueda_id)
            except:
                  pass
            
      contexto = {
            'alumnos': alumnos,
            'busqueda': busqueda,
      }
      
      return render (request, 'alumnos/lista.html', contexto)

def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = AlumnoForm()
    return render(request, 'alumnos/crear.html', {'form': form})


def editar_alumno(request, pk):
      alumno = get_object_or_404(Alumno, pk=pk)
      if request.method == 'POST':
            form = AlumnoForm(request.POST, instance=alumno)
            if form.is_valid():
                  form.save()
                  return redirect('lista')
      else:
            form = AlumnoForm(instance= alumno, 
                              initial={
                              'fecha_ingreso': alumno.fecha_ingreso.strftime('%d-%m-%Y')
                        })
      return render(request, 'alumnos/editar.html', {'form': form, 'alumno': alumno})


def eliminar_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        alumno.delete()
        return redirect('lista')
    return render(request, 'alumnos/eliminar.html', {'alumno': alumno})

def detalle_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    return render(request, 'alumnos/detalle.html', {'alumno': alumno})