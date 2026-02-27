# App 5: Network monitoring with ingress

En este proyecto se implementa el uso de [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) a modo de API para gestionar el acceso desde el exterior al cluster.

![Diagrama Ingress](https://mermaid.live/edit#pako:eNqNUsGOmzAQ_RVrcmklQIQkQLxVLt0eKvVQdW8NORg8JFaMjWzT7jabf6-J2WSjXsqBmXnz5nk84xM0miNQqNTesP5Avv14qBQhjRSo3IdtsLuPcUK-egZaG3dMsT1y8qk2GyI146RmkqkGDUnijQis7cTeXdQmMI43r0YPzofEDBJfLZpfosHtU7CBbIc6tNLIwTo07wRCPpC9WK_5fPtd892_eHbDUfFwI2btI7akl0wo0gop6YxzHlln9BHprG3byY9_C-4OdNk_R42W2tBZmqYPdyLH0k4SiyxvcPVfKj53rzLdcFK6ldJZXdf3MtlNJpx4U3qbTjRNIBrnMv6ysc13vLDMMIA7OHQxWZ-pFESwN4IDdWbACDo0HRtDOI11FbgDdlgB9S5n5lj593P2NT1TP7Xu3sr8svcHoC2T1kdDz5nDR8H8eq-UAH7hwmlzZbLB6acX1Vx1_A7RfNaDckDnxeUcoCd4BrpI8yTL03K9LIrVYp3mEbx4NE_mZbE6R_Dn0k6alMVy7b98VRbeS5fnv7VGAqM)

*Nota: Actualmente Kubernetes recomienda el uso de [Gateway](https://gateway-api.sigs.k8s.io/) en lugar de Ingress, ya que este proyecto ya no está en desarrollo*

> <b>Importante:</b>
> 
> Este proyecto toma como base [App-4: network monitoring](App-4.md) y lo modifica para implementar Ingress.

## Requisitos

Además de los necesarios para [App-4: network monitoring](App-4.md), instalaremos un ingresscontroller en el cluster

## Guía

1. Instalar el controlador

Instalamos el controlador NGINX Ingress controller con el siguiente comando:

```
minikube addons enable ingress
```

2. Modificar los services

Como ahora vamos a utilizar ingress como puerta de entrada al cluster, ya no necesitamos tener configurado el service de dashboard como NodePort, puedes cambiarlo por ClusterIP en el archivo values.yaml. Puedes ver el cambio [aquí](./../projects/App-5/network-monitoring/helm/network-monitoring/charts/dashboard/values.yaml)

3. Crear el recurso ingress

Creamos el recurso ingress dentro de las templates del umbrella chart (chart padre). Puedes ver el contenido del archivo [aquí](./../projects/App-5/network-monitoring/helm/network-monitoring/templates/ingress.yaml)