#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

#SHOPIFY_API_KEY=fc2962ce1305cfdce9b236b95bf505e8
#SHOPIFY_API_SECRET=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
#SHOPIFY_API_KEY=80bfae12da3708eb70710aadd51c28e2
#SHOPIFY_API_SECRET=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

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopify_django_app.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
