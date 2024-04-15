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

docler images --no-trunc

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
