# Importar las bibliotecas necesarias
import os
import shutil
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from .forms import ClienteForm

def index(request):
    return render(request, 'crudpy/index.html')

def listar_clientes(request):
    # Obtener el término de búsqueda (si se proporciona)
    search_query = request.GET.get('search', '').lower()

    # Obtener el parámetro de ordenación (si se proporciona)
    ordering = request.GET.get('ordering', 'id')

    # Obtener el parámetro para reiniciar la búsqueda (si se proporciona)
    reset_search = request.GET.get('reset', False)

    if reset_search:
        search_query = ''  # Reiniciar la búsqueda si el parámetro reset es proporcionado


    # Filtrar los clientes por el término de búsqueda y ordenarlos por el campo especificado
    clientes = Cliente.objects.filter(nombre__icontains=search_query).order_by(ordering)

    # Paginación de los clientes (mostrar 10 clientes por página)
    paginator = Paginator(clientes, 10)
    page_number = request.GET.get('page')

    try:
        clientes_paginados = paginator.get_page(page_number)
    except (PageNotAnInteger, EmptyPage):
        # Si el número de página no es un entero o está fuera de rango, mostrar la primera página
        clientes_paginados = paginator.get_page(1)

    # Verificar si se está enviando el formulario para eliminar clientes seleccionados
    if request.method == 'POST':
        selected_clients = request.POST.getlist('selected_clients')
        if selected_clients:
            try:
                # Obtenemos los clientes a eliminar
                clients_to_delete = Cliente.objects.filter(id__in=selected_clients)

                for client in clients_to_delete:
                    # Borramos la foto del cliente (si existe)
                    if client.foto and os.path.exists(client.foto.path):
                        os.remove(client.foto.path)

                    # Borramos la carpeta asociada al cliente (si existe)
                    folder_path = os.path.join('media', 'clientes', str(client.nombre))
                    if os.path.exists(folder_path):
                        # Usamos shutil.rmtree para eliminar la carpeta y su contenido
                        shutil.rmtree(folder_path)

                # Finalmente, eliminamos los clientes de la base de datos
                clients_to_delete.delete()

                messages.success(request, 'Clientes seleccionados eliminados correctamente.')

            except Exception as e:
                messages.error(request, 'Error al eliminar los clientes seleccionados.')

    context = {
        'clientes': clientes_paginados,
        'search_query': search_query,
    }

    return render(request, 'crudpy/listar_clientes.html', context)

def añadir_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()

    context = {
        'form': form,
    }

    return render(request, 'crudpy/añadir_cliente.html', context)

def detalle_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)

    if request.method == 'POST':
        if 'eliminar' in request.POST:
            # Obtenemos la ruta de la carpeta del cliente (suponiendo que está dentro del directorio 'clientes')
            carpeta_cliente_path = os.path.join('media', 'clientes', str(cliente.nombre))

            # Borramos la foto del cliente (si existe)
            if cliente.foto and os.path.exists(cliente.foto.path):
                os.remove(cliente.foto.path)

            # Borramos la carpeta asociada al cliente (si existe)
            if os.path.exists(carpeta_cliente_path):
                # Usamos shutil.rmtree para eliminar la carpeta y su contenido
                shutil.rmtree(carpeta_cliente_path)

            # Finalmente, eliminamos el cliente de la base de datos
            cliente.delete()

            messages.success(request, 'Cliente eliminado correctamente.')

            return redirect('listar_clientes')
        else:
            form = ClienteForm(request.POST, request.FILES, instance=cliente)
            if form.is_valid():
                form.save()
                return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)

    context = {
        'cliente': cliente,
        'form': form,
        'edit_mode': True,
    }

    return render(request, 'crudpy/detalle_cliente.html', context)