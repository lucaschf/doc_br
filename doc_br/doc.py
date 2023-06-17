from abc import ABC, abstractmethod
from typing import Set


class Document(ABC):
    """
    Abstract base class for document objects.

    Provides methods for sanitizing, masking, unmasking, and validating document strings.
    """

    @property
    @abstractmethod
    def plain(self) -> str:
        """Get the plain document string."""

    @property
    @abstractmethod
    def masked(self) -> str:
        """Get the masked document string."""

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
    def mask(self, doc: str) -> str:
        """
        Apply a mask to the document string.

        :param doc: The document string to be masked.
        :return: The masked document string.
        """

    @abstractmethod
    def un_mask(self, doc: str, validate: bool) -> str:
        """
        Remove the mask from the document string.

        :param doc: The masked document string.
        :param validate: Whether to validate the unmasked document string.
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
    def _validate_input(
        input_data: str | None, accepted_characters: Set[str] | None = None
    ) -> None:
        """
        Validate the input data by checking for invalid characters.

        :param input_data: The input data to be validated.
        :param accepted_characters: Optional set of accepted characters.
                                    If None, the default set {'.'', '-', '/', ' '} will be used.
        :raises ValueError: If invalid character(s) are found in the input data.
        """
