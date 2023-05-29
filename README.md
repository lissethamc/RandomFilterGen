# RandomFilterGen

El arte generativo es una forma de expresión artística en la que se utilizan sistemas o algoritmos computacionales para generar obras de arte. En lugar de ser creadas directamente por un artista humano, estas obras se generan a través de procesos automáticos o semi-automáticos, donde se establecen reglas, parámetros o algoritmos que determinan cómo se desarrolla la obra.

RandomFilterGen es un sistema basado en arte generativo que emplea algoritmos y parámetros aleatorios para aplicar filtros a las imágenes, generando resultados únicos en cada iteración. Esta herramienta te permite explorar la creatividad a través de la personalización de los parámetros y experimentar con una amplia variedad de filtros generativos. Descubre la belleza del arte en lo impredecible y transforma tus imágenes en obras de arte auténticas y sorprendentes.

## Sitio hasta el momento:
![imagen](https://github.com/lissethamc/RandomFilterGen/assets/101375005/2bf948b8-f999-449f-8284-f2b78676accc)

## Implementación en DigitalOcean

Para su administración se hace uso de Kubectl, Doctl e Istioctl.
Es necesario hacer un contenedor donde se incluya la aplicación desarrollada, esto a partir de un Dockerfile, también es necesario indicar en un archivo `requirements.txt` las librerías que funcionan como requisitos, que son `PIL`, `Flask` `glitch_this`.

Después de hacer `docker build .` podemos ver en las imágenes nuestra imagen creada con `docker images`
![image](https://github.com/lissethamc/RandomFilterGen/assets/33168405/5d28d23b-b0a8-4577-a1fa-735c736d5b29)

Podemos correr el contenedor para asegurarnos de que está bien configurada la imagen con el comando `docker run -p 80:80 <NOMBREIMAGEN:TAG>`, la bandera -p seguida de 80:80 nos ayuda a bindear los puertos del contenedor.

Ya contábamos con un registry en DigitalOcean por lo que a continuación, por lo que necesitábamos renombrarla para que apunte a nuestro registro de imágenes en DigitalOcean, utilizando
```shell
docker tag <NOMBRE DE LA IMAGEN LOCAL> registry.digitalocean.com/<NOMBRE DEL REGISTRO>/<NOMBRE DE LA IMAGEN EN D.O.>
```
Es necesario autenticarse en el registro de imágenes con `doctl registry login`

Una vez hecho eso, subimos la imagen con
```shell
docker push registry.digitalocean.com/<NOMBRE DEL REGISTRO>/<NOMBRE DE LA IMAGEN EN D.O.>
```
Utilizamos el comando para obtener los manifiestos de las imágenes almacenadas. Estos manifiestos contienen información sobre las imágenes y sus configuraciones relacionadas.
```shell
  doctl registry kubernetes-manifest | kubectl apply -f -
```
Cada manifiesto contiene información acerda del deploy por kubernetes

Creamos el deploy desde `kubectl` desde la imagen a la que le hicimos `push`

```shell
kubectl create deployment flask-app-filter --image=registry.digitalocean.com/<REGISTRO>/<NOMBRE IMAGEN>
```
Verificamos que tengramos un solo pod creado con `kubectl get pods`
![image](https://github.com/lissethamc/RandomFilterGen/assets/33168405/c787fae3-69f3-4c2a-9f6b-d745f18eedf2)

Para poder aplicar un balanceador de cargas creamos 4 replicas con el siguiente comando

```shell
kubectl scale deployment/flask-app-filter --replicas=4
```
![image](https://github.com/lissethamc/RandomFilterGen/assets/33168405/3e77c767-db7e-4e34-b0f9-9690c41957c3

Y configuramos el balanceador de cargas con el siguiente comando

```shell
kubectl expose deployment flask-app-filter --type=LoadBalancer --port=80 --target-port=80
```
Debemos esperar un rato a que termine de configurar las IPs, pero después podemos ver la lista de balanceadores de cargas
```shell
doctl compute load-balancer list --format Name,Created,IP,Status
```
![image](https://github.com/lissethamc/RandomFilterGen/assets/33168405/c50f8dca-fb76-466d-880a-68d28e8ce7f4)

Podemos ver la información de los servicios, siendo el balanceador de cargas uno de ellos con `kubectl get services`
![image](https://github.com/lissethamc/RandomFilterGen/assets/33168405/aac75554-c8ed-4b1a-8bfa-9f832a8ea149)

Para el monitoreo de la ServiceMesh se usa kiali, podemos entrar a ella con istio
![image](https://github.com/lissethamc/RandomFilterGen/assets/33168405/f0c789f6-8963-4f13-9885-aa304a059326), nos pedirá un token que obtenemos con el comando
```shell
kubectl exec $(kubectl get pod -n istio-system -l app=kiali -o jsonpath='{.items[0].metadata.name}') -n istio-system -- cat /var/run/secrets/kubernetes.io/serviceaccount/token
```

Donde podemos ver el tráfico
![image](https://github.com/lissethamc/RandomFilterGen/assets/33168405/d029c9f2-2357-4141-826f-ecceb941ec86)

