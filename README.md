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

