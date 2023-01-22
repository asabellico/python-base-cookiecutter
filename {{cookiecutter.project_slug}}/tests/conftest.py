import pytest  # noqa: F401
{% if cookiecutter.use_message_broker == 'RabbitMQ' -%}
from pifpaf.drivers import rabbitmq
{%- endif %}
{% if cookiecutter.use_message_broker == 'Redis' -%}
from pifpaf.drivers import redis
{%- endif %}
{% if cookiecutter.use_rest == 'y' -%}
from starlette.testclient import TestClient
from {{cookiecutter.project_slug}}.api import app as api_app
{%- endif %}


{% if cookiecutter.use_message_broker == 'RabbitMQ' -%}
@pytest.fixture(scope="session")
def rmq_pifpaf():
    rmq_server = rabbitmq.RabbitMQDriver(port=5672)
    rmq_server.setUp()
    yield rmq_server
    rmq_server.cleanUp()

{%- endif %}
{% if cookiecutter.use_message_broker == 'Redis' -%}
@pytest.fixture(scope="session")
def redis_pifpaf():
    redis_server = redis.RedisDriver(port=6379)
    redis_server.setUp()
    yield redis_server
    redis_server.cleanUp()

{%- endif %}
{% if cookiecutter.use_rest == 'y' -%}
@pytest.fixture(scope="module")
def api_client():
    yield TestClient(api_app)

{%- endif %}

def pytest_logger_config(logger_config):
    logger_config.add_loggers(["{{cookiecutter.project_slug}}"], stdout_level="debug")
    logger_config.set_log_option_default("{{cookiecutter.project_slug}}")
