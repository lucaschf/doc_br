from typing import Optional

from sqlalchemy.engine.interfaces import Dialect
from sqlalchemy.types import String, TypeDecorator

from doc_br.types import CNPJ


class CNPJTypeDecorator(TypeDecorator):
    """
    Custom SQLAlchemy type for storing CNPJ documents.

    This type decorator is used to convert CNPJ objects to their plain string representation
    when storing them in the
    database, and to convert the plain string representation back to CNPJ objects when
    retrieving them from the database.
    """

    impl = String

    def process_bind_param(self, value: Optional[CNPJ], dialect: Dialect) -> Optional[str]:
        """
        Convert a CNPJ object to its plain string representation for storage.

        :param value: The CNPJ object to be converted.
        :param dialect: The SQLAlchemy dialect in use.
        :return: The plain string representation of the CNPJ object.
        """
        if value is not None:
            return value.plain

    def process_result_value(self, value: Optional[str], dialect: Dialect) -> Optional[CNPJ]:
        """
        Convert a plain string representing a CNPJ to a CNPJ object when retrieving from the db.

        :param value: The plain string representation of the CNPJ.
        :param dialect: The SQLAlchemy dialect in use.
        :return: The CNPJ object.
        """
        if value is not None:
            return CNPJ(value)
