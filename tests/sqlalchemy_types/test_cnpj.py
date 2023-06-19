import pytest
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy import text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from doc_br.sqlalchemy_types import CNPJTypeDecorator
from doc_br.types import CNPJ

Base = declarative_base()


class CNPJTable(Base):
    __tablename__ = 'cnpj_table'
    id = Column(Integer, primary_key=True)
    cnpj = Column(CNPJTypeDecorator)


@pytest.fixture(scope="module")
def test_db():
    engine = create_engine('sqlite:///:memory:')
    session_maker = sessionmaker(bind=engine)
    session = session_maker()
    Base.metadata.create_all(engine)
    return session


def test_process_bind_param(test_db):
    session = test_db
    cnpj_obj = CNPJ.generate()

    # Create an instance of TestTable and add it to the session
    test_instance = CNPJTable(id=1, cnpj=cnpj_obj)
    session.add(test_instance)
    session.commit()

    result = session.execute(text("SELECT cnpj FROM cnpj_table WHERE id=1")).first()
    assert result[0] == cnpj_obj.plain


def test_process_result_value(test_db):
    session = test_db
    cnpj = CNPJ.generate()
    test_instance = CNPJTable(id=2, cnpj=cnpj)
    session.add(test_instance)
    session.commit()

    row = session.get(CNPJTable, 2)
    assert row.cnpj == CNPJ(cnpj.plain)
