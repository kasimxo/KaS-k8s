# App 4: Network monitoring with Helm

En este proyecto se implementa el uso de [Helm](https://helm.sh/es/) como gestor de paquetes para Kubernetes.

Helm permite la centralización de la configuración de todos los servicios. Esto es, un archivo values.yaml, que permite modificar las propiedades de todas las imágenes que participan en el cluster. Algunas de las ventajas son, mejoras en la escalabilidad, reducción en la complejidad en los despliegues (despliegues con un solo comando), versionado de la app (versionado de todo el conjunto de servicios) y facilidades a la hora de hacer rollbacks entre otros.

> <b>Importante:</b>
> 
> Este proyecto reutiliza todo el código de aplicaciones de [App-3: network monitoring](App-3.md) y lo modifica para implementar Helm.

## Requisitos

Los mismos del archivo README base además de conocimientos básicos (a alto nivel) sobre Helm.

## Guía