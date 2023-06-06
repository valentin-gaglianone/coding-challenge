# 🚀 Coding Challenge - Python 🐍 
¡Bienvenidos al desafío de Python del curso de [Señales y Sistemas de la UNTREF](https://github.com/maxiyommi/signal-systems)! En este desafío, los alumnos tendrán la oportunidad de demostrar sus habilidades en programación utilizando Python. Cada resultado se subirá a una rama específica en este repositorio.

## Instrucciones 📝
La consigna se encuentra en la carpeta `/consignas` en el notebook con nombre de la fecha del corriente año (Ej:`/consignas/junio_2023.ipynb`)
1. Cada alumno deberá crear una rama nueva con el siguiente formato: <nombre_alumno>-<apellido_alumno>.
    * Por ejemplo: juan-perez
2. Dentro de su rama, cada alumno deberá crear una carpeta con su nombre y apellido en minúsculas separados por guiones bajos.
    * Por ejemplo: juan_perez
3. Dentro de su carpeta personal, los alumnos deben agregar los archivos de su solución (todos los necesarios para reproducir su respuesta).
    * Por ejemplo: ejercicio_1.py

## Estructura del Repositorio 📂
El repositorio tendrá la siguiente estructura:
``` markdown
- master
  - readme.md
- branch <nombre_alumno>-<apellido_alumno>
  - <nombre_alumno>_<apellido_alumno>
    - solucion.py
- ...
```

## Cómo subir tu solución 📤
1. Clona el repositorio a tu máquina local utilizando el comando:
``` bash
git clone <url_del_repositorio>
```
2. Crea una nueva rama utilizando tu nombre y apellido:
``` bash
git checkout -b <nombre_alumno>-<apellido_alumno>
```
3. Crea una carpeta con tu nombre y apellido en minúsculas separados por guiones bajos.
``` bash
mkdir <nombre_alumno>_<apellido_alumno>
```
4. Agrega tu solución dentro de la carpeta personal que creaste.
    * Asegúrate de utilizar el nombre del ejercicio, por ejemplo: ejercicio_1.py.
5. Haz commit de los cambios y empuja tu rama al repositorio remoto.
``` bash
git add .
git commit -m "Agregando solución de <nombre_alumno>"
git push origin <nombre_alumno>-<apellido_alumno>
```

¡Y eso es todo! Tu solución se habrá subido correctamente a tu rama en el repositorio. Recuerda que puedes verificar las soluciones de tus compañeros en las ramas correspondientes.

Buena suerte y diviértete resolviendo el desafío de Python. ¡Esperamos ver tus resultados! Si tienes alguna pregunta, no dudes en comunicarte. 🎉👩‍🏫👨‍🏫