## Contributing

Thank you for helping improve this project. This guide explains how to work with the docs and APIs.

### Docs workflow

1. Install tooling:
   - `python3 -m pip install --user mkdocs mkdocs-material mkdocstrings[python]`
2. Generate API page:
   - `python3 scripts/discover_python_modules.py`
3. Preview locally:
   - `python3 -m mkdocs serve`
4. Build static site:
   - `python3 -m mkdocs build`

### Adding/Updating APIs

- Place Python modules under `src/` (recommended) or the repository root.
- Public members (not starting with `_`) are documented automatically by mkdocstrings.
- Re-run `scripts/discover_python_modules.py` after adding new modules.

### Writing examples

- Add end-to-end examples to `docs/examples.md` or create new pages under `docs/` and link them from `mkdocs.yml`.

### Style

- Use Google-style docstrings for functions, classes, and methods.
- Prefer descriptive names and clear parameter/return descriptions.
