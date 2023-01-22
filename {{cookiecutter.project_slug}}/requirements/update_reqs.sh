# pip install pip-tools

REQS_DIR=$(cd -- "$(dirname -- ${BASH_SOURCE[0]})" && pwd)
pip-compile --resolver=backtracking --output-file=$REQS_DIR/prod.txt $REQS_DIR/base.in
pip-compile --resolver=backtracking --output-file=$REQS_DIR/dev.txt $REQS_DIR/dev.in
