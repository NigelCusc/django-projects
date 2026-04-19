# Django projects

Personal practice while working through **[Python Django — The Practical Guide](https://www.udemy.com/course/python-django-the-practical-guide)** on Udemy.

## `monthly-challenges`

A small site that lists monthly coding challenges and shows a detail page per month. Challenge text is stored in a JSON file and loaded in the views (no database models in this app yet).

**What it does**

- Home page with links to each month’s challenge.
- Challenge detail pages addressed by month name (e.g. `/challenges/january/`).
- Numeric month URLs (e.g. `/challenges/1/`) redirect to the named month route.

**Django topics practiced so far**

- Project and app layout (`startproject` / `startapp`), `INSTALLED_APPS`, and settings such as templates and static files.
- URL routing: `path()`, `include()`, URL names, **namespaces** (`app_name`), and path converters (`<int:…>`, `<str:…>`).
- Function-based **views**: `render()`, `redirect()`, raising `Http404`, and the `@require_GET` decorator.
- **Templates**: base template with `{% block %}`, child templates, `{% include %}`, `{% url %}`, and `{% static %}`.
- **Static files** and the staticfiles app for CSS (project- and app-level static assets).
- A project-level **404** template for custom “not found” pages.

To run the app locally, use the `manage.py` and virtual environment inside `monthly-challenges/` (see the course for the usual `runserver` workflow).

## `my_site`

A small site with a **home page** and a **blog** area (list + post detail by slug). Built with Django 4.2.x while following the same Udemy course.

**URLs**

| Path | Purpose |
|------|---------|
| `/` | Home |
| `/posts/` | Blog post list |
| `/posts/<slug>/` | Single post (slug in the URL) |

**Layout**

- **`blog`** — Registered app (`blog.apps.BlogConfig` in `INSTALLED_APPS`); views and templates live under `blog/` (`blog/templates/blog/…`).
- **Project templates** — Shared pieces in `my_site/templates/` (`base.html`, `navbar.html`); home page templates under `my_site/my_site/templates/home/`.
- **Static files** — Project-level `static/` via `STATICFILES_DIRS`.

The blog URLconf uses a namespace (`app_name = 'blog-posts'` in `blog/urls.py`), so named URLs look like `blog-posts:index` and `blog-posts:post_detail`.

**Run locally**

From the repo root:

```bash
cd my_site
python -m venv .venv          # once
source .venv/bin/activate     # macOS/Linux; on Windows use .venv\Scripts\activate
pip install django~=4.2       # or match your course / pyproject
python manage.py migrate
python manage.py runserver
```

Then open [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
