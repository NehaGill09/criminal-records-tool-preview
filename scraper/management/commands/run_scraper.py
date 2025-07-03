from django.core.management.base import BaseCommand
from scraper.scraper_bot import run_scraper

class Command(BaseCommand):
    help = "Run the criminal record scraper with optional date range."

    def add_arguments(self, parser):
        parser.add_argument('--from', type=str, dest='from_date', help='Start date (YYYY-MM-DD)', default="2020-01-01")
        parser.add_argument('--to', type=str, dest='to_date', help='End date (YYYY-MM-DD)', default="2025-07-01")

    def handle(self, *args, **options):
        from_date = options['from_date']
        to_date = options['to_date']
        self.stdout.write(self.style.SUCCESS(f"Running scraper from {from_date} to {to_date}..."))
        run_scraper(from_date, to_date)
        self.stdout.write(self.style.SUCCESS("✅ Scraper completed."))
