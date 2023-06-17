from abc import ABC, abstractmethod
from typing import Set

from doc_br.types.doc import Document


class DocumentUtils(ABC):
    """
    Abstract base class for document strings.

    This class defines the basic interface for working with documents, including methods
    for normalization, masking, validation, and generation. Concrete subclasses must implement
    these methods to handle specific types of documents.
    """

    @abstractmethod
    def sanitize(self, doc: str) -> str:
        """
        Sanitize the document string.

        :param doc: The document string to be normalized.
        :return: The sanitized document string.
        :raises ValueError: If the document string is invalid.
        """

    @abstractmethod
    def mask(self, doc: str) -> str:
        """
        Mask the document string.

        :param doc: The document string to be masked.
        :return: The masked document string.
        :raises ValueError: If the document string is invalid.
        """

    @abstractmethod
    def un_mask(self, doc: str) -> str:
        """
        Remove the mask from the document string.

        :param doc: The document string to be masked.
        :return: The masked document string.
        :raises ValueError: If the document string is invalid.
        """

    @abstractmethod
    def validate(self, doc: str) -> None:
        """
        Validate the document string.

        :param doc: The document string to be validated.
        :raises ValueError: If the document is invalid.
        """

    @abstractmethod
    def generate(self) -> Document:
        """
        Generate a new document.

        :return: The generated document.
        """

    def generate_documents(self, n: int = 1) -> Set[Document]:
        """
        Generate a set of documents.

        :param n: The number of documents to generate. Default to 1.
        :return: A set of generated documents.
        """
        docs = set()

        while len(docs) < n:
            docs.add(self.generate())

        return docs
