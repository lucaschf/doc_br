import pytest
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy import text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from doc_br.sqlalchemy_types import CPFTypeDecorator
from doc_br.types import CPF

Base = declarative_base()


class CPFTable(Base):
    __tablename__ = 'cpf_table'
    id = Column(Integer, primary_key=True)
    cpf = Column(CPFTypeDecorator)


@pytest.fixture(scope="module")
def test_db():
    engine = create_engine('sqlite:///:memory:')
    session_maker = sessionmaker(bind=engine)
    session = session_maker()
    Base.metadata.create_all(engine)
    return session


def test_process_bind_param(test_db):
    session = test_db
    cpf_obj = CPF.generate()

    # Create an instance of TestTable and add it to the session
    test_instance = CPFTable(id=1, cpf=cpf_obj)
    session.add(test_instance)
    session.commit()

    result = session.execute(text("SELECT cpf FROM cpf_table WHERE id=1")).first()
    assert result[0] == cpf_obj.plain


def test_process_result_value(test_db):
    session = test_db
    cpf = CPF.generate()
    test_instance = CPFTable(id=2, cpf=cpf)
    session.add(test_instance)
    session.commit()

    row = session.get(CPFTable, 2)
    assert row.cpf == CPF(cpf.plain)
