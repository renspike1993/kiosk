from sqlalchemy import create_engine, Column, Integer, String, Text, Float, func, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# --- Database Config ---
DB_NAME = "moist"
DB_USER = "postgres"
DB_PASSWORD = "renspike"
DB_HOST = "localhost"
DB_PORT = "5432"

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

Base = declarative_base()
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)


class Record(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True, autoincrement=True)
    year = Column(String(255))
    sem = Column(String(255))
    full_name = Column(Text)
    sub_code = Column(String(255))
    sub_desc = Column(Text)
    grade = Column(String(255), nullable=True)
    unit = Column(String(255), nullable=True)
    source_file = Column(Text)
    last_name = Column(Text)
    first_name = Column(Text)

    @staticmethod
    def search_by_name(name_parts):
        session = SessionLocal()
        try:
            if not name_parts:
                return []
                
            query = session.query(Record)
            
            for part in name_parts:
                # Each part must match in either last_name OR first_name
                query = query.filter(or_(
                        # Record.last_name.ilike(f"%{part}%"),
                        # Record.first_name.ilike(f"%{part}%"),
                        Record.full_name.ilike(f"%{part}%")
                    )
                )
            
            results = query.order_by(Record.year, Record.sem, Record.sub_code).all()
            return results
        finally:
            session.close()
