from sqlmodel import SQLModel, Session, create_engine

# postgresql://username:password@host:port/database
DATABASE_URL = "postgresql://shipment_user:shipment_pass@localhost:5432/shipment_db"

engine = create_engine(DATABASE_URL)

def get_session():
    with Session(engine) as session:
        yield session