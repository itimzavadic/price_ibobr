"""
Точка входа для uvicorn: `uvicorn main:app --reload`
"""
from fastapi_app import app

__all__ = ["app"]
