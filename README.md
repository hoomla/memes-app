# Aplicación de ejemplo para demostrar cómo trabajar con GitHub Copilot

Este repositorio es utilizado como ejemplo para demotrar cómo podemos sacar el mayor provecho a día de hoy a GitHub Copilot, una herramienta de inteligencia artificial que ayuda a los desarrolladores a escribir código más rápido y con mayor precisión.

# FastAPI como framework web

Para poder demostrar las capacidades de GitHub Copilot, hemos decidido utilizar FastAPI como framework web. FastAPI es un framework moderno y rápido para construir APIs con Python 3.7+ basado en las anotaciones de tipos estándar de Python. Tiene un tutorial muy completo que puedes seguir paso a paso para entender el código aquí incluido: https://fastapi.tiangolo.com/tutorial/

Crea un virtual environment:

```shell
python -m venv .venv
```

y luego instala las dependencias:

```shell
pip3 install -r requirements.txt
```


Para ejecutar este código solamente tienes que escribir en el terminal

```shell
fastapi dev main.py
```

Lo chulo es que simplemente con este comando ya puedes ir a

- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc
- http://127.0.0.1:8000/openapi.json


Me quedé aquí: https://fastapi.tiangolo.com/tutorial/extra-models/