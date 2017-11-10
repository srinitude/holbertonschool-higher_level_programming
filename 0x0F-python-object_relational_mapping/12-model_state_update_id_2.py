#!/usr/bin/python3
"""
List all State objects
"""
if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.orm.exc import NoResultFound

    target = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(target.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        state = session.query(State).filter(State.id == 2).one()
        state.name = "New Mexico"
        session.commit()
    except NoResultFound:
        pass
