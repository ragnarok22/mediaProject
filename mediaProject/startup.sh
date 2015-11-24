#! /usr/bin/bash
echo montando server de la pagina The Wall

port=$(zenity --forms --add-entry=puerto)
python3 manage.py runserver 0.0.0.0:$port

