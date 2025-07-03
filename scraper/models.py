from django.db import models

# Create your models here.\\
from django.db import models

class CriminalRecord(models.Model):
    defendant_name = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=20, null=True, blank=True)
    race = models.CharField(max_length=50, null=True, blank=True)
    case_number = models.CharField(max_length=100, unique=True)
    date_filed = models.DateField(null=True, blank=True)
    charges = models.TextField(null=True, blank=True)
    arrest_citation_date = models.DateField(null=True, blank=True)
    parish = models.CharField(max_length=100, null=True, blank=True)
    alert_available = models.BooleanField(default=False)
    scraped_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.defendant_name} - {self.case_number}"
