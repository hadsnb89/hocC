## Project Overview

Welcome to the documentation site. This site contains:

- Usage instructions to get started
- Realistic examples for common tasks
- A comprehensive, auto-generated API reference

If you add Python packages/modules under `src/` or the repository root, the API page will populate automatically via mkdocstrings after running the generation script.

### Quick Start

1. Ensure Python 3.8+ is installed
2. Install docs tooling: `pip install mkdocs mkdocs-material mkdocstrings[python]`
3. Generate API page: `python scripts/discover_python_modules.py`
4. Serve docs locally: `mkdocs serve`
5. Build static site: `mkdocs build`
