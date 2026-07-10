@echo off
cd /d "%~dp0"
call uv sync --extra dev
if errorlevel 1 pause & exit /b 1
call uv run pyinstaller --noconfirm --clean --windowed --name "Markdown Reader" --paths src src\markdown_reader\app.py
if errorlevel 1 pause & exit /b 1
echo.
echo Built: %CD%\dist\Markdown Reader\Markdown Reader.exe
pause
