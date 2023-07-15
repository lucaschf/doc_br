from abc import ABC, abstractmethod
from typing import Set


class Document(ABC):
    """
    Abstract base class for document objects.

    Provides methods for sanitizing, masking, unmasking, and validating document strings.
    """

    _plain: str = ''
    _masked: str = ''

    @property
    def plain(self) -> str:
        """Get the plain document string."""
        return self._plain

    @property
    def masked(self) -> str:
        """Get the masked document string."""
        return self._masked

    @abstractmethod
    def sanitize(self, doc: str) -> str:
        """
        Sanitize and standardize a document string by removing formatting and unwanted characters.

        This method is a way to standardize the document string.
        If you just want to remove any formatting or unwanted characters but not standardize,
        use the un_mask method.

        :param doc: The document string to be sanitized.
        :return: The sanitized document string.
        :raises ValueError: If the document string is invalid.
        """

    @abstractmethod
    def apply_mask(self, doc: str) -> str:
        """
        Apply a mask to the document string.

        :param doc: The document string to be masked.
        :return: The masked document string.
        """

    @abstractmethod
    def remove_mask(self, masked_document: str, validate_unmasked: bool) -> str:
        """
        Remove the mask from the document string.

        :param masked_document: The masked document string.
        :param validate_unmasked: Whether to validate the unmasked document string.
        :return: The unmasked document string.
        """

    @abstractmethod
    def validate(self, doc: str) -> None:
        """
        Validate the document string.

        :param doc: The document string to be validated.
        :raises ValueError: If the document string is invalid.
        """

    @staticmethod
    def _validate_input(input_data: str | None, mask_characters: Set[str] | None = None) -> None:
        """
        Validate the input data by checking for invalid characters.

        :param input_data: The input data to be validated.
        :param mask_characters: Optional set of accepted mask characters.
               If None, the default set {'.'', '-', '/', ' '} will be used.
        :raises ValueError: If invalid character(s) are found in the input data.
        """
        if input_data is None:
            raise ValueError('Invalid input.')

        mask_characters = mask_characters or {'.', '-', '/', ' '}
        non_digits = set([c for c in input_data if not c.isdigit()])

        if len(non_digits.difference(mask_characters)) > 0:
            raise ValueError('Invalid character(s) found in the document string.')

    @staticmethod
    def _fill_with_zeros(doc: str, digits: int) -> str:
        """Fill a document string with leading zeros if necessary.

        :param doc: The document string.
        :param digits: The number of digits in the desired document string.
        :return: The document string with leading zeros.
        """
        if doc is None:
            raise ValueError('Invalid input.')

        return doc.zfill(digits)

    def __hash__(self) -> int:
        """Return the hash value of the Document object.

        :return: The hash value.
        """
        return hash(self._plain)

    def __eq__(self, other: 'Document') -> bool:
        """Check if two CPF objects are equal.

        :param other: The other CPF object to compare.
        :return: True if the objects are equal, False otherwise.
        """
        return self._plain == other._plain

    def __repr__(self) -> str:
        """Return the string representation of the object.

        :return: The plain document string.
        """
        return self.plain

    def __init__(self, doc: str):
        """Initialize a document object.

        :param doc: The document string.
        :raises ValueError: If the document string is invalid.
        """
        self._plain = self.sanitize(doc)
        self._masked = self.apply_mask(self._plain)
