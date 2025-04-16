from data.database import SessionLocal
from data.models import TopGainer, TopLoser

db = SessionLocal()

print("Top Gainers:")
for g in db.query(TopGainer).limit(5).all():
    print(g.symbol, g.price, g.percent_change)

print("\nTop Losers:")
for l in db.query(TopLoser).limit(5).all():
    print(l.symbol, l.price, l.percent_change)

db.close()
