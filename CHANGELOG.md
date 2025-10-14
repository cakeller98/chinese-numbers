# Changelog


All notable changes to this project will be documented in this file.

## How to use this changelog
- Add a new section for each release or major update, using a heading like `## [1.0.0] - 2025-07-02`.
- List added, changed, fixed, and removed items as bullet points under each version.
- Use `[Unreleased]` for changes not yet released.
- Newest releases should be at the top of the file just after these instructions.

---
## [Release Candidate] - 2025-10-14
- First published to github.

## [Unreleased.2] - 2025-10-14
- Refactored for use with poetry.
- Added more edge cases to the test suite.
- Improved documentation for better clarity.
- Restructured the project to be used as a module, not just a proof of concept script.
- Added the pytest testing as the main way to ensure that the code works as expected.
- Added src/example.py as a runnable script and added it to the pyproject.toml as a console script entry point.

## [Unreleased.1] - 2025-10-10
- Project initialization and initial research on number conversion.
- Created initial project structure and configuration files.
- Established testing framework and wrote initial tests.
- Compiled the list of edge cases for number conversion to ensure that the implementation handles all scenarios correctly.