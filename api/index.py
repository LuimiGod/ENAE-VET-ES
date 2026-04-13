"""Entrada serverless para Vercel: reutiliza la misma app que `app.py`.

Sin este fichero, algunos proyectos se despliegan solo como estáticos (sin
runtime Python) y `/` devuelve NOT_FOUND.
"""

from app import app

__all__ = ["app"]
