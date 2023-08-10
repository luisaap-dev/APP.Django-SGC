# Sistema de Gestión de Clientes utilizando Django

Este repositorio contiene un Sistema de Gestión de Clientes desarrollado en Django. Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en una base de datos de clientes, así como búsquedas y ordenamientos. Además, proporciona una interfaz de usuario amigable para administrar los clientes y sus detalles.

## Instrucciones de Configuración

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone <SGC-Django>
   ```

2. Navega al directorio del proyecto:

   ```bash
   cd <SGC-Djang>
   ```

3. Instala las dependencias utilizando `pip`:

   ```bash
   pip install -r requirements.txt
   ```

4. Realiza las migraciones para configurar la base de datos:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Recopila los archivos estáticos:

   ```bash
   python manage.py collectstatic
   ```

6. Opcional: Si deseas cargar datos de prueba, asegúrate de que el archivo `clientes.json` esté en la carpeta data. Luego, ejecuta el siguiente comando para cargar los datos:

   ```bash
   python manage.py loaddata data/clientes.json
   ```

7. Inicia el servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```

8. Abre tu navegador web y visita `http://localhost:8000` para acceder al sistema.

## Uso del Sistema

### Página de Inicio

La página de inicio proporciona una introducción al Sistema de Gestión de Clientes.

### Listar Clientes

Aquí puedes ver la lista de clientes existentes en la base de datos. Realiza búsquedas por nombre y ordena los resultados por diferentes criterios. Se muestran 10 clientes por página, con navegación de paginación.

También puedes eliminar varios clientes seleccionados al mismo tiempo.

### Añadir Cliente

Utiliza esta sección para añadir un nuevo cliente a la base de datos. Completa el formulario con la información del cliente y una foto (opcional), luego haz clic en "Guardar" para agregarlo.

### Detalle de Cliente

Aquí puedes ver los detalles de un cliente específico. Edita la información existente del cliente o elimínalo por completo. Si decides eliminar un cliente, se eliminarán sus detalles y la carpeta asociada (si existe) que contiene los archivos relacionados.

### Nota

Configurar bases de datos antes de ejecutar los comandos 
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "app_clientes",
        "USER": "root",  
        "PASSWORD": "afd",  
        "HOST": "localhost",
        "PORT": "3306", 
    }
}
```
## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo [LICENSE](LICENSE).

## Autor

Este proyecto fue creado por Luis Ares. Puedes encontrar más información sobre el autor en su perfil de GitHub: [@luisaap-dev](https://github.com/luisaap-dev).
```