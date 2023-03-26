@echo off

set GIT=git\\cmd\\git.exe
set PYTHON=py310\\python.exe

%PYTHON% ChatGLM_local.py

pause
exit /b