from lib.db.connection import Base, engine
from lib.models.client import Client
from lib.models.project import Project
from lib.models.invoice import Invoice

Base.metadata.create_all(engine)