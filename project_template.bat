@echo off


echo ****************************************
echo Upgrading pip
py -m pip install --upgrade pip

echo ****************************************
echo Installing wheel
pip install wheel

echo ****************************************
echo Installing package streamlit
pip install streamlit

echo ****************************************
echo end of scripts
echo Written by Fazleali Pirbhai
echo ****************************************
