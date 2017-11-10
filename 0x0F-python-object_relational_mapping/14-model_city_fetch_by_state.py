#!/usr/bin/python3
"""
List all State objects
"""
if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    target = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(target.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State, City).filter(State.id == City.state_id)
    for s, c in states.order_by(City.id).all():
        print("{:s}: ({:d}) {:s}".format(s.name, c.id, c.name))
