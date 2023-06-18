import pytest

from doc_br.types import CPF


def test_cpf_creation():
    # Test valid CPF creation
    valid_cpf = "52998224725"  # valid CPF number
    cpf = CPF(valid_cpf)
    assert cpf.plain == valid_cpf

    # Test masked CPF
    assert cpf.masked == "529.982.247-25"


def test_invalid_cpf_creation():
    # Test invalid CPF creation
    invalid_cpf = "11111111111"  # invalid CPF number
    with pytest.raises(ValueError):
        CPF(invalid_cpf)

    with pytest.raises(ValueError):
        CPF('None')


def test_cpf_generation():
    # Test CPF generation
    cpf = CPF.generate()
    assert len(cpf.plain) == 11  # A valid CPF should have 11 digits


def test_cpf_equality():
    # Test CPF equality
    cpf1 = CPF("52998224725")
    cpf2 = CPF("52998224725")
    assert cpf1 == cpf2

    # Different CPFs should not be equal
    cpf3 = CPF.generate()
    assert cpf1 != cpf3


def test_cpf_hash():
    # Test CPF hash
    cpf1 = CPF("52998224725")
    cpf2 = CPF("52998224725")
    assert hash(cpf1) == hash(cpf2)

    # Different CPFs should not have the same hash
    cpf3 = CPF.generate()
    assert hash(cpf1) != hash(cpf3)


def test_cpf_repr():
    # Test CPF repr
    cpf = CPF("52998224725")
    assert repr(cpf) == "52998224725"


def test_un_mask():
    cpf = CPF("52998224725")
    assert cpf.un_mask(cpf.masked, validate=True) == "52998224725"

    cpf = CPF("52998224725")
    assert cpf.un_mask(cpf.masked, validate=False) == "52998224725"

    with pytest.raises(ValueError):
        cpf.un_mask('111111111', validate=True)

    assert cpf.un_mask('111111111', validate=False) == '111111111'

    with pytest.raises(ValueError):
        # noinspection PyTypeChecker
        cpf.un_mask(None, validate=True)


def test_sanitize():
    # Test a plain, valid CPF
    cpf = CPF("52998224725")
    assert cpf.sanitize("52998224725") == "52998224725"

    # Test a masked, valid CPF
    assert cpf.sanitize("529.982.247-25") == "52998224725"

    # Test a CPF that needs to be filled with zeros
    assert cpf.sanitize("337231923") == "00337231923"

    # Test a CPF that's None
    with pytest.raises(ValueError):
        # noinspection PyTypeChecker
        cpf.sanitize(None)

    # Test an invalid CPF
    with pytest.raises(ValueError):
        cpf.sanitize("11111111111")
