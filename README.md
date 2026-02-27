El propósito de este proyecto es hacer una exploración a las posibilidades de kubernetes a través de varios proyectos.

Cada uno amplía sobre el anterior, por lo que si estás interesado en aprender sobre estas tecnologías, te recomiendo que los veas uno a uno. Si por el contrario buscas un ejemplo de qué permiten, puedes ir directamente a los últimos proyectos, que son los más completos.

## Requisitos previos

A continuación se detallan todas las configuraciones e instalaciones necesarias (las que al menos yo he necesitado) para poder realizar todos estos proyecto:

- Docker: Si estas utilizando Windows, debes instalar Docker Desktop y asegurarte de configurarlo de forma que utilice WSL. *Nota: Puedes conseguir Docker Desktop a través de la App Store de Windows si la página está caída.*
- WSL: Asegurate de que tienes WSL correctamente configurado en tu pc y listo para utilizar
- Minikube: Puedes descargarlo e instalarlo a través del siguiente enlace [aquí](https://minikube.sigs.k8s.io/docs/start/?arch=%2Fwindows%2Fx86-64%2Fstable%2F.exe+download)
- Helm: Aunque no es necesario en los primeros proyectos, en clusters complejos lo utilizo para simplificar la gestión de los pods. Puedes descargarlo e instalarlo a través del siguiente enlace [aquí](https://helm.sh/docs/intro/install)

En cada uno de los proyectos se detallan los requerimientos adicionales, como conocimientos básicos sobre Python, Django, FastAPI, Redis...

## Proyectos

Puedes encontrar la documentación de todos los proyectos dentro de docs/. 

- [App-1](./docs/App-1.md): Creación de un set-up por el que tengamos una aplicación ejecutándose en un pod y un service que exponga dicha aplicación para que pueda ser utilizada
- [App-2](./docs/App-2.md): Configuración de una aplicación de Django para que pueda ser utilizada en k8s y expuesta a través de un service
- [App-3](./docs/App-3.md): Construcción de un sistema que se encarga de la supervisión de una red de comunicación. Utiliza varios pods que se comunican entre ellos
- [App-4](./docs/App-4.md): Utilización de Helm como gestor de paquetes para kubernetes
- [App-5](./docs/App-5.md): Introducción a Ingress para gestionar los accesos al cluster
- [App-6](./docs/App-6.md): Introducción a MLOps, despliegue del primer modelo en un cluster
