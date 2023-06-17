from typing import Optional

from sqlalchemy.engine.interfaces import Dialect
from sqlalchemy.types import String, TypeDecorator

from doc_br.types import CPF


class CPFTypeDecorator(TypeDecorator):
    """
    Custom SQLAlchemy type for storing CPF documents.

    This type decorator is used to convert CPF objects to their plain string representation
    when storing them in the
    database, and to convert the plain string representation back to CPF objects when
    retrieving them from the database.
    """

    impl = String

    def process_bind_param(self, value: Optional[CPF], dialect: Dialect) -> Optional[str]:
        """
        Convert a CPF object to its plain string representation for storage.

        :param value: The CPF object to be converted.
        :param dialect: The SQLAlchemy dialect in use.
        :return: The plain string representation of the CPF object.
        """
        if value is not None:
            return value.plain

    def process_result_value(self, value: Optional[str], dialect: Dialect) -> Optional[CPF]:
        """
        Convert a plain string representing a CPF to a CPF object when retrieving from the database.

        :param value: The plain string representation of the CPF.
        :param dialect: The SQLAlchemy dialect in use.
        :return: The CPF object.
        """
        if value is not None:
            return CPF(value)
