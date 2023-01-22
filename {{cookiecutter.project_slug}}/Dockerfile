## {{cookiecutter.project_slug}} base image
FROM {{cookiecutter.base_image}} as base

# ENV TZ=Europe/Rome

# install system packages deps
# RUN apt-get update
#     && apt-get install -y <APT PACKAGE DEPS HERE>

# Copy app
WORKDIR /app/
COPY .. /app

# Create virtual env
ENV PIP_FORMAT=legacy
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE=1
RUN python3 -m venv $VIRTUAL_ENV

# Create unprivileged user
RUN groupadd --non-unique --gid 1000 {{cookiecutter.project_slug}} && yes | adduser --disabled-password --uid 1000 --gid 1000 {{cookiecutter.project_slug}} \
    && chown -R {{cookiecutter.project_slug}}:{{cookiecutter.project_slug}} /app ${VIRTUAL_ENV}

USER {{cookiecutter.project_slug}}

# Install package requirements in virtual env
RUN $VIRTUAL_ENV/bin/pip install -r requirements/prod.txt

FROM base AS dev
USER root
RUN apt-get update && apt-get install -y git net-tools curl wget locales locales-all

USER {{cookiecutter.project_slug}}
RUN $VIRTUAL_ENV/bin/pip install -r requirements/dev.txt \
    && $VIRTUAL_ENV/bin/pip install -e .


{% if cookiecutter.use_rest == 'y' -%}
## api image
FROM base AS api
ENTRYPOINT ["uvicorn", "{{cookiecutter.project_slug}}.api.app:app", "--host", "0.0.0.0", "--port", "8000"]
{%- endif %}

