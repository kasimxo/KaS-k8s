# App 1

Este documento trata de cómo hacer el set-up necesario para tener un pod con un service expuesto al que le podamos hacer llamadas. Es por esto que este proyecto se centra más en el uso básico de minikube y kubectl a través de la terminal que en k8s en profundidad.

En este caso, utilizamos una imagen ya configurada a modo de hello world para evitar problemas a la hora de configurar el dockerfile, o archivos de configuración como deployment.yaml o service.yaml.

## Requisitos

Los detallados en el README de este repositorio. No vas a necesitar nada adicional.

## Guía

Puedes encontrar la guía original paso a paso aquí: https://kubernetes.io/docs/tutorials/hello-minikube/

1. Configuración de Docker Desktop

    1.1 En Configuración > General, asegurate de que está marcada la opción "Use the WSL 2 based engine"

    1.2 En Configuración > Resources > WSL integration asegurate de que está activa la opción "Enable integration with my default WSL distro" y marca también la distro que tengas configurada. Ejemplo, Ubuntu.

    1.3 Revisa que tengas Docker en la variable de entorno PATH

2. Comandos

    2.1 Para ejecutar minikube, utiliza el comando 

    ```
    minikube start
    ``` 

    desde powershell como administrador.

    *Nota*: Para poder ejecutar minikube (lanzarlo) tendrás que tener docker ejecutándose

    2.2 Puedes revisar que se esté ejecutando con 
    
    ```
    minikube status
    ```

    2.3 Y para lanzar el dashboard (lo abrirá en el navegador)
    
    ```
    minikube dashboard 
    ```

    Está bien para ver toda la información de forma visual, aunque en otros ejercicios recuperaremos esta misma información a través de comandos como 'kubectl logs -f < nombre del pod >'

    2.4 Generar una imagen de prueba: 
    
    ```
    kubectl create deployment hello-node --image=registry.k8s.io/e2e-test-images/agnhost:2.53 -- /agnhost netexec --http-port=8080
    ```

    Aquí estamos creando un deployment con una imagen de un repositorio. (Podrás verla desde el dashboard o verificar su estado con el comando kubectl get deployments)

    2.5 Exponer la imagen a través de un servicio
    > <b>Create a Service</b>
    > 
    > By default, the Pod is only accessible by its internal IP  address within the Kubernetes cluster. To make the hello-node Container accessible from outside the Kubernetes virtual network, you have to expose the Pod as a Kubernetes Service."

    Para esto puedes utilizar:
    
    ```
    kubectl expose deployment hello-node --type=LoadBalancer --port=8080
    ```

    En este punto ya deberíamos tener todo listo y se nos abrirá en el navegador.

    2.6 Cerrar y eliminar pods

    ```
    kubectl delete service hello-node
    kubectl delete deployment hello-node
    minikube stop
    ```