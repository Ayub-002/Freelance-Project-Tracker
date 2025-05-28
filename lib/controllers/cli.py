from lib.db.connection import Session
from lib.models.client import Client
from lib.models.project import Project
from lib.models.invoice import Invoice
from datetime import datetime

session = Session()

def main():
    while True:
        print("\n--- Freelance Project Tracker ---")
        print("1. Add Client")
        print("2. View Clients")
        print("3. Add Project")
        print("4. View Projects")
        print("5. Add Invoice")
        print("6. View Invoices")
        print("0. Exit")

        choice = input("Select an option: ").strip()

        if choice == '1':
            add_client()
        elif choice == '2':
            view_clients()
        elif choice == '3':
            add_project()
        elif choice == '4':
            view_projects()
        elif choice == '5':
            add_invoice()
        elif choice == '6':
            view_invoices()
        elif choice == '0':
            break
        else:
            print("Invalid choice.")

def add_client():
    name = input("Client Name: ").strip()
    email = input("Email: ").strip()
    phone = input("Phone: ").strip()
    if name and email:
        client = Client(name=name, email=email, phone=phone)
        session.add(client)
        session.commit()
        print("Client added.")
    else:
        print("Name and Email are required.")

def view_clients():
    clients = session.query(Client).all()
    if clients:
        for client in clients:
            print(client)
    else:
        print("No clients found.")

def add_project():
    try:
        client_id_input = input("Client ID: ").strip()
        if not client_id_input.isdigit():
            raise ValueError("Client ID must be a number.")
        client_id = int(client_id_input)
        name = input("Project Name: ").strip()
        description = input("Description: ").strip()
        rate_input = input("Rate: ").strip()
        if not rate_input:
            raise ValueError("Rate is required.")
        rate = float(rate_input)
        deadline_input = input("Deadline (YYYY-MM-DD): ").strip()
        if not deadline_input:
            raise ValueError("Deadline is required.")
        deadline = datetime.strptime(deadline_input, "%Y-%m-%d")
        project = Project(name=name, description=description, rate=rate, deadline=deadline, client_id=client_id)
        session.add(project)
        session.commit()
        print("Project added.")
    except Exception as e:
        session.rollback()
        print(f"Error adding project: {e}")

def view_projects():
    projects = session.query(Project).all()
    if projects:
        for project in projects:
            print(project)
    else:
        print("No projects found.")

def add_invoice():
    try:
        project_id_input = input("Project ID: ").strip()
        if not project_id_input.isdigit():
            raise ValueError("Project ID must be a number.")
        project_id = int(project_id_input)
        amount_input = input("Amount: ").strip()
        if not amount_input:
            raise ValueError("Amount is required.")
        amount = float(amount_input)
        status = input("Status (paid/unpaid): ").strip().lower()
        if status not in ['paid', 'unpaid']:
            raise ValueError("Status must be 'paid' or 'unpaid'.")
        date_issued_input = input("Date Issued (YYYY-MM-DD): ").strip()
        if not date_issued_input:
            raise ValueError("Date Issued is required.")
        date_issued = datetime.strptime(date_issued_input, "%Y-%m-%d")
        invoice = Invoice(amount=amount, status=status, date_issued=date_issued, project_id=project_id)
        session.add(invoice)
        session.commit()
        print("Invoice added.")
    except Exception as e:
        session.rollback()
        print(f"Error adding invoice: {e}")

def view_invoices():
    invoices = session.query(Invoice).all()
    if invoices:
        for invoice in invoices:
            print(invoice)
    else:
        print("No invoices found.")
