@echo off

D:

cd "D:\Code\ak\langchain-academy"

echo Launching AKY's app

call .\lc-academy-env\Scripts\activate && streamlit run .\module-1\emailer_ak\app.py

pause