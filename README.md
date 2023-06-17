# doc_br

Uma biblioteca para manipulação de documentos brasileiros.

## Instalação

Você pode instalar a biblioteca `doc_br` usando pip:

```bash
pip install doc_br
```


## Uso

Aqui está um exemplo de como usar a biblioteca `doc_br`:

```python
from doc_br import CPF, CNPJ

cpf = CPF('012.345.678-90')
print(cpf.valido)  # Retorna True se o CPF for válido

cnpj = CNPJ('11.222.333/0001-81')
print(cnpj.valido)  # Retorna True se o CNPJ for válido
