# locust-csv-to-junit-xml

Simple program to convert [locust.io](https://locust.io) csv output into [JUnit](https://junit.org) XML. Use this to convert the output into pipelines like Azure DevOps or Jenkins.

## Sample usage

```bash
python main.py -p <prefix>
```

## Development

### Requirements

* [pyenv](https://github.com/pyenv/pyenv#getting-pyenv)

### Running on Host OS

Install the necessary Python version and virtual environment:

```bash
./dev.sh
```

Activate the virtual environment in order to run the right Python version:

```bash
. venv/bin/activate
```

Installing Python package dependencies requires updates to the `pyproject.toml`, and then re-generating `requirements.txt`:

```bash
pip-compile --extra=dev --output-file=requirements.txt pyproject.toml
```

Syncing the virtual environment's packages:

```bash
pip-sync
```

### Running in Docker

```bash
docker build -t locust-csv-to-junit .
```
