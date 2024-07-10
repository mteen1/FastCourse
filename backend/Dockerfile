# BASE
FROM python:3.12.2-bullseye as base

# DEVELOPMENT
FROM base as development
ENV \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    VIRTUAL_ENV=/fast-env
ENV \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1 \
    POETRY_VERSION=1.8.3

# Install Poetry
RUN pip install "poetry==$POETRY_VERSION"
# Copy requirements
COPY poetry.lock pyproject.toml ./

# Add venv to path 
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install python packages
RUN python -m venv $VIRTUAL_ENV \
    && . $VIRTUAL_ENV/bin/activate \
    && poetry install --no-root

WORKDIR /code/


# BUILDER
FROM development as builder
WORKDIR /code/
COPY . . 
RUN poetry install --without dev
# Export build
RUN poetry build --format wheel

# PRODUCTION
FROM base as production
WORKDIR /code/ 
COPY --from=builder /code/dist/*.whl ./
RUN pip install ./*.whl
RUN rm ./*.whl
