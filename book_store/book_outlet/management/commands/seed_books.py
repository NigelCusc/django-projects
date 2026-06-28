import json
from pathlib import Path

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from book_outlet.models import Author, Book


# Custom management commands live in <app>/management/commands/.
# The file name (seed_books) becomes the command name, so we run it with:
#   python manage.py seed_books
# Django auto-discovers any class named "Command" that subclasses BaseCommand.
class Command(BaseCommand):
    # Shown when running `python manage.py seed_books --help`.
    help = "Seed the Author and Book tables with real books from a JSON file."

    # add_arguments lets us define optional flags for the command.
    def add_arguments(self, parser):
        # Pass --clear to wipe existing data before seeding.
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete all existing books and authors before seeding.",
        )

    # handle() is the entry point Django calls when the command runs.
    def handle(self, *args, **options):
        # Build an absolute path to books.json that works no matter where
        # the command is run from. __file__ is this file's location, so we
        # walk up to the app folder (commands -> management -> book_outlet)
        # and then into the data/ folder.
        data_file = Path(__file__).resolve().parents[2] / "data" / "books.json"

        # Load the JSON file into a Python list of dicts.
        with open(data_file, encoding="utf-8") as file:
            books = json.load(file)

        if options["clear"]:
            # Delete books first: a Book points at an Author via a foreign key,
            # so removing books avoids dangling references.
            deleted_books, _ = Book.objects.all().delete()
            deleted_authors, _ = Author.objects.all().delete()
            # self.stdout.write is the management-command way to print output.
            self.stdout.write(
                f"Deleted {deleted_books} book(s) and {deleted_authors} author(s)."
            )

        created_count = 0
        for entry in books:
            author_data = entry["author"]

            # Author is now its own model linked to Book by a ForeignKey, so
            # we create (or fetch) the Author first. get_or_create looks up an
            # author by name and only creates a new row if one doesn't exist,
            # which lets several books share the same author (e.g. Tolkien).
            author, _ = Author.objects.get_or_create(
                name=author_data["name"],
                defaults={
                    "email": author_data["email"],
                    # slug is required and unique; slugify turns
                    # "J. R. R. Tolkien" into "j-r-r-tolkien".
                    "slug": slugify(author_data["name"]),
                },
            )

            # update_or_create avoids duplicate books if we run the seeder
            # twice: it looks up a Book by title, then creates or updates it.
            _, created = Book.objects.update_or_create(
                title=entry["title"],
                defaults={
                    "author": author,
                    "rating": entry["rating"],
                    "is_bestselling": entry["is_bestselling"],
                    # Book also has a required unique slug derived from title.
                    "slug": slugify(entry["title"]),
                },
            )
            if created:
                created_count += 1

        # self.style.SUCCESS colours the message green in the terminal.
        self.stdout.write(
            self.style.SUCCESS(
                f"Seeding complete: {created_count} new book(s) added, "
                f"{len(books)} total processed."
            )
        )
