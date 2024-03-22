#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(mysql_username,
        mysql_password, database_name))

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query all State objects and sort them by id
    states = session.query(State).order_by(State.id).all()

    # Display results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()
