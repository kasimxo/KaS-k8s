El propósito de este proyecto es hacer una exploración a las posibilidades de kubernetes a través de varios proyectos.

## Requisitos previos

A continuación se detallan todas las configuraciones e instalaciones necesarias (las que al menos yo he necesitado) para poder realizar todos estos proyecto:

- Docker: Si estas utilizando Windows, debes instalar Docker Desktop y asegurarte de configurarlo de forma que utilice WSL. *Nota: Puedes conseguir Docker Desktop a través de la App Store de Windows si la página está caída.*
- WSL: Asegurate de que tienes WSL correctamente configurado en tu pc y listo para utilizar
- Minikube: Puedes descargarlo e instalarlo a través del siguiente enlace https://minikube.sigs.k8s.io/docs/start/?arch=%2Fwindows%2Fx86-64%2Fstable%2F.exe+download 

## Proyectos

Puedes encontrar la documentación de todos los proyectos dentro de docs/. 

- App-1: Cómo crear un set-up por el que tengamos una aplicación ejecutándose en un pod y un service que exponga dicha aplicación para que pueda ser utilizada
- App-2: Cómo configurar una aplicación de Django para que pueda ser utilizada en k8s y expuesta a través de un service
