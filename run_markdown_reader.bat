@echo off
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo First run: installing Markdown Reader...
  uv sync --extra dev
  if errorlevel 1 pause & exit /b 1
)
start "Markdown Reader" ".venv\Scripts\pythonw.exe" -m markdown_reader.app %*
