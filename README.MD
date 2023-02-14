# Coffee Shop

---

## Algorytm implementacji funkcjonalności w Django
1. Czy potrzebuje do tego django app?
   - `python manage.py startapp <app_name>`
   - następnie dodaj do settings.py w INSTALLED_APPS -> '<app_name>.apps.<class>'
2. Czy potrzebujemy do tego dane?
   - tworze modele w `<app_name>/models.py`
   - tworze migracje -> `python manage.py makemigrations <app_name>`
   - aplikuje migracje => `python manage.py migrate <app_name>`
   - ? sprawdzam fizycznie w bazie danych, czy jest ok
   - piszę unit tests
3. Czy potrzebuje obsługę z CMS (django Admin)?
   - w pliku `<app_name>/admin.py` rejestrujemy model
   - admin.site.register(`<model_name>`)
4. Czy potrzebuje formularz?
   - w pliku `<app_name>/forms.py` tworze formularz za pomocą django forms
   - piszę unit tests
5. Czy potrzebuje Widok (Logike)?
   - w pliku `<app_name>/views.py` tworze widoki -> docelowo należy używać class
   - piszę unit test
6. Czy potrzebny jest template do widoku?
   - tworze go w `<app_name>/templates/<app_name_namespace>/<file_name>.html`
   - podpinam do widoku
   - piszę unit tests
7. Czy potrzebny jest router?
   - tworzę lokalny router -> `<app_name>/urls.py` -> użyj live template
   - pamiętaj o app_name (namespace) i name do endpointa
   - podpinam lokalny router do globalnego -> `config/urls.py` -> funkcja include
   - piszę unit tests
8. Testuje manualnie, czy działa
   - PROFIT!
