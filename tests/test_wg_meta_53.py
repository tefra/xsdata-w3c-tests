import pytest

from tests.utils import assert_bindings


@pytest.mark.skip(reason="Invalid instance")
def test_sg_abstract_edc_ee1s_xml(save_xml):

    assert_bindings(
        schema="wgData/sg/edc.xsd",
        instance="wgData/sg/ee1s.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_sg_abstract_edc_ee1t_xml(save_xml):

    assert_bindings(
        schema="wgData/sg/edc.xsd",
        instance="wgData/sg/ee1t.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


def test_sg_abstract_edc_ee1i_xml(save_xml):

    assert_bindings(
        schema="wgData/sg/edc.xsd",
        instance="wgData/sg/ee1i.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_sg_abstract_edc_e1se1s_xml(save_xml):

    assert_bindings(
        schema="wgData/sg/edc.xsd",
        instance="wgData/sg/e1se1s.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_sg_abstract_edc_e1se1t_xml(save_xml):

    assert_bindings(
        schema="wgData/sg/edc.xsd",
        instance="wgData/sg/e1se1t.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_sg_abstract_edc_e1se1i_xml(save_xml):

    assert_bindings(
        schema="wgData/sg/edc.xsd",
        instance="wgData/sg/e1se1.xml",
        class_name="",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_sg_abstract_edc_e1ite1s_xml(save_xml):

    assert_bindings(
        schema="wgData/sg/edc.xsd",
        instance="wgData/sg/e1ite1s.xml",
        class_name="",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_sg_abstract_edc_e1ite1t_xml(save_xml):

    assert_bindings(
        schema="wgData/sg/edc.xsd",
        instance="wgData/sg/e1ite1t.xml",
        class_name="",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_sg_abstract_edc_e1ite1i_xml(save_xml):

    assert_bindings(
        schema="wgData/sg/edc.xsd",
        instance="wgData/sg/e1ite1.xml",
        class_name="",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_sg_abstract_edc_e1ie1s_xml(save_xml):

    assert_bindings(
        schema="wgData/sg/edc.xsd",
        instance="wgData/sg/e1ie1s.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_sg_abstract_edc_e1ie1t_xml(save_xml):

    assert_bindings(
        schema="wgData/sg/edc.xsd",
        instance="wgData/sg/e1ie1t.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_sg_abstract_edc_e1ie1i_xml(save_xml):

    assert_bindings(
        schema="wgData/sg/edc.xsd",
        instance="wgData/sg/e1ie1.xml",
        class_name="",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_sg_abstract_upa2_e1_xml(save_xml):

    assert_bindings(
        schema="wgData/sg/upa2.xsd",
        instance="wgData/sg/e1.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


def test_sg_abstract_upa2_e1bis_xml(save_xml):

    assert_bindings(
        schema="wgData/sg/upa2.xsd",
        instance="wgData/sg/e1.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_sg_abstract_upa2_e1token_xml(save_xml):

    assert_bindings(
        schema="wgData/sg/upa2.xsd",
        instance="wgData/sg/e1token.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


def test_sg_abstract_upa2_e1short_xml(save_xml):

    assert_bindings(
        schema="wgData/sg/upa2.xsd",
        instance="wgData/sg/e1short.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


def test_sg_abstract_upa_e1_xml(save_xml):

    assert_bindings(
        schema="wgData/sg/upa.xsd",
        instance="wgData/sg/e1.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


def test_sg_abstract_upa_e1token_xml(save_xml):

    assert_bindings(
        schema="wgData/sg/upa.xsd",
        instance="wgData/sg/e1token.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_sg_abstract_upa_e1short_xml(save_xml):

    assert_bindings(
        schema="wgData/sg/upa.xsd",
        instance="wgData/sg/e1short.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_sg_and_defined_sibling_3_sns1a(save_xml):

    assert_bindings(
        schema="wgData/sg/snbranch.xsd",
        instance="wgData/sg/sns1a.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.xfail
def test_sg_and_defined_sibling_3_sns1b(save_xml):

    assert_bindings(
        schema="wgData/sg/snbranch.xsd",
        instance="wgData/sg/sns1b.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_sg_and_defined_sibling_3_sns1c(save_xml):

    assert_bindings(
        schema="wgData/sg/snbranch.xsd",
        instance="wgData/sg/sns1c.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_sg_and_defined_sibling_3_snn1a(save_xml):

    assert_bindings(
        schema="wgData/sg/snbranch.xsd",
        instance="wgData/sg/snn1a.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_sg_and_defined_sibling_3_snn1b(save_xml):

    assert_bindings(
        schema="wgData/sg/snbranch.xsd",
        instance="wgData/sg/snn1b.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


def test_sg_and_defined_sibling_3_snn1c(save_xml):

    assert_bindings(
        schema="wgData/sg/snbranch.xsd",
        instance="wgData/sg/snn1c.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


def test_sg_and_defined_sibling_3_snea(save_xml):

    assert_bindings(
        schema="wgData/sg/snbranch.xsd",
        instance="wgData/sg/snea.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_sg_and_defined_sibling_3_sneb(save_xml):

    assert_bindings(
        schema="wgData/sg/snbranch.xsd",
        instance="wgData/sg/sneb.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_sg_and_defined_sibling_3_snec(save_xml):

    assert_bindings(
        schema="wgData/sg/snbranch.xsd",
        instance="wgData/sg/snec.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


def test_sg_and_defined_sibling_2_esn(save_xml):

    assert_bindings(
        schema="wgData/sg/negsn.xsd",
        instance="wgData/sg/esn.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_sg_and_defined_sibling_2_nsn(save_xml):

    assert_bindings(
        schema="wgData/sg/negsn.xsd",
        instance="wgData/sg/nsn.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_sg_and_defined_sibling_2_ssn(save_xml):

    assert_bindings(
        schema="wgData/sg/negsn.xsd",
        instance="wgData/sg/ssn.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


def test_sg_and_defined_sibling_2_n1sn(save_xml):

    assert_bindings(
        schema="wgData/sg/negsn.xsd",
        instance="wgData/sg/n1sn.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_sg_and_defined_sibling_2_s1sn(save_xml):

    assert_bindings(
        schema="wgData/sg/negsn.xsd",
        instance="wgData/sg/s1sn.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


def test_sg_and_defined_sibling_1_sn(save_xml):

    assert_bindings(
        schema="wgData/sg/snneg.xsd",
        instance="wgData/sg/sn.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


def test_sg_and_defined_sibling_1_s1n(save_xml):

    assert_bindings(
        schema="wgData/sg/snneg.xsd",
        instance="wgData/sg/s1n.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_sg_and_defined_sibling_1_sn1(save_xml):

    assert_bindings(
        schema="wgData/sg/snneg.xsd",
        instance="wgData/sg/sn1.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


def test_sg_and_defined_sibling_1_sne(save_xml):

    assert_bindings(
        schema="wgData/sg/snneg.xsd",
        instance="wgData/sg/sne.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_sg_and_defined_sibling_1_snn(save_xml):

    assert_bindings(
        schema="wgData/sg/snneg.xsd",
        instance="wgData/sg/snn.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_sg_and_defined_sibling_1_sns(save_xml):

    assert_bindings(
        schema="wgData/sg/snneg.xsd",
        instance="wgData/sg/sns.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


def test_sg_and_defined_sibling_1_snn1(save_xml):

    assert_bindings(
        schema="wgData/sg/snneg.xsd",
        instance="wgData/sg/snn1.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_sg_and_defined_sibling_1_sns1(save_xml):

    assert_bindings(
        schema="wgData/sg/snneg.xsd",
        instance="wgData/sg/sns1.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


def test_iri_001_uri_3986_valid_001(save_xml):

    assert_bindings(
        schema="wgData/iri/ElementDeclarations.xsd",
        instance="wgData/iri/URI-3986-valid-001.xml",
        class_name="Uri3986",
        version="1.1",
        save_xml=save_xml,
    )


def test_iri_001_uri_3986_valid_002(save_xml):

    assert_bindings(
        schema="wgData/iri/ElementDeclarations.xsd",
        instance="wgData/iri/URI-3986-valid-002.xml",
        class_name="Uri3986",
        version="1.1",
        save_xml=save_xml,
    )


def test_iri_001_uri_3986_valid_003(save_xml):

    assert_bindings(
        schema="wgData/iri/ElementDeclarations.xsd",
        instance="wgData/iri/URI-3986-valid-003.xml",
        class_name="Uri3986",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_iri_001_uri_3986_invalid_001(save_xml):

    assert_bindings(
        schema="wgData/iri/ElementDeclarations.xsd",
        instance="wgData/iri/URI-3986-invalid-001.xml",
        class_name="Uri3986",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_iri_001_uri_3986_invalid_002(save_xml):

    assert_bindings(
        schema="wgData/iri/ElementDeclarations.xsd",
        instance="wgData/iri/URI-3986-invalid-002.xml",
        class_name="Uri3986",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_iri_001_uri_3986_invalid_003(save_xml):

    assert_bindings(
        schema="wgData/iri/ElementDeclarations.xsd",
        instance="wgData/iri/URI-3986-invalid-003.xml",
        class_name="Uri3986",
        version="1.1",
        save_xml=save_xml,
    )


def test_iri_001_absolute_uri_3986_valid_001(save_xml):

    assert_bindings(
        schema="wgData/iri/ElementDeclarations.xsd",
        instance="wgData/iri/absolute-URI-3986-valid-001.xml",
        class_name="AbsoluteUri3986",
        version="1.1",
        save_xml=save_xml,
    )


def test_iri_001_absolute_uri_3986_valid_002(save_xml):

    assert_bindings(
        schema="wgData/iri/ElementDeclarations.xsd",
        instance="wgData/iri/absolute-URI-3986-valid-002.xml",
        class_name="AbsoluteUri3986",
        version="1.1",
        save_xml=save_xml,
    )


def test_iri_001_absolute_uri_3986_valid_003(save_xml):

    assert_bindings(
        schema="wgData/iri/ElementDeclarations.xsd",
        instance="wgData/iri/absolute-URI-3986-valid-003.xml",
        class_name="AbsoluteUri3986",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_iri_001_absolute_uri_3986_invalid_001(save_xml):

    assert_bindings(
        schema="wgData/iri/ElementDeclarations.xsd",
        instance="wgData/iri/absolute-URI-3986-invalid-001.xml",
        class_name="AbsoluteUri3986",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_iri_001_absolute_uri_3986_invalid_002(save_xml):

    assert_bindings(
        schema="wgData/iri/ElementDeclarations.xsd",
        instance="wgData/iri/absolute-URI-3986-invalid-002.xml",
        class_name="AbsoluteUri3986",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_iri_001_absolute_uri_3986_invalid_003(save_xml):

    assert_bindings(
        schema="wgData/iri/ElementDeclarations.xsd",
        instance="wgData/iri/absolute-URI-3986-invalid-003.xml",
        class_name="AbsoluteUri3986",
        version="1.1",
        save_xml=save_xml,
    )
