# scripts/seed_data.py

from lib.db.connection import Session
from lib.models.client import Client
from lib.models.project import Project
from lib.models.invoice import Invoice
from datetime import date

session = Session()

# Clear existing data
session.query(Invoice).delete()
session.query(Project).delete()
session.query(Client).delete()

# Sample Clients
client1 = Client(name="Alice Johnson", email="alice@example.com", phone="123-456-7890")
client2 = Client(name="Bob Smith", email="bob@example.com", phone="987-654-3210")

# Sample Projects
project1 = Project(
    name="Website Redesign",
    description="Redesign company website for SEO and UX",
    rate=1500.0,
    deadline=date(2025, 6, 30),
    client=client1
)

project2 = Project(
    name="Marketing Campaign",
    description="Social media marketing campaign",
    rate=2000.0,
    deadline=date(2025, 7, 15),
    client=client2
)

# Sample Invoices
invoice1 = Invoice(
    amount=750.0,
    status="paid",
    date_issued=date(2025, 5, 15),
    project=project1
)

invoice2 = Invoice(
    amount=500.0,
    status="unpaid",
    date_issued=date(2025, 5, 20),
    project=project2
)

# Add to session and commit
session.add_all([client1, client2, project1, project2, invoice1, invoice2])
session.commit()

print("Seed data added.")
