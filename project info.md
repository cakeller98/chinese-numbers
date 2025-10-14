# Project Structure Overview

---

## Section 1: Bare-Bones Documentation (Minimal Project)

These files are required for a minimal, local Python project:

- `src/` — Source code folder
- `pyproject.toml` — Project metadata and dependency configuration (required by Poetry)
- `.gitignore` — Ensures only relevant files are tracked by git
- `README.md` — Project overview and usage instructions
- `CHANGELOG.md` — Track changes and releases

---

## Section 2: Full-Fledged Project Items

These files and folders are recommended for collaboration, code quality, and best practices, but not strictly required for a minimal project:

- `src/tests/` — All test code (unit, integration, etc. test_<module>.py)
- `license.txt` — Project license (edit as needed)
- `.editorconfig` — Editor settings for consistent code style
- `.env.example` — Template for environment variables
- `.pre-commit-config.yaml` — Pre-commit hooks for code quality
- `CONTRIBUTING.md` — Guidelines for contributing to the project
- `.vscode/` — VS Code settings and tasks (optional; review for secrets/private info)

---

## Section 3: Building an Installable Wheel for PyPI

To make your project installable via PyPI, ensure you have:

- `pyproject.toml` — Must specify project metadata, dependencies, and build system
    - `[tool.poetry]` section with `name`, `version`, `description`, `authors`, `license`, `readme`, and `packages`
    - `[build-system]` section (already present in your template)
- Source code in a subfolder under `src/` (e.g., `src/your_project_name/`)
- `README.md` — Used for PyPI project description
- `license.txt` — Required for open source projects
- (Optional but recommended) `CHANGELOG.md`, `.gitignore`, and tests

**Note:** Poetry handles wheel building automatically if the above are present
