# WWWURF Project Generator

A powerful CLI tool for generating structured multi-package Python projects using Poetry.

## Features

- 🎯 Creates a structured multi-package Python project
- 📦 Generates package scaffolding with Poetry configuration
- 🧪 Includes testing setup with pytest
- 🔄 Git initialization
- 🛠️ Management script for adding new packages
- 🎨 Modern project structure following best practices

## Installation

```bash
pip install wwwurf-project-generator
```

## Quick Start

Create a new project with default settings:
```bash
wwwurf-gen create my-project
```

Create a project with multiple packages:
```bash
wwwurf-gen create my-project --packages core api database utils
```

Add a new package to an existing project:
```bash
cd my-project
wwwurf-gen add-package new-package
```

## Project Structure

The generated project will have the following structure:

```
my-project/
├── main_app/              # Main application package
│   ├── __init__.py
│   └── main.py           # Application entry point
├── packages/             # Individual packages directory
│   ├── core/            # Core package
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── main.py
│   │   │   └── utils/
│   │   ├── tests/
│   │   ├── pyproject.toml
│   │   └── README.md
│   └── [other-packages]/
├── pyproject.toml       # Root project configuration
├── README.md           # Project documentation
├── .gitignore         # Git ignore configuration
└── manage.py          # Project management script
```

## Package Features

Each generated package includes:

- 📝 Individual `pyproject.toml` for package-specific configuration
- 🧪 Pre-configured test directory with pytest
- 📚 Package-specific README
- 🔧 Utils directory for common functionality
- ⚙️ Poetry scripts for easy execution

## Development Workflow

### Creating a New Project

1. Generate the project structure:
```bash
wwwurf-gen create my-project --packages core api
```

2. Install dependencies:
```bash
cd my-project
poetry install
```

3. Run the application:
```bash
poetry run python -m main_app.main
```

### Adding New Packages

1. Generate new package structure:
```bash
./manage.py add-package new-package
```

2. Install the new package:
```bash
cd packages/new-package
poetry install
cd ../..
poetry install
```

### Running Tests

Each package can be tested individually:
```bash
cd packages/core
poetry run pytest
```

Or test the entire project:
```bash
poetry run pytest
```

## Contributing

1. Fork the repository
2. Create your feature branch:
```bash
git checkout -b feature/amazing-feature
```

3. Install development dependencies:
```bash
poetry install
```

4. Make your changes and ensure tests pass:
```bash
poetry run pytest
poetry run black .
poetry run isort .
poetry run flake8 .
```

5. Commit your changes:
```bash
git commit -m 'Add amazing feature'
```

6. Push to the branch:
```bash
git push origin feature/amazing-feature
```

7. Open a Pull Request

## Release Process

1. Update version in `pyproject.toml`
2. Create and push a new tag:
```bash
git tag v0.1.0
git push origin v0.1.0
```

The GitHub Actions workflow will automatically:
- Run tests across multiple Python versions
- Check code formatting and linting
- Build and publish to PyPI (for tagged releases)

## Configuration

### Package Configuration

Each package's `pyproject.toml` can be customized with:
- Dependencies
- Development dependencies
- Build settings
- Entry points
- Package metadata

Example:
```toml
[tool.poetry.dependencies]
python = "^3.9"
requests = "^2.31.0"

[tool.poetry.scripts]
my-command = "package_name.main:main"
```

## Troubleshooting

### Common Issues

1. **Poetry not found**
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. **Package conflicts**
```bash
poetry update
```

3. **Import errors**
Ensure you're in the correct directory and have run `poetry install`

## License

MIT License - see LICENSE file for details.

## Author

WorldWideWurf (worldwidewurf@gmail.com)

## Links

- GitHub: [worldwidewurf/wwwurf-project-generator](https://github.com/worldwidewurf-io/wwwurf-project-generator)
- PyPI: [wwwurf-project-generator](https://pypi.org/project/wwwurf-project-generator/)
