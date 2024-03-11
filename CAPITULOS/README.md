# CAPITULO I
REALIZADO

# CAPITULO II

# COMANDOS DOCKER
## Iniciales del proyecto

### Crear las imagenes 

docker-compose -f .\local.yml build

![] (CAPITULOS/img/2.build.png)

### Levantar el servicio

docker-compose -f .\local.yml up

![] (CAPITULOS/img/2.up.png)

![] (CAPITULOS/img/2.prueba.png)

## Otros

### Muestra los servicios
docker-compose -f local.yml ps

![] (CAPITULOS/img/2.Servicios.png)

### Matar Servicios
docker-compose -f local.yml down

### Exportar local.yml
export COMPOSE_FILE=local.yml

## Comandos Administrativos
<rm para matar el contenedor al terminar el comando>

docker- compose run --rm django COMMAND

### Crear super usuario administrador
docker-compose run --rm django python manage.py createsuperuser
docker-compose -f local.yml run --rm django python manage.py createsuperuser

![] (CAPITULOS/img/2.user.png)

![] (CAPITULOS/img/2.ingreso.png)

## Habilitar debugger

docker-compose -f local.yml up
docker-compose -f local.yml ps

docker-compose rm -f<ID>
docker-compose rm -f cride_django_1_cbb7cab2669f

docker-compose run --rm --service-ports django
