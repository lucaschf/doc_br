import validate_docbr

from doc_br.types.doc import Document


class CNPJ(Document):
    """
    Class representing a CNPJ (Cadastro Nacional da Pessoa Jurídica) document.

    Provides methods for sanitizing, validating, masking, and generating CNPJ document strings.

    Args:
       doc (str): The CNPJ document string.

    Raises:
       ValueError: If the document string is invalid.

    Attributes:
       _plain (str): The plain CNPJ document string.
       _masked (str): The masked CNPJ document string.

    Examples:
       >>> cnpj = CNPJ('12345678901234')  # consider as valid CNPJ document string
       >>> cnpj.plain
       '12345678901234'
       >>> cnpj.masked
       '12.345.678/9012-34'

       >>> cnpj = CNPJ('12345678')  # Invalid CNPJ
       Traceback (most recent call last):
           ...
       ValueError: Invalid CNPJ document string.
    """

    _PLAIN_DIGITS = 14
    """Number of digits in a CNPJ document string without mask."""

    def sanitize(self, doc: str) -> str:
        """
        Sanitize and standardize a CNPJ string by removing formatting and unwanted characters.

        This method will also fill a CNPJ document string with leading zeros if necessary.

        :param doc: The CNPJ document string to be sanitized and standardized.
        :return: The sanitized and standardized CNPJ document string.
        :raises ValueError: If the document string is invalid.
        """
        if doc is None:
            raise ValueError('Invalid CNPJ document.')

        self._validate_input(doc, mask_characters={'.', '-', '/'})
        plain_doc = self.remove_mask(doc, validate_unmasked=False)
        plain_doc = self._fill_with_zeros(plain_doc, self._PLAIN_DIGITS)
        self.validate(plain_doc)
        return plain_doc

    def validate(self, doc: str) -> None:
        """Validate a CNPJ document string.

        :param doc: The CNPJ document string to be validated.
        :raises ValueError: If the document string is invalid.
        """
        if doc is None or not validate_docbr.CNPJ().validate(doc):
            raise ValueError('Invalid CNPJ document.')

    def apply_mask(self, doc: str) -> str:
        """Apply mask to a CNPJ document string.

        :param doc: The CNPJ document string to be masked.
        :return: The masked CNPJ document string.
        :raises ValueError: If the document string is invalid.
        """
        if doc is None:
            raise ValueError('Invalid CNPJ document.')

        plain_doc = self.sanitize(doc)
        return '{}.{}.{}/{}-{}'.format(
            plain_doc[:2], plain_doc[2:5], plain_doc[5:8], plain_doc[8:12], plain_doc[12:]
        )

    def remove_mask(self, masked_document: str, validate_unmasked: bool) -> str:
        """Remove a mask from a CNPJ document string.

        :param masked_document: The masked CNPJ document string.
        :param validate_unmasked: Whether to validate the unmasked CNPJ document string.
        :return: The unmasked CNPJ document string.
        :raises ValueError: If the document string is invalid and validate_unmasked is True.
        """
        if validate_unmasked:
            return self.sanitize(masked_document)

        return ''.join(filter(str.isdigit, masked_document))

    @staticmethod
    def generate() -> 'CNPJ':
        """Generate a random CNPJ document.

        :return: The generated CNPJ document.
        """
        return CNPJ(validate_docbr.CNPJ().generate())

    def __init__(self, doc: str):
        """Initialize a CNPJ object.

        :param doc: The CNPJ document string.
        :raises ValueError: If the document string is invalid.
        """
        super().__init__(doc)
