from pathlib import Path

import pytest
from PySide6.QtWidgets import QFileDialog

from markdown_reader.app import MarkdownWindow


@pytest.fixture
def window(qtbot, monkeypatch):
    monkeypatch.setattr(MarkdownWindow, "_restore_settings", lambda self: None)
    widget = MarkdownWindow()
    qtbot.addWidget(widget)
    return widget


def test_open_renders_markdown(window, tmp_path):
    source = tmp_path / "hello.md"
    source.write_text("# Hello\n\nThis is **bold**.", encoding="utf-8")

    assert window.open_path(source)

    assert window.current_path == source.resolve()
    assert window.editor.toPlainText().startswith("# Hello")
    assert "Hello" in window.preview.toPlainText()
    assert "bold" in window.preview.toPlainText()
    assert not window.dirty


def test_edit_marks_dirty_and_save_writes_utf8(window, tmp_path):
    source = tmp_path / "notes.md"
    source.write_text("Original", encoding="utf-8")
    window.open_path(source)

    window.editor.setPlainText("Changed — café")
    assert window.dirty
    assert window.save()

    assert source.read_text(encoding="utf-8") == "Changed — café"
    assert not window.dirty


def test_save_as_adds_markdown_extension(window, tmp_path, monkeypatch):
    destination = tmp_path / "new-document"
    monkeypatch.setattr(
        QFileDialog,
        "getSaveFileName",
        lambda *args, **kwargs: (str(destination), "Markdown files (*.md)"),
    )
    window.new_document()
    window.editor.setPlainText("# New")

    assert window.save_as()
    assert destination.with_suffix(".md").read_text(encoding="utf-8") == "# New"


def test_view_modes_and_zoom(window):
    window.set_view("preview")
    assert not window.editor.isVisible()
    window.set_view("editor")
    assert not window.preview.isVisible()
    window.set_view("split")

    window.zoom_in()
    assert window._preview_zoom == 1
    window.zoom_reset()
    assert window._preview_zoom == 0


def test_pdf_export_creates_nonempty_file(window, tmp_path, monkeypatch):
    source = tmp_path / "report.md"
    output = tmp_path / "report.pdf"
    source.write_text("# Report\n\nPDF body.", encoding="utf-8")
    window.open_path(source)
    monkeypatch.setattr(
        QFileDialog,
        "getSaveFileName",
        lambda *args, **kwargs: (str(output), "PDF files (*.pdf)"),
    )

    window.export_pdf()

    assert output.exists()
    assert output.stat().st_size > 100
    assert output.read_bytes().startswith(b"%PDF")
