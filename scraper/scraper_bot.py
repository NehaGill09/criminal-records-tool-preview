import random
from datetime import datetime, timedelta
from faker import Faker
from .models import CriminalRecord
import logging
import os

# ✅ Set up logging
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, 'logs')
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, 'scraper.log'),
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
)

fake = Faker()

# ✅ Run the scraper and save records
def run_scraper(from_date="2020-01-01", to_date="2025-07-01"):
    logging.info("🔁 Scraper started...")

    try:
        from_dt = datetime.strptime(from_date, "%Y-%m-%d")
        to_dt = datetime.strptime(to_date, "%Y-%m-%d")
    except ValueError:
        logging.error("❌ Invalid date format. Use YYYY-MM-DD.")
        return

    created = 0
    try:
        for _ in range(20):
            date_filed = fake.date_between(start_date=from_dt, end_date=to_dt)
            case_number = f"CASE-{fake.random_number(digits=6)}"

            # Skip duplicates
            if CriminalRecord.objects.filter(case_number=case_number).exists():
                continue

            record = CriminalRecord(
                defendant_name=fake.name(),
                birth_date=fake.date_of_birth(minimum_age=18, maximum_age=75),
                sex=random.choice(["Male", "Female", "Other"]),
                race=random.choice(["White", "Black", "Hispanic", "Asian", "Other"]),
                case_number=case_number,
                date_filed=date_filed,
                charges=fake.sentence(nb_words=6),
                arrest_citation_date=date_filed - timedelta(days=random.randint(1, 30)),
                parish=random.choice(["Orleans", "East Baton Rouge", "Jefferson", "Caddo"]),
                alert_available=random.choice([True, False])
            )
            record.save()
            created += 1

        logging.info(f"✅ Successfully saved {created} records.")
    except Exception as e:
        logging.exception(f"❌ Scraper crashed: {str(e)}")
