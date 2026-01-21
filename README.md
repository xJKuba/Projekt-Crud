# Projekt-Crud - Todo List

## Opis projektu
Prosta konsolowa aplikacja w Pythonie do zarządzania listą zadań (CRUD: Create, Read, Update, Delete).

## Użyte narzędzia
- Git: Do kontroli wersji, śledzenia zmian.
- Pip: Do zarządzania zależnościami (requirements.txt).
- Makefile: Do automatyzacji (uruchamianie, testy).
- Pytest: Do testów automatycznych.
- Dokumentacja: Ten README.md.

## Instrukcja uruchomienia
1. Sklonuj repo: `git clone https://github.com/xJKuba/Projekt-Crud.git`
2. Wejdź do folderu: `cd Projekt-Crud`
3. Utwórz venv: `python -m venv venv` i aktywuj.
4. Zainstaluj: `make install` lub `pip install -r requirements.txt`
5. Uruchom: `make run` lub `python app.py`

## Instrukcja testowania
Uruchom: `make test` lub `pytest` – sprawdzi 3 testy dla CRUD.

## Krótki opis architektury
Klasa TodoList obsługuje operacje na liście. Główna funkcja main() to interfejs konsolowy. Brak bazy danych – dane w pamięci.

## Rola narzędzi w wytwarzaniu oprogramowania
- Git: Służy do wersjonowania kodu, współpracy, cofania błędów.
- Testy: Rozwiązują problem błędów – automatyzują sprawdzanie, zapewniają, że zmiany nie psują apki.
- Automatyzacja: Ułatwia budowanie/uruchamianie, np. Makefile pozwala na jedną komendę zamiast wielu.
- Dokumentacja: Pomaga innym zrozumieć i uruchomić projekt, promuje dobre praktyki.# Projekt-Crud