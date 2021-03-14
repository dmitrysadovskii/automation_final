from sqlalchemy import create_engine
from sqlalchemy import insert
from sqlalchemy import table, column


def connect_db():
    engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/postgres')
    return engine


def add_db_group(db, group_name):
    auth_group_table = table("auth_group",
                             column("id"),
                             column("name")
                             )
    stmt = (
        insert(auth_group_table).values(name=group_name)
    )
    db.execute(stmt)
