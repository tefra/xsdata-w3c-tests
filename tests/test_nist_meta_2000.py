from tests.utils import assert_bindings


def test_list_id_pattern_1_nistxml_sv_iv_list_id_pattern_2_1(mode, save_output, output_format):
    r"""
    Type list/ID is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{5} [\i-[:]][\c-[:]]{36} [\i-[:]][\c-[:]]{42}
    [\i-[:]][\c-[:]]{37} [\i-[:]][\c-[:]]{23} [\i-[:]][\c-[:]]{20}
    [\i-[:]][\c-[:]]{4} [\i-[:]][\c-[:]]{36}.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-pattern-2.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-pattern-2-1.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_pattern_1_nistxml_sv_iv_list_id_pattern_2_2(mode, save_output, output_format):
    r"""
    Type list/ID is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{5} [\i-[:]][\c-[:]]{36} [\i-[:]][\c-[:]]{42}
    [\i-[:]][\c-[:]]{37} [\i-[:]][\c-[:]]{23} [\i-[:]][\c-[:]]{20}
    [\i-[:]][\c-[:]]{4} [\i-[:]][\c-[:]]{36}.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-pattern-2.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-pattern-2-2.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_pattern_1_nistxml_sv_iv_list_id_pattern_2_3(mode, save_output, output_format):
    r"""
    Type list/ID is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{5} [\i-[:]][\c-[:]]{36} [\i-[:]][\c-[:]]{42}
    [\i-[:]][\c-[:]]{37} [\i-[:]][\c-[:]]{23} [\i-[:]][\c-[:]]{20}
    [\i-[:]][\c-[:]]{4} [\i-[:]][\c-[:]]{36}.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-pattern-2.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-pattern-2-3.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_pattern_1_nistxml_sv_iv_list_id_pattern_2_4(mode, save_output, output_format):
    r"""
    Type list/ID is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{5} [\i-[:]][\c-[:]]{36} [\i-[:]][\c-[:]]{42}
    [\i-[:]][\c-[:]]{37} [\i-[:]][\c-[:]]{23} [\i-[:]][\c-[:]]{20}
    [\i-[:]][\c-[:]]{4} [\i-[:]][\c-[:]]{36}.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-pattern-2.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-pattern-2-4.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_pattern_1_nistxml_sv_iv_list_id_pattern_2_5(mode, save_output, output_format):
    r"""
    Type list/ID is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{5} [\i-[:]][\c-[:]]{36} [\i-[:]][\c-[:]]{42}
    [\i-[:]][\c-[:]]{37} [\i-[:]][\c-[:]]{23} [\i-[:]][\c-[:]]{20}
    [\i-[:]][\c-[:]]{4} [\i-[:]][\c-[:]]{36}.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-pattern-2.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-pattern-2-5.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_pattern_nistxml_sv_iv_list_id_pattern_1_1(mode, save_output, output_format):
    r"""
    Type list/ID is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{2} [\i-[:]][\c-[:]]{57} [\i-[:]][\c-[:]]{31}
    [\i-[:]][\c-[:]]{5} [\i-[:]][\c-[:]]{10} [\i-[:]][\c-[:]]{47}
    [\i-[:]][\c-[:]]{21}.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-pattern-1.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-pattern-1-1.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_pattern_nistxml_sv_iv_list_id_pattern_1_2(mode, save_output, output_format):
    r"""
    Type list/ID is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{2} [\i-[:]][\c-[:]]{57} [\i-[:]][\c-[:]]{31}
    [\i-[:]][\c-[:]]{5} [\i-[:]][\c-[:]]{10} [\i-[:]][\c-[:]]{47}
    [\i-[:]][\c-[:]]{21}.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-pattern-1.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-pattern-1-2.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_pattern_nistxml_sv_iv_list_id_pattern_1_3(mode, save_output, output_format):
    r"""
    Type list/ID is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{2} [\i-[:]][\c-[:]]{57} [\i-[:]][\c-[:]]{31}
    [\i-[:]][\c-[:]]{5} [\i-[:]][\c-[:]]{10} [\i-[:]][\c-[:]]{47}
    [\i-[:]][\c-[:]]{21}.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-pattern-1.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-pattern-1-3.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_pattern_nistxml_sv_iv_list_id_pattern_1_4(mode, save_output, output_format):
    r"""
    Type list/ID is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{2} [\i-[:]][\c-[:]]{57} [\i-[:]][\c-[:]]{31}
    [\i-[:]][\c-[:]]{5} [\i-[:]][\c-[:]]{10} [\i-[:]][\c-[:]]{47}
    [\i-[:]][\c-[:]]{21}.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-pattern-1.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-pattern-1-4.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_pattern_nistxml_sv_iv_list_id_pattern_1_5(mode, save_output, output_format):
    r"""
    Type list/ID is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{2} [\i-[:]][\c-[:]]{57} [\i-[:]][\c-[:]]{31}
    [\i-[:]][\c-[:]]{5} [\i-[:]][\c-[:]]{10} [\i-[:]][\c-[:]]{47}
    [\i-[:]][\c-[:]]{21}.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-pattern-1.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-pattern-1-5.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_length_4_nistxml_sv_iv_list_id_length_5_1(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-length-5.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-length-5-1.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_length_4_nistxml_sv_iv_list_id_length_5_2(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-length-5.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-length-5-2.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_length_4_nistxml_sv_iv_list_id_length_5_3(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-length-5.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-length-5-3.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_length_4_nistxml_sv_iv_list_id_length_5_4(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-length-5.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-length-5-4.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_length_4_nistxml_sv_iv_list_id_length_5_5(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-length-5.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-length-5-5.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_length_3_nistxml_sv_iv_list_id_length_4_1(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-length-4.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-length-4-1.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_length_3_nistxml_sv_iv_list_id_length_4_2(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-length-4.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-length-4-2.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_length_3_nistxml_sv_iv_list_id_length_4_3(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-length-4.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-length-4-3.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_length_3_nistxml_sv_iv_list_id_length_4_4(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-length-4.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-length-4-4.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_length_3_nistxml_sv_iv_list_id_length_4_5(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-length-4.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-length-4-5.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_length_2_nistxml_sv_iv_list_id_length_3_1(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-length-3.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-length-3-1.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_length_2_nistxml_sv_iv_list_id_length_3_2(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-length-3.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-length-3-2.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_length_2_nistxml_sv_iv_list_id_length_3_3(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-length-3.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-length-3-3.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_length_2_nistxml_sv_iv_list_id_length_3_4(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-length-3.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-length-3-4.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_length_2_nistxml_sv_iv_list_id_length_3_5(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-length-3.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-length-3-5.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_length_1_nistxml_sv_iv_list_id_length_2_1(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-length-2.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-length-2-1.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_length_1_nistxml_sv_iv_list_id_length_2_2(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-length-2.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-length-2-2.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_length_1_nistxml_sv_iv_list_id_length_2_3(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-length-2.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-length-2-3.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_length_1_nistxml_sv_iv_list_id_length_2_4(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-length-2.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-length-2-4.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_length_1_nistxml_sv_iv_list_id_length_2_5(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-length-2.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-length-2-5.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_length_nistxml_sv_iv_list_id_length_1_1(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-length-1.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-length-1-1.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_length_nistxml_sv_iv_list_id_length_1_2(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-length-1.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-length-1-2.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_length_nistxml_sv_iv_list_id_length_1_3(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-length-1.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-length-1-3.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_length_nistxml_sv_iv_list_id_length_1_4(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-length-1.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-length-1-4.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_length_nistxml_sv_iv_list_id_length_1_5(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-length-1.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-length-1-5.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_min_length_4_nistxml_sv_iv_list_id_min_length_5_1(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-minLength-5.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-minLength-5-1.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_min_length_4_nistxml_sv_iv_list_id_min_length_5_2(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-minLength-5.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-minLength-5-2.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_min_length_4_nistxml_sv_iv_list_id_min_length_5_3(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-minLength-5.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-minLength-5-3.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_min_length_4_nistxml_sv_iv_list_id_min_length_5_4(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-minLength-5.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-minLength-5-4.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_min_length_4_nistxml_sv_iv_list_id_min_length_5_5(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-minLength-5.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-minLength-5-5.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_min_length_3_nistxml_sv_iv_list_id_min_length_4_1(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-minLength-4.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-minLength-4-1.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_min_length_3_nistxml_sv_iv_list_id_min_length_4_2(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-minLength-4.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-minLength-4-2.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_min_length_3_nistxml_sv_iv_list_id_min_length_4_3(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-minLength-4.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-minLength-4-3.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_min_length_3_nistxml_sv_iv_list_id_min_length_4_4(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-minLength-4.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-minLength-4-4.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_min_length_3_nistxml_sv_iv_list_id_min_length_4_5(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-minLength-4.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-minLength-4-5.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_min_length_2_nistxml_sv_iv_list_id_min_length_3_1(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-minLength-3.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-minLength-3-1.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_min_length_2_nistxml_sv_iv_list_id_min_length_3_2(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-minLength-3.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-minLength-3-2.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_min_length_2_nistxml_sv_iv_list_id_min_length_3_3(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-minLength-3.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-minLength-3-3.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_min_length_2_nistxml_sv_iv_list_id_min_length_3_4(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-minLength-3.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-minLength-3-4.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_min_length_2_nistxml_sv_iv_list_id_min_length_3_5(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-minLength-3.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-minLength-3-5.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_min_length_1_nistxml_sv_iv_list_id_min_length_2_1(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-minLength-2.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-minLength-2-1.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_min_length_1_nistxml_sv_iv_list_id_min_length_2_2(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-minLength-2.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-minLength-2-2.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_min_length_1_nistxml_sv_iv_list_id_min_length_2_3(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-minLength-2.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-minLength-2-3.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_min_length_1_nistxml_sv_iv_list_id_min_length_2_4(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-minLength-2.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-minLength-2-4.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_min_length_1_nistxml_sv_iv_list_id_min_length_2_5(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-minLength-2.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-minLength-2-5.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_min_length_nistxml_sv_iv_list_id_min_length_1_1(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-minLength-1.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-minLength-1-1.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_min_length_nistxml_sv_iv_list_id_min_length_1_2(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-minLength-1.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-minLength-1-2.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_min_length_nistxml_sv_iv_list_id_min_length_1_3(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-minLength-1.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-minLength-1-3.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_min_length_nistxml_sv_iv_list_id_min_length_1_4(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-minLength-1.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-minLength-1-4.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_min_length_nistxml_sv_iv_list_id_min_length_1_5(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-minLength-1.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-minLength-1-5.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_max_length_4_nistxml_sv_iv_list_id_max_length_5_1(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-maxLength-5.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-maxLength-5-1.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_max_length_4_nistxml_sv_iv_list_id_max_length_5_2(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-maxLength-5.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-maxLength-5-2.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_max_length_4_nistxml_sv_iv_list_id_max_length_5_3(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-maxLength-5.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-maxLength-5-3.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_max_length_4_nistxml_sv_iv_list_id_max_length_5_4(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-maxLength-5.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-maxLength-5-4.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_max_length_4_nistxml_sv_iv_list_id_max_length_5_5(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-maxLength-5.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-maxLength-5-5.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_max_length_3_nistxml_sv_iv_list_id_max_length_4_1(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-maxLength-4.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-maxLength-4-1.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_max_length_3_nistxml_sv_iv_list_id_max_length_4_2(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-maxLength-4.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-maxLength-4-2.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_max_length_3_nistxml_sv_iv_list_id_max_length_4_3(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-maxLength-4.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-maxLength-4-3.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_max_length_3_nistxml_sv_iv_list_id_max_length_4_4(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-maxLength-4.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-maxLength-4-4.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_max_length_3_nistxml_sv_iv_list_id_max_length_4_5(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-maxLength-4.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-maxLength-4-5.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_max_length_2_nistxml_sv_iv_list_id_max_length_3_1(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-maxLength-3.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-maxLength-3-1.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_max_length_2_nistxml_sv_iv_list_id_max_length_3_2(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-maxLength-3.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-maxLength-3-2.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_max_length_2_nistxml_sv_iv_list_id_max_length_3_3(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-maxLength-3.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-maxLength-3-3.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_max_length_2_nistxml_sv_iv_list_id_max_length_3_4(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-maxLength-3.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-maxLength-3-4.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_max_length_2_nistxml_sv_iv_list_id_max_length_3_5(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-maxLength-3.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-maxLength-3-5.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_max_length_1_nistxml_sv_iv_list_id_max_length_2_1(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-maxLength-2.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-maxLength-2-1.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_max_length_1_nistxml_sv_iv_list_id_max_length_2_2(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-maxLength-2.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-maxLength-2-2.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_max_length_1_nistxml_sv_iv_list_id_max_length_2_3(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-maxLength-2.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-maxLength-2-3.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_max_length_1_nistxml_sv_iv_list_id_max_length_2_4(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-maxLength-2.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-maxLength-2-4.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_max_length_1_nistxml_sv_iv_list_id_max_length_2_5(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-maxLength-2.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-maxLength-2-5.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_max_length_nistxml_sv_iv_list_id_max_length_1_1(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-maxLength-1.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-maxLength-1-1.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_max_length_nistxml_sv_iv_list_id_max_length_1_2(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-maxLength-1.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-maxLength-1-2.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_max_length_nistxml_sv_iv_list_id_max_length_1_3(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-maxLength-1.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-maxLength-1-3.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_max_length_nistxml_sv_iv_list_id_max_length_1_4(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-maxLength-1.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-maxLength-1-4.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_id_max_length_nistxml_sv_iv_list_id_max_length_1_5(mode, save_output, output_format):
    """
    Type list/ID is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/ID/Schema+Instance/NISTSchema-SV-IV-list-ID-maxLength-1.xsd",
        instance="nistData/list/ID/Schema+Instance/NISTXML-SV-IV-list-ID-maxLength-1-5.xml",
        class_name="Out",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_white_space_nistxml_sv_iv_list_ncname_white_space_1_1(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet whiteSpace with value
    collapse.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-whiteSpace-1.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-whiteSpace-1-1.xml",
        class_name="NistschemaSvIvListNcnameWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_white_space_nistxml_sv_iv_list_ncname_white_space_1_2(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet whiteSpace with value
    collapse.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-whiteSpace-1.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-whiteSpace-1-2.xml",
        class_name="NistschemaSvIvListNcnameWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_white_space_nistxml_sv_iv_list_ncname_white_space_1_3(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet whiteSpace with value
    collapse.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-whiteSpace-1.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-whiteSpace-1-3.xml",
        class_name="NistschemaSvIvListNcnameWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_white_space_nistxml_sv_iv_list_ncname_white_space_1_4(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet whiteSpace with value
    collapse.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-whiteSpace-1.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-whiteSpace-1-4.xml",
        class_name="NistschemaSvIvListNcnameWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_white_space_nistxml_sv_iv_list_ncname_white_space_1_5(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet whiteSpace with value
    collapse.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-whiteSpace-1.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-whiteSpace-1-5.xml",
        class_name="NistschemaSvIvListNcnameWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_enumeration_4_nistxml_sv_iv_list_ncname_enumeration_5_1(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-enumeration-5.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-enumeration-5-1.xml",
        class_name="NistschemaSvIvListNcnameEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_enumeration_4_nistxml_sv_iv_list_ncname_enumeration_5_2(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-enumeration-5.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-enumeration-5-2.xml",
        class_name="NistschemaSvIvListNcnameEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_enumeration_4_nistxml_sv_iv_list_ncname_enumeration_5_3(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-enumeration-5.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-enumeration-5-3.xml",
        class_name="NistschemaSvIvListNcnameEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_enumeration_4_nistxml_sv_iv_list_ncname_enumeration_5_4(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-enumeration-5.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-enumeration-5-4.xml",
        class_name="NistschemaSvIvListNcnameEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_enumeration_4_nistxml_sv_iv_list_ncname_enumeration_5_5(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-enumeration-5.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-enumeration-5-5.xml",
        class_name="NistschemaSvIvListNcnameEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_enumeration_3_nistxml_sv_iv_list_ncname_enumeration_4_1(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-enumeration-4.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-enumeration-4-1.xml",
        class_name="NistschemaSvIvListNcnameEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_enumeration_3_nistxml_sv_iv_list_ncname_enumeration_4_2(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-enumeration-4.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-enumeration-4-2.xml",
        class_name="NistschemaSvIvListNcnameEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_enumeration_3_nistxml_sv_iv_list_ncname_enumeration_4_3(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-enumeration-4.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-enumeration-4-3.xml",
        class_name="NistschemaSvIvListNcnameEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_enumeration_3_nistxml_sv_iv_list_ncname_enumeration_4_4(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-enumeration-4.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-enumeration-4-4.xml",
        class_name="NistschemaSvIvListNcnameEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_enumeration_3_nistxml_sv_iv_list_ncname_enumeration_4_5(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-enumeration-4.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-enumeration-4-5.xml",
        class_name="NistschemaSvIvListNcnameEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_enumeration_2_nistxml_sv_iv_list_ncname_enumeration_3_1(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-enumeration-3.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-enumeration-3-1.xml",
        class_name="NistschemaSvIvListNcnameEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_enumeration_2_nistxml_sv_iv_list_ncname_enumeration_3_2(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-enumeration-3.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-enumeration-3-2.xml",
        class_name="NistschemaSvIvListNcnameEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_enumeration_2_nistxml_sv_iv_list_ncname_enumeration_3_3(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-enumeration-3.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-enumeration-3-3.xml",
        class_name="NistschemaSvIvListNcnameEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_enumeration_2_nistxml_sv_iv_list_ncname_enumeration_3_4(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-enumeration-3.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-enumeration-3-4.xml",
        class_name="NistschemaSvIvListNcnameEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_enumeration_2_nistxml_sv_iv_list_ncname_enumeration_3_5(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-enumeration-3.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-enumeration-3-5.xml",
        class_name="NistschemaSvIvListNcnameEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_enumeration_1_nistxml_sv_iv_list_ncname_enumeration_2_1(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-enumeration-2.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-enumeration-2-1.xml",
        class_name="NistschemaSvIvListNcnameEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_enumeration_1_nistxml_sv_iv_list_ncname_enumeration_2_2(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-enumeration-2.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-enumeration-2-2.xml",
        class_name="NistschemaSvIvListNcnameEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_enumeration_1_nistxml_sv_iv_list_ncname_enumeration_2_3(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-enumeration-2.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-enumeration-2-3.xml",
        class_name="NistschemaSvIvListNcnameEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_enumeration_1_nistxml_sv_iv_list_ncname_enumeration_2_4(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-enumeration-2.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-enumeration-2-4.xml",
        class_name="NistschemaSvIvListNcnameEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_enumeration_1_nistxml_sv_iv_list_ncname_enumeration_2_5(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-enumeration-2.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-enumeration-2-5.xml",
        class_name="NistschemaSvIvListNcnameEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_enumeration_nistxml_sv_iv_list_ncname_enumeration_1_1(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-enumeration-1.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-enumeration-1-1.xml",
        class_name="NistschemaSvIvListNcnameEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_enumeration_nistxml_sv_iv_list_ncname_enumeration_1_2(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-enumeration-1.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-enumeration-1-2.xml",
        class_name="NistschemaSvIvListNcnameEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_enumeration_nistxml_sv_iv_list_ncname_enumeration_1_3(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-enumeration-1.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-enumeration-1-3.xml",
        class_name="NistschemaSvIvListNcnameEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_enumeration_nistxml_sv_iv_list_ncname_enumeration_1_4(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-enumeration-1.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-enumeration-1-4.xml",
        class_name="NistschemaSvIvListNcnameEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_enumeration_nistxml_sv_iv_list_ncname_enumeration_1_5(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-enumeration-1.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-enumeration-1-5.xml",
        class_name="NistschemaSvIvListNcnameEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_pattern_4_nistxml_sv_iv_list_ncname_pattern_5_1(mode, save_output, output_format):
    r"""
    Type list/NCName is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{40} [\i-[:]][\c-[:]]{59} [\i-[:]][\c-[:]]{55}
    [\i-[:]][\c-[:]]{41} [\i-[:]][\c-[:]]{12} [\i-[:]][\c-[:]]{25}.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-pattern-5.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-pattern-5-1.xml",
        class_name="NistschemaSvIvListNcnamePattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_pattern_4_nistxml_sv_iv_list_ncname_pattern_5_2(mode, save_output, output_format):
    r"""
    Type list/NCName is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{40} [\i-[:]][\c-[:]]{59} [\i-[:]][\c-[:]]{55}
    [\i-[:]][\c-[:]]{41} [\i-[:]][\c-[:]]{12} [\i-[:]][\c-[:]]{25}.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-pattern-5.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-pattern-5-2.xml",
        class_name="NistschemaSvIvListNcnamePattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_pattern_4_nistxml_sv_iv_list_ncname_pattern_5_3(mode, save_output, output_format):
    r"""
    Type list/NCName is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{40} [\i-[:]][\c-[:]]{59} [\i-[:]][\c-[:]]{55}
    [\i-[:]][\c-[:]]{41} [\i-[:]][\c-[:]]{12} [\i-[:]][\c-[:]]{25}.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-pattern-5.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-pattern-5-3.xml",
        class_name="NistschemaSvIvListNcnamePattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_pattern_4_nistxml_sv_iv_list_ncname_pattern_5_4(mode, save_output, output_format):
    r"""
    Type list/NCName is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{40} [\i-[:]][\c-[:]]{59} [\i-[:]][\c-[:]]{55}
    [\i-[:]][\c-[:]]{41} [\i-[:]][\c-[:]]{12} [\i-[:]][\c-[:]]{25}.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-pattern-5.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-pattern-5-4.xml",
        class_name="NistschemaSvIvListNcnamePattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_pattern_4_nistxml_sv_iv_list_ncname_pattern_5_5(mode, save_output, output_format):
    r"""
    Type list/NCName is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{40} [\i-[:]][\c-[:]]{59} [\i-[:]][\c-[:]]{55}
    [\i-[:]][\c-[:]]{41} [\i-[:]][\c-[:]]{12} [\i-[:]][\c-[:]]{25}.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-pattern-5.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-pattern-5-5.xml",
        class_name="NistschemaSvIvListNcnamePattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_pattern_3_nistxml_sv_iv_list_ncname_pattern_4_1(mode, save_output, output_format):
    r"""
    Type list/NCName is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{44} [\i-[:]][\c-[:]]{50} [\i-[:]][\c-[:]]{47}
    [\i-[:]][\c-[:]]{60} [\i-[:]][\c-[:]]{10} [\i-[:]][\c-[:]]{0}
    [\i-[:]][\c-[:]]{17} [\i-[:]][\c-[:]]{45} [\i-[:]][\c-[:]]{50}
    [\i-[:]][\c-[:]]{36}.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-pattern-4.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-pattern-4-1.xml",
        class_name="NistschemaSvIvListNcnamePattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_pattern_3_nistxml_sv_iv_list_ncname_pattern_4_2(mode, save_output, output_format):
    r"""
    Type list/NCName is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{44} [\i-[:]][\c-[:]]{50} [\i-[:]][\c-[:]]{47}
    [\i-[:]][\c-[:]]{60} [\i-[:]][\c-[:]]{10} [\i-[:]][\c-[:]]{0}
    [\i-[:]][\c-[:]]{17} [\i-[:]][\c-[:]]{45} [\i-[:]][\c-[:]]{50}
    [\i-[:]][\c-[:]]{36}.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-pattern-4.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-pattern-4-2.xml",
        class_name="NistschemaSvIvListNcnamePattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_pattern_3_nistxml_sv_iv_list_ncname_pattern_4_3(mode, save_output, output_format):
    r"""
    Type list/NCName is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{44} [\i-[:]][\c-[:]]{50} [\i-[:]][\c-[:]]{47}
    [\i-[:]][\c-[:]]{60} [\i-[:]][\c-[:]]{10} [\i-[:]][\c-[:]]{0}
    [\i-[:]][\c-[:]]{17} [\i-[:]][\c-[:]]{45} [\i-[:]][\c-[:]]{50}
    [\i-[:]][\c-[:]]{36}.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-pattern-4.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-pattern-4-3.xml",
        class_name="NistschemaSvIvListNcnamePattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_pattern_3_nistxml_sv_iv_list_ncname_pattern_4_4(mode, save_output, output_format):
    r"""
    Type list/NCName is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{44} [\i-[:]][\c-[:]]{50} [\i-[:]][\c-[:]]{47}
    [\i-[:]][\c-[:]]{60} [\i-[:]][\c-[:]]{10} [\i-[:]][\c-[:]]{0}
    [\i-[:]][\c-[:]]{17} [\i-[:]][\c-[:]]{45} [\i-[:]][\c-[:]]{50}
    [\i-[:]][\c-[:]]{36}.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-pattern-4.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-pattern-4-4.xml",
        class_name="NistschemaSvIvListNcnamePattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_pattern_3_nistxml_sv_iv_list_ncname_pattern_4_5(mode, save_output, output_format):
    r"""
    Type list/NCName is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{44} [\i-[:]][\c-[:]]{50} [\i-[:]][\c-[:]]{47}
    [\i-[:]][\c-[:]]{60} [\i-[:]][\c-[:]]{10} [\i-[:]][\c-[:]]{0}
    [\i-[:]][\c-[:]]{17} [\i-[:]][\c-[:]]{45} [\i-[:]][\c-[:]]{50}
    [\i-[:]][\c-[:]]{36}.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-pattern-4.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-pattern-4-5.xml",
        class_name="NistschemaSvIvListNcnamePattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_pattern_2_nistxml_sv_iv_list_ncname_pattern_3_1(mode, save_output, output_format):
    r"""
    Type list/NCName is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{33} [\i-[:]][\c-[:]]{63} [\i-[:]][\c-[:]]{13}
    [\i-[:]][\c-[:]]{35} [\i-[:]][\c-[:]]{29}.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-pattern-3.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-pattern-3-1.xml",
        class_name="NistschemaSvIvListNcnamePattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_pattern_2_nistxml_sv_iv_list_ncname_pattern_3_2(mode, save_output, output_format):
    r"""
    Type list/NCName is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{33} [\i-[:]][\c-[:]]{63} [\i-[:]][\c-[:]]{13}
    [\i-[:]][\c-[:]]{35} [\i-[:]][\c-[:]]{29}.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-pattern-3.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-pattern-3-2.xml",
        class_name="NistschemaSvIvListNcnamePattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_pattern_2_nistxml_sv_iv_list_ncname_pattern_3_3(mode, save_output, output_format):
    r"""
    Type list/NCName is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{33} [\i-[:]][\c-[:]]{63} [\i-[:]][\c-[:]]{13}
    [\i-[:]][\c-[:]]{35} [\i-[:]][\c-[:]]{29}.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-pattern-3.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-pattern-3-3.xml",
        class_name="NistschemaSvIvListNcnamePattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_pattern_2_nistxml_sv_iv_list_ncname_pattern_3_4(mode, save_output, output_format):
    r"""
    Type list/NCName is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{33} [\i-[:]][\c-[:]]{63} [\i-[:]][\c-[:]]{13}
    [\i-[:]][\c-[:]]{35} [\i-[:]][\c-[:]]{29}.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-pattern-3.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-pattern-3-4.xml",
        class_name="NistschemaSvIvListNcnamePattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_pattern_2_nistxml_sv_iv_list_ncname_pattern_3_5(mode, save_output, output_format):
    r"""
    Type list/NCName is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{33} [\i-[:]][\c-[:]]{63} [\i-[:]][\c-[:]]{13}
    [\i-[:]][\c-[:]]{35} [\i-[:]][\c-[:]]{29}.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-pattern-3.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-pattern-3-5.xml",
        class_name="NistschemaSvIvListNcnamePattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_pattern_1_nistxml_sv_iv_list_ncname_pattern_2_1(mode, save_output, output_format):
    r"""
    Type list/NCName is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{7} [\i-[:]][\c-[:]]{35} [\i-[:]][\c-[:]]{46}
    [\i-[:]][\c-[:]]{25} [\i-[:]][\c-[:]]{53} [\i-[:]][\c-[:]]{58}
    [\i-[:]][\c-[:]]{11}.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-pattern-2.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-pattern-2-1.xml",
        class_name="NistschemaSvIvListNcnamePattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_pattern_1_nistxml_sv_iv_list_ncname_pattern_2_2(mode, save_output, output_format):
    r"""
    Type list/NCName is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{7} [\i-[:]][\c-[:]]{35} [\i-[:]][\c-[:]]{46}
    [\i-[:]][\c-[:]]{25} [\i-[:]][\c-[:]]{53} [\i-[:]][\c-[:]]{58}
    [\i-[:]][\c-[:]]{11}.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-pattern-2.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-pattern-2-2.xml",
        class_name="NistschemaSvIvListNcnamePattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_pattern_1_nistxml_sv_iv_list_ncname_pattern_2_3(mode, save_output, output_format):
    r"""
    Type list/NCName is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{7} [\i-[:]][\c-[:]]{35} [\i-[:]][\c-[:]]{46}
    [\i-[:]][\c-[:]]{25} [\i-[:]][\c-[:]]{53} [\i-[:]][\c-[:]]{58}
    [\i-[:]][\c-[:]]{11}.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-pattern-2.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-pattern-2-3.xml",
        class_name="NistschemaSvIvListNcnamePattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_pattern_1_nistxml_sv_iv_list_ncname_pattern_2_4(mode, save_output, output_format):
    r"""
    Type list/NCName is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{7} [\i-[:]][\c-[:]]{35} [\i-[:]][\c-[:]]{46}
    [\i-[:]][\c-[:]]{25} [\i-[:]][\c-[:]]{53} [\i-[:]][\c-[:]]{58}
    [\i-[:]][\c-[:]]{11}.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-pattern-2.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-pattern-2-4.xml",
        class_name="NistschemaSvIvListNcnamePattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_pattern_1_nistxml_sv_iv_list_ncname_pattern_2_5(mode, save_output, output_format):
    r"""
    Type list/NCName is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{7} [\i-[:]][\c-[:]]{35} [\i-[:]][\c-[:]]{46}
    [\i-[:]][\c-[:]]{25} [\i-[:]][\c-[:]]{53} [\i-[:]][\c-[:]]{58}
    [\i-[:]][\c-[:]]{11}.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-pattern-2.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-pattern-2-5.xml",
        class_name="NistschemaSvIvListNcnamePattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_pattern_nistxml_sv_iv_list_ncname_pattern_1_1(mode, save_output, output_format):
    r"""
    Type list/NCName is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{39} [\i-[:]][\c-[:]]{15} [\i-[:]][\c-[:]]{23}
    [\i-[:]][\c-[:]]{44} [\i-[:]][\c-[:]]{55} [\i-[:]][\c-[:]]{18}
    [\i-[:]][\c-[:]]{44} [\i-[:]][\c-[:]]{1}.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-pattern-1.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-pattern-1-1.xml",
        class_name="NistschemaSvIvListNcnamePattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_pattern_nistxml_sv_iv_list_ncname_pattern_1_2(mode, save_output, output_format):
    r"""
    Type list/NCName is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{39} [\i-[:]][\c-[:]]{15} [\i-[:]][\c-[:]]{23}
    [\i-[:]][\c-[:]]{44} [\i-[:]][\c-[:]]{55} [\i-[:]][\c-[:]]{18}
    [\i-[:]][\c-[:]]{44} [\i-[:]][\c-[:]]{1}.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-pattern-1.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-pattern-1-2.xml",
        class_name="NistschemaSvIvListNcnamePattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_pattern_nistxml_sv_iv_list_ncname_pattern_1_3(mode, save_output, output_format):
    r"""
    Type list/NCName is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{39} [\i-[:]][\c-[:]]{15} [\i-[:]][\c-[:]]{23}
    [\i-[:]][\c-[:]]{44} [\i-[:]][\c-[:]]{55} [\i-[:]][\c-[:]]{18}
    [\i-[:]][\c-[:]]{44} [\i-[:]][\c-[:]]{1}.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-pattern-1.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-pattern-1-3.xml",
        class_name="NistschemaSvIvListNcnamePattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_pattern_nistxml_sv_iv_list_ncname_pattern_1_4(mode, save_output, output_format):
    r"""
    Type list/NCName is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{39} [\i-[:]][\c-[:]]{15} [\i-[:]][\c-[:]]{23}
    [\i-[:]][\c-[:]]{44} [\i-[:]][\c-[:]]{55} [\i-[:]][\c-[:]]{18}
    [\i-[:]][\c-[:]]{44} [\i-[:]][\c-[:]]{1}.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-pattern-1.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-pattern-1-4.xml",
        class_name="NistschemaSvIvListNcnamePattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_pattern_nistxml_sv_iv_list_ncname_pattern_1_5(mode, save_output, output_format):
    r"""
    Type list/NCName is restricted by facet pattern with value
    [\i-[:]][\c-[:]]{39} [\i-[:]][\c-[:]]{15} [\i-[:]][\c-[:]]{23}
    [\i-[:]][\c-[:]]{44} [\i-[:]][\c-[:]]{55} [\i-[:]][\c-[:]]{18}
    [\i-[:]][\c-[:]]{44} [\i-[:]][\c-[:]]{1}.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-pattern-1.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-pattern-1-5.xml",
        class_name="NistschemaSvIvListNcnamePattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_length_4_nistxml_sv_iv_list_ncname_length_5_1(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-length-5.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-length-5-1.xml",
        class_name="NistschemaSvIvListNcnameLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_length_4_nistxml_sv_iv_list_ncname_length_5_2(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-length-5.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-length-5-2.xml",
        class_name="NistschemaSvIvListNcnameLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_length_4_nistxml_sv_iv_list_ncname_length_5_3(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-length-5.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-length-5-3.xml",
        class_name="NistschemaSvIvListNcnameLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_length_4_nistxml_sv_iv_list_ncname_length_5_4(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-length-5.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-length-5-4.xml",
        class_name="NistschemaSvIvListNcnameLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_length_4_nistxml_sv_iv_list_ncname_length_5_5(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-length-5.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-length-5-5.xml",
        class_name="NistschemaSvIvListNcnameLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_length_3_nistxml_sv_iv_list_ncname_length_4_1(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-length-4.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-length-4-1.xml",
        class_name="NistschemaSvIvListNcnameLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_length_3_nistxml_sv_iv_list_ncname_length_4_2(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-length-4.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-length-4-2.xml",
        class_name="NistschemaSvIvListNcnameLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_length_3_nistxml_sv_iv_list_ncname_length_4_3(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-length-4.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-length-4-3.xml",
        class_name="NistschemaSvIvListNcnameLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_length_3_nistxml_sv_iv_list_ncname_length_4_4(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-length-4.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-length-4-4.xml",
        class_name="NistschemaSvIvListNcnameLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_length_3_nistxml_sv_iv_list_ncname_length_4_5(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-length-4.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-length-4-5.xml",
        class_name="NistschemaSvIvListNcnameLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_length_2_nistxml_sv_iv_list_ncname_length_3_1(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-length-3.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-length-3-1.xml",
        class_name="NistschemaSvIvListNcnameLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_length_2_nistxml_sv_iv_list_ncname_length_3_2(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-length-3.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-length-3-2.xml",
        class_name="NistschemaSvIvListNcnameLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_length_2_nistxml_sv_iv_list_ncname_length_3_3(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-length-3.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-length-3-3.xml",
        class_name="NistschemaSvIvListNcnameLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_length_2_nistxml_sv_iv_list_ncname_length_3_4(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-length-3.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-length-3-4.xml",
        class_name="NistschemaSvIvListNcnameLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_length_2_nistxml_sv_iv_list_ncname_length_3_5(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-length-3.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-length-3-5.xml",
        class_name="NistschemaSvIvListNcnameLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_length_1_nistxml_sv_iv_list_ncname_length_2_1(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-length-2.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-length-2-1.xml",
        class_name="NistschemaSvIvListNcnameLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_length_1_nistxml_sv_iv_list_ncname_length_2_2(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-length-2.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-length-2-2.xml",
        class_name="NistschemaSvIvListNcnameLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_length_1_nistxml_sv_iv_list_ncname_length_2_3(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-length-2.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-length-2-3.xml",
        class_name="NistschemaSvIvListNcnameLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_length_1_nistxml_sv_iv_list_ncname_length_2_4(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-length-2.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-length-2-4.xml",
        class_name="NistschemaSvIvListNcnameLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_length_1_nistxml_sv_iv_list_ncname_length_2_5(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-length-2.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-length-2-5.xml",
        class_name="NistschemaSvIvListNcnameLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_length_nistxml_sv_iv_list_ncname_length_1_1(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-length-1.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-length-1-1.xml",
        class_name="NistschemaSvIvListNcnameLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_length_nistxml_sv_iv_list_ncname_length_1_2(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-length-1.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-length-1-2.xml",
        class_name="NistschemaSvIvListNcnameLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_length_nistxml_sv_iv_list_ncname_length_1_3(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-length-1.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-length-1-3.xml",
        class_name="NistschemaSvIvListNcnameLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_length_nistxml_sv_iv_list_ncname_length_1_4(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-length-1.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-length-1-4.xml",
        class_name="NistschemaSvIvListNcnameLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_length_nistxml_sv_iv_list_ncname_length_1_5(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-length-1.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-length-1-5.xml",
        class_name="NistschemaSvIvListNcnameLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_min_length_4_nistxml_sv_iv_list_ncname_min_length_5_1(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-minLength-5.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-minLength-5-1.xml",
        class_name="NistschemaSvIvListNcnameMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_min_length_4_nistxml_sv_iv_list_ncname_min_length_5_2(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-minLength-5.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-minLength-5-2.xml",
        class_name="NistschemaSvIvListNcnameMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_min_length_4_nistxml_sv_iv_list_ncname_min_length_5_3(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-minLength-5.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-minLength-5-3.xml",
        class_name="NistschemaSvIvListNcnameMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_min_length_4_nistxml_sv_iv_list_ncname_min_length_5_4(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-minLength-5.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-minLength-5-4.xml",
        class_name="NistschemaSvIvListNcnameMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_min_length_4_nistxml_sv_iv_list_ncname_min_length_5_5(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-minLength-5.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-minLength-5-5.xml",
        class_name="NistschemaSvIvListNcnameMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_min_length_3_nistxml_sv_iv_list_ncname_min_length_4_1(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-minLength-4.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-minLength-4-1.xml",
        class_name="NistschemaSvIvListNcnameMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_min_length_3_nistxml_sv_iv_list_ncname_min_length_4_2(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-minLength-4.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-minLength-4-2.xml",
        class_name="NistschemaSvIvListNcnameMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_min_length_3_nistxml_sv_iv_list_ncname_min_length_4_3(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-minLength-4.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-minLength-4-3.xml",
        class_name="NistschemaSvIvListNcnameMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_min_length_3_nistxml_sv_iv_list_ncname_min_length_4_4(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-minLength-4.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-minLength-4-4.xml",
        class_name="NistschemaSvIvListNcnameMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_min_length_3_nistxml_sv_iv_list_ncname_min_length_4_5(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-minLength-4.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-minLength-4-5.xml",
        class_name="NistschemaSvIvListNcnameMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_min_length_2_nistxml_sv_iv_list_ncname_min_length_3_1(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-minLength-3.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-minLength-3-1.xml",
        class_name="NistschemaSvIvListNcnameMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_min_length_2_nistxml_sv_iv_list_ncname_min_length_3_2(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-minLength-3.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-minLength-3-2.xml",
        class_name="NistschemaSvIvListNcnameMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_min_length_2_nistxml_sv_iv_list_ncname_min_length_3_3(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-minLength-3.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-minLength-3-3.xml",
        class_name="NistschemaSvIvListNcnameMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_min_length_2_nistxml_sv_iv_list_ncname_min_length_3_4(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-minLength-3.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-minLength-3-4.xml",
        class_name="NistschemaSvIvListNcnameMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_min_length_2_nistxml_sv_iv_list_ncname_min_length_3_5(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-minLength-3.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-minLength-3-5.xml",
        class_name="NistschemaSvIvListNcnameMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_min_length_1_nistxml_sv_iv_list_ncname_min_length_2_1(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-minLength-2.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-minLength-2-1.xml",
        class_name="NistschemaSvIvListNcnameMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_min_length_1_nistxml_sv_iv_list_ncname_min_length_2_2(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-minLength-2.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-minLength-2-2.xml",
        class_name="NistschemaSvIvListNcnameMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_min_length_1_nistxml_sv_iv_list_ncname_min_length_2_3(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-minLength-2.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-minLength-2-3.xml",
        class_name="NistschemaSvIvListNcnameMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_min_length_1_nistxml_sv_iv_list_ncname_min_length_2_4(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-minLength-2.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-minLength-2-4.xml",
        class_name="NistschemaSvIvListNcnameMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_min_length_1_nistxml_sv_iv_list_ncname_min_length_2_5(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-minLength-2.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-minLength-2-5.xml",
        class_name="NistschemaSvIvListNcnameMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_min_length_nistxml_sv_iv_list_ncname_min_length_1_1(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-minLength-1.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-minLength-1-1.xml",
        class_name="NistschemaSvIvListNcnameMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_min_length_nistxml_sv_iv_list_ncname_min_length_1_2(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-minLength-1.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-minLength-1-2.xml",
        class_name="NistschemaSvIvListNcnameMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_min_length_nistxml_sv_iv_list_ncname_min_length_1_3(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-minLength-1.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-minLength-1-3.xml",
        class_name="NistschemaSvIvListNcnameMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_min_length_nistxml_sv_iv_list_ncname_min_length_1_4(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-minLength-1.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-minLength-1-4.xml",
        class_name="NistschemaSvIvListNcnameMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_min_length_nistxml_sv_iv_list_ncname_min_length_1_5(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-minLength-1.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-minLength-1-5.xml",
        class_name="NistschemaSvIvListNcnameMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_max_length_4_nistxml_sv_iv_list_ncname_max_length_5_1(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-maxLength-5.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-maxLength-5-1.xml",
        class_name="NistschemaSvIvListNcnameMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_max_length_4_nistxml_sv_iv_list_ncname_max_length_5_2(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-maxLength-5.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-maxLength-5-2.xml",
        class_name="NistschemaSvIvListNcnameMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_max_length_4_nistxml_sv_iv_list_ncname_max_length_5_3(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-maxLength-5.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-maxLength-5-3.xml",
        class_name="NistschemaSvIvListNcnameMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_max_length_4_nistxml_sv_iv_list_ncname_max_length_5_4(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-maxLength-5.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-maxLength-5-4.xml",
        class_name="NistschemaSvIvListNcnameMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_max_length_4_nistxml_sv_iv_list_ncname_max_length_5_5(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-maxLength-5.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-maxLength-5-5.xml",
        class_name="NistschemaSvIvListNcnameMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_max_length_3_nistxml_sv_iv_list_ncname_max_length_4_1(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-maxLength-4.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-maxLength-4-1.xml",
        class_name="NistschemaSvIvListNcnameMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_max_length_3_nistxml_sv_iv_list_ncname_max_length_4_2(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-maxLength-4.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-maxLength-4-2.xml",
        class_name="NistschemaSvIvListNcnameMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_max_length_3_nistxml_sv_iv_list_ncname_max_length_4_3(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-maxLength-4.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-maxLength-4-3.xml",
        class_name="NistschemaSvIvListNcnameMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_max_length_3_nistxml_sv_iv_list_ncname_max_length_4_4(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-maxLength-4.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-maxLength-4-4.xml",
        class_name="NistschemaSvIvListNcnameMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_max_length_3_nistxml_sv_iv_list_ncname_max_length_4_5(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-maxLength-4.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-maxLength-4-5.xml",
        class_name="NistschemaSvIvListNcnameMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_max_length_2_nistxml_sv_iv_list_ncname_max_length_3_1(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-maxLength-3.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-maxLength-3-1.xml",
        class_name="NistschemaSvIvListNcnameMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_max_length_2_nistxml_sv_iv_list_ncname_max_length_3_2(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-maxLength-3.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-maxLength-3-2.xml",
        class_name="NistschemaSvIvListNcnameMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_max_length_2_nistxml_sv_iv_list_ncname_max_length_3_3(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-maxLength-3.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-maxLength-3-3.xml",
        class_name="NistschemaSvIvListNcnameMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_max_length_2_nistxml_sv_iv_list_ncname_max_length_3_4(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-maxLength-3.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-maxLength-3-4.xml",
        class_name="NistschemaSvIvListNcnameMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_max_length_2_nistxml_sv_iv_list_ncname_max_length_3_5(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-maxLength-3.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-maxLength-3-5.xml",
        class_name="NistschemaSvIvListNcnameMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_max_length_1_nistxml_sv_iv_list_ncname_max_length_2_1(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-maxLength-2.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-maxLength-2-1.xml",
        class_name="NistschemaSvIvListNcnameMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_max_length_1_nistxml_sv_iv_list_ncname_max_length_2_2(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-maxLength-2.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-maxLength-2-2.xml",
        class_name="NistschemaSvIvListNcnameMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_max_length_1_nistxml_sv_iv_list_ncname_max_length_2_3(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-maxLength-2.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-maxLength-2-3.xml",
        class_name="NistschemaSvIvListNcnameMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_max_length_1_nistxml_sv_iv_list_ncname_max_length_2_4(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-maxLength-2.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-maxLength-2-4.xml",
        class_name="NistschemaSvIvListNcnameMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_max_length_1_nistxml_sv_iv_list_ncname_max_length_2_5(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-maxLength-2.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-maxLength-2-5.xml",
        class_name="NistschemaSvIvListNcnameMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_max_length_nistxml_sv_iv_list_ncname_max_length_1_1(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-maxLength-1.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-maxLength-1-1.xml",
        class_name="NistschemaSvIvListNcnameMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_max_length_nistxml_sv_iv_list_ncname_max_length_1_2(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-maxLength-1.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-maxLength-1-2.xml",
        class_name="NistschemaSvIvListNcnameMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_max_length_nistxml_sv_iv_list_ncname_max_length_1_3(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-maxLength-1.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-maxLength-1-3.xml",
        class_name="NistschemaSvIvListNcnameMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_max_length_nistxml_sv_iv_list_ncname_max_length_1_4(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-maxLength-1.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-maxLength-1-4.xml",
        class_name="NistschemaSvIvListNcnameMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_ncname_max_length_nistxml_sv_iv_list_ncname_max_length_1_5(mode, save_output, output_format):
    """
    Type list/NCName is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/NCName/Schema+Instance/NISTSchema-SV-IV-list-NCName-maxLength-1.xsd",
        instance="nistData/list/NCName/Schema+Instance/NISTXML-SV-IV-list-NCName-maxLength-1-5.xml",
        class_name="NistschemaSvIvListNcnameMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_white_space_nistxml_sv_iv_list_nmtokens_white_space_1_1(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet whiteSpace with value
    collapse.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-whiteSpace-1.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-whiteSpace-1-1.xml",
        class_name="NistschemaSvIvListNmtokensWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_white_space_nistxml_sv_iv_list_nmtokens_white_space_1_2(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet whiteSpace with value
    collapse.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-whiteSpace-1.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-whiteSpace-1-2.xml",
        class_name="NistschemaSvIvListNmtokensWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_white_space_nistxml_sv_iv_list_nmtokens_white_space_1_3(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet whiteSpace with value
    collapse.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-whiteSpace-1.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-whiteSpace-1-3.xml",
        class_name="NistschemaSvIvListNmtokensWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_white_space_nistxml_sv_iv_list_nmtokens_white_space_1_4(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet whiteSpace with value
    collapse.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-whiteSpace-1.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-whiteSpace-1-4.xml",
        class_name="NistschemaSvIvListNmtokensWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_white_space_nistxml_sv_iv_list_nmtokens_white_space_1_5(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet whiteSpace with value
    collapse.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-whiteSpace-1.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-whiteSpace-1-5.xml",
        class_name="NistschemaSvIvListNmtokensWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_enumeration_4_nistxml_sv_iv_list_nmtokens_enumeration_5_1(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-enumeration-5.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-enumeration-5-1.xml",
        class_name="NistschemaSvIvListNmtokensEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_enumeration_4_nistxml_sv_iv_list_nmtokens_enumeration_5_2(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-enumeration-5.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-enumeration-5-2.xml",
        class_name="NistschemaSvIvListNmtokensEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_enumeration_4_nistxml_sv_iv_list_nmtokens_enumeration_5_3(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-enumeration-5.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-enumeration-5-3.xml",
        class_name="NistschemaSvIvListNmtokensEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_enumeration_4_nistxml_sv_iv_list_nmtokens_enumeration_5_4(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-enumeration-5.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-enumeration-5-4.xml",
        class_name="NistschemaSvIvListNmtokensEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_enumeration_4_nistxml_sv_iv_list_nmtokens_enumeration_5_5(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-enumeration-5.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-enumeration-5-5.xml",
        class_name="NistschemaSvIvListNmtokensEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_enumeration_3_nistxml_sv_iv_list_nmtokens_enumeration_4_1(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-enumeration-4.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-enumeration-4-1.xml",
        class_name="NistschemaSvIvListNmtokensEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_enumeration_3_nistxml_sv_iv_list_nmtokens_enumeration_4_2(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-enumeration-4.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-enumeration-4-2.xml",
        class_name="NistschemaSvIvListNmtokensEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_enumeration_3_nistxml_sv_iv_list_nmtokens_enumeration_4_3(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-enumeration-4.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-enumeration-4-3.xml",
        class_name="NistschemaSvIvListNmtokensEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_enumeration_3_nistxml_sv_iv_list_nmtokens_enumeration_4_4(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-enumeration-4.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-enumeration-4-4.xml",
        class_name="NistschemaSvIvListNmtokensEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_enumeration_3_nistxml_sv_iv_list_nmtokens_enumeration_4_5(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-enumeration-4.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-enumeration-4-5.xml",
        class_name="NistschemaSvIvListNmtokensEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_enumeration_2_nistxml_sv_iv_list_nmtokens_enumeration_3_1(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-enumeration-3.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-enumeration-3-1.xml",
        class_name="NistschemaSvIvListNmtokensEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_enumeration_2_nistxml_sv_iv_list_nmtokens_enumeration_3_2(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-enumeration-3.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-enumeration-3-2.xml",
        class_name="NistschemaSvIvListNmtokensEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_enumeration_2_nistxml_sv_iv_list_nmtokens_enumeration_3_3(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-enumeration-3.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-enumeration-3-3.xml",
        class_name="NistschemaSvIvListNmtokensEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_enumeration_2_nistxml_sv_iv_list_nmtokens_enumeration_3_4(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-enumeration-3.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-enumeration-3-4.xml",
        class_name="NistschemaSvIvListNmtokensEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_enumeration_2_nistxml_sv_iv_list_nmtokens_enumeration_3_5(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-enumeration-3.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-enumeration-3-5.xml",
        class_name="NistschemaSvIvListNmtokensEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_enumeration_1_nistxml_sv_iv_list_nmtokens_enumeration_2_1(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-enumeration-2.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-enumeration-2-1.xml",
        class_name="NistschemaSvIvListNmtokensEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_enumeration_1_nistxml_sv_iv_list_nmtokens_enumeration_2_2(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-enumeration-2.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-enumeration-2-2.xml",
        class_name="NistschemaSvIvListNmtokensEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_enumeration_1_nistxml_sv_iv_list_nmtokens_enumeration_2_3(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-enumeration-2.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-enumeration-2-3.xml",
        class_name="NistschemaSvIvListNmtokensEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_enumeration_1_nistxml_sv_iv_list_nmtokens_enumeration_2_4(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-enumeration-2.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-enumeration-2-4.xml",
        class_name="NistschemaSvIvListNmtokensEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_enumeration_1_nistxml_sv_iv_list_nmtokens_enumeration_2_5(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-enumeration-2.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-enumeration-2-5.xml",
        class_name="NistschemaSvIvListNmtokensEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_enumeration_nistxml_sv_iv_list_nmtokens_enumeration_1_1(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-enumeration-1.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-enumeration-1-1.xml",
        class_name="NistschemaSvIvListNmtokensEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_enumeration_nistxml_sv_iv_list_nmtokens_enumeration_1_2(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-enumeration-1.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-enumeration-1-2.xml",
        class_name="NistschemaSvIvListNmtokensEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_enumeration_nistxml_sv_iv_list_nmtokens_enumeration_1_3(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-enumeration-1.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-enumeration-1-3.xml",
        class_name="NistschemaSvIvListNmtokensEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_enumeration_nistxml_sv_iv_list_nmtokens_enumeration_1_4(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-enumeration-1.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-enumeration-1-4.xml",
        class_name="NistschemaSvIvListNmtokensEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_enumeration_nistxml_sv_iv_list_nmtokens_enumeration_1_5(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-enumeration-1.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-enumeration-1-5.xml",
        class_name="NistschemaSvIvListNmtokensEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_pattern_4_nistxml_sv_iv_list_nmtokens_pattern_5_1(mode, save_output, output_format):
    r"""
    Type list/NMTOKENS is restricted by facet pattern with value \c{44}
    \c{22} \c{22} \c{56} \c{18} \c{15} \c{5} \c{38}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-pattern-5.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-pattern-5-1.xml",
        class_name="NistschemaSvIvListNmtokensPattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_pattern_4_nistxml_sv_iv_list_nmtokens_pattern_5_2(mode, save_output, output_format):
    r"""
    Type list/NMTOKENS is restricted by facet pattern with value \c{44}
    \c{22} \c{22} \c{56} \c{18} \c{15} \c{5} \c{38}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-pattern-5.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-pattern-5-2.xml",
        class_name="NistschemaSvIvListNmtokensPattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_pattern_4_nistxml_sv_iv_list_nmtokens_pattern_5_3(mode, save_output, output_format):
    r"""
    Type list/NMTOKENS is restricted by facet pattern with value \c{44}
    \c{22} \c{22} \c{56} \c{18} \c{15} \c{5} \c{38}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-pattern-5.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-pattern-5-3.xml",
        class_name="NistschemaSvIvListNmtokensPattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_pattern_4_nistxml_sv_iv_list_nmtokens_pattern_5_4(mode, save_output, output_format):
    r"""
    Type list/NMTOKENS is restricted by facet pattern with value \c{44}
    \c{22} \c{22} \c{56} \c{18} \c{15} \c{5} \c{38}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-pattern-5.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-pattern-5-4.xml",
        class_name="NistschemaSvIvListNmtokensPattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_pattern_4_nistxml_sv_iv_list_nmtokens_pattern_5_5(mode, save_output, output_format):
    r"""
    Type list/NMTOKENS is restricted by facet pattern with value \c{44}
    \c{22} \c{22} \c{56} \c{18} \c{15} \c{5} \c{38}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-pattern-5.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-pattern-5-5.xml",
        class_name="NistschemaSvIvListNmtokensPattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_pattern_3_nistxml_sv_iv_list_nmtokens_pattern_4_1(mode, save_output, output_format):
    r"""
    Type list/NMTOKENS is restricted by facet pattern with value \c{29}
    \c{7} \c{23} \c{2} \c{63} \c{24} \c{34} \c{59}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-pattern-4.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-pattern-4-1.xml",
        class_name="NistschemaSvIvListNmtokensPattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_pattern_3_nistxml_sv_iv_list_nmtokens_pattern_4_2(mode, save_output, output_format):
    r"""
    Type list/NMTOKENS is restricted by facet pattern with value \c{29}
    \c{7} \c{23} \c{2} \c{63} \c{24} \c{34} \c{59}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-pattern-4.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-pattern-4-2.xml",
        class_name="NistschemaSvIvListNmtokensPattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_pattern_3_nistxml_sv_iv_list_nmtokens_pattern_4_3(mode, save_output, output_format):
    r"""
    Type list/NMTOKENS is restricted by facet pattern with value \c{29}
    \c{7} \c{23} \c{2} \c{63} \c{24} \c{34} \c{59}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-pattern-4.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-pattern-4-3.xml",
        class_name="NistschemaSvIvListNmtokensPattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_pattern_3_nistxml_sv_iv_list_nmtokens_pattern_4_4(mode, save_output, output_format):
    r"""
    Type list/NMTOKENS is restricted by facet pattern with value \c{29}
    \c{7} \c{23} \c{2} \c{63} \c{24} \c{34} \c{59}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-pattern-4.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-pattern-4-4.xml",
        class_name="NistschemaSvIvListNmtokensPattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_pattern_3_nistxml_sv_iv_list_nmtokens_pattern_4_5(mode, save_output, output_format):
    r"""
    Type list/NMTOKENS is restricted by facet pattern with value \c{29}
    \c{7} \c{23} \c{2} \c{63} \c{24} \c{34} \c{59}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-pattern-4.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-pattern-4-5.xml",
        class_name="NistschemaSvIvListNmtokensPattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_pattern_2_nistxml_sv_iv_list_nmtokens_pattern_3_1(mode, save_output, output_format):
    r"""
    Type list/NMTOKENS is restricted by facet pattern with value \c{20}
    \c{48} \c{3} \c{54} \c{13} \c{29} \c{5}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-pattern-3.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-pattern-3-1.xml",
        class_name="NistschemaSvIvListNmtokensPattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_pattern_2_nistxml_sv_iv_list_nmtokens_pattern_3_2(mode, save_output, output_format):
    r"""
    Type list/NMTOKENS is restricted by facet pattern with value \c{20}
    \c{48} \c{3} \c{54} \c{13} \c{29} \c{5}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-pattern-3.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-pattern-3-2.xml",
        class_name="NistschemaSvIvListNmtokensPattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_pattern_2_nistxml_sv_iv_list_nmtokens_pattern_3_3(mode, save_output, output_format):
    r"""
    Type list/NMTOKENS is restricted by facet pattern with value \c{20}
    \c{48} \c{3} \c{54} \c{13} \c{29} \c{5}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-pattern-3.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-pattern-3-3.xml",
        class_name="NistschemaSvIvListNmtokensPattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_pattern_2_nistxml_sv_iv_list_nmtokens_pattern_3_4(mode, save_output, output_format):
    r"""
    Type list/NMTOKENS is restricted by facet pattern with value \c{20}
    \c{48} \c{3} \c{54} \c{13} \c{29} \c{5}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-pattern-3.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-pattern-3-4.xml",
        class_name="NistschemaSvIvListNmtokensPattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_pattern_2_nistxml_sv_iv_list_nmtokens_pattern_3_5(mode, save_output, output_format):
    r"""
    Type list/NMTOKENS is restricted by facet pattern with value \c{20}
    \c{48} \c{3} \c{54} \c{13} \c{29} \c{5}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-pattern-3.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-pattern-3-5.xml",
        class_name="NistschemaSvIvListNmtokensPattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_pattern_1_nistxml_sv_iv_list_nmtokens_pattern_2_1(mode, save_output, output_format):
    r"""
    Type list/NMTOKENS is restricted by facet pattern with value \c{64}
    \c{61} \c{8} \c{25} \c{14} \c{53} \c{12} \c{20}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-pattern-2.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-pattern-2-1.xml",
        class_name="NistschemaSvIvListNmtokensPattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_pattern_1_nistxml_sv_iv_list_nmtokens_pattern_2_2(mode, save_output, output_format):
    r"""
    Type list/NMTOKENS is restricted by facet pattern with value \c{64}
    \c{61} \c{8} \c{25} \c{14} \c{53} \c{12} \c{20}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-pattern-2.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-pattern-2-2.xml",
        class_name="NistschemaSvIvListNmtokensPattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_pattern_1_nistxml_sv_iv_list_nmtokens_pattern_2_3(mode, save_output, output_format):
    r"""
    Type list/NMTOKENS is restricted by facet pattern with value \c{64}
    \c{61} \c{8} \c{25} \c{14} \c{53} \c{12} \c{20}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-pattern-2.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-pattern-2-3.xml",
        class_name="NistschemaSvIvListNmtokensPattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_pattern_1_nistxml_sv_iv_list_nmtokens_pattern_2_4(mode, save_output, output_format):
    r"""
    Type list/NMTOKENS is restricted by facet pattern with value \c{64}
    \c{61} \c{8} \c{25} \c{14} \c{53} \c{12} \c{20}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-pattern-2.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-pattern-2-4.xml",
        class_name="NistschemaSvIvListNmtokensPattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_pattern_1_nistxml_sv_iv_list_nmtokens_pattern_2_5(mode, save_output, output_format):
    r"""
    Type list/NMTOKENS is restricted by facet pattern with value \c{64}
    \c{61} \c{8} \c{25} \c{14} \c{53} \c{12} \c{20}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-pattern-2.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-pattern-2-5.xml",
        class_name="NistschemaSvIvListNmtokensPattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_pattern_nistxml_sv_iv_list_nmtokens_pattern_1_1(mode, save_output, output_format):
    r"""
    Type list/NMTOKENS is restricted by facet pattern with value \c{16}
    \c{9} \c{44} \c{34} \c{46} \c{6}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-pattern-1.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-pattern-1-1.xml",
        class_name="NistschemaSvIvListNmtokensPattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_pattern_nistxml_sv_iv_list_nmtokens_pattern_1_2(mode, save_output, output_format):
    r"""
    Type list/NMTOKENS is restricted by facet pattern with value \c{16}
    \c{9} \c{44} \c{34} \c{46} \c{6}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-pattern-1.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-pattern-1-2.xml",
        class_name="NistschemaSvIvListNmtokensPattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_pattern_nistxml_sv_iv_list_nmtokens_pattern_1_3(mode, save_output, output_format):
    r"""
    Type list/NMTOKENS is restricted by facet pattern with value \c{16}
    \c{9} \c{44} \c{34} \c{46} \c{6}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-pattern-1.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-pattern-1-3.xml",
        class_name="NistschemaSvIvListNmtokensPattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_pattern_nistxml_sv_iv_list_nmtokens_pattern_1_4(mode, save_output, output_format):
    r"""
    Type list/NMTOKENS is restricted by facet pattern with value \c{16}
    \c{9} \c{44} \c{34} \c{46} \c{6}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-pattern-1.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-pattern-1-4.xml",
        class_name="NistschemaSvIvListNmtokensPattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_pattern_nistxml_sv_iv_list_nmtokens_pattern_1_5(mode, save_output, output_format):
    r"""
    Type list/NMTOKENS is restricted by facet pattern with value \c{16}
    \c{9} \c{44} \c{34} \c{46} \c{6}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-pattern-1.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-pattern-1-5.xml",
        class_name="NistschemaSvIvListNmtokensPattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_length_4_nistxml_sv_iv_list_nmtokens_length_5_1(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-length-5.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-length-5-1.xml",
        class_name="NistschemaSvIvListNmtokensLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_length_4_nistxml_sv_iv_list_nmtokens_length_5_2(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-length-5.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-length-5-2.xml",
        class_name="NistschemaSvIvListNmtokensLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_length_4_nistxml_sv_iv_list_nmtokens_length_5_3(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-length-5.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-length-5-3.xml",
        class_name="NistschemaSvIvListNmtokensLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_length_4_nistxml_sv_iv_list_nmtokens_length_5_4(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-length-5.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-length-5-4.xml",
        class_name="NistschemaSvIvListNmtokensLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_length_4_nistxml_sv_iv_list_nmtokens_length_5_5(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-length-5.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-length-5-5.xml",
        class_name="NistschemaSvIvListNmtokensLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_length_3_nistxml_sv_iv_list_nmtokens_length_4_1(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-length-4.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-length-4-1.xml",
        class_name="NistschemaSvIvListNmtokensLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_length_3_nistxml_sv_iv_list_nmtokens_length_4_2(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-length-4.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-length-4-2.xml",
        class_name="NistschemaSvIvListNmtokensLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_length_3_nistxml_sv_iv_list_nmtokens_length_4_3(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-length-4.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-length-4-3.xml",
        class_name="NistschemaSvIvListNmtokensLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_length_3_nistxml_sv_iv_list_nmtokens_length_4_4(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-length-4.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-length-4-4.xml",
        class_name="NistschemaSvIvListNmtokensLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_length_3_nistxml_sv_iv_list_nmtokens_length_4_5(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-length-4.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-length-4-5.xml",
        class_name="NistschemaSvIvListNmtokensLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_length_2_nistxml_sv_iv_list_nmtokens_length_3_1(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-length-3.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-length-3-1.xml",
        class_name="NistschemaSvIvListNmtokensLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_length_2_nistxml_sv_iv_list_nmtokens_length_3_2(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-length-3.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-length-3-2.xml",
        class_name="NistschemaSvIvListNmtokensLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_length_2_nistxml_sv_iv_list_nmtokens_length_3_3(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-length-3.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-length-3-3.xml",
        class_name="NistschemaSvIvListNmtokensLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_length_2_nistxml_sv_iv_list_nmtokens_length_3_4(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-length-3.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-length-3-4.xml",
        class_name="NistschemaSvIvListNmtokensLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_length_2_nistxml_sv_iv_list_nmtokens_length_3_5(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-length-3.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-length-3-5.xml",
        class_name="NistschemaSvIvListNmtokensLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_length_1_nistxml_sv_iv_list_nmtokens_length_2_1(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-length-2.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-length-2-1.xml",
        class_name="NistschemaSvIvListNmtokensLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_length_1_nistxml_sv_iv_list_nmtokens_length_2_2(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-length-2.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-length-2-2.xml",
        class_name="NistschemaSvIvListNmtokensLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_length_1_nistxml_sv_iv_list_nmtokens_length_2_3(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-length-2.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-length-2-3.xml",
        class_name="NistschemaSvIvListNmtokensLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_length_1_nistxml_sv_iv_list_nmtokens_length_2_4(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-length-2.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-length-2-4.xml",
        class_name="NistschemaSvIvListNmtokensLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_length_1_nistxml_sv_iv_list_nmtokens_length_2_5(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-length-2.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-length-2-5.xml",
        class_name="NistschemaSvIvListNmtokensLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_length_nistxml_sv_iv_list_nmtokens_length_1_1(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-length-1.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-length-1-1.xml",
        class_name="NistschemaSvIvListNmtokensLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_length_nistxml_sv_iv_list_nmtokens_length_1_2(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-length-1.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-length-1-2.xml",
        class_name="NistschemaSvIvListNmtokensLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_length_nistxml_sv_iv_list_nmtokens_length_1_3(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-length-1.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-length-1-3.xml",
        class_name="NistschemaSvIvListNmtokensLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_length_nistxml_sv_iv_list_nmtokens_length_1_4(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-length-1.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-length-1-4.xml",
        class_name="NistschemaSvIvListNmtokensLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_length_nistxml_sv_iv_list_nmtokens_length_1_5(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-length-1.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-length-1-5.xml",
        class_name="NistschemaSvIvListNmtokensLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_min_length_4_nistxml_sv_iv_list_nmtokens_min_length_5_1(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-minLength-5.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-minLength-5-1.xml",
        class_name="NistschemaSvIvListNmtokensMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_min_length_4_nistxml_sv_iv_list_nmtokens_min_length_5_2(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-minLength-5.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-minLength-5-2.xml",
        class_name="NistschemaSvIvListNmtokensMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_min_length_4_nistxml_sv_iv_list_nmtokens_min_length_5_3(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-minLength-5.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-minLength-5-3.xml",
        class_name="NistschemaSvIvListNmtokensMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_min_length_4_nistxml_sv_iv_list_nmtokens_min_length_5_4(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-minLength-5.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-minLength-5-4.xml",
        class_name="NistschemaSvIvListNmtokensMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_min_length_4_nistxml_sv_iv_list_nmtokens_min_length_5_5(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-minLength-5.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-minLength-5-5.xml",
        class_name="NistschemaSvIvListNmtokensMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_min_length_3_nistxml_sv_iv_list_nmtokens_min_length_4_1(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-minLength-4.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-minLength-4-1.xml",
        class_name="NistschemaSvIvListNmtokensMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_min_length_3_nistxml_sv_iv_list_nmtokens_min_length_4_2(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-minLength-4.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-minLength-4-2.xml",
        class_name="NistschemaSvIvListNmtokensMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_min_length_3_nistxml_sv_iv_list_nmtokens_min_length_4_3(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-minLength-4.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-minLength-4-3.xml",
        class_name="NistschemaSvIvListNmtokensMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_min_length_3_nistxml_sv_iv_list_nmtokens_min_length_4_4(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-minLength-4.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-minLength-4-4.xml",
        class_name="NistschemaSvIvListNmtokensMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_min_length_3_nistxml_sv_iv_list_nmtokens_min_length_4_5(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-minLength-4.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-minLength-4-5.xml",
        class_name="NistschemaSvIvListNmtokensMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_min_length_2_nistxml_sv_iv_list_nmtokens_min_length_3_1(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-minLength-3.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-minLength-3-1.xml",
        class_name="NistschemaSvIvListNmtokensMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_min_length_2_nistxml_sv_iv_list_nmtokens_min_length_3_2(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-minLength-3.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-minLength-3-2.xml",
        class_name="NistschemaSvIvListNmtokensMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_min_length_2_nistxml_sv_iv_list_nmtokens_min_length_3_3(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-minLength-3.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-minLength-3-3.xml",
        class_name="NistschemaSvIvListNmtokensMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_min_length_2_nistxml_sv_iv_list_nmtokens_min_length_3_4(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-minLength-3.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-minLength-3-4.xml",
        class_name="NistschemaSvIvListNmtokensMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_min_length_2_nistxml_sv_iv_list_nmtokens_min_length_3_5(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-minLength-3.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-minLength-3-5.xml",
        class_name="NistschemaSvIvListNmtokensMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_min_length_1_nistxml_sv_iv_list_nmtokens_min_length_2_1(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-minLength-2.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-minLength-2-1.xml",
        class_name="NistschemaSvIvListNmtokensMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_min_length_1_nistxml_sv_iv_list_nmtokens_min_length_2_2(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-minLength-2.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-minLength-2-2.xml",
        class_name="NistschemaSvIvListNmtokensMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_min_length_1_nistxml_sv_iv_list_nmtokens_min_length_2_3(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-minLength-2.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-minLength-2-3.xml",
        class_name="NistschemaSvIvListNmtokensMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_min_length_1_nistxml_sv_iv_list_nmtokens_min_length_2_4(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-minLength-2.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-minLength-2-4.xml",
        class_name="NistschemaSvIvListNmtokensMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_min_length_1_nistxml_sv_iv_list_nmtokens_min_length_2_5(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-minLength-2.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-minLength-2-5.xml",
        class_name="NistschemaSvIvListNmtokensMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_min_length_nistxml_sv_iv_list_nmtokens_min_length_1_1(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-minLength-1.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-minLength-1-1.xml",
        class_name="NistschemaSvIvListNmtokensMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_min_length_nistxml_sv_iv_list_nmtokens_min_length_1_2(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-minLength-1.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-minLength-1-2.xml",
        class_name="NistschemaSvIvListNmtokensMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_min_length_nistxml_sv_iv_list_nmtokens_min_length_1_3(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-minLength-1.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-minLength-1-3.xml",
        class_name="NistschemaSvIvListNmtokensMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_min_length_nistxml_sv_iv_list_nmtokens_min_length_1_4(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-minLength-1.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-minLength-1-4.xml",
        class_name="NistschemaSvIvListNmtokensMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_min_length_nistxml_sv_iv_list_nmtokens_min_length_1_5(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-minLength-1.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-minLength-1-5.xml",
        class_name="NistschemaSvIvListNmtokensMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_max_length_4_nistxml_sv_iv_list_nmtokens_max_length_5_1(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-maxLength-5.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-maxLength-5-1.xml",
        class_name="NistschemaSvIvListNmtokensMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_max_length_4_nistxml_sv_iv_list_nmtokens_max_length_5_2(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-maxLength-5.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-maxLength-5-2.xml",
        class_name="NistschemaSvIvListNmtokensMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_max_length_4_nistxml_sv_iv_list_nmtokens_max_length_5_3(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-maxLength-5.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-maxLength-5-3.xml",
        class_name="NistschemaSvIvListNmtokensMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_max_length_4_nistxml_sv_iv_list_nmtokens_max_length_5_4(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-maxLength-5.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-maxLength-5-4.xml",
        class_name="NistschemaSvIvListNmtokensMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_max_length_4_nistxml_sv_iv_list_nmtokens_max_length_5_5(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-maxLength-5.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-maxLength-5-5.xml",
        class_name="NistschemaSvIvListNmtokensMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_max_length_3_nistxml_sv_iv_list_nmtokens_max_length_4_1(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-maxLength-4.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-maxLength-4-1.xml",
        class_name="NistschemaSvIvListNmtokensMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_max_length_3_nistxml_sv_iv_list_nmtokens_max_length_4_2(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-maxLength-4.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-maxLength-4-2.xml",
        class_name="NistschemaSvIvListNmtokensMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_max_length_3_nistxml_sv_iv_list_nmtokens_max_length_4_3(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-maxLength-4.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-maxLength-4-3.xml",
        class_name="NistschemaSvIvListNmtokensMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_max_length_3_nistxml_sv_iv_list_nmtokens_max_length_4_4(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-maxLength-4.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-maxLength-4-4.xml",
        class_name="NistschemaSvIvListNmtokensMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_max_length_3_nistxml_sv_iv_list_nmtokens_max_length_4_5(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-maxLength-4.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-maxLength-4-5.xml",
        class_name="NistschemaSvIvListNmtokensMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_max_length_2_nistxml_sv_iv_list_nmtokens_max_length_3_1(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-maxLength-3.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-maxLength-3-1.xml",
        class_name="NistschemaSvIvListNmtokensMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_max_length_2_nistxml_sv_iv_list_nmtokens_max_length_3_2(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-maxLength-3.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-maxLength-3-2.xml",
        class_name="NistschemaSvIvListNmtokensMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_max_length_2_nistxml_sv_iv_list_nmtokens_max_length_3_3(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-maxLength-3.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-maxLength-3-3.xml",
        class_name="NistschemaSvIvListNmtokensMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_max_length_2_nistxml_sv_iv_list_nmtokens_max_length_3_4(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-maxLength-3.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-maxLength-3-4.xml",
        class_name="NistschemaSvIvListNmtokensMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_max_length_2_nistxml_sv_iv_list_nmtokens_max_length_3_5(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-maxLength-3.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-maxLength-3-5.xml",
        class_name="NistschemaSvIvListNmtokensMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_max_length_1_nistxml_sv_iv_list_nmtokens_max_length_2_1(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-maxLength-2.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-maxLength-2-1.xml",
        class_name="NistschemaSvIvListNmtokensMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_max_length_1_nistxml_sv_iv_list_nmtokens_max_length_2_2(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-maxLength-2.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-maxLength-2-2.xml",
        class_name="NistschemaSvIvListNmtokensMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_max_length_1_nistxml_sv_iv_list_nmtokens_max_length_2_3(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-maxLength-2.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-maxLength-2-3.xml",
        class_name="NistschemaSvIvListNmtokensMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_max_length_1_nistxml_sv_iv_list_nmtokens_max_length_2_4(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-maxLength-2.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-maxLength-2-4.xml",
        class_name="NistschemaSvIvListNmtokensMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_max_length_1_nistxml_sv_iv_list_nmtokens_max_length_2_5(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-maxLength-2.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-maxLength-2-5.xml",
        class_name="NistschemaSvIvListNmtokensMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_max_length_nistxml_sv_iv_list_nmtokens_max_length_1_1(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-maxLength-1.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-maxLength-1-1.xml",
        class_name="NistschemaSvIvListNmtokensMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_max_length_nistxml_sv_iv_list_nmtokens_max_length_1_2(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-maxLength-1.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-maxLength-1-2.xml",
        class_name="NistschemaSvIvListNmtokensMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_max_length_nistxml_sv_iv_list_nmtokens_max_length_1_3(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-maxLength-1.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-maxLength-1-3.xml",
        class_name="NistschemaSvIvListNmtokensMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_max_length_nistxml_sv_iv_list_nmtokens_max_length_1_4(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-maxLength-1.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-maxLength-1-4.xml",
        class_name="NistschemaSvIvListNmtokensMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtokens_max_length_nistxml_sv_iv_list_nmtokens_max_length_1_5(mode, save_output, output_format):
    """
    Type list/NMTOKENS is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/NMTOKENS/Schema+Instance/NISTSchema-SV-IV-list-NMTOKENS-maxLength-1.xsd",
        instance="nistData/list/NMTOKENS/Schema+Instance/NISTXML-SV-IV-list-NMTOKENS-maxLength-1-5.xml",
        class_name="NistschemaSvIvListNmtokensMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_white_space_nistxml_sv_iv_list_nmtoken_white_space_1_1(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet whiteSpace with value
    collapse.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-whiteSpace-1.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-whiteSpace-1-1.xml",
        class_name="NistschemaSvIvListNmtokenWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_white_space_nistxml_sv_iv_list_nmtoken_white_space_1_2(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet whiteSpace with value
    collapse.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-whiteSpace-1.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-whiteSpace-1-2.xml",
        class_name="NistschemaSvIvListNmtokenWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_white_space_nistxml_sv_iv_list_nmtoken_white_space_1_3(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet whiteSpace with value
    collapse.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-whiteSpace-1.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-whiteSpace-1-3.xml",
        class_name="NistschemaSvIvListNmtokenWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_white_space_nistxml_sv_iv_list_nmtoken_white_space_1_4(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet whiteSpace with value
    collapse.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-whiteSpace-1.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-whiteSpace-1-4.xml",
        class_name="NistschemaSvIvListNmtokenWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_white_space_nistxml_sv_iv_list_nmtoken_white_space_1_5(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet whiteSpace with value
    collapse.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-whiteSpace-1.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-whiteSpace-1-5.xml",
        class_name="NistschemaSvIvListNmtokenWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_enumeration_4_nistxml_sv_iv_list_nmtoken_enumeration_5_1(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-enumeration-5.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-enumeration-5-1.xml",
        class_name="NistschemaSvIvListNmtokenEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_enumeration_4_nistxml_sv_iv_list_nmtoken_enumeration_5_2(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-enumeration-5.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-enumeration-5-2.xml",
        class_name="NistschemaSvIvListNmtokenEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_enumeration_4_nistxml_sv_iv_list_nmtoken_enumeration_5_3(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-enumeration-5.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-enumeration-5-3.xml",
        class_name="NistschemaSvIvListNmtokenEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_enumeration_4_nistxml_sv_iv_list_nmtoken_enumeration_5_4(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-enumeration-5.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-enumeration-5-4.xml",
        class_name="NistschemaSvIvListNmtokenEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_enumeration_4_nistxml_sv_iv_list_nmtoken_enumeration_5_5(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-enumeration-5.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-enumeration-5-5.xml",
        class_name="NistschemaSvIvListNmtokenEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_enumeration_3_nistxml_sv_iv_list_nmtoken_enumeration_4_1(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-enumeration-4.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-enumeration-4-1.xml",
        class_name="NistschemaSvIvListNmtokenEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_enumeration_3_nistxml_sv_iv_list_nmtoken_enumeration_4_2(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-enumeration-4.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-enumeration-4-2.xml",
        class_name="NistschemaSvIvListNmtokenEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_enumeration_3_nistxml_sv_iv_list_nmtoken_enumeration_4_3(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-enumeration-4.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-enumeration-4-3.xml",
        class_name="NistschemaSvIvListNmtokenEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_enumeration_3_nistxml_sv_iv_list_nmtoken_enumeration_4_4(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-enumeration-4.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-enumeration-4-4.xml",
        class_name="NistschemaSvIvListNmtokenEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_enumeration_3_nistxml_sv_iv_list_nmtoken_enumeration_4_5(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-enumeration-4.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-enumeration-4-5.xml",
        class_name="NistschemaSvIvListNmtokenEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_enumeration_2_nistxml_sv_iv_list_nmtoken_enumeration_3_1(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-enumeration-3.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-enumeration-3-1.xml",
        class_name="NistschemaSvIvListNmtokenEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_enumeration_2_nistxml_sv_iv_list_nmtoken_enumeration_3_2(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-enumeration-3.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-enumeration-3-2.xml",
        class_name="NistschemaSvIvListNmtokenEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_enumeration_2_nistxml_sv_iv_list_nmtoken_enumeration_3_3(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-enumeration-3.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-enumeration-3-3.xml",
        class_name="NistschemaSvIvListNmtokenEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_enumeration_2_nistxml_sv_iv_list_nmtoken_enumeration_3_4(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-enumeration-3.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-enumeration-3-4.xml",
        class_name="NistschemaSvIvListNmtokenEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_enumeration_2_nistxml_sv_iv_list_nmtoken_enumeration_3_5(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-enumeration-3.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-enumeration-3-5.xml",
        class_name="NistschemaSvIvListNmtokenEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_enumeration_1_nistxml_sv_iv_list_nmtoken_enumeration_2_1(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-enumeration-2.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-enumeration-2-1.xml",
        class_name="NistschemaSvIvListNmtokenEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_enumeration_1_nistxml_sv_iv_list_nmtoken_enumeration_2_2(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-enumeration-2.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-enumeration-2-2.xml",
        class_name="NistschemaSvIvListNmtokenEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_enumeration_1_nistxml_sv_iv_list_nmtoken_enumeration_2_3(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-enumeration-2.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-enumeration-2-3.xml",
        class_name="NistschemaSvIvListNmtokenEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_enumeration_1_nistxml_sv_iv_list_nmtoken_enumeration_2_4(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-enumeration-2.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-enumeration-2-4.xml",
        class_name="NistschemaSvIvListNmtokenEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_enumeration_1_nistxml_sv_iv_list_nmtoken_enumeration_2_5(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-enumeration-2.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-enumeration-2-5.xml",
        class_name="NistschemaSvIvListNmtokenEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_enumeration_nistxml_sv_iv_list_nmtoken_enumeration_1_1(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-enumeration-1.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-enumeration-1-1.xml",
        class_name="NistschemaSvIvListNmtokenEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_enumeration_nistxml_sv_iv_list_nmtoken_enumeration_1_2(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-enumeration-1.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-enumeration-1-2.xml",
        class_name="NistschemaSvIvListNmtokenEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_enumeration_nistxml_sv_iv_list_nmtoken_enumeration_1_3(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-enumeration-1.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-enumeration-1-3.xml",
        class_name="NistschemaSvIvListNmtokenEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_enumeration_nistxml_sv_iv_list_nmtoken_enumeration_1_4(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-enumeration-1.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-enumeration-1-4.xml",
        class_name="NistschemaSvIvListNmtokenEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_enumeration_nistxml_sv_iv_list_nmtoken_enumeration_1_5(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-enumeration-1.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-enumeration-1-5.xml",
        class_name="NistschemaSvIvListNmtokenEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_pattern_4_nistxml_sv_iv_list_nmtoken_pattern_5_1(mode, save_output, output_format):
    r"""
    Type list/NMTOKEN is restricted by facet pattern with value \c{45}
    \c{5} \c{56} \c{45} \c{33} \c{37} \c{45} \c{40}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-pattern-5.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-pattern-5-1.xml",
        class_name="NistschemaSvIvListNmtokenPattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_pattern_4_nistxml_sv_iv_list_nmtoken_pattern_5_2(mode, save_output, output_format):
    r"""
    Type list/NMTOKEN is restricted by facet pattern with value \c{45}
    \c{5} \c{56} \c{45} \c{33} \c{37} \c{45} \c{40}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-pattern-5.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-pattern-5-2.xml",
        class_name="NistschemaSvIvListNmtokenPattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_pattern_4_nistxml_sv_iv_list_nmtoken_pattern_5_3(mode, save_output, output_format):
    r"""
    Type list/NMTOKEN is restricted by facet pattern with value \c{45}
    \c{5} \c{56} \c{45} \c{33} \c{37} \c{45} \c{40}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-pattern-5.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-pattern-5-3.xml",
        class_name="NistschemaSvIvListNmtokenPattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_pattern_4_nistxml_sv_iv_list_nmtoken_pattern_5_4(mode, save_output, output_format):
    r"""
    Type list/NMTOKEN is restricted by facet pattern with value \c{45}
    \c{5} \c{56} \c{45} \c{33} \c{37} \c{45} \c{40}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-pattern-5.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-pattern-5-4.xml",
        class_name="NistschemaSvIvListNmtokenPattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_pattern_4_nistxml_sv_iv_list_nmtoken_pattern_5_5(mode, save_output, output_format):
    r"""
    Type list/NMTOKEN is restricted by facet pattern with value \c{45}
    \c{5} \c{56} \c{45} \c{33} \c{37} \c{45} \c{40}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-pattern-5.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-pattern-5-5.xml",
        class_name="NistschemaSvIvListNmtokenPattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_pattern_3_nistxml_sv_iv_list_nmtoken_pattern_4_1(mode, save_output, output_format):
    r"""
    Type list/NMTOKEN is restricted by facet pattern with value \c{35}
    \c{8} \c{43} \c{19} \c{53} \c{18} \c{33} \c{59} \c{10} \c{41}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-pattern-4.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-pattern-4-1.xml",
        class_name="NistschemaSvIvListNmtokenPattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_pattern_3_nistxml_sv_iv_list_nmtoken_pattern_4_2(mode, save_output, output_format):
    r"""
    Type list/NMTOKEN is restricted by facet pattern with value \c{35}
    \c{8} \c{43} \c{19} \c{53} \c{18} \c{33} \c{59} \c{10} \c{41}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-pattern-4.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-pattern-4-2.xml",
        class_name="NistschemaSvIvListNmtokenPattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_pattern_3_nistxml_sv_iv_list_nmtoken_pattern_4_3(mode, save_output, output_format):
    r"""
    Type list/NMTOKEN is restricted by facet pattern with value \c{35}
    \c{8} \c{43} \c{19} \c{53} \c{18} \c{33} \c{59} \c{10} \c{41}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-pattern-4.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-pattern-4-3.xml",
        class_name="NistschemaSvIvListNmtokenPattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_pattern_3_nistxml_sv_iv_list_nmtoken_pattern_4_4(mode, save_output, output_format):
    r"""
    Type list/NMTOKEN is restricted by facet pattern with value \c{35}
    \c{8} \c{43} \c{19} \c{53} \c{18} \c{33} \c{59} \c{10} \c{41}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-pattern-4.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-pattern-4-4.xml",
        class_name="NistschemaSvIvListNmtokenPattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_pattern_3_nistxml_sv_iv_list_nmtoken_pattern_4_5(mode, save_output, output_format):
    r"""
    Type list/NMTOKEN is restricted by facet pattern with value \c{35}
    \c{8} \c{43} \c{19} \c{53} \c{18} \c{33} \c{59} \c{10} \c{41}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-pattern-4.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-pattern-4-5.xml",
        class_name="NistschemaSvIvListNmtokenPattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_pattern_2_nistxml_sv_iv_list_nmtoken_pattern_3_1(mode, save_output, output_format):
    r"""
    Type list/NMTOKEN is restricted by facet pattern with value \c{1}
    \c{36} \c{63} \c{7} \c{26} \c{11} \c{55} \c{29}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-pattern-3.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-pattern-3-1.xml",
        class_name="NistschemaSvIvListNmtokenPattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_pattern_2_nistxml_sv_iv_list_nmtoken_pattern_3_2(mode, save_output, output_format):
    r"""
    Type list/NMTOKEN is restricted by facet pattern with value \c{1}
    \c{36} \c{63} \c{7} \c{26} \c{11} \c{55} \c{29}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-pattern-3.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-pattern-3-2.xml",
        class_name="NistschemaSvIvListNmtokenPattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_pattern_2_nistxml_sv_iv_list_nmtoken_pattern_3_3(mode, save_output, output_format):
    r"""
    Type list/NMTOKEN is restricted by facet pattern with value \c{1}
    \c{36} \c{63} \c{7} \c{26} \c{11} \c{55} \c{29}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-pattern-3.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-pattern-3-3.xml",
        class_name="NistschemaSvIvListNmtokenPattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_pattern_2_nistxml_sv_iv_list_nmtoken_pattern_3_4(mode, save_output, output_format):
    r"""
    Type list/NMTOKEN is restricted by facet pattern with value \c{1}
    \c{36} \c{63} \c{7} \c{26} \c{11} \c{55} \c{29}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-pattern-3.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-pattern-3-4.xml",
        class_name="NistschemaSvIvListNmtokenPattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_pattern_2_nistxml_sv_iv_list_nmtoken_pattern_3_5(mode, save_output, output_format):
    r"""
    Type list/NMTOKEN is restricted by facet pattern with value \c{1}
    \c{36} \c{63} \c{7} \c{26} \c{11} \c{55} \c{29}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-pattern-3.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-pattern-3-5.xml",
        class_name="NistschemaSvIvListNmtokenPattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_pattern_1_nistxml_sv_iv_list_nmtoken_pattern_2_1(mode, save_output, output_format):
    r"""
    Type list/NMTOKEN is restricted by facet pattern with value \c{20}
    \c{60} \c{47} \c{22} \c{42} \c{14}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-pattern-2.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-pattern-2-1.xml",
        class_name="NistschemaSvIvListNmtokenPattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_pattern_1_nistxml_sv_iv_list_nmtoken_pattern_2_2(mode, save_output, output_format):
    r"""
    Type list/NMTOKEN is restricted by facet pattern with value \c{20}
    \c{60} \c{47} \c{22} \c{42} \c{14}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-pattern-2.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-pattern-2-2.xml",
        class_name="NistschemaSvIvListNmtokenPattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_pattern_1_nistxml_sv_iv_list_nmtoken_pattern_2_3(mode, save_output, output_format):
    r"""
    Type list/NMTOKEN is restricted by facet pattern with value \c{20}
    \c{60} \c{47} \c{22} \c{42} \c{14}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-pattern-2.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-pattern-2-3.xml",
        class_name="NistschemaSvIvListNmtokenPattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_pattern_1_nistxml_sv_iv_list_nmtoken_pattern_2_4(mode, save_output, output_format):
    r"""
    Type list/NMTOKEN is restricted by facet pattern with value \c{20}
    \c{60} \c{47} \c{22} \c{42} \c{14}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-pattern-2.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-pattern-2-4.xml",
        class_name="NistschemaSvIvListNmtokenPattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_pattern_1_nistxml_sv_iv_list_nmtoken_pattern_2_5(mode, save_output, output_format):
    r"""
    Type list/NMTOKEN is restricted by facet pattern with value \c{20}
    \c{60} \c{47} \c{22} \c{42} \c{14}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-pattern-2.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-pattern-2-5.xml",
        class_name="NistschemaSvIvListNmtokenPattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_pattern_nistxml_sv_iv_list_nmtoken_pattern_1_1(mode, save_output, output_format):
    r"""
    Type list/NMTOKEN is restricted by facet pattern with value \c{40}
    \c{21} \c{50} \c{36} \c{35} \c{42} \c{54} \c{48}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-pattern-1.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-pattern-1-1.xml",
        class_name="NistschemaSvIvListNmtokenPattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_pattern_nistxml_sv_iv_list_nmtoken_pattern_1_2(mode, save_output, output_format):
    r"""
    Type list/NMTOKEN is restricted by facet pattern with value \c{40}
    \c{21} \c{50} \c{36} \c{35} \c{42} \c{54} \c{48}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-pattern-1.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-pattern-1-2.xml",
        class_name="NistschemaSvIvListNmtokenPattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_pattern_nistxml_sv_iv_list_nmtoken_pattern_1_3(mode, save_output, output_format):
    r"""
    Type list/NMTOKEN is restricted by facet pattern with value \c{40}
    \c{21} \c{50} \c{36} \c{35} \c{42} \c{54} \c{48}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-pattern-1.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-pattern-1-3.xml",
        class_name="NistschemaSvIvListNmtokenPattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_pattern_nistxml_sv_iv_list_nmtoken_pattern_1_4(mode, save_output, output_format):
    r"""
    Type list/NMTOKEN is restricted by facet pattern with value \c{40}
    \c{21} \c{50} \c{36} \c{35} \c{42} \c{54} \c{48}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-pattern-1.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-pattern-1-4.xml",
        class_name="NistschemaSvIvListNmtokenPattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_pattern_nistxml_sv_iv_list_nmtoken_pattern_1_5(mode, save_output, output_format):
    r"""
    Type list/NMTOKEN is restricted by facet pattern with value \c{40}
    \c{21} \c{50} \c{36} \c{35} \c{42} \c{54} \c{48}.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-pattern-1.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-pattern-1-5.xml",
        class_name="NistschemaSvIvListNmtokenPattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_length_4_nistxml_sv_iv_list_nmtoken_length_5_1(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-length-5.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-length-5-1.xml",
        class_name="NistschemaSvIvListNmtokenLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_length_4_nistxml_sv_iv_list_nmtoken_length_5_2(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-length-5.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-length-5-2.xml",
        class_name="NistschemaSvIvListNmtokenLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_length_4_nistxml_sv_iv_list_nmtoken_length_5_3(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-length-5.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-length-5-3.xml",
        class_name="NistschemaSvIvListNmtokenLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_length_4_nistxml_sv_iv_list_nmtoken_length_5_4(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-length-5.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-length-5-4.xml",
        class_name="NistschemaSvIvListNmtokenLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_length_4_nistxml_sv_iv_list_nmtoken_length_5_5(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-length-5.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-length-5-5.xml",
        class_name="NistschemaSvIvListNmtokenLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_length_3_nistxml_sv_iv_list_nmtoken_length_4_1(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-length-4.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-length-4-1.xml",
        class_name="NistschemaSvIvListNmtokenLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_length_3_nistxml_sv_iv_list_nmtoken_length_4_2(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-length-4.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-length-4-2.xml",
        class_name="NistschemaSvIvListNmtokenLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_length_3_nistxml_sv_iv_list_nmtoken_length_4_3(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-length-4.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-length-4-3.xml",
        class_name="NistschemaSvIvListNmtokenLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_length_3_nistxml_sv_iv_list_nmtoken_length_4_4(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-length-4.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-length-4-4.xml",
        class_name="NistschemaSvIvListNmtokenLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_length_3_nistxml_sv_iv_list_nmtoken_length_4_5(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-length-4.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-length-4-5.xml",
        class_name="NistschemaSvIvListNmtokenLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_length_2_nistxml_sv_iv_list_nmtoken_length_3_1(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-length-3.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-length-3-1.xml",
        class_name="NistschemaSvIvListNmtokenLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_length_2_nistxml_sv_iv_list_nmtoken_length_3_2(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-length-3.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-length-3-2.xml",
        class_name="NistschemaSvIvListNmtokenLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_length_2_nistxml_sv_iv_list_nmtoken_length_3_3(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-length-3.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-length-3-3.xml",
        class_name="NistschemaSvIvListNmtokenLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_length_2_nistxml_sv_iv_list_nmtoken_length_3_4(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-length-3.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-length-3-4.xml",
        class_name="NistschemaSvIvListNmtokenLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_length_2_nistxml_sv_iv_list_nmtoken_length_3_5(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-length-3.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-length-3-5.xml",
        class_name="NistschemaSvIvListNmtokenLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_length_1_nistxml_sv_iv_list_nmtoken_length_2_1(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-length-2.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-length-2-1.xml",
        class_name="NistschemaSvIvListNmtokenLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_length_1_nistxml_sv_iv_list_nmtoken_length_2_2(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-length-2.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-length-2-2.xml",
        class_name="NistschemaSvIvListNmtokenLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_length_1_nistxml_sv_iv_list_nmtoken_length_2_3(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-length-2.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-length-2-3.xml",
        class_name="NistschemaSvIvListNmtokenLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_length_1_nistxml_sv_iv_list_nmtoken_length_2_4(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-length-2.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-length-2-4.xml",
        class_name="NistschemaSvIvListNmtokenLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_length_1_nistxml_sv_iv_list_nmtoken_length_2_5(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-length-2.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-length-2-5.xml",
        class_name="NistschemaSvIvListNmtokenLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_length_nistxml_sv_iv_list_nmtoken_length_1_1(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-length-1.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-length-1-1.xml",
        class_name="NistschemaSvIvListNmtokenLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_length_nistxml_sv_iv_list_nmtoken_length_1_2(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-length-1.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-length-1-2.xml",
        class_name="NistschemaSvIvListNmtokenLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_length_nistxml_sv_iv_list_nmtoken_length_1_3(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-length-1.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-length-1-3.xml",
        class_name="NistschemaSvIvListNmtokenLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_length_nistxml_sv_iv_list_nmtoken_length_1_4(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-length-1.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-length-1-4.xml",
        class_name="NistschemaSvIvListNmtokenLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_length_nistxml_sv_iv_list_nmtoken_length_1_5(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-length-1.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-length-1-5.xml",
        class_name="NistschemaSvIvListNmtokenLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_min_length_4_nistxml_sv_iv_list_nmtoken_min_length_5_1(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-minLength-5.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-minLength-5-1.xml",
        class_name="NistschemaSvIvListNmtokenMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_min_length_4_nistxml_sv_iv_list_nmtoken_min_length_5_2(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-minLength-5.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-minLength-5-2.xml",
        class_name="NistschemaSvIvListNmtokenMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_min_length_4_nistxml_sv_iv_list_nmtoken_min_length_5_3(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-minLength-5.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-minLength-5-3.xml",
        class_name="NistschemaSvIvListNmtokenMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_min_length_4_nistxml_sv_iv_list_nmtoken_min_length_5_4(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-minLength-5.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-minLength-5-4.xml",
        class_name="NistschemaSvIvListNmtokenMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_min_length_4_nistxml_sv_iv_list_nmtoken_min_length_5_5(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-minLength-5.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-minLength-5-5.xml",
        class_name="NistschemaSvIvListNmtokenMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_min_length_3_nistxml_sv_iv_list_nmtoken_min_length_4_1(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-minLength-4.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-minLength-4-1.xml",
        class_name="NistschemaSvIvListNmtokenMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_min_length_3_nistxml_sv_iv_list_nmtoken_min_length_4_2(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-minLength-4.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-minLength-4-2.xml",
        class_name="NistschemaSvIvListNmtokenMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_min_length_3_nistxml_sv_iv_list_nmtoken_min_length_4_3(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-minLength-4.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-minLength-4-3.xml",
        class_name="NistschemaSvIvListNmtokenMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_min_length_3_nistxml_sv_iv_list_nmtoken_min_length_4_4(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-minLength-4.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-minLength-4-4.xml",
        class_name="NistschemaSvIvListNmtokenMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_min_length_3_nistxml_sv_iv_list_nmtoken_min_length_4_5(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-minLength-4.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-minLength-4-5.xml",
        class_name="NistschemaSvIvListNmtokenMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_min_length_2_nistxml_sv_iv_list_nmtoken_min_length_3_1(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-minLength-3.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-minLength-3-1.xml",
        class_name="NistschemaSvIvListNmtokenMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_min_length_2_nistxml_sv_iv_list_nmtoken_min_length_3_2(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-minLength-3.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-minLength-3-2.xml",
        class_name="NistschemaSvIvListNmtokenMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_min_length_2_nistxml_sv_iv_list_nmtoken_min_length_3_3(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-minLength-3.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-minLength-3-3.xml",
        class_name="NistschemaSvIvListNmtokenMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_min_length_2_nistxml_sv_iv_list_nmtoken_min_length_3_4(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-minLength-3.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-minLength-3-4.xml",
        class_name="NistschemaSvIvListNmtokenMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_min_length_2_nistxml_sv_iv_list_nmtoken_min_length_3_5(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-minLength-3.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-minLength-3-5.xml",
        class_name="NistschemaSvIvListNmtokenMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_min_length_1_nistxml_sv_iv_list_nmtoken_min_length_2_1(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-minLength-2.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-minLength-2-1.xml",
        class_name="NistschemaSvIvListNmtokenMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_min_length_1_nistxml_sv_iv_list_nmtoken_min_length_2_2(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-minLength-2.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-minLength-2-2.xml",
        class_name="NistschemaSvIvListNmtokenMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_min_length_1_nistxml_sv_iv_list_nmtoken_min_length_2_3(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-minLength-2.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-minLength-2-3.xml",
        class_name="NistschemaSvIvListNmtokenMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_min_length_1_nistxml_sv_iv_list_nmtoken_min_length_2_4(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-minLength-2.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-minLength-2-4.xml",
        class_name="NistschemaSvIvListNmtokenMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_min_length_1_nistxml_sv_iv_list_nmtoken_min_length_2_5(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-minLength-2.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-minLength-2-5.xml",
        class_name="NistschemaSvIvListNmtokenMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_min_length_nistxml_sv_iv_list_nmtoken_min_length_1_1(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-minLength-1.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-minLength-1-1.xml",
        class_name="NistschemaSvIvListNmtokenMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_min_length_nistxml_sv_iv_list_nmtoken_min_length_1_2(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-minLength-1.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-minLength-1-2.xml",
        class_name="NistschemaSvIvListNmtokenMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_min_length_nistxml_sv_iv_list_nmtoken_min_length_1_3(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-minLength-1.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-minLength-1-3.xml",
        class_name="NistschemaSvIvListNmtokenMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_min_length_nistxml_sv_iv_list_nmtoken_min_length_1_4(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-minLength-1.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-minLength-1-4.xml",
        class_name="NistschemaSvIvListNmtokenMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_min_length_nistxml_sv_iv_list_nmtoken_min_length_1_5(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-minLength-1.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-minLength-1-5.xml",
        class_name="NistschemaSvIvListNmtokenMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_max_length_4_nistxml_sv_iv_list_nmtoken_max_length_5_1(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-maxLength-5.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-maxLength-5-1.xml",
        class_name="NistschemaSvIvListNmtokenMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_max_length_4_nistxml_sv_iv_list_nmtoken_max_length_5_2(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-maxLength-5.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-maxLength-5-2.xml",
        class_name="NistschemaSvIvListNmtokenMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_max_length_4_nistxml_sv_iv_list_nmtoken_max_length_5_3(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-maxLength-5.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-maxLength-5-3.xml",
        class_name="NistschemaSvIvListNmtokenMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_max_length_4_nistxml_sv_iv_list_nmtoken_max_length_5_4(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-maxLength-5.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-maxLength-5-4.xml",
        class_name="NistschemaSvIvListNmtokenMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_max_length_4_nistxml_sv_iv_list_nmtoken_max_length_5_5(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-maxLength-5.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-maxLength-5-5.xml",
        class_name="NistschemaSvIvListNmtokenMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_max_length_3_nistxml_sv_iv_list_nmtoken_max_length_4_1(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-maxLength-4.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-maxLength-4-1.xml",
        class_name="NistschemaSvIvListNmtokenMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_max_length_3_nistxml_sv_iv_list_nmtoken_max_length_4_2(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-maxLength-4.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-maxLength-4-2.xml",
        class_name="NistschemaSvIvListNmtokenMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_max_length_3_nistxml_sv_iv_list_nmtoken_max_length_4_3(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-maxLength-4.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-maxLength-4-3.xml",
        class_name="NistschemaSvIvListNmtokenMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_max_length_3_nistxml_sv_iv_list_nmtoken_max_length_4_4(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-maxLength-4.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-maxLength-4-4.xml",
        class_name="NistschemaSvIvListNmtokenMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_max_length_3_nistxml_sv_iv_list_nmtoken_max_length_4_5(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-maxLength-4.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-maxLength-4-5.xml",
        class_name="NistschemaSvIvListNmtokenMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_max_length_2_nistxml_sv_iv_list_nmtoken_max_length_3_1(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-maxLength-3.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-maxLength-3-1.xml",
        class_name="NistschemaSvIvListNmtokenMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_max_length_2_nistxml_sv_iv_list_nmtoken_max_length_3_2(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-maxLength-3.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-maxLength-3-2.xml",
        class_name="NistschemaSvIvListNmtokenMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_max_length_2_nistxml_sv_iv_list_nmtoken_max_length_3_3(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-maxLength-3.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-maxLength-3-3.xml",
        class_name="NistschemaSvIvListNmtokenMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_max_length_2_nistxml_sv_iv_list_nmtoken_max_length_3_4(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-maxLength-3.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-maxLength-3-4.xml",
        class_name="NistschemaSvIvListNmtokenMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_max_length_2_nistxml_sv_iv_list_nmtoken_max_length_3_5(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-maxLength-3.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-maxLength-3-5.xml",
        class_name="NistschemaSvIvListNmtokenMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_max_length_1_nistxml_sv_iv_list_nmtoken_max_length_2_1(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-maxLength-2.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-maxLength-2-1.xml",
        class_name="NistschemaSvIvListNmtokenMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_max_length_1_nistxml_sv_iv_list_nmtoken_max_length_2_2(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-maxLength-2.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-maxLength-2-2.xml",
        class_name="NistschemaSvIvListNmtokenMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_max_length_1_nistxml_sv_iv_list_nmtoken_max_length_2_3(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-maxLength-2.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-maxLength-2-3.xml",
        class_name="NistschemaSvIvListNmtokenMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_max_length_1_nistxml_sv_iv_list_nmtoken_max_length_2_4(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-maxLength-2.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-maxLength-2-4.xml",
        class_name="NistschemaSvIvListNmtokenMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_max_length_1_nistxml_sv_iv_list_nmtoken_max_length_2_5(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-maxLength-2.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-maxLength-2-5.xml",
        class_name="NistschemaSvIvListNmtokenMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_max_length_nistxml_sv_iv_list_nmtoken_max_length_1_1(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-maxLength-1.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-maxLength-1-1.xml",
        class_name="NistschemaSvIvListNmtokenMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_max_length_nistxml_sv_iv_list_nmtoken_max_length_1_2(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-maxLength-1.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-maxLength-1-2.xml",
        class_name="NistschemaSvIvListNmtokenMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_max_length_nistxml_sv_iv_list_nmtoken_max_length_1_3(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-maxLength-1.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-maxLength-1-3.xml",
        class_name="NistschemaSvIvListNmtokenMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_max_length_nistxml_sv_iv_list_nmtoken_max_length_1_4(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-maxLength-1.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-maxLength-1-4.xml",
        class_name="NistschemaSvIvListNmtokenMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_nmtoken_max_length_nistxml_sv_iv_list_nmtoken_max_length_1_5(mode, save_output, output_format):
    """
    Type list/NMTOKEN is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/NMTOKEN/Schema+Instance/NISTSchema-SV-IV-list-NMTOKEN-maxLength-1.xsd",
        instance="nistData/list/NMTOKEN/Schema+Instance/NISTXML-SV-IV-list-NMTOKEN-maxLength-1-5.xml",
        class_name="NistschemaSvIvListNmtokenMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_white_space_nistxml_sv_iv_list_name_white_space_1_1(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet whiteSpace with value collapse.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-whiteSpace-1.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-whiteSpace-1-1.xml",
        class_name="NistschemaSvIvListNameWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_white_space_nistxml_sv_iv_list_name_white_space_1_2(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet whiteSpace with value collapse.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-whiteSpace-1.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-whiteSpace-1-2.xml",
        class_name="NistschemaSvIvListNameWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_white_space_nistxml_sv_iv_list_name_white_space_1_3(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet whiteSpace with value collapse.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-whiteSpace-1.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-whiteSpace-1-3.xml",
        class_name="NistschemaSvIvListNameWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_white_space_nistxml_sv_iv_list_name_white_space_1_4(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet whiteSpace with value collapse.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-whiteSpace-1.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-whiteSpace-1-4.xml",
        class_name="NistschemaSvIvListNameWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_white_space_nistxml_sv_iv_list_name_white_space_1_5(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet whiteSpace with value collapse.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-whiteSpace-1.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-whiteSpace-1-5.xml",
        class_name="NistschemaSvIvListNameWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_enumeration_4_nistxml_sv_iv_list_name_enumeration_5_1(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-enumeration-5.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-enumeration-5-1.xml",
        class_name="NistschemaSvIvListNameEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_enumeration_4_nistxml_sv_iv_list_name_enumeration_5_2(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-enumeration-5.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-enumeration-5-2.xml",
        class_name="NistschemaSvIvListNameEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_enumeration_4_nistxml_sv_iv_list_name_enumeration_5_3(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-enumeration-5.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-enumeration-5-3.xml",
        class_name="NistschemaSvIvListNameEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_enumeration_4_nistxml_sv_iv_list_name_enumeration_5_4(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-enumeration-5.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-enumeration-5-4.xml",
        class_name="NistschemaSvIvListNameEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_enumeration_4_nistxml_sv_iv_list_name_enumeration_5_5(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-enumeration-5.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-enumeration-5-5.xml",
        class_name="NistschemaSvIvListNameEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_enumeration_3_nistxml_sv_iv_list_name_enumeration_4_1(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-enumeration-4.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-enumeration-4-1.xml",
        class_name="NistschemaSvIvListNameEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_enumeration_3_nistxml_sv_iv_list_name_enumeration_4_2(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-enumeration-4.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-enumeration-4-2.xml",
        class_name="NistschemaSvIvListNameEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_enumeration_3_nistxml_sv_iv_list_name_enumeration_4_3(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-enumeration-4.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-enumeration-4-3.xml",
        class_name="NistschemaSvIvListNameEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_enumeration_3_nistxml_sv_iv_list_name_enumeration_4_4(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-enumeration-4.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-enumeration-4-4.xml",
        class_name="NistschemaSvIvListNameEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_enumeration_3_nistxml_sv_iv_list_name_enumeration_4_5(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-enumeration-4.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-enumeration-4-5.xml",
        class_name="NistschemaSvIvListNameEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_enumeration_2_nistxml_sv_iv_list_name_enumeration_3_1(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-enumeration-3.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-enumeration-3-1.xml",
        class_name="NistschemaSvIvListNameEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_enumeration_2_nistxml_sv_iv_list_name_enumeration_3_2(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-enumeration-3.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-enumeration-3-2.xml",
        class_name="NistschemaSvIvListNameEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_enumeration_2_nistxml_sv_iv_list_name_enumeration_3_3(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-enumeration-3.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-enumeration-3-3.xml",
        class_name="NistschemaSvIvListNameEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_enumeration_2_nistxml_sv_iv_list_name_enumeration_3_4(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-enumeration-3.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-enumeration-3-4.xml",
        class_name="NistschemaSvIvListNameEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_enumeration_2_nistxml_sv_iv_list_name_enumeration_3_5(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-enumeration-3.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-enumeration-3-5.xml",
        class_name="NistschemaSvIvListNameEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_enumeration_1_nistxml_sv_iv_list_name_enumeration_2_1(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-enumeration-2.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-enumeration-2-1.xml",
        class_name="NistschemaSvIvListNameEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_enumeration_1_nistxml_sv_iv_list_name_enumeration_2_2(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-enumeration-2.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-enumeration-2-2.xml",
        class_name="NistschemaSvIvListNameEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_enumeration_1_nistxml_sv_iv_list_name_enumeration_2_3(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-enumeration-2.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-enumeration-2-3.xml",
        class_name="NistschemaSvIvListNameEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_enumeration_1_nistxml_sv_iv_list_name_enumeration_2_4(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-enumeration-2.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-enumeration-2-4.xml",
        class_name="NistschemaSvIvListNameEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_enumeration_1_nistxml_sv_iv_list_name_enumeration_2_5(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-enumeration-2.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-enumeration-2-5.xml",
        class_name="NistschemaSvIvListNameEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_enumeration_nistxml_sv_iv_list_name_enumeration_1_1(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-enumeration-1.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-enumeration-1-1.xml",
        class_name="NistschemaSvIvListNameEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_enumeration_nistxml_sv_iv_list_name_enumeration_1_2(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-enumeration-1.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-enumeration-1-2.xml",
        class_name="NistschemaSvIvListNameEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_enumeration_nistxml_sv_iv_list_name_enumeration_1_3(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-enumeration-1.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-enumeration-1-3.xml",
        class_name="NistschemaSvIvListNameEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_enumeration_nistxml_sv_iv_list_name_enumeration_1_4(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-enumeration-1.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-enumeration-1-4.xml",
        class_name="NistschemaSvIvListNameEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_enumeration_nistxml_sv_iv_list_name_enumeration_1_5(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-enumeration-1.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-enumeration-1-5.xml",
        class_name="NistschemaSvIvListNameEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_pattern_4_nistxml_sv_iv_list_name_pattern_5_1(mode, save_output, output_format):
    r"""
    Type list/Name is restricted by facet pattern with value \i\c{21}
    \i\c{22} \i\c{35} \i\c{25} \i\c{26} \i\c{12} \i\c{48} \i\c{33}
    \i\c{44} \i\c{57}.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-pattern-5.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-pattern-5-1.xml",
        class_name="NistschemaSvIvListNamePattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_pattern_4_nistxml_sv_iv_list_name_pattern_5_2(mode, save_output, output_format):
    r"""
    Type list/Name is restricted by facet pattern with value \i\c{21}
    \i\c{22} \i\c{35} \i\c{25} \i\c{26} \i\c{12} \i\c{48} \i\c{33}
    \i\c{44} \i\c{57}.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-pattern-5.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-pattern-5-2.xml",
        class_name="NistschemaSvIvListNamePattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_pattern_4_nistxml_sv_iv_list_name_pattern_5_3(mode, save_output, output_format):
    r"""
    Type list/Name is restricted by facet pattern with value \i\c{21}
    \i\c{22} \i\c{35} \i\c{25} \i\c{26} \i\c{12} \i\c{48} \i\c{33}
    \i\c{44} \i\c{57}.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-pattern-5.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-pattern-5-3.xml",
        class_name="NistschemaSvIvListNamePattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_pattern_4_nistxml_sv_iv_list_name_pattern_5_4(mode, save_output, output_format):
    r"""
    Type list/Name is restricted by facet pattern with value \i\c{21}
    \i\c{22} \i\c{35} \i\c{25} \i\c{26} \i\c{12} \i\c{48} \i\c{33}
    \i\c{44} \i\c{57}.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-pattern-5.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-pattern-5-4.xml",
        class_name="NistschemaSvIvListNamePattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_pattern_4_nistxml_sv_iv_list_name_pattern_5_5(mode, save_output, output_format):
    r"""
    Type list/Name is restricted by facet pattern with value \i\c{21}
    \i\c{22} \i\c{35} \i\c{25} \i\c{26} \i\c{12} \i\c{48} \i\c{33}
    \i\c{44} \i\c{57}.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-pattern-5.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-pattern-5-5.xml",
        class_name="NistschemaSvIvListNamePattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_pattern_3_nistxml_sv_iv_list_name_pattern_4_1(mode, save_output, output_format):
    r"""
    Type list/Name is restricted by facet pattern with value \i\c{19}
    \i\c{63} \i\c{18} \i\c{40} \i\c{12} \i\c{58} \i\c{47} \i\c{54}
    \i\c{15}.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-pattern-4.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-pattern-4-1.xml",
        class_name="NistschemaSvIvListNamePattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_pattern_3_nistxml_sv_iv_list_name_pattern_4_2(mode, save_output, output_format):
    r"""
    Type list/Name is restricted by facet pattern with value \i\c{19}
    \i\c{63} \i\c{18} \i\c{40} \i\c{12} \i\c{58} \i\c{47} \i\c{54}
    \i\c{15}.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-pattern-4.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-pattern-4-2.xml",
        class_name="NistschemaSvIvListNamePattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_pattern_3_nistxml_sv_iv_list_name_pattern_4_3(mode, save_output, output_format):
    r"""
    Type list/Name is restricted by facet pattern with value \i\c{19}
    \i\c{63} \i\c{18} \i\c{40} \i\c{12} \i\c{58} \i\c{47} \i\c{54}
    \i\c{15}.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-pattern-4.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-pattern-4-3.xml",
        class_name="NistschemaSvIvListNamePattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_pattern_3_nistxml_sv_iv_list_name_pattern_4_4(mode, save_output, output_format):
    r"""
    Type list/Name is restricted by facet pattern with value \i\c{19}
    \i\c{63} \i\c{18} \i\c{40} \i\c{12} \i\c{58} \i\c{47} \i\c{54}
    \i\c{15}.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-pattern-4.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-pattern-4-4.xml",
        class_name="NistschemaSvIvListNamePattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_pattern_3_nistxml_sv_iv_list_name_pattern_4_5(mode, save_output, output_format):
    r"""
    Type list/Name is restricted by facet pattern with value \i\c{19}
    \i\c{63} \i\c{18} \i\c{40} \i\c{12} \i\c{58} \i\c{47} \i\c{54}
    \i\c{15}.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-pattern-4.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-pattern-4-5.xml",
        class_name="NistschemaSvIvListNamePattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_pattern_2_nistxml_sv_iv_list_name_pattern_3_1(mode, save_output, output_format):
    r"""
    Type list/Name is restricted by facet pattern with value \i\c{24}
    \i\c{23} \i\c{57} \i\c{50} \i\c{52} \i\c{35} \i\c{28}.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-pattern-3.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-pattern-3-1.xml",
        class_name="NistschemaSvIvListNamePattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_pattern_2_nistxml_sv_iv_list_name_pattern_3_2(mode, save_output, output_format):
    r"""
    Type list/Name is restricted by facet pattern with value \i\c{24}
    \i\c{23} \i\c{57} \i\c{50} \i\c{52} \i\c{35} \i\c{28}.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-pattern-3.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-pattern-3-2.xml",
        class_name="NistschemaSvIvListNamePattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_pattern_2_nistxml_sv_iv_list_name_pattern_3_3(mode, save_output, output_format):
    r"""
    Type list/Name is restricted by facet pattern with value \i\c{24}
    \i\c{23} \i\c{57} \i\c{50} \i\c{52} \i\c{35} \i\c{28}.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-pattern-3.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-pattern-3-3.xml",
        class_name="NistschemaSvIvListNamePattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_pattern_2_nistxml_sv_iv_list_name_pattern_3_4(mode, save_output, output_format):
    r"""
    Type list/Name is restricted by facet pattern with value \i\c{24}
    \i\c{23} \i\c{57} \i\c{50} \i\c{52} \i\c{35} \i\c{28}.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-pattern-3.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-pattern-3-4.xml",
        class_name="NistschemaSvIvListNamePattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_pattern_2_nistxml_sv_iv_list_name_pattern_3_5(mode, save_output, output_format):
    r"""
    Type list/Name is restricted by facet pattern with value \i\c{24}
    \i\c{23} \i\c{57} \i\c{50} \i\c{52} \i\c{35} \i\c{28}.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-pattern-3.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-pattern-3-5.xml",
        class_name="NistschemaSvIvListNamePattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_pattern_1_nistxml_sv_iv_list_name_pattern_2_1(mode, save_output, output_format):
    r"""
    Type list/Name is restricted by facet pattern with value \i\c{33}
    \i\c{52} \i\c{56} \i\c{6} \i\c{22}.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-pattern-2.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-pattern-2-1.xml",
        class_name="NistschemaSvIvListNamePattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_pattern_1_nistxml_sv_iv_list_name_pattern_2_2(mode, save_output, output_format):
    r"""
    Type list/Name is restricted by facet pattern with value \i\c{33}
    \i\c{52} \i\c{56} \i\c{6} \i\c{22}.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-pattern-2.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-pattern-2-2.xml",
        class_name="NistschemaSvIvListNamePattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_pattern_1_nistxml_sv_iv_list_name_pattern_2_3(mode, save_output, output_format):
    r"""
    Type list/Name is restricted by facet pattern with value \i\c{33}
    \i\c{52} \i\c{56} \i\c{6} \i\c{22}.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-pattern-2.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-pattern-2-3.xml",
        class_name="NistschemaSvIvListNamePattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_pattern_1_nistxml_sv_iv_list_name_pattern_2_4(mode, save_output, output_format):
    r"""
    Type list/Name is restricted by facet pattern with value \i\c{33}
    \i\c{52} \i\c{56} \i\c{6} \i\c{22}.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-pattern-2.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-pattern-2-4.xml",
        class_name="NistschemaSvIvListNamePattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_pattern_1_nistxml_sv_iv_list_name_pattern_2_5(mode, save_output, output_format):
    r"""
    Type list/Name is restricted by facet pattern with value \i\c{33}
    \i\c{52} \i\c{56} \i\c{6} \i\c{22}.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-pattern-2.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-pattern-2-5.xml",
        class_name="NistschemaSvIvListNamePattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_pattern_nistxml_sv_iv_list_name_pattern_1_1(mode, save_output, output_format):
    r"""
    Type list/Name is restricted by facet pattern with value \i\c{48}
    \i\c{47} \i\c{13} \i\c{4} \i\c{46} \i\c{37}.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-pattern-1.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-pattern-1-1.xml",
        class_name="NistschemaSvIvListNamePattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_pattern_nistxml_sv_iv_list_name_pattern_1_2(mode, save_output, output_format):
    r"""
    Type list/Name is restricted by facet pattern with value \i\c{48}
    \i\c{47} \i\c{13} \i\c{4} \i\c{46} \i\c{37}.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-pattern-1.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-pattern-1-2.xml",
        class_name="NistschemaSvIvListNamePattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_pattern_nistxml_sv_iv_list_name_pattern_1_3(mode, save_output, output_format):
    r"""
    Type list/Name is restricted by facet pattern with value \i\c{48}
    \i\c{47} \i\c{13} \i\c{4} \i\c{46} \i\c{37}.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-pattern-1.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-pattern-1-3.xml",
        class_name="NistschemaSvIvListNamePattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_pattern_nistxml_sv_iv_list_name_pattern_1_4(mode, save_output, output_format):
    r"""
    Type list/Name is restricted by facet pattern with value \i\c{48}
    \i\c{47} \i\c{13} \i\c{4} \i\c{46} \i\c{37}.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-pattern-1.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-pattern-1-4.xml",
        class_name="NistschemaSvIvListNamePattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_pattern_nistxml_sv_iv_list_name_pattern_1_5(mode, save_output, output_format):
    r"""
    Type list/Name is restricted by facet pattern with value \i\c{48}
    \i\c{47} \i\c{13} \i\c{4} \i\c{46} \i\c{37}.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-pattern-1.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-pattern-1-5.xml",
        class_name="NistschemaSvIvListNamePattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_length_4_nistxml_sv_iv_list_name_length_5_1(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-length-5.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-length-5-1.xml",
        class_name="NistschemaSvIvListNameLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_length_4_nistxml_sv_iv_list_name_length_5_2(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-length-5.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-length-5-2.xml",
        class_name="NistschemaSvIvListNameLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_length_4_nistxml_sv_iv_list_name_length_5_3(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-length-5.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-length-5-3.xml",
        class_name="NistschemaSvIvListNameLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_length_4_nistxml_sv_iv_list_name_length_5_4(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-length-5.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-length-5-4.xml",
        class_name="NistschemaSvIvListNameLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_length_4_nistxml_sv_iv_list_name_length_5_5(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-length-5.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-length-5-5.xml",
        class_name="NistschemaSvIvListNameLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_length_3_nistxml_sv_iv_list_name_length_4_1(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-length-4.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-length-4-1.xml",
        class_name="NistschemaSvIvListNameLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_length_3_nistxml_sv_iv_list_name_length_4_2(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-length-4.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-length-4-2.xml",
        class_name="NistschemaSvIvListNameLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_length_3_nistxml_sv_iv_list_name_length_4_3(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-length-4.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-length-4-3.xml",
        class_name="NistschemaSvIvListNameLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_length_3_nistxml_sv_iv_list_name_length_4_4(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-length-4.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-length-4-4.xml",
        class_name="NistschemaSvIvListNameLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_length_3_nistxml_sv_iv_list_name_length_4_5(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-length-4.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-length-4-5.xml",
        class_name="NistschemaSvIvListNameLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_length_2_nistxml_sv_iv_list_name_length_3_1(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-length-3.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-length-3-1.xml",
        class_name="NistschemaSvIvListNameLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_length_2_nistxml_sv_iv_list_name_length_3_2(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-length-3.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-length-3-2.xml",
        class_name="NistschemaSvIvListNameLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_length_2_nistxml_sv_iv_list_name_length_3_3(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-length-3.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-length-3-3.xml",
        class_name="NistschemaSvIvListNameLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_length_2_nistxml_sv_iv_list_name_length_3_4(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-length-3.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-length-3-4.xml",
        class_name="NistschemaSvIvListNameLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_length_2_nistxml_sv_iv_list_name_length_3_5(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-length-3.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-length-3-5.xml",
        class_name="NistschemaSvIvListNameLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_length_1_nistxml_sv_iv_list_name_length_2_1(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-length-2.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-length-2-1.xml",
        class_name="NistschemaSvIvListNameLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_length_1_nistxml_sv_iv_list_name_length_2_2(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-length-2.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-length-2-2.xml",
        class_name="NistschemaSvIvListNameLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_length_1_nistxml_sv_iv_list_name_length_2_3(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-length-2.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-length-2-3.xml",
        class_name="NistschemaSvIvListNameLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_length_1_nistxml_sv_iv_list_name_length_2_4(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-length-2.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-length-2-4.xml",
        class_name="NistschemaSvIvListNameLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_length_1_nistxml_sv_iv_list_name_length_2_5(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-length-2.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-length-2-5.xml",
        class_name="NistschemaSvIvListNameLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_length_nistxml_sv_iv_list_name_length_1_1(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-length-1.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-length-1-1.xml",
        class_name="NistschemaSvIvListNameLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_length_nistxml_sv_iv_list_name_length_1_2(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-length-1.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-length-1-2.xml",
        class_name="NistschemaSvIvListNameLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_length_nistxml_sv_iv_list_name_length_1_3(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-length-1.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-length-1-3.xml",
        class_name="NistschemaSvIvListNameLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_length_nistxml_sv_iv_list_name_length_1_4(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-length-1.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-length-1-4.xml",
        class_name="NistschemaSvIvListNameLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_length_nistxml_sv_iv_list_name_length_1_5(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-length-1.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-length-1-5.xml",
        class_name="NistschemaSvIvListNameLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_min_length_4_nistxml_sv_iv_list_name_min_length_5_1(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-minLength-5.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-minLength-5-1.xml",
        class_name="NistschemaSvIvListNameMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_min_length_4_nistxml_sv_iv_list_name_min_length_5_2(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-minLength-5.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-minLength-5-2.xml",
        class_name="NistschemaSvIvListNameMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_min_length_4_nistxml_sv_iv_list_name_min_length_5_3(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-minLength-5.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-minLength-5-3.xml",
        class_name="NistschemaSvIvListNameMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_min_length_4_nistxml_sv_iv_list_name_min_length_5_4(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-minLength-5.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-minLength-5-4.xml",
        class_name="NistschemaSvIvListNameMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_min_length_4_nistxml_sv_iv_list_name_min_length_5_5(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-minLength-5.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-minLength-5-5.xml",
        class_name="NistschemaSvIvListNameMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_min_length_3_nistxml_sv_iv_list_name_min_length_4_1(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-minLength-4.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-minLength-4-1.xml",
        class_name="NistschemaSvIvListNameMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_min_length_3_nistxml_sv_iv_list_name_min_length_4_2(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-minLength-4.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-minLength-4-2.xml",
        class_name="NistschemaSvIvListNameMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_min_length_3_nistxml_sv_iv_list_name_min_length_4_3(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-minLength-4.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-minLength-4-3.xml",
        class_name="NistschemaSvIvListNameMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_min_length_3_nistxml_sv_iv_list_name_min_length_4_4(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-minLength-4.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-minLength-4-4.xml",
        class_name="NistschemaSvIvListNameMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_min_length_3_nistxml_sv_iv_list_name_min_length_4_5(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-minLength-4.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-minLength-4-5.xml",
        class_name="NistschemaSvIvListNameMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_min_length_2_nistxml_sv_iv_list_name_min_length_3_1(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-minLength-3.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-minLength-3-1.xml",
        class_name="NistschemaSvIvListNameMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_min_length_2_nistxml_sv_iv_list_name_min_length_3_2(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-minLength-3.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-minLength-3-2.xml",
        class_name="NistschemaSvIvListNameMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_min_length_2_nistxml_sv_iv_list_name_min_length_3_3(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-minLength-3.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-minLength-3-3.xml",
        class_name="NistschemaSvIvListNameMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_min_length_2_nistxml_sv_iv_list_name_min_length_3_4(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-minLength-3.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-minLength-3-4.xml",
        class_name="NistschemaSvIvListNameMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_min_length_2_nistxml_sv_iv_list_name_min_length_3_5(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-minLength-3.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-minLength-3-5.xml",
        class_name="NistschemaSvIvListNameMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_min_length_1_nistxml_sv_iv_list_name_min_length_2_1(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-minLength-2.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-minLength-2-1.xml",
        class_name="NistschemaSvIvListNameMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_min_length_1_nistxml_sv_iv_list_name_min_length_2_2(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-minLength-2.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-minLength-2-2.xml",
        class_name="NistschemaSvIvListNameMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_min_length_1_nistxml_sv_iv_list_name_min_length_2_3(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-minLength-2.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-minLength-2-3.xml",
        class_name="NistschemaSvIvListNameMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_min_length_1_nistxml_sv_iv_list_name_min_length_2_4(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-minLength-2.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-minLength-2-4.xml",
        class_name="NistschemaSvIvListNameMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_min_length_1_nistxml_sv_iv_list_name_min_length_2_5(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-minLength-2.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-minLength-2-5.xml",
        class_name="NistschemaSvIvListNameMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_min_length_nistxml_sv_iv_list_name_min_length_1_1(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-minLength-1.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-minLength-1-1.xml",
        class_name="NistschemaSvIvListNameMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_min_length_nistxml_sv_iv_list_name_min_length_1_2(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-minLength-1.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-minLength-1-2.xml",
        class_name="NistschemaSvIvListNameMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_min_length_nistxml_sv_iv_list_name_min_length_1_3(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-minLength-1.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-minLength-1-3.xml",
        class_name="NistschemaSvIvListNameMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_min_length_nistxml_sv_iv_list_name_min_length_1_4(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-minLength-1.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-minLength-1-4.xml",
        class_name="NistschemaSvIvListNameMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_min_length_nistxml_sv_iv_list_name_min_length_1_5(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-minLength-1.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-minLength-1-5.xml",
        class_name="NistschemaSvIvListNameMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_max_length_4_nistxml_sv_iv_list_name_max_length_5_1(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-maxLength-5.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-maxLength-5-1.xml",
        class_name="NistschemaSvIvListNameMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_max_length_4_nistxml_sv_iv_list_name_max_length_5_2(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-maxLength-5.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-maxLength-5-2.xml",
        class_name="NistschemaSvIvListNameMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_max_length_4_nistxml_sv_iv_list_name_max_length_5_3(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-maxLength-5.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-maxLength-5-3.xml",
        class_name="NistschemaSvIvListNameMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_max_length_4_nistxml_sv_iv_list_name_max_length_5_4(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-maxLength-5.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-maxLength-5-4.xml",
        class_name="NistschemaSvIvListNameMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_max_length_4_nistxml_sv_iv_list_name_max_length_5_5(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-maxLength-5.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-maxLength-5-5.xml",
        class_name="NistschemaSvIvListNameMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_max_length_3_nistxml_sv_iv_list_name_max_length_4_1(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-maxLength-4.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-maxLength-4-1.xml",
        class_name="NistschemaSvIvListNameMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_max_length_3_nistxml_sv_iv_list_name_max_length_4_2(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-maxLength-4.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-maxLength-4-2.xml",
        class_name="NistschemaSvIvListNameMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_max_length_3_nistxml_sv_iv_list_name_max_length_4_3(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-maxLength-4.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-maxLength-4-3.xml",
        class_name="NistschemaSvIvListNameMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_max_length_3_nistxml_sv_iv_list_name_max_length_4_4(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-maxLength-4.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-maxLength-4-4.xml",
        class_name="NistschemaSvIvListNameMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_max_length_3_nistxml_sv_iv_list_name_max_length_4_5(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-maxLength-4.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-maxLength-4-5.xml",
        class_name="NistschemaSvIvListNameMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_max_length_2_nistxml_sv_iv_list_name_max_length_3_1(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-maxLength-3.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-maxLength-3-1.xml",
        class_name="NistschemaSvIvListNameMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_max_length_2_nistxml_sv_iv_list_name_max_length_3_2(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-maxLength-3.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-maxLength-3-2.xml",
        class_name="NistschemaSvIvListNameMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_max_length_2_nistxml_sv_iv_list_name_max_length_3_3(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-maxLength-3.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-maxLength-3-3.xml",
        class_name="NistschemaSvIvListNameMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_max_length_2_nistxml_sv_iv_list_name_max_length_3_4(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-maxLength-3.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-maxLength-3-4.xml",
        class_name="NistschemaSvIvListNameMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_max_length_2_nistxml_sv_iv_list_name_max_length_3_5(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-maxLength-3.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-maxLength-3-5.xml",
        class_name="NistschemaSvIvListNameMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_max_length_1_nistxml_sv_iv_list_name_max_length_2_1(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-maxLength-2.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-maxLength-2-1.xml",
        class_name="NistschemaSvIvListNameMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_max_length_1_nistxml_sv_iv_list_name_max_length_2_2(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-maxLength-2.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-maxLength-2-2.xml",
        class_name="NistschemaSvIvListNameMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_max_length_1_nistxml_sv_iv_list_name_max_length_2_3(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-maxLength-2.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-maxLength-2-3.xml",
        class_name="NistschemaSvIvListNameMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_max_length_1_nistxml_sv_iv_list_name_max_length_2_4(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-maxLength-2.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-maxLength-2-4.xml",
        class_name="NistschemaSvIvListNameMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_max_length_1_nistxml_sv_iv_list_name_max_length_2_5(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-maxLength-2.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-maxLength-2-5.xml",
        class_name="NistschemaSvIvListNameMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_max_length_nistxml_sv_iv_list_name_max_length_1_1(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-maxLength-1.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-maxLength-1-1.xml",
        class_name="NistschemaSvIvListNameMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_max_length_nistxml_sv_iv_list_name_max_length_1_2(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-maxLength-1.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-maxLength-1-2.xml",
        class_name="NistschemaSvIvListNameMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_max_length_nistxml_sv_iv_list_name_max_length_1_3(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-maxLength-1.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-maxLength-1-3.xml",
        class_name="NistschemaSvIvListNameMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_max_length_nistxml_sv_iv_list_name_max_length_1_4(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-maxLength-1.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-maxLength-1-4.xml",
        class_name="NistschemaSvIvListNameMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_name_max_length_nistxml_sv_iv_list_name_max_length_1_5(mode, save_output, output_format):
    """
    Type list/Name is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/Name/Schema+Instance/NISTSchema-SV-IV-list-Name-maxLength-1.xsd",
        instance="nistData/list/Name/Schema+Instance/NISTXML-SV-IV-list-Name-maxLength-1-5.xml",
        class_name="NistschemaSvIvListNameMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_white_space_nistxml_sv_iv_list_token_white_space_1_1(mode, save_output, output_format):
    """
    Type list/token is restricted by facet whiteSpace with value collapse.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-whiteSpace-1.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-whiteSpace-1-1.xml",
        class_name="NistschemaSvIvListTokenWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_white_space_nistxml_sv_iv_list_token_white_space_1_2(mode, save_output, output_format):
    """
    Type list/token is restricted by facet whiteSpace with value collapse.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-whiteSpace-1.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-whiteSpace-1-2.xml",
        class_name="NistschemaSvIvListTokenWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_white_space_nistxml_sv_iv_list_token_white_space_1_3(mode, save_output, output_format):
    """
    Type list/token is restricted by facet whiteSpace with value collapse.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-whiteSpace-1.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-whiteSpace-1-3.xml",
        class_name="NistschemaSvIvListTokenWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_white_space_nistxml_sv_iv_list_token_white_space_1_4(mode, save_output, output_format):
    """
    Type list/token is restricted by facet whiteSpace with value collapse.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-whiteSpace-1.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-whiteSpace-1-4.xml",
        class_name="NistschemaSvIvListTokenWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_white_space_nistxml_sv_iv_list_token_white_space_1_5(mode, save_output, output_format):
    """
    Type list/token is restricted by facet whiteSpace with value collapse.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-whiteSpace-1.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-whiteSpace-1-5.xml",
        class_name="NistschemaSvIvListTokenWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_enumeration_4_nistxml_sv_iv_list_token_enumeration_5_1(mode, save_output, output_format):
    """
    Type list/token is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-enumeration-5.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-enumeration-5-1.xml",
        class_name="NistschemaSvIvListTokenEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_enumeration_4_nistxml_sv_iv_list_token_enumeration_5_2(mode, save_output, output_format):
    """
    Type list/token is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-enumeration-5.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-enumeration-5-2.xml",
        class_name="NistschemaSvIvListTokenEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_enumeration_4_nistxml_sv_iv_list_token_enumeration_5_3(mode, save_output, output_format):
    """
    Type list/token is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-enumeration-5.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-enumeration-5-3.xml",
        class_name="NistschemaSvIvListTokenEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_enumeration_4_nistxml_sv_iv_list_token_enumeration_5_4(mode, save_output, output_format):
    """
    Type list/token is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-enumeration-5.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-enumeration-5-4.xml",
        class_name="NistschemaSvIvListTokenEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_enumeration_4_nistxml_sv_iv_list_token_enumeration_5_5(mode, save_output, output_format):
    """
    Type list/token is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-enumeration-5.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-enumeration-5-5.xml",
        class_name="NistschemaSvIvListTokenEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_enumeration_3_nistxml_sv_iv_list_token_enumeration_4_1(mode, save_output, output_format):
    """
    Type list/token is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-enumeration-4.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-enumeration-4-1.xml",
        class_name="NistschemaSvIvListTokenEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_enumeration_3_nistxml_sv_iv_list_token_enumeration_4_2(mode, save_output, output_format):
    """
    Type list/token is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-enumeration-4.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-enumeration-4-2.xml",
        class_name="NistschemaSvIvListTokenEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_enumeration_3_nistxml_sv_iv_list_token_enumeration_4_3(mode, save_output, output_format):
    """
    Type list/token is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-enumeration-4.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-enumeration-4-3.xml",
        class_name="NistschemaSvIvListTokenEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_enumeration_3_nistxml_sv_iv_list_token_enumeration_4_4(mode, save_output, output_format):
    """
    Type list/token is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-enumeration-4.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-enumeration-4-4.xml",
        class_name="NistschemaSvIvListTokenEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_enumeration_3_nistxml_sv_iv_list_token_enumeration_4_5(mode, save_output, output_format):
    """
    Type list/token is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-enumeration-4.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-enumeration-4-5.xml",
        class_name="NistschemaSvIvListTokenEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_enumeration_2_nistxml_sv_iv_list_token_enumeration_3_1(mode, save_output, output_format):
    """
    Type list/token is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-enumeration-3.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-enumeration-3-1.xml",
        class_name="NistschemaSvIvListTokenEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_enumeration_2_nistxml_sv_iv_list_token_enumeration_3_2(mode, save_output, output_format):
    """
    Type list/token is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-enumeration-3.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-enumeration-3-2.xml",
        class_name="NistschemaSvIvListTokenEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_enumeration_2_nistxml_sv_iv_list_token_enumeration_3_3(mode, save_output, output_format):
    """
    Type list/token is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-enumeration-3.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-enumeration-3-3.xml",
        class_name="NistschemaSvIvListTokenEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_enumeration_2_nistxml_sv_iv_list_token_enumeration_3_4(mode, save_output, output_format):
    """
    Type list/token is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-enumeration-3.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-enumeration-3-4.xml",
        class_name="NistschemaSvIvListTokenEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_enumeration_2_nistxml_sv_iv_list_token_enumeration_3_5(mode, save_output, output_format):
    """
    Type list/token is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-enumeration-3.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-enumeration-3-5.xml",
        class_name="NistschemaSvIvListTokenEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_enumeration_1_nistxml_sv_iv_list_token_enumeration_2_1(mode, save_output, output_format):
    """
    Type list/token is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-enumeration-2.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-enumeration-2-1.xml",
        class_name="NistschemaSvIvListTokenEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_enumeration_1_nistxml_sv_iv_list_token_enumeration_2_2(mode, save_output, output_format):
    """
    Type list/token is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-enumeration-2.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-enumeration-2-2.xml",
        class_name="NistschemaSvIvListTokenEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_enumeration_1_nistxml_sv_iv_list_token_enumeration_2_3(mode, save_output, output_format):
    """
    Type list/token is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-enumeration-2.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-enumeration-2-3.xml",
        class_name="NistschemaSvIvListTokenEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_enumeration_1_nistxml_sv_iv_list_token_enumeration_2_4(mode, save_output, output_format):
    """
    Type list/token is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-enumeration-2.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-enumeration-2-4.xml",
        class_name="NistschemaSvIvListTokenEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_enumeration_1_nistxml_sv_iv_list_token_enumeration_2_5(mode, save_output, output_format):
    """
    Type list/token is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-enumeration-2.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-enumeration-2-5.xml",
        class_name="NistschemaSvIvListTokenEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_enumeration_nistxml_sv_iv_list_token_enumeration_1_1(mode, save_output, output_format):
    """
    Type list/token is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-enumeration-1.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-enumeration-1-1.xml",
        class_name="NistschemaSvIvListTokenEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_enumeration_nistxml_sv_iv_list_token_enumeration_1_2(mode, save_output, output_format):
    """
    Type list/token is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-enumeration-1.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-enumeration-1-2.xml",
        class_name="NistschemaSvIvListTokenEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_enumeration_nistxml_sv_iv_list_token_enumeration_1_3(mode, save_output, output_format):
    """
    Type list/token is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-enumeration-1.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-enumeration-1-3.xml",
        class_name="NistschemaSvIvListTokenEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_enumeration_nistxml_sv_iv_list_token_enumeration_1_4(mode, save_output, output_format):
    """
    Type list/token is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-enumeration-1.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-enumeration-1-4.xml",
        class_name="NistschemaSvIvListTokenEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_enumeration_nistxml_sv_iv_list_token_enumeration_1_5(mode, save_output, output_format):
    """
    Type list/token is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-enumeration-1.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-enumeration-1-5.xml",
        class_name="NistschemaSvIvListTokenEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_pattern_4_nistxml_sv_iv_list_token_pattern_5_1(mode, save_output, output_format):
    r"""
    Type list/token is restricted by facet pattern with value \d{1,5}_([A-
    Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_17988 \d{1,5
    }_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_14056-
    1024 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_10607 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_17619-1280 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_13978 \d{1,5}_([A
    -Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_18746 \d{1,
    5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_17171-1364 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-
    z]{1,20}_){1},_[A-Z]{2}_16881.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-pattern-5.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-pattern-5-1.xml",
        class_name="NistschemaSvIvListTokenPattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_pattern_4_nistxml_sv_iv_list_token_pattern_5_2(mode, save_output, output_format):
    r"""
    Type list/token is restricted by facet pattern with value \d{1,5}_([A-
    Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_17988 \d{1,5
    }_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_14056-
    1024 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_10607 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_17619-1280 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_13978 \d{1,5}_([A
    -Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_18746 \d{1,
    5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_17171-1364 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-
    z]{1,20}_){1},_[A-Z]{2}_16881.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-pattern-5.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-pattern-5-2.xml",
        class_name="NistschemaSvIvListTokenPattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_pattern_4_nistxml_sv_iv_list_token_pattern_5_3(mode, save_output, output_format):
    r"""
    Type list/token is restricted by facet pattern with value \d{1,5}_([A-
    Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_17988 \d{1,5
    }_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_14056-
    1024 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_10607 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_17619-1280 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_13978 \d{1,5}_([A
    -Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_18746 \d{1,
    5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_17171-1364 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-
    z]{1,20}_){1},_[A-Z]{2}_16881.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-pattern-5.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-pattern-5-3.xml",
        class_name="NistschemaSvIvListTokenPattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_pattern_4_nistxml_sv_iv_list_token_pattern_5_4(mode, save_output, output_format):
    r"""
    Type list/token is restricted by facet pattern with value \d{1,5}_([A-
    Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_17988 \d{1,5
    }_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_14056-
    1024 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_10607 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_17619-1280 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_13978 \d{1,5}_([A
    -Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_18746 \d{1,
    5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_17171-1364 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-
    z]{1,20}_){1},_[A-Z]{2}_16881.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-pattern-5.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-pattern-5-4.xml",
        class_name="NistschemaSvIvListTokenPattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_pattern_4_nistxml_sv_iv_list_token_pattern_5_5(mode, save_output, output_format):
    r"""
    Type list/token is restricted by facet pattern with value \d{1,5}_([A-
    Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_17988 \d{1,5
    }_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_14056-
    1024 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_10607 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_17619-1280 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_13978 \d{1,5}_([A
    -Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_18746 \d{1,
    5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_17171-1364 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-
    z]{1,20}_){1},_[A-Z]{2}_16881.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-pattern-5.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-pattern-5-5.xml",
        class_name="NistschemaSvIvListTokenPattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_pattern_3_nistxml_sv_iv_list_token_pattern_4_1(mode, save_output, output_format):
    r"""
    Type list/token is restricted by facet pattern with value \d{1,5}_([A-
    Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_17930-1652 \
    d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_19453 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_18434-1961 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_14405 \d{1,5}_([A
    -Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_15365 \d{1,
    5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_16114
    \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_14742 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_12190-1064 \d{1,5}_([A-Z][a-
    z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_13082-1344.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-pattern-4.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-pattern-4-1.xml",
        class_name="NistschemaSvIvListTokenPattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_pattern_3_nistxml_sv_iv_list_token_pattern_4_2(mode, save_output, output_format):
    r"""
    Type list/token is restricted by facet pattern with value \d{1,5}_([A-
    Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_17930-1652 \
    d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_19453 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_18434-1961 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_14405 \d{1,5}_([A
    -Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_15365 \d{1,
    5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_16114
    \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_14742 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_12190-1064 \d{1,5}_([A-Z][a-
    z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_13082-1344.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-pattern-4.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-pattern-4-2.xml",
        class_name="NistschemaSvIvListTokenPattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_pattern_3_nistxml_sv_iv_list_token_pattern_4_3(mode, save_output, output_format):
    r"""
    Type list/token is restricted by facet pattern with value \d{1,5}_([A-
    Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_17930-1652 \
    d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_19453 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_18434-1961 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_14405 \d{1,5}_([A
    -Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_15365 \d{1,
    5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_16114
    \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_14742 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_12190-1064 \d{1,5}_([A-Z][a-
    z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_13082-1344.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-pattern-4.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-pattern-4-3.xml",
        class_name="NistschemaSvIvListTokenPattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_pattern_3_nistxml_sv_iv_list_token_pattern_4_4(mode, save_output, output_format):
    r"""
    Type list/token is restricted by facet pattern with value \d{1,5}_([A-
    Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_17930-1652 \
    d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_19453 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_18434-1961 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_14405 \d{1,5}_([A
    -Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_15365 \d{1,
    5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_16114
    \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_14742 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_12190-1064 \d{1,5}_([A-Z][a-
    z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_13082-1344.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-pattern-4.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-pattern-4-4.xml",
        class_name="NistschemaSvIvListTokenPattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_pattern_3_nistxml_sv_iv_list_token_pattern_4_5(mode, save_output, output_format):
    r"""
    Type list/token is restricted by facet pattern with value \d{1,5}_([A-
    Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_17930-1652 \
    d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_19453 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_18434-1961 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_14405 \d{1,5}_([A
    -Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_15365 \d{1,
    5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_16114
    \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_14742 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_12190-1064 \d{1,5}_([A-Z][a-
    z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_13082-1344.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-pattern-4.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-pattern-4-5.xml",
        class_name="NistschemaSvIvListTokenPattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_pattern_2_nistxml_sv_iv_list_token_pattern_3_1(mode, save_output, output_format):
    r"""
    Type list/token is restricted by facet pattern with value \d{1,5}_([A-
    Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_11426-1564 \
    d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_12210 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-
    z]{1,20}_){3},_[A-Z]{2}_10273 \d{1,5}_([A-Z][a-
    z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_15228-1341 \d{1,5
    }_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_19382 
    \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_15012-1071 \d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_16723.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-pattern-3.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-pattern-3-1.xml",
        class_name="NistschemaSvIvListTokenPattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_pattern_2_nistxml_sv_iv_list_token_pattern_3_2(mode, save_output, output_format):
    r"""
    Type list/token is restricted by facet pattern with value \d{1,5}_([A-
    Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_11426-1564 \
    d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_12210 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-
    z]{1,20}_){3},_[A-Z]{2}_10273 \d{1,5}_([A-Z][a-
    z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_15228-1341 \d{1,5
    }_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_19382 
    \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_15012-1071 \d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_16723.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-pattern-3.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-pattern-3-2.xml",
        class_name="NistschemaSvIvListTokenPattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_pattern_2_nistxml_sv_iv_list_token_pattern_3_3(mode, save_output, output_format):
    r"""
    Type list/token is restricted by facet pattern with value \d{1,5}_([A-
    Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_11426-1564 \
    d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_12210 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-
    z]{1,20}_){3},_[A-Z]{2}_10273 \d{1,5}_([A-Z][a-
    z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_15228-1341 \d{1,5
    }_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_19382 
    \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_15012-1071 \d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_16723.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-pattern-3.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-pattern-3-3.xml",
        class_name="NistschemaSvIvListTokenPattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_pattern_2_nistxml_sv_iv_list_token_pattern_3_4(mode, save_output, output_format):
    r"""
    Type list/token is restricted by facet pattern with value \d{1,5}_([A-
    Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_11426-1564 \
    d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_12210 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-
    z]{1,20}_){3},_[A-Z]{2}_10273 \d{1,5}_([A-Z][a-
    z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_15228-1341 \d{1,5
    }_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_19382 
    \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_15012-1071 \d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_16723.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-pattern-3.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-pattern-3-4.xml",
        class_name="NistschemaSvIvListTokenPattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_pattern_2_nistxml_sv_iv_list_token_pattern_3_5(mode, save_output, output_format):
    r"""
    Type list/token is restricted by facet pattern with value \d{1,5}_([A-
    Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_11426-1564 \
    d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_12210 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-
    z]{1,20}_){3},_[A-Z]{2}_10273 \d{1,5}_([A-Z][a-
    z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_15228-1341 \d{1,5
    }_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_19382 
    \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_15012-1071 \d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_16723.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-pattern-3.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-pattern-3-5.xml",
        class_name="NistschemaSvIvListTokenPattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_pattern_1_nistxml_sv_iv_list_token_pattern_2_1(mode, save_output, output_format):
    r"""
    Type list/token is restricted by facet pattern with value \d{1,5}_([A-
    Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_13797-1926 \
    d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_13549-1185 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_11867 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_13558-1548 \d{1,5
    }_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_10722-
    1701 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_14892 \d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_15901-1354 \d{1,5}_([A-Z][a-
    z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_12361 \d{1,5}_([A
    -Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_13151-1383.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-pattern-2.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-pattern-2-1.xml",
        class_name="NistschemaSvIvListTokenPattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_pattern_1_nistxml_sv_iv_list_token_pattern_2_2(mode, save_output, output_format):
    r"""
    Type list/token is restricted by facet pattern with value \d{1,5}_([A-
    Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_13797-1926 \
    d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_13549-1185 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_11867 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_13558-1548 \d{1,5
    }_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_10722-
    1701 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_14892 \d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_15901-1354 \d{1,5}_([A-Z][a-
    z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_12361 \d{1,5}_([A
    -Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_13151-1383.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-pattern-2.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-pattern-2-2.xml",
        class_name="NistschemaSvIvListTokenPattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_pattern_1_nistxml_sv_iv_list_token_pattern_2_3(mode, save_output, output_format):
    r"""
    Type list/token is restricted by facet pattern with value \d{1,5}_([A-
    Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_13797-1926 \
    d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_13549-1185 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_11867 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_13558-1548 \d{1,5
    }_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_10722-
    1701 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_14892 \d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_15901-1354 \d{1,5}_([A-Z][a-
    z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_12361 \d{1,5}_([A
    -Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_13151-1383.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-pattern-2.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-pattern-2-3.xml",
        class_name="NistschemaSvIvListTokenPattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_pattern_1_nistxml_sv_iv_list_token_pattern_2_4(mode, save_output, output_format):
    r"""
    Type list/token is restricted by facet pattern with value \d{1,5}_([A-
    Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_13797-1926 \
    d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_13549-1185 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_11867 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_13558-1548 \d{1,5
    }_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_10722-
    1701 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_14892 \d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_15901-1354 \d{1,5}_([A-Z][a-
    z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_12361 \d{1,5}_([A
    -Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_13151-1383.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-pattern-2.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-pattern-2-4.xml",
        class_name="NistschemaSvIvListTokenPattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_pattern_1_nistxml_sv_iv_list_token_pattern_2_5(mode, save_output, output_format):
    r"""
    Type list/token is restricted by facet pattern with value \d{1,5}_([A-
    Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_13797-1926 \
    d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_13549-1185 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_11867 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_13558-1548 \d{1,5
    }_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_10722-
    1701 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_14892 \d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_15901-1354 \d{1,5}_([A-Z][a-
    z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_12361 \d{1,5}_([A
    -Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_13151-1383.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-pattern-2.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-pattern-2-5.xml",
        class_name="NistschemaSvIvListTokenPattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_pattern_nistxml_sv_iv_list_token_pattern_1_1(mode, save_output, output_format):
    r"""
    Type list/token is restricted by facet pattern with value \d{1,5}_([A-
    Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_15685 \d{1,5
    }_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_13673 
    \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_10126 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_12533 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_13175.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-pattern-1.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-pattern-1-1.xml",
        class_name="NistschemaSvIvListTokenPattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_pattern_nistxml_sv_iv_list_token_pattern_1_2(mode, save_output, output_format):
    r"""
    Type list/token is restricted by facet pattern with value \d{1,5}_([A-
    Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_15685 \d{1,5
    }_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_13673 
    \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_10126 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_12533 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_13175.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-pattern-1.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-pattern-1-2.xml",
        class_name="NistschemaSvIvListTokenPattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_pattern_nistxml_sv_iv_list_token_pattern_1_3(mode, save_output, output_format):
    r"""
    Type list/token is restricted by facet pattern with value \d{1,5}_([A-
    Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_15685 \d{1,5
    }_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_13673 
    \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_10126 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_12533 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_13175.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-pattern-1.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-pattern-1-3.xml",
        class_name="NistschemaSvIvListTokenPattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_pattern_nistxml_sv_iv_list_token_pattern_1_4(mode, save_output, output_format):
    r"""
    Type list/token is restricted by facet pattern with value \d{1,5}_([A-
    Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_15685 \d{1,5
    }_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_13673 
    \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_10126 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_12533 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_13175.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-pattern-1.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-pattern-1-4.xml",
        class_name="NistschemaSvIvListTokenPattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_pattern_nistxml_sv_iv_list_token_pattern_1_5(mode, save_output, output_format):
    r"""
    Type list/token is restricted by facet pattern with value \d{1,5}_([A-
    Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_15685 \d{1,5
    }_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_13673 
    \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_10126 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_12533 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_13175.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-pattern-1.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-pattern-1-5.xml",
        class_name="NistschemaSvIvListTokenPattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_length_4_nistxml_sv_iv_list_token_length_5_1(mode, save_output, output_format):
    """
    Type list/token is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-length-5.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-length-5-1.xml",
        class_name="NistschemaSvIvListTokenLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_length_4_nistxml_sv_iv_list_token_length_5_2(mode, save_output, output_format):
    """
    Type list/token is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-length-5.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-length-5-2.xml",
        class_name="NistschemaSvIvListTokenLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_length_4_nistxml_sv_iv_list_token_length_5_3(mode, save_output, output_format):
    """
    Type list/token is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-length-5.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-length-5-3.xml",
        class_name="NistschemaSvIvListTokenLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_length_4_nistxml_sv_iv_list_token_length_5_4(mode, save_output, output_format):
    """
    Type list/token is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-length-5.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-length-5-4.xml",
        class_name="NistschemaSvIvListTokenLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_length_4_nistxml_sv_iv_list_token_length_5_5(mode, save_output, output_format):
    """
    Type list/token is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-length-5.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-length-5-5.xml",
        class_name="NistschemaSvIvListTokenLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_length_3_nistxml_sv_iv_list_token_length_4_1(mode, save_output, output_format):
    """
    Type list/token is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-length-4.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-length-4-1.xml",
        class_name="NistschemaSvIvListTokenLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_length_3_nistxml_sv_iv_list_token_length_4_2(mode, save_output, output_format):
    """
    Type list/token is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-length-4.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-length-4-2.xml",
        class_name="NistschemaSvIvListTokenLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_length_3_nistxml_sv_iv_list_token_length_4_3(mode, save_output, output_format):
    """
    Type list/token is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-length-4.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-length-4-3.xml",
        class_name="NistschemaSvIvListTokenLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_length_3_nistxml_sv_iv_list_token_length_4_4(mode, save_output, output_format):
    """
    Type list/token is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-length-4.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-length-4-4.xml",
        class_name="NistschemaSvIvListTokenLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_length_3_nistxml_sv_iv_list_token_length_4_5(mode, save_output, output_format):
    """
    Type list/token is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-length-4.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-length-4-5.xml",
        class_name="NistschemaSvIvListTokenLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_length_2_nistxml_sv_iv_list_token_length_3_1(mode, save_output, output_format):
    """
    Type list/token is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-length-3.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-length-3-1.xml",
        class_name="NistschemaSvIvListTokenLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_length_2_nistxml_sv_iv_list_token_length_3_2(mode, save_output, output_format):
    """
    Type list/token is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-length-3.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-length-3-2.xml",
        class_name="NistschemaSvIvListTokenLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_length_2_nistxml_sv_iv_list_token_length_3_3(mode, save_output, output_format):
    """
    Type list/token is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-length-3.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-length-3-3.xml",
        class_name="NistschemaSvIvListTokenLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_length_2_nistxml_sv_iv_list_token_length_3_4(mode, save_output, output_format):
    """
    Type list/token is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-length-3.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-length-3-4.xml",
        class_name="NistschemaSvIvListTokenLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_length_2_nistxml_sv_iv_list_token_length_3_5(mode, save_output, output_format):
    """
    Type list/token is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-length-3.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-length-3-5.xml",
        class_name="NistschemaSvIvListTokenLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_length_1_nistxml_sv_iv_list_token_length_2_1(mode, save_output, output_format):
    """
    Type list/token is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-length-2.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-length-2-1.xml",
        class_name="NistschemaSvIvListTokenLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_length_1_nistxml_sv_iv_list_token_length_2_2(mode, save_output, output_format):
    """
    Type list/token is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-length-2.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-length-2-2.xml",
        class_name="NistschemaSvIvListTokenLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_length_1_nistxml_sv_iv_list_token_length_2_3(mode, save_output, output_format):
    """
    Type list/token is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-length-2.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-length-2-3.xml",
        class_name="NistschemaSvIvListTokenLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_length_1_nistxml_sv_iv_list_token_length_2_4(mode, save_output, output_format):
    """
    Type list/token is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-length-2.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-length-2-4.xml",
        class_name="NistschemaSvIvListTokenLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_length_1_nistxml_sv_iv_list_token_length_2_5(mode, save_output, output_format):
    """
    Type list/token is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-length-2.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-length-2-5.xml",
        class_name="NistschemaSvIvListTokenLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_length_nistxml_sv_iv_list_token_length_1_1(mode, save_output, output_format):
    """
    Type list/token is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-length-1.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-length-1-1.xml",
        class_name="NistschemaSvIvListTokenLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_length_nistxml_sv_iv_list_token_length_1_2(mode, save_output, output_format):
    """
    Type list/token is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-length-1.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-length-1-2.xml",
        class_name="NistschemaSvIvListTokenLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_length_nistxml_sv_iv_list_token_length_1_3(mode, save_output, output_format):
    """
    Type list/token is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-length-1.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-length-1-3.xml",
        class_name="NistschemaSvIvListTokenLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_length_nistxml_sv_iv_list_token_length_1_4(mode, save_output, output_format):
    """
    Type list/token is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-length-1.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-length-1-4.xml",
        class_name="NistschemaSvIvListTokenLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_length_nistxml_sv_iv_list_token_length_1_5(mode, save_output, output_format):
    """
    Type list/token is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-length-1.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-length-1-5.xml",
        class_name="NistschemaSvIvListTokenLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_min_length_4_nistxml_sv_iv_list_token_min_length_5_1(mode, save_output, output_format):
    """
    Type list/token is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-minLength-5.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-minLength-5-1.xml",
        class_name="NistschemaSvIvListTokenMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_min_length_4_nistxml_sv_iv_list_token_min_length_5_2(mode, save_output, output_format):
    """
    Type list/token is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-minLength-5.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-minLength-5-2.xml",
        class_name="NistschemaSvIvListTokenMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_min_length_4_nistxml_sv_iv_list_token_min_length_5_3(mode, save_output, output_format):
    """
    Type list/token is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-minLength-5.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-minLength-5-3.xml",
        class_name="NistschemaSvIvListTokenMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_min_length_4_nistxml_sv_iv_list_token_min_length_5_4(mode, save_output, output_format):
    """
    Type list/token is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-minLength-5.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-minLength-5-4.xml",
        class_name="NistschemaSvIvListTokenMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_min_length_4_nistxml_sv_iv_list_token_min_length_5_5(mode, save_output, output_format):
    """
    Type list/token is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-minLength-5.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-minLength-5-5.xml",
        class_name="NistschemaSvIvListTokenMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_min_length_3_nistxml_sv_iv_list_token_min_length_4_1(mode, save_output, output_format):
    """
    Type list/token is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-minLength-4.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-minLength-4-1.xml",
        class_name="NistschemaSvIvListTokenMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_min_length_3_nistxml_sv_iv_list_token_min_length_4_2(mode, save_output, output_format):
    """
    Type list/token is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-minLength-4.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-minLength-4-2.xml",
        class_name="NistschemaSvIvListTokenMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_min_length_3_nistxml_sv_iv_list_token_min_length_4_3(mode, save_output, output_format):
    """
    Type list/token is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-minLength-4.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-minLength-4-3.xml",
        class_name="NistschemaSvIvListTokenMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_min_length_3_nistxml_sv_iv_list_token_min_length_4_4(mode, save_output, output_format):
    """
    Type list/token is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-minLength-4.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-minLength-4-4.xml",
        class_name="NistschemaSvIvListTokenMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_min_length_3_nistxml_sv_iv_list_token_min_length_4_5(mode, save_output, output_format):
    """
    Type list/token is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-minLength-4.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-minLength-4-5.xml",
        class_name="NistschemaSvIvListTokenMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_min_length_2_nistxml_sv_iv_list_token_min_length_3_1(mode, save_output, output_format):
    """
    Type list/token is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-minLength-3.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-minLength-3-1.xml",
        class_name="NistschemaSvIvListTokenMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_min_length_2_nistxml_sv_iv_list_token_min_length_3_2(mode, save_output, output_format):
    """
    Type list/token is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-minLength-3.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-minLength-3-2.xml",
        class_name="NistschemaSvIvListTokenMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_min_length_2_nistxml_sv_iv_list_token_min_length_3_3(mode, save_output, output_format):
    """
    Type list/token is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-minLength-3.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-minLength-3-3.xml",
        class_name="NistschemaSvIvListTokenMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_min_length_2_nistxml_sv_iv_list_token_min_length_3_4(mode, save_output, output_format):
    """
    Type list/token is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-minLength-3.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-minLength-3-4.xml",
        class_name="NistschemaSvIvListTokenMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_min_length_2_nistxml_sv_iv_list_token_min_length_3_5(mode, save_output, output_format):
    """
    Type list/token is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-minLength-3.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-minLength-3-5.xml",
        class_name="NistschemaSvIvListTokenMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_min_length_1_nistxml_sv_iv_list_token_min_length_2_1(mode, save_output, output_format):
    """
    Type list/token is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-minLength-2.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-minLength-2-1.xml",
        class_name="NistschemaSvIvListTokenMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_min_length_1_nistxml_sv_iv_list_token_min_length_2_2(mode, save_output, output_format):
    """
    Type list/token is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-minLength-2.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-minLength-2-2.xml",
        class_name="NistschemaSvIvListTokenMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_min_length_1_nistxml_sv_iv_list_token_min_length_2_3(mode, save_output, output_format):
    """
    Type list/token is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-minLength-2.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-minLength-2-3.xml",
        class_name="NistschemaSvIvListTokenMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_min_length_1_nistxml_sv_iv_list_token_min_length_2_4(mode, save_output, output_format):
    """
    Type list/token is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-minLength-2.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-minLength-2-4.xml",
        class_name="NistschemaSvIvListTokenMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_min_length_1_nistxml_sv_iv_list_token_min_length_2_5(mode, save_output, output_format):
    """
    Type list/token is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-minLength-2.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-minLength-2-5.xml",
        class_name="NistschemaSvIvListTokenMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_min_length_nistxml_sv_iv_list_token_min_length_1_1(mode, save_output, output_format):
    """
    Type list/token is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-minLength-1.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-minLength-1-1.xml",
        class_name="NistschemaSvIvListTokenMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_min_length_nistxml_sv_iv_list_token_min_length_1_2(mode, save_output, output_format):
    """
    Type list/token is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-minLength-1.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-minLength-1-2.xml",
        class_name="NistschemaSvIvListTokenMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_min_length_nistxml_sv_iv_list_token_min_length_1_3(mode, save_output, output_format):
    """
    Type list/token is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-minLength-1.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-minLength-1-3.xml",
        class_name="NistschemaSvIvListTokenMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_min_length_nistxml_sv_iv_list_token_min_length_1_4(mode, save_output, output_format):
    """
    Type list/token is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-minLength-1.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-minLength-1-4.xml",
        class_name="NistschemaSvIvListTokenMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_min_length_nistxml_sv_iv_list_token_min_length_1_5(mode, save_output, output_format):
    """
    Type list/token is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-minLength-1.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-minLength-1-5.xml",
        class_name="NistschemaSvIvListTokenMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_max_length_4_nistxml_sv_iv_list_token_max_length_5_1(mode, save_output, output_format):
    """
    Type list/token is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-maxLength-5.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-maxLength-5-1.xml",
        class_name="NistschemaSvIvListTokenMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_max_length_4_nistxml_sv_iv_list_token_max_length_5_2(mode, save_output, output_format):
    """
    Type list/token is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-maxLength-5.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-maxLength-5-2.xml",
        class_name="NistschemaSvIvListTokenMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_max_length_4_nistxml_sv_iv_list_token_max_length_5_3(mode, save_output, output_format):
    """
    Type list/token is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-maxLength-5.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-maxLength-5-3.xml",
        class_name="NistschemaSvIvListTokenMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_max_length_4_nistxml_sv_iv_list_token_max_length_5_4(mode, save_output, output_format):
    """
    Type list/token is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-maxLength-5.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-maxLength-5-4.xml",
        class_name="NistschemaSvIvListTokenMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_max_length_4_nistxml_sv_iv_list_token_max_length_5_5(mode, save_output, output_format):
    """
    Type list/token is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-maxLength-5.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-maxLength-5-5.xml",
        class_name="NistschemaSvIvListTokenMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_max_length_3_nistxml_sv_iv_list_token_max_length_4_1(mode, save_output, output_format):
    """
    Type list/token is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-maxLength-4.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-maxLength-4-1.xml",
        class_name="NistschemaSvIvListTokenMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_max_length_3_nistxml_sv_iv_list_token_max_length_4_2(mode, save_output, output_format):
    """
    Type list/token is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-maxLength-4.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-maxLength-4-2.xml",
        class_name="NistschemaSvIvListTokenMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_max_length_3_nistxml_sv_iv_list_token_max_length_4_3(mode, save_output, output_format):
    """
    Type list/token is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-maxLength-4.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-maxLength-4-3.xml",
        class_name="NistschemaSvIvListTokenMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_max_length_3_nistxml_sv_iv_list_token_max_length_4_4(mode, save_output, output_format):
    """
    Type list/token is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-maxLength-4.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-maxLength-4-4.xml",
        class_name="NistschemaSvIvListTokenMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_max_length_3_nistxml_sv_iv_list_token_max_length_4_5(mode, save_output, output_format):
    """
    Type list/token is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-maxLength-4.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-maxLength-4-5.xml",
        class_name="NistschemaSvIvListTokenMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_max_length_2_nistxml_sv_iv_list_token_max_length_3_1(mode, save_output, output_format):
    """
    Type list/token is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-maxLength-3.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-maxLength-3-1.xml",
        class_name="NistschemaSvIvListTokenMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_max_length_2_nistxml_sv_iv_list_token_max_length_3_2(mode, save_output, output_format):
    """
    Type list/token is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-maxLength-3.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-maxLength-3-2.xml",
        class_name="NistschemaSvIvListTokenMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_max_length_2_nistxml_sv_iv_list_token_max_length_3_3(mode, save_output, output_format):
    """
    Type list/token is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-maxLength-3.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-maxLength-3-3.xml",
        class_name="NistschemaSvIvListTokenMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_max_length_2_nistxml_sv_iv_list_token_max_length_3_4(mode, save_output, output_format):
    """
    Type list/token is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-maxLength-3.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-maxLength-3-4.xml",
        class_name="NistschemaSvIvListTokenMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_max_length_2_nistxml_sv_iv_list_token_max_length_3_5(mode, save_output, output_format):
    """
    Type list/token is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-maxLength-3.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-maxLength-3-5.xml",
        class_name="NistschemaSvIvListTokenMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_max_length_1_nistxml_sv_iv_list_token_max_length_2_1(mode, save_output, output_format):
    """
    Type list/token is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-maxLength-2.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-maxLength-2-1.xml",
        class_name="NistschemaSvIvListTokenMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_max_length_1_nistxml_sv_iv_list_token_max_length_2_2(mode, save_output, output_format):
    """
    Type list/token is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-maxLength-2.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-maxLength-2-2.xml",
        class_name="NistschemaSvIvListTokenMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_max_length_1_nistxml_sv_iv_list_token_max_length_2_3(mode, save_output, output_format):
    """
    Type list/token is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-maxLength-2.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-maxLength-2-3.xml",
        class_name="NistschemaSvIvListTokenMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_max_length_1_nistxml_sv_iv_list_token_max_length_2_4(mode, save_output, output_format):
    """
    Type list/token is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-maxLength-2.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-maxLength-2-4.xml",
        class_name="NistschemaSvIvListTokenMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_max_length_1_nistxml_sv_iv_list_token_max_length_2_5(mode, save_output, output_format):
    """
    Type list/token is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-maxLength-2.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-maxLength-2-5.xml",
        class_name="NistschemaSvIvListTokenMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_max_length_nistxml_sv_iv_list_token_max_length_1_1(mode, save_output, output_format):
    """
    Type list/token is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-maxLength-1.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-maxLength-1-1.xml",
        class_name="NistschemaSvIvListTokenMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_max_length_nistxml_sv_iv_list_token_max_length_1_2(mode, save_output, output_format):
    """
    Type list/token is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-maxLength-1.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-maxLength-1-2.xml",
        class_name="NistschemaSvIvListTokenMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_max_length_nistxml_sv_iv_list_token_max_length_1_3(mode, save_output, output_format):
    """
    Type list/token is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-maxLength-1.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-maxLength-1-3.xml",
        class_name="NistschemaSvIvListTokenMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_max_length_nistxml_sv_iv_list_token_max_length_1_4(mode, save_output, output_format):
    """
    Type list/token is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-maxLength-1.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-maxLength-1-4.xml",
        class_name="NistschemaSvIvListTokenMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_token_max_length_nistxml_sv_iv_list_token_max_length_1_5(mode, save_output, output_format):
    """
    Type list/token is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/token/Schema+Instance/NISTSchema-SV-IV-list-token-maxLength-1.xsd",
        instance="nistData/list/token/Schema+Instance/NISTXML-SV-IV-list-token-maxLength-1-5.xml",
        class_name="NistschemaSvIvListTokenMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_white_space_nistxml_sv_iv_list_normalized_string_white_space_1_1(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet whiteSpace with
    value collapse.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-whiteSpace-1.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-whiteSpace-1-1.xml",
        class_name="NistschemaSvIvListNormalizedStringWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_white_space_nistxml_sv_iv_list_normalized_string_white_space_1_2(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet whiteSpace with
    value collapse.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-whiteSpace-1.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-whiteSpace-1-2.xml",
        class_name="NistschemaSvIvListNormalizedStringWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_white_space_nistxml_sv_iv_list_normalized_string_white_space_1_3(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet whiteSpace with
    value collapse.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-whiteSpace-1.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-whiteSpace-1-3.xml",
        class_name="NistschemaSvIvListNormalizedStringWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_white_space_nistxml_sv_iv_list_normalized_string_white_space_1_4(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet whiteSpace with
    value collapse.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-whiteSpace-1.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-whiteSpace-1-4.xml",
        class_name="NistschemaSvIvListNormalizedStringWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_white_space_nistxml_sv_iv_list_normalized_string_white_space_1_5(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet whiteSpace with
    value collapse.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-whiteSpace-1.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-whiteSpace-1-5.xml",
        class_name="NistschemaSvIvListNormalizedStringWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_enumeration_4_nistxml_sv_iv_list_normalized_string_enumeration_5_1(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-enumeration-5.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-enumeration-5-1.xml",
        class_name="NistschemaSvIvListNormalizedStringEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_enumeration_4_nistxml_sv_iv_list_normalized_string_enumeration_5_2(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-enumeration-5.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-enumeration-5-2.xml",
        class_name="NistschemaSvIvListNormalizedStringEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_enumeration_4_nistxml_sv_iv_list_normalized_string_enumeration_5_3(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-enumeration-5.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-enumeration-5-3.xml",
        class_name="NistschemaSvIvListNormalizedStringEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_enumeration_4_nistxml_sv_iv_list_normalized_string_enumeration_5_4(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-enumeration-5.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-enumeration-5-4.xml",
        class_name="NistschemaSvIvListNormalizedStringEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_enumeration_4_nistxml_sv_iv_list_normalized_string_enumeration_5_5(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-enumeration-5.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-enumeration-5-5.xml",
        class_name="NistschemaSvIvListNormalizedStringEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_enumeration_3_nistxml_sv_iv_list_normalized_string_enumeration_4_1(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-enumeration-4.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-enumeration-4-1.xml",
        class_name="NistschemaSvIvListNormalizedStringEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_enumeration_3_nistxml_sv_iv_list_normalized_string_enumeration_4_2(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-enumeration-4.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-enumeration-4-2.xml",
        class_name="NistschemaSvIvListNormalizedStringEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_enumeration_3_nistxml_sv_iv_list_normalized_string_enumeration_4_3(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-enumeration-4.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-enumeration-4-3.xml",
        class_name="NistschemaSvIvListNormalizedStringEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_enumeration_3_nistxml_sv_iv_list_normalized_string_enumeration_4_4(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-enumeration-4.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-enumeration-4-4.xml",
        class_name="NistschemaSvIvListNormalizedStringEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_enumeration_3_nistxml_sv_iv_list_normalized_string_enumeration_4_5(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-enumeration-4.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-enumeration-4-5.xml",
        class_name="NistschemaSvIvListNormalizedStringEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_enumeration_2_nistxml_sv_iv_list_normalized_string_enumeration_3_1(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-enumeration-3.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-enumeration-3-1.xml",
        class_name="NistschemaSvIvListNormalizedStringEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_enumeration_2_nistxml_sv_iv_list_normalized_string_enumeration_3_2(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-enumeration-3.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-enumeration-3-2.xml",
        class_name="NistschemaSvIvListNormalizedStringEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_enumeration_2_nistxml_sv_iv_list_normalized_string_enumeration_3_3(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-enumeration-3.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-enumeration-3-3.xml",
        class_name="NistschemaSvIvListNormalizedStringEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_enumeration_2_nistxml_sv_iv_list_normalized_string_enumeration_3_4(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-enumeration-3.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-enumeration-3-4.xml",
        class_name="NistschemaSvIvListNormalizedStringEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_enumeration_2_nistxml_sv_iv_list_normalized_string_enumeration_3_5(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-enumeration-3.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-enumeration-3-5.xml",
        class_name="NistschemaSvIvListNormalizedStringEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_enumeration_1_nistxml_sv_iv_list_normalized_string_enumeration_2_1(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-enumeration-2.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-enumeration-2-1.xml",
        class_name="NistschemaSvIvListNormalizedStringEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_enumeration_1_nistxml_sv_iv_list_normalized_string_enumeration_2_2(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-enumeration-2.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-enumeration-2-2.xml",
        class_name="NistschemaSvIvListNormalizedStringEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_enumeration_1_nistxml_sv_iv_list_normalized_string_enumeration_2_3(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-enumeration-2.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-enumeration-2-3.xml",
        class_name="NistschemaSvIvListNormalizedStringEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_enumeration_1_nistxml_sv_iv_list_normalized_string_enumeration_2_4(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-enumeration-2.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-enumeration-2-4.xml",
        class_name="NistschemaSvIvListNormalizedStringEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_enumeration_1_nistxml_sv_iv_list_normalized_string_enumeration_2_5(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-enumeration-2.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-enumeration-2-5.xml",
        class_name="NistschemaSvIvListNormalizedStringEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_enumeration_nistxml_sv_iv_list_normalized_string_enumeration_1_1(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-enumeration-1.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-enumeration-1-1.xml",
        class_name="NistschemaSvIvListNormalizedStringEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_enumeration_nistxml_sv_iv_list_normalized_string_enumeration_1_2(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-enumeration-1.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-enumeration-1-2.xml",
        class_name="NistschemaSvIvListNormalizedStringEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_enumeration_nistxml_sv_iv_list_normalized_string_enumeration_1_3(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-enumeration-1.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-enumeration-1-3.xml",
        class_name="NistschemaSvIvListNormalizedStringEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_enumeration_nistxml_sv_iv_list_normalized_string_enumeration_1_4(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-enumeration-1.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-enumeration-1-4.xml",
        class_name="NistschemaSvIvListNormalizedStringEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_enumeration_nistxml_sv_iv_list_normalized_string_enumeration_1_5(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-enumeration-1.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-enumeration-1-5.xml",
        class_name="NistschemaSvIvListNormalizedStringEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_pattern_4_nistxml_sv_iv_list_normalized_string_pattern_5_1(mode, save_output, output_format):
    r"""
    Type list/normalizedString is restricted by facet pattern with value \
    d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_14600 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-
    z]{1,20}_){3},_[A-Z]{2}_15165-1290 \d{1,5}_([A-Z][a-
    z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_17813-1396 \d{1,5
    }_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_18970 
    \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_13025 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-
    z]{1,20}_){3},_[A-Z]{2}_15706-1707 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_16336.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-pattern-5.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-pattern-5-1.xml",
        class_name="NistschemaSvIvListNormalizedStringPattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_pattern_4_nistxml_sv_iv_list_normalized_string_pattern_5_2(mode, save_output, output_format):
    r"""
    Type list/normalizedString is restricted by facet pattern with value \
    d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_14600 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-
    z]{1,20}_){3},_[A-Z]{2}_15165-1290 \d{1,5}_([A-Z][a-
    z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_17813-1396 \d{1,5
    }_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_18970 
    \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_13025 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-
    z]{1,20}_){3},_[A-Z]{2}_15706-1707 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_16336.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-pattern-5.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-pattern-5-2.xml",
        class_name="NistschemaSvIvListNormalizedStringPattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_pattern_4_nistxml_sv_iv_list_normalized_string_pattern_5_3(mode, save_output, output_format):
    r"""
    Type list/normalizedString is restricted by facet pattern with value \
    d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_14600 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-
    z]{1,20}_){3},_[A-Z]{2}_15165-1290 \d{1,5}_([A-Z][a-
    z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_17813-1396 \d{1,5
    }_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_18970 
    \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_13025 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-
    z]{1,20}_){3},_[A-Z]{2}_15706-1707 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_16336.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-pattern-5.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-pattern-5-3.xml",
        class_name="NistschemaSvIvListNormalizedStringPattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_pattern_4_nistxml_sv_iv_list_normalized_string_pattern_5_4(mode, save_output, output_format):
    r"""
    Type list/normalizedString is restricted by facet pattern with value \
    d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_14600 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-
    z]{1,20}_){3},_[A-Z]{2}_15165-1290 \d{1,5}_([A-Z][a-
    z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_17813-1396 \d{1,5
    }_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_18970 
    \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_13025 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-
    z]{1,20}_){3},_[A-Z]{2}_15706-1707 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_16336.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-pattern-5.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-pattern-5-4.xml",
        class_name="NistschemaSvIvListNormalizedStringPattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_pattern_4_nistxml_sv_iv_list_normalized_string_pattern_5_5(mode, save_output, output_format):
    r"""
    Type list/normalizedString is restricted by facet pattern with value \
    d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_14600 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-
    z]{1,20}_){3},_[A-Z]{2}_15165-1290 \d{1,5}_([A-Z][a-
    z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_17813-1396 \d{1,5
    }_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_18970 
    \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_13025 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-
    z]{1,20}_){3},_[A-Z]{2}_15706-1707 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_16336.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-pattern-5.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-pattern-5-5.xml",
        class_name="NistschemaSvIvListNormalizedStringPattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_pattern_3_nistxml_sv_iv_list_normalized_string_pattern_4_1(mode, save_output, output_format):
    r"""
    Type list/normalizedString is restricted by facet pattern with value \
    d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_17466-1733 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_16877 \d{1,5}_([A-Z][a-
    z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_16698-1324 \d{1,5
    }_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_18587 
    \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_10792 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_11619-1091.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-pattern-4.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-pattern-4-1.xml",
        class_name="NistschemaSvIvListNormalizedStringPattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_pattern_3_nistxml_sv_iv_list_normalized_string_pattern_4_2(mode, save_output, output_format):
    r"""
    Type list/normalizedString is restricted by facet pattern with value \
    d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_17466-1733 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_16877 \d{1,5}_([A-Z][a-
    z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_16698-1324 \d{1,5
    }_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_18587 
    \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_10792 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_11619-1091.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-pattern-4.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-pattern-4-2.xml",
        class_name="NistschemaSvIvListNormalizedStringPattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_pattern_3_nistxml_sv_iv_list_normalized_string_pattern_4_3(mode, save_output, output_format):
    r"""
    Type list/normalizedString is restricted by facet pattern with value \
    d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_17466-1733 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_16877 \d{1,5}_([A-Z][a-
    z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_16698-1324 \d{1,5
    }_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_18587 
    \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_10792 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_11619-1091.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-pattern-4.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-pattern-4-3.xml",
        class_name="NistschemaSvIvListNormalizedStringPattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_pattern_3_nistxml_sv_iv_list_normalized_string_pattern_4_4(mode, save_output, output_format):
    r"""
    Type list/normalizedString is restricted by facet pattern with value \
    d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_17466-1733 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_16877 \d{1,5}_([A-Z][a-
    z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_16698-1324 \d{1,5
    }_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_18587 
    \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_10792 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_11619-1091.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-pattern-4.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-pattern-4-4.xml",
        class_name="NistschemaSvIvListNormalizedStringPattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_pattern_3_nistxml_sv_iv_list_normalized_string_pattern_4_5(mode, save_output, output_format):
    r"""
    Type list/normalizedString is restricted by facet pattern with value \
    d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_17466-1733 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_16877 \d{1,5}_([A-Z][a-
    z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_16698-1324 \d{1,5
    }_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_18587 
    \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_10792 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_11619-1091.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-pattern-4.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-pattern-4-5.xml",
        class_name="NistschemaSvIvListNormalizedStringPattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_pattern_2_nistxml_sv_iv_list_normalized_string_pattern_3_1(mode, save_output, output_format):
    r"""
    Type list/normalizedString is restricted by facet pattern with value \
    d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_12432 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-
    z]{1,20}_){1},_[A-Z]{2}_10161 \d{1,5}_([A-Z][a-
    z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_11432-1137 \d{1,5
    }_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_14004 
    \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_19543-1772 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-
    z]{1,20}_){3},_[A-Z]{2}_16553-1944.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-pattern-3.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-pattern-3-1.xml",
        class_name="NistschemaSvIvListNormalizedStringPattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_pattern_2_nistxml_sv_iv_list_normalized_string_pattern_3_2(mode, save_output, output_format):
    r"""
    Type list/normalizedString is restricted by facet pattern with value \
    d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_12432 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-
    z]{1,20}_){1},_[A-Z]{2}_10161 \d{1,5}_([A-Z][a-
    z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_11432-1137 \d{1,5
    }_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_14004 
    \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_19543-1772 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-
    z]{1,20}_){3},_[A-Z]{2}_16553-1944.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-pattern-3.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-pattern-3-2.xml",
        class_name="NistschemaSvIvListNormalizedStringPattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_pattern_2_nistxml_sv_iv_list_normalized_string_pattern_3_3(mode, save_output, output_format):
    r"""
    Type list/normalizedString is restricted by facet pattern with value \
    d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_12432 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-
    z]{1,20}_){1},_[A-Z]{2}_10161 \d{1,5}_([A-Z][a-
    z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_11432-1137 \d{1,5
    }_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_14004 
    \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_19543-1772 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-
    z]{1,20}_){3},_[A-Z]{2}_16553-1944.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-pattern-3.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-pattern-3-3.xml",
        class_name="NistschemaSvIvListNormalizedStringPattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_pattern_2_nistxml_sv_iv_list_normalized_string_pattern_3_4(mode, save_output, output_format):
    r"""
    Type list/normalizedString is restricted by facet pattern with value \
    d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_12432 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-
    z]{1,20}_){1},_[A-Z]{2}_10161 \d{1,5}_([A-Z][a-
    z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_11432-1137 \d{1,5
    }_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_14004 
    \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_19543-1772 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-
    z]{1,20}_){3},_[A-Z]{2}_16553-1944.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-pattern-3.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-pattern-3-4.xml",
        class_name="NistschemaSvIvListNormalizedStringPattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_pattern_2_nistxml_sv_iv_list_normalized_string_pattern_3_5(mode, save_output, output_format):
    r"""
    Type list/normalizedString is restricted by facet pattern with value \
    d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_12432 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-
    z]{1,20}_){1},_[A-Z]{2}_10161 \d{1,5}_([A-Z][a-
    z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_11432-1137 \d{1,5
    }_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_14004 
    \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_19543-1772 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-
    z]{1,20}_){3},_[A-Z]{2}_16553-1944.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-pattern-3.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-pattern-3-5.xml",
        class_name="NistschemaSvIvListNormalizedStringPattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_pattern_1_nistxml_sv_iv_list_normalized_string_pattern_2_1(mode, save_output, output_format):
    r"""
    Type list/normalizedString is restricted by facet pattern with value \
    d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_15950 \d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_15905 \d{1,5}_([A-Z][a-
    z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_15311 \d{1,5}_([A
    -Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_12031 \d{1,
    5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_10376.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-pattern-2.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-pattern-2-1.xml",
        class_name="NistschemaSvIvListNormalizedStringPattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_pattern_1_nistxml_sv_iv_list_normalized_string_pattern_2_2(mode, save_output, output_format):
    r"""
    Type list/normalizedString is restricted by facet pattern with value \
    d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_15950 \d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_15905 \d{1,5}_([A-Z][a-
    z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_15311 \d{1,5}_([A
    -Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_12031 \d{1,
    5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_10376.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-pattern-2.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-pattern-2-2.xml",
        class_name="NistschemaSvIvListNormalizedStringPattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_pattern_1_nistxml_sv_iv_list_normalized_string_pattern_2_3(mode, save_output, output_format):
    r"""
    Type list/normalizedString is restricted by facet pattern with value \
    d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_15950 \d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_15905 \d{1,5}_([A-Z][a-
    z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_15311 \d{1,5}_([A
    -Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_12031 \d{1,
    5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_10376.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-pattern-2.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-pattern-2-3.xml",
        class_name="NistschemaSvIvListNormalizedStringPattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_pattern_1_nistxml_sv_iv_list_normalized_string_pattern_2_4(mode, save_output, output_format):
    r"""
    Type list/normalizedString is restricted by facet pattern with value \
    d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_15950 \d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_15905 \d{1,5}_([A-Z][a-
    z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_15311 \d{1,5}_([A
    -Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_12031 \d{1,
    5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_10376.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-pattern-2.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-pattern-2-4.xml",
        class_name="NistschemaSvIvListNormalizedStringPattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_pattern_1_nistxml_sv_iv_list_normalized_string_pattern_2_5(mode, save_output, output_format):
    r"""
    Type list/normalizedString is restricted by facet pattern with value \
    d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_15950 \d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_15905 \d{1,5}_([A-Z][a-
    z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_15311 \d{1,5}_([A
    -Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_12031 \d{1,
    5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_10376.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-pattern-2.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-pattern-2-5.xml",
        class_name="NistschemaSvIvListNormalizedStringPattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_pattern_nistxml_sv_iv_list_normalized_string_pattern_1_1(mode, save_output, output_format):
    r"""
    Type list/normalizedString is restricted by facet pattern with value \
    d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_13058 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_14172 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_13454 \d{1,5}_([A
    -Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_10133-1061 
    \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_10981 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_16632 \d{1,5}_([A-Z][a-
    z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_19839.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-pattern-1.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-pattern-1-1.xml",
        class_name="NistschemaSvIvListNormalizedStringPattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_pattern_nistxml_sv_iv_list_normalized_string_pattern_1_2(mode, save_output, output_format):
    r"""
    Type list/normalizedString is restricted by facet pattern with value \
    d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_13058 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_14172 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_13454 \d{1,5}_([A
    -Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_10133-1061 
    \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_10981 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_16632 \d{1,5}_([A-Z][a-
    z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_19839.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-pattern-1.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-pattern-1-2.xml",
        class_name="NistschemaSvIvListNormalizedStringPattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_pattern_nistxml_sv_iv_list_normalized_string_pattern_1_3(mode, save_output, output_format):
    r"""
    Type list/normalizedString is restricted by facet pattern with value \
    d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_13058 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_14172 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_13454 \d{1,5}_([A
    -Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_10133-1061 
    \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_10981 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_16632 \d{1,5}_([A-Z][a-
    z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_19839.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-pattern-1.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-pattern-1-3.xml",
        class_name="NistschemaSvIvListNormalizedStringPattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_pattern_nistxml_sv_iv_list_normalized_string_pattern_1_4(mode, save_output, output_format):
    r"""
    Type list/normalizedString is restricted by facet pattern with value \
    d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_13058 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_14172 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_13454 \d{1,5}_([A
    -Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_10133-1061 
    \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_10981 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_16632 \d{1,5}_([A-Z][a-
    z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_19839.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-pattern-1.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-pattern-1-4.xml",
        class_name="NistschemaSvIvListNormalizedStringPattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_pattern_nistxml_sv_iv_list_normalized_string_pattern_1_5(mode, save_output, output_format):
    r"""
    Type list/normalizedString is restricted by facet pattern with value \
    d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_13058 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_14172 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_13454 \d{1,5}_([A
    -Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_10133-1061 
    \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_10981 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_16632 \d{1,5}_([A-Z][a-
    z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_19839.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-pattern-1.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-pattern-1-5.xml",
        class_name="NistschemaSvIvListNormalizedStringPattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_length_4_nistxml_sv_iv_list_normalized_string_length_5_1(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet length with value
    10.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-length-5.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-length-5-1.xml",
        class_name="NistschemaSvIvListNormalizedStringLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_length_4_nistxml_sv_iv_list_normalized_string_length_5_2(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet length with value
    10.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-length-5.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-length-5-2.xml",
        class_name="NistschemaSvIvListNormalizedStringLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_length_4_nistxml_sv_iv_list_normalized_string_length_5_3(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet length with value
    10.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-length-5.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-length-5-3.xml",
        class_name="NistschemaSvIvListNormalizedStringLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_length_4_nistxml_sv_iv_list_normalized_string_length_5_4(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet length with value
    10.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-length-5.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-length-5-4.xml",
        class_name="NistschemaSvIvListNormalizedStringLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_length_4_nistxml_sv_iv_list_normalized_string_length_5_5(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet length with value
    10.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-length-5.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-length-5-5.xml",
        class_name="NistschemaSvIvListNormalizedStringLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_length_3_nistxml_sv_iv_list_normalized_string_length_4_1(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-length-4.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-length-4-1.xml",
        class_name="NistschemaSvIvListNormalizedStringLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_length_3_nistxml_sv_iv_list_normalized_string_length_4_2(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-length-4.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-length-4-2.xml",
        class_name="NistschemaSvIvListNormalizedStringLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_length_3_nistxml_sv_iv_list_normalized_string_length_4_3(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-length-4.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-length-4-3.xml",
        class_name="NistschemaSvIvListNormalizedStringLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_length_3_nistxml_sv_iv_list_normalized_string_length_4_4(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-length-4.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-length-4-4.xml",
        class_name="NistschemaSvIvListNormalizedStringLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_length_3_nistxml_sv_iv_list_normalized_string_length_4_5(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-length-4.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-length-4-5.xml",
        class_name="NistschemaSvIvListNormalizedStringLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_length_2_nistxml_sv_iv_list_normalized_string_length_3_1(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-length-3.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-length-3-1.xml",
        class_name="NistschemaSvIvListNormalizedStringLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_length_2_nistxml_sv_iv_list_normalized_string_length_3_2(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-length-3.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-length-3-2.xml",
        class_name="NistschemaSvIvListNormalizedStringLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_length_2_nistxml_sv_iv_list_normalized_string_length_3_3(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-length-3.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-length-3-3.xml",
        class_name="NistschemaSvIvListNormalizedStringLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_length_2_nistxml_sv_iv_list_normalized_string_length_3_4(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-length-3.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-length-3-4.xml",
        class_name="NistschemaSvIvListNormalizedStringLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_length_2_nistxml_sv_iv_list_normalized_string_length_3_5(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-length-3.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-length-3-5.xml",
        class_name="NistschemaSvIvListNormalizedStringLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_length_1_nistxml_sv_iv_list_normalized_string_length_2_1(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-length-2.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-length-2-1.xml",
        class_name="NistschemaSvIvListNormalizedStringLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_length_1_nistxml_sv_iv_list_normalized_string_length_2_2(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-length-2.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-length-2-2.xml",
        class_name="NistschemaSvIvListNormalizedStringLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_length_1_nistxml_sv_iv_list_normalized_string_length_2_3(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-length-2.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-length-2-3.xml",
        class_name="NistschemaSvIvListNormalizedStringLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_length_1_nistxml_sv_iv_list_normalized_string_length_2_4(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-length-2.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-length-2-4.xml",
        class_name="NistschemaSvIvListNormalizedStringLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_length_1_nistxml_sv_iv_list_normalized_string_length_2_5(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-length-2.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-length-2-5.xml",
        class_name="NistschemaSvIvListNormalizedStringLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_length_nistxml_sv_iv_list_normalized_string_length_1_1(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-length-1.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-length-1-1.xml",
        class_name="NistschemaSvIvListNormalizedStringLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_length_nistxml_sv_iv_list_normalized_string_length_1_2(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-length-1.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-length-1-2.xml",
        class_name="NistschemaSvIvListNormalizedStringLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_length_nistxml_sv_iv_list_normalized_string_length_1_3(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-length-1.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-length-1-3.xml",
        class_name="NistschemaSvIvListNormalizedStringLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_length_nistxml_sv_iv_list_normalized_string_length_1_4(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-length-1.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-length-1-4.xml",
        class_name="NistschemaSvIvListNormalizedStringLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_length_nistxml_sv_iv_list_normalized_string_length_1_5(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-length-1.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-length-1-5.xml",
        class_name="NistschemaSvIvListNormalizedStringLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_min_length_4_nistxml_sv_iv_list_normalized_string_min_length_5_1(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet minLength with value
    10.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-minLength-5.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-minLength-5-1.xml",
        class_name="NistschemaSvIvListNormalizedStringMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_min_length_4_nistxml_sv_iv_list_normalized_string_min_length_5_2(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet minLength with value
    10.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-minLength-5.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-minLength-5-2.xml",
        class_name="NistschemaSvIvListNormalizedStringMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_min_length_4_nistxml_sv_iv_list_normalized_string_min_length_5_3(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet minLength with value
    10.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-minLength-5.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-minLength-5-3.xml",
        class_name="NistschemaSvIvListNormalizedStringMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_min_length_4_nistxml_sv_iv_list_normalized_string_min_length_5_4(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet minLength with value
    10.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-minLength-5.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-minLength-5-4.xml",
        class_name="NistschemaSvIvListNormalizedStringMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_min_length_4_nistxml_sv_iv_list_normalized_string_min_length_5_5(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet minLength with value
    10.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-minLength-5.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-minLength-5-5.xml",
        class_name="NistschemaSvIvListNormalizedStringMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_min_length_3_nistxml_sv_iv_list_normalized_string_min_length_4_1(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet minLength with value
    8.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-minLength-4.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-minLength-4-1.xml",
        class_name="NistschemaSvIvListNormalizedStringMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_min_length_3_nistxml_sv_iv_list_normalized_string_min_length_4_2(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet minLength with value
    8.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-minLength-4.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-minLength-4-2.xml",
        class_name="NistschemaSvIvListNormalizedStringMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_min_length_3_nistxml_sv_iv_list_normalized_string_min_length_4_3(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet minLength with value
    8.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-minLength-4.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-minLength-4-3.xml",
        class_name="NistschemaSvIvListNormalizedStringMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_min_length_3_nistxml_sv_iv_list_normalized_string_min_length_4_4(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet minLength with value
    8.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-minLength-4.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-minLength-4-4.xml",
        class_name="NistschemaSvIvListNormalizedStringMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_min_length_3_nistxml_sv_iv_list_normalized_string_min_length_4_5(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet minLength with value
    8.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-minLength-4.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-minLength-4-5.xml",
        class_name="NistschemaSvIvListNormalizedStringMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_min_length_2_nistxml_sv_iv_list_normalized_string_min_length_3_1(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet minLength with value
    7.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-minLength-3.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-minLength-3-1.xml",
        class_name="NistschemaSvIvListNormalizedStringMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_min_length_2_nistxml_sv_iv_list_normalized_string_min_length_3_2(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet minLength with value
    7.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-minLength-3.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-minLength-3-2.xml",
        class_name="NistschemaSvIvListNormalizedStringMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_min_length_2_nistxml_sv_iv_list_normalized_string_min_length_3_3(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet minLength with value
    7.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-minLength-3.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-minLength-3-3.xml",
        class_name="NistschemaSvIvListNormalizedStringMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_min_length_2_nistxml_sv_iv_list_normalized_string_min_length_3_4(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet minLength with value
    7.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-minLength-3.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-minLength-3-4.xml",
        class_name="NistschemaSvIvListNormalizedStringMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_min_length_2_nistxml_sv_iv_list_normalized_string_min_length_3_5(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet minLength with value
    7.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-minLength-3.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-minLength-3-5.xml",
        class_name="NistschemaSvIvListNormalizedStringMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_min_length_1_nistxml_sv_iv_list_normalized_string_min_length_2_1(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet minLength with value
    6.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-minLength-2.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-minLength-2-1.xml",
        class_name="NistschemaSvIvListNormalizedStringMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_min_length_1_nistxml_sv_iv_list_normalized_string_min_length_2_2(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet minLength with value
    6.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-minLength-2.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-minLength-2-2.xml",
        class_name="NistschemaSvIvListNormalizedStringMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_min_length_1_nistxml_sv_iv_list_normalized_string_min_length_2_3(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet minLength with value
    6.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-minLength-2.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-minLength-2-3.xml",
        class_name="NistschemaSvIvListNormalizedStringMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_min_length_1_nistxml_sv_iv_list_normalized_string_min_length_2_4(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet minLength with value
    6.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-minLength-2.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-minLength-2-4.xml",
        class_name="NistschemaSvIvListNormalizedStringMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_min_length_1_nistxml_sv_iv_list_normalized_string_min_length_2_5(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet minLength with value
    6.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-minLength-2.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-minLength-2-5.xml",
        class_name="NistschemaSvIvListNormalizedStringMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_min_length_nistxml_sv_iv_list_normalized_string_min_length_1_1(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet minLength with value
    5.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-minLength-1.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-minLength-1-1.xml",
        class_name="NistschemaSvIvListNormalizedStringMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_min_length_nistxml_sv_iv_list_normalized_string_min_length_1_2(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet minLength with value
    5.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-minLength-1.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-minLength-1-2.xml",
        class_name="NistschemaSvIvListNormalizedStringMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_min_length_nistxml_sv_iv_list_normalized_string_min_length_1_3(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet minLength with value
    5.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-minLength-1.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-minLength-1-3.xml",
        class_name="NistschemaSvIvListNormalizedStringMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_min_length_nistxml_sv_iv_list_normalized_string_min_length_1_4(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet minLength with value
    5.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-minLength-1.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-minLength-1-4.xml",
        class_name="NistschemaSvIvListNormalizedStringMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_min_length_nistxml_sv_iv_list_normalized_string_min_length_1_5(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet minLength with value
    5.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-minLength-1.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-minLength-1-5.xml",
        class_name="NistschemaSvIvListNormalizedStringMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_max_length_4_nistxml_sv_iv_list_normalized_string_max_length_5_1(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet maxLength with value
    10.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-maxLength-5.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-maxLength-5-1.xml",
        class_name="NistschemaSvIvListNormalizedStringMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_max_length_4_nistxml_sv_iv_list_normalized_string_max_length_5_2(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet maxLength with value
    10.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-maxLength-5.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-maxLength-5-2.xml",
        class_name="NistschemaSvIvListNormalizedStringMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_max_length_4_nistxml_sv_iv_list_normalized_string_max_length_5_3(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet maxLength with value
    10.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-maxLength-5.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-maxLength-5-3.xml",
        class_name="NistschemaSvIvListNormalizedStringMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_max_length_4_nistxml_sv_iv_list_normalized_string_max_length_5_4(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet maxLength with value
    10.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-maxLength-5.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-maxLength-5-4.xml",
        class_name="NistschemaSvIvListNormalizedStringMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_max_length_4_nistxml_sv_iv_list_normalized_string_max_length_5_5(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet maxLength with value
    10.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-maxLength-5.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-maxLength-5-5.xml",
        class_name="NistschemaSvIvListNormalizedStringMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_max_length_3_nistxml_sv_iv_list_normalized_string_max_length_4_1(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet maxLength with value
    8.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-maxLength-4.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-maxLength-4-1.xml",
        class_name="NistschemaSvIvListNormalizedStringMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_max_length_3_nistxml_sv_iv_list_normalized_string_max_length_4_2(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet maxLength with value
    8.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-maxLength-4.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-maxLength-4-2.xml",
        class_name="NistschemaSvIvListNormalizedStringMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_max_length_3_nistxml_sv_iv_list_normalized_string_max_length_4_3(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet maxLength with value
    8.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-maxLength-4.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-maxLength-4-3.xml",
        class_name="NistschemaSvIvListNormalizedStringMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_max_length_3_nistxml_sv_iv_list_normalized_string_max_length_4_4(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet maxLength with value
    8.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-maxLength-4.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-maxLength-4-4.xml",
        class_name="NistschemaSvIvListNormalizedStringMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_max_length_3_nistxml_sv_iv_list_normalized_string_max_length_4_5(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet maxLength with value
    8.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-maxLength-4.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-maxLength-4-5.xml",
        class_name="NistschemaSvIvListNormalizedStringMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_max_length_2_nistxml_sv_iv_list_normalized_string_max_length_3_1(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet maxLength with value
    7.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-maxLength-3.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-maxLength-3-1.xml",
        class_name="NistschemaSvIvListNormalizedStringMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_max_length_2_nistxml_sv_iv_list_normalized_string_max_length_3_2(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet maxLength with value
    7.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-maxLength-3.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-maxLength-3-2.xml",
        class_name="NistschemaSvIvListNormalizedStringMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_max_length_2_nistxml_sv_iv_list_normalized_string_max_length_3_3(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet maxLength with value
    7.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-maxLength-3.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-maxLength-3-3.xml",
        class_name="NistschemaSvIvListNormalizedStringMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_max_length_2_nistxml_sv_iv_list_normalized_string_max_length_3_4(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet maxLength with value
    7.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-maxLength-3.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-maxLength-3-4.xml",
        class_name="NistschemaSvIvListNormalizedStringMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_max_length_2_nistxml_sv_iv_list_normalized_string_max_length_3_5(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet maxLength with value
    7.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-maxLength-3.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-maxLength-3-5.xml",
        class_name="NistschemaSvIvListNormalizedStringMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_max_length_1_nistxml_sv_iv_list_normalized_string_max_length_2_1(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet maxLength with value
    6.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-maxLength-2.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-maxLength-2-1.xml",
        class_name="NistschemaSvIvListNormalizedStringMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_max_length_1_nistxml_sv_iv_list_normalized_string_max_length_2_2(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet maxLength with value
    6.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-maxLength-2.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-maxLength-2-2.xml",
        class_name="NistschemaSvIvListNormalizedStringMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_max_length_1_nistxml_sv_iv_list_normalized_string_max_length_2_3(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet maxLength with value
    6.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-maxLength-2.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-maxLength-2-3.xml",
        class_name="NistschemaSvIvListNormalizedStringMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_max_length_1_nistxml_sv_iv_list_normalized_string_max_length_2_4(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet maxLength with value
    6.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-maxLength-2.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-maxLength-2-4.xml",
        class_name="NistschemaSvIvListNormalizedStringMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_max_length_1_nistxml_sv_iv_list_normalized_string_max_length_2_5(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet maxLength with value
    6.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-maxLength-2.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-maxLength-2-5.xml",
        class_name="NistschemaSvIvListNormalizedStringMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_max_length_nistxml_sv_iv_list_normalized_string_max_length_1_1(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet maxLength with value
    5.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-maxLength-1.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-maxLength-1-1.xml",
        class_name="NistschemaSvIvListNormalizedStringMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_max_length_nistxml_sv_iv_list_normalized_string_max_length_1_2(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet maxLength with value
    5.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-maxLength-1.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-maxLength-1-2.xml",
        class_name="NistschemaSvIvListNormalizedStringMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_max_length_nistxml_sv_iv_list_normalized_string_max_length_1_3(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet maxLength with value
    5.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-maxLength-1.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-maxLength-1-3.xml",
        class_name="NistschemaSvIvListNormalizedStringMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_max_length_nistxml_sv_iv_list_normalized_string_max_length_1_4(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet maxLength with value
    5.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-maxLength-1.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-maxLength-1-4.xml",
        class_name="NistschemaSvIvListNormalizedStringMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_normalized_string_max_length_nistxml_sv_iv_list_normalized_string_max_length_1_5(mode, save_output, output_format):
    """
    Type list/normalizedString is restricted by facet maxLength with value
    5.
    """
    assert_bindings(
        schema="nistData/list/normalizedString/Schema+Instance/NISTSchema-SV-IV-list-normalizedString-maxLength-1.xsd",
        instance="nistData/list/normalizedString/Schema+Instance/NISTXML-SV-IV-list-normalizedString-maxLength-1-5.xml",
        class_name="NistschemaSvIvListNormalizedStringMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_white_space_nistxml_sv_iv_list_string_white_space_1_1(mode, save_output, output_format):
    """
    Type list/string is restricted by facet whiteSpace with value
    collapse.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-whiteSpace-1.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-whiteSpace-1-1.xml",
        class_name="NistschemaSvIvListStringWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_white_space_nistxml_sv_iv_list_string_white_space_1_2(mode, save_output, output_format):
    """
    Type list/string is restricted by facet whiteSpace with value
    collapse.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-whiteSpace-1.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-whiteSpace-1-2.xml",
        class_name="NistschemaSvIvListStringWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_white_space_nistxml_sv_iv_list_string_white_space_1_3(mode, save_output, output_format):
    """
    Type list/string is restricted by facet whiteSpace with value
    collapse.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-whiteSpace-1.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-whiteSpace-1-3.xml",
        class_name="NistschemaSvIvListStringWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_white_space_nistxml_sv_iv_list_string_white_space_1_4(mode, save_output, output_format):
    """
    Type list/string is restricted by facet whiteSpace with value
    collapse.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-whiteSpace-1.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-whiteSpace-1-4.xml",
        class_name="NistschemaSvIvListStringWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_white_space_nistxml_sv_iv_list_string_white_space_1_5(mode, save_output, output_format):
    """
    Type list/string is restricted by facet whiteSpace with value
    collapse.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-whiteSpace-1.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-whiteSpace-1-5.xml",
        class_name="NistschemaSvIvListStringWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_enumeration_4_nistxml_sv_iv_list_string_enumeration_5_1(mode, save_output, output_format):
    """
    Type list/string is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-enumeration-5.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-enumeration-5-1.xml",
        class_name="NistschemaSvIvListStringEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_enumeration_4_nistxml_sv_iv_list_string_enumeration_5_2(mode, save_output, output_format):
    """
    Type list/string is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-enumeration-5.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-enumeration-5-2.xml",
        class_name="NistschemaSvIvListStringEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_enumeration_4_nistxml_sv_iv_list_string_enumeration_5_3(mode, save_output, output_format):
    """
    Type list/string is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-enumeration-5.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-enumeration-5-3.xml",
        class_name="NistschemaSvIvListStringEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_enumeration_4_nistxml_sv_iv_list_string_enumeration_5_4(mode, save_output, output_format):
    """
    Type list/string is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-enumeration-5.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-enumeration-5-4.xml",
        class_name="NistschemaSvIvListStringEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_enumeration_4_nistxml_sv_iv_list_string_enumeration_5_5(mode, save_output, output_format):
    """
    Type list/string is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-enumeration-5.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-enumeration-5-5.xml",
        class_name="NistschemaSvIvListStringEnumeration5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_enumeration_3_nistxml_sv_iv_list_string_enumeration_4_1(mode, save_output, output_format):
    """
    Type list/string is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-enumeration-4.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-enumeration-4-1.xml",
        class_name="NistschemaSvIvListStringEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_enumeration_3_nistxml_sv_iv_list_string_enumeration_4_2(mode, save_output, output_format):
    """
    Type list/string is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-enumeration-4.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-enumeration-4-2.xml",
        class_name="NistschemaSvIvListStringEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_enumeration_3_nistxml_sv_iv_list_string_enumeration_4_3(mode, save_output, output_format):
    """
    Type list/string is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-enumeration-4.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-enumeration-4-3.xml",
        class_name="NistschemaSvIvListStringEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_enumeration_3_nistxml_sv_iv_list_string_enumeration_4_4(mode, save_output, output_format):
    """
    Type list/string is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-enumeration-4.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-enumeration-4-4.xml",
        class_name="NistschemaSvIvListStringEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_enumeration_3_nistxml_sv_iv_list_string_enumeration_4_5(mode, save_output, output_format):
    """
    Type list/string is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-enumeration-4.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-enumeration-4-5.xml",
        class_name="NistschemaSvIvListStringEnumeration4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_enumeration_2_nistxml_sv_iv_list_string_enumeration_3_1(mode, save_output, output_format):
    """
    Type list/string is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-enumeration-3.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-enumeration-3-1.xml",
        class_name="NistschemaSvIvListStringEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_enumeration_2_nistxml_sv_iv_list_string_enumeration_3_2(mode, save_output, output_format):
    """
    Type list/string is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-enumeration-3.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-enumeration-3-2.xml",
        class_name="NistschemaSvIvListStringEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_enumeration_2_nistxml_sv_iv_list_string_enumeration_3_3(mode, save_output, output_format):
    """
    Type list/string is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-enumeration-3.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-enumeration-3-3.xml",
        class_name="NistschemaSvIvListStringEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_enumeration_2_nistxml_sv_iv_list_string_enumeration_3_4(mode, save_output, output_format):
    """
    Type list/string is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-enumeration-3.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-enumeration-3-4.xml",
        class_name="NistschemaSvIvListStringEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_enumeration_2_nistxml_sv_iv_list_string_enumeration_3_5(mode, save_output, output_format):
    """
    Type list/string is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-enumeration-3.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-enumeration-3-5.xml",
        class_name="NistschemaSvIvListStringEnumeration3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_enumeration_1_nistxml_sv_iv_list_string_enumeration_2_1(mode, save_output, output_format):
    """
    Type list/string is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-enumeration-2.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-enumeration-2-1.xml",
        class_name="NistschemaSvIvListStringEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_enumeration_1_nistxml_sv_iv_list_string_enumeration_2_2(mode, save_output, output_format):
    """
    Type list/string is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-enumeration-2.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-enumeration-2-2.xml",
        class_name="NistschemaSvIvListStringEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_enumeration_1_nistxml_sv_iv_list_string_enumeration_2_3(mode, save_output, output_format):
    """
    Type list/string is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-enumeration-2.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-enumeration-2-3.xml",
        class_name="NistschemaSvIvListStringEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_enumeration_1_nistxml_sv_iv_list_string_enumeration_2_4(mode, save_output, output_format):
    """
    Type list/string is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-enumeration-2.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-enumeration-2-4.xml",
        class_name="NistschemaSvIvListStringEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_enumeration_1_nistxml_sv_iv_list_string_enumeration_2_5(mode, save_output, output_format):
    """
    Type list/string is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-enumeration-2.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-enumeration-2-5.xml",
        class_name="NistschemaSvIvListStringEnumeration2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_enumeration_nistxml_sv_iv_list_string_enumeration_1_1(mode, save_output, output_format):
    """
    Type list/string is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-enumeration-1.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-enumeration-1-1.xml",
        class_name="NistschemaSvIvListStringEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_enumeration_nistxml_sv_iv_list_string_enumeration_1_2(mode, save_output, output_format):
    """
    Type list/string is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-enumeration-1.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-enumeration-1-2.xml",
        class_name="NistschemaSvIvListStringEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_enumeration_nistxml_sv_iv_list_string_enumeration_1_3(mode, save_output, output_format):
    """
    Type list/string is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-enumeration-1.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-enumeration-1-3.xml",
        class_name="NistschemaSvIvListStringEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_enumeration_nistxml_sv_iv_list_string_enumeration_1_4(mode, save_output, output_format):
    """
    Type list/string is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-enumeration-1.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-enumeration-1-4.xml",
        class_name="NistschemaSvIvListStringEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_enumeration_nistxml_sv_iv_list_string_enumeration_1_5(mode, save_output, output_format):
    """
    Type list/string is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-enumeration-1.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-enumeration-1-5.xml",
        class_name="NistschemaSvIvListStringEnumeration1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_pattern_4_nistxml_sv_iv_list_string_pattern_5_1(mode, save_output, output_format):
    r"""
    Type list/string is restricted by facet pattern with value \d{1,5}_([A
    -Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_17435-1843 
    \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_16376 \d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-
    z]{1,20}_){1},_[A-Z]{2}_11348 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_14973 \d{1,5}_([A
    -Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_16518-1410 
    \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_10254-1649 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-
    z]{1,20}_){1},_[A-Z]{2}_17642 \d{1,5}_([A-Z][a-
    z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_18742 \d{1,5}_([A
    -Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_17310-1594.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-pattern-5.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-pattern-5-1.xml",
        class_name="NistschemaSvIvListStringPattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_pattern_4_nistxml_sv_iv_list_string_pattern_5_2(mode, save_output, output_format):
    r"""
    Type list/string is restricted by facet pattern with value \d{1,5}_([A
    -Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_17435-1843 
    \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_16376 \d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-
    z]{1,20}_){1},_[A-Z]{2}_11348 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_14973 \d{1,5}_([A
    -Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_16518-1410 
    \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_10254-1649 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-
    z]{1,20}_){1},_[A-Z]{2}_17642 \d{1,5}_([A-Z][a-
    z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_18742 \d{1,5}_([A
    -Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_17310-1594.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-pattern-5.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-pattern-5-2.xml",
        class_name="NistschemaSvIvListStringPattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_pattern_4_nistxml_sv_iv_list_string_pattern_5_3(mode, save_output, output_format):
    r"""
    Type list/string is restricted by facet pattern with value \d{1,5}_([A
    -Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_17435-1843 
    \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_16376 \d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-
    z]{1,20}_){1},_[A-Z]{2}_11348 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_14973 \d{1,5}_([A
    -Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_16518-1410 
    \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_10254-1649 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-
    z]{1,20}_){1},_[A-Z]{2}_17642 \d{1,5}_([A-Z][a-
    z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_18742 \d{1,5}_([A
    -Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_17310-1594.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-pattern-5.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-pattern-5-3.xml",
        class_name="NistschemaSvIvListStringPattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_pattern_4_nistxml_sv_iv_list_string_pattern_5_4(mode, save_output, output_format):
    r"""
    Type list/string is restricted by facet pattern with value \d{1,5}_([A
    -Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_17435-1843 
    \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_16376 \d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-
    z]{1,20}_){1},_[A-Z]{2}_11348 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_14973 \d{1,5}_([A
    -Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_16518-1410 
    \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_10254-1649 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-
    z]{1,20}_){1},_[A-Z]{2}_17642 \d{1,5}_([A-Z][a-
    z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_18742 \d{1,5}_([A
    -Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_17310-1594.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-pattern-5.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-pattern-5-4.xml",
        class_name="NistschemaSvIvListStringPattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_pattern_4_nistxml_sv_iv_list_string_pattern_5_5(mode, save_output, output_format):
    r"""
    Type list/string is restricted by facet pattern with value \d{1,5}_([A
    -Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_17435-1843 
    \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_16376 \d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-
    z]{1,20}_){1},_[A-Z]{2}_11348 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_14973 \d{1,5}_([A
    -Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_16518-1410 
    \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_10254-1649 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-
    z]{1,20}_){1},_[A-Z]{2}_17642 \d{1,5}_([A-Z][a-
    z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_18742 \d{1,5}_([A
    -Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_17310-1594.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-pattern-5.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-pattern-5-5.xml",
        class_name="NistschemaSvIvListStringPattern5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_pattern_3_nistxml_sv_iv_list_string_pattern_4_1(mode, save_output, output_format):
    r"""
    Type list/string is restricted by facet pattern with value \d{1,5}_([A
    -Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_15352 \d{1,
    5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_18423-1985 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_15520-1083 \d{1,5}_([A-Z][a-
    z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_18786-1596 \d{1,5
    }_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_12834-
    1343.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-pattern-4.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-pattern-4-1.xml",
        class_name="NistschemaSvIvListStringPattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_pattern_3_nistxml_sv_iv_list_string_pattern_4_2(mode, save_output, output_format):
    r"""
    Type list/string is restricted by facet pattern with value \d{1,5}_([A
    -Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_15352 \d{1,
    5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_18423-1985 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_15520-1083 \d{1,5}_([A-Z][a-
    z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_18786-1596 \d{1,5
    }_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_12834-
    1343.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-pattern-4.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-pattern-4-2.xml",
        class_name="NistschemaSvIvListStringPattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_pattern_3_nistxml_sv_iv_list_string_pattern_4_3(mode, save_output, output_format):
    r"""
    Type list/string is restricted by facet pattern with value \d{1,5}_([A
    -Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_15352 \d{1,
    5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_18423-1985 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_15520-1083 \d{1,5}_([A-Z][a-
    z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_18786-1596 \d{1,5
    }_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_12834-
    1343.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-pattern-4.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-pattern-4-3.xml",
        class_name="NistschemaSvIvListStringPattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_pattern_3_nistxml_sv_iv_list_string_pattern_4_4(mode, save_output, output_format):
    r"""
    Type list/string is restricted by facet pattern with value \d{1,5}_([A
    -Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_15352 \d{1,
    5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_18423-1985 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_15520-1083 \d{1,5}_([A-Z][a-
    z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_18786-1596 \d{1,5
    }_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_12834-
    1343.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-pattern-4.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-pattern-4-4.xml",
        class_name="NistschemaSvIvListStringPattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_pattern_3_nistxml_sv_iv_list_string_pattern_4_5(mode, save_output, output_format):
    r"""
    Type list/string is restricted by facet pattern with value \d{1,5}_([A
    -Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_15352 \d{1,
    5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_18423-1985 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_15520-1083 \d{1,5}_([A-Z][a-
    z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_18786-1596 \d{1,5
    }_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_12834-
    1343.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-pattern-4.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-pattern-4-5.xml",
        class_name="NistschemaSvIvListStringPattern4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_pattern_2_nistxml_sv_iv_list_string_pattern_3_1(mode, save_output, output_format):
    r"""
    Type list/string is restricted by facet pattern with value \d{1,5}_([A
    -Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_11654-1789 
    \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_19111-1980 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_15774-1852 \d{1,5}_([A-Z][a-
    z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_18248-1891 \d{1,5
    }_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_15314.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-pattern-3.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-pattern-3-1.xml",
        class_name="NistschemaSvIvListStringPattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_pattern_2_nistxml_sv_iv_list_string_pattern_3_2(mode, save_output, output_format):
    r"""
    Type list/string is restricted by facet pattern with value \d{1,5}_([A
    -Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_11654-1789 
    \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_19111-1980 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_15774-1852 \d{1,5}_([A-Z][a-
    z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_18248-1891 \d{1,5
    }_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_15314.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-pattern-3.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-pattern-3-2.xml",
        class_name="NistschemaSvIvListStringPattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_pattern_2_nistxml_sv_iv_list_string_pattern_3_3(mode, save_output, output_format):
    r"""
    Type list/string is restricted by facet pattern with value \d{1,5}_([A
    -Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_11654-1789 
    \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_19111-1980 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_15774-1852 \d{1,5}_([A-Z][a-
    z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_18248-1891 \d{1,5
    }_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_15314.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-pattern-3.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-pattern-3-3.xml",
        class_name="NistschemaSvIvListStringPattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_pattern_2_nistxml_sv_iv_list_string_pattern_3_4(mode, save_output, output_format):
    r"""
    Type list/string is restricted by facet pattern with value \d{1,5}_([A
    -Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_11654-1789 
    \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_19111-1980 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_15774-1852 \d{1,5}_([A-Z][a-
    z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_18248-1891 \d{1,5
    }_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_15314.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-pattern-3.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-pattern-3-4.xml",
        class_name="NistschemaSvIvListStringPattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_pattern_2_nistxml_sv_iv_list_string_pattern_3_5(mode, save_output, output_format):
    r"""
    Type list/string is restricted by facet pattern with value \d{1,5}_([A
    -Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_11654-1789 
    \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_19111-1980 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_15774-1852 \d{1,5}_([A-Z][a-
    z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_18248-1891 \d{1,5
    }_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_15314.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-pattern-3.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-pattern-3-5.xml",
        class_name="NistschemaSvIvListStringPattern3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_pattern_1_nistxml_sv_iv_list_string_pattern_2_1(mode, save_output, output_format):
    r"""
    Type list/string is restricted by facet pattern with value \d{1,5}_([A
    -Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_11551-1386 
    \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_15792-1475 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_16933 \d{1,5}_([A-Z][a-
    z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_10446 \d{1,5}_([A
    -Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_13824 \d{1,
    5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_10173-1992 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-
    z]{1,20}_){3},_[A-Z]{2}_10148-1029.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-pattern-2.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-pattern-2-1.xml",
        class_name="NistschemaSvIvListStringPattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_pattern_1_nistxml_sv_iv_list_string_pattern_2_2(mode, save_output, output_format):
    r"""
    Type list/string is restricted by facet pattern with value \d{1,5}_([A
    -Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_11551-1386 
    \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_15792-1475 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_16933 \d{1,5}_([A-Z][a-
    z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_10446 \d{1,5}_([A
    -Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_13824 \d{1,
    5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_10173-1992 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-
    z]{1,20}_){3},_[A-Z]{2}_10148-1029.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-pattern-2.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-pattern-2-2.xml",
        class_name="NistschemaSvIvListStringPattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_pattern_1_nistxml_sv_iv_list_string_pattern_2_3(mode, save_output, output_format):
    r"""
    Type list/string is restricted by facet pattern with value \d{1,5}_([A
    -Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_11551-1386 
    \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_15792-1475 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_16933 \d{1,5}_([A-Z][a-
    z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_10446 \d{1,5}_([A
    -Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_13824 \d{1,
    5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_10173-1992 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-
    z]{1,20}_){3},_[A-Z]{2}_10148-1029.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-pattern-2.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-pattern-2-3.xml",
        class_name="NistschemaSvIvListStringPattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_pattern_1_nistxml_sv_iv_list_string_pattern_2_4(mode, save_output, output_format):
    r"""
    Type list/string is restricted by facet pattern with value \d{1,5}_([A
    -Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_11551-1386 
    \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_15792-1475 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_16933 \d{1,5}_([A-Z][a-
    z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_10446 \d{1,5}_([A
    -Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_13824 \d{1,
    5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_10173-1992 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-
    z]{1,20}_){3},_[A-Z]{2}_10148-1029.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-pattern-2.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-pattern-2-4.xml",
        class_name="NistschemaSvIvListStringPattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_pattern_1_nistxml_sv_iv_list_string_pattern_2_5(mode, save_output, output_format):
    r"""
    Type list/string is restricted by facet pattern with value \d{1,5}_([A
    -Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_11551-1386 
    \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-
    Z]{2}_15792-1475 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_16933 \d{1,5}_([A-Z][a-
    z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_10446 \d{1,5}_([A
    -Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_13824 \d{1,
    5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_10173-1992 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-
    z]{1,20}_){3},_[A-Z]{2}_10148-1029.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-pattern-2.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-pattern-2-5.xml",
        class_name="NistschemaSvIvListStringPattern2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_pattern_nistxml_sv_iv_list_string_pattern_1_1(mode, save_output, output_format):
    r"""
    Type list/string is restricted by facet pattern with value \d{1,5}_([A
    -Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_19751 \d{1,
    5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_11837-1623 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_14030 \d{1,5}_([A-Z][a-
    z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_13653-1327 \d{1,5
    }_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_18424-
    1338 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_19584-1412 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-
    z]{1,20}_){3},_[A-Z]{2}_11267 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_16578 \d{1,5}_([A
    -Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_14818-1281.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-pattern-1.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-pattern-1-1.xml",
        class_name="NistschemaSvIvListStringPattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_pattern_nistxml_sv_iv_list_string_pattern_1_2(mode, save_output, output_format):
    r"""
    Type list/string is restricted by facet pattern with value \d{1,5}_([A
    -Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_19751 \d{1,
    5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_11837-1623 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_14030 \d{1,5}_([A-Z][a-
    z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_13653-1327 \d{1,5
    }_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_18424-
    1338 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_19584-1412 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-
    z]{1,20}_){3},_[A-Z]{2}_11267 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_16578 \d{1,5}_([A
    -Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_14818-1281.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-pattern-1.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-pattern-1-2.xml",
        class_name="NistschemaSvIvListStringPattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_pattern_nistxml_sv_iv_list_string_pattern_1_3(mode, save_output, output_format):
    r"""
    Type list/string is restricted by facet pattern with value \d{1,5}_([A
    -Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_19751 \d{1,
    5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_11837-1623 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_14030 \d{1,5}_([A-Z][a-
    z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_13653-1327 \d{1,5
    }_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_18424-
    1338 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_19584-1412 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-
    z]{1,20}_){3},_[A-Z]{2}_11267 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_16578 \d{1,5}_([A
    -Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_14818-1281.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-pattern-1.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-pattern-1-3.xml",
        class_name="NistschemaSvIvListStringPattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_pattern_nistxml_sv_iv_list_string_pattern_1_4(mode, save_output, output_format):
    r"""
    Type list/string is restricted by facet pattern with value \d{1,5}_([A
    -Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_19751 \d{1,
    5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_11837-1623 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_14030 \d{1,5}_([A-Z][a-
    z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_13653-1327 \d{1,5
    }_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_18424-
    1338 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_19584-1412 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-
    z]{1,20}_){3},_[A-Z]{2}_11267 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_16578 \d{1,5}_([A
    -Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_14818-1281.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-pattern-1.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-pattern-1-4.xml",
        class_name="NistschemaSvIvListStringPattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_pattern_nistxml_sv_iv_list_string_pattern_1_5(mode, save_output, output_format):
    r"""
    Type list/string is restricted by facet pattern with value \d{1,5}_([A
    -Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_19751 \d{1,
    5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-
    Z]{2}_11837-1623 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-
    z]{1,20}_){2},_[A-Z]{2}_14030 \d{1,5}_([A-Z][a-
    z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_13653-1327 \d{1,5
    }_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_18424-
    1338 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-
    Z]{2}_19584-1412 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-
    z]{1,20}_){3},_[A-Z]{2}_11267 \d{1,5}_([A-Z][a-
    z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_16578 \d{1,5}_([A
    -Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_14818-1281.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-pattern-1.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-pattern-1-5.xml",
        class_name="NistschemaSvIvListStringPattern1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_length_4_nistxml_sv_iv_list_string_length_5_1(mode, save_output, output_format):
    """
    Type list/string is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-length-5.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-length-5-1.xml",
        class_name="NistschemaSvIvListStringLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_length_4_nistxml_sv_iv_list_string_length_5_2(mode, save_output, output_format):
    """
    Type list/string is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-length-5.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-length-5-2.xml",
        class_name="NistschemaSvIvListStringLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_length_4_nistxml_sv_iv_list_string_length_5_3(mode, save_output, output_format):
    """
    Type list/string is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-length-5.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-length-5-3.xml",
        class_name="NistschemaSvIvListStringLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_length_4_nistxml_sv_iv_list_string_length_5_4(mode, save_output, output_format):
    """
    Type list/string is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-length-5.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-length-5-4.xml",
        class_name="NistschemaSvIvListStringLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_length_4_nistxml_sv_iv_list_string_length_5_5(mode, save_output, output_format):
    """
    Type list/string is restricted by facet length with value 10.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-length-5.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-length-5-5.xml",
        class_name="NistschemaSvIvListStringLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_length_3_nistxml_sv_iv_list_string_length_4_1(mode, save_output, output_format):
    """
    Type list/string is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-length-4.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-length-4-1.xml",
        class_name="NistschemaSvIvListStringLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_length_3_nistxml_sv_iv_list_string_length_4_2(mode, save_output, output_format):
    """
    Type list/string is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-length-4.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-length-4-2.xml",
        class_name="NistschemaSvIvListStringLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_length_3_nistxml_sv_iv_list_string_length_4_3(mode, save_output, output_format):
    """
    Type list/string is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-length-4.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-length-4-3.xml",
        class_name="NistschemaSvIvListStringLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_length_3_nistxml_sv_iv_list_string_length_4_4(mode, save_output, output_format):
    """
    Type list/string is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-length-4.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-length-4-4.xml",
        class_name="NistschemaSvIvListStringLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_length_3_nistxml_sv_iv_list_string_length_4_5(mode, save_output, output_format):
    """
    Type list/string is restricted by facet length with value 8.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-length-4.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-length-4-5.xml",
        class_name="NistschemaSvIvListStringLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_length_2_nistxml_sv_iv_list_string_length_3_1(mode, save_output, output_format):
    """
    Type list/string is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-length-3.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-length-3-1.xml",
        class_name="NistschemaSvIvListStringLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_length_2_nistxml_sv_iv_list_string_length_3_2(mode, save_output, output_format):
    """
    Type list/string is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-length-3.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-length-3-2.xml",
        class_name="NistschemaSvIvListStringLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_length_2_nistxml_sv_iv_list_string_length_3_3(mode, save_output, output_format):
    """
    Type list/string is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-length-3.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-length-3-3.xml",
        class_name="NistschemaSvIvListStringLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_length_2_nistxml_sv_iv_list_string_length_3_4(mode, save_output, output_format):
    """
    Type list/string is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-length-3.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-length-3-4.xml",
        class_name="NistschemaSvIvListStringLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_length_2_nistxml_sv_iv_list_string_length_3_5(mode, save_output, output_format):
    """
    Type list/string is restricted by facet length with value 7.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-length-3.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-length-3-5.xml",
        class_name="NistschemaSvIvListStringLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_length_1_nistxml_sv_iv_list_string_length_2_1(mode, save_output, output_format):
    """
    Type list/string is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-length-2.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-length-2-1.xml",
        class_name="NistschemaSvIvListStringLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_length_1_nistxml_sv_iv_list_string_length_2_2(mode, save_output, output_format):
    """
    Type list/string is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-length-2.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-length-2-2.xml",
        class_name="NistschemaSvIvListStringLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_length_1_nistxml_sv_iv_list_string_length_2_3(mode, save_output, output_format):
    """
    Type list/string is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-length-2.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-length-2-3.xml",
        class_name="NistschemaSvIvListStringLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_length_1_nistxml_sv_iv_list_string_length_2_4(mode, save_output, output_format):
    """
    Type list/string is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-length-2.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-length-2-4.xml",
        class_name="NistschemaSvIvListStringLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_length_1_nistxml_sv_iv_list_string_length_2_5(mode, save_output, output_format):
    """
    Type list/string is restricted by facet length with value 6.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-length-2.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-length-2-5.xml",
        class_name="NistschemaSvIvListStringLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_length_nistxml_sv_iv_list_string_length_1_1(mode, save_output, output_format):
    """
    Type list/string is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-length-1.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-length-1-1.xml",
        class_name="NistschemaSvIvListStringLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_length_nistxml_sv_iv_list_string_length_1_2(mode, save_output, output_format):
    """
    Type list/string is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-length-1.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-length-1-2.xml",
        class_name="NistschemaSvIvListStringLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_length_nistxml_sv_iv_list_string_length_1_3(mode, save_output, output_format):
    """
    Type list/string is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-length-1.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-length-1-3.xml",
        class_name="NistschemaSvIvListStringLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_length_nistxml_sv_iv_list_string_length_1_4(mode, save_output, output_format):
    """
    Type list/string is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-length-1.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-length-1-4.xml",
        class_name="NistschemaSvIvListStringLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_length_nistxml_sv_iv_list_string_length_1_5(mode, save_output, output_format):
    """
    Type list/string is restricted by facet length with value 5.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-length-1.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-length-1-5.xml",
        class_name="NistschemaSvIvListStringLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_min_length_4_nistxml_sv_iv_list_string_min_length_5_1(mode, save_output, output_format):
    """
    Type list/string is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-minLength-5.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-minLength-5-1.xml",
        class_name="NistschemaSvIvListStringMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_min_length_4_nistxml_sv_iv_list_string_min_length_5_2(mode, save_output, output_format):
    """
    Type list/string is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-minLength-5.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-minLength-5-2.xml",
        class_name="NistschemaSvIvListStringMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_min_length_4_nistxml_sv_iv_list_string_min_length_5_3(mode, save_output, output_format):
    """
    Type list/string is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-minLength-5.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-minLength-5-3.xml",
        class_name="NistschemaSvIvListStringMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_min_length_4_nistxml_sv_iv_list_string_min_length_5_4(mode, save_output, output_format):
    """
    Type list/string is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-minLength-5.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-minLength-5-4.xml",
        class_name="NistschemaSvIvListStringMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_min_length_4_nistxml_sv_iv_list_string_min_length_5_5(mode, save_output, output_format):
    """
    Type list/string is restricted by facet minLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-minLength-5.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-minLength-5-5.xml",
        class_name="NistschemaSvIvListStringMinLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_min_length_3_nistxml_sv_iv_list_string_min_length_4_1(mode, save_output, output_format):
    """
    Type list/string is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-minLength-4.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-minLength-4-1.xml",
        class_name="NistschemaSvIvListStringMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_min_length_3_nistxml_sv_iv_list_string_min_length_4_2(mode, save_output, output_format):
    """
    Type list/string is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-minLength-4.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-minLength-4-2.xml",
        class_name="NistschemaSvIvListStringMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_min_length_3_nistxml_sv_iv_list_string_min_length_4_3(mode, save_output, output_format):
    """
    Type list/string is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-minLength-4.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-minLength-4-3.xml",
        class_name="NistschemaSvIvListStringMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_min_length_3_nistxml_sv_iv_list_string_min_length_4_4(mode, save_output, output_format):
    """
    Type list/string is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-minLength-4.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-minLength-4-4.xml",
        class_name="NistschemaSvIvListStringMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_min_length_3_nistxml_sv_iv_list_string_min_length_4_5(mode, save_output, output_format):
    """
    Type list/string is restricted by facet minLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-minLength-4.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-minLength-4-5.xml",
        class_name="NistschemaSvIvListStringMinLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_min_length_2_nistxml_sv_iv_list_string_min_length_3_1(mode, save_output, output_format):
    """
    Type list/string is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-minLength-3.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-minLength-3-1.xml",
        class_name="NistschemaSvIvListStringMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_min_length_2_nistxml_sv_iv_list_string_min_length_3_2(mode, save_output, output_format):
    """
    Type list/string is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-minLength-3.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-minLength-3-2.xml",
        class_name="NistschemaSvIvListStringMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_min_length_2_nistxml_sv_iv_list_string_min_length_3_3(mode, save_output, output_format):
    """
    Type list/string is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-minLength-3.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-minLength-3-3.xml",
        class_name="NistschemaSvIvListStringMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_min_length_2_nistxml_sv_iv_list_string_min_length_3_4(mode, save_output, output_format):
    """
    Type list/string is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-minLength-3.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-minLength-3-4.xml",
        class_name="NistschemaSvIvListStringMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_min_length_2_nistxml_sv_iv_list_string_min_length_3_5(mode, save_output, output_format):
    """
    Type list/string is restricted by facet minLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-minLength-3.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-minLength-3-5.xml",
        class_name="NistschemaSvIvListStringMinLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_min_length_1_nistxml_sv_iv_list_string_min_length_2_1(mode, save_output, output_format):
    """
    Type list/string is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-minLength-2.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-minLength-2-1.xml",
        class_name="NistschemaSvIvListStringMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_min_length_1_nistxml_sv_iv_list_string_min_length_2_2(mode, save_output, output_format):
    """
    Type list/string is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-minLength-2.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-minLength-2-2.xml",
        class_name="NistschemaSvIvListStringMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_min_length_1_nistxml_sv_iv_list_string_min_length_2_3(mode, save_output, output_format):
    """
    Type list/string is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-minLength-2.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-minLength-2-3.xml",
        class_name="NistschemaSvIvListStringMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_min_length_1_nistxml_sv_iv_list_string_min_length_2_4(mode, save_output, output_format):
    """
    Type list/string is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-minLength-2.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-minLength-2-4.xml",
        class_name="NistschemaSvIvListStringMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_min_length_1_nistxml_sv_iv_list_string_min_length_2_5(mode, save_output, output_format):
    """
    Type list/string is restricted by facet minLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-minLength-2.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-minLength-2-5.xml",
        class_name="NistschemaSvIvListStringMinLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_min_length_nistxml_sv_iv_list_string_min_length_1_1(mode, save_output, output_format):
    """
    Type list/string is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-minLength-1.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-minLength-1-1.xml",
        class_name="NistschemaSvIvListStringMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_min_length_nistxml_sv_iv_list_string_min_length_1_2(mode, save_output, output_format):
    """
    Type list/string is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-minLength-1.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-minLength-1-2.xml",
        class_name="NistschemaSvIvListStringMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_min_length_nistxml_sv_iv_list_string_min_length_1_3(mode, save_output, output_format):
    """
    Type list/string is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-minLength-1.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-minLength-1-3.xml",
        class_name="NistschemaSvIvListStringMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_min_length_nistxml_sv_iv_list_string_min_length_1_4(mode, save_output, output_format):
    """
    Type list/string is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-minLength-1.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-minLength-1-4.xml",
        class_name="NistschemaSvIvListStringMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_min_length_nistxml_sv_iv_list_string_min_length_1_5(mode, save_output, output_format):
    """
    Type list/string is restricted by facet minLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-minLength-1.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-minLength-1-5.xml",
        class_name="NistschemaSvIvListStringMinLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_max_length_4_nistxml_sv_iv_list_string_max_length_5_1(mode, save_output, output_format):
    """
    Type list/string is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-maxLength-5.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-maxLength-5-1.xml",
        class_name="NistschemaSvIvListStringMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_max_length_4_nistxml_sv_iv_list_string_max_length_5_2(mode, save_output, output_format):
    """
    Type list/string is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-maxLength-5.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-maxLength-5-2.xml",
        class_name="NistschemaSvIvListStringMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_max_length_4_nistxml_sv_iv_list_string_max_length_5_3(mode, save_output, output_format):
    """
    Type list/string is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-maxLength-5.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-maxLength-5-3.xml",
        class_name="NistschemaSvIvListStringMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_max_length_4_nistxml_sv_iv_list_string_max_length_5_4(mode, save_output, output_format):
    """
    Type list/string is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-maxLength-5.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-maxLength-5-4.xml",
        class_name="NistschemaSvIvListStringMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_max_length_4_nistxml_sv_iv_list_string_max_length_5_5(mode, save_output, output_format):
    """
    Type list/string is restricted by facet maxLength with value 10.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-maxLength-5.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-maxLength-5-5.xml",
        class_name="NistschemaSvIvListStringMaxLength5",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_max_length_3_nistxml_sv_iv_list_string_max_length_4_1(mode, save_output, output_format):
    """
    Type list/string is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-maxLength-4.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-maxLength-4-1.xml",
        class_name="NistschemaSvIvListStringMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_max_length_3_nistxml_sv_iv_list_string_max_length_4_2(mode, save_output, output_format):
    """
    Type list/string is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-maxLength-4.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-maxLength-4-2.xml",
        class_name="NistschemaSvIvListStringMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_max_length_3_nistxml_sv_iv_list_string_max_length_4_3(mode, save_output, output_format):
    """
    Type list/string is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-maxLength-4.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-maxLength-4-3.xml",
        class_name="NistschemaSvIvListStringMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_max_length_3_nistxml_sv_iv_list_string_max_length_4_4(mode, save_output, output_format):
    """
    Type list/string is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-maxLength-4.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-maxLength-4-4.xml",
        class_name="NistschemaSvIvListStringMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_max_length_3_nistxml_sv_iv_list_string_max_length_4_5(mode, save_output, output_format):
    """
    Type list/string is restricted by facet maxLength with value 8.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-maxLength-4.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-maxLength-4-5.xml",
        class_name="NistschemaSvIvListStringMaxLength4",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_max_length_2_nistxml_sv_iv_list_string_max_length_3_1(mode, save_output, output_format):
    """
    Type list/string is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-maxLength-3.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-maxLength-3-1.xml",
        class_name="NistschemaSvIvListStringMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_max_length_2_nistxml_sv_iv_list_string_max_length_3_2(mode, save_output, output_format):
    """
    Type list/string is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-maxLength-3.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-maxLength-3-2.xml",
        class_name="NistschemaSvIvListStringMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_max_length_2_nistxml_sv_iv_list_string_max_length_3_3(mode, save_output, output_format):
    """
    Type list/string is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-maxLength-3.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-maxLength-3-3.xml",
        class_name="NistschemaSvIvListStringMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_max_length_2_nistxml_sv_iv_list_string_max_length_3_4(mode, save_output, output_format):
    """
    Type list/string is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-maxLength-3.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-maxLength-3-4.xml",
        class_name="NistschemaSvIvListStringMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_max_length_2_nistxml_sv_iv_list_string_max_length_3_5(mode, save_output, output_format):
    """
    Type list/string is restricted by facet maxLength with value 7.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-maxLength-3.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-maxLength-3-5.xml",
        class_name="NistschemaSvIvListStringMaxLength3",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_max_length_1_nistxml_sv_iv_list_string_max_length_2_1(mode, save_output, output_format):
    """
    Type list/string is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-maxLength-2.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-maxLength-2-1.xml",
        class_name="NistschemaSvIvListStringMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_max_length_1_nistxml_sv_iv_list_string_max_length_2_2(mode, save_output, output_format):
    """
    Type list/string is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-maxLength-2.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-maxLength-2-2.xml",
        class_name="NistschemaSvIvListStringMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_max_length_1_nistxml_sv_iv_list_string_max_length_2_3(mode, save_output, output_format):
    """
    Type list/string is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-maxLength-2.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-maxLength-2-3.xml",
        class_name="NistschemaSvIvListStringMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_max_length_1_nistxml_sv_iv_list_string_max_length_2_4(mode, save_output, output_format):
    """
    Type list/string is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-maxLength-2.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-maxLength-2-4.xml",
        class_name="NistschemaSvIvListStringMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_max_length_1_nistxml_sv_iv_list_string_max_length_2_5(mode, save_output, output_format):
    """
    Type list/string is restricted by facet maxLength with value 6.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-maxLength-2.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-maxLength-2-5.xml",
        class_name="NistschemaSvIvListStringMaxLength2",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_max_length_nistxml_sv_iv_list_string_max_length_1_1(mode, save_output, output_format):
    """
    Type list/string is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-maxLength-1.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-maxLength-1-1.xml",
        class_name="NistschemaSvIvListStringMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_max_length_nistxml_sv_iv_list_string_max_length_1_2(mode, save_output, output_format):
    """
    Type list/string is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-maxLength-1.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-maxLength-1-2.xml",
        class_name="NistschemaSvIvListStringMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_max_length_nistxml_sv_iv_list_string_max_length_1_3(mode, save_output, output_format):
    """
    Type list/string is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-maxLength-1.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-maxLength-1-3.xml",
        class_name="NistschemaSvIvListStringMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_max_length_nistxml_sv_iv_list_string_max_length_1_4(mode, save_output, output_format):
    """
    Type list/string is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-maxLength-1.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-maxLength-1-4.xml",
        class_name="NistschemaSvIvListStringMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_string_max_length_nistxml_sv_iv_list_string_max_length_1_5(mode, save_output, output_format):
    """
    Type list/string is restricted by facet maxLength with value 5.
    """
    assert_bindings(
        schema="nistData/list/string/Schema+Instance/NISTSchema-SV-IV-list-string-maxLength-1.xsd",
        instance="nistData/list/string/Schema+Instance/NISTXML-SV-IV-list-string-maxLength-1-5.xml",
        class_name="NistschemaSvIvListStringMaxLength1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_g_month_white_space_nistxml_sv_iv_list_g_month_white_space_1_1(mode, save_output, output_format):
    """
    Type list/gMonth is restricted by facet whiteSpace with value
    collapse.
    """
    assert_bindings(
        schema="nistData/list/gMonth/Schema+Instance/NISTSchema-SV-IV-list-gMonth-whiteSpace-1.xsd",
        instance="nistData/list/gMonth/Schema+Instance/NISTXML-SV-IV-list-gMonth-whiteSpace-1-1.xml",
        class_name="NistschemaSvIvListGMonthWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_g_month_white_space_nistxml_sv_iv_list_g_month_white_space_1_2(mode, save_output, output_format):
    """
    Type list/gMonth is restricted by facet whiteSpace with value
    collapse.
    """
    assert_bindings(
        schema="nistData/list/gMonth/Schema+Instance/NISTSchema-SV-IV-list-gMonth-whiteSpace-1.xsd",
        instance="nistData/list/gMonth/Schema+Instance/NISTXML-SV-IV-list-gMonth-whiteSpace-1-2.xml",
        class_name="NistschemaSvIvListGMonthWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_g_month_white_space_nistxml_sv_iv_list_g_month_white_space_1_3(mode, save_output, output_format):
    """
    Type list/gMonth is restricted by facet whiteSpace with value
    collapse.
    """
    assert_bindings(
        schema="nistData/list/gMonth/Schema+Instance/NISTSchema-SV-IV-list-gMonth-whiteSpace-1.xsd",
        instance="nistData/list/gMonth/Schema+Instance/NISTXML-SV-IV-list-gMonth-whiteSpace-1-3.xml",
        class_name="NistschemaSvIvListGMonthWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_g_month_white_space_nistxml_sv_iv_list_g_month_white_space_1_4(mode, save_output, output_format):
    """
    Type list/gMonth is restricted by facet whiteSpace with value
    collapse.
    """
    assert_bindings(
        schema="nistData/list/gMonth/Schema+Instance/NISTSchema-SV-IV-list-gMonth-whiteSpace-1.xsd",
        instance="nistData/list/gMonth/Schema+Instance/NISTXML-SV-IV-list-gMonth-whiteSpace-1-4.xml",
        class_name="NistschemaSvIvListGMonthWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_list_g_month_white_space_nistxml_sv_iv_list_g_month_white_space_1_5(mode, save_output, output_format):
    """
    Type list/gMonth is restricted by facet whiteSpace with value
    collapse.
    """
    assert_bindings(
        schema="nistData/list/gMonth/Schema+Instance/NISTSchema-SV-IV-list-gMonth-whiteSpace-1.xsd",
        instance="nistData/list/gMonth/Schema+Instance/NISTXML-SV-IV-list-gMonth-whiteSpace-1-5.xml",
        class_name="NistschemaSvIvListGMonthWhiteSpace1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )
