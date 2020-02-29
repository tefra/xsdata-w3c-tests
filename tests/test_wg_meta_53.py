import pytest

from tests.utils import assert_bindings


def test_sg_abstract_edc_ee1s_xml():

    assert_bindings(
        schema="wgData/sg/edc.xsd",
        is_valid=True,
        instance="wgData/sg/ee1s.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.1",
    )


def test_sg_abstract_edc_ee1t_xml():

    assert_bindings(
        schema="wgData/sg/edc.xsd",
        is_valid=True,
        instance="wgData/sg/ee1t.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.1",
    )


def test_sg_abstract_edc_ee1i_xml():

    assert_bindings(
        schema="wgData/sg/edc.xsd",
        is_valid=True,
        instance="wgData/sg/ee1i.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.1",
    )


def test_sg_abstract_edc_e1se1s_xml():

    assert_bindings(
        schema="wgData/sg/edc.xsd",
        is_valid=True,
        instance="wgData/sg/e1se1s.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.1",
    )


def test_sg_abstract_edc_e1se1t_xml():

    assert_bindings(
        schema="wgData/sg/edc.xsd",
        is_valid=True,
        instance="wgData/sg/e1se1t.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.1",
    )


def test_sg_abstract_edc_e1se1i_xml():

    assert_bindings(
        schema="wgData/sg/edc.xsd",
        is_valid=True,
        instance="wgData/sg/e1se1.xml",
        instance_is_valid=False,
        class_name="",
        version="1.1",
    )


def test_sg_abstract_edc_e1ite1s_xml():

    assert_bindings(
        schema="wgData/sg/edc.xsd",
        is_valid=True,
        instance="wgData/sg/e1ite1s.xml",
        instance_is_valid=False,
        class_name="",
        version="1.1",
    )


def test_sg_abstract_edc_e1ite1t_xml():

    assert_bindings(
        schema="wgData/sg/edc.xsd",
        is_valid=True,
        instance="wgData/sg/e1ite1t.xml",
        instance_is_valid=False,
        class_name="",
        version="1.1",
    )


def test_sg_abstract_edc_e1ite1i_xml():

    assert_bindings(
        schema="wgData/sg/edc.xsd",
        is_valid=True,
        instance="wgData/sg/e1ite1.xml",
        instance_is_valid=False,
        class_name="",
        version="1.1",
    )


def test_sg_abstract_edc_e1ie1s_xml():

    assert_bindings(
        schema="wgData/sg/edc.xsd",
        is_valid=True,
        instance="wgData/sg/e1ie1s.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.1",
    )


def test_sg_abstract_edc_e1ie1t_xml():

    assert_bindings(
        schema="wgData/sg/edc.xsd",
        is_valid=True,
        instance="wgData/sg/e1ie1t.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.1",
    )


def test_sg_abstract_edc_e1ie1i_xml():

    assert_bindings(
        schema="wgData/sg/edc.xsd",
        is_valid=True,
        instance="wgData/sg/e1ie1.xml",
        instance_is_valid=False,
        class_name="",
        version="1.1",
    )


def test_sg_abstract_upa2_e1_xml():

    assert_bindings(
        schema="wgData/sg/upa2.xsd",
        is_valid=True,
        instance="wgData/sg/e1.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0 1.1",
    )


@pytest.mark.xfail
def test_sg_abstract_upa2_e1bis_xml():

    assert_bindings(
        schema="wgData/sg/upa2.xsd",
        is_valid=True,
        instance="wgData/sg/e1.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0 1.1",
    )


def test_sg_abstract_upa2_e1token_xml():

    assert_bindings(
        schema="wgData/sg/upa2.xsd",
        is_valid=True,
        instance="wgData/sg/e1token.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0 1.1",
    )


def test_sg_abstract_upa2_e1short_xml():

    assert_bindings(
        schema="wgData/sg/upa2.xsd",
        is_valid=True,
        instance="wgData/sg/e1short.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0 1.1",
    )


def test_sg_abstract_upa_e1_xml():

    assert_bindings(
        schema="wgData/sg/upa.xsd",
        is_valid=True,
        instance="wgData/sg/e1.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0 1.1",
    )


def test_sg_abstract_upa_e1token_xml():

    assert_bindings(
        schema="wgData/sg/upa.xsd",
        is_valid=True,
        instance="wgData/sg/e1token.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0 1.1",
    )


def test_sg_abstract_upa_e1short_xml():

    assert_bindings(
        schema="wgData/sg/upa.xsd",
        is_valid=True,
        instance="wgData/sg/e1short.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0 1.1",
    )


def test_sg_and_defined_sibling_3_sns1a():

    assert_bindings(
        schema="wgData/sg/snbranch.xsd",
        is_valid=True,
        instance="wgData/sg/sns1a.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0 1.1",
    )


@pytest.mark.xfail
def test_sg_and_defined_sibling_3_sns1b():

    assert_bindings(
        schema="wgData/sg/snbranch.xsd",
        is_valid=True,
        instance="wgData/sg/sns1b.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0 1.1",
    )


def test_sg_and_defined_sibling_3_sns1c():

    assert_bindings(
        schema="wgData/sg/snbranch.xsd",
        is_valid=True,
        instance="wgData/sg/sns1c.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0 1.1",
    )


def test_sg_and_defined_sibling_3_snn1a():

    assert_bindings(
        schema="wgData/sg/snbranch.xsd",
        is_valid=True,
        instance="wgData/sg/snn1a.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0 1.1",
    )


def test_sg_and_defined_sibling_3_snn1b():

    assert_bindings(
        schema="wgData/sg/snbranch.xsd",
        is_valid=True,
        instance="wgData/sg/snn1b.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0 1.1",
    )


@pytest.mark.xfail
def test_sg_and_defined_sibling_3_snn1c():

    assert_bindings(
        schema="wgData/sg/snbranch.xsd",
        is_valid=True,
        instance="wgData/sg/snn1c.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0 1.1",
    )


@pytest.mark.xfail
def test_sg_and_defined_sibling_3_snea():

    assert_bindings(
        schema="wgData/sg/snbranch.xsd",
        is_valid=True,
        instance="wgData/sg/snea.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0 1.1",
    )


def test_sg_and_defined_sibling_3_sneb():

    assert_bindings(
        schema="wgData/sg/snbranch.xsd",
        is_valid=True,
        instance="wgData/sg/sneb.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0 1.1",
    )


def test_sg_and_defined_sibling_3_snec():

    assert_bindings(
        schema="wgData/sg/snbranch.xsd",
        is_valid=True,
        instance="wgData/sg/snec.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0 1.1",
    )


@pytest.mark.xfail
def test_sg_and_defined_sibling_2_esn():

    assert_bindings(
        schema="wgData/sg/negsn.xsd",
        is_valid=True,
        instance="wgData/sg/esn.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0 1.1",
    )


def test_sg_and_defined_sibling_2_nsn():

    assert_bindings(
        schema="wgData/sg/negsn.xsd",
        is_valid=True,
        instance="wgData/sg/nsn.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0 1.1",
    )


def test_sg_and_defined_sibling_2_ssn():

    assert_bindings(
        schema="wgData/sg/negsn.xsd",
        is_valid=True,
        instance="wgData/sg/ssn.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0 1.1",
    )


@pytest.mark.xfail
def test_sg_and_defined_sibling_2_n1sn():

    assert_bindings(
        schema="wgData/sg/negsn.xsd",
        is_valid=True,
        instance="wgData/sg/n1sn.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0 1.1",
    )


def test_sg_and_defined_sibling_2_s1sn():

    assert_bindings(
        schema="wgData/sg/negsn.xsd",
        is_valid=True,
        instance="wgData/sg/s1sn.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0 1.1",
    )


@pytest.mark.xfail
def test_sg_and_defined_sibling_1_sn():

    assert_bindings(
        schema="wgData/sg/snneg.xsd",
        is_valid=True,
        instance="wgData/sg/sn.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0 1.1",
    )


@pytest.mark.xfail
def test_sg_and_defined_sibling_1_s1n():

    assert_bindings(
        schema="wgData/sg/snneg.xsd",
        is_valid=True,
        instance="wgData/sg/s1n.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0 1.1",
    )


def test_sg_and_defined_sibling_1_sn1():

    assert_bindings(
        schema="wgData/sg/snneg.xsd",
        is_valid=True,
        instance="wgData/sg/sn1.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0 1.1",
    )


@pytest.mark.xfail
def test_sg_and_defined_sibling_1_sne():

    assert_bindings(
        schema="wgData/sg/snneg.xsd",
        is_valid=True,
        instance="wgData/sg/sne.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0 1.1",
    )


def test_sg_and_defined_sibling_1_snn():

    assert_bindings(
        schema="wgData/sg/snneg.xsd",
        is_valid=True,
        instance="wgData/sg/snn.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0 1.1",
    )


def test_sg_and_defined_sibling_1_sns():

    assert_bindings(
        schema="wgData/sg/snneg.xsd",
        is_valid=True,
        instance="wgData/sg/sns.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0 1.1",
    )


@pytest.mark.xfail
def test_sg_and_defined_sibling_1_snn1():

    assert_bindings(
        schema="wgData/sg/snneg.xsd",
        is_valid=True,
        instance="wgData/sg/snn1.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0 1.1",
    )


def test_sg_and_defined_sibling_1_sns1():

    assert_bindings(
        schema="wgData/sg/snneg.xsd",
        is_valid=True,
        instance="wgData/sg/sns1.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0 1.1",
    )


def test_iri_001_uri_3986_valid_001():

    assert_bindings(
        schema="wgData/iri/ElementDeclarations.xsd",
        is_valid=True,
        instance="wgData/iri/URI-3986-valid-001.xml",
        instance_is_valid=True,
        class_name="Uri3986",
        version="1.0",
    )


def test_iri_001_uri_3986_valid_002():

    assert_bindings(
        schema="wgData/iri/ElementDeclarations.xsd",
        is_valid=True,
        instance="wgData/iri/URI-3986-valid-002.xml",
        instance_is_valid=True,
        class_name="Uri3986",
        version="1.0",
    )


def test_iri_001_uri_3986_valid_003():

    assert_bindings(
        schema="wgData/iri/ElementDeclarations.xsd",
        is_valid=True,
        instance="wgData/iri/URI-3986-valid-003.xml",
        instance_is_valid=True,
        class_name="Uri3986",
        version="1.0",
    )


def test_iri_001_uri_3986_invalid_001():

    assert_bindings(
        schema="wgData/iri/ElementDeclarations.xsd",
        is_valid=True,
        instance="wgData/iri/URI-3986-invalid-001.xml",
        instance_is_valid=False,
        class_name="Uri3986",
        version="1.0",
    )


def test_iri_001_uri_3986_invalid_002():

    assert_bindings(
        schema="wgData/iri/ElementDeclarations.xsd",
        is_valid=True,
        instance="wgData/iri/URI-3986-invalid-002.xml",
        instance_is_valid=False,
        class_name="Uri3986",
        version="1.0",
    )


def test_iri_001_uri_3986_invalid_003():

    assert_bindings(
        schema="wgData/iri/ElementDeclarations.xsd",
        is_valid=True,
        instance="wgData/iri/URI-3986-invalid-003.xml",
        instance_is_valid=False,
        class_name="Uri3986",
        version="1.0",
    )


def test_iri_001_absolute_uri_3986_valid_001():

    assert_bindings(
        schema="wgData/iri/ElementDeclarations.xsd",
        is_valid=True,
        instance="wgData/iri/absolute-URI-3986-valid-001.xml",
        instance_is_valid=True,
        class_name="AbsoluteUri3986",
        version="1.0",
    )


def test_iri_001_absolute_uri_3986_valid_002():

    assert_bindings(
        schema="wgData/iri/ElementDeclarations.xsd",
        is_valid=True,
        instance="wgData/iri/absolute-URI-3986-valid-002.xml",
        instance_is_valid=True,
        class_name="AbsoluteUri3986",
        version="1.0",
    )


def test_iri_001_absolute_uri_3986_valid_003():

    assert_bindings(
        schema="wgData/iri/ElementDeclarations.xsd",
        is_valid=True,
        instance="wgData/iri/absolute-URI-3986-valid-003.xml",
        instance_is_valid=True,
        class_name="AbsoluteUri3986",
        version="1.0",
    )


def test_iri_001_absolute_uri_3986_invalid_001():

    assert_bindings(
        schema="wgData/iri/ElementDeclarations.xsd",
        is_valid=True,
        instance="wgData/iri/absolute-URI-3986-invalid-001.xml",
        instance_is_valid=False,
        class_name="AbsoluteUri3986",
        version="1.0",
    )


def test_iri_001_absolute_uri_3986_invalid_002():

    assert_bindings(
        schema="wgData/iri/ElementDeclarations.xsd",
        is_valid=True,
        instance="wgData/iri/absolute-URI-3986-invalid-002.xml",
        instance_is_valid=False,
        class_name="AbsoluteUri3986",
        version="1.0",
    )


def test_iri_001_absolute_uri_3986_invalid_003():

    assert_bindings(
        schema="wgData/iri/ElementDeclarations.xsd",
        is_valid=True,
        instance="wgData/iri/absolute-URI-3986-invalid-003.xml",
        instance_is_valid=False,
        class_name="AbsoluteUri3986",
        version="1.0",
    )
