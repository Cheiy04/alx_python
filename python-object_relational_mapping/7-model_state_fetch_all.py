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

def conn(username, password, db):
    engine = create_engine(f"mysql+mysqldb://{password}:{username}@localhost:/{db}" , pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).all()
    for state in states:
        print(f"{state.id}:{state.name}")

    #close session
    session.close()

if __name__ == '__main__':

    conn(argv[1], argv[2], argv[3])