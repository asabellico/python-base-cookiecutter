import sys

from {{cookiecutter.project_slug}}.{{cookiecutter.project_slug}} import fib


def main():
    n = int(sys.argv[1])
    print(fib(n))


if __name__ == "__main__":
    sys.exit(main())