import pytest

from tests.utils import assert_bindings


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k73_re_k73_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Cc}*', value='#x9;',
    type='invalid', RULE='26,35'
    """
    assert_bindings(
        schema="msData/regex/reK73.xsd",
        instance="msData/regex/reK73.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k72_re_k72_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{C}*', value='#x20A0;',
    type='valid', RULE='26,35'
    """
    assert_bindings(
        schema="msData/regex/reK72.xsd",
        instance="msData/regex/reK72.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k71_re_k71_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{C}*', value='#x9;#x070F;#x70
    F;#xE0078;#xE000;#xE000;#x100000;#xF0000;#xFFFFD;#x10FFFD;',
    type='invalid', RULE='26,35'
    """
    assert_bindings(
        schema="msData/regex/reK71.xsd",
        instance="msData/regex/reK71.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k70_re_k70_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{So}*', value='#x9;',
    type='valid', RULE='26,34'
    """
    assert_bindings(
        schema="msData/regex/reK70.xsd",
        instance="msData/regex/reK70.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k69_re_k69_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{So}*',
    value='#x3190;#x1D1DD;', type='invalid', RULE='26,34'
    """
    assert_bindings(
        schema="msData/regex/reK69.xsd",
        instance="msData/regex/reK69.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k68_re_k68_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Sk}*', value='#x3190;',
    type='valid', RULE='26,34'
    """
    assert_bindings(
        schema="msData/regex/reK68.xsd",
        instance="msData/regex/reK68.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k67_re_k67_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Sk}*',
    value='#x309B;#xFFE3;', type='invalid', RULE='26,34'
    """
    assert_bindings(
        schema="msData/regex/reK67.xsd",
        instance="msData/regex/reK67.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k66_re_k66_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Sc}*', value='#x309B;',
    type='valid', RULE='26,34'
    """
    assert_bindings(
        schema="msData/regex/reK66.xsd",
        instance="msData/regex/reK66.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k65_re_k65_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Sc}*',
    value='#x20A0;#xFFE6;', type='invalid', RULE='26,34'
    """
    assert_bindings(
        schema="msData/regex/reK65.xsd",
        instance="msData/regex/reK65.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k64_re_k64_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Sm}*', value='#x20A0;',
    type='valid', RULE='26,34'
    """
    assert_bindings(
        schema="msData/regex/reK64.xsd",
        instance="msData/regex/reK64.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k63_re_k63_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Sm}*',
    value='#x2044;#xFFE2;', type='invalid', RULE='26,34'
    """
    assert_bindings(
        schema="msData/regex/reK63.xsd",
        instance="msData/regex/reK63.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k62_re_k62_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{S}*', value='#x1680;',
    type='valid', RULE='26,34'
    """
    assert_bindings(
        schema="msData/regex/reK62.xsd",
        instance="msData/regex/reK62.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k61_re_k61_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{S}*', value='#x2044;#xFFE2;#
    x20A0;#x20A0;#xFFE6;#x309B;#x309B;#xFFE3;#x3190;#x3190;#x1D1DD;',
    type='invalid', RULE='26,34'
    """
    assert_bindings(
        schema="msData/regex/reK61.xsd",
        instance="msData/regex/reK61.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k60_re_k60_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Zp}*', value='#x2044;',
    type='valid', RULE='26,33'
    """
    assert_bindings(
        schema="msData/regex/reK60.xsd",
        instance="msData/regex/reK60.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k59_re_k59_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Zp}*', value='#x2029;',
    type='invalid', RULE='26,33'
    """
    assert_bindings(
        schema="msData/regex/reK59.xsd",
        instance="msData/regex/reK59.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k58_re_k58_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Zl}*', value='#x2029;',
    type='valid', RULE='26,33'
    """
    assert_bindings(
        schema="msData/regex/reK58.xsd",
        instance="msData/regex/reK58.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k57_re_k57_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Zl}*', value='#x2028;',
    type='invalid', RULE='26,33'
    """
    assert_bindings(
        schema="msData/regex/reK57.xsd",
        instance="msData/regex/reK57.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k56_re_k56_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Zs}*', value='#x2028;',
    type='valid', RULE='26,33'
    """
    assert_bindings(
        schema="msData/regex/reK56.xsd",
        instance="msData/regex/reK56.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k55_re_k55_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Zs}*',
    value='#x1680;#x3000;', type='invalid', RULE='26,33'
    """
    assert_bindings(
        schema="msData/regex/reK55.xsd",
        instance="msData/regex/reK55.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k54_re_k54_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Z}*', value='#xBF;',
    type='valid', RULE='26,33'
    """
    assert_bindings(
        schema="msData/regex/reK54.xsd",
        instance="msData/regex/reK54.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k53_re_k53_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Z}*',
    value='#x1680;#x3000;#x2028;#x2028;#x2029;#x2029;', type='invalid',
    RULE='26,33'
    """
    assert_bindings(
        schema="msData/regex/reK53.xsd",
        instance="msData/regex/reK53.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k52_re_k52_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Po}*', value='#x1680;',
    type='valid', RULE='26,32'
    """
    assert_bindings(
        schema="msData/regex/reK52.xsd",
        instance="msData/regex/reK52.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k51_re_k51_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Po}*', value='#xBF;#xFF64;',
    type='invalid', RULE='26,32'
    """
    assert_bindings(
        schema="msData/regex/reK51.xsd",
        instance="msData/regex/reK51.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k50_re_k50_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Pf}*', value='#xBF;',
    type='valid', RULE='26,32'
    """
    assert_bindings(
        schema="msData/regex/reK50.xsd",
        instance="msData/regex/reK50.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k49_re_k49_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Pf}*', value='#xBB;#x203A;',
    type='invalid', RULE='26,32'
    """
    assert_bindings(
        schema="msData/regex/reK49.xsd",
        instance="msData/regex/reK49.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k48_re_k48_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Pi}*', value='#xBB;',
    type='valid', RULE='26,32'
    """
    assert_bindings(
        schema="msData/regex/reK48.xsd",
        instance="msData/regex/reK48.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k47_re_k47_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Pi}*', value='#xAB;#x2039;',
    type='invalid', RULE='26,32'
    """
    assert_bindings(
        schema="msData/regex/reK47.xsd",
        instance="msData/regex/reK47.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k46_re_k46_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Pe}*', value='#xAB;',
    type='valid', RULE='26,32'
    """
    assert_bindings(
        schema="msData/regex/reK46.xsd",
        instance="msData/regex/reK46.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k45_re_k45_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Pe}*',
    value='#x301E;#xFF63;', type='invalid', RULE='26,32'
    """
    assert_bindings(
        schema="msData/regex/reK45.xsd",
        instance="msData/regex/reK45.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k44_re_k44_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Ps}*', value='#x301E;',
    type='valid', RULE='26,32'
    """
    assert_bindings(
        schema="msData/regex/reK44.xsd",
        instance="msData/regex/reK44.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k43_re_k43_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Ps}*',
    value='#x301D;#xFF62;', type='invalid', RULE='26,32'
    """
    assert_bindings(
        schema="msData/regex/reK43.xsd",
        instance="msData/regex/reK43.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k42_re_k42_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Pd}*', value='#x301D;',
    type='valid', RULE='26,32'
    """
    assert_bindings(
        schema="msData/regex/reK42.xsd",
        instance="msData/regex/reK42.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k41_re_k41_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Pd}*',
    value='#x301C;#xFF0D;', type='invalid', RULE='26,32'
    """
    assert_bindings(
        schema="msData/regex/reK41.xsd",
        instance="msData/regex/reK41.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k40_re_k40_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Pc}*', value='#x301C;',
    type='valid', RULE='26,32'
    """
    assert_bindings(
        schema="msData/regex/reK40.xsd",
        instance="msData/regex/reK40.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k39_re_k39_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Pc}*',
    value='#x203F;#xFF65;', type='invalid', RULE='26,32'
    """
    assert_bindings(
        schema="msData/regex/reK39.xsd",
        instance="msData/regex/reK39.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k38_re_k38_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{P}*', value='#xB2;',
    type='valid', RULE='26,32'
    """
    assert_bindings(
        schema="msData/regex/reK38.xsd",
        instance="msData/regex/reK38.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k37_re_k37_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{P}*', value='#x203F;#xFF65;#
    x301C;#x301C;#xFF0D;#x301D;#x301D;#xFF62;#x301E;#x301E;#xFF63;#xAB;#xA
    B;#x2039;#xBB;#xBB;#x203A;#xBF;#xBF;#xFF64;', type='invalid',
    RULE='26,32'
    """
    assert_bindings(
        schema="msData/regex/reK37.xsd",
        instance="msData/regex/reK37.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k36_re_k36_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{No}*', value='#x203F;',
    type='valid', RULE='26,31'
    """
    assert_bindings(
        schema="msData/regex/reK36.xsd",
        instance="msData/regex/reK36.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k35_re_k35_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{No}*',
    value='#xB2;#x10323;', type='invalid', RULE='26,31'
    """
    assert_bindings(
        schema="msData/regex/reK35.xsd",
        instance="msData/regex/reK35.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k34_re_k34_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Nl}*', value='#xB2;',
    type='valid', RULE='26,31'
    """
    assert_bindings(
        schema="msData/regex/reK34.xsd",
        instance="msData/regex/reK34.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k33_re_k33_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Nl}*',
    value='#x1034A;#x3025;', type='invalid', RULE='26,31'
    """
    assert_bindings(
        schema="msData/regex/reK33.xsd",
        instance="msData/regex/reK33.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k32_re_k32_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Nd}*', value='#x1034A;',
    type='valid', RULE='26,31'
    """
    assert_bindings(
        schema="msData/regex/reK32.xsd",
        instance="msData/regex/reK32.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k31_re_k31_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Nd}*',
    value='#xFF10;#x1D7FF;', type='invalid', RULE='26,31'
    """
    assert_bindings(
        schema="msData/regex/reK31.xsd",
        instance="msData/regex/reK31.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k30_re_k30_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{N}*', value='#x903;',
    type='valid', RULE='26,31'
    """
    assert_bindings(
        schema="msData/regex/reK30.xsd",
        instance="msData/regex/reK30.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k29_re_k29_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{N}*',
    value='#xFF10;#x1D7FF;#x1034A;#x1034A;#x3025;#xB2;#xB2;#x10323;',
    type='invalid', RULE='26,31'
    """
    assert_bindings(
        schema="msData/regex/reK29.xsd",
        instance="msData/regex/reK29.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k28_re_k28_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Me}*', value='#xFF10;',
    type='valid', RULE='26,30'
    """
    assert_bindings(
        schema="msData/regex/reK28.xsd",
        instance="msData/regex/reK28.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k27_re_k27_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Me}*',
    value='#x20DD;#x20E0;', type='invalid', RULE='26,30'
    """
    assert_bindings(
        schema="msData/regex/reK27.xsd",
        instance="msData/regex/reK27.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k26_re_k26_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Mc}*', value='#x20DD;',
    type='valid', RULE='26,30'
    """
    assert_bindings(
        schema="msData/regex/reK26.xsd",
        instance="msData/regex/reK26.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k25_re_k25_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Mc}*',
    value='#x903;#x1D172;', type='invalid', RULE='26,30'
    """
    assert_bindings(
        schema="msData/regex/reK25.xsd",
        instance="msData/regex/reK25.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k24_re_k24_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Mn}*',
    value='#x903;#x1D172;', type='valid', RULE='26,30'
    """
    assert_bindings(
        schema="msData/regex/reK24.xsd",
        instance="msData/regex/reK24.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k23_re_k23_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Mn}*',
    value='#x64B;#x1D1AD;', type='invalid', RULE='26,30'
    """
    assert_bindings(
        schema="msData/regex/reK23.xsd",
        instance="msData/regex/reK23.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k22_re_k22_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{M}*', value='#x1C5;',
    type='valid', RULE='26,30'
    """
    assert_bindings(
        schema="msData/regex/reK22.xsd",
        instance="msData/regex/reK22.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k21_re_k21_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{M}*', value='#x64B;#x1D1AD;#
    x903;#x1D172;#x903;#x1D172;#x20DD;#x20DD;#x20E0;', type='invalid',
    RULE='26,30'
    """
    assert_bindings(
        schema="msData/regex/reK21.xsd",
        instance="msData/regex/reK21.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k20_re_k20_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Lo}*', value='#x64B;',
    type='valid', RULE='26,29'
    """
    assert_bindings(
        schema="msData/regex/reK20.xsd",
        instance="msData/regex/reK20.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k19_re_k19_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Lo}*',
    value='#x5D0;#x2FA1D;', type='invalid', RULE='26,29'
    """
    assert_bindings(
        schema="msData/regex/reK19.xsd",
        instance="msData/regex/reK19.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k18_re_k18_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Lm}*', value='#x5D0;',
    type='valid', RULE='26,29'
    """
    assert_bindings(
        schema="msData/regex/reK18.xsd",
        instance="msData/regex/reK18.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k17_re_k17_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Lm}*',
    value='#x2B0;#xFF9F;', type='invalid', RULE='26,29'
    """
    assert_bindings(
        schema="msData/regex/reK17.xsd",
        instance="msData/regex/reK17.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k16_re_k16_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Lt}*', value='#x2B0;',
    type='valid', RULE='26,29'
    """
    assert_bindings(
        schema="msData/regex/reK16.xsd",
        instance="msData/regex/reK16.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k15_re_k15_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Lt}*',
    value='#x1C5;#x1FFC;', type='invalid', RULE='26,29'
    """
    assert_bindings(
        schema="msData/regex/reK15.xsd",
        instance="msData/regex/reK15.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k14_re_k14_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Ll}*', value='#x1C5;',
    type='valid', RULE='26,29'
    """
    assert_bindings(
        schema="msData/regex/reK14.xsd",
        instance="msData/regex/reK14.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k13_re_k13_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Ll}*',
    value='#x61;#x1D7C9;', type='invalid', RULE='26,29'
    """
    assert_bindings(
        schema="msData/regex/reK13.xsd",
        instance="msData/regex/reK13.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k12_re_k12_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Lu}*', value='#x61;',
    type='valid', RULE='26,29'
    """
    assert_bindings(
        schema="msData/regex/reK12.xsd",
        instance="msData/regex/reK12.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k11_re_k11_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{Lu}*',
    value='#x41;#x1D7A8;', type='invalid', RULE='26,29'
    """
    assert_bindings(
        schema="msData/regex/reK11.xsd",
        instance="msData/regex/reK11.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k10_re_k10_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{L}*', value='#x20DD;',
    type='valid', RULE='26,29'
    """
    assert_bindings(
        schema="msData/regex/reK10.xsd",
        instance="msData/regex/reK10.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k9_re_k9_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{L}*', value='#x41;#x1D7A8;#x
    61;#x61;#x1D7C9;#x1C5;#x1C5;#x1FFC;#x2B0;#x2B0;#xFF9F;#x5D0;#x5D0;#x2F
    A1D;', type='invalid', RULE='26,29'
    """
    assert_bindings(
        schema="msData/regex/reK9.xsd",
        instance="msData/regex/reK9.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k6_re_k6_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='[\P{L}*]{0,2}', value='A',
    type='invalid', RULE='26,29'
    """
    assert_bindings(
        schema="msData/regex/reK6.xsd",
        instance="msData/regex/reK6.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k5_re_k5_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='[\P{L}*]{0,2}', value='!$#',
    type='invalid', RULE='26,29'
    """
    assert_bindings(
        schema="msData/regex/reK5.xsd",
        instance="msData/regex/reK5.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k4_re_k4_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='[\P{L}*]{0,2}', value='#$',
    type='valid', RULE='26,29'
    """
    assert_bindings(
        schema="msData/regex/reK4.xsd",
        instance="msData/regex/reK4.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k3_re_k3_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='[\P{L}*]{0,2}', value='',
    type='valid', RULE='26,29'
    """
    assert_bindings(
        schema="msData/regex/reK3.xsd",
        instance="msData/regex/reK3.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_k2_re_k2_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{L}*', value='_',
    type='valid', RULE='26,29'
    """
    assert_bindings(
        schema="msData/regex/reK2.xsd",
        instance="msData/regex/reK2.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_k1_re_k1_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\P{L}*', value='aAbB',
    type='invalid', RULE='26,29'
    """
    assert_bindings(
        schema="msData/regex/reK1.xsd",
        instance="msData/regex/reK1.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j80_re_j80_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Cn}*', value='#x9;',
    type='invalid', RULE='25,35'
    """
    assert_bindings(
        schema="msData/regex/reJ80.xsd",
        instance="msData/regex/reJ80.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j78_re_j78_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Co}*', value='#x2044;',
    type='invalid', RULE='25,35'
    """
    assert_bindings(
        schema="msData/regex/reJ78.xsd",
        instance="msData/regex/reJ78.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j77_re_j77_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Co}*',
    value='#xE000;#x100000;#xF0000;#xFFFFD;#x10FFFD;', type='valid',
    RULE='25,35'
    """
    assert_bindings(
        schema="msData/regex/reJ77.xsd",
        instance="msData/regex/reJ77.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j76_re_j76_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Cf}*', value='#xE000;',
    type='invalid', RULE='25,35'
    """
    assert_bindings(
        schema="msData/regex/reJ76.xsd",
        instance="msData/regex/reJ76.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j75_re_j75_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Cf}*',
    value='#x70F;#xE0078;', type='valid', RULE='25,35'
    """
    assert_bindings(
        schema="msData/regex/reJ75.xsd",
        instance="msData/regex/reJ75.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j74_re_j74_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Cc}*', value='#x070F;',
    type='invalid', RULE='25,35'
    """
    assert_bindings(
        schema="msData/regex/reJ74.xsd",
        instance="msData/regex/reJ74.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_j73_re_j73_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Cc}*', value='#x9;',
    type='valid', RULE='25,35'
    """
    assert_bindings(
        schema="msData/regex/reJ73.xsd",
        instance="msData/regex/reJ73.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j72_re_j72_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{C}*', value='#x20A0;',
    type='invalid', RULE='25,35'
    """
    assert_bindings(
        schema="msData/regex/reJ72.xsd",
        instance="msData/regex/reJ72.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j70_re_j70_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{So}*', value='#x9;',
    type='invalid', RULE='25,34'
    """
    assert_bindings(
        schema="msData/regex/reJ70.xsd",
        instance="msData/regex/reJ70.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j69_re_j69_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{So}*',
    value='#x3190;#x1D1DD;', type='valid', RULE='25,34'
    """
    assert_bindings(
        schema="msData/regex/reJ69.xsd",
        instance="msData/regex/reJ69.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j68_re_j68_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Sk}*', value='#x3190;',
    type='invalid', RULE='25,34'
    """
    assert_bindings(
        schema="msData/regex/reJ68.xsd",
        instance="msData/regex/reJ68.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_j67_re_j67_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Sk}*',
    value='#x309B;#xFFE3;', type='valid', RULE='25,34'
    """
    assert_bindings(
        schema="msData/regex/reJ67.xsd",
        instance="msData/regex/reJ67.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j66_re_j66_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Sc}*', value='#x309B;',
    type='invalid', RULE='25,34'
    """
    assert_bindings(
        schema="msData/regex/reJ66.xsd",
        instance="msData/regex/reJ66.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_j65_re_j65_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Sc}*',
    value='#x20A0;#xFFE6;', type='valid', RULE='25,34'
    """
    assert_bindings(
        schema="msData/regex/reJ65.xsd",
        instance="msData/regex/reJ65.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j64_re_j64_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Sm}*', value='#x20A0;',
    type='invalid', RULE='25,34'
    """
    assert_bindings(
        schema="msData/regex/reJ64.xsd",
        instance="msData/regex/reJ64.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_j63_re_j63_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Sm}*',
    value='#x2044;#xFFE2;', type='valid', RULE='25,34'
    """
    assert_bindings(
        schema="msData/regex/reJ63.xsd",
        instance="msData/regex/reJ63.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j62_re_j62_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{S}*', value='#x1680;',
    type='invalid', RULE='25,34'
    """
    assert_bindings(
        schema="msData/regex/reJ62.xsd",
        instance="msData/regex/reJ62.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j61_re_j61_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{S}*', value='#x2044;#xFFE2;#
    x20A0;#x20A0;#xFFE6;#x309B;#x309B;#xFFE3;#x3190;#x3190;#x1D1DD;',
    type='valid', RULE='25,34'
    """
    assert_bindings(
        schema="msData/regex/reJ61.xsd",
        instance="msData/regex/reJ61.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j60_re_j60_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Zp}*', value='#x2044;',
    type='invalid', RULE='25,33'
    """
    assert_bindings(
        schema="msData/regex/reJ60.xsd",
        instance="msData/regex/reJ60.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_j59_re_j59_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Zp}*', value='#x2029;',
    type='valid', RULE='25,33'
    """
    assert_bindings(
        schema="msData/regex/reJ59.xsd",
        instance="msData/regex/reJ59.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j58_re_j58_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Zl}*', value='#x2029;',
    type='invalid', RULE='25,33'
    """
    assert_bindings(
        schema="msData/regex/reJ58.xsd",
        instance="msData/regex/reJ58.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_j57_re_j57_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Zl}*', value='#x2028;',
    type='valid', RULE='25,33'
    """
    assert_bindings(
        schema="msData/regex/reJ57.xsd",
        instance="msData/regex/reJ57.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j56_re_j56_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Zs}*', value='#x2028;',
    type='invalid', RULE='25,33'
    """
    assert_bindings(
        schema="msData/regex/reJ56.xsd",
        instance="msData/regex/reJ56.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_j55_re_j55_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Zs}*',
    value='#x1680;#x3000;', type='valid', RULE='25,33'
    """
    assert_bindings(
        schema="msData/regex/reJ55.xsd",
        instance="msData/regex/reJ55.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j54_re_j54_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Z}*', value='#xBF;',
    type='invalid', RULE='25,33'
    """
    assert_bindings(
        schema="msData/regex/reJ54.xsd",
        instance="msData/regex/reJ54.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_j53_re_j53_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Z}*',
    value='#x1680;#x3000;#x2028;#x2028;#x2029;#x2029;', type='valid',
    RULE='25,33'
    """
    assert_bindings(
        schema="msData/regex/reJ53.xsd",
        instance="msData/regex/reJ53.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j52_re_j52_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Po}*', value='#x1680;',
    type='invalid', RULE='25,32'
    """
    assert_bindings(
        schema="msData/regex/reJ52.xsd",
        instance="msData/regex/reJ52.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_j51_re_j51_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Po}*', value='#xBF;#xFF64;',
    type='valid', RULE='25,32'
    """
    assert_bindings(
        schema="msData/regex/reJ51.xsd",
        instance="msData/regex/reJ51.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j50_re_j50_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Pf}*', value='#xBF;',
    type='invalid', RULE='25,32'
    """
    assert_bindings(
        schema="msData/regex/reJ50.xsd",
        instance="msData/regex/reJ50.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_j49_re_j49_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Pf}*', value='#xBB;#x203A;',
    type='valid', RULE='25,32'
    """
    assert_bindings(
        schema="msData/regex/reJ49.xsd",
        instance="msData/regex/reJ49.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j48_re_j48_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Pi}*', value='#xBB;',
    type='invalid', RULE='25,32'
    """
    assert_bindings(
        schema="msData/regex/reJ48.xsd",
        instance="msData/regex/reJ48.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_j47_re_j47_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Pi}*', value='#xAB;#x2039;',
    type='valid', RULE='25,32'
    """
    assert_bindings(
        schema="msData/regex/reJ47.xsd",
        instance="msData/regex/reJ47.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j46_re_j46_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Pe}*', value='#xAB;',
    type='invalid', RULE='25,32'
    """
    assert_bindings(
        schema="msData/regex/reJ46.xsd",
        instance="msData/regex/reJ46.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_j45_re_j45_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Pe}*',
    value='#x301E;#xFF63;', type='valid', RULE='25,32'
    """
    assert_bindings(
        schema="msData/regex/reJ45.xsd",
        instance="msData/regex/reJ45.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j44_re_j44_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Ps}*', value='#x301E;',
    type='invalid', RULE='25,32'
    """
    assert_bindings(
        schema="msData/regex/reJ44.xsd",
        instance="msData/regex/reJ44.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_j43_re_j43_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Ps}*',
    value='#x301D;#xFF62;', type='valid', RULE='25,32'
    """
    assert_bindings(
        schema="msData/regex/reJ43.xsd",
        instance="msData/regex/reJ43.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j42_re_j42_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Pd}*', value='#x301D;',
    type='invalid', RULE='25,32'
    """
    assert_bindings(
        schema="msData/regex/reJ42.xsd",
        instance="msData/regex/reJ42.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_j41_re_j41_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Pd}*',
    value='#x301C;#xFF0D;', type='valid', RULE='25,32'
    """
    assert_bindings(
        schema="msData/regex/reJ41.xsd",
        instance="msData/regex/reJ41.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j40_re_j40_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Pc}*', value='#x301C;',
    type='invalid', RULE='25,32'
    """
    assert_bindings(
        schema="msData/regex/reJ40.xsd",
        instance="msData/regex/reJ40.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j38_re_j38_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{P}*', value='#xB2;',
    type='invalid', RULE='25,32'
    """
    assert_bindings(
        schema="msData/regex/reJ38.xsd",
        instance="msData/regex/reJ38.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_j37_re_j37_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{P}*', value='#x203F;#xFF65;#
    x301C;#x301C;#xFF0D;#x301D;#x301D;#xFF62;#x301E;#x301E;#xFF63;#xAB;#xA
    B;#x2039;#xBB;#xBB;#x203A;#xBF;#xBF;#xFF64;', type='valid',
    RULE='25,32'
    """
    assert_bindings(
        schema="msData/regex/reJ37.xsd",
        instance="msData/regex/reJ37.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j36_re_j36_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{No}*', value='#x203F;',
    type='invalid', RULE='25,31'
    """
    assert_bindings(
        schema="msData/regex/reJ36.xsd",
        instance="msData/regex/reJ36.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j35_re_j35_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{No}*',
    value='#xB2;#x10323;', type='valid', RULE='25,31'
    """
    assert_bindings(
        schema="msData/regex/reJ35.xsd",
        instance="msData/regex/reJ35.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j34_re_j34_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Nl}*', value='#xB2;',
    type='invalid', RULE='25,31'
    """
    assert_bindings(
        schema="msData/regex/reJ34.xsd",
        instance="msData/regex/reJ34.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j33_re_j33_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Nl}*',
    value='#x1034A;#x3025;', type='valid', RULE='25,31'
    """
    assert_bindings(
        schema="msData/regex/reJ33.xsd",
        instance="msData/regex/reJ33.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j32_re_j32_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Nd}*', value='#x1034A;',
    type='invalid', RULE='25,31'
    """
    assert_bindings(
        schema="msData/regex/reJ32.xsd",
        instance="msData/regex/reJ32.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j31_re_j31_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Nd}*',
    value='#xFF10;#x1D7FF;', type='valid', RULE='25,31'
    """
    assert_bindings(
        schema="msData/regex/reJ31.xsd",
        instance="msData/regex/reJ31.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j30_re_j30_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{N}*', value='#x903;',
    type='invalid', RULE='25,31'
    """
    assert_bindings(
        schema="msData/regex/reJ30.xsd",
        instance="msData/regex/reJ30.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j29_re_j29_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{N}*',
    value='#xFF10;#x1D7FF;#x1034A;#x1034A;#x3025;#xB2;#xB2;#x10323;',
    type='valid', RULE='25,31'
    """
    assert_bindings(
        schema="msData/regex/reJ29.xsd",
        instance="msData/regex/reJ29.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j28_re_j28_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Me}*', value='#xFF10;',
    type='invalid', RULE='25,30'
    """
    assert_bindings(
        schema="msData/regex/reJ28.xsd",
        instance="msData/regex/reJ28.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_j27_re_j27_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Me}*',
    value='#x20DD;#x20E0;', type='valid', RULE='25,30'
    """
    assert_bindings(
        schema="msData/regex/reJ27.xsd",
        instance="msData/regex/reJ27.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j26_re_j26_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Mc}*', value='#x20DD;',
    type='invalid', RULE='25,30'
    """
    assert_bindings(
        schema="msData/regex/reJ26.xsd",
        instance="msData/regex/reJ26.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j25_re_j25_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Mc}*',
    value='#x903;#x1D172;', type='valid', RULE='25,30'
    """
    assert_bindings(
        schema="msData/regex/reJ25.xsd",
        instance="msData/regex/reJ25.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j24_re_j24_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Mn}*', value='#x903;',
    type='invalid', RULE='25,30'
    """
    assert_bindings(
        schema="msData/regex/reJ24.xsd",
        instance="msData/regex/reJ24.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j23_re_j23_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Mn}*',
    value='#x64B;#x1D1AD;', type='valid', RULE='25,30'
    """
    assert_bindings(
        schema="msData/regex/reJ23.xsd",
        instance="msData/regex/reJ23.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j22_re_j22_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{M}*', value='#x1C5;',
    type='invalid', RULE='25,30'
    """
    assert_bindings(
        schema="msData/regex/reJ22.xsd",
        instance="msData/regex/reJ22.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j21_re_j21_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{M}*', value='#x64B;#x1D1AD;#
    x903;#x1D172;#x903;#x1D172;#x20DD;#x20DD;#x20E0;', type='valid',
    RULE='25,30'
    """
    assert_bindings(
        schema="msData/regex/reJ21.xsd",
        instance="msData/regex/reJ21.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j20_re_j20_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Lo}*', value='#x64B;',
    type='invalid', RULE='25,29'
    """
    assert_bindings(
        schema="msData/regex/reJ20.xsd",
        instance="msData/regex/reJ20.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j19_re_j19_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Lo}*',
    value='#x5D0;#x2FA1D;', type='valid', RULE='25,29'
    """
    assert_bindings(
        schema="msData/regex/reJ19.xsd",
        instance="msData/regex/reJ19.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j18_re_j18_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Lm}*', value='#x5D0;',
    type='invalid', RULE='25,29'
    """
    assert_bindings(
        schema="msData/regex/reJ18.xsd",
        instance="msData/regex/reJ18.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_j17_re_j17_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Lm}*',
    value='#x2B0;#xFF9F;', type='valid', RULE='25,29'
    """
    assert_bindings(
        schema="msData/regex/reJ17.xsd",
        instance="msData/regex/reJ17.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j16_re_j16_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Lt}*', value='#x2B0;',
    type='invalid', RULE='25,29'
    """
    assert_bindings(
        schema="msData/regex/reJ16.xsd",
        instance="msData/regex/reJ16.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_j15_re_j15_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Lt}*',
    value='#x1C5;#x1FFC;', type='valid', RULE='25,29'
    """
    assert_bindings(
        schema="msData/regex/reJ15.xsd",
        instance="msData/regex/reJ15.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j14_re_j14_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Ll}*', value='#x1C5;',
    type='invalid', RULE='25,29'
    """
    assert_bindings(
        schema="msData/regex/reJ14.xsd",
        instance="msData/regex/reJ14.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j13_re_j13_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Ll}*',
    value='#x61;#x1D7C9;', type='valid', RULE='25,29'
    """
    assert_bindings(
        schema="msData/regex/reJ13.xsd",
        instance="msData/regex/reJ13.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j12_re_j12_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Lu}*', value='#x61;',
    type='invalid', RULE='25,29'
    """
    assert_bindings(
        schema="msData/regex/reJ12.xsd",
        instance="msData/regex/reJ12.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j11_re_j11_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{Lu}*',
    value='#x41;#x1D7A8;', type='valid', RULE='25,29'
    """
    assert_bindings(
        schema="msData/regex/reJ11.xsd",
        instance="msData/regex/reJ11.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j10_re_j10_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\p{L}*', value='#x20DD;',
    type='invalid', RULE='25,29'
    """
    assert_bindings(
        schema="msData/regex/reJ10.xsd",
        instance="msData/regex/reJ10.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j8_re_j8_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='(\p{Ll}\p{Cc}\p{Nd})*',
    value='#x1680;', type='invalid', RULE='25,29'
    """
    assert_bindings(
        schema="msData/regex/reJ8.xsd",
        instance="msData/regex/reJ8.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_j5_re_j5_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='[\p{L}*]{0,2}', value='aBC',
    type='invalid', RULE='25,29'
    """
    assert_bindings(
        schema="msData/regex/reJ5.xsd",
        instance="msData/regex/reJ5.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_j4_re_j4_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='[\p{L}*]{0,2}', value='aX',
    type='valid', RULE='25,29'
    """
    assert_bindings(
        schema="msData/regex/reJ4.xsd",
        instance="msData/regex/reJ4.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i83_re_i83_v(save_xml):
    r"""
    TEST :branch : base='string',pattern="\\.*,\\s*,\\S*,\\i*,\\I?,\\c+,\\
    C+,\\d{0,3},\\D{1,1000},\\w*,\\W*",
    value='\.,\s,\S,\i,\I,\c,\C,\d,\D,\w,\W', type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI83.xsd",
        instance="msData/regex/reI83.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i82_re_i82_v(save_xml):
    r"""
    TEST :branch : base='string',
    pattern="\\.,\\s,\\S,\\i,\\I,\\c,\\C,\\d,\\D,\\w,\\W",
    value='\.,\s,\S,\i,\I,\c,\C,\d,\D,\w,\W', type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI82.xsd",
        instance="msData/regex/reI82.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_i81_re_i81_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\\c', value='\\', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI79.xsd",
        instance="msData/regex/reI81.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_i80_re_i80_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\\c', value='\\c',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI79.xsd",
        instance="msData/regex/reI80.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_i79_re_i79_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\\c', value='\p{_xmlC}',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI79.xsd",
        instance="msData/regex/reI79.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i78_re_i78_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\\c', value='\c', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI78.xsd",
        instance="msData/regex/reI78.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i77_re_i77_v(save_xml):
    r"""
    TEST :branch : base='string',
    pattern='(\t|\s)a(\r\n|\r|\n|\s)+(\s|\t)b(\s|\r\n|\r|\n)*', value=' a
    b', type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI77.xsd",
        instance="msData/regex/reI77.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_i76_re_i76_i(save_xml):
    r"""
    TEST :branch : base='string',
    pattern='(\t|\s)a(\r\n|\r|\n|\s)+(\s|\t)b(\s|\r\n|\r|\n)*', value=' a
    b ', type='invalid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI76.xsd",
        instance="msData/regex/reI76.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_i75_re_i75_i(save_xml):
    r"""
    TEST :branch : base='string',
    pattern='(\t|\s)a(\r\n|\r|\n|\s)+(\s|\t)b(\s|\r\n|\r|\n)*', value=' a
    b', type='invalid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI75.xsd",
        instance="msData/regex/reI75.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i74_re_i74_v(save_xml):
    r"""
    TEST :branch : base='string',
    pattern='(\t|\s)a(\r\n|\r|\n|\s)+(\s|\t)b(\s|\r\n|\r|\n)*', value=' a
    b ', type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI74.xsd",
        instance="msData/regex/reI74.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i73_re_i73_v(save_xml):
    r"""
    TEST :branch : base='string',
    pattern='(\t|\s)a(\r\n|\r|\n|\s)+(\s|\t)b(\s|\r\n|\r|\n)*', value=' a
    b', type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI73.xsd",
        instance="msData/regex/reI73.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i72_re_i72_v(save_xml):
    r"""
    TEST :branch : base='string',
    pattern='(\t|\s)a(\r\n|\r|\n|\s)+(\s|\t)b(\s|\r\n|\r|\n)*', value=' a
    b', type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI72.xsd",
        instance="msData/regex/reI72.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i71_re_i71_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\na\nb\nc\n', value=' a b c ',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI71.xsd",
        instance="msData/regex/reI71.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i69_re_i69_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\ta\tb\tc\t', value=' a b c ',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI69.xsd",
        instance="msData/regex/reI69.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i67_re_i67_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\n\ra\n\rb', value=' a b',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI67.xsd",
        instance="msData/regex/reI67.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i65_re_i65_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='a\r\nb', value='a b',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI65.xsd",
        instance="msData/regex/reI65.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_i64_re_i64_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\t\ta\t\tb\t\t', value=' a b ',
    type='invalid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI64.xsd",
        instance="msData/regex/reI64.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_i63_re_i63_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\t\ta\t\tb\t\t', value=' a ',
    type='invalid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI63.xsd",
        instance="msData/regex/reI63.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_i62_re_i62_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\t\ta\t\tb\t\t', value=' a b ',
    type='invalid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI62.xsd",
        instance="msData/regex/reI62.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_i61_re_i61_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\t\ta\t\tb\t\t', value=' a b ',
    type='invalid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI61.xsd",
        instance="msData/regex/reI61.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_i59_re_i59_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\r\ra\r\rb\r\r', value=' a b ',
    type='invalid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI59.xsd",
        instance="msData/regex/reI59.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_i58_re_i58_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\r\ra\r\rb\r\r', value=' a ',
    type='invalid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI58.xsd",
        instance="msData/regex/reI58.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_i57_re_i57_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\r\ra\r\rb\r\r', value=' a b ',
    type='invalid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI57.xsd",
        instance="msData/regex/reI57.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_i56_re_i56_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\r\ra\r\rb\r\r', value=' a b ',
    type='invalid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI56.xsd",
        instance="msData/regex/reI56.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i55_re_i55_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\r\ra\r\rb\r\r', value=' a b ',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI55.xsd",
        instance="msData/regex/reI55.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_i54_re_i54_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\n\na\n\nb\n\n', value=' a b ',
    type='invalid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI54.xsd",
        instance="msData/regex/reI54.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_i53_re_i53_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\n\na\n\nb\n\n', value=' a ',
    type='invalid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI53.xsd",
        instance="msData/regex/reI53.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_i52_re_i52_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\n\na\n\nb\n\n', value=' a b ',
    type='invalid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI52.xsd",
        instance="msData/regex/reI52.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_i51_re_i51_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\n\na\n\nb\n\n', value=' a b ',
    type='invalid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI51.xsd",
        instance="msData/regex/reI51.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_i49_re_i49_i(save_xml):
    r"""
    TEST :branch : base='string',
    pattern='\n\\\r\|\t\.\-\^\?\*\+\{\}\(\)\[\]', value=' \ |
    -^?*+{}()[]', type='invalid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI49.xsd",
        instance="msData/regex/reI49.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_i48_re_i48_i(save_xml):
    r"""
    TEST :branch : base='string',
    pattern='\n\\\r\|\t\.\-\^\?\*\+\{\}\(\)\[\]', value='\ |
    .-^?*+{}()[]', type='invalid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI48.xsd",
        instance="msData/regex/reI48.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_i47_re_i47_i(save_xml):
    r"""
    TEST :branch : base='string',
    pattern='\n\\\r\|\t\.\-\^\?\*\+\{\}\(\)\[\]', value=' \ |
    .-^?*+{}()[', type='invalid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI47.xsd",
        instance="msData/regex/reI47.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i45_re_i45_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\]', value=']', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI45.xsd",
        instance="msData/regex/reI45.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i44_re_i44_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\[', value='[', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI44.xsd",
        instance="msData/regex/reI44.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i43_re_i43_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\)', value=')', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI43.xsd",
        instance="msData/regex/reI43.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i42_re_i42_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\(', value='(', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI42.xsd",
        instance="msData/regex/reI42.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i41_re_i41_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\}', value='}', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI41.xsd",
        instance="msData/regex/reI41.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i40_re_i40_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\{', value='{', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI40.xsd",
        instance="msData/regex/reI40.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i39_re_i39_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\+', value='+', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI39.xsd",
        instance="msData/regex/reI39.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i38_re_i38_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\*', value='*', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI38.xsd",
        instance="msData/regex/reI38.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i37_re_i37_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\?', value='?', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI37.xsd",
        instance="msData/regex/reI37.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i36_re_i36_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\^', value='^', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI36.xsd",
        instance="msData/regex/reI36.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i35_re_i35_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\-', value='-', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI35.xsd",
        instance="msData/regex/reI35.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i34_re_i34_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\.', value='.', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI34.xsd",
        instance="msData/regex/reI34.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i33_re_i33_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\|', value='|', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI33.xsd",
        instance="msData/regex/reI33.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i32_re_i32_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\\', value='\', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI32.xsd",
        instance="msData/regex/reI32.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i31_re_i31_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\t', value='#x9;',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI31.xsd",
        instance="msData/regex/reI31.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i29_re_i29_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\n', value='#xA;',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI29.xsd",
        instance="msData/regex/reI29.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_i28_re_i28_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\\r', value='#xD;',
    type='invalid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI28.xsd",
        instance="msData/regex/reI28.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_i27_re_i27_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\\r', value='\\r',
    type='invalid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI27.xsd",
        instance="msData/regex/reI27.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_i26_re_i26_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\\r', value='r',
    type='invalid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI26.xsd",
        instance="msData/regex/reI26.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i25_re_i25_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\\r', value='\r', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI25.xsd",
        instance="msData/regex/reI25.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_i24_re_i24_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\\n', value='#xA;',
    type='invalid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI24.xsd",
        instance="msData/regex/reI24.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_i23_re_i23_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\\n', value='\\n',
    type='invalid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI23.xsd",
        instance="msData/regex/reI23.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_i22_re_i22_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\\n', value='n',
    type='invalid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI22.xsd",
        instance="msData/regex/reI22.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i21_re_i21_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\\n', value='\n', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI21.xsd",
        instance="msData/regex/reI21.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_i20_re_i20_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\\t', value='#x9;',
    type='invalid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI20.xsd",
        instance="msData/regex/reI20.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_i19_re_i19_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\\t', value='\\t',
    type='invalid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI19.xsd",
        instance="msData/regex/reI19.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_i18_re_i18_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\\t', value='t',
    type='invalid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI18.xsd",
        instance="msData/regex/reI18.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i17_re_i17_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\\t', value='\t', type='valid',
    RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI17.xsd",
        instance="msData/regex/reI17.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i16_re_i16_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='[(a\?)?]+', value='aa?',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI16.xsd",
        instance="msData/regex/reI16.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i15_re_i15_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='[(a\?)?]+', value='a??',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI15.xsd",
        instance="msData/regex/reI15.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i14_re_i14_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='[(a\?)?]+', value='a',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI14.xsd",
        instance="msData/regex/reI14.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i13_re_i13_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='[(a\?)?]+', value='a?a?a?',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI13.xsd",
        instance="msData/regex/reI13.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i12_re_i12_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='[(a\?)?]+', value='a?',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI12.xsd",
        instance="msData/regex/reI12.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_i11_re_i11_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='[(a\?)?]+', value='',
    type='invalid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI11.xsd",
        instance="msData/regex/reI11.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i10_re_i10_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='[a\*]*', value='a',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI10.xsd",
        instance="msData/regex/reI10.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i9_re_i9_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='[a\*]*', value='aa*',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI9.xsd",
        instance="msData/regex/reI9.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i8_re_i8_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='[a\*]*', value='a**',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI8.xsd",
        instance="msData/regex/reI8.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_i1_re_i1_v(save_xml):
    r"""
    TEST :branch : base='string',
    pattern='(\n\r\t\\\|\.\-\^\?\*\+\{\}\[\]\(\))*',
    value='\|.-^?*+[]{}()*[[]{}}))#xA;#xD;#x9;#x9;#xA;#xa;#xd;*()',
    type='valid', RULE='24'
    """
    assert_bindings(
        schema="msData/regex/reI1.xsd",
        instance="msData/regex/reI1.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_h21_re_h21_i(save_xml):
    """
    TEST :branch : base='string', pattern='[a-a-x-x]+', value='a-b',
    type='invalid', RULE='22'
    """
    assert_bindings(
        schema="msData/regex/reH21.xsd",
        instance="msData/regex/reH21.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_h20_re_h20_i(save_xml):
    """
    TEST :branch : base='string', pattern='[a-a-x-x]+', value='j',
    type='invalid', RULE='22'
    """
    assert_bindings(
        schema="msData/regex/reH20.xsd",
        instance="msData/regex/reH20.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_h19_re_h19_v(save_xml):
    """
    TEST :branch : base='string', pattern='[a-a-x-x]+', value='a-x',
    type='valid', RULE='22'
    """
    assert_bindings(
        schema="msData/regex/reH19.xsd",
        instance="msData/regex/reH19.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_h18_re_h18_v(save_xml):
    """
    TEST :branch : base='string', pattern='[a-]*', value='a--aa---',
    type='valid', RULE='22'
    """
    assert_bindings(
        schema="msData/regex/reH18.xsd",
        instance="msData/regex/reH18.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_h17_re_h17_v(save_xml):
    """
    TEST :branch : base='string', pattern='[-a]+', value='a--aa---',
    type='valid', RULE='22'
    """
    assert_bindings(
        schema="msData/regex/reH17.xsd",
        instance="msData/regex/reH17.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_h16_re_h16_v(save_xml):
    """
    TEST :branch : base='string', pattern='[-]', value='-', type='valid',
    RULE='22'
    """
    assert_bindings(
        schema="msData/regex/reH16.xsd",
        instance="msData/regex/reH16.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_h15_re_h15_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='[\\\[\]]{0,3}', value='[][]',
    type='invalid', RULE='21,22'
    """
    assert_bindings(
        schema="msData/regex/reH15.xsd",
        instance="msData/regex/reH15.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_h14_re_h14_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='[\\\[\]]{0,3}', value='\]\]',
    type='invalid', RULE='21,22'
    """
    assert_bindings(
        schema="msData/regex/reH14.xsd",
        instance="msData/regex/reH14.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_h13_re_h13_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='[\\\[\]]{0,3}', value='\[][',
    type='invalid', RULE='21,22'
    """
    assert_bindings(
        schema="msData/regex/reH13.xsd",
        instance="msData/regex/reH13.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_h12_re_h12_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='[\\\[\]]{0,3}', value='[][',
    type='valid', RULE='21,22'
    """
    assert_bindings(
        schema="msData/regex/reH12.xsd",
        instance="msData/regex/reH12.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_h11_re_h11_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='[\\\[\]]{0,3}', value='\]\',
    type='valid', RULE='21,22'
    """
    assert_bindings(
        schema="msData/regex/reH11.xsd",
        instance="msData/regex/reH11.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_h10_re_h10_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='[\\\[\]]{0,3}', value='[\\',
    type='valid', RULE='21,22'
    """
    assert_bindings(
        schema="msData/regex/reH10.xsd",
        instance="msData/regex/reH10.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_h9_re_h9_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='[\\\[\]]{0,3}', value='[]',
    type='valid', RULE='21,22'
    """
    assert_bindings(
        schema="msData/regex/reH9.xsd",
        instance="msData/regex/reH9.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_h8_re_h8_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='[\\\[\]]{0,3}', value='\[]',
    type='valid', RULE='21,22'
    """
    assert_bindings(
        schema="msData/regex/reH8.xsd",
        instance="msData/regex/reH8.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_h7_re_h7_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='[\\\[\]]{0,3}', value='\[',
    type='valid', RULE='21,22'
    """
    assert_bindings(
        schema="msData/regex/reH7.xsd",
        instance="msData/regex/reH7.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_h6_re_h6_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='[\\\[\]]{0,3}', value=']',
    type='valid', RULE='21,22'
    """
    assert_bindings(
        schema="msData/regex/reH6.xsd",
        instance="msData/regex/reH6.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_h5_re_h5_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='[\\\[\]]{0,3}', value='[',
    type='valid', RULE='21,22'
    """
    assert_bindings(
        schema="msData/regex/reH5.xsd",
        instance="msData/regex/reH5.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_h4_re_h4_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='[\\\[\]]{0,3}', value='\',
    type='valid', RULE='21,22'
    """
    assert_bindings(
        schema="msData/regex/reH4.xsd",
        instance="msData/regex/reH4.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_g51_re_g51_i(save_xml):
    """
    TEST :branch : base='string', pattern='[#x10000;]', value='#x10001;',
    type='invalid', RULE='19'
    """
    assert_bindings(
        schema="msData/regex/reG51.xsd",
        instance="msData/regex/reG51.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_g50_re_g50_i(save_xml):
    """
    TEST :branch : base='string', pattern='[#x10000;]', value='#x10000;',
    type='valid', RULE='19' MK & HST agreed this one is OK, as does MS's
    own comment
    """
    assert_bindings(
        schema="msData/regex/reG50.xsd",
        instance="msData/regex/reG50.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_g49_re_g49_v(save_xml):
    """
    TEST :branch : base='string', pattern='[?]', value='#x0FFF;',
    type='valid', RULE='19'
    """
    assert_bindings(
        schema="msData/regex/reG49.xsd",
        instance="msData/regex/reG49.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_g48_re_g48_i(save_xml):
    """
    TEST :branch : base='string', pattern='[@]', value='a',
    type='invalid', RULE='19'
    """
    assert_bindings(
        schema="msData/regex/reG48.xsd",
        instance="msData/regex/reG48.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_g47_re_g47_v(save_xml):
    """
    TEST :branch : base='string', pattern='[@]', value='@', type='valid',
    RULE='19'
    """
    assert_bindings(
        schema="msData/regex/reG47.xsd",
        instance="msData/regex/reG47.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_g45_re_g45_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='[=->]', value='\?',
    type='invalid', RULE='18'
    """
    assert_bindings(
        schema="msData/regex/reG45.xsd",
        instance="msData/regex/reG45.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_g44_re_g44_v(save_xml):
    """
    TEST :branch : base='string', pattern='[=->]', value='>',
    type='valid', RULE='18'
    """
    assert_bindings(
        schema="msData/regex/reG44.xsd",
        instance="msData/regex/reG44.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_g43_re_g43_v(save_xml):
    """
    TEST :branch : base='string', pattern='[=->]', value='=',
    type='valid', RULE='18'
    """
    assert_bindings(
        schema="msData/regex/reG43.xsd",
        instance="msData/regex/reG43.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_g40_re_g40_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='[1-\]]+', value='^',
    type='invalid', RULE='18'
    """
    assert_bindings(
        schema="msData/regex/reG40.xsd",
        instance="msData/regex/reG40.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_g39_re_g39_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='[1-\]]+', value='0',
    type='invalid', RULE='18'
    """
    assert_bindings(
        schema="msData/regex/reG39.xsd",
        instance="msData/regex/reG39.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_g38_re_g38_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='[1-\]]+', value='1]',
    type='valid', RULE='18'
    """
    assert_bindings(
        schema="msData/regex/reG38.xsd",
        instance="msData/regex/reG38.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_g36_re_g36_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='[\*a]*', value='a*a****aaaaa*',
    type='valid', RULE='18'
    """
    assert_bindings(
        schema="msData/regex/reG36.xsd",
        instance="msData/regex/reG36.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_g33_re_g33_v(save_xml):
    """
    TEST :branch : base='string', pattern='[a-c-1-4x-z-7-9]*',
    value='z-9', type='valid', RULE='14'
    """
    assert_bindings(
        schema="msData/regex/reG33.xsd",
        instance="msData/regex/reG33.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_g32_re_g32_v(save_xml):
    """
    TEST :branch : base='string', pattern='[a-c-1-4x-z-7-9]*',
    value='a-1', type='valid', RULE='14'
    """
    assert_bindings(
        schema="msData/regex/reG32.xsd",
        instance="msData/regex/reG32.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_g31_re_g31_v(save_xml):
    """
    TEST :branch : base='string', pattern='[a-c-1-4x-z-7-9]*',
    value='a-1z8', type='valid', RULE='14'
    """
    assert_bindings(
        schema="msData/regex/reG31.xsd",
        instance="msData/regex/reG31.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_g30_re_g30_v(save_xml):
    """
    TEST :branch : base='string', pattern='[a-c-1-4x-z-7-9]*',
    value='a1z-9', type='valid', RULE='14'
    """
    assert_bindings(
        schema="msData/regex/reG30.xsd",
        instance="msData/regex/reG30.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_g29_re_g29_v(save_xml):
    """
    TEST :branch : base='string', pattern='[a-c-1-4x-z-7-9]*',
    value='a-1z-8a-1z-9', type='valid', RULE='14'
    """
    assert_bindings(
        schema="msData/regex/reG29.xsd",
        instance="msData/regex/reG29.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_g28_re_g28_v(save_xml):
    """
    TEST :branch : base='string', pattern='[a-c-1-4x-z-7-9]*',
    value='c-4z-9', type='valid', RULE='14'
    """
    assert_bindings(
        schema="msData/regex/reG28.xsd",
        instance="msData/regex/reG28.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_g27_re_g27_v(save_xml):
    """
    TEST :branch : base='string', pattern='[a-c-1-4x-z-7-9]*',
    value='a-1x-7', type='valid', RULE='14'
    """
    assert_bindings(
        schema="msData/regex/reG27.xsd",
        instance="msData/regex/reG27.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_g26_re_g26_v(save_xml):
    """
    TEST :branch : base='string', pattern='[a-c-1-4x-z-7-9]*', value='',
    type='valid', RULE='14'
    """
    assert_bindings(
        schema="msData/regex/reG26.xsd",
        instance="msData/regex/reG26.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_g25_re_g25_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='[\S\D\?a-c\?]+',
    value='?#x9;?', type='invalid', RULE='14'
    """
    assert_bindings(
        schema="msData/regex/reG25.xsd",
        instance="msData/regex/reG25.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_g24_re_g24_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='[\S\D\?a-c\?]+', value='? ?',
    type='invalid', RULE='14'
    """
    assert_bindings(
        schema="msData/regex/reG24.xsd",
        instance="msData/regex/reG24.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_g23_re_g23_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='[\S\D\?a-c\?]+', value='?1?',
    type='invalid', RULE='14'
    """
    assert_bindings(
        schema="msData/regex/reG23.xsd",
        instance="msData/regex/reG23.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_g22_re_g22_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='[\S\D\?a-c\?]+', value='?',
    type='valid', RULE='14'
    """
    assert_bindings(
        schema="msData/regex/reG22.xsd",
        instance="msData/regex/reG22.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_g21_re_g21_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='[\S\D\?a-c\?]+', value='?d?',
    type='invalid', RULE='14'
    """
    assert_bindings(
        schema="msData/regex/reG21.xsd",
        instance="msData/regex/reG21.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_g20_re_g20_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='[\S\D\?a-c\?]+', value='?c?',
    type='valid', RULE='14'
    """
    assert_bindings(
        schema="msData/regex/reG20.xsd",
        instance="msData/regex/reG20.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_g19_re_g19_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='[\S\D\?a-c\?]+', value='?b?',
    type='valid', RULE='14'
    """
    assert_bindings(
        schema="msData/regex/reG19.xsd",
        instance="msData/regex/reG19.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_g18_re_g18_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='[\S\D\?a-c\?]+', value='?a?',
    type='valid', RULE='14'
    """
    assert_bindings(
        schema="msData/regex/reG18.xsd",
        instance="msData/regex/reG18.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_g17_re_g17_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='[\\-\{^]', value='',
    type='error', RULE='12,13,14,17'
    """
    assert_bindings(
        schema="msData/regex/reG17.xsd",
        instance="msData/regex/reG17.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_g16_re_g16_i(save_xml):
    """
    TEST :branch : base='string', pattern='[^a-z^]', value='',
    type='error', RULE='12,13,14,17'
    """
    assert_bindings(
        schema="msData/regex/reG16.xsd",
        instance="msData/regex/reG16.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_g14_re_g14_v(save_xml):
    r"""
    TEST :branch : base='string',
    pattern='[\\\|\.\?\*\+\(\)\{\}\-\[\]\^]*', value='\|.?*+(){}-[]^',
    type='valid', RULE='12,13,14,17'
    """
    assert_bindings(
        schema="msData/regex/reG14.xsd",
        instance="msData/regex/reG14.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_g13_re_g13_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='[\t]', value='#x9;',
    type='valid', RULE='12,13,14,17'
    """
    assert_bindings(
        schema="msData/regex/reG13.xsd",
        instance="msData/regex/reG13.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_g11_re_g11_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='[\n]', value='#xA;',
    type='valid', RULE='12,13,14,17'
    """
    assert_bindings(
        schema="msData/regex/reG11.xsd",
        instance="msData/regex/reG11.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_g10_re_g10_i(save_xml):
    """
    TEST :branch : base='string', pattern='[0-z]*', value='/',
    type='invalid', RULE='12,13,14,17'
    """
    assert_bindings(
        schema="msData/regex/reG10.xsd",
        instance="msData/regex/reG10.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_g9_re_g9_i(save_xml):
    """
    TEST :branch : base='string', pattern='[0-z]*', value='{',
    type='invalid', RULE='12,13,14,17'
    """
    assert_bindings(
        schema="msData/regex/reG9.xsd",
        instance="msData/regex/reG9.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_g8_re_g8_v(save_xml):
    """
    TEST :branch : base='string', pattern='[0-z]*',
    value='1234567890:;<=>?@Azaz', type='valid', RULE='12,13,14,17'
    """
    assert_bindings(
        schema="msData/regex/reG8.xsd",
        instance="msData/regex/reG8.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_g7_re_g7_i(save_xml):
    """
    TEST :branch : base='string', pattern='[a-a]', value='b',
    type='invalid', RULE='12,13,14,17'
    """
    assert_bindings(
        schema="msData/regex/reG7.xsd",
        instance="msData/regex/reG7.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_g6_re_g6_v(save_xml):
    """
    TEST :branch : base='string', pattern='[a-a]', value='a',
    type='valid', RULE='12,13,14,17'
    """
    assert_bindings(
        schema="msData/regex/reG6.xsd",
        instance="msData/regex/reG6.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_g4_re_g4_v(save_xml):
    """
    TEST :branch : base='string', pattern='[1-3]{1,4}', value='123',
    type='valid', RULE='12,13,14,17'
    """
    assert_bindings(
        schema="msData/regex/reG4.xsd",
        instance="msData/regex/reG4.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_g3_re_g3_i(save_xml):
    """
    TEST :branch : base='string', pattern='[a]', value='', type='invalid',
    RULE='12,13,14,17'
    """
    assert_bindings(
        schema="msData/regex/reG3.xsd",
        instance="msData/regex/reG3.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_g2_re_g2_i(save_xml):
    """
    TEST :branch : base='string', pattern='[a]', value='b',
    type='invalid', RULE='12,13,14,17'
    """
    assert_bindings(
        schema="msData/regex/reG2.xsd",
        instance="msData/regex/reG2.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_f55_re_f55_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='[a-\}-]', value='}-',
    type='valid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF55.xsd",
        instance="msData/regex/reF55.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_f54_re_f54_v(save_xml):
    """
    TEST :branch : base='string', pattern='[a-abc]', value='abc',
    type='valid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF54.xsd",
        instance="msData/regex/reF54.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_f53_re_f53_i(save_xml):
    """
    TEST :branch : base='string', pattern='^^a', value='^a',
    type='invalid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF53.xsd",
        instance="msData/regex/reF53.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_f52_re_f52_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='^\^a', value='^', type='valid',
    RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF52.xsd",
        instance="msData/regex/reF52.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_f51_re_f51_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\c^\d\c', value='a r',
    type='invalid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF51.xsd",
        instance="msData/regex/reF51.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_f50_re_f50_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\c^\d\c', value='a c',
    type='invalid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF50.xsd",
        instance="msData/regex/reF50.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_f49_re_f49_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\c^\d\c', value='a z',
    type='invalid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF49.xsd",
        instance="msData/regex/reF49.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_f48_re_f48_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\c^\d\c', value='a c',
    type='invalid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF48.xsd",
        instance="msData/regex/reF48.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_f47_re_f47_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='\c^\d\c', value='aa',
    type='invalid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF47.xsd",
        instance="msData/regex/reF47.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_f46_re_f46_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\c^\d\c', value='a*a',
    type='valid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF46.xsd",
        instance="msData/regex/reF46.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_f45_re_f45_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='(^\?)*', value='a+*abc',
    type='valid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF45.xsd",
        instance="msData/regex/reF45.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_f44_re_f44_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='^\?', value='?',
    type='invalid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF44.xsd",
        instance="msData/regex/reF44.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_f43_re_f43_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='^\P{IsBasicLatin}', value='a',
    type='valid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF43.xsd",
        instance="msData/regex/reF43.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_f42_re_f42_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='^\P{IsBasicLatin}',
    value='#x0100;', type='invalid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF42.xsd",
        instance="msData/regex/reF42.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_f41_re_f41_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='^\p{IsBasicLatin}', value='a',
    type='invalid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF41.xsd",
        instance="msData/regex/reF41.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_f40_re_f40_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='^\p{IsBasicLatin}',
    value='#x0100;', type='valid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF40.xsd",
        instance="msData/regex/reF40.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_f39_re_f39_i(save_xml):
    """
    TEST :branch : base='string', pattern='[a-z-[^a]]', value='b',
    type='invalid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF39.xsd",
        instance="msData/regex/reF39.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_f36_re_f36_i(save_xml):
    """
    TEST :branch : base='string', pattern='[a-c-[^a-c]]', value='d',
    type='invalid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF36.xsd",
        instance="msData/regex/reF36.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_f34_re_f34_i(save_xml):
    """
    TEST :branch : base='string', pattern='[a-b-[0-9]]+', value='a1',
    type='invalid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF34.xsd",
        instance="msData/regex/reF34.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_f32_re_f32_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='[a-\}]+', value='abcxyz}',
    type='valid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF32.xsd",
        instance="msData/regex/reF32.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_f23_re_f23_i(save_xml):
    """
    TEST :branch : base='string', pattern='[^a-d-b-c]', value='cc',
    type='invalid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF23.xsd",
        instance="msData/regex/reF23.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_f22_re_f22_i(save_xml):
    """
    TEST :branch : base='string', pattern='[^a-d-b-c]', value='ab',
    type='invalid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF22.xsd",
        instance="msData/regex/reF22.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_f21_re_f21_i(save_xml):
    """
    TEST :branch : base='string', pattern='[^a-d-b-c]', value='c-c',
    type='valid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF21.xsd",
        instance="msData/regex/reF21.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_f20_re_f20_i(save_xml):
    """
    TEST :branch : base='string', pattern='[^a-d-b-c]', value='a-b',
    type='valid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF20.xsd",
        instance="msData/regex/reF20.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_f18_re_f18_i(save_xml):
    """
    TEST :branch : base='string', pattern='[a-d-[b-c]]', value='c',
    type='invalid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF18.xsd",
        instance="msData/regex/reF18.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_f17_re_f17_i(save_xml):
    """
    TEST :branch : base='string', pattern='[a-d-[b-c]]', value='b',
    type='invalid', RULE='15,16'
    """
    assert_bindings(
        schema="msData/regex/reF17.xsd",
        instance="msData/regex/reF17.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_f15_re_f15_i(save_xml):
    """
    TEST :branch : base='string', pattern='[^-z]+', value='a-z',
    type='invalid', RULE='15'
    """
    assert_bindings(
        schema="msData/regex/reF15.xsd",
        instance="msData/regex/reF15.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_f14_re_f14_i(save_xml):
    """
    TEST :branch : base='string', pattern='[^-z]+', value='aaz',
    type='valid', RULE='15'
    """
    assert_bindings(
        schema="msData/regex/reF14.xsd",
        instance="msData/regex/reF14.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_f13_re_f13_i(save_xml):
    """
    TEST :branch : base='string', pattern='[^(]{0,2}', value='@',
    type='invalid', RULE='15'
    """
    assert_bindings(
        schema="msData/regex/reF13.xsd",
        instance="msData/regex/reF13.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_f12_re_f12_v(save_xml):
    """
    TEST :branch : base='string', pattern='[^(]{0,2}', value=' a',
    type='valid', RULE='15'
    """
    assert_bindings(
        schema="msData/regex/reF12.xsd",
        instance="msData/regex/reF12.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_f11_re_f11_v(save_xml):
    """
    TEST :branch : base='string', pattern='[^(]{0,2}', value='ab',
    type='valid', RULE='15'
    """
    assert_bindings(
        schema="msData/regex/reF11.xsd",
        instance="msData/regex/reF11.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_f10_re_f10_v(save_xml):
    """
    TEST :branch : base='string', pattern='[^(]{0,2}', value='a',
    type='valid', RULE='15'
    """
    assert_bindings(
        schema="msData/regex/reF10.xsd",
        instance="msData/regex/reF10.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_f9_re_f9_v(save_xml):
    """
    TEST :branch : base='string', pattern='[^(]{0,2}', value='',
    type='valid', RULE='15'
    """
    assert_bindings(
        schema="msData/regex/reF9.xsd",
        instance="msData/regex/reF9.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_f8_re_f8_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='[^\s]{3}', value='a c',
    type='invalid', RULE='15'
    """
    assert_bindings(
        schema="msData/regex/reF8.xsd",
        instance="msData/regex/reF8.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_f7_re_f7_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='[^\s]{3}', value='abc',
    type='valid', RULE='15'
    """
    assert_bindings(
        schema="msData/regex/reF7.xsd",
        instance="msData/regex/reF7.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_f6_re_f6_i(save_xml):
    """
    TEST :branch : base='string', pattern='[^2-9a-x]{2}', value='1x',
    type='invalid', RULE='15'
    """
    assert_bindings(
        schema="msData/regex/reF6.xsd",
        instance="msData/regex/reF6.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_f4_re_f4_v(save_xml):
    """
    TEST :branch : base='string', pattern='[^2-9a-x]{2}', value='1z',
    type='valid', RULE='15'
    """
    assert_bindings(
        schema="msData/regex/reF4.xsd",
        instance="msData/regex/reF4.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_e14_re_e14_v(save_xml):
    r"""
    TEST :branch : base='string',
    pattern='(([\.\\\?\*\+\{\}\[\]\(\)\|]?)*)+',
    value='.\?*+{}[]()|.\?*+{}[]()|.\?*+{}[]()|', type='valid', RULE='10'
    """
    assert_bindings(
        schema="msData/regex/reE14.xsd",
        instance="msData/regex/reE14.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_e13_re_e13_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='\.\\\?\*\+\{\}\[\]\(\)\|',
    value='.\?*+{}[]()|', type='valid', RULE='10'
    """
    assert_bindings(
        schema="msData/regex/reE13.xsd",
        instance="msData/regex/reE13.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_e10_re_e10_v(save_xml):
    """
    TEST :branch : base='string', pattern='|', value='', type='error',
    RULE='10'. This is valid because branch allow zero or more pieces. A
    single '|' will be same ase EMPTY, it will not allow anything.
    """
    assert_bindings(
        schema="msData/regex/reE10.xsd",
        instance="msData/regex/reE10.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_d8_re_d8_i(save_xml):
    """
    TEST :branch : base='string',
    pattern='(((((boy)|(girl))[0-1][x-z]{2})?)|(man|woman)[0-1]?[y|n])*',
    value='boyxx', type='invalid', RULE='2,3,4,5,6,7,8,9'
    """
    assert_bindings(
        schema="msData/regex/reD8.xsd",
        instance="msData/regex/reD8.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_d7_re_d7_i(save_xml):
    """
    TEST :branch : base='string',
    pattern='(((((boy)|(girl))[0-1][x-z]{2})?)|(man|woman)[0-1]?[y|n])*',
    value='boy0xxwoman1ygirl1xyman', type='invalid',
    RULE='2,3,4,5,6,7,8,9'
    """
    assert_bindings(
        schema="msData/regex/reD7.xsd",
        instance="msData/regex/reD7.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_d6_re_d6_v(save_xml):
    """
    TEST :branch : base='string',
    pattern='(((((boy)|(girl))[0-1][x-z]{2})?)|(man|woman)[0-1]?[y|n])*',
    value='boy0xxwoman1ygirl1xymanyboy0xxwoman1ygirl1xymany',
    type='valid', RULE='2,3,4,5,6,7,8,9'
    """
    assert_bindings(
        schema="msData/regex/reD6.xsd",
        instance="msData/regex/reD6.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_d5_re_d5_v(save_xml):
    """
    TEST :branch : base='string',
    pattern='(((((boy)|(girl))[0-1][x-z]{2})?)|(man|woman)[0-1]?[y|n])*',
    value='boy0xxwoman1ygirl1xymany', type='valid', RULE='2,3,4,5,6,7,8,9'
    """
    assert_bindings(
        schema="msData/regex/reD5.xsd",
        instance="msData/regex/reD5.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_d4_re_d4_v(save_xml):
    """
    TEST :branch : base='string',
    pattern='(((((boy)|(girl))[0-1][x-z]{2})?)|(man|woman)[0-1]?[y|n])*',
    value='girl1xymany', type='valid', RULE='2,3,4,5,6,7,8,9'
    """
    assert_bindings(
        schema="msData/regex/reD4.xsd",
        instance="msData/regex/reD4.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_d3_re_d3_v(save_xml):
    """
    TEST :branch : base='string',
    pattern='(((((boy)|(girl))[0-1][x-z]{2})?)|(man|woman)[0-1]?[y|n])*',
    value='woman1y', type='valid', RULE='2,3,4,5,6,7,8,9'
    """
    assert_bindings(
        schema="msData/regex/reD3.xsd",
        instance="msData/regex/reD3.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_d2_re_d2_v(save_xml):
    """
    TEST :branch : base='string',
    pattern='(((((boy)|(girl))[0-1][x-z]{2})?)|(man|woman)[0-1]?[y|n])*',
    value='boy0xx', type='valid', RULE='2,3,4,5,6,7,8,9'
    """
    assert_bindings(
        schema="msData/regex/reD2.xsd",
        instance="msData/regex/reD2.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_d1_re_d1_v(save_xml):
    """
    TEST :branch : base='string',
    pattern='(((((boy)|(girl))[0-1][x-z]{2})?)|(man|woman)[0-1]?[y|n])*',
    value='', type='valid', RULE='2,3,4,5,6,7,8,9'
    """
    assert_bindings(
        schema="msData/regex/reD1.xsd",
        instance="msData/regex/reD1.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c84_re_c84_i(save_xml):
    """
    TEST :branch : base='string', pattern='a{0,1}b{1,2}c{2,3}',
    value='abbcccc', type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC84.xsd",
        instance="msData/regex/reC84.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c83_re_c83_i(save_xml):
    """
    TEST :branch : base='string', pattern='a{0,1}b{1,2}c{2,3}',
    value='abbc', type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC83.xsd",
        instance="msData/regex/reC83.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c82_re_c82_i(save_xml):
    """
    TEST :branch : base='string', pattern='a{0,1}b{1,2}c{2,3}',
    value='aabcc', type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC82.xsd",
        instance="msData/regex/reC82.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c81_re_c81_i(save_xml):
    """
    TEST :branch : base='string', pattern='a{0,1}b{1,2}c{2,3}',
    value='acc', type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC81.xsd",
        instance="msData/regex/reC81.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c80_re_c80_i(save_xml):
    """
    TEST :branch : base='string', pattern='a{0,1}b{1,2}c{2,3}',
    value='bbbcc', type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC80.xsd",
        instance="msData/regex/reC80.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c79_re_c79_i(save_xml):
    """
    TEST :branch : base='string', pattern='a{0,1}b{1,2}c{2,3}',
    value='aabcc', type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC79.xsd",
        instance="msData/regex/reC79.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_c78_re_c78_v(save_xml):
    """
    TEST :branch : base='string', pattern='a{0,1}b{1,2}c{2,3}',
    value='bbccc', type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC78.xsd",
        instance="msData/regex/reC78.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_c77_re_c77_v(save_xml):
    """
    TEST :branch : base='string', pattern='a{0,1}b{1,2}c{2,3}',
    value='bbcc', type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC77.xsd",
        instance="msData/regex/reC77.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_c76_re_c76_v(save_xml):
    """
    TEST :branch : base='string', pattern='a{0,1}b{1,2}c{2,3}',
    value='abbccc', type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC76.xsd",
        instance="msData/regex/reC76.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_c75_re_c75_v(save_xml):
    """
    TEST :branch : base='string', pattern='a{0,1}b{1,2}c{2,3}',
    value='abbcc', type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC75.xsd",
        instance="msData/regex/reC75.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_c74_re_c74_v(save_xml):
    """
    TEST :branch : base='string', pattern='a{0,1}b{1,2}c{2,3}',
    value='abccc', type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC74.xsd",
        instance="msData/regex/reC74.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_c73_re_c73_v(save_xml):
    """
    TEST :branch : base='string', pattern='a{0,1}b{1,2}c{2,3}',
    value='abcc', type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC73.xsd",
        instance="msData/regex/reC73.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c72_re_c72_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab{0,0}', value='ab',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC72.xsd",
        instance="msData/regex/reC72.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c71_re_c71_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab{0,0}', value='a',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC71.xsd",
        instance="msData/regex/reC71.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_c70_re_c70_v(save_xml):
    """
    TEST :branch : base='string', pattern='ab{0,0}', value='',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC70.xsd",
        instance="msData/regex/reC70.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c64_re_c64_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab{2,}', value='',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC64.xsd",
        instance="msData/regex/reC64.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c63_re_c63_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab{2,}', value='abab abab',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC63.xsd",
        instance="msData/regex/reC63.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c62_re_c62_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab{2,}', value='ababababa',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC62.xsd",
        instance="msData/regex/reC62.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c61_re_c61_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab{2,}', value='ababaa',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC61.xsd",
        instance="msData/regex/reC61.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c60_re_c60_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab{2,}', value='ababa',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC60.xsd",
        instance="msData/regex/reC60.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c59_re_c59_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab{2,}', value='ab',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC59.xsd",
        instance="msData/regex/reC59.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_c58_re_c58_v(save_xml):
    """
    TEST :branch : base='string', pattern='ab{2,}', value='abababababababa
    bababababababababababababababababababababababababab', type='valid',
    RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC58.xsd",
        instance="msData/regex/reC58.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_c57_re_c57_v(save_xml):
    """
    TEST :branch : base='string', pattern='ab{2,}', value='ababab',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC57.xsd",
        instance="msData/regex/reC57.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_c56_re_c56_v(save_xml):
    """
    TEST :branch : base='string', pattern='ab{2,}', value='abab',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC56.xsd",
        instance="msData/regex/reC56.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c55_re_c55_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='(a\sb){0,2}', value='a b',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC55.xsd",
        instance="msData/regex/reC55.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c54_re_c54_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='(a\sb){0,2}', value='a b a b',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC54.xsd",
        instance="msData/regex/reC54.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c53_re_c53_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='(a\sb){0,2}', value='ab',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC53.xsd",
        instance="msData/regex/reC53.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c52_re_c52_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='(a\sb){0,2}', value='a ba ba
    b', type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC52.xsd",
        instance="msData/regex/reC52.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_c51_re_c51_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='(a\sb){0,2}', value='a ba b',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC51.xsd",
        instance="msData/regex/reC51.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_c50_re_c50_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='(a\sb){0,2}', value='a b',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC50.xsd",
        instance="msData/regex/reC50.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_c49_re_c49_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='(a\sb){0,2}', value='',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC49.xsd",
        instance="msData/regex/reC49.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c48_re_c48_i(save_xml):
    """
    TEST :branch : base='string', pattern='((ab)(ac){0,2})?',
    value='abacabac', type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC48.xsd",
        instance="msData/regex/reC48.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c47_re_c47_i(save_xml):
    """
    TEST :branch : base='string', pattern='((ab)(ac){0,2})?',
    value='abab', type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC47.xsd",
        instance="msData/regex/reC47.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c46_re_c46_i(save_xml):
    """
    TEST :branch : base='string', pattern='((ab)(ac){0,2})?',
    value='abaca', type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC46.xsd",
        instance="msData/regex/reC46.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c45_re_c45_i(save_xml):
    """
    TEST :branch : base='string', pattern='((ab)(ac){0,2})?',
    value='abacacac', type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC45.xsd",
        instance="msData/regex/reC45.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c44_re_c44_i(save_xml):
    """
    TEST :branch : base='string', pattern='((ab)(ac){0,2})?', value='ac',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC44.xsd",
        instance="msData/regex/reC44.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_c43_re_c43_v(save_xml):
    """
    TEST :branch : base='string', pattern='((ab)(ac){0,2})?',
    value='abacac', type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC43.xsd",
        instance="msData/regex/reC43.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_c42_re_c42_v(save_xml):
    """
    TEST :branch : base='string', pattern='((ab)(ac){0,2})?',
    value='abac', type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC42.xsd",
        instance="msData/regex/reC42.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_c41_re_c41_v(save_xml):
    """
    TEST :branch : base='string', pattern='((ab)(ac){0,2})?', value='ab',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC41.xsd",
        instance="msData/regex/reC41.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c40_re_c40_i(save_xml):
    """
    TEST :branch : base='string', pattern='a*b{2,4}c{0}', value='',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC40.xsd",
        instance="msData/regex/reC40.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c39_re_c39_i(save_xml):
    """
    TEST :branch : base='string', pattern='a*b{2,4}c{0}', value='abbbbb',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC39.xsd",
        instance="msData/regex/reC39.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c38_re_c38_i(save_xml):
    """
    TEST :branch : base='string', pattern='a*b{2,4}c{0}', value='bbc',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC38.xsd",
        instance="msData/regex/reC38.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c37_re_c37_i(save_xml):
    """
    TEST :branch : base='string', pattern='a*b{2,4}c{0}', value='abbc',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC37.xsd",
        instance="msData/regex/reC37.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c36_re_c36_i(save_xml):
    """
    TEST :branch : base='string', pattern='a*b{2,4}c{0}', value='ab',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC36.xsd",
        instance="msData/regex/reC36.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_c35_re_c35_v(save_xml):
    """
    TEST :branch : base='string', pattern='a*b{2,4}c{0}', value='bbbb',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC35.xsd",
        instance="msData/regex/reC35.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_c34_re_c34_v(save_xml):
    """
    TEST :branch : base='string', pattern='a*b{2,4}c{0}', value='bbb',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC34.xsd",
        instance="msData/regex/reC34.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_c33_re_c33_v(save_xml):
    """
    TEST :branch : base='string', pattern='a*b{2,4}c{0}', value='bb',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC33.xsd",
        instance="msData/regex/reC33.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_c32_re_c32_v(save_xml):
    """
    TEST :branch : base='string', pattern='a*b{2,4}c{0}', value='aaabbb',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC32.xsd",
        instance="msData/regex/reC32.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c31_re_c31_i(save_xml):
    """
    TEST :branch : base='string', pattern='abc{2}', value='',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC31.xsd",
        instance="msData/regex/reC31.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c30_re_c30_i(save_xml):
    """
    TEST :branch : base='string', pattern='abc{2}', value='abccc',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC30.xsd",
        instance="msData/regex/reC30.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c29_re_c29_i(save_xml):
    """
    TEST :branch : base='string', pattern='abc{2}', value='abc',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC29.xsd",
        instance="msData/regex/reC29.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_c28_re_c28_v(save_xml):
    """
    TEST :branch : base='string', pattern='abc{2}', value='abcc',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC28.xsd",
        instance="msData/regex/reC28.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c27_re_c27_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab{2}c', value='',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC27.xsd",
        instance="msData/regex/reC27.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c26_re_c26_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab{2}c', value='a',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC26.xsd",
        instance="msData/regex/reC26.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c25_re_c25_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab{2}c', value='abbbc',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC25.xsd",
        instance="msData/regex/reC25.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c24_re_c24_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab{2}c', value='abc',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC24.xsd",
        instance="msData/regex/reC24.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c23_re_c23_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab{2}c', value='ac',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC23.xsd",
        instance="msData/regex/reC23.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_c22_re_c22_v(save_xml):
    """
    TEST :branch : base='string', pattern='ab{2}c', value='abbc',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC22.xsd",
        instance="msData/regex/reC22.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c21_re_c21_i(save_xml):
    """
    TEST :branch : base='string', pattern='(a{2})*', value='aaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC21.xsd",
        instance="msData/regex/reC21.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c20_re_c20_i(save_xml):
    """
    TEST :branch : base='string', pattern='(a{2})*', value='aaa',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC20.xsd",
        instance="msData/regex/reC20.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c19_re_c19_i(save_xml):
    """
    TEST :branch : base='string', pattern='(a{2})*', value='a',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC19.xsd",
        instance="msData/regex/reC19.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_c18_re_c18_v(save_xml):
    """
    TEST :branch : base='string', pattern='(a{2})*', value='aaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC18.xsd",
        instance="msData/regex/reC18.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_c17_re_c17_v(save_xml):
    """
    TEST :branch : base='string', pattern='(a{2})*', value='aa',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC17.xsd",
        instance="msData/regex/reC17.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_c16_re_c16_v(save_xml):
    """
    TEST :branch : base='string', pattern='(a{2})*', value='',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC16.xsd",
        instance="msData/regex/reC16.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c15_re_c15_i(save_xml):
    """
    TEST :branch : base='string', pattern='(a{2})+', value='aaa',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC15.xsd",
        instance="msData/regex/reC15.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c14_re_c14_i(save_xml):
    """
    TEST :branch : base='string', pattern='(a{2})+', value='a2',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC14.xsd",
        instance="msData/regex/reC14.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c13_re_c13_i(save_xml):
    """
    TEST :branch : base='string', pattern='(a{2})+', value='a',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC13.xsd",
        instance="msData/regex/reC13.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c12_re_c12_i(save_xml):
    """
    TEST :branch : base='string', pattern='(a{2})+', value='',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC12.xsd",
        instance="msData/regex/reC12.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_c11_re_c11_v(save_xml):
    """
    TEST :branch : base='string', pattern='(a{2})+',
    value='aaaaaaaaaaaaaaaaaaaa', type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC11.xsd",
        instance="msData/regex/reC11.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_c10_re_c10_v(save_xml):
    """
    TEST :branch : base='string', pattern='(a{2})+', value='aaaa',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC10.xsd",
        instance="msData/regex/reC10.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_c9_re_c9_v(save_xml):
    """
    TEST :branch : base='string', pattern='(a{2})+', value='aa',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC9.xsd",
        instance="msData/regex/reC9.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c8_re_c8_i(save_xml):
    """
    TEST :branch : base='string', pattern='((ab){2})?', value='abababab',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC8.xsd",
        instance="msData/regex/reC8.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c7_re_c7_i(save_xml):
    """
    TEST :branch : base='string', pattern='((ab){2})?', value='ababa',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC7.xsd",
        instance="msData/regex/reC7.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c6_re_c6_i(save_xml):
    """
    TEST :branch : base='string', pattern='((ab){2})?', value='ab',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC6.xsd",
        instance="msData/regex/reC6.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c5_re_c5_i(save_xml):
    """
    TEST :branch : base='string', pattern='((ab){2})?', value='a',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC5.xsd",
        instance="msData/regex/reC5.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_c4_re_c4_v(save_xml):
    """
    TEST :branch : base='string', pattern='((ab){2})?', value='',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC4.xsd",
        instance="msData/regex/reC4.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_c3_re_c3_v(save_xml):
    """
    TEST :branch : base='string', pattern='((ab){2})?', value='abab',
    type='valid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC3.xsd",
        instance="msData/regex/reC3.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_c2_re_c2_v(save_xml):
    """
    TEST :branch : base='string', pattern='a{0}', value='', type='valid',
    RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC2.xsd",
        instance="msData/regex/reC2.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_c1_re_c1_i(save_xml):
    """
    TEST :branch : base='string', pattern='a{0}', value='a',
    type='invalid', RULE='2,3,4,5,6,7,8'
    """
    assert_bindings(
        schema="msData/regex/reC1.xsd",
        instance="msData/regex/reC1.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_b78_re_b78_v(save_xml):
    """
    TEST :branch : base='string', pattern='a{0}', value='', type='valid',
    RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB78.xsd",
        instance="msData/regex/reB78.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b61_re_b61_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='(ab+c)a?\?\??', value='abc???',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB61.xsd",
        instance="msData/regex/reB61.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b60_re_b60_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='(ab+c)a?\?\??', value='abc',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB60.xsd",
        instance="msData/regex/reB60.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b59_re_b59_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='(ab+c)a?\?\??', value='bc??',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB59.xsd",
        instance="msData/regex/reB59.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b58_re_b58_i(save_xml):
    r"""
    TEST :branch : base='string', pattern='(ab+c)a?\?\??', value='ac??',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB58.xsd",
        instance="msData/regex/reB58.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_b57_re_b57_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='(ab+c)a?\?\??',
    value='abbbbca?', type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB57.xsd",
        instance="msData/regex/reB57.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_b56_re_b56_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='(ab+c)a?\?\??', value='abca??',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB56.xsd",
        instance="msData/regex/reB56.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_b55_re_b55_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='(ab+c)a?\?\??',
    value='abbbc??', type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB55.xsd",
        instance="msData/regex/reB55.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_b54_re_b54_v(save_xml):
    r"""
    TEST :branch : base='string', pattern='(ab+c)a?\?\??', value='abc?',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB54.xsd",
        instance="msData/regex/reB54.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b53_re_b53_i(save_xml):
    """
    TEST :branch : base='string', pattern='a?b+c*', value='',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB53.xsd",
        instance="msData/regex/reB53.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b52_re_b52_i(save_xml):
    """
    TEST :branch : base='string', pattern='a?b+c*', value='ac',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB52.xsd",
        instance="msData/regex/reB52.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b51_re_b51_i(save_xml):
    """
    TEST :branch : base='string', pattern='a?b+c*', value='c',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB51.xsd",
        instance="msData/regex/reB51.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b50_re_b50_i(save_xml):
    """
    TEST :branch : base='string', pattern='a?b+c*', value='a',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB50.xsd",
        instance="msData/regex/reB50.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b49_re_b49_i(save_xml):
    """
    TEST :branch : base='string', pattern='a?b+c*', value='aabc',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB49.xsd",
        instance="msData/regex/reB49.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_b48_re_b48_v(save_xml):
    """
    TEST :branch : base='string', pattern='a?b+c*', value='abbbc',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB48.xsd",
        instance="msData/regex/reB48.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_b47_re_b47_v(save_xml):
    """
    TEST :branch : base='string', pattern='a?b+c*', value='abc',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB47.xsd",
        instance="msData/regex/reB47.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_b46_re_b46_v(save_xml):
    """
    TEST :branch : base='string', pattern='a?b+c*', value='bcccccc',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB46.xsd",
        instance="msData/regex/reB46.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_b45_re_b45_v(save_xml):
    """
    TEST :branch : base='string', pattern='a?b+c*', value='ab',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB45.xsd",
        instance="msData/regex/reB45.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_b44_re_b44_v(save_xml):
    """
    TEST :branch : base='string', pattern='a?b+c*', value='b',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB44.xsd",
        instance="msData/regex/reB44.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b43_re_b43_i(save_xml):
    """
    TEST :branch : base='string', pattern='abc*', value='',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB43.xsd",
        instance="msData/regex/reB43.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b42_re_b42_i(save_xml):
    """
    TEST :branch : base='string', pattern='abc*', value='abbc',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB42.xsd",
        instance="msData/regex/reB42.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b41_re_b41_i(save_xml):
    """
    TEST :branch : base='string', pattern='abc*', value='abcd',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB41.xsd",
        instance="msData/regex/reB41.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b40_re_b40_i(save_xml):
    """
    TEST :branch : base='string', pattern='abc*', value='a',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB40.xsd",
        instance="msData/regex/reB40.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_b39_re_b39_v(save_xml):
    """
    TEST :branch : base='string', pattern='abc*', value='abccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccc', type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB39.xsd",
        instance="msData/regex/reB39.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_b38_re_b38_v(save_xml):
    """
    TEST :branch : base='string', pattern='abc*', value='ab',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB38.xsd",
        instance="msData/regex/reB38.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_b37_re_b37_v(save_xml):
    """
    TEST :branch : base='string', pattern='abc*', value='abc',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB37.xsd",
        instance="msData/regex/reB37.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b36_re_b36_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab*c', value='',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB36.xsd",
        instance="msData/regex/reB36.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b35_re_b35_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab*c', value='abcb',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB35.xsd",
        instance="msData/regex/reB35.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b34_re_b34_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab*c', value='c',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB34.xsd",
        instance="msData/regex/reB34.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b33_re_b33_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab*c', value='bc',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB33.xsd",
        instance="msData/regex/reB33.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b32_re_b32_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab*c', value='ab',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB32.xsd",
        instance="msData/regex/reB32.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b31_re_b31_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab*c', value='a',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB31.xsd",
        instance="msData/regex/reB31.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_b30_re_b30_v(save_xml):
    """
    TEST :branch : base='string', pattern='ab*c', value='ac',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB30.xsd",
        instance="msData/regex/reB30.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_b29_re_b29_v(save_xml):
    """
    TEST :branch : base='string', pattern='ab*c', value='abbbbbbbc',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB29.xsd",
        instance="msData/regex/reB29.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_b28_re_b28_v(save_xml):
    """
    TEST :branch : base='string', pattern='ab*c', value='abc',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB28.xsd",
        instance="msData/regex/reB28.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b27_re_b27_i(save_xml):
    """
    TEST :branch : base='string', pattern='abc+', value='abcd',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB27.xsd",
        instance="msData/regex/reB27.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b26_re_b26_i(save_xml):
    """
    TEST :branch : base='string', pattern='abc+', value='ab',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB26.xsd",
        instance="msData/regex/reB26.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b25_re_b25_i(save_xml):
    """
    TEST :branch : base='string', pattern='abc+', value='a',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB25.xsd",
        instance="msData/regex/reB25.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_b24_re_b24_v(save_xml):
    """
    TEST :branch : base='string', pattern='abc+', value='abccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccc', type='valid',
    RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB24.xsd",
        instance="msData/regex/reB24.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_b23_re_b23_v(save_xml):
    """
    TEST :branch : base='string', pattern='abc+', value='abc',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB23.xsd",
        instance="msData/regex/reB23.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b22_re_b22_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab+c', value='',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB22.xsd",
        instance="msData/regex/reB22.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b21_re_b21_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab+c', value='abbb',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB21.xsd",
        instance="msData/regex/reB21.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b20_re_b20_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab+c', value='bbbc',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB20.xsd",
        instance="msData/regex/reB20.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b19_re_b19_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab+c', value='ac',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB19.xsd",
        instance="msData/regex/reB19.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_b18_re_b18_v(save_xml):
    """
    TEST :branch : base='string', pattern='ab+c', value='abbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
    bbbbbbbc', type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB18.xsd",
        instance="msData/regex/reB18.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_b17_re_b17_v(save_xml):
    """
    TEST :branch : base='string', pattern='ab+c', value='abc',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB17.xsd",
        instance="msData/regex/reB17.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b16_re_b16_i(save_xml):
    """
    TEST :branch : base='string', pattern='abc?', value='',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB16.xsd",
        instance="msData/regex/reB16.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b15_re_b15_i(save_xml):
    """
    TEST :branch : base='string', pattern='abc?', value='abcc',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB15.xsd",
        instance="msData/regex/reB15.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b14_re_b14_i(save_xml):
    """
    TEST :branch : base='string', pattern='abc?', value='bc',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB14.xsd",
        instance="msData/regex/reB14.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b13_re_b13_i(save_xml):
    """
    TEST :branch : base='string', pattern='abc?', value='a',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB13.xsd",
        instance="msData/regex/reB13.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_b12_re_b12_v(save_xml):
    """
    TEST :branch : base='string', pattern='abc?', value='abc',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB12.xsd",
        instance="msData/regex/reB12.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_b11_re_b11_v(save_xml):
    """
    TEST :branch : base='string', pattern='abc?', value='ab',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB11.xsd",
        instance="msData/regex/reB11.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b10_re_b10_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab?c', value='',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB10.xsd",
        instance="msData/regex/reB10.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b5_re_b5_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab?c', value='bc',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB5.xsd",
        instance="msData/regex/reB5.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b4_re_b4_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab?c', value='ab',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB4.xsd",
        instance="msData/regex/reB4.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_b3_re_b3_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab?c', value='a',
    type='invalid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB3.xsd",
        instance="msData/regex/reB3.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_b2_re_b2_v(save_xml):
    """
    TEST :branch : base='string', pattern='ab?c', value='abc',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB2.xsd",
        instance="msData/regex/reB2.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_b1_re_b1_v(save_xml):
    """
    TEST :branch : base='string', pattern='ab?c', value='ac',
    type='valid', RULE='2,3,4'
    """
    assert_bindings(
        schema="msData/regex/reB1.xsd",
        instance="msData/regex/reB1.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_a45_re_a45_v(save_xml):
    """
    TEST :branch : base='string', pattern=' a|b ', value='a',
    type='valid', RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA45.xsd",
        instance="msData/regex/reA45.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_a34_re_a34_i(save_xml):
    """
    TEST :branch : base='string', pattern='a|b|a|c|b|d|a', value='e',
    type='invalid', RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA34.xsd",
        instance="msData/regex/reA34.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_a33_re_a33_i(save_xml):
    """
    TEST :branch : base='string', pattern='a|b|a|c|b|d|a', value='ac',
    type='invalid', RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA33.xsd",
        instance="msData/regex/reA33.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_a32_re_a32_i(save_xml):
    """
    TEST :branch : base='string', pattern='a|b|a|c|b|d|a', value='aa',
    type='invalid', RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA32.xsd",
        instance="msData/regex/reA32.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_a31_re_a31_v(save_xml):
    """
    TEST :branch : base='string', pattern='a|b|a|c|b|d|a', value='d',
    type='valid', RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA31.xsd",
        instance="msData/regex/reA31.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_a30_re_a30_v(save_xml):
    """
    TEST :branch : base='string', pattern='a|b|a|c|b|d|a', value='c',
    type='valid', RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA30.xsd",
        instance="msData/regex/reA30.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_a29_re_a29_v(save_xml):
    """
    TEST :branch : base='string', pattern='a|b|a|c|b|d|a', value='b',
    type='valid', RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA29.xsd",
        instance="msData/regex/reA29.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_a28_re_a28_v(save_xml):
    """
    TEST :branch : base='string', pattern='a|b|a|c|b|d|a', value='a',
    type='valid', RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA28.xsd",
        instance="msData/regex/reA28.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_a27_re_a27_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab', value='', type='invalid',
    RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA27.xsd",
        instance="msData/regex/reA27.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_a26_re_a26_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab', value='bb',
    type='invalid', RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA26.xsd",
        instance="msData/regex/reA26.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_a25_re_a25_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab', value='aa',
    type='invalid', RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA25.xsd",
        instance="msData/regex/reA25.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_a24_re_a24_v(save_xml):
    """
    TEST :branch : base='string', pattern='ab', value='ab', type='valid',
    RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA24.xsd",
        instance="msData/regex/reA24.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_a23_re_a23_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab', value='b', type='invalid',
    RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA23.xsd",
        instance="msData/regex/reA23.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_a22_re_a22_i(save_xml):
    """
    TEST :branch : base='string', pattern='ab', value='a', type='invalid',
    RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA22.xsd",
        instance="msData/regex/reA22.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_a21_re_a21_i(save_xml):
    """
    TEST :branch : base='string', pattern='a|b', value='', type='invalid',
    RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA21.xsd",
        instance="msData/regex/reA21.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_a20_re_a20_i(save_xml):
    """
    TEST :branch : base='string', pattern='a|b', value='ab',
    type='invalid', RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA20.xsd",
        instance="msData/regex/reA20.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_a19_re_a19_i(save_xml):
    """
    TEST :branch : base='string', pattern='a|b', value='bb',
    type='invalid', RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA19.xsd",
        instance="msData/regex/reA19.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_a18_re_a18_i(save_xml):
    """
    TEST :branch : base='string', pattern='a|b', value='aa',
    type='invalid', RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA18.xsd",
        instance="msData/regex/reA18.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_a17_re_a17_v(save_xml):
    """
    TEST :branch : base='string', pattern='a|b', value='b', type='valid',
    RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA17.xsd",
        instance="msData/regex/reA17.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_a16_re_a16_v(save_xml):
    """
    TEST :branch : base='string', pattern='a|b', value='a', type='valid',
    RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA16.xsd",
        instance="msData/regex/reA16.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_a15_re_a15_i(save_xml):
    """
    TEST :branch : base='string', pattern='a|a', value='', type='invalid',
    RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA15.xsd",
        instance="msData/regex/reA15.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_a14_re_a14_i(save_xml):
    """
    TEST :branch : base='string', pattern='a|a', value='b',
    type='invalid', RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA14.xsd",
        instance="msData/regex/reA14.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_a13_re_a13_i(save_xml):
    """
    TEST :branch : base='string', pattern='a|a', value='aa',
    type='invalid', RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA13.xsd",
        instance="msData/regex/reA13.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_a12_re_a12_v(save_xml):
    """
    TEST :branch : base='string', pattern='a|a', value='a', type='valid',
    RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA12.xsd",
        instance="msData/regex/reA12.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_a11_re_a11_i(save_xml):
    """
    TEST :branch : base='string', pattern='a', value='', type='invalid',
    RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA11.xsd",
        instance="msData/regex/reA11.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_a10_re_a10_i(save_xml):
    """
    TEST :branch : base='string', pattern='a', value='b', type='invalid',
    RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA10.xsd",
        instance="msData/regex/reA10.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_a9_re_a9_i(save_xml):
    """
    TEST :branch : base='string', pattern='a', value='aa', type='invalid',
    RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA9.xsd",
        instance="msData/regex/reA9.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_a8_re_a8_v(save_xml):
    """
    TEST :branch : base='string', pattern='a', value='a', type='valid',
    RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA8.xsd",
        instance="msData/regex/reA8.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_a7_re_a7_v(save_xml):
    """
    TEST :branch : base='string', pattern='', value='', type='valid',
    RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA7.xsd",
        instance="msData/regex/reA7.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_a6_re_a6_i(save_xml):
    """
    TEST :branch : base='string', pattern='', value='#xA;',
    type='invalid', RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA6.xsd",
        instance="msData/regex/reA6.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_a5_re_a5_i(save_xml):
    """
    TEST :branch : base='string', pattern='', value='#x9;',
    type='invalid', RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA5.xsd",
        instance="msData/regex/reA5.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_a4_re_a4_i(save_xml):
    """
    TEST :branch : base='string', pattern='', value='#xD;',
    type='invalid', RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA4.xsd",
        instance="msData/regex/reA4.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_a3_re_a3_i(save_xml):
    """
    TEST :branch : base='string', pattern='', value='#x20;',
    type='invalid', RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA3.xsd",
        instance="msData/regex/reA3.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_re_a2_re_a2_i(save_xml):
    """
    TEST :branch : base='string', pattern='', value='a', type='invalid',
    RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA2.xsd",
        instance="msData/regex/reA2.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_re_a1_re_a1_v(save_xml):
    """
    TEST :branch : base='string', pattern='', value='', type='valid',
    RULE='1'
    """
    assert_bindings(
        schema="msData/regex/reA1.xsd",
        instance="msData/regex/reA1.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid schema")
def test_sch_u5_sch_u5_i(save_xml):
    """
    TEST :schema collection and schema location : Circulcar redefines
    handeling (5) The WG decided the spec. is underspecified in this area,
    so implementations may reasonably differ
    """
    assert_bindings(
        schema="msData/schema/schU5_a.xsd",
        instance="msData/schema/schU5.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid schema")
def test_sch_u4_sch_u4_i(save_xml):
    """
    TEST :schema collection and schema location : Circulcar redefines
    handeling (4) The WG decided the spec. is underspecified in this area,
    so implementations may reasonably differ
    """
    assert_bindings(
        schema="msData/schema/schU4_a.xsd",
        instance="msData/schema/schU4.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid schema")
def test_sch_u3_sch_u3_i(save_xml):
    """
    TEST :schema collection and schema location : Circulcar redefines
    handeling (3) The WG decided the spec. is underspecified in this area,
    so implementations may reasonably differ
    """
    assert_bindings(
        schema="msData/schema/schU3_a.xsd",
        instance="msData/schema/schU3.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_sch_t10_sch_t10_v(save_xml):
    """
    TEST :schema collection and schema location : redefine with an
    attributeGroup, attribute group's content items are a subset of the
    redefined group, test that attribute uses are not inherited. base
    attriburte with effective value absent, but redefining attribute has
    fixed="bar" , (SRC 7.2.2)
    """
    assert_bindings(
        schema="msData/schema/schT10_a.xsd",
        instance="msData/schema/schT10.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_sch_t9_sch_t9_v(save_xml):
    """
    TEST :schema collection and schema location : redefine with a
    attributeGroup, attribute group's content items are a subset of the
    redefined group, test that attribute uses are not inherited. Have a
    default="foo" in redefined attriubte, but redefining attribute has
    default="bar", the actual value of the instance should have 'bar' as
    the default attribute value (SRC 7.2.2)
    """
    assert_bindings(
        schema="msData/schema/schT9_a.xsd",
        instance="msData/schema/schT9.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_sch_t6_sch_t6_i(save_xml):
    """
    TEST :schema collection and schema location : redefine with an
    attributeGroup, attribute group's content items are a subset of the
    redefined group, test that attribute uses are not inherited. Have a
    use=optional on redefined attriubte, but have use=required in
    redefining attribute, and instance xml has no attribute, (SRC 7.2.2)
    """
    assert_bindings(
        schema="msData/schema/schT6_a.xsd",
        instance="msData/schema/schT6.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_sch_t3_sch_t3_v(save_xml):
    """
    TEST :schema collection and schema location : redefine with a
    attributeGroup, attribute group's content items are a subset of the
    redefined group, (SRC 7.2.2)
    """
    assert_bindings(
        schema="msData/schema/schT3_a.xsd",
        instance="msData/schema/schT3.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_sch_r2_sch_r2_i(save_xml):
    """
    TEST :schema collection and schema location : redefine with a group,
    which has a group ref to itself in the middle, group min,maxOccurs is
    absent, (SRC 6.1.2)
    """
    assert_bindings(
        schema="msData/schema/schR2_a.xsd",
        instance="msData/schema/schR2.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_sch_q3_sch_q3_v(save_xml):
    """
    TEST :schema collection and schema location : redefine with a
    complexType, which has a restriction, (SRC 5)
    """
    assert_bindings(
        schema="msData/schema/schQ3_a.xsd",
        instance="msData/schema/schQ3.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_sch_q1_sch_q1_v(save_xml):
    """
    TEST :schema collection and schema location : redefine with a
    complexType, which has an extension, (SRC 5)
    """
    assert_bindings(
        schema="msData/schema/schQ1_a.xsd",
        instance="msData/schema/schQ1.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_sch_p2_sch_p2_v(save_xml):
    """
    TEST :schema collection and schema location : redefine with a
    complexType, which has a restriction, (SRC 5)
    """
    assert_bindings(
        schema="msData/schema/schP2_a.xsd",
        instance="msData/schema/schP2.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_sch_g12_sch_g12_v(save_xml):
    """
    TEST :schema collection and schema location : A import B, B import C,
    A's ns="A", B's ns="B", C's ns="B", All declaration in B and C should
    be available to validation
    """
    assert_bindings(
        schema="msData/schema/schG12_a.xsd",
        instance="msData/schema/schG12.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_sch_g8_sch_g8_v(save_xml):
    """
    TEST :schema collection and schema location : A import B and C, B is
    bogus URL, C is valid XSD, test that there is no error and C is
    imported.
    """
    assert_bindings(
        schema="msData/schema/schG8_a.xsd",
        instance="msData/schema/schG8.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_sch_g7_sch_g7_v(save_xml):
    """
    TEST :schema collection and schema location : A imports B and B and C,
    B imports C and D, C imports D and A, multiple import of the same XSD
    is ok
    """
    assert_bindings(
        schema="msData/schema/schG7_a.xsd",
        instance="msData/schema/schG7.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_sch_g5_sch_g5_v(save_xml):
    """
    TEST :schema collection and schema location : A import B and C, A's
    ns="A", B's ns="B", C's ns="B", (B and C have no confilcting decl)
    """
    assert_bindings(
        schema="msData/schema/schG5_a.xsd",
        instance="msData/schema/schG5.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_sch_g4_sch_g4_v(save_xml):
    """
    TEST :schema collection and schema location : A import B and C, A's
    ns="A", B's ns="B", C's ns="C"
    """
    assert_bindings(
        schema="msData/schema/schG4_a.xsd",
        instance="msData/schema/schG4.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_sch_g3_sch_g3_v(save_xml):
    """
    TEST :schema collection and schema location : A import B, B import C,
    A's ns="A", B's ns="B", C's ns="A", (A and C have no confilcting decl)
    """
    assert_bindings(
        schema="msData/schema/schG3_a.xsd",
        instance="msData/schema/schG3.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_sch_g2_sch_g2_v(save_xml):
    """
    TEST :schema collection and schema location : A import B, B import C,
    A's ns="A", B's ns="", C's ns="C"
    """
    assert_bindings(
        schema="msData/schema/schG2_a.xsd",
        instance="msData/schema/schG2.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_sch_g1_sch_g1_v(save_xml):
    """
    TEST :schema collection and schema location : A import B, B import C,
    A's ns="A", B's ns="B", C's ns="C"
    """
    assert_bindings(
        schema="msData/schema/schG1_a.xsd",
        instance="msData/schema/schG1.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_sch_f5_sch_f5_v(save_xml):
    """
    TEST :schema collection and schema location : XSD X import XSD Y, X's
    ns="A", Y's ns="B", test the namespace of import
    """
    assert_bindings(
        schema="msData/schema/schF5_a.xsd",
        instance="msData/schema/schF5.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_sch_f2_sch_f2_v(save_xml):
    """
    TEST :schema collection and schema location : XSD X import XSD Y, X's
    ns="", Y's ns="A", test the namespace of import
    """
    assert_bindings(
        schema="msData/schema/schF2_a.xsd",
        instance="msData/schema/schF2.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_sch_f1_sch_f1_v(save_xml):
    """
    TEST :schema collection and schema location : XSD X import XSD Y, X's
    ns="A", Y's ns="", test the namespace of import
    """
    assert_bindings(
        schema="msData/schema/schF1_a.xsd",
        instance="msData/schema/schF1.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_sch_e4_sch_e4_v(save_xml):
    """
    TEST :schema collection and schema location : import namespace="foo"
    """
    assert_bindings(
        schema="msData/schema/schE4.xsd",
        instance="msData/schema/schE4.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_sch_d10_sch_d10_v(save_xml):
    """
    TEST :schema collection and schema location : validate instance
    against 'chameleon' include schema (2)
    """
    assert_bindings(
        schema="msData/schema/schD10_a.xsd",
        instance="msData/schema/schD10.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_sch_d7_sch_d7_v(save_xml):
    """
    TEST :schema collection and schema location : A includes B and C, B is
    bogus URL, C is valid XSD, test that there is no error and C is
    included.
    """
    assert_bindings(
        schema="msData/schema/schD7_a.xsd",
        instance="msData/schema/schD7.xml",
        class_name="Root",
        version="1.1",
        ns_struct=True,
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_sch_d5_sch_d5_v(save_xml):
    """
    TEST :schema collection and schema location : A include B and C, A's
    ns="A", B's ns="A", C's ns="A", type ref from A to B and C, B to A and
    C, C to A and B
    """
    assert_bindings(
        schema="msData/schema/schD5_a.xsd",
        instance="msData/schema/schD5.xml",
        class_name="Root",
        version="1.1",
        ns_struct=True,
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_sch_c4_sch_c4_v(save_xml):
    """
    TEST :schema collection and schema location : XSD A include XSD B, A's
    ns="A", B's ns="A", test the namespace of include (4.2.1) (SRC 2)
    """
    assert_bindings(
        schema="msData/schema/schC4_a.xsd",
        instance="msData/schema/schC4.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_sch_c3_sch_c3_v(save_xml):
    """
    TEST :schema collection and schema location : XSD A include XSD B, A's
    ns="", B's ns="", test the namespace of include (4.2.1) (SRC 2)
    """
    assert_bindings(
        schema="msData/schema/schC3_a.xsd",
        instance="msData/schema/schC3.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="No schema")
def test_sch_a8_sch_a8_i(save_xml):
    """
    TEST :schema collection and schema location : Schema
    Collection:(A,a.xsd), SchemaLocation:(A,c.xsd)(B,b.xsd where b.xsd's
    tns=foo), NoNSSchemaLocation: Since b.xsd exist, this should give
    error because the targetNS 'B' is not the same as what is in b.xsd
    'foo'
    """
    assert_bindings(
        schema="",
        instance="msData/schema/schA8.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_sch_a7_sch_a7_i(save_xml):
    """
    TEST :schema collection and schema location : Schema
    Collection:(A,a.xsd), SchemaLocation:(A,c.xsd)(B,b.xsd),
    NoNSSchemaLocation: The instance xml conform to (A,a.xsd)(B,b.xsd) WG
    decided this might reasonably vary between implementations
    """
    assert_bindings(
        schema="msData/schema/schA7_a.xsd",
        instance="msData/schema/schA7.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_sch_a5_sch_a5_i(save_xml):
    """
    TEST :schema collection and schema location : Schema
    Collection:(A,a.xsd) (B, b.xsd), SchemaLocation:(B,a.xsd),
    NoNSSchemaLocation:, xmlinstance should conform to (A,a.xsd)(B,b.xsd),
    ignore the inline SchemaLocation (B,a.xsd) WG decided this might
    reasonably vary between implementations
    """
    assert_bindings(
        schema="msData/schema/schA5_a.xsd",
        instance="msData/schema/schA5.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="No schema")
def test_sch_a4_sch_a4_v(save_xml):
    """
    TEST :schema collection and schema location : Schema Collection:,
    SchemaLocation:(A,a.xsd), NoNSSchemaLocation:,
    """
    assert_bindings(
        schema="",
        instance="msData/schema/schA4.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_sch_a3_sch_a3_v(save_xml):
    """
    TEST :schema collection and schema location : Schema
    Collection:(A,a.xsd), SchemaLocation:, NoNSSchemaLocation:,
    """
    assert_bindings(
        schema="msData/schema/schA3_a.xsd",
        instance="msData/schema/schA3.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_sch_a2_sch_a2_i(save_xml):
    """
    TEST :schema collection and schema location : Schema
    Collection:(A,a.xsd), SchemaLocation: (A,b.xsd), NoNSSchemaLocation:,
    expected: the xml instance must conform to (A,a.xsd), the inline
    schemaLocation (A,b.xsd) is ignored. WG decided this might reasonably
    vary between implementations
    """
    assert_bindings(
        schema="msData/schema/schA2_a.xsd",
        instance="msData/schema/schA2.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_sch_a1_sch_a1_v(save_xml):
    """
    TEST :schema collection and schema location : Schema Collection:
    (A,a.xsd), SchemaLocation: (B,b.xsd), NoNSSchemaLocation: c.xsd
    """
    assert_bindings(
        schema="msData/schema/schA1_a.xsd",
        instance="msData/schema/schA1.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_z075_st_z075_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : XSD: xs:NOTATION
    type on elements
    """
    assert_bindings(
        schema="msData/simpleType/stZ075.xsd",
        instance="msData/simpleType/stZ075.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_z074_st_z074_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : chameleon lists and
    union of lists
    """
    assert_bindings(
        schema="msData/simpleType/stZ074_a.xsd",
        instance="msData/simpleType/stZ074.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_z073ba_st_z073b_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : XSD: valid xsi:type
    on a union type(2) Instance test awaiting disposition of 5784, which
    in turn may or may not require schema test to change
    """
    assert_bindings(
        schema="msData/simpleType/stZ073b.xsd",
        instance="msData/simpleType/stZ073.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_z073b_st_z073b_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : XSD: valid xsi:type
    on a union type(2) Instance test awaiting disposition of 5784, which
    in turn may or may not require schema test to change
    """
    assert_bindings(
        schema="msData/simpleType/stZ073b.xsd",
        instance="msData/simpleType/stZ073.xml",
        class_name="Test",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_z072_st_z072_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : XSD: valid default
    value of a list of union with enumeration facet
    """
    assert_bindings(
        schema="msData/simpleType/stZ072.xsd",
        instance="msData/simpleType/stZ072.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_z071_st_z071_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : adding chameleon
    schemas that have unions without memberTypes
    """
    assert_bindings(
        schema="msData/simpleType/test298668_a.xsd",
        instance="msData/simpleType/test298668.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="No schema")
def test_st_z066_st_z066_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Facet and value
    constraint validation in lists
    """
    assert_bindings(
        schema="",
        instance="msData/simpleType/test102159_9.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="No schema")
def test_st_z064_st_z064_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Facet and value
    constraint validation in lists
    """
    assert_bindings(
        schema="",
        instance="msData/simpleType/test102159_7.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="No schema")
def test_st_z063_st_z063_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Facet and value
    constraint validation in lists
    """
    assert_bindings(
        schema="",
        instance="msData/simpleType/test102159_6.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="No schema")
def test_st_z062_st_z062_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Facet and value
    constraint validation in lists
    """
    assert_bindings(
        schema="",
        instance="msData/simpleType/test102159_5.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="No schema")
def test_st_z061_st_z061_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Facet and value
    constraint validation in lists
    """
    assert_bindings(
        schema="",
        instance="msData/simpleType/test102159_4.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="No schema")
def test_st_z060_st_z060_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Facet and value
    constraint validation in lists
    """
    assert_bindings(
        schema="",
        instance="msData/simpleType/test102159_3.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="No schema")
def test_st_z059_st_z059_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Facet and value
    constraint validation in lists
    """
    assert_bindings(
        schema="",
        instance="msData/simpleType/test102159_2.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="No schema")
def test_st_z058_st_z058_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Facet and value
    constraint validation in lists
    """
    assert_bindings(
        schema="",
        instance="msData/simpleType/test102159_1.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_z057_st_z057_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Need to permit
    anyType as a valid data type for the head element of a substitution
    group
    """
    assert_bindings(
        schema="msData/simpleType/test107331_j.xsd",
        instance="msData/simpleType/test107331_10.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_z056_st_z056_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Need to permit
    anySimpleType as a valid data type for the head element of a
    substitution group, with xsi:type=anyType
    """
    assert_bindings(
        schema="msData/simpleType/test107331_a.xsd",
        instance="msData/simpleType/test107331_10.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_z055_st_z055_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Need to permit
    anySimpleType as a valid data type for the head element of a
    substitution group, with xsi:type (CT with simplecontent)
    """
    assert_bindings(
        schema="msData/simpleType/test107331_e.xsd",
        instance="msData/simpleType/test107331_9.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.xfail
def test_st_z054_st_z054_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Need to permit
    anySimpleType as a valid data type for the head element of a
    substitution group, with xsi:type (List Unions)
    """
    assert_bindings(
        schema="msData/simpleType/test107331_c.xsd",
        instance="msData/simpleType/test107331_8.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_z053_st_z053_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Need to permit
    anySimpleType as a valid data type for the head element of a
    substitution group, with xsi:type (anyType)
    """
    assert_bindings(
        schema="msData/simpleType/test107331_h.xsd",
        instance="msData/simpleType/test107331_7.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_z052_st_z052_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Need to permit
    anySimpleType as a valid data type for the head element of a
    substitution group, with xsi:type (basic types)
    """
    assert_bindings(
        schema="msData/simpleType/test107331_a.xsd",
        instance="msData/simpleType/test107331_6.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_z051_st_z051_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Need to permit
    anySimpleType as a valid data type for the head element of a
    substitution group, with block=#all
    """
    assert_bindings(
        schema="msData/simpleType/test107331_i.xsd",
        instance="msData/simpleType/test107331_1.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_z050_st_z050_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Need to permit
    anySimpleType as a valid data type for the head element of a
    substitution group, anySimpleType substituting anyType
    """
    assert_bindings(
        schema="msData/simpleType/test107331_h.xsd",
        instance="msData/simpleType/test107331_5.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_z047_st_z047_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Need to permit
    anySimpleType as a valid data type for the head element of a
    substitution group, CT with simpleContent
    """
    assert_bindings(
        schema="msData/simpleType/test107331_e.xsd",
        instance="msData/simpleType/test107331_4.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_z046_st_z046_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Need to permit
    anySimpleType as a valid data type for the head element of a
    substitution group, substituting anyST with anyST
    """
    assert_bindings(
        schema="msData/simpleType/test107331_d.xsd",
        instance="msData/simpleType/test107331_3.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.xfail
def test_st_z045_st_z045_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Need to permit
    anySimpleType as a valid data type for the head element of a
    substitution group, Lists and Unions
    """
    assert_bindings(
        schema="msData/simpleType/test107331_c.xsd",
        instance="msData/simpleType/test107331_2.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_z044_st_z044_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Need to permit
    anySimpleType as a valid data type for the head element of a
    substitution group, head has abstract=true.
    """
    assert_bindings(
        schema="msData/simpleType/test107331_b.xsd",
        instance="msData/simpleType/test107331_1.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_z043_st_z043_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Need to permit
    anySimpleType as a valid data type for the head element of a
    substitution group.
    """
    assert_bindings(
        schema="msData/simpleType/test107331_a.xsd",
        instance="msData/simpleType/test107331_1.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_z040_st_z040_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Using an xsd union
    in the definition of another
    """
    assert_bindings(
        schema="msData/simpleType/stZ040.xsd",
        instance="msData/simpleType/stZ040.xml",
        class_name="Info2",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_z039_st_z039_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Defining a
    simpleType by restricting another simpleType
    """
    assert_bindings(
        schema="msData/simpleType/stZ039.xsd",
        instance="msData/simpleType/stZ039.xml",
        class_name="AlphaTestValue",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_z037_st_z037_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : xsd: simpleType
    restriction with pattern should be the intersaction of the base type
    and the derived type.
    """
    assert_bindings(
        schema="msData/simpleType/stZ035.xsd",
        instance="msData/simpleType/stZ037.xml",
        class_name="A",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_z036_st_z036_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : xsd: simpleType
    restriction with pattern should be the intersaction of the base type
    and the derived type.
    """
    assert_bindings(
        schema="msData/simpleType/stZ035.xsd",
        instance="msData/simpleType/stZ036.xml",
        class_name="A",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_z035_st_z035_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : xsd: simpleType
    restriction with pattern should be the intersaction of the base type
    and the derived type.
    """
    assert_bindings(
        schema="msData/simpleType/stZ035.xsd",
        instance="msData/simpleType/stZ035.xml",
        class_name="A",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_z034_st_z034_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : xsd: redefine
    should persist the last redefine in multiple document or multiple
    redefine.
    """
    assert_bindings(
        schema="msData/simpleType/stZ033.xsd",
        instance="msData/simpleType/stZ034.xml",
        class_name="B1",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_z033_st_z033_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : xsd: redefine
    should persist the last redefine in multiple document or multiple
    redefine.
    """
    assert_bindings(
        schema="msData/simpleType/stZ033.xsd",
        instance="msData/simpleType/stZ033.xml",
        class_name="B2",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_z032_st_z032_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : xsd: redefine
    should persist the last redefine in multiple document or multiple
    redefine.
    """
    assert_bindings(
        schema="msData/simpleType/stZ032.xsd",
        instance="msData/simpleType/stZ032.xml",
        class_name="A",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_z031_st_z031_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : xsd: we should not
    parser Name as QName.
    """
    assert_bindings(
        schema="msData/simpleType/stZ031.xsd",
        instance="msData/simpleType/stZ031.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_z030_st_z030_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : xsd: facet
    minExclusive in restricted type while minInclusive is in base type
    """
    assert_bindings(
        schema="msData/simpleType/stZ030.xsd",
        instance="msData/simpleType/stZ030.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_z015_st_z015_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : The value of
    totalDigits facet on a base simple type carrying forward to the
    derivedType
    """
    assert_bindings(
        schema="msData/simpleType/stZ015.xsd",
        instance="msData/simpleType/stZ015.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_z008_st_z008_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : rename a
    complexType to anySimpleType using extension, and extend it to another
    complexType with attribute
    """
    assert_bindings(
        schema="msData/simpleType/stZ008.xsd",
        instance="msData/simpleType/stZ008.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_z007_st_z007_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : rename a
    complexType to anySimpleType using extension, and restrict it to
    another complexType
    """
    assert_bindings(
        schema="msData/simpleType/stZ007.xsd",
        instance="msData/simpleType/stZ007.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_z004_st_z004_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : xsd:can not specify
    HalfWidth-KANA to Instance documents when schema has pattern facet
    including Japanese character.
    """
    assert_bindings(
        schema="msData/simpleType/stZ004.xsd",
        instance="msData/simpleType/stZ004.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_h008_st_h008_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : union derived from
    list of states with restriction facet 'enumeration' with a value of
    'CA' instance document has state = 'WA'
    """
    assert_bindings(
        schema="msData/simpleType/stH008.xsd",
        instance="msData/simpleType/stH008.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_h007_st_h007_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : union derived from
    list of states with restriction facet 'enumeration' with a value of
    'CA' instance document has state = 'CA'
    """
    assert_bindings(
        schema="msData/simpleType/stH007.xsd",
        instance="msData/simpleType/stH007.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_h006_st_h006_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : union derived from
    list of zip codes with restriction facet 'pattern' with a value of
    '[0-8]{5}' instance document has zip code = '98765'
    """
    assert_bindings(
        schema="msData/simpleType/stH006.xsd",
        instance="msData/simpleType/stH006.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_h005_st_h005_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : union derived from
    list of zip codes with restriction facet 'pattern' with a value of
    '[0-8]{5}' instance document has zip code='12345'
    """
    assert_bindings(
        schema="msData/simpleType/stH005.xsd",
        instance="msData/simpleType/stH005.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_h004_st_h004_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : schema defines a
    union with memberTypes of a list of states(restricted strings) and a
    list of zip codes(restricted positiveIntegers) instance document has
    zip code out of range
    """
    assert_bindings(
        schema="msData/simpleType/stH004.xsd",
        instance="msData/simpleType/stH004.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_h003_st_h003_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : schema defines a
    union with memberTypes of a list of states(restricted strings) and a
    list of zip codes(restricted positiveIntegers) instance document has
    valid values
    """
    assert_bindings(
        schema="msData/simpleType/stH003.xsd",
        instance="msData/simpleType/stH003.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_h002_st_h002_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : schema defines a
    union of positiveInteger with minInclusive and maxInclusive
    restrictions and NMTOKEN with enumeration instance document an invalid
    value
    """
    assert_bindings(
        schema="msData/simpleType/stH002.xsd",
        instance="msData/simpleType/stH002.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_h001_st_h001_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : schema defines a
    union of positiveInteger with minInclusive and maxInclusive
    restrictions and NMTOKEN with enumeration instance document has valid
    values
    """
    assert_bindings(
        schema="msData/simpleType/stH001.xsd",
        instance="msData/simpleType/stH001.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_g013_st_g013_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : list of string type
    with facet of 'pattern' value = '[A-C]{0,2}' instance document has
    'WA' value
    """
    assert_bindings(
        schema="msData/simpleType/stG013.xsd",
        instance="msData/simpleType/stG013.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_g012_st_g012_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : list of string type
    with facet of 'pattern' value = '[A-C]{0,2}' instance document has
    'CA' value
    """
    assert_bindings(
        schema="msData/simpleType/stG012.xsd",
        instance="msData/simpleType/stG012.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_g011_st_g011_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : list of NMTOKEN
    type with facet of 'enumeration' value = 'CA' instance document has
    'WA' value
    """
    assert_bindings(
        schema="msData/simpleType/stG011.xsd",
        instance="msData/simpleType/stG011.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_g010_st_g010_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : list of NMTOKEN
    type with facet of 'enumeration' value = 'CA' instance document has
    'CA' value
    """
    assert_bindings(
        schema="msData/simpleType/stG010.xsd",
        instance="msData/simpleType/stG010.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_g009_st_g009_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : list of atomic type
    with facet of 'minLength' value = '2' instance document has 1 item
    """
    assert_bindings(
        schema="msData/simpleType/stG009.xsd",
        instance="msData/simpleType/stG009.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_g008_st_g008_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : list of atomic type
    with facet of 'minLength' value = '2' instance document has 3 items
    """
    assert_bindings(
        schema="msData/simpleType/stG008.xsd",
        instance="msData/simpleType/stG008.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_g007_st_g007_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : list of atomic type
    with facet of 'length' value = '2' instance document has 1 item
    """
    assert_bindings(
        schema="msData/simpleType/stG007.xsd",
        instance="msData/simpleType/stG007.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_g006_st_g006_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : list of atomic type
    with facet of 'length' value = '2' instance document has 2 items
    """
    assert_bindings(
        schema="msData/simpleType/stG006.xsd",
        instance="msData/simpleType/stG006.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_g005_st_g005_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : schema is a list
    derived from a union of integer and NMTOKEN instance document contains
    float
    """
    assert_bindings(
        schema="msData/simpleType/stG005.xsd",
        instance="msData/simpleType/stG005.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_g004_st_g004_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : schema is a list
    derived from a union of integer and NMTOKEN instance document contains
    valid items of integer and NMTOKEN
    """
    assert_bindings(
        schema="msData/simpleType/stG004.xsd",
        instance="msData/simpleType/stG004.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_g003_st_g003_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : list of atomic type
    with facet of 'maxLength' value = '3' instance document has 4 items
    """
    assert_bindings(
        schema="msData/simpleType/stG003.xsd",
        instance="msData/simpleType/stG003.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_g002_st_g002_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : list of atomic type
    with facet of 'maxLength' value = '3' instance document has 3 items
    """
    assert_bindings(
        schema="msData/simpleType/stG002.xsd",
        instance="msData/simpleType/stG002.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_g001_st_g001_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : list of atomic type
    instance document contains items of the same atomic type
    """
    assert_bindings(
        schema="msData/simpleType/stG001.xsd",
        instance="msData/simpleType/stG001.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_ste110_ste110_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : test circular union
    """
    assert_bindings(
        schema="msData/simpleType/stE110.xsd",
        instance="msData/simpleType/ste100.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_ste100_ste100_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (46)
    """
    assert_bindings(
        schema="msData/simpleType/ste100.xsd",
        instance="msData/simpleType/ste100.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_ste099_ste099_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (45)
    """
    assert_bindings(
        schema="msData/simpleType/ste099.xsd",
        instance="msData/simpleType/ste099.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_ste098_ste098_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (44)
    """
    assert_bindings(
        schema="msData/simpleType/ste098.xsd",
        instance="msData/simpleType/ste098.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_e097_st_e097_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (43)
    """
    assert_bindings(
        schema="msData/simpleType/stE097.xsd",
        instance="msData/simpleType/stE097.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_e096_st_e096_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (42)
    """
    assert_bindings(
        schema="msData/simpleType/stE096.xsd",
        instance="msData/simpleType/stE096.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_e095_st_e095_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (41)
    """
    assert_bindings(
        schema="msData/simpleType/stE095.xsd",
        instance="msData/simpleType/stE095.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_e094_st_e094_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (40)
    """
    assert_bindings(
        schema="msData/simpleType/stE094.xsd",
        instance="msData/simpleType/stE094.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_e093_st_e093_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (39)
    """
    assert_bindings(
        schema="msData/simpleType/stE093.xsd",
        instance="msData/simpleType/stE093.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_e092_st_e092_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (38)
    """
    assert_bindings(
        schema="msData/simpleType/stE092.xsd",
        instance="msData/simpleType/stE092.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_e091_st_e091_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (37)
    """
    assert_bindings(
        schema="msData/simpleType/stE091.xsd",
        instance="msData/simpleType/stE091.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_e090_st_e090_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (36)
    """
    assert_bindings(
        schema="msData/simpleType/stE090.xsd",
        instance="msData/simpleType/stE090.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_e082_st_e082_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (35)
    """
    assert_bindings(
        schema="msData/simpleType/stE082.xsd",
        instance="msData/simpleType/stE082.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_e081_st_e081_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (34)
    """
    assert_bindings(
        schema="msData/simpleType/stE081.xsd",
        instance="msData/simpleType/stE081.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_e080_st_e080_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (33)
    """
    assert_bindings(
        schema="msData/simpleType/stE080.xsd",
        instance="msData/simpleType/stE080.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_e079_st_e079_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (32)
    """
    assert_bindings(
        schema="msData/simpleType/stE079.xsd",
        instance="msData/simpleType/stE079.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_e078_st_e078_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (31)
    """
    assert_bindings(
        schema="msData/simpleType/stE078.xsd",
        instance="msData/simpleType/stE078.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_e077_st_e077_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (30)
    """
    assert_bindings(
        schema="msData/simpleType/stE077.xsd",
        instance="msData/simpleType/stE077.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_e076_st_e076_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (29)
    """
    assert_bindings(
        schema="msData/simpleType/stE076.xsd",
        instance="msData/simpleType/stE076.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_e075_st_e075_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (28)
    """
    assert_bindings(
        schema="msData/simpleType/stE075.xsd",
        instance="msData/simpleType/stE075.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_ste074v_ste074v_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (27)
    """
    assert_bindings(
        schema="msData/simpleType/ste074v.xsd",
        instance="msData/simpleType/ste074v.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_e074_st_e074_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (26)
    """
    assert_bindings(
        schema="msData/simpleType/stE074.xsd",
        instance="msData/simpleType/stE074.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_e073v_st_e073v_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (25)
    """
    assert_bindings(
        schema="msData/simpleType/stE073v.xsd",
        instance="msData/simpleType/stE073v.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_e073_st_e073_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (24)
    """
    assert_bindings(
        schema="msData/simpleType/stE073.xsd",
        instance="msData/simpleType/stE073.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_e072_st_e072_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (23) Changed to add a wrapper element to avoid problems with
    having an ID in the outermost element - MHK 2010-07-10 But schema is
    possibly invalid in XSD 1.0 because ID cannot have a fixed value.
    """
    assert_bindings(
        schema="msData/simpleType/stE072.xsd",
        instance="msData/simpleType/stE072.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_e071_st_e071_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (22)
    """
    assert_bindings(
        schema="msData/simpleType/stE071.xsd",
        instance="msData/simpleType/stE071.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_e070_st_e070_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (21)
    """
    assert_bindings(
        schema="msData/simpleType/stE070.xsd",
        instance="msData/simpleType/stE070.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_e069_st_e069_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (20)
    """
    assert_bindings(
        schema="msData/simpleType/stE069.xsd",
        instance="msData/simpleType/stE069.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_e068_st_e068_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (19)
    """
    assert_bindings(
        schema="msData/simpleType/stE068.xsd",
        instance="msData/simpleType/stE068.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_e067_st_e067_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (18)
    """
    assert_bindings(
        schema="msData/simpleType/stE067.xsd",
        instance="msData/simpleType/stE067.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_e066_st_e066_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (17)
    """
    assert_bindings(
        schema="msData/simpleType/stE066.xsd",
        instance="msData/simpleType/stE066.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_e065_st_e065_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (16)
    """
    assert_bindings(
        schema="msData/simpleType/stE065.xsd",
        instance="msData/simpleType/stE065.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_e064_st_e064_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (15)
    """
    assert_bindings(
        schema="msData/simpleType/stE064.xsd",
        instance="msData/simpleType/stE064.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_e063_st_e063_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (14)
    """
    assert_bindings(
        schema="msData/simpleType/stE063.xsd",
        instance="msData/simpleType/stE063.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_e062_st_e062_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (13)
    """
    assert_bindings(
        schema="msData/simpleType/stE062.xsd",
        instance="msData/simpleType/stE062.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_e061_st_e061_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (12)
    """
    assert_bindings(
        schema="msData/simpleType/stE061.xsd",
        instance="msData/simpleType/stE061.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_e060_st_e060_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (11)
    """
    assert_bindings(
        schema="msData/simpleType/stE060.xsd",
        instance="msData/simpleType/stE060.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_e059_st_e059_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (10)
    """
    assert_bindings(
        schema="msData/simpleType/stE059.xsd",
        instance="msData/simpleType/stE059.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_e058_st_e058_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (9)
    """
    assert_bindings(
        schema="msData/simpleType/stE058.xsd",
        instance="msData/simpleType/stE058.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_e057_st_e057_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (8)
    """
    assert_bindings(
        schema="msData/simpleType/stE057.xsd",
        instance="msData/simpleType/stE057.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_e056_st_e056_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (7)
    """
    assert_bindings(
        schema="msData/simpleType/stE056.xsd",
        instance="msData/simpleType/stE056.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_e055_st_e055_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (6)
    """
    assert_bindings(
        schema="msData/simpleType/stE055.xsd",
        instance="msData/simpleType/stE055.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_e054_st_e054_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (5)
    """
    assert_bindings(
        schema="msData/simpleType/stE054.xsd",
        instance="msData/simpleType/stE054.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_e053_st_e053_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (4) In XSD 1.1, xs:simpleType is not allowed as a member type of
    a union (see note in Part 2 section 2.4.1)
    """
    assert_bindings(
        schema="msData/simpleType/stE053.xsd",
        instance="msData/simpleType/stE053.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_e052_st_e052_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (3)
    """
    assert_bindings(
        schema="msData/simpleType/stE052.xsd",
        instance="msData/simpleType/stE052.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_e051_st_e051_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (2)
    """
    assert_bindings(
        schema="msData/simpleType/stE051.xsd",
        instance="msData/simpleType/stE051.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_st_e050_st_e050_v(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : Union with Fixed
    Value (1)
    """
    assert_bindings(
        schema="msData/simpleType/stE050.xsd",
        instance="msData/simpleType/stE050.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_st_c034_st_c034_i(save_xml):
    """
    TEST :Syntax Checking for simpleType Declaration : error for duration
    value that is not conformed to the duration format.
    """
    assert_bindings(
        schema="msData/simpleType/stC034.xsd",
        instance="msData/simpleType/stC034.xml",
        class_name="A",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_z013f_wild_z013f_i(save_xml):
    """
    TEST :Syntax Validation - any : 328873: Attribute Wildcard
    Intersection and Union rules according to Errata E1-10 in schema set
    """
    assert_bindings(
        schema="msData/wildcards/test328873.xsd",
        instance="msData/wildcards/test328873f.xml",
        class_name="Sub6",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_z013e_wild_z013e_i(save_xml):
    """
    TEST :Syntax Validation - any : 328873: Attribute Wildcard
    Intersection and Union rules according to Errata E1-10 in schema set
    """
    assert_bindings(
        schema="msData/wildcards/test328873.xsd",
        instance="msData/wildcards/test328873e.xml",
        class_name="Sub5",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_z013d_wild_z013d_i(save_xml):
    """
    TEST :Syntax Validation - any : 328873: Attribute Wildcard
    Intersection and Union rules according to Errata E1-10 in schema set
    """
    assert_bindings(
        schema="msData/wildcards/test328873.xsd",
        instance="msData/wildcards/test328873d.xml",
        class_name="Sub4",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_z013c_wild_z013c_v(save_xml):
    """
    TEST :Syntax Validation - any : 328873: Attribute Wildcard
    Intersection and Union rules according to Errata E1-10 in schema set
    """
    assert_bindings(
        schema="msData/wildcards/test328873.xsd",
        instance="msData/wildcards/test328873c.xml",
        class_name="Sub3",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_z013b_wild_z013b_v(save_xml):
    """
    TEST :Syntax Validation - any : 328873: Attribute Wildcard
    Intersection and Union rules according to Errata E1-10 in schema set
    """
    assert_bindings(
        schema="msData/wildcards/test328873.xsd",
        instance="msData/wildcards/test328873b.xml",
        class_name="Sub2",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_z013a_wild_z013a_i(save_xml):
    """
    TEST :Syntax Validation - any : 328873: Attribute Wildcard
    Intersection and Union rules according to Errata E1-10 in schema set
    """
    assert_bindings(
        schema="msData/wildcards/test328873.xsd",
        instance="msData/wildcards/test328873a.xml",
        class_name="Sub",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_z011_wild_z011_i(save_xml):
    """
    TEST :Syntax Validation - any : XSD: process Contents for the complete
    wildcard component
    """
    assert_bindings(
        schema="msData/wildcards/wildZ011a.xsd",
        instance="msData/wildcards/wildZ011.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_z010_wild_z010_v(save_xml):
    """
    TEST :Syntax Validation - any : xsd: namespace='' on wildcard any
    should match against ##any TSTF ruled the instance invalid -- no
    defaulting of the empty string to ##any is licensed by the spec.
    """
    assert_bindings(
        schema="msData/wildcards/wildZ010_a.xsd",
        instance="msData/wildcards/wildZ010.xml",
        class_name="Doc",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_z007_wild_z007_v(save_xml):
    """
    TEST :Syntax Validation - any : XSD: When processContents=lax, xsd:any
    doesn't allow attributes from target namespace
    """
    assert_bindings(
        schema="msData/wildcards/wildZ007.xsd",
        instance="msData/wildcards/wildZ007.xml",
        class_name="Stylesheet",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_z006_wild_z006_i(save_xml):
    """
    TEST :Syntax Validation - any : any with namespace ##other should not
    allow local element
    """
    assert_bindings(
        schema="msData/wildcards/wildZ006.xsd",
        instance="msData/wildcards/wildZ006.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_z005_wild_z005_i(save_xml):
    """
    TEST :Syntax Validation - any : any with namespace ##other should not
    allow targetNamespace's element
    """
    assert_bindings(
        schema="msData/wildcards/wildZ005.xsd",
        instance="msData/wildcards/wildZ005.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_z004_wild_z004_v(save_xml):
    """
    TEST :Syntax Validation - any : xsd: un-declared element when content
    is xsd:anyType.
    """
    assert_bindings(
        schema="msData/wildcards/wildZ004.xsd",
        instance="msData/wildcards/wildZ004.xml",
        class_name="RootElem",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_z003_wild_z003_v(save_xml):
    """
    TEST :Syntax Validation - any : xsd: test valid instance with elements
    from a different namespace where xsd defint 'any' with ##other
    """
    assert_bindings(
        schema="msData/wildcards/wildZ003_a.xsd",
        instance="msData/wildcards/wildZ003.xml",
        class_name="Elt1",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_z002_wild_z002_v(save_xml):
    """
    TEST :Syntax Validation - any : attribute on xsd:any
    processContents="skip"
    """
    assert_bindings(
        schema="msData/wildcards/wildZ002.xsd",
        instance="msData/wildcards/wildZ002.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_z001_wild_z001_i(save_xml):
    """
    TEST :Syntax Validation - any : validate namespace set to a valid
    namespace URI and instance document has correct elements
    """
    assert_bindings(
        schema="msData/wildcards/wildZ001.xsd",
        instance="msData/wildcards/wildZ001.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_p006_wild_p006_v(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ processContents=skip
    and namespace=##targetNamespace) with schema
    targetNamespace=http://foobar, attribute not declared and instance
    document has attributes from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildP006.xsd",
        instance="msData/wildcards/wildP006.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_p005_wild_p005_v(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ processContents=skip
    and namespace=##targetNamespace) with schema
    targetNamespace=http://foobar, attribute declared and instance
    document has attributes from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildP005.xsd",
        instance="msData/wildcards/wildP005.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_p004_wild_p004_v(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ processContents=lax
    and namespace=##targetNamespace) with schema
    targetNamespace=http://foobar, attribute not declared and instance
    document has attributes from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildP004.xsd",
        instance="msData/wildcards/wildP004.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_p003_wild_p003_v(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ processContents=lax
    and namespace=##targetNamespace) with schema
    targetNamespace=http://foobar, attribute declared and instance
    document has attributes from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildP003.xsd",
        instance="msData/wildcards/wildP003.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_p002_wild_p002_i(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/
    processContents=strict and namespace=##targetNamespace) with schema
    targetNamespace=http://foobar, attribute not declared and instance
    document has attributes from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildP002.xsd",
        instance="msData/wildcards/wildP002.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_p001_wild_p001_v(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/
    processContents=strict and namespace=##targetNamespace) with schema
    targetNamespace=http://foobar, attribute declared and instance
    document has attributes from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildP001.xsd",
        instance="msData/wildcards/wildP001.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_o040_wild_o040_v(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/
    namespace=##targetNamespace http://www.w3.org/1999/xhtml) with schema
    targetNamespace=http://foobar and instance document has attributes
    from the xhtml namespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO040.xsd",
        instance="msData/wildcards/wildO040.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_o039_wild_o039_i(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/
    namespace=##targetNamespace http://www.w3.org/1999/xhtml) with schema
    targetNamespace=http://foobar and instance document has attributes
    from other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildO039.xsd",
        instance="msData/wildcards/wildO039.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_o038_wild_o038_v(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/
    namespace=##targetNamespace http://www.w3.org/1999/xhtml) with schema
    targetNamespace=http://foobar and instance document has attributes
    from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO038.xsd",
        instance="msData/wildcards/wildO038.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_o037_wild_o037_v(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ namespace=##local
    http://www.w3.org/1999/xhtml) with schema
    targetNamespace=http://foobar and instance document has attributes
    from the xhtml namespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO037.xsd",
        instance="msData/wildcards/wildO037.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_o035_wild_o035_i(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ namespace=##local
    http://www.w3.org/1999/xhtml) with schema
    targetNamespace=http://foobar and instance document has attributes
    from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO035.xsd",
        instance="msData/wildcards/wildO035.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_o034_wild_o034_i(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ namespace=##local
    http://foobar) with schema targetNamespace=http://foobar and instance
    document has attributes from other namespaces besides listed
    """
    assert_bindings(
        schema="msData/wildcards/wildO034.xsd",
        instance="msData/wildcards/wildO034.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_o033_wild_o033_v(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ namespace=##local
    http://foobar) with schema targetNamespace=http://foobar and instance
    document has attributes from local
    """
    assert_bindings(
        schema="msData/wildcards/wildO033.xsd",
        instance="msData/wildcards/wildO033.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_o032_wild_o032_i(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=http://foobar) with
    schema targetNamespace=http://foobar and instance document has
    attributes from other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildO032.xsd",
        instance="msData/wildcards/wildO032.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_o031_wild_o031_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=http://foobar) with
    schema targetNamespace=http://foobar and instance document has
    attributes from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO031.xsd",
        instance="msData/wildcards/wildO031.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_o030_wild_o030_i(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##local) with schema
    targetNamespace=http://foobar and instance document has attributes
    from other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildO030.xsd",
        instance="msData/wildcards/wildO030.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_o029_wild_o029_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##local) with schema
    targetNamespace=http://foobar and instance document has attributes
    from local
    """
    assert_bindings(
        schema="msData/wildcards/wildO029.xsd",
        instance="msData/wildcards/wildO029.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_o028_wild_o028_i(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##targetNamespace)
    with schema targetNamespace=http://foobar and instance document has
    attributes from other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildO028.xsd",
        instance="msData/wildcards/wildO028.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_o027_wild_o027_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##targetNamespace)
    with schema targetNamespace=http://foobar and instance document has
    attributes from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO027.xsd",
        instance="msData/wildcards/wildO027.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_o026_wild_o026_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##other) with schema
    targetNamespace=http://foobar and instance document has attributes
    from other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildO026.xsd",
        instance="msData/wildcards/wildO026.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_o025_wild_o025_i(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##other) with schema
    targetNamespace=http://foobar and instance document has attributes
    from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO025.xsd",
        instance="msData/wildcards/wildO025.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_o024_wild_o024_i(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/
    namespace=http://foobar) with schema targetNamespace=http://foobar and
    instance document has attributes from other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildO024.xsd",
        instance="msData/wildcards/wildO024.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_o023_wild_o023_v(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/
    namespace=http://foobar) with schema targetNamespace=http://foobar and
    instance document has attributes from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO023.xsd",
        instance="msData/wildcards/wildO023.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_o022_wild_o022_i(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/
    namespace=##targetNamespace) with schema targetNamespace=http://foobar
    and instance document has attributes from other namespaces besides
    target
    """
    assert_bindings(
        schema="msData/wildcards/wildO022.xsd",
        instance="msData/wildcards/wildO022.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_o021_wild_o021_v(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/
    namespace=##targetNamespace) with schema targetNamespace=http://foobar
    and instance document has attributes from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO021.xsd",
        instance="msData/wildcards/wildO021.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_o020_wild_o020_i(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ namespace=##local)
    with schema targetNamespace=http://foobar and instance document has
    attributes from other namespaces besides local
    """
    assert_bindings(
        schema="msData/wildcards/wildO020.xsd",
        instance="msData/wildcards/wildO020.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_o019_wild_o019_v(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ namespace=##local)
    with schema targetNamespace=http://foobar and instance document has
    attributes from local
    """
    assert_bindings(
        schema="msData/wildcards/wildO019.xsd",
        instance="msData/wildcards/wildO019.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_o018_wild_o018_v(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ namespace=##other)
    with schema targetNamespace=http://foobar and instance document has
    attributes from other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildO018.xsd",
        instance="msData/wildcards/wildO018.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_o017_wild_o017_i(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ namespace=##other)
    with schema targetNamespace=http://foobar and instance document has
    attributes from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO017.xsd",
        instance="msData/wildcards/wildO017.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_o016_wild_o016_v(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ namespace=##any) with
    schema targetNamespace=http://foobar and instance document has
    attributes from other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildO016.xsd",
        instance="msData/wildcards/wildO016.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_o015_wild_o015_v(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ namespace=##any) with
    schema targetNamespace=http://foobar and instance document has
    attributes from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO015.xsd",
        instance="msData/wildcards/wildO015.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_o014_wild_o014_i(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/
    namespace=##targetNamespace http://www.w3.org/1999/xhtml) and instance
    document has attributes from other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildO014.xsd",
        instance="msData/wildcards/wildO014.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_o013_wild_o013_v(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/
    namespace=##targetNamespace http://www.w3.org/1999/xhtml) and instance
    document has attributes from the xhtml namespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO013.xsd",
        instance="msData/wildcards/wildO013.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_o012_wild_o012_v(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/
    namespace=##targetNamespace http://www.w3.org/1999/xhtml) and instance
    document has attributes from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO012.xsd",
        instance="msData/wildcards/wildO012.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_o011_wild_o011_i(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ namespace=##local
    http://www.w3.org/1999/xhtml) and instance document has attributes
    from other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildO011.xsd",
        instance="msData/wildcards/wildO011.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_o010_wild_o010_v(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ namespace=##local
    http://www.w3.org/1999/xhtml) and instance document has attributes
    from the xhtml namespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO010.xsd",
        instance="msData/wildcards/wildO010.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_o009_wild_o009_i(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ namespace=##local
    http://www.w3.org/1999/xhtml) and instance document has attributes
    from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO009.xsd",
        instance="msData/wildcards/wildO009.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_o008_wild_o008_i(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/
    namespace=##targetNamespace) and instance document has attributes from
    other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildO008.xsd",
        instance="msData/wildcards/wildO008.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_o007_wild_o007_v(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/
    namespace=##targetNamespace) and instance document has attributes from
    targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO007.xsd",
        instance="msData/wildcards/wildO007.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_o006_wild_o006_i(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ namespace=##local)
    and instance document has attributes from other namespaces besides
    local
    """
    assert_bindings(
        schema="msData/wildcards/wildO006.xsd",
        instance="msData/wildcards/wildO006.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_o005_wild_o005_v(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ namespace=##local)
    and instance document has attributes from local Namespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO005.xsd",
        instance="msData/wildcards/wildO005.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_o004_wild_o004_v(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ namespace=##other)
    and instance document has attributes from other namespaces besides
    target
    """
    assert_bindings(
        schema="msData/wildcards/wildO004.xsd",
        instance="msData/wildcards/wildO004.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_o003_wild_o003_i(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ namespace=##other)
    and instance document has attributes from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO003.xsd",
        instance="msData/wildcards/wildO003.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_o002_wild_o002_v(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ namespace=##any) and
    instance document has attributes from other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildO002.xsd",
        instance="msData/wildcards/wildO002.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_o001_wild_o001_v(save_xml):
    """
    TEST :Syntax Validation - any : ANYAttribute (w/ namespace=##any) and
    instance document has attributes from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildO001.xsd",
        instance="msData/wildcards/wildO001.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_i012_wild_i012_v(save_xml):
    """
    TEST :Syntax Validation - any : multiple any in sequence with
    namespaces (##other{1}, A{2}), non-deterministic declaration
    """
    assert_bindings(
        schema="msData/wildcards/wildI012.xsd",
        instance="msData/wildcards/wildI012.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_i011_wild_i011_v(save_xml):
    """
    TEST :Syntax Validation - any : multiple any in sequence with
    namespaces (##other{1}, A{1}), non-deterministic declaration
    """
    assert_bindings(
        schema="msData/wildcards/wildI011.xsd",
        instance="msData/wildcards/wildI011.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_i007_wild_i007_v(save_xml):
    """
    TEST :Syntax Validation - any : multiple any in choice with namespaces
    (##other, ##targetNamespace), and valid instance xml
    """
    assert_bindings(
        schema="msData/wildcards/wildI007.xsd",
        instance="msData/wildcards/wildI007.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_i006_wild_i006_v(save_xml):
    """
    TEST :Syntax Validation - any : multiple any in choice with different
    namespaces (a, b, ##targetNamespace, ##local), and valid instance xml
    """
    assert_bindings(
        schema="msData/wildcards/wildI006.xsd",
        instance="msData/wildcards/wildI006.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_i005_wild_i005_v(save_xml):
    """
    TEST :Syntax Validation - any : multiple any in sequence with
    different namespaces and valid instance xml
    """
    assert_bindings(
        schema="msData/wildcards/wildI005.xsd",
        instance="msData/wildcards/wildI005.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_i004i_wild_i004i_i(save_xml):
    """
    TEST :Syntax Validation - any : 67191 - ensuring that processContents
    of lax will validate
    """
    assert_bindings(
        schema="msData/wildcards/wildI004i.xsd",
        instance="msData/wildcards/wildI004i.xml",
        class_name="Alpha",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_i004_wild_i004_v(save_xml):
    """
    TEST :Syntax Validation - any : 67191 - ensuring that processContents
    of lax will validate
    """
    assert_bindings(
        schema="msData/wildcards/wildI004.xsd",
        instance="msData/wildcards/wildI004.xml",
        class_name="Root",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_h012_wild_h012_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/
    namespace=http://www.w3.org/1999/xhtml and undeclared element,
    processContents=skip)
    """
    assert_bindings(
        schema="msData/wildcards/wildH012.xsd",
        instance="msData/wildcards/wildH012.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_h011_wild_h011_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/
    namespace=http://www.w3.org/1999/xhtml and declared element,
    processContents=skip)
    """
    assert_bindings(
        schema="msData/wildcards/wildH011.xsd",
        instance="msData/wildcards/wildH011.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_h010_wild_h010_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/
    namespace=http://www.w3.org/1999/xhtml and undeclared element,
    processContents=lax)
    """
    assert_bindings(
        schema="msData/wildcards/wildH010.xsd",
        instance="msData/wildcards/wildH010.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_h009_wild_h009_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/
    namespace=http://www.w3.org/1999/xhtml and declared element,
    processContents=lax)
    """
    assert_bindings(
        schema="msData/wildcards/wildH009.xsd",
        instance="msData/wildcards/wildH009.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_h008_wild_h008_i(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/
    namespace=http://www.w3.org/1999/xhtml and undeclared element,
    processContents=strict)
    """
    assert_bindings(
        schema="msData/wildcards/wildH008.xsd",
        instance="msData/wildcards/wildH008.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_h007_wild_h007_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/
    namespace=http://www.w3.org/1999/xhtml and declared element,
    processContents=strict)
    """
    assert_bindings(
        schema="msData/wildcards/wildH007.xsd",
        instance="msData/wildcards/wildH007.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_h006_wild_h006_i(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ processContents=skip and
    namespace=##targetNamespace) with schema targetNamespace=http://foobar
    and instance document has elements from other namespace
    """
    assert_bindings(
        schema="msData/wildcards/wildH006.xsd",
        instance="msData/wildcards/wildH006.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_h005_wild_h005_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ processContents=skip and
    namespace=##targetNamespace) with schema targetNamespace=http://foobar
    and instance document has undeclared elements from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildH005.xsd",
        instance="msData/wildcards/wildH005.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_h004_wild_h004_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ processContents=lax and
    namespace=##targetNamespace) with schema targetNamespace=http://foobar
    and instance document has undeclared elements from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildH004.xsd",
        instance="msData/wildcards/wildH004.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_h003_wild_h003_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ processContents=lax and
    namespace=##targetNamespace) with schema targetNamespace=http://foobar
    and instance document has elements from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildH003.xsd",
        instance="msData/wildcards/wildH003.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_h002_wild_h002_i(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ processContents=strict and
    namespace=##targetNamespace) with schema
    targetNamespace=http://www.w3.org/1999/xhtml and instance document has
    elements from other namespace
    """
    assert_bindings(
        schema="msData/wildcards/wildH002.xsd",
        instance="msData/wildcards/wildH002.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_h001_wild_h001_i(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ processContents=strict and
    namespace=##targetNamespace) with schema
    targetNamespace=http://www.w3.org/1999/xhtml and instance document has
    undeclared elements from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildH001.xsd",
        instance="msData/wildcards/wildH001.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_g040_wild_g040_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##targetNamespace
    http://www.w3.org/1999/xhtml) with schema
    targetNamespace=http://foobar and instance document has elements from
    the xhtml namespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG040.xsd",
        instance="msData/wildcards/wildG040.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_g039_wild_g039_i(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##targetNamespace
    http://www.w3.org/1999/xhtml) with schema
    targetNamespace=http://foobar and instance document has elements from
    other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildG039.xsd",
        instance="msData/wildcards/wildG039.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_g038_wild_g038_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##targetNamespace
    http://www.w3.org/1999/xhtml) with schema
    targetNamespace=http://foobar and instance document has elements from
    targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG038.xsd",
        instance="msData/wildcards/wildG038.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_g037_wild_g037_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##local
    http://www.w3.org/1999/xhtml) with schema
    targetNamespace=http://foobar and instance document has elements from
    the xhtml namespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG037.xsd",
        instance="msData/wildcards/wildG037.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_g036_wild_g036_i(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##local
    http://www.w3.org/1999/xhtml) with schema
    targetNamespace=http://foobar and instance document has elements from
    other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildG036.xsd",
        instance="msData/wildcards/wildG036.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_g035_wild_g035_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##local
    http://www.w3.org/1999/xhtml) with schema
    targetNamespace=http://www.w3.org/1999/xhtml and instance document has
    elements from local
    """
    assert_bindings(
        schema="msData/wildcards/wildG035.xsd",
        instance="msData/wildcards/wildG035.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_g034_wild_g034_i(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##local
    http://foobar) with schema targetNamespace=http://foobar and instance
    document has elements from other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildG034.xsd",
        instance="msData/wildcards/wildG034.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_g033_wild_g033_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##local
    http://foobar) with schema targetNamespace=http://foobar and instance
    document has elements from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG033.xsd",
        instance="msData/wildcards/wildG033.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_g032_wild_g032_i(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=A B C D E ##local
    ##targetNamespace) with schema targetNamespace=http://foobar and
    instance document has elements from all of them + bar
    """
    assert_bindings(
        schema="msData/wildcards/wildG032.xsd",
        instance="msData/wildcards/wildG032.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_g031_wild_g031_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=A B C D E ##local
    ##targetNamespace) with schema targetNamespace=http://foobar and
    instance document has elements from all of them
    """
    assert_bindings(
        schema="msData/wildcards/wildG031.xsd",
        instance="msData/wildcards/wildG031.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_g030_wild_g030_i(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##local) with schema
    targetNamespace=http://foobar and instance document has elements from
    other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildG030.xsd",
        instance="msData/wildcards/wildG030.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_g029_wild_g029_i(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##local) with schema
    targetNamespace=http://foobar and instance document has elements from
    targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG029.xsd",
        instance="msData/wildcards/wildG029.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_g028_wild_g028_i(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##targetNamespace)
    with schema targetNamespace=http://foobar and instance document has
    elements from other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildG028.xsd",
        instance="msData/wildcards/wildG028.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_g027_wild_g027_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##targetNamespace)
    with schema targetNamespace=http://foobar and instance document has
    elements from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG027.xsd",
        instance="msData/wildcards/wildG027.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_g026_wild_g026_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##other) with schema
    targetNamespace=http://foobar and instance document has elements from
    other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildG026.xsd",
        instance="msData/wildcards/wildG026.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_g025_wild_g025_i(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##other) with schema
    targetNamespace=http://foobar and instance document has elements from
    targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG025.xsd",
        instance="msData/wildcards/wildG025.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_g024_wild_g024_i(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=http://foobar) with
    schema targetNamespace=http://foobar and instance document has
    elements from other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildG024.xsd",
        instance="msData/wildcards/wildG024.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_g023_wild_g023_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=http://foobar) with
    schema targetNamespace=http://foobar and instance document has
    elements from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG023.xsd",
        instance="msData/wildcards/wildG023.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_g022_wild_g022_i(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##targetNamespace)
    with schema targetNamespace=http://foobar and instance document has
    elements from other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildG022.xsd",
        instance="msData/wildcards/wildG022.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_g021_wild_g021_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##targetNamespace)
    with schema targetNamespace=http://foobar and instance document has
    elements from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG021.xsd",
        instance="msData/wildcards/wildG021.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_g020_wild_g020_i(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##local) with schema
    targetNamespace=http://foobar and instance document has elements from
    other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildG020.xsd",
        instance="msData/wildcards/wildG020.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_g019_wild_g019_i(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##local) with schema
    targetNamespace=http://foobar and instance document has elements from
    targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG019.xsd",
        instance="msData/wildcards/wildG019.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_g018_wild_g018_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##other) with schema
    targetNamespace=http://foobar and instance document has elements from
    other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildG018.xsd",
        instance="msData/wildcards/wildG018.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_g017_wild_g017_i(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##other) with schema
    targetNamespace=http://foobar and instance document has elements from
    targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG017.xsd",
        instance="msData/wildcards/wildG017.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_g016_wild_g016_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##any) with schema
    targetNamespace=http://foobar and instance document has elements from
    other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildG016.xsd",
        instance="msData/wildcards/wildG016.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_g015_wild_g015_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##any) with schema
    targetNamespace=http://foobar and instance document has elements from
    targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG015.xsd",
        instance="msData/wildcards/wildG015.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_g014_wild_g014_i(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##targetNamespace
    http://www.w3.org/1999/xhtml) and instance document has elements from
    other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildG014.xsd",
        instance="msData/wildcards/wildG014.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_g013_wild_g013_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##targetNamespace
    http://www.w3.org/1999/xhtml) and instance document has elements from
    the xhtml namespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG013.xsd",
        instance="msData/wildcards/wildG013.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_g012_wild_g012_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##targetNamespace
    http://www.w3.org/1999/xhtml) and instance document has elements from
    targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG012.xsd",
        instance="msData/wildcards/wildG012.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_g011_wild_g011_i(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##local
    http://www.w3.org/1999/xhtml) and instance document has elements from
    other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildG011.xsd",
        instance="msData/wildcards/wildG011.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_g010_wild_g010_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##local
    http://www.w3.org/1999/xhtml) and instance document has elements from
    both namespaces
    """
    assert_bindings(
        schema="msData/wildcards/wildG010.xsd",
        instance="msData/wildcards/wildG010.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_g009_wild_g009_i(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##local
    http://www.w3.org/1999/xhtml) and instance document has elements from
    targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG009.xsd",
        instance="msData/wildcards/wildG009.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_g008_wild_g008_i(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##targetNamespace)
    and instance document has elements from other namespaces besides
    target
    """
    assert_bindings(
        schema="msData/wildcards/wildG008.xsd",
        instance="msData/wildcards/wildG008.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_g007_wild_g007_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##targetNamespace)
    and instance document has elements from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG007.xsd",
        instance="msData/wildcards/wildG007.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_g006_wild_g006_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##local) and
    instance document has elements from no namespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG006.xsd",
        instance="msData/wildcards/wildG006.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_g005_wild_g005_i(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##local) and
    instance document has elements from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG005.xsd",
        instance="msData/wildcards/wildG005.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_g004_wild_g004_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##other) and
    instance document has elements from other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildG004.xsd",
        instance="msData/wildcards/wildG004.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
@pytest.mark.skip(reason="Invalid instance")
def test_wild_g003_wild_g003_i(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##other) and
    instance document has elements from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG003.xsd",
        instance="msData/wildcards/wildG003.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_g002_wild_g002_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##any) and instance
    document has elements from other namespaces besides target
    """
    assert_bindings(
        schema="msData/wildcards/wildG002.xsd",
        instance="msData/wildcards/wildG002.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )


@pytest.mark.schema11
def test_wild_g001_wild_g001_v(save_xml):
    """
    TEST :Syntax Validation - any : ANY (w/ namespace=##any) and instance
    document has elements from targetNamespace
    """
    assert_bindings(
        schema="msData/wildcards/wildG001.xsd",
        instance="msData/wildcards/wildG001.xml",
        class_name="Foo",
        version="1.1",
        save_xml=save_xml,
    )
