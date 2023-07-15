from doc_br.types import CNPJ
from doc_br.utils.document_utils import DocumentUtils


class CNPJDocumentUtils(DocumentUtils):
    """
    Utility class for CNPJ documents.

    Provides methods for generating, sanitizing, validating, and masking CNPJ document strings.
    """

    def generate(self, mask: bool = False) -> CNPJ:
        """Generate a random CNPJ document string.

        :param mask: If True, return the masked CNPJ document.
                    If False, return the plain CNPJ document.
        :return: The generated CNPJ document.
        """
        return CNPJ.generate()

    def sanitize(self, doc: str) -> str:
        """Sanitize a CNPJ document string.

        This method is a way to standardize the document string.
        If you just want to remove any formatting or unwanted characters but not standardize,
        use the un_mask method.

        :param doc: The CNPJ document to be normalized.
        :returns: The normalized CNPJ document.
        :raises ValueError: If the document is invalid.
        """
        return CNPJ(doc).plain

    def validate(self, doc: str) -> None:
        """Validate a CNPJ document string.

        :param doc: The CNPJ document to be validated.
        :raise ValueError: If the document is invalid.
        """
        CNPJ(doc)

    def apply_mask(self, doc: str) -> str:
        """Mask a CNPJ document string.

        :param doc: The CNPJ document to be masked.
        :return: The masked CNPJ document.
        :raise ValueError: If the document is invalid.
        """
        return CNPJ(doc).masked

    def remove_mask(self, doc: str) -> str:
        """Unmask a CNPJ document string.

        :param doc: The CNPJ document to be unmasked.
        :return: The unmasked CNPJ document.
        :raise ValueError: If the document is invalid.
        """
        return CNPJ(doc).plain
