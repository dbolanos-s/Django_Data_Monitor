# Progreso - Guía 24

## Completado hasta antes de `pip install requests`

- [x] Estructura preparada para el repositorio `django_data_monitor`.
- [x] `README.md` con título y objetivo.
- [x] `.gitignore` para Python/Django.
- [x] Carpetas `static/` y `templates/dashboard/`.
- [x] Proyecto Django `backend_analytics_server` en la raíz.
- [x] Aplicación `dashboard`.
- [x] `dashboard` registrada en `INSTALLED_APPS`.
- [x] `dashboard` registrada en la ruta raíz (`/`).
- [x] Plantilla `templates/dashboard/base.html`.
- [x] Configuración de `TEMPLATES[0]["DIRS"]`.
- [x] Configuración de `STATICFILES_DIRS`.
- [x] Uso de `{% load static %}` y `{% static ... %}`.
- [x] Vista principal que renderiza `dashboard/base.html` mediante SSR.
- [x] Archivos estáticos locales en `static/assets/`.

## No realizado intencionalmente

La guía se detuvo antes de esta instrucción:

```bash
pip install requests
```

Por tanto aún **no** se implementó:

- `requests`.
- Consumo de APIs externas.
- Herencia de plantillas (`{% extends %}` / `{% block %}`).
- Fragmentos (`{% include %}`).
- Datos de API en el contexto SSR.
- `requirements.txt` final de esta guía.
- Pull request remoto de este nuevo repositorio.

## Pasos que requieren tu entorno/cuenta

1. Crear el repositorio remoto `django_data_monitor` en GitHub.
2. Crear/usar una rama de desarrollo.
3. Crear el entorno virtual `env`.
4. Instalar Django dentro de ese entorno.
5. Ejecutar `python manage.py migrate` y `python manage.py runserver` para comprobar la URL raíz.
