## Some commands:

docker build .

## construir apartir del documento docker o dockerfile

docker build -t sitioweb:latest .

## construir apartir del documento docker o dockerfile pero con nombre y tag

docker images

## consultar images de docker existentes

docker rmi -f ##########

## eliminar de forma forazada el docker file pero se tiene que senialar el numero del archivo

docker ps

## para ver los contenedores disponibles/ no aparecen contenedores aunque esten en la version desktop si es que no se estan ejecutando.

docker run

## Ejecutara lo que hicimos en docker desktop ???

docker run -it

## interactivo, si hay algun registro de ngx, o similar que este regresando logs o lo que sea, lo veremos en la terminal

docker run -it -rm

## remove, para remover versioens previas del contenedor ejeutandose

docker run -it -rm -d

## se ejecuta en otro plano para que este listo para ser llamado cuando se requiera sin ser llamada la app de forma fortuita

docker run -it --rm -d -p 8080

## es el puerto, lo que hace es escribir el puerto en el que se comunica con el host, como el 8080, se comunica al contenedor y el contenedor se comunica traves del puerto 8080, es la puerta de entrada a la app

docker run -it =-rm -d -p 8080:80

## puerto por medio del que docker se comunica con la app.

docker run -it --rm -d -p 8080:80 --name web

## nombre del contenedor

docker run -it --rm -d -p 8080:80 --name web sitioweb
docker run -it --rm -d -p 8080:80 --name web sitioweb:01

## para tener dos contenedores operando al mismo tiempo

docker run -it --rm -d -p 8085:80 --name web2 sitioweb:01

## la imagen que quiero hacer contenedor, regresa una respeusta

## confirmar que el archivo se encuentra en exec dentro de docker desktop en la parte de contenederoes, para nevagar en la estructura de los arhcivos de la imagen

## copia de vsc la ruta, en este caso:

/usr/share/nginx/html

## y utilizalo en exec con:

cd /usr/share/nginx/html

## luego aplica ls para ver que archivos existen

## ahora ya lo podemos ver en nuestro sistema local en localhost8080

## no quiere decir que nosotros tengamos nginx, sino que estamos conectados a un contenedor que si lo tiene como imagen.

## gracias a docker run desplegamos nuestra imagen como un docker container.

## Formas alternativas de buscar con Docker

## para buscar todas las imagenes

docker images

## para buscar una imagen en especifico a partir de su nombre y no de su tag

docker images (nombreDeLaImagen)
docker images sitioweb

## para buscar a partir de un tag, luego de un nombre que no importa

docker images --filter=reference='tag'
docker images --filter=reference='\*:01'

## para poner el image ID de una forma mas extendida, el ID real de cada imagen, que sera el mismo si vienen del ismo docker file

docker images --no-trunc

## crear un nuevo tag para alguna de las imagenes en particular

docker image tag sitioweb:latest admin/sitioweb:latest

## eliminar las imagenes, existen 2 opciones.

## eliminar con una etiqueta nueva

docker rmi admin/sitioweb:latest

## states: Untagged:admin/sitioweb:latest

## eliminar imagen o grupo de imagenes, a partir de id

docker rmi tag
docker rmi 652b0fc1f6c6

## forzar eliminacion

docker rmi -f tag
docker rmi -f 652b0fc1f6c6

## da lo mismo que docker image pero para los contenedores, un listado de todos los conetenedores desplegados en el momento

docker ps

## para muchos contenedores desplegados, para visualizarlos se usa

docker ps -a

##

## Recuerda que lo importante de estos comandos es ver el container id

##

## una variable del comenado es, para tener una columna adicional llamada "size", en kb pero el tamanio real al trabajar con el contenedor en docker es distinto y en mb, el tamanio en MB es el tamanio real que se usara cada vez que se ejecute el contenedor

docker ps --size

## para detener los contenedores que en el momento no estoy utilizando, se usa, para gestionar los recursos de docker de una forma mas flexible

docker stop <id>
docker stop a46e50b77d37

##

## Ahora es importante revisar que pasa con docker desktop

##

## para ver el desempenio de tu equipo al desplegar el docker puedes utilizar

docker stats

##

## para volver a tu terminal una vez los stats, puedes utilizar ctr + c

##

## PARA TEMAS DE FLASK

## para instalar python

apt install python3.10-venv

## para crear el entorno

python3 -m venv .venv

## para instalar flask

pip install Flask

## para correr flask

python3 -m flask run

##

## Para desplegar app en contenedor de docker

##

## puede utilizar a docker desktop para saber que imagen utilizaras a partir de la barra de busqueda y viendo la version de tu python con python3 --version y las tags que hay en los resultados de la busqueda

## en el archivo docker file o DockerFile agregar:

FROM python:3.13.0a6-alpine3.18

## para crear el area de trabajo para desplegar todo lo que requiera la aplicacion o el directorio del proyect

## la version mas estandarizada en los proyectos es /app porque varia segun lenguaje

WORKDIR /app

## ahora ya con directorio de trabajo, hay que agarrar del entorno global, el archivo requirement.txt para instalar enpython y para que API trabaje de maravilla. copiar de entorno local a docker

COPY requirements.txt requirements.txt

## despue se utiliza el comando run para ejecutar un comando dentro del contenedor para que la instalacion se quede completammente lista

RUN pip install -r requirements.txt

## para pasar el contenido de todo el directorio a /app

COPY . .

## las instrucciones se crean en sucuencia, se tienen que poner las instrucciones en orden

## Poner comando pero en modo lista, para tener dockerfile listo para una imagen de python con api para tener un contenedor.

## es importante que aclarar que las palabras reservadas y secuencias sirven para cualquier proyecto, como para despliegues de infraestructura y base de datos, sin iimprotar la tecnologia, lplataforma, del docker file, se usarn las palabras en todos los proyecto

## de las mejorares caracteristicas de docker son sus volumenes, son espacios compartidos entre equipo local y contenedor de docker, no imagen, es algo que ya se esta ejecutando, se tiene una especie de carpeta cmpartida, o unidad de disco compartido, un puente de comunicacion de datos, entre contendedor y equipo lcoal, escenarios hay muchos, para acutalizar un sitio web mientras contenedor se ejecuta, puedes utilizar el vilumne para actualizar el sitio, para analisis de datos, el volumen es importante para tuliazar las bases de datos mientras el contenedor se acutaliza, un escenario es

## comando inicial para el proyecto de sustitucion de imagenes (el parametro de volumen esta fijado, por eso se puede utilizar ese comando)

docker run -it --rm -d -p 8080:80 -v ./sitio:/usr/share/nginx/html/sitio --name web nginx

## ejecutar comando para ir a contenedor deseado dentro de docker desktop

cd usr/share/nginx/html/sitio

ls

cd assets

ls

## la diferencia entre una copia y crear un volumen de docker consiste en que copy produce cambios permanentes, mientras que un volumen genera un cambio temporal, hay escenarios para cada palabrar reservda

## sitio es el origen, la siguiente ruta es el destino

VOLUME [ "/sitio", "/usr/share/nginx/html" ]

## dependiendo del escenario podras elegir entre copy y volume, y lo importante es que sea la mas conveniente

## para inspeccionar el contenedor que utilizamos a traves de un archivo json, el que mas interesa es la seccion Networks, pero tambiien vienen los puertos

## para hacer modificaciones, primero tenemos que detener el docker

docker stop web

## ahora haremos una mdoificacion a la ip, asi se puede asignar una ip para cad auno de los contenedores y asi se podra orquestar sin ningun problema, si no se asigna una ip en eel comenda, se adsigna de manera interna, para que no haya un clocnlficto de comandos en la red de docker

docker run -it --rm -d -p 127.0.0.1:8080:80 --name web nginx

## bridge, genera un enlace entre cualquier entorno y el entorno de docker, y la mejor forma de explorarlo explroar las redes es

docker network ls

## existe conexiones tipo bridge, host y none, bridge es la conxion tradicional entre contenedores, el host es una conexion entre dos contenedores y none es aquella que desea que no haya conexiones en la red. y se pueden hacer bridges personalizados, donde se puede interactuar de forma personalizada.

## para crear un puente o red en docker se hace

docker network create platzinet

## eso fue hacer una segmentacion de redes, para crear un precepto de minimo acceso, para que solo accedan a los contenedores que estrictamente necesitan, y evitar que accedan a los que no.

## ahora trabajaremos con docker hub para compartir proyectos en la nube

## lo primero que hay que hacer es hacer login via terminal de comando o desde docker desktop

docker login

## y luego ingresar login y password

## para compartir proyectos productivos o en desarrollo con equipos de trabajo

## ahora con trabajaremos con la imagen para poderlo desplegar en docker hub

docker build -t <nombreDeUsuario>/<nombrededespliege>:<version> .
docker build -t dr1602/linktree:latest .

## con esto lo crearemos con la tag correcta a publicar, con esto docker sabe a que cuenta de usuario publicar imagen y validara que sea la misma cuenta, al crear la imagen se valida con

docker images

## lo identificas con el nombre del repo, una vez que validaz que son correctos, aplicas

docker push <nombreDeUsuario>/<nombredeproyecto>:<version>
docker push dr1602/linktree:latest

## una vez publicado se puede volver a docker hub para comprobar que esta publicado, ver que ya es una imagen compartida.

## para descargar la imagen remota del docker, dentro de mi cuenta en mi entorno local, lo que se necesatria hacer es

## los parametros utilizados no varian entre una imagen local y una imagen que aun no se tiene en el equipo.

## hoy en dia al descargar una imagen de docker hub, no hay una forma de saber en que puerto esta corriendo dicha imagen descargada, para crear una imagen publica hay que crear una explicacion publica sobre que funcion hace tu imagen para que el usuario no tenga que adivinar.

## para saber como funciona docker: 1. correr docker, 2. correr docker ps, 3. verificar la columna command, si ese archivo deja de funcionar, el contenedor deja de funcionar.

## podemos emular ese archivo con:

/bin/bash

docker run --name dr1602 --rm -it -p 8080:80 dr1602/linktree:latest /bin/bash

## pero no se corre de forma normal, por lo cual se tiene que forzar a un exit.

## tienes que ejectuar este codigo para volver al normalidad

exit

## bash es una terminal de linux per hay mas posibildiades como sh

## ahora vamos a inspeccionar que viene en el contenedor

docker run --name dr1602 --rm -it -p 8080:80 dr1602/linktree:latest /bin/bash

## con

docker ps

## y docker inspect

## pueden existir casos en los que no puedas compartir imagenes por restricciones de red, o que no las puedas compartir por el ancho de banda de tu red, y por ello se tenga que hacer por una unidad extraible, existen 2 comandos para poderlo lograr, save y export y docker load e import para cargarlo.

## para exportar a archivo comprimido

docker save <archivoAExportar> > <nombreYTipoDeaArchivo>
docker save dr1602/linktree > linktree.rar

## verificar con ls que exista archivo

## el archivo, al seleccionarlo, puede contener varias versiones del archivo que se esta seleccionando y un archivo manifest.json, con enorme cantidad de layers. tag que rerpesenta una version previa de la imagen, como agrear librearias o instruccion, lo que crea una nueva capa o version que se acumula en layers, es un historial de versiones.x

## para extraer archivo, usamos:

docker load --input linktree.rar

## y lo puedes verificar tanto en docker desktop como en docker images
