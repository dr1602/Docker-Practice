FROM nginx:latest

#jalando el build del servidor , ahora escribir la ruta donde queremos que el sitio html se desplegado o copiado
#ngix es una estrutura basada en linux
# Path: /usr/share/nginx/html
# todos los archivos en esa carpeta gracias al servidor web, se haran istio web

COPY /sitio /usr/share/nginx/html

VOLUME [ "/sitio", "/usr/share/nginx/html" ]