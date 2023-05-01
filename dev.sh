#!/bin/bash

SCRIPT_DIR=$(dirname $0)
VENV_NAME="venv"
VENV_DIR="${SCRIPT_DIR}/${VENV_NAME}"

help() {
  echo "Run \`. ${VENV_DIR}/bin/activate\` to activate"
}

if [ -d "${VENV_DIR}" ]
then
  echo "${VENV_DIR} already exists."
  help
  exit 1
fi

echo "Initializing venv: ${VENV_DIR}"
pyenv install
pyenv local
python -m venv "${VENV_NAME}"
. "${VENV_DIR}/bin/activate"
pip install pip-tools
help
