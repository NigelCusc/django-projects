# Django projects

Personal practice while working through **[Python Django — The Practical Guide](https://www.udemy.com/course/python-django-the-practical-guide)** on Udemy.

Each top-level folder is a standalone Django project from a different stage of the course, roughly in order of increasing complexity:

| Project | Focus |
|---------|-------|
| [`monthly-challenges`](#monthly-challenges) | URLs, views, and templates (no database) |
| [`my_site`](#my_site) | Multi-app project with a blog (list + slug detail) |
| [`book_store`](#book_store) | Models, the ORM, relationships, and the admin |
| [`feedback`](#feedback) | Forms, `ModelForm` validation, and class-based views |

## Running locally

The repo uses a single shared virtual environment at the root (`.venv`, currently **Django 6.0.x**). From the repo root:

```bash
python -m venv .venv          # once
source .venv/bin/activate     # macOS/Linux; on Windows use .venv\Scripts\activate
pip install django

cd <project>                  # e.g. book_store
python manage.py migrate
python manage.py runserver
```

Then open [http://127.0.0.1:8000/](http://127.0.0.1:8000/). (`monthly-challenges` has its own `venv/` from earlier in the course.)

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

See [Running locally](#running-locally) for the shared setup.

## `book_store`

A small "book outlet" site backed by a database, used to practise Django **models, the ORM, and the admin**. The `book_outlet` app lists books ordered by rating (with a total count and average rating) and shows a detail page per book addressed by slug.

**URLs**

| Path | Purpose |
|------|---------|
| `/` | Book list (sorted by rating, with totals) |
| `/<slug>` | Single book detail (slug in the URL) |
| `/admin/` | Django admin |

**Models** (`book_outlet/models.py`)

- `Book` — title, rating (validated 1–5), `is_bestselling` flag, and a `slug`.
- `Author` — name, email, slug, with a **one-to-one** link to `Address`.
- `Address` and `Country` — supporting models (`Country` is **many-to-many** with `Book` via `published_countries`).
- Relationships: `Book → Author` is a **foreign key**; `Book ↔ Country` is **many-to-many**; `Author → Address` is **one-to-one**.

**Django topics practiced**

- Defining models, fields, and validators (`MinValueValidator`, `MaxValueValidator`).
- Model relationships (`ForeignKey`, `OneToOneField`, `ManyToManyField`) and `related_name`.
- The ORM: `all()`, `order_by()`, `count()`, `aggregate(Avg(...))`, and `get_object_or_404()`.
- `SlugField` and `get_absolute_url()` with `reverse()`.
- Customising the **admin** (`ModelAdmin`, `list_display`, `list_filter`, `prepopulated_fields`).
- A `RedirectView` so `/admin` (no trailing slash) isn't swallowed by the `<slug:slug>` route.

## `feedback`

A single-page feedback form that collects reviews and stores them in the database, used to practise **forms and form validation**. The `reviews` app renders a form, validates it, saves a `Review`, and redirects to a thank-you page.

**URLs**

| Path | Purpose |
|------|---------|
| `/` | Review form (and POST handling) |
| `/thank-you/` | Confirmation page after a successful submit |
| `/admin/` | Django admin |

**Django topics practiced**

- `ModelForm` generated from a `Review` model, with custom `labels`, `error_messages`, and `widgets`.
- Model-level validation (`MinLengthValidator`, `MinValueValidator`, `MaxValueValidator`).
- Handling `GET` vs `POST`, `form.is_valid()`, `form.save()`, and `redirect()`.
- Both **function-based** and **class-based** views (the URLconf wires up the CBV `ReviewView`).
- URL namespacing (`app_name = 'reviews'`).

See [Running locally](#running-locally) for the shared setup.
