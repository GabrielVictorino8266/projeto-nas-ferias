#!/usr/bin/env python
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto_ferias.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Verifica se a variável PORT está definida (caso esteja, usa-a, caso contrário usa 8000)
    port = os.getenv("PORT", "8000")
    
    # Se estiver rodando localmente (sem a variável PORT definida), a porta será 8000
    if port == "8000":
        execute_from_command_line(["manage.py", "runserver", "127.0.0.1:8000"])
    else:
        execute_from_command_line(["manage.py", "runserver", f"0.0.0.0:{port}"])

if __name__ == '__main__':
    main()
