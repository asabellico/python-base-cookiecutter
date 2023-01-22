import os
import sys
import shutil

REMOVE_PATHS = [
    '{% if cookiecutter.use_rest == "n" %} {{cookiecutter.project_slug}}/api {% endif %}',
    '{% if cookiecutter.use_rest == "n" %} tests/unit/test_api.py {% endif %}',
    '{% if cookiecutter.use_rest == "n"  and cookiecutter.use_elk == "n" and cookiecutter.use_message_broker == "None" %} docker-compose.yml {% endif %}',
    '{% if cookiecutter.use_rest == "n"  and cookiecutter.use_elk == "n" and cookiecutter.use_message_broker == "None" %} .env {% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)