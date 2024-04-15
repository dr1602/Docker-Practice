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
docker images --filter=reference='*:01'

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
