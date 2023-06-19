import pytest
import validate_docbr

from doc_br.types import CPF


@pytest.fixture
def valid_cpf():
    return CPF(validate_docbr.CPF().generate())


@pytest.fixture
def valid_cpf_str():
    return validate_docbr.CPF().generate(mask=True)


def test_cpf_creation(valid_cpf, valid_cpf_str):
    plain = ''.join([c for c in valid_cpf.masked if c.isdigit()])
    assert valid_cpf.plain == plain
    assert valid_cpf.masked == validate_docbr.CPF().mask(plain)


@pytest.mark.parametrize("invalid_cpf", ['11111111111', '', None, 'abcd.efgh.ijkl-mn'])
def test_invalid_cpf_creation(invalid_cpf):
    with pytest.raises(ValueError):
        CPF(invalid_cpf)


def test_cpf_generation(valid_cpf):
    assert len(valid_cpf.plain) == 11


def test_cpf_equality():
    cpf1 = CPF.generate()
    cpf2 = CPF(cpf1.plain)
    cpf3 = CPF.generate()
    assert cpf1 == cpf2
    assert cpf1 != cpf3


def test_cpf_hash():
    cpf1 = CPF.generate()
    cpf2 = CPF(cpf1.plain)
    cpf3 = CPF.generate()
    assert hash(cpf1) == hash(cpf2)
    assert hash(cpf1) != hash(cpf3)


def test_cpf_repr(valid_cpf):
    assert repr(valid_cpf) == valid_cpf.plain


def test_un_mask(valid_cpf):
    assert valid_cpf.un_mask(valid_cpf.masked, validate=True) == valid_cpf.plain
    assert valid_cpf.un_mask(valid_cpf.masked, validate=False) == valid_cpf.plain

    with pytest.raises(ValueError):
        valid_cpf.un_mask('111111111', validate=True)

    assert valid_cpf.un_mask('111111111', validate=False) == '111111111'

    with pytest.raises(ValueError):
        valid_cpf.un_mask(None, validate=True)


def test_sanitize(valid_cpf, valid_cpf_str):
    plain = ''.join([c for c in valid_cpf_str if c.isdigit()])
    assert valid_cpf.sanitize(valid_cpf_str) == plain
    assert valid_cpf.sanitize("529.982.247-25") == '52998224725'
    assert valid_cpf.sanitize("337231923") == "00337231923"

    with pytest.raises(ValueError):
        valid_cpf.sanitize(None)

    with pytest.raises(ValueError):
        valid_cpf.sanitize("11111111111")
