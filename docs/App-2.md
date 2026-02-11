# App 2



### Hello world con django

- Crear venv
- Ejecutar venv
- Install django
- django-admin startproject hello .
- Modificar urls.py para incluir path("", lambda request: HttpResponse('Hello, World!'))
- Modificamos settings: ALLOWED_HOSTS = ["*"]
- Incluimos un archivo Dockerfile en la raíz del proyecto


DockerFile -> Dockerfile o, en su defecto especificar concretamente el formato que vas a emplear