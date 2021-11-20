from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import infra.config as config

engine = create_engine(url=config.SQLALCHEMY_DATABASE_URI, future=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


import datetime
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session
from sqlalchemy.event import listen


def listeners():
    instrumentador = SqlAlchemyListener()

    listen(Engine, "before_cursor_execute", instrumentador._before_cursor_execute)
    listen(Engine, "after_cursor_execute", instrumentador._after_cursor_execute)
    listen(Engine, "handle_error", instrumentador._handle_error)

    listen(Engine, "begin", instrumentador._begin)
    listen(Engine, "first_connect", instrumentador._first_connect)
    listen(Engine, "engine_disposed", instrumentador._engine_disposed)
    listen(Engine, "engine_connect", instrumentador._engine_connect)
    listen(Engine, "close", instrumentador._close)
    listen(Engine, "connect", instrumentador._connect)
    listen(Engine, "detach", instrumentador._detach)
    listen(Engine, "savepoint", instrumentador._savepoint)

    listen(Session, "after_begin", instrumentador._after_begin)
    listen(Session, "before_flush", instrumentador._before_flush)
    listen(Session, "after_flush", instrumentador._after_flush)
    listen(
        Session, "after_transaction_create", instrumentador._after_transaction_create
    )
    listen(Session, "after_transaction_end", instrumentador._after_transaction_end)
    listen(Session, "before_attach", instrumentador._before_attach)


class SqlAlchemyListener:
    """WIP"""

    def _savepoint(self, conn, name):
        print(f"savepoint: {datetime.datetime.now()}")

    def _begin(self, conn):
        print(f"begin: {datetime.datetime.now()}")

    def _begin_twophase(self, conn, xid):
        print(f"begin 2 fase: {datetime.datetime.now()}")

    def _after_transaction_end(self, session, transaction):
        print(f"after transaction end: {datetime.datetime.now()}")

    def _before_attach(self, session, instance):
        print(f"before transaction attach: {datetime.datetime.now()}")

    def _after_transaction_create(self, session, transaction):
        print(f"after transaction create: {datetime.datetime.now()}")

    def _after_begin(self, session, transaction, connection):
        print(f"after begin: {datetime.datetime.now()}")

    def _before_flush(self, session, flush_context):
        print(f"before flush: {datetime.datetime.now()}")

    def _after_flush(self, session, flush_context):
        print(f"after flush: {datetime.datetime.now()}")

    def _detach(self, dbapi_connection, connection_record):
        print(f"detac: {datetime.datetime.now()}")

    def _connect(self, dbapi_connection, connection_record):
        print(f"conn pool: {datetime.datetime.now()}")

    def _close(self, dbapi_connection, connection_record):
        print(f"close: {datetime.datetime.now()}")

    def _engine_connect(self, conn, branch):
        print(f"conn: {datetime.datetime.now()}")

    def _engine_disposed(self, engine):
        print(f"dispose: {datetime.datetime.now()}")

    def _first_connect(self, dbapi_connection, connection_record):
        print(f"first conn: {datetime.datetime.now()}")

    def _before_cursor_execute(
        self, conn, cursor, statement, parameters, context, executemany
    ):
        print(f"before: {datetime.datetime.now()}")

    def _after_cursor_execute(self, *args):
        print(f"after: {datetime.datetime.now()}")

    def _handle_error(self, *args):
        print(f"error: {datetime.datetime.now()}")


# listeners()
