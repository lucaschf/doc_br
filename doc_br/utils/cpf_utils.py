from doc_br.types import CPF
from doc_br.utils.document_utils import DocumentUtils


class CPFDocumentUtils(DocumentUtils):
    """
    Utility class for CPF documents.

    Provides methods for generating, sanitizing, validating, and masking CPF document strings.
    """

    def generate(self, mask: bool = False) -> CPF:
        """Generate a random CPF document string.

        :param mask: If True, return the masked CPF document.
                    If False, return the plain CPF document.
        :return: The generated CPF document.
        """
        return CPF.generate()

    def sanitize(self, doc: str) -> str:
        """Sanitize a CPF document string.

        This method is a way to standardize the document string.
        If you just want to remove any formatting or unwanted characters but not standardize,
        use the un_mask method.

        :param doc: The CPF document to be normalized.
        :returns: The normalized CPF document.
        :raises ValueError: If the document is invalid.
        """
        return CPF(doc).plain

    def validate(self, doc: str) -> None:
        """Validate a CPF document string.

        :param doc: The CPF document to be validated.
        :raise ValueError: If the document is invalid.
        """
        CPF(doc)

    def mask(self, doc: str) -> str:
        """Mask a CPF document string.

        :param doc: The CPF document to be masked.
        :return: The masked CPF document.
        :raise ValueError: If the document is invalid.
        """
        return CPF(doc).masked

    def un_mask(self, doc: str) -> str:
        """Unmask a CPF document string.

        :param doc: The CPF document to be unmasked.
        :return: The unmasked CPF document.
        :raise ValueError: If the document is invalid.
        """
        return CPF(doc).plain
