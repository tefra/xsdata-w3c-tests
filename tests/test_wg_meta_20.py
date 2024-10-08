from tests.utils import assert_bindings


def test_sg_abstract_edc_ee1i_xml(mode, save_output, output_format):

    assert_bindings(
        schema="wgData/sg/edc.xsd",
        instance="wgData/sg/ee1i.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sg_abstract_upa2_e1bis_xml(mode, save_output, output_format):

    assert_bindings(
        schema="wgData/sg/upa2.xsd",
        instance="wgData/sg/e1.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sg_abstract_upa2_e1short_xml(mode, save_output, output_format):

    assert_bindings(
        schema="wgData/sg/upa2.xsd",
        instance="wgData/sg/e1short.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sg_abstract_upa_e1_xml(mode, save_output, output_format):

    assert_bindings(
        schema="wgData/sg/upa.xsd",
        instance="wgData/sg/e1.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sg_abstract_upa_e1token_xml(mode, save_output, output_format):

    assert_bindings(
        schema="wgData/sg/upa.xsd",
        instance="wgData/sg/e1token.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sg_and_defined_sibling_3_sns1b(mode, save_output, output_format):

    assert_bindings(
        schema="wgData/sg/snbranch.xsd",
        instance="wgData/sg/sns1b.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sg_and_defined_sibling_3_snn1c(mode, save_output, output_format):

    assert_bindings(
        schema="wgData/sg/snbranch.xsd",
        instance="wgData/sg/snn1c.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sg_and_defined_sibling_3_snea(mode, save_output, output_format):

    assert_bindings(
        schema="wgData/sg/snbranch.xsd",
        instance="wgData/sg/snea.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sg_and_defined_sibling_2_esn(mode, save_output, output_format):

    assert_bindings(
        schema="wgData/sg/negsn.xsd",
        instance="wgData/sg/esn.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sg_and_defined_sibling_2_n1sn(mode, save_output, output_format):

    assert_bindings(
        schema="wgData/sg/negsn.xsd",
        instance="wgData/sg/n1sn.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sg_and_defined_sibling_1_sn(mode, save_output, output_format):

    assert_bindings(
        schema="wgData/sg/snneg.xsd",
        instance="wgData/sg/sn.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sg_and_defined_sibling_1_s1n(mode, save_output, output_format):

    assert_bindings(
        schema="wgData/sg/snneg.xsd",
        instance="wgData/sg/s1n.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sg_and_defined_sibling_1_sne(mode, save_output, output_format):

    assert_bindings(
        schema="wgData/sg/snneg.xsd",
        instance="wgData/sg/sne.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_sg_and_defined_sibling_1_snn1(mode, save_output, output_format):

    assert_bindings(
        schema="wgData/sg/snneg.xsd",
        instance="wgData/sg/snn1.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_iri_001_uri_3986_valid_001(mode, save_output, output_format):

    assert_bindings(
        schema="wgData/iri/ElementDeclarations.xsd",
        instance="wgData/iri/URI-3986-valid-001.xml",
        class_name="Uri3986",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_iri_001_uri_3986_valid_002(mode, save_output, output_format):

    assert_bindings(
        schema="wgData/iri/ElementDeclarations.xsd",
        instance="wgData/iri/URI-3986-valid-002.xml",
        class_name="Uri3986",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_iri_001_uri_3986_valid_003(mode, save_output, output_format):

    assert_bindings(
        schema="wgData/iri/ElementDeclarations.xsd",
        instance="wgData/iri/URI-3986-valid-003.xml",
        class_name="Uri3986",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_iri_001_absolute_uri_3986_valid_001(mode, save_output, output_format):

    assert_bindings(
        schema="wgData/iri/ElementDeclarations.xsd",
        instance="wgData/iri/absolute-URI-3986-valid-001.xml",
        class_name="AbsoluteUri3986",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_iri_001_absolute_uri_3986_valid_002(mode, save_output, output_format):

    assert_bindings(
        schema="wgData/iri/ElementDeclarations.xsd",
        instance="wgData/iri/absolute-URI-3986-valid-002.xml",
        class_name="AbsoluteUri3986",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_iri_001_absolute_uri_3986_valid_003(mode, save_output, output_format):

    assert_bindings(
        schema="wgData/iri/ElementDeclarations.xsd",
        instance="wgData/iri/absolute-URI-3986-valid-003.xml",
        class_name="AbsoluteUri3986",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )
