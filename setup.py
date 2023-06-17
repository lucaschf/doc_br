from setuptools import find_packages, setup

setup(
    name='doc_br',
    version='0.0.1',
    url='https://github.com/lucaschf/doc_br',
    author='Lucas Cristovam',
    author_email='lucaschfonseca@gmail.com',
    description='Uma biblioteca para manipulação e validação de CPF e CNPJ',
    packages=find_packages(),
    install_requires=['validate-docbr'],
)
