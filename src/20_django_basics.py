"""
Django Basics: Web Framework Fundamentals

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

This example demonstrates:
- Setting up Django without a full project structure
- Defining models with fields and relationships
- Database operations (CRUD)
- QuerySets and filtering
- Model relationships (ForeignKey, ManyToMany)
- Admin interface concepts

Note: This is a standalone script for demonstration. In production, use Django's project structure.

To run this example:
1. Install Django: pip install django
2. Run this script: python 20_django_basics.py
"""

import os
import sys
import django
from django.conf import settings
from django.db import models
from django.core.management import execute_from_command_line

# Configure Django settings
if not settings.configured:
    settings.configure(
        DEBUG=True,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',  # In-memory database for demo
            }
        },
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
            'django.contrib.auth',
            '__main__',  # This script as an app
        ],
        SECRET_KEY='demo-secret-key-for-concepts',
        USE_TZ=True,
    )

# Setup Django
django.setup()

# Define models
class Author(models.Model):
    """Author model demonstrating basic fields."""
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Book(models.Model):
    """Book model demonstrating relationships."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField(max_length=13, unique=True)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    genres = models.ManyToManyField('Genre', related_name='books')
    pages = models.PositiveIntegerField()
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['publication_date']

    def __str__(self):
        return f"{self.title} by {self.author.name}"

class Genre(models.Model):
    """Genre model for many-to-many relationship."""
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# Create tables
from django.core.management import call_command
from django.db import connection

def setup_database():
    """Create database tables."""
    with connection.schema_editor() as schema_editor:
        schema_editor.create_model(Author)
        schema_editor.create_model(Genre)
        schema_editor.create_model(Book)

def demo_crud_operations():
    """Demonstrate Create, Read, Update, Delete operations."""
    print("=== CRUD Operations Demo ===\n")

    # Create authors
    author1 = Author.objects.create(
        name="Jane Austen",
        email="jane.austen@example.com",
        birth_date="1775-12-16",
        bio="English novelist known for her witty social commentary."
    )
    author2 = Author.objects.create(
        name="Charles Dickens",
        email="charles.dickens@example.com",
        birth_date="1812-02-07",
        bio="English writer and social critic."
    )
    print(f"Created authors: {author1}, {author2}")

    # Create genres
    fiction = Genre.objects.create(name="Fiction")
    romance = Genre.objects.create(name="Romance")
    social_commentary = Genre.objects.create(name="Social Commentary")
    print(f"Created genres: {fiction}, {romance}, {social_commentary}")

    # Create books
    book1 = Book.objects.create(
        title="Pride and Prejudice",
        author=author1,
        isbn="9780141439518",
        publication_date="1813-01-28",
        price=12.99,
        pages=432,
        description="A romantic novel of manners."
    )
    book1.genres.add(fiction, romance)

    book2 = Book.objects.create(
        title="Great Expectations",
        author=author2,
        isbn="9780141439563",
        publication_date="1861-08-01",
        price=14.99,
        pages=544,
        description="A bildungsroman novel."
    )
    book2.genres.add(fiction, social_commentary)

    print(f"Created books: {book1}, {book2}")

    # Read operations
    print("\n=== Read Operations ===")
    all_authors = Author.objects.all()
    print(f"All authors: {[str(a) for a in all_authors]}")

    # Filter by condition
    active_authors = Author.objects.filter(is_active=True)
    print(f"Active authors: {[str(a) for a in active_authors]}")

    # Get specific object
    jane = Author.objects.get(name="Jane Austen")
    print(f"Jane Austen's books: {[str(b) for b in jane.books.all()]}")

    # Complex queries
    expensive_books = Book.objects.filter(price__gte=14.00)
    print(f"Books priced >= $14: {[str(b) for b in expensive_books]}")

    recent_books = Book.objects.filter(publication_date__year__gte=1800)
    print(f"Books published after 1800: {[str(b) for b in recent_books]}")

    # Update operation
    print("\n=== Update Operation ===")
    book1.price = 13.99
    book1.save()
    print(f"Updated {book1.title} price to ${book1.price}")

    # Delete operation
    print("\n=== Delete Operation ===")
    Genre.objects.filter(name="Social Commentary").delete()
    print("Deleted 'Social Commentary' genre")

    # Check relationships after deletion
    print(f"Book genres after deletion: {list(book2.genres.all())}")

def demo_query_techniques():
    """Demonstrate advanced QuerySet techniques."""
    print("\n=== Advanced Query Techniques ===\n")

    # Aggregation
    from django.db.models import Count, Avg, Max, Min

    author_book_counts = Author.objects.annotate(book_count=Count('books'))
    for author in author_book_counts:
        print(f"{author.name} has {author.book_count} books")

    # Average price
    avg_price = Book.objects.aggregate(Avg('price'))['price__avg']
    print(".2f")

    # Max pages
    max_pages = Book.objects.aggregate(Max('pages'))['pages__max']
    print(f"Maximum pages in any book: {max_pages}")

    # Filtering with Q objects
    from django.db.models import Q

    # Books that are either expensive or have many pages
    special_books = Book.objects.filter(
        Q(price__gte=14.00) | Q(pages__gte=500)
    )
    print(f"Special books (expensive or long): {[b.title for b in special_books]}")

    # Exclude certain conditions
    affordable_books = Book.objects.exclude(price__gte=14.00)
    print(f"Affordable books (< $14): {[b.title for b in affordable_books]}")

def demo_relationships():
    """Demonstrate model relationships."""
    print("\n=== Model Relationships Demo ===\n")

    # Access related objects
    for author in Author.objects.all():
        print(f"{author.name}'s books:")
        for book in author.books.all():
            print(f"  - {book.title} ({', '.join([g.name for g in book.genres.all()])})")

    # Reverse relationships
    for genre in Genre.objects.all():
        print(f"{genre.name} books:")
        for book in genre.books.all():
            print(f"  - {book.title} by {book.author.name}")

def main():
    """Main demonstration function."""
    print("Django Basics Demonstration")
    print("=" * 40)

    # Setup database
    setup_database()
    print("Database setup complete.\n")

    # Run demonstrations
    demo_crud_operations()
    demo_query_techniques()
    demo_relationships()

    print("\n=== Django Admin Concepts ===")
    print("In a real Django project, you would:")
    print("1. Register models in admin.py: admin.site.register(Author)")
    print("2. Create superuser: python manage.py createsuperuser")
    print("3. Run server: python manage.py runserver")
    print("4. Access admin at: http://127.0.0.1:8000/admin/")

    print("\nDjango basics demo completed!")

if __name__ == "__main__":
    main()