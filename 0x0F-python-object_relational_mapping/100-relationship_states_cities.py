#!/usr/bin/python3
"""Create the State "California" with the City "San Francisco"
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(mysql_username, mysql_password, database_name))

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Create the State "California" with the City "San Francisco"
    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)
    
    # Add the new objects to the session
    session.add(california)
    session.add(san_francisco)

    # Commit the changes
    session.commit()

    # Close session
    session.close()
