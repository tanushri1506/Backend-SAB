import os
import django
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")  # replace with your settings module
django.setup()

from api.models import Workshops

for w in Workshops.objects.all():
    try:
        json.loads(w.instructors)  # Try parsing JSON
    except Exception:
        print(f"Fixing id={w.id}, old value={w.instructors}")
        # If not valid JSON, convert to JSON array or empty list
        if w.instructors and w.instructors.strip() not in ["null", ""]:
            # Wrap existing string in a list
            new_value = json.dumps([w.instructors])
        else:
            # Empty list if empty or null string
            new_value = json.dumps([])
        w.instructors = new_value
        w.save()

print("Data cleanup done.")
