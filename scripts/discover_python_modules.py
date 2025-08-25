#!/usr/bin/env python3
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS_API = ROOT / "docs" / "api.md"


def discover_python_packages(root: Path) -> list[str]:
    candidates: list[Path] = []
    # Prefer src/ layout if present
    src = root / "src"
    if src.exists():
        candidates.append(src)
    # Also consider repository root for flat-layout projects
    candidates.append(root)

    discovered: set[str] = set()
    for base in candidates:
        for dirpath, dirnames, filenames in os.walk(base):
            path = Path(dirpath)
            # Skip hidden and typical non-source directories
            parts = set(path.parts)
            if any(p.startswith(".") for p in parts) or {".venv", "venv", "docs", "site", "node_modules", "__pycache__"} & parts:
                continue
            if "__init__.py" in filenames:
                # Build module path from base
                module = ".".join(path.relative_to(base).parts)
                if module:
                    discovered.add(module)
            for fname in filenames:
                if fname.endswith(".py") and fname != "__init__.py":
                    mod = ".".join(Path(fname).with_suffix("").parts)
                    pkg = ".".join(path.relative_to(base).parts)
                    dotted = f"{pkg}.{mod}" if pkg else mod
                    if dotted:
                        discovered.add(dotted)
    # Filter obvious non-package file names
    return sorted(m for m in discovered if re.match(r"^[A-Za-z_][A-Za-z0-9_\.]*$", m))


def render_api(md_modules: list[str]) -> str:
    lines: list[str] = []
    lines.append("## API Reference\n")
    lines.append("This page is generated from source code via mkdocstrings.\n\n")
    lines.append("<!-- BEGIN-AUTO-API -->\n")
    if not md_modules:
        lines.append("No Python modules discovered yet. Add modules under `src/` or project root.\n\n")
    for module in md_modules:
        lines.append(f"### `{module}`\n\n")
        lines.append(f"::: {module}\n")
        lines.append("\n")
    lines.append("<!-- END-AUTO-API -->\n")
    return "".join(lines)


def main() -> None:
    modules = discover_python_packages(ROOT)
    content = render_api(modules)
    DOCS_API.write_text(content, encoding="utf-8")
    print(f"Discovered {len(modules)} module(s). Wrote {DOCS_API}")


if __name__ == "__main__":
    main()

