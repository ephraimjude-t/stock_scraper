from data.database import Base, engine
from data.models import TopGainer, TopLoser  # <-- This must be here

print("[INFO] Creating tables...")
Base.metadata.create_all(bind=engine)
print("[INFO] Tables created!")

