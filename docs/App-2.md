# App 2

En este proyecto vamos a construir una aplicación a la que podremos hacer peticiones y nos devolverá un "Hello World!" en el navegador.

Como crearemos la aplicación de cero, veremos como crear y configurar archivos como Dockerfile, deployment.yaml o service.yaml.

## Requisitos

Además de los detallados en el archivo README previo, necesitarás tener instalado Python y tener conocimientos básicos sobre Django.

### Hello world con django en k8s

1. Aplicación Django

    1.1 Crear venv
    > python -m venv venv
    
    1.2 Activar venv:
    > .\venv\Scripts\activate
    
    1.3 Install django
    > pip install django
    
    1.4 Creamos la aplicación base de django: 
    > django-admin startproject hello .
    
    1.5 Modificar urls.py e incluir: 
    > path("", lambda request: HttpResponse('Hello, World!'))
    
    1.6 Modificamos settings: 
    > ALLOWED_HOSTS = ["*"]
    
    1.7 Ejecutar migraciones (técnicamente se puede incluir en el archivo Dockerfile, pero me daba problemas)
    > python manage.py makemigrations
    > python manage.py migrate
    
    1.8 Crear archivo requirements.txt:
    > pip freeze > requirements.txt

2. Archivos k8s

    2.1 Incluimos un archivo Dockerfile en la raíz del proyecto

    Puedes ver el contenido del archivo Dockerfile [aquí](../django-hello-world/Dockerfile)

    > <b>Importante I</b>
    > 
    > El contenido del archivo Dockerfile es bastante self-explanatory (el archivo contiene comentarios), pero asegurate de que el puerto que hayas incluido en el comando EXPOSE y el puerto que utilices en el comando CMD para levantar el servidor sean el mismo. Además, este puerto lo utilizaremos más adelante en otros archivos de configuración, así que asgurate siempre de utilizar el puerto correcto

    > <b>Importante II</b>
    >
    > El archivo Dockerfile tiene que ser nombrado EXACTAMENTE así. Si, por ejemplo, lo nombras "DockerFile" (como hice yo) en el momento de hacer la build no te encontrará dicho archivo (puedes utilizar argumentos en el comando para especificar esto, pero también puedes ahorrarte esa preocupación)

    2.2 Creamos el archivo deployment.yaml

    *Nota: Los archivos deployment.yaml y service.yaml se han unificado en un mismo directorio, /k8s/*

    Puedes ver el contenido del archivo deployment.yaml [aquí](../django-hello-world/k8s/deployment.yaml)

    > <b>Importante I</b>
    >
    > De nuevo, asegurate de que estás empleando el mismo puerto

    > <b>Importante II</b>
    >
    > imagePullPolicy: Never - Agregué esta propiedad ya que al principio parecía que había un problema al encontrar el pod, aunque con una mejor configuración desde el principio quizá no fuera necesario:
    > "Error from server (BadRequest): container "< container name >" in pod "< pod name >" is waiting to start: trying and failing to pull image"

    > <b>Importante III</b>
    >
    > image: django-hello:v3 - Relacionado con cómo haces build del contenedor. Agregar vXX ayuda a un mejor seguimiento de versiones y errores. En mi caso me ayudó a resolver errores de builds previas

    2.3 Archivo service.yaml

    Este es el archivo encargado de levantar el servicio que permitirá exponer la aplicación al través de un puerto.

    Puedes ver el contenido del archivo [aquí](../django-hello-world/k8s/service.yaml)

    > <b>Importante</b>
    >
    > De nuevo, asegurate de que el puerto que estés especificando coincida con el puerto de Django.

3. Comandos

    3.1 Hacer build de la imagen
    Para utilizar docker a través de minikube y que pueda ver las imágenes
    > minikube docker-env | Invoke-Expression

    > docker build --no-cache -t < image name > .

    > <b>Importante I</b>
    >
    > Te recomiendo, en la medida de lo posible, que lances ese comando desde la ruta del proyecto (aunque no es estrictamente necesario, podrías detallar la ruta absoluta)

    > <b>Importante II</b>
    >
    > ¿Te acuerdas cuando mencioné lo de nombrar el archivo Dockerfile exactamente así? Aquí es donde te dará un fallo si no lo encuentra

    > <b>Importante III</b>
    >
    > El argumento --no-cache no es estrictamente necesario, pero en mi caso, lo utilizaba para asegurarme de que no se estuviera reutilizando una capa que se hubiera aplicado mal en un primer momento

    Puedes utilizar el comando docker images para ver que realmente se ha construido tu imagen correctamente

    3.2 Archivos deployment.yaml y service.yaml

    En este punto los vamos a ejecutar con kubectl apply:
    > kubectl apply -f deployment.yaml

    > kubectl apply -f service.yaml

    Puedes revisar ambos con los correspondientes comandos:
    > kubectl get pods

    > kubectl get svc

    3.3 Debug a través de logs
    Algo que me resultó muy útil fue ver los logs de la imagen. Para ello puedes utilizar los siguientes comandos:
    > kubectl get pods

    > kubectl logs -f < nombre del pod >

    3.4 Reiniciar imagen/continer/pod

    Si en algún momento has necesitado cambiar archivos de configuración (por ejemplo, si en un primer momento has comentido algún error con la configuración), necesitarás volver a hacer build.
    > kubectl rollout restart deployment < nombre del deployment (deployment metadata name) >