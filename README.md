# Markdown Reader

A small native Windows Markdown reader/editor built with Python and PySide6.

## Run

Double-click `run_markdown_reader.bat`. On the first run it creates a local virtual environment and installs dependencies. You can also run:

```bash
uv sync --extra dev
uv run markdown-reader
```

Open `sample.md` to try it. You can also drag any `.md`, `.markdown`, `.mdown`, or `.mkd` file into the window.

## Features

- Drag-and-drop Markdown files
- Live GitHub-style Markdown preview
- Source editor and preview-only/edit-only/split layouts
- Open, Close, Save, Save As, and recent files
- Export rendered document to PDF
- Zoom in, zoom out, and reset zoom
- Find, undo/redo, clipboard commands, and keyboard shortcuts
- Local image/link paths resolved relative to the Markdown document
- Unsaved-change protection

## Build a standalone Windows EXE

Double-click `build_exe.bat`. The executable will be created at:

`dist\Markdown Reader\Markdown Reader.exe`

The folder produced by PyInstaller is portable; copy the entire `Markdown Reader` folder to another Windows computer.

## Tests

```bash
uv run pytest
```
