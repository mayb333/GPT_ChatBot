#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export PYTHONPATH="${PYTHONPATH}:${DIR}"
source "$DIR/venv/bin/activate"
python ${DIR}/static/start_bot.py