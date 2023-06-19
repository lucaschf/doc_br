import pytest
import validate_docbr

from doc_br.types import CNPJ


@pytest.fixture
def valid_cnpj() -> CNPJ:
    return CNPJ(validate_docbr.CNPJ().generate())


@pytest.fixture
def valid_cnpj_str():
    return validate_docbr.CNPJ().generate(mask=True)


@pytest.mark.parametrize(
    "invalid_cnpj",
    ['12345678901', '', None, 'abcd.efgh/ijkl-mn', '11.111.111/1111-11']
)
def test_sanitize_invalid_inputs(invalid_cnpj, valid_cnpj):
    with pytest.raises(ValueError):
        valid_cnpj.sanitize(invalid_cnpj)


def test_sanitize_valid_inputs(valid_cnpj, valid_cnpj_str):
    plain = ''.join([c for c in valid_cnpj.masked if c.isdigit()])
    assert valid_cnpj.sanitize(valid_cnpj.masked) == plain


@pytest.mark.parametrize(
    "invalid_cnpj",
    ['12345678901', '', None, 'abcd.efgh/ijkl-mn', '11.111.111/1111-11']
)
def test_validate(invalid_cnpj, valid_cnpj):
    with pytest.raises(ValueError):
        valid_cnpj.validate(invalid_cnpj)

    assert valid_cnpj.validate(valid_cnpj.plain) is None


def test_mask(valid_cnpj, valid_cnpj_str):
    plain = ''.join([c for c in valid_cnpj_str if c.isdigit()])

    assert valid_cnpj.mask(plain) == valid_cnpj_str
    with pytest.raises(ValueError):
        valid_cnpj.mask(None)


def test_un_mask(valid_cnpj):
    plain = ''.join([c for c in valid_cnpj.masked if c.isdigit()])
    assert valid_cnpj.un_mask(valid_cnpj.masked, False) == plain

    with pytest.raises(ValueError):
        valid_cnpj.un_mask('12.345.678/9012-34', True)


def test_generate(valid_cnpj):
    assert validate_docbr.CNPJ().validate(valid_cnpj.plain)


@pytest.mark.parametrize(
    "invalid_cnpj",
    ['12345678901', '', None, 'abcd.efgh/ijkl-mn', '11.111.111/1111-11']
)
def test_init(invalid_cnpj):
    with pytest.raises(ValueError):
        CNPJ(invalid_cnpj)

    assert valid_cnpj is not None


def test_hash(valid_cnpj):
    assert hash(valid_cnpj) == hash(valid_cnpj.plain)


def test_eq():
    cnpj1 = CNPJ.generate()
    cnpj2 = CNPJ(cnpj1.plain)
    cnpj3 = CNPJ.generate()
    assert cnpj1 == cnpj2
    assert cnpj1 != cnpj3


def test_repr(valid_cnpj):
    assert repr(valid_cnpj) == valid_cnpj.plain
