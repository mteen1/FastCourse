
# FastCourse: Getting Started

## Introduction

FastCourse is a platform for building courses with the power of AI. It utilizes AI for course creation, idea generation, topic selection, and image creation.

## Prerequisites

Before you start, ensure you have the following installed:

- Docker
- Docker Compose
- Python 3.12.2
- Poetry (for managing Python dependencies)

## Setting Up the Development Environment

### Clone the Repository

First, clone the repository to your local machine:

```sh
git clone https://github.com/your-username/fastcourse.git
cd fastcourse
```

### Building the Docker Image

To build the Docker image, use the following command:

```sh
docker-compose up --build
```

This will build the image and start the services defined in your `docker-compose.yml` file.

### Directory Structure

Here's an overview of the project structure:

```sh
.
├── backend
│   ├── alembic.ini
│   ├── Dockerfile
│   ├── docs
│   │   ├── getting_started.md
│   │   └── index.md
│   ├── mkdocs.yml
│   ├── poetry.lock
│   ├── pyproject.toml
│   └── src
│       ├── alembic
│       ├── api
│       │   ├── content_blocks.py
│       │   ├── courses.py
│       │   ├── sections.py
│       │   ├── users.py
│       │   └── utils
│       │       ├── content_blocks.py
│       │       ├── courses.py
│       │       ├── sections.py
│       │       └── users.py
│       ├── db
│       │   ├── db_setup.py
│       │   └── models
│       │       ├── ai_content.py
│       │       ├── course.py
│       │       ├── mixins.py
│       │       └── user.py
│       ├── main.py
│       └── pydantic_schemas
│           ├── content_block.py
│           ├── course.py
│           ├── section.py
│           └── user.py
├── docker-compose.yml
├── frontend
└── makefile 
```

## Running Tests

To run the tests, use the following command:

```sh
pytest
```

## Conclusion

You are now ready to start developing with FastCourse. For any additional information or help, refer to the [documentation](./docs).
