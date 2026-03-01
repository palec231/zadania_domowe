import random

from django.core.management.base import BaseCommand
from faker import Faker

from ogloszenia.models import Post


class Command(BaseCommand):
    help = "Seeds the database with sample data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding data...")

        fake = Faker("pl_PL")

        # 10 autorów
        # authors = []
        # for _ in range(10):
        #     author = Author.objects.create(
        #         name=fake.name(),
        #         email=fake.email(),
        #     )
        #     authors.append(author)

        # self.stdout.write(self.style.SUCCESS(f"{len(authors)} authors created."))

        # 50 postów
        posts = []
        for _ in range(50):
            post = Post.objects.create(
                title=fake.sentence(nb_words=6),
                content="\n\n".join(fake.paragraphs(nb=5)),
                #author=random.choice(authors),
                published_date=fake.date_time_this_year(),
            )
            posts.append(post)

        self.stdout.write(self.style.SUCCESS(f"{len(posts)} posts created."))
        self.stdout.write(self.style.SUCCESS("Data seeding complete."))