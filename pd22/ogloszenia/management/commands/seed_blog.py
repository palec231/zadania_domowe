# Zadanie 7
import random

from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker

from ogloszenia.models import Category, Post, Tag


class Command(BaseCommand):
    help = "Seeds blog with 10 predefined categories and 100 fake posts."

    CATEGORIES = [
        "Technologia",
        "Podróże",
        "Kulinaria",
        "Sport",
        "Zdrowie",
        "Edukacja",
        "Finanse",
        "Kultura",
        "Rozwój osobisty",
        "Nauka",
    ]

    TAGS = [
        "Django",
        "Python",
        "Web Development",
        "Faker",
        "Testowanie",
        "Programowanie",
        "Bazy danych",
        "API",
        "Frontend",
        "Backend",
    ]

    @transaction.atomic
    def handle(self, *args, **kwargs):
        fake = Faker("pl_PL")

        self.stdout.write("Usuwam istniejące posty i kategorie...")
        Post.objects.all().delete()
        Category.objects.all().delete()

        # Zadanie 9
        self.stdout.write("Tworzę / upewniam się, że tagi istnieją...")
        for name in self.TAGS:
            Tag.objects.get_or_create(name=name)
        tag_objs = list(Tag.objects.all())
        max_k = min(5, len(tag_objs))

        self.stdout.write("Tworzę 10 kategorii...")
        categories = [Category.objects.create(name=name) for name in self.CATEGORIES]

        self.stdout.write("Tworzę 100 postów (Faker) i losowo przypisuję kategorie...")
        posts = []
        for _ in range(100):
            posts.append(
                Post(
                    title=fake.sentence(nb_words=6).rstrip("."),
                    content="\n\n".join(fake.paragraphs(nb=random.randint(3, 8))),
                    author=fake.name(),
                    category=random.choice(categories),  
                )
            )

        Post.objects.bulk_create(posts)

        # Zadanie 9
        self.stdout.write("Losowo przypisuję 1–5 tagów do każdego posta...")
        created_posts = list(Post.objects.all())  # po delete() to są tylko nowe
        for post in created_posts:
            k = random.randint(1, max_k)
            post.tags.set(random.sample(tag_objs, k))

        self.stdout.write(self.style.SUCCESS("Utworzono 10 kategorii i 100 postów z tagami."))