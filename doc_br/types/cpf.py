import validate_docbr

from doc_br.types.doc import Document


class CPF(Document):
    """
    Class representing a CPF (Cadastro de Pessoas Físicas) document.

    Provides methods for sanitizing, validating, masking, and generating CPF document strings.

    Args:
        doc (str): The CPF document string.

    Raises:
        ValueError: If the document string is invalid.

    Attributes:
        _plain (str): The plain CPF document string.
        _masked (str): The masked CPF document string.

    Examples:
        >>> cpf = CPF('12345678900') # consider as valid CPF document string
        >>> cpf.plain
        '12345678900'
        >>> cpf.masked
        '123.456.789-00'

        >>> cpf = CPF('12345678')  # Invalid CPF
        Traceback (most recent call last):
            ...
        ValueError: Invalid CPF document string.
    """

    _PLAIN_DIGITS = 11
    """Number of digits in a CPF document string without mask."""

    def sanitize(self, doc: str) -> str:
        """
        Sanitize and standardize a CPF string by removing formatting and unwanted characters.

        This method will also fill a CPF document string with leading zeros if necessary.

        :param doc: The CPF document string to be sanitized and standardized.
        :return: The sanitized and standardized CPF document string.
        :raises ValueError: If the document string is invalid.
        """
        if doc is None:
            raise ValueError('Invalid CPF document.')

        self._validate_input(doc, mask_characters={'-', '.'})
        plain_doc = self.un_mask(doc, validate=False)
        plain_doc = self._fill_with_zeros(plain_doc, self._PLAIN_DIGITS)
        self.validate(plain_doc)
        return plain_doc

    def validate(self, doc: str) -> None:
        """Validate a CPF document string.

        :param doc: The CPF document string to be validated.
        :raises ValueError: If the document string is invalid.
        """
        if doc is None or not validate_docbr.CPF().validate(doc):
            raise ValueError('Invalid CPF document.')

    def mask(self, doc: str) -> str:
        """Apply mask to a CPF document string.

        :param doc: The CPF document string to be masked.
        :return: The masked CPF document string.
        :raises ValueError: If the document string is invalid.
        """
        plain_doc = self.sanitize(doc)
        return '{}.{}.{}-{}'.format(plain_doc[:3], plain_doc[3:6], plain_doc[6:9], plain_doc[9:])

    def un_mask(self, doc: str, validate: bool) -> str:
        """Remove a mask from a CPF document string.

        :param doc: The masked CPF document string.
        :param validate: Whether to validate the unmasked CPF document string.
        :return: The unmasked CPF document string.
        :raises ValueError: If the document string is invalid and validate is True.
        """
        if doc is None:
            raise ValueError('Invalid CPF document.')

        if validate:
            return self.sanitize(doc)

        return ''.join(filter(str.isdigit, doc))

    @staticmethod
    def generate() -> 'CPF':
        """Generate a random CPF document.

        :return: The generated CPF document.
        """
        return CPF(validate_docbr.CPF().generate())

    def __init__(self, doc: str):
        """Initialize a CPF object.

        :param doc: The CPF document string.
        :raises ValueError: If the document string is invalid.
        """
        super().__init__(doc)

    def __hash__(self) -> int:
        """Return the hash value of the CPF object.

        :return: The hash value.
        """
        return hash(self._plain)

    def __eq__(self, other: 'CPF') -> bool:
        """Check if two CPF objects are equal.

        :param other: The other CPF object to compare.
        :return: True if the objects are equal, False otherwise.
        """
        return self._plain == other._plain

    def __repr__(self) -> str:
        """Return the string representation of the CPF object.

        :return: The plain CPF document string.
        """
        return self.plain
