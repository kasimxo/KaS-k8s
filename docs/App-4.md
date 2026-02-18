# App 4: Network monitoring with Helm

En este proyecto se implementa el uso de [Helm](https://helm.sh/es/) como gestor de paquetes para Kubernetes.

Helm permite la centralización de la configuración de todos los servicios. Esto es, un archivo values.yaml, que permite modificar las propiedades de todas las imágenes que participan en el cluster. Algunas de las ventajas son, mejoras en la escalabilidad, reducción en la complejidad en los despliegues (despliegues con un solo comando), versionado de la app (versionado de todo el conjunto de servicios) y facilidades a la hora de hacer rollbacks entre otros.

> <b>Importante:</b>
> 
> Este proyecto reutiliza todo el código de aplicaciones de [App-3: network monitoring](App-3.md) y lo modifica para implementar Helm.

## Requisitos

Los mismos del archivo README base además de conocimientos básicos sobre Helm (y tenerlo instalado).

## Arquitectura

La organización de los archivos Helm va a tener un chart para cada servicio y un chart principal que los orquesta.

## Guía

Aquí se detalla cómo migrar cada servicio de su archivo yaml a su correspondiente estructura Helm. La transición de cada servicio es más sencilla de lo que aparenta y, la orquestación final, no tiene demasiada complicación si has integradado todos los servicios con Helm.

### Dashboard

1. Guía 



2. Comandos

    2.1 Validación de charts

    Es muy útil validar la integridad de un Chart antes de su aplicación, para ello puedes utilizar el siguiente comando

    ```
    helm lint < ruta >
    ```

    *Nota: Aunque no se va a volver a hacer una mención explícita a este comando, se recomienda ejecutarlo cada vez que hayas configurado un chart, para validarlo*

    2.2 Build de la imagen

    Este paso sigue siendo necesario, no ha cambiado con respecto al proyecto anterior. Se necesita hacer build de la imagen cada vez que hagas cambios para tener lista la última versión. El comando sigue siendo: 

    ```
    minikube image build -t < nombre de la imagen > .
    ```

    2.3 Instalación del Chart

    Aquí es cuanto comenzamos a aprovechar las ventajas de Helm para instalar la imagen.

    ```
    helm install < nombre de la release > < ruta al chart >
    ```

    En este punto tuve varios errores:

    > <b>Cluster reachability check failed</b>
    >
    > En mi caso, se debía a que no había iniciado minikube ('minikube start') y por tanto no estaba el cluster disponible

    > <b>INSTALLATION FAILED: Service "dashboard-dashboard" is invalid: spec.ports[0].nodePort: Invalid value: 30081: provided port is already allocated</b>
    >
    > Self explanatory. Como ya tenemos este puerto ocupado con el otro servicio, entra en conflicto. Aquí hay dos soluciones posibles:
    > Borrar el actual para poder hacer la instalación del Chart
    > Modificar el puerto. Puedes cambiar la configuración del values.yaml o pasar el parámetro en el momento de hacer install

### Analytics

1. Guía 

2. Comandos

### Redis

1. Guía 

2. Comandos

### Simulator

1. Guía 

2. Comandos

### Orquestador

Este es el Chart encargado de orquestar el resto de charts y de coordinar los microservicios.

1. Guía 

2. Comandos
