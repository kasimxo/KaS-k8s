# App 3: Networking monitoring

En este proyecto se utiliza un sistema de varios pods para supervisar el rendimiento de una red de comunicación.

## Aquitectura

- Simulator: Pod encargado de producir mensajes simulando ser una red de antenas de comunicación. Para ello utiliza el nombre de pod como id único, así se puede replicar todas las veces que se quiera y cada una de las réplicas tiene un id distinto.

- Broker: Redis. Funciona como broker de mensajes

- Processor: Pod que emplea PySpark para analizar los mensajes entrantes y calcular métricas como latencia media, paquetes entregados, % de éxito, identificación de antenas con más fallos...

- Dashboard: Pod encargado de la visualización de estos datos a través del navegador. Es el único que se comunica con el usuario a través del navegador.


## Dashboard

Creamos un venv
Activamos el venv
Instalamos las dependencias que necesitaremos en el proyecto: django, requests
Creamos requirements.txt: pip freeze > requirements.txt
Creamos el proyecto django: django-admin startproject dashboard_project .
Creamos la segunda app que tendrá las vistas: python manage.py startapp metrics
Agregamos una vista básica (le incluimos un método de mockup mientras no tengamos el resto de servicios desarrollados)
Creamos un archivo de template para el dashboard
Agregamos el archivo urls
Incluimos las urls de metrics en la app principal
Incluimos la app de metrics en installed_apps de la app principal
Modificamos allowed hosts en la app principal
Creamos archivo Dockerfile en la raíz del proyecto
Creamos archivo dashboard.yaml en el directorio k8s: En este archivo hemos incluido el bloque de deployment y el del service, separados por ---
Comandos de powershell:
> minikube start
> minikube image build -t dashboard:v1 .
> minikube image ls
> cd ..
> kubectl apply -f .\k8s\dashboard.yaml
> minikube service dashboard-service
