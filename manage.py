#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""

    print("""
        |*******************Select Setting Module*********************|
        |=============================================================|
        ||| 1. Local DEV                                           ||||
        ||| 2. Oracle DEV                                          ||||
        ||| 3. Oracle Production                                   |||| 
        |=============================================================|
        |*************************************************************|
    """)
    number = input()
    if number not in ["1", "2", "3"] or number.isspace():
        print("Please select module")
        exit()

    dic = {"1": "django_real_estate_map.config.settings.debug",
           "2": "django_real_estate_map.config.settings.oci_dev",
           "3": "django_real_estate_map.config.settings.production"}

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', dic[number])
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
