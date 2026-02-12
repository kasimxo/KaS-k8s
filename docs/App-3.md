# App 3: Networking monitoring

En este proyecto se utiliza un sistema de varios pods para supervisar el rendimiento de una red de comunicación.

Aquí entra en juego la coordinación entre los distintos pods o servicios. En este sentido es importante tener en cuenta que kubernetes ya te da un DNS interno con el nombre del service. Esto se traduce a que aunque en cada pod distinto hayas configurado el puerto 8000 para escuchar peticiones, no va a haber riesgo de colisión (al fin y al cabo, a todos los efectos, son pods distintos). En cambio, si quieres hacer una petición al servicio "analytics-service", basta con que hagas una petición a "http://analytics-service:8000".

## Requisitos

Los mismos del archivo README base además de Python y conocimientos sobre Django. También emplearemos Redis y FastApi en este proyecto.

## Aquitectura

- Simulator: Pod encargado de producir mensajes simulando ser una antena de una red de antenas de comunicación. Para ello utiliza el nombre de pod como id único, así se puede replicar todas las veces que se quiera y cada una de las réplicas tiene un id distinto.

- Broker: Redis. Funciona como broker de mensajes

- Analytics: Pod que emplea PySpark para analizar los mensajes entrantes y calcular métricas como latencia media, paquetes entregados, % de éxito, identificación de antenas con más fallos...

- Dashboard: Pod encargado de la visualización de estos datos a través del navegador. Es el único que se comunica con el usuario a través del navegador.

## Guía

A continuación se detalla la construcción de este proyecto capa por capa, en el mismo orden y con los mismos pasos que he utilizado para llevarlo a cabo. Se incluyen anotaciones sobre cualquier error que haya encontrado por el camino.

Cada una de las capas se divide en dos secciones, siendo la primera la pura construcción de la aplicación y la segunda los comandos requeridos para hacer el despliegue y configuración en minikube/kubectl.

*Nota: Todos los comandos (a menos que se especifique lo contrario) se utilizan en powershell ejecutándose como administrador.*

### Dashboard

1. Aplicación Django

    1.1 Creamos un venv

    ```
    python -m venv venv
    ```

    1.2 Activamos el venv

    ```
    .\venv\Scripts\activate
    ```

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

    Puedes ver el contenido del archivo [aquí](../proyects/App-3/network-monitoring/dashboard/Dockerfile).

    1.14 Creamos archivo dashboard.yaml en el directorio k8s: En este archivo hemos incluido el bloque de deployment y el del service, separados por ---

2. Comandos

    ```
    minikube start # Iniciar minikube si no está iniciado
    minikube image build -t dashboard:v1 . # Construir la imagen con el archivo Dockerfile
    minikube image ls # Ver el listado de imágenes, debería aparecer dashboard:v1
    kubectl apply -f .\k8s\dashboard.yaml
    minikube service dashboard-service # Inicia el servicio, se te abrirá una pestaña en el navegador
    ```

Con todo esto ya tenemos la 1ª capa en funcionamiento.

### Analytics

1. Aplicación de ingesta y analítica de datos

    1.1 Creamos un venv

    ```
    python -m venv venv
    ```

    1.2 Activamos el venv

    ```
    .\venv\Scripts\activate
    ```

    1.3 Instalamos las dependencias que necesitaremos en el proyecto:

    ```
    pip install fastapi uvicorn pyspark redis requests
    ```

    1.4 Creamos requirements.txt: 
    
    ```
    pip freeze > requirements.txt
    ```

    1.5 Creamos el directorio app

    ```
    mkdir app
    ```

    1.6 Creamos el estado

    Creamos el archivo state.py, puedes ver el contenido [aquí](../proyects/App-3/network-monitoring/analytics/app/state.py).

    Estos son los datos que compartirán pyspark y fastapi para, por un lado, actualizar los datos a través de las analíticas y por otro, servir esos datos en respuesta a las peticiones recibidas.

    Es una zona de memoria compartida entre los dos procesos.

    1.7 Creamos el job de spark

    Creamos el archivo spark_job.py, puedes ver el contenido [aquí](../proyects/App-3/network-monitoring/analytics/app/spark_job.py).

    Este será el trabajo encargado de ir actualizando la información. Puedes comenzar creando un pequeño mock de los datos.

    1.8 Creamos la api

    Creamos el archivo main.py, puedes ver el contenido [aquí](../proyects/App-3/network-monitoring/analytics/app/main.py).

    Esta es la api que servirá los datos a partir de las peticiones recibidas. Podremos agregar más endpoints en el futuro, pero por el momento basta con exponer uno ("/metrics") que envíe los datos actualizados.

    En este punto ya puedes probar este servicio de forma local.
    
    Necesitarás tener JAVA instalado (jdk 21 por ejemplo) y las variables JAVA_HOME y JAVA correctamente configuradas.
    Una vez hayas hecho esto, puedes lanzar el servicio con el comando:
    
    ```
    uvicorn main:app --reload
    ```
    
    En el navegador, ve a /metrics y podrás ver el resultado.

    1.9 Archivo Dockerfile

    Creamos el archivo Dockerfile, puedes ver el contenido [aquí](../proyects/App-3/network-monitoring/analytics/Dockerfile).

    > <b>Importante</b>
    >
    > Como FastAPI necesita tener JAVA instalado y configurado, este archivo contiene los comandos necesarios para llevarlo a cabo en el momento de construir la imagen.

    1.10 Archivo analytics.yaml

    Creamos el archivo analytics.yaml dentro del directorio /k8s/, puedes ver el contenido [aquí](../proyects/App-3/network-monitoring/k8s/analytics.yaml).

    De nuevo, este archivo contiene la información necesaria tanto para el depoyment como para el service. Nuevamente recomiendo utilizar el versionado de las imágenes para tener un mayor control sobre ellas (utiliza el sufijo :vXX en el nombre de la imagen).

2. Comandos

    ```
    minikube image build -t analytics:v1 .
    minikube image ls
    kubectl apply -f .\analytics.yaml
    minikube service analytics-service
    kubectl get svc
    kubectl get pods
    kubectl logs -f analytics-859bb7848d-pvkdz

    kubectl apply -f analytics.yaml
    kubectl rollout restart deployment analytics # Como habíamos corregido un fallo en el archivo yaml, lo aplicamos de nuevo y después reiniciamos el pod

    kubectl get pods
    minikube service dashboard-service
    docker build -t dashboard:v2 .
    minikube build -t dashboard:v2 .
    minikube image build -t dashboard:v2 .
    minikube image ls
    minikube image rm dashboard:v1
    kubectl apply -f .\dashboard.yaml
    kubectl rollout restart deployment dashboard
    minikube image rm dashboard:v1
    minikube service dashboard-service
    ```

### Dashboard + Analytics

En este punto ya tenemos la capa de presentación de datos (dashboard) y la de ingesta, tratamiento y servicio de datos creadas y correctamente configuradas. 

Si lo has hecho todo bien, deberían estar funcionando correctamente, pero, por si acaso, revisa los siguientes puntos:

1. Que ambos pods están en funcionamiento

```
kubectl get pods
```

2. Que ambos servicios están en funcionamiento

```
kubectl get svc
```

3. Que tienes los archivos dashboard.yaml y analytics.yaml correctamente configurados

### Broker

### Simulator