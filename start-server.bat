@echo off
title YouTube 챕터 생성기 서버

echo.
echo ========================================
echo   YouTube 챕터 생성기 로컬 서버 시작
echo ========================================
echo.

REM Check if youtube-transcript-api is installed
pip show youtube-transcript-api >nul 2>&1
if errorlevel 1 (
    echo 📦 youtube-transcript-api 설치 중...
    pip install youtube-transcript-api
    echo.
)

echo 🚀 서버 시작 중...
echo.
python server.py

pause
