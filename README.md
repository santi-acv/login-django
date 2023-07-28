# Inicio de sesión con cURL en Django

## Documentación de la API

### Página de inicio

Este comando permite acceder a la página de inicio del servidor. Si el usuario
aún no ha iniciado sesión, recibirá un mensaje indicándolo. Si ya lo ha hecho,
recibirá un saludo con su nombre.

```
curl -b ./cookies -c ./cookies http://127.0.0.1:8000/
```


### Iniciar sesión

Para iniciar sesión, utilize el siguiente comando. Recuerde reemplazar la
cadena ```username:password``` con su nombre de usuario y contraseña. También
puede omitir la contraseña y escribir solamente el nombre de usuario, lo cual
hará que cURL solicite la contraseña.

```
curl -b ./cookies -c ./cookies http://127.0.0.1:8000/login -u username:password
```

### Cerrar sesión

El siguiente comando finaliza la sesión actual.

```
curl -b ./cookies -c ./cookies http://127.0.0.1:8000/logout
```
