# doc_br

Uma biblioteca para manipulação de documentos brasileiros.

[![Coverage Status](https://coveralls.io/repos/github/lucaschf/doc_br/badge.svg)](https://coveralls.io/github/lucaschf/doc_br)

## Instalação

Você pode instalar a biblioteca `doc_br` usando pip:

```bash
pip install doc_br
```

## Uso

### CPF e CNPJ

A biblioteca `doc_br` fornece classes para manipulação de CPF e CNPJ. Aqui está um exemplo de como
usá-las:

```python
from doc_br.types import CPF, CNPJ

try:
    cpf = CPF('012.345.678-90')
    print(cpf.plain)  # Retorna a string padronizada
    print(cpf.masked)  # Retorna a string com mascara
except ValueError as e:
    print(str(e))  # Trata a exceção caso o CPF seja inválido

try:
    cnpj = CNPJ('11.222.333/0001-81')
    print(cnpj.plain)  # Retorna a string padronizada
    print(cnpj.masked)  # Retorna a string com mascara
except ValueError as e:
    print(str(e))  # Trata a exceção caso o CNPJ seja inválido
```

Ao instanciar um CPF ou CNPJ com uma string inválida, será lançada uma exceção `ValueError`.
Portanto, é importante envolver as instâncias dessas classes em um bloco `try-except` para tratar a
exceção, caso o documento seja inválido.

## Métodos do Documento

A classe `Document` possui os seguintes métodos:

- `sanitize(doc: str) -> str`: Sanitiza um documento removendo formatação e caracteres indesejados.
  Retorna o documento sanitizado e padronizado.
- `validate(doc: str) -> None`: Valida um documento.
  Lança uma exceção ValueError se o documento for inválido.
- `mask(doc: str) -> str`: Aplica uma máscara a um documento.
  Retorna o documento com a máscara aplicada.
- `un_mask(doc: str, validate: bool) -> str`: Remove a máscara de um documento.
  Se validate for True, realiza a validação do documento após a remoção da máscara.
  Retorna o documento desmascarado.
- `generate() -> CPF`:  CPF: Gera um CPF aleatório.

### DocumentUtils

A biblioteca também fornece a classe `DocumentUtils`, que oferece utilitários para geração e
validação de documentos. Aqui está um exemplo de como usá-la para gerar CPFs:

```python
from doc_br import CPFDocumentUtils

cpf_utils = CPFDocumentUtils()
cpf = cpf_utils.generate()
print(cpf)

cpf_list = cpf_utils.generate_documents(n=5)
print(cpf_list)
```

Nesse exemplo, estamos usando o `CPFDocumentUtils` para gerar um CPF aleatório e uma lista de 5 
CPFs aleatórios.
A classe `DocumentUtils` oferece métodos convenientes para geração de 
documentos, permitindo especificar o número de documentos a serem gerados.

## Métodos do DocumentUtils

A classe `DocumentUtils` possui os seguintes métodos:

- `generate(mask: bool = False) -> Document`: Generate a random document string.
- `generate_documents(n

  : int = 1, mask: bool = False) -> Set[Document]`: Generate a set of document strings.
  - `normalize(doc: str) -> str`: Normalize a document string.
  - `validate(doc: str) -> None`: Validate a document string.
  - `mask(doc: str) -> str`: Apply a mask to a document string.
  - `un_mask(doc: str) -> str`: Remove the mask from a document string.

Certifique-se de tratar as exceções apropriadas ao usar esses métodos para manipulação de
documentos.
