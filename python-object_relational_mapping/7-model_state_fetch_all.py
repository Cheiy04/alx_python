'''script that lists all State objects from the database hbtn_0e_6_usa'''
from sys import argv
import sqlalchemy
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# user =      argv[1]
# passwd =    argv[2]
# db =        argv[3]
# port =      3306

if __name__ == '__main__':
    def conn(username=argv[1], password=argv[2], port=3306, db=argv[3]):
        engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:{port}/{db}" , pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        states = session.query(State).order_by(State.id).all()
        for state in states:
            print(f"{state.id}:{state.name}")

        #close session
        session.close()

    conn()