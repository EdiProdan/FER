#!/bin/bash

BGreen='\033[0;32m'  # Green
NC='\033[0m' # No Color

printf "Inicijalizacija programa...\n"
printf "$ ${BGreen}python3${NC} tajnik.py init mAsterPasswrd\n"
python3 tajnik.py init mAsterPasswrd
printf "\n"
printf "Unos novih zapisa...\n"
printf "$ ${BGreen}python3${NC} tajnik.py put mAsterPasswrd www.fer.hr neprobojnAsifrA\n"
python3 tajnik.py put mAsterPasswrd www.fer.hr neprobojnAsifrA
printf "\n"
printf "Dohvat zapisa...\n"
printf "$ ${BGreen}python3${NC} tajnik.py get mAsterPasswrd www.fer.hr\n"
python3 tajnik.py get mAsterPasswrd www.fer.hr
printf "\n"
printf "Dohvat zapisa s pogrešnom lozinkom...\n"
printf "$ ${BGreen}python3${NC} tajnik.py get wrongPasswrd www.fer.hr\n"
python3 tajnik.py get wrongPasswrd www.fer.hr
