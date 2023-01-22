import os
from setuptools import setup

def parse_requirements(req_path):
    with open(req_path) as fp:
        content = fp.read()

    reqs = []
    for _line in content.split('\n'):
        line = _line.strip()
        if not line:
            continue

        if line.startswith('#'):
            continue
        if line.startswith('-'):
            continue

        reqs.append(line)
    return reqs

lib_folder = os.path.dirname(os.path.realpath(__file__))
base_requirement_path = os.path.join(lib_folder, 'requirements/base.in')
base_reqs = parse_requirements(base_requirement_path)

dev_requirement_path = os.path.join(lib_folder, 'requirements/dev.in')
dev_reqs = parse_requirements(dev_requirement_path)

setup(
    install_requires=base_reqs,
    extras_require={"dev": dev_reqs},
)
