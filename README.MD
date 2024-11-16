En Linux:
Instalar virtualenv (si no lo tienes instalado):

bash

pip install virtualenv
Crear un entorno virtual:

bash

virtualenv venv
Activar el entorno virtual:

bash

source venv/bin/activate
Instalar Flask dentro del entorno virtual:

bash

pip install Flask
Desactivar el entorno virtual (cuando termines):

bash

deactivate
En Windows:
Instalar virtualenv (si no lo tienes instalado):

bash

pip install virtualenv
Crear un entorno virtual:

bash

virtualenv venv
Activar el entorno virtual:

bash

.\venv\Scripts\activate
Instalar Flask dentro del entorno virtual:

bash

pip install Flask
Desactivar el entorno virtual (cuando termines):

bash

deactivate
Resumen de Comandos:
Linux:

Crear entorno: virtualenv venv

Activar entorno: source venv/bin/activate

Desactivar entorno: deactivate

Windows:

Crear entorno: virtualenv venv

Activar entorno: .\venv\Scripts\activate

Desactivar entorno: deactivate

Notas Adicionales:
venv es el nombre del directorio donde se creará el entorno virtual. Puedes cambiarlo por cualquier otro nombre si lo deseas.

Si estás utilizando Python 3.3 o superior, puedes usar el módulo venv incorporado en Python en lugar de virtualenv:

Linux/Windows: python -m venv venv

Activar en Linux: source venv/bin/activate

Activar en Windows: .\venv\Scripts\activate

Una vez que hayas creado y activado el entorno virtual, puedes instalar Flask y otras dependencias sin preocuparte por conflictos con otras versiones de paquetes en tu sistema.