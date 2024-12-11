from sqlalchemy import *
from sqlalchemy.orm import Session

class DBSettings():
    @staticmethod
    def get_session():
        engine = create_engine(f"postgresql+psycopg2://postgres:wowpop228@localhost:5432/FasApiTest")
        return Session(bind=engine)