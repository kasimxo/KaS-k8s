# App 3: Networking monitoring

En este proyecto se utiliza un sistema de varios pods para supervisar el rendimiento de una red de comunicación.

## Requisitos

Los mismos del archivo README base además de Python y conocimientos sobre Django.

## Aquitectura

- Simulator: Pod encargado de producir mensajes simulando ser una antena de una red de antenas de comunicación. Para ello utiliza el nombre de pod como id único, así se puede replicar todas las veces que se quiera y cada una de las réplicas tiene un id distinto.

- Broker: Redis. Funciona como broker de mensajes

- Processor: Pod que emplea PySpark para analizar los mensajes entrantes y calcular métricas como latencia media, paquetes entregados, % de éxito, identificación de antenas con más fallos...

- Dashboard: Pod encargado de la visualización de estos datos a través del navegador. Es el único que se comunica con el usuario a través del navegador.

## Guía

A continuación se detalla la construcción de este proyecto capa por capa, en el mismo orden y con los mismos pasos que he utilizado para llevarlo a cabo. Se incluyen anotaciones sobre cualquier error que haya encontrado por el camino.

*Nota: Todos los comandos (a menos que se especifique lo contrario) se utilizan en powershell ejecutándose como administrador.*

### Dashboard

1. Aplicación Django

    1.1 Creamos un venv

    1.2 Activamos el venv

    1.3 Instalamos las dependencias que necesitaremos en el proyecto: django, requests

    1.4 Creamos requirements.txt: 
    
    ```
    pip freeze > requirements.txt
    ```

    1.5 Creamos el proyecto django: django-admin startproject dashboard_project .

    1.6 Creamos la segunda app que tendrá las vistas: 
    
    ```
    python manage.py startapp metrics
    ```

    1.7 Agregamos una vista básica (le incluimos un método de mockup mientras no tengamos el resto de servicios desarrollados)

    1.8 Creamos un archivo de template para el dashboard

    1.9 Agregamos el archivo urls

    1.10 Incluimos las urls de metrics en la app principal

    1.11 Incluimos la app de metrics en installed_apps de la app principal

    1.12 Modificamos allowed hosts en la app principal

    1.13 Creamos archivo Dockerfile en la raíz del proyecto

    1.14 Creamos archivo dashboard.yaml en el directorio k8s: En este archivo hemos incluido el bloque de deployment y el del service, separados por ---

2. Comandos

```
minikube start # Iniciar minikube si no está iniciado
minikube image build -t dashboard:v1 . # Construir la imagen con el archivo Dockerfile
minikube image ls
cd ..
kubectl apply -f .\k8s\dashboard.yaml
minikube service dashboard-service # Inicia el servicio, se te abrirá una pestaña en el navegador
```

Con todo esto ya tenemos la 1ª capa en funcionamiento.

### Processor

### Broker

### Simulator