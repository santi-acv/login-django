# Inicio de sesión con cURL en Django

## Arquitectura

El proyecto usa una arquitectura de 3 capas, las cuales consisten en>

1. Servidor HTTP Guniconr
2. Framework back end Django
3. Base de datos PostgreSQL

## Requerimientos

* Python >= 3.8
* PostgreSQL >= 12

## Instalación

En primer lugar, verifique que los siguientes paquetes se encuentren instalados.

```
sudo apt install python3-venv postgresql libpq-dev curl
```

Luego, ejecute ambos comandos. El primero requiere permisos de administrador debido a que creará un usuario y una base de datos para el proyecto. El segundo creará un ambiente virtual con las dependencias necesarias.
```
sudo -u postgres psql < init_db.sql
./setup.sh
```

Para ejecutar el servidor, utilice los siguientes comandos.
```
cd project
gunicorn project.wsgi:application
```


## Documentación de la API

### Página de inicio

Este comando permite acceder a la página de inicio del servidor. Si el usuario aún no ha iniciado sesión, recibirá un mensaje indicándolo. Si ya lo ha hecho, recibirá un saludo, su nombre de usuario y su última fecha de conexión.

```
curl -b ./cookies -c ./cookies http://127.0.0.1:8000/
```

### Registrarse

Si aún no tiene una cuenta, deberá crear una utilizando el siguiente comando. Debe reemplazar la cadena `username:password` con su nombre de usuario y contraseña. También puede omitir la contraseña y escribir solamente el nombre de usuario, lo cual hará que cURL solicite la contraseña.

```
curl -b ./cookies -c ./cookies http://127.0.0.1:8000/register -u username:password
```

### Iniciar sesión

El comando para iniciar sesión es muy similar. No olvide reemplazar la cadena ```username:password``` con su nombre de usuario y contraseña, aunque al igual que con el comando anterior, puede omitir la contraseñá.

```
curl -b ./cookies -c ./cookies http://127.0.0.1:8000/login -u username:password
```

### Cerrar sesión

Por último, si desea finalizar su sesión, puede usar el siguiente comando.

```
curl -b ./cookies -c ./cookies http://127.0.0.1:8000/logout
```
