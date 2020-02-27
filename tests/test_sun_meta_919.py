import pytest

from tests.utils import assert_bindings


@pytest.mark.xfail
def test_xsd024_xsd024_v00():
    """
    xsd024 Use of the chameleon schema and "smart reference reparing"
    """
    assert_bindings(
        schema="sunData/combined/xsd024/xsd024.xsd",
        is_valid=True,
        instance="sunData/combined/xsd024/xsd024.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_xsd022_xsd022_n00():
    """
    xsd022 Various forms of forward reference to the simple type.
    """
    assert_bindings(
        schema="sunData/combined/xsd022/xsd022.xsd",
        is_valid=True,
        instance="sunData/combined/xsd022/xsd022.n00.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd022_xsd022_v00():
    """
    xsd022 Various forms of forward reference to the simple type.
    """
    assert_bindings(
        schema="sunData/combined/xsd022/xsd022.xsd",
        is_valid=True,
        instance="sunData/combined/xsd022/xsd022.v00.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_xsd021_xsd021_n00():
    """
    xsd021 anyOtherAttribute.
    """
    assert_bindings(
        schema="sunData/combined/xsd021/xsd021.xsd",
        is_valid=True,
        instance="sunData/combined/xsd021/xsd021.n00.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd021_xsd021_n01():
    """
    xsd021 anyOtherAttribute.
    """
    assert_bindings(
        schema="sunData/combined/xsd021/xsd021.xsd",
        is_valid=True,
        instance="sunData/combined/xsd021/xsd021.n01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd021_xsd021_n02():
    """
    xsd021 anyOtherAttribute.
    """
    assert_bindings(
        schema="sunData/combined/xsd021/xsd021.xsd",
        is_valid=True,
        instance="sunData/combined/xsd021/xsd021.n02.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd021_xsd021_n03():
    """
    xsd021 anyOtherAttribute.
    """
    assert_bindings(
        schema="sunData/combined/xsd021/xsd021.xsd",
        is_valid=True,
        instance="sunData/combined/xsd021/xsd021.n03.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd021_xsd021_n04():
    """
    xsd021 anyOtherAttribute.
    """
    assert_bindings(
        schema="sunData/combined/xsd021/xsd021.xsd",
        is_valid=True,
        instance="sunData/combined/xsd021/xsd021.n04.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd021_xsd021_n05():
    """
    xsd021 anyOtherAttribute.
    """
    assert_bindings(
        schema="sunData/combined/xsd021/xsd021.xsd",
        is_valid=True,
        instance="sunData/combined/xsd021/xsd021.n05.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd021_xsd021_n06():
    """
    xsd021 anyOtherAttribute.
    """
    assert_bindings(
        schema="sunData/combined/xsd021/xsd021.xsd",
        is_valid=True,
        instance="sunData/combined/xsd021/xsd021.n06.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd021_xsd021_n07():
    """
    xsd021 anyOtherAttribute.
    """
    assert_bindings(
        schema="sunData/combined/xsd021/xsd021.xsd",
        is_valid=True,
        instance="sunData/combined/xsd021/xsd021.n07.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd021_xsd021_n08():
    """
    xsd021 anyOtherAttribute.
    """
    assert_bindings(
        schema="sunData/combined/xsd021/xsd021.xsd",
        is_valid=True,
        instance="sunData/combined/xsd021/xsd021.n08.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd021_xsd021_n09():
    """
    xsd021 anyOtherAttribute.
    """
    assert_bindings(
        schema="sunData/combined/xsd021/xsd021.xsd",
        is_valid=True,
        instance="sunData/combined/xsd021/xsd021.n09.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd021_xsd021_n10():
    """
    xsd021 anyOtherAttribute.
    """
    assert_bindings(
        schema="sunData/combined/xsd021/xsd021.xsd",
        is_valid=True,
        instance="sunData/combined/xsd021/xsd021.n10.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd021_xsd021_n11():
    """
    xsd021 anyOtherAttribute.
    """
    assert_bindings(
        schema="sunData/combined/xsd021/xsd021.xsd",
        is_valid=True,
        instance="sunData/combined/xsd021/xsd021.n11.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd021_xsd021_v00():
    """
    xsd021 anyOtherAttribute.
    """
    assert_bindings(
        schema="sunData/combined/xsd021/xsd021.xsd",
        is_valid=True,
        instance="sunData/combined/xsd021/xsd021.v00.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_xsd012_xsd012_n00():
    """
    xsd012 Mixed content model.
    """
    assert_bindings(
        schema="sunData/combined/xsd012/xsd012.xsd",
        is_valid=True,
        instance="sunData/combined/xsd012/xsd012.n00.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd012_xsd012_v00():
    """
    xsd012 Mixed content model.
    """
    assert_bindings(
        schema="sunData/combined/xsd012/xsd012.xsd",
        is_valid=True,
        instance="sunData/combined/xsd012/xsd012.v00.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_xsd011_xsd011_n00():
    """
    xsd011 Nillable.
    """
    assert_bindings(
        schema="sunData/combined/xsd011/xsd011.xsd",
        is_valid=True,
        instance="sunData/combined/xsd011/xsd011.n00.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd011_xsd011_n01():
    """
    xsd011 Nillable.
    """
    assert_bindings(
        schema="sunData/combined/xsd011/xsd011.xsd",
        is_valid=True,
        instance="sunData/combined/xsd011/xsd011.n01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd011_xsd011_n02():
    """
    xsd011 Nillable.
    """
    assert_bindings(
        schema="sunData/combined/xsd011/xsd011.xsd",
        is_valid=True,
        instance="sunData/combined/xsd011/xsd011.n02.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd011_xsd011_n03():
    """
    xsd011 Nillable.
    """
    assert_bindings(
        schema="sunData/combined/xsd011/xsd011.xsd",
        is_valid=True,
        instance="sunData/combined/xsd011/xsd011.n03.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd011_xsd011_n04():
    """
    xsd011 Nillable.
    """
    assert_bindings(
        schema="sunData/combined/xsd011/xsd011.xsd",
        is_valid=True,
        instance="sunData/combined/xsd011/xsd011.n04.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_xsd011_xsd011_v00():
    """
    xsd011 Nillable.
    """
    assert_bindings(
        schema="sunData/combined/xsd011/xsd011.xsd",
        is_valid=True,
        instance="sunData/combined/xsd011/xsd011.v00.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_xsd008_xsd008_n00():
    """
    xsd008 Abstract element and element substitution group.
    """
    assert_bindings(
        schema="sunData/combined/xsd008/xsd008.xsd",
        is_valid=True,
        instance="sunData/combined/xsd008/xsd008.n00.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd008_xsd008_n01():
    """
    xsd008 Abstract element and element substitution group.
    """
    assert_bindings(
        schema="sunData/combined/xsd008/xsd008.xsd",
        is_valid=True,
        instance="sunData/combined/xsd008/xsd008.n01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd008_xsd008_n02():
    """
    xsd008 Abstract element and element substitution group.
    """
    assert_bindings(
        schema="sunData/combined/xsd008/xsd008.xsd",
        is_valid=True,
        instance="sunData/combined/xsd008/xsd008.n02.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_xsd008_xsd008_v00():
    """
    xsd008 Abstract element and element substitution group.
    """
    assert_bindings(
        schema="sunData/combined/xsd008/xsd008.xsd",
        is_valid=True,
        instance="sunData/combined/xsd008/xsd008.v00.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_xsd006_xsd006_n00():
    """
    xsd006 minOccurs/maxOccurs. Various combinations.
    """
    assert_bindings(
        schema="sunData/combined/xsd006/xsd006.xsd",
        is_valid=True,
        instance="sunData/combined/xsd006/xsd006.n00.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd006_xsd006_n01():
    """
    xsd006 minOccurs/maxOccurs. Various combinations.
    """
    assert_bindings(
        schema="sunData/combined/xsd006/xsd006.xsd",
        is_valid=True,
        instance="sunData/combined/xsd006/xsd006.n01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd006_xsd006_n02():
    """
    xsd006 minOccurs/maxOccurs. Various combinations.
    """
    assert_bindings(
        schema="sunData/combined/xsd006/xsd006.xsd",
        is_valid=True,
        instance="sunData/combined/xsd006/xsd006.n02.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd006_xsd006_n03():
    """
    xsd006 minOccurs/maxOccurs. Various combinations.
    """
    assert_bindings(
        schema="sunData/combined/xsd006/xsd006.xsd",
        is_valid=True,
        instance="sunData/combined/xsd006/xsd006.n03.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd006_xsd006_n04():
    """
    xsd006 minOccurs/maxOccurs. Various combinations.
    """
    assert_bindings(
        schema="sunData/combined/xsd006/xsd006.xsd",
        is_valid=True,
        instance="sunData/combined/xsd006/xsd006.n04.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd006_xsd006_n05():
    """
    xsd006 minOccurs/maxOccurs. Various combinations.
    """
    assert_bindings(
        schema="sunData/combined/xsd006/xsd006.xsd",
        is_valid=True,
        instance="sunData/combined/xsd006/xsd006.n05.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd006_xsd006_n06():
    """
    xsd006 minOccurs/maxOccurs. Various combinations.
    """
    assert_bindings(
        schema="sunData/combined/xsd006/xsd006.xsd",
        is_valid=True,
        instance="sunData/combined/xsd006/xsd006.n06.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd006_xsd006_n07():
    """
    xsd006 minOccurs/maxOccurs. Various combinations.
    """
    assert_bindings(
        schema="sunData/combined/xsd006/xsd006.xsd",
        is_valid=True,
        instance="sunData/combined/xsd006/xsd006.n07.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd006_xsd006_n08():
    """
    xsd006 minOccurs/maxOccurs. Various combinations.
    """
    assert_bindings(
        schema="sunData/combined/xsd006/xsd006.xsd",
        is_valid=True,
        instance="sunData/combined/xsd006/xsd006.n08.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd006_xsd006_n09():
    """
    xsd006 minOccurs/maxOccurs. Various combinations.
    """
    assert_bindings(
        schema="sunData/combined/xsd006/xsd006.xsd",
        is_valid=True,
        instance="sunData/combined/xsd006/xsd006.n09.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd006_xsd006_n10():
    """
    xsd006 minOccurs/maxOccurs. Various combinations.
    """
    assert_bindings(
        schema="sunData/combined/xsd006/xsd006.xsd",
        is_valid=True,
        instance="sunData/combined/xsd006/xsd006.n10.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd006_xsd006_n11():
    """
    xsd006 minOccurs/maxOccurs. Various combinations.
    """
    assert_bindings(
        schema="sunData/combined/xsd006/xsd006.xsd",
        is_valid=True,
        instance="sunData/combined/xsd006/xsd006.n11.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd006_xsd006_v00():
    """
    xsd006 minOccurs/maxOccurs. Various combinations.
    """
    assert_bindings(
        schema="sunData/combined/xsd006/xsd006.xsd",
        is_valid=True,
        instance="sunData/combined/xsd006/xsd006.v00.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_xsd005_xsd005_n00():
    """
    xsd005 Complex type derivation. Missing content model.
    """
    assert_bindings(
        schema="sunData/combined/xsd005/xsd005.xsd",
        is_valid=True,
        instance="sunData/combined/xsd005/xsd005.n00.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd005_xsd005_n01():
    """
    xsd005 Complex type derivation. Missing content model.
    """
    assert_bindings(
        schema="sunData/combined/xsd005/xsd005.xsd",
        is_valid=True,
        instance="sunData/combined/xsd005/xsd005.n01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd005_xsd005_n02():
    """
    xsd005 Complex type derivation. Missing content model.
    """
    assert_bindings(
        schema="sunData/combined/xsd005/xsd005.xsd",
        is_valid=True,
        instance="sunData/combined/xsd005/xsd005.n02.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd005_xsd005_n03():
    """
    xsd005 Complex type derivation. Missing content model.
    """
    assert_bindings(
        schema="sunData/combined/xsd005/xsd005.xsd",
        is_valid=True,
        instance="sunData/combined/xsd005/xsd005.n03.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd005_xsd005_n04():
    """
    xsd005 Complex type derivation. Missing content model.
    """
    assert_bindings(
        schema="sunData/combined/xsd005/xsd005.xsd",
        is_valid=True,
        instance="sunData/combined/xsd005/xsd005.n04.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd005_xsd005_n05():
    """
    xsd005 Complex type derivation. Missing content model.
    """
    assert_bindings(
        schema="sunData/combined/xsd005/xsd005.xsd",
        is_valid=True,
        instance="sunData/combined/xsd005/xsd005.n05.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd005_xsd005_n06():
    """
    xsd005 Complex type derivation. Missing content model.
    """
    assert_bindings(
        schema="sunData/combined/xsd005/xsd005.xsd",
        is_valid=True,
        instance="sunData/combined/xsd005/xsd005.n06.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_xsd005_xsd005_v00():
    """
    xsd005 Complex type derivation. Missing content model.
    """
    assert_bindings(
        schema="sunData/combined/xsd005/xsd005.xsd",
        is_valid=True,
        instance="sunData/combined/xsd005/xsd005.v00.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_xsd004_xsd004_n00():
    """
    xsd004 Use of three different type of any element with different
    @namespace.
    """
    assert_bindings(
        schema="sunData/combined/xsd004/xsd004.xsd",
        is_valid=True,
        instance="sunData/combined/xsd004/xsd004.n00.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd004_xsd004_n01():
    """
    xsd004 Use of three different type of any element with different
    @namespace.
    """
    assert_bindings(
        schema="sunData/combined/xsd004/xsd004.xsd",
        is_valid=True,
        instance="sunData/combined/xsd004/xsd004.n01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd004_xsd004_n02():
    """
    xsd004 Use of three different type of any element with different
    @namespace.
    """
    assert_bindings(
        schema="sunData/combined/xsd004/xsd004.xsd",
        is_valid=True,
        instance="sunData/combined/xsd004/xsd004.n02.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd004_xsd004_n03():
    """
    xsd004 Use of three different type of any element with different
    @namespace.
    """
    assert_bindings(
        schema="sunData/combined/xsd004/xsd004.xsd",
        is_valid=True,
        instance="sunData/combined/xsd004/xsd004.n03.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd004_xsd004_n04():
    """
    xsd004 Use of three different type of any element with different
    @namespace.
    """
    assert_bindings(
        schema="sunData/combined/xsd004/xsd004.xsd",
        is_valid=True,
        instance="sunData/combined/xsd004/xsd004.n04.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd004_xsd004_n05():
    """
    xsd004 Use of three different type of any element with different
    @namespace.
    """
    assert_bindings(
        schema="sunData/combined/xsd004/xsd004.xsd",
        is_valid=True,
        instance="sunData/combined/xsd004/xsd004.n05.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd004_xsd004_n06():
    """
    xsd004 Use of three different type of any element with different
    @namespace.
    """
    assert_bindings(
        schema="sunData/combined/xsd004/xsd004.xsd",
        is_valid=True,
        instance="sunData/combined/xsd004/xsd004.n06.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd004_xsd004_n07():
    """
    xsd004 Use of three different type of any element with different
    @namespace.
    """
    assert_bindings(
        schema="sunData/combined/xsd004/xsd004.xsd",
        is_valid=True,
        instance="sunData/combined/xsd004/xsd004.n07.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd004_xsd004_n08():
    """
    xsd004 Use of three different type of any element with different
    @namespace.
    """
    assert_bindings(
        schema="sunData/combined/xsd004/xsd004.xsd",
        is_valid=True,
        instance="sunData/combined/xsd004/xsd004.n08.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd004_xsd004_n09():
    """
    xsd004 Use of three different type of any element with different
    @namespace.
    """
    assert_bindings(
        schema="sunData/combined/xsd004/xsd004.xsd",
        is_valid=True,
        instance="sunData/combined/xsd004/xsd004.n09.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd004_xsd004_n10():
    """
    xsd004 Use of three different type of any element with different
    @namespace.
    """
    assert_bindings(
        schema="sunData/combined/xsd004/xsd004.xsd",
        is_valid=True,
        instance="sunData/combined/xsd004/xsd004.n10.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd004_xsd004_n11():
    """
    xsd004 Use of three different type of any element with different
    @namespace.
    """
    assert_bindings(
        schema="sunData/combined/xsd004/xsd004.xsd",
        is_valid=True,
        instance="sunData/combined/xsd004/xsd004.n11.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd004_xsd004_n12():
    """
    xsd004 Use of three different type of any element with different
    @namespace.
    """
    assert_bindings(
        schema="sunData/combined/xsd004/xsd004.xsd",
        is_valid=True,
        instance="sunData/combined/xsd004/xsd004.n12.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd004_xsd004_v00():
    """
    xsd004 Use of three different type of any element with different
    @namespace.
    """
    assert_bindings(
        schema="sunData/combined/xsd004/xsd004.xsd",
        is_valid=True,
        instance="sunData/combined/xsd004/xsd004.v00.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_xsd003b_xsd003b_n00():
    """
    xsd003b Element redefinition. Test with redefinition with self-
    reference.                              @add in xsd003b.n00.xml must
    be number.
    """
    assert_bindings(
        schema="sunData/combined/xsd003b/xsd003b.xsd",
        is_valid=True,
        instance="sunData/combined/xsd003b/xsd003b.n00.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd003b_xsd003b_n01():
    """
    xsd003b Element redefinition. Test with redefinition with self-
    reference.                              @add in xsd003b.n00.xml must
    be number.
    """
    assert_bindings(
        schema="sunData/combined/xsd003b/xsd003b.xsd",
        is_valid=True,
        instance="sunData/combined/xsd003b/xsd003b.n01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_xsd003b_xsd003b_v00():
    """
    xsd003b Element redefinition. Test with redefinition with self-
    reference.                              @add in xsd003b.n00.xml must
    be number.
    """
    assert_bindings(
        schema="sunData/combined/xsd003b/xsd003b.xsd",
        is_valid=True,
        instance="sunData/combined/xsd003b/xsd003b.v00.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_xsd003b_xsd003b_v01():
    """
    xsd003b Element redefinition. Test with redefinition with self-
    reference.                              @add in xsd003b.n00.xml must
    be number.
    """
    assert_bindings(
        schema="sunData/combined/xsd003b/xsd003b.xsd",
        is_valid=True,
        instance="sunData/combined/xsd003b/xsd003b.v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_xsd003a_xsd003a_v00():
    """
    xsd003a Element redefinition. Test without redefinition.
    """
    assert_bindings(
        schema="sunData/combined/xsd003a/xsd003a.xsd",
        is_valid=True,
        instance="sunData/combined/xsd003a/xsd003a.v00.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_xsd002_xsd002_n00():
    """
    xsd002 - use of elementFormDefault="unqualified".
    - use of elementFormDefault and form attribute.
    - implicit use of "ur-type" as the content model of element.
    """
    assert_bindings(
        schema="sunData/combined/xsd002/xsd002.xsd",
        is_valid=True,
        instance="sunData/combined/xsd002/xsd002.n00.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd002_xsd002_n01():
    """
    xsd002 - use of elementFormDefault="unqualified".
    - use of elementFormDefault and form attribute.
    - implicit use of "ur-type" as the content model of element.
    """
    assert_bindings(
        schema="sunData/combined/xsd002/xsd002.xsd",
        is_valid=True,
        instance="sunData/combined/xsd002/xsd002.n01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd002_xsd002_n02():
    """
    xsd002 - use of elementFormDefault="unqualified".
    - use of elementFormDefault and form attribute.
    - implicit use of "ur-type" as the content model of element.
    """
    assert_bindings(
        schema="sunData/combined/xsd002/xsd002.xsd",
        is_valid=True,
        instance="sunData/combined/xsd002/xsd002.n02.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd002_xsd002_v00():
    """
    xsd002 - use of elementFormDefault="unqualified".
    - use of elementFormDefault and form attribute.
    - implicit use of "ur-type" as the content model of element.
    """
    assert_bindings(
        schema="sunData/combined/xsd002/xsd002.xsd",
        is_valid=True,
        instance="sunData/combined/xsd002/xsd002.v00.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_xsd002_xsd002_v01():
    """
    xsd002 - use of elementFormDefault="unqualified".
    - use of elementFormDefault and form attribute.
    - implicit use of "ur-type" as the content model of element.
    """
    assert_bindings(
        schema="sunData/combined/xsd002/xsd002.xsd",
        is_valid=True,
        instance="sunData/combined/xsd002/xsd002.v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_xsd001_xsd001_n00():
    """
    xsd001 - use of elementFormDefault="unqualified"
    - unusual minOccurs/maxOccurs (3 and 7 respectively)
    - complexType with simpleContent, and restriction.
    - simpleType within restriction.
    """
    assert_bindings(
        schema="sunData/combined/xsd001/xsd001.xsd",
        is_valid=True,
        instance="sunData/combined/xsd001/xsd001.n00.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd001_xsd001_n01():
    """
    xsd001 - use of elementFormDefault="unqualified"
    - unusual minOccurs/maxOccurs (3 and 7 respectively)
    - complexType with simpleContent, and restriction.
    - simpleType within restriction.
    """
    assert_bindings(
        schema="sunData/combined/xsd001/xsd001.xsd",
        is_valid=True,
        instance="sunData/combined/xsd001/xsd001.n01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd001_xsd001_n02():
    """
    xsd001 - use of elementFormDefault="unqualified"
    - unusual minOccurs/maxOccurs (3 and 7 respectively)
    - complexType with simpleContent, and restriction.
    - simpleType within restriction.
    """
    assert_bindings(
        schema="sunData/combined/xsd001/xsd001.xsd",
        is_valid=True,
        instance="sunData/combined/xsd001/xsd001.n02.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd001_xsd001_n03():
    """
    xsd001 - use of elementFormDefault="unqualified"
    - unusual minOccurs/maxOccurs (3 and 7 respectively)
    - complexType with simpleContent, and restriction.
    - simpleType within restriction.
    """
    assert_bindings(
        schema="sunData/combined/xsd001/xsd001.xsd",
        is_valid=True,
        instance="sunData/combined/xsd001/xsd001.n03.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd001_xsd001_n04():
    """
    xsd001 - use of elementFormDefault="unqualified"
    - unusual minOccurs/maxOccurs (3 and 7 respectively)
    - complexType with simpleContent, and restriction.
    - simpleType within restriction.
    """
    assert_bindings(
        schema="sunData/combined/xsd001/xsd001.xsd",
        is_valid=True,
        instance="sunData/combined/xsd001/xsd001.n04.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd001_xsd001_n05():
    """
    xsd001 - use of elementFormDefault="unqualified"
    - unusual minOccurs/maxOccurs (3 and 7 respectively)
    - complexType with simpleContent, and restriction.
    - simpleType within restriction.
    """
    assert_bindings(
        schema="sunData/combined/xsd001/xsd001.xsd",
        is_valid=True,
        instance="sunData/combined/xsd001/xsd001.n05.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd001_xsd001_n06():
    """
    xsd001 - use of elementFormDefault="unqualified"
    - unusual minOccurs/maxOccurs (3 and 7 respectively)
    - complexType with simpleContent, and restriction.
    - simpleType within restriction.
    """
    assert_bindings(
        schema="sunData/combined/xsd001/xsd001.xsd",
        is_valid=True,
        instance="sunData/combined/xsd001/xsd001.n06.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd001_xsd001_n07():
    """
    xsd001 - use of elementFormDefault="unqualified"
    - unusual minOccurs/maxOccurs (3 and 7 respectively)
    - complexType with simpleContent, and restriction.
    - simpleType within restriction.
    """
    assert_bindings(
        schema="sunData/combined/xsd001/xsd001.xsd",
        is_valid=True,
        instance="sunData/combined/xsd001/xsd001.n07.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_xsd001_xsd001_v00():
    """
    xsd001 - use of elementFormDefault="unqualified"
    - unusual minOccurs/maxOccurs (3 and 7 respectively)
    - complexType with simpleContent, and restriction.
    - simpleType within restriction.
    """
    assert_bindings(
        schema="sunData/combined/xsd001/xsd001.xsd",
        is_valid=True,
        instance="sunData/combined/xsd001/xsd001.v00.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_xsd001_xsd001_v01():
    """
    xsd001 - use of elementFormDefault="unqualified"
    - unusual minOccurs/maxOccurs (3 and 7 respectively)
    - complexType with simpleContent, and restriction.
    - simpleType within restriction.
    """
    assert_bindings(
        schema="sunData/combined/xsd001/xsd001.xsd",
        is_valid=True,
        instance="sunData/combined/xsd001/xsd001.v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_xsd001_xsd001_v02():
    """
    xsd001 - use of elementFormDefault="unqualified"
    - unusual minOccurs/maxOccurs (3 and 7 respectively)
    - complexType with simpleContent, and restriction.
    - simpleType within restriction.
    """
    assert_bindings(
        schema="sunData/combined/xsd001/xsd001.xsd",
        is_valid=True,
        instance="sunData/combined/xsd001/xsd001.v02.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_xsd001_xsd001_v03():
    """
    xsd001 - use of elementFormDefault="unqualified"
    - unusual minOccurs/maxOccurs (3 and 7 respectively)
    - complexType with simpleContent, and restriction.
    - simpleType within restriction.
    """
    assert_bindings(
        schema="sunData/combined/xsd001/xsd001.xsd",
        is_valid=True,
        instance="sunData/combined/xsd001/xsd001.v03.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_idc006_nogen_idc006_nogen_n00():
    """
    idc006.nogen ID Constaints. XPath engine test:  ".//a/*/b" and use of
    "." for both selector and field.
    """
    assert_bindings(
        schema="sunData/combined/identity/idc006/idc006.nogen.xsd",
        is_valid=True,
        instance="sunData/combined/identity/idc006/idc006.nogen.n00.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_idc006_nogen_idc006_nogen_n01():
    """
    idc006.nogen ID Constaints. XPath engine test:  ".//a/*/b" and use of
    "." for both selector and field.
    """
    assert_bindings(
        schema="sunData/combined/identity/idc006/idc006.nogen.xsd",
        is_valid=True,
        instance="sunData/combined/identity/idc006/idc006.nogen.n01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_idc006_nogen_idc006_nogen_v00():
    """
    idc006.nogen ID Constaints. XPath engine test:  ".//a/*/b" and use of
    "." for both selector and field.
    """
    assert_bindings(
        schema="sunData/combined/identity/idc006/idc006.nogen.xsd",
        is_valid=True,
        instance="sunData/combined/identity/idc006/idc006.nogen.v00.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_idc005_nogen_idc005_nogen_n00():
    """
    idc005.nogen ID Constraints. very naive test of identity constraint.
    """
    assert_bindings(
        schema="sunData/combined/identity/idc005/idc005.nogen.xsd",
        is_valid=True,
        instance="sunData/combined/identity/idc005/idc005.nogen.n00.xml",
        instance_is_valid=False,
        class_name="BookCatalogue",
        version="1.0",
    )


def test_idc005_nogen_idc005_nogen_n01():
    """
    idc005.nogen ID Constraints. very naive test of identity constraint.
    """
    assert_bindings(
        schema="sunData/combined/identity/idc005/idc005.nogen.xsd",
        is_valid=True,
        instance="sunData/combined/identity/idc005/idc005.nogen.n01.xml",
        instance_is_valid=False,
        class_name="BookCatalogue",
        version="1.0",
    )


def test_idc005_nogen_idc005_nogen_v00():
    """
    idc005.nogen ID Constraints. very naive test of identity constraint.
    """
    assert_bindings(
        schema="sunData/combined/identity/idc005/idc005.nogen.xsd",
        is_valid=True,
        instance="sunData/combined/identity/idc005/idc005.nogen.v00.xml",
        instance_is_valid=True,
        class_name="BookCatalogue",
        version="1.0",
    )


def test_idc004_nogen_idc004_nogen_n00():
    """
    idc004.nogen ID Constraints.
    """
    assert_bindings(
        schema="sunData/combined/identity/idc004/idc004.nogen.xsd",
        is_valid=True,
        instance="sunData/combined/identity/idc004/idc004.nogen.n00.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_idc004_nogen_idc004_nogen_n01():
    """
    idc004.nogen ID Constraints.
    """
    assert_bindings(
        schema="sunData/combined/identity/idc004/idc004.nogen.xsd",
        is_valid=True,
        instance="sunData/combined/identity/idc004/idc004.nogen.n01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_idc004_nogen_idc004_nogen_n02():
    """
    idc004.nogen ID Constraints.
    """
    assert_bindings(
        schema="sunData/combined/identity/idc004/idc004.nogen.xsd",
        is_valid=True,
        instance="sunData/combined/identity/idc004/idc004.nogen.n02.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_idc004_nogen_idc004_nogen_n03():
    """
    idc004.nogen ID Constraints.
    """
    assert_bindings(
        schema="sunData/combined/identity/idc004/idc004.nogen.xsd",
        is_valid=True,
        instance="sunData/combined/identity/idc004/idc004.nogen.n03.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_idc004_nogen_idc004_nogen_v00():
    """
    idc004.nogen ID Constraints.
    """
    assert_bindings(
        schema="sunData/combined/identity/idc004/idc004.nogen.xsd",
        is_valid=True,
        instance="sunData/combined/identity/idc004/idc004.nogen.v00.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_idc001_nogen_idc001_nogen_n00():
    """
    idc001.nogen ID Constraints.
    """
    assert_bindings(
        schema="sunData/combined/identity/idc001/idc001.nogen.xsd",
        is_valid=True,
        instance="sunData/combined/identity/idc001/idc001.nogen.n00.xml",
        instance_is_valid=False,
        class_name="BookCatalogue",
        version="1.0",
    )


def test_idc001_nogen_idc001_nogen_v00():
    """
    idc001.nogen ID Constraints.
    """
    assert_bindings(
        schema="sunData/combined/identity/idc001/idc001.nogen.xsd",
        is_valid=True,
        instance="sunData/combined/identity/idc001/idc001.nogen.v00.xml",
        instance_is_valid=True,
        class_name="BookCatalogue",
        version="1.0",
    )


def test_idc001_nogen_idc001_nogen_v01():
    """
    idc001.nogen ID Constraints.
    """
    assert_bindings(
        schema="sunData/combined/identity/idc001/idc001.nogen.xsd",
        is_valid=True,
        instance="sunData/combined/identity/idc001/idc001.nogen.v01.xml",
        instance_is_valid=True,
        class_name="BookCatalogue",
        version="1.0",
    )


def test_identitytestsuitetest004_test_1_v():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/identity/IdentityTestSuite/004/test.xsd",
        is_valid=True,
        instance="sunData/combined/identity/IdentityTestSuite/004/test.1.v.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_identitytestsuitetest004_test_2_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/identity/IdentityTestSuite/004/test.xsd",
        is_valid=True,
        instance="sunData/combined/identity/IdentityTestSuite/004/test.2.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_identitytestsuitetest004_test_3_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/identity/IdentityTestSuite/004/test.xsd",
        is_valid=True,
        instance="sunData/combined/identity/IdentityTestSuite/004/test.3.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_identitytestsuitetest003_test_1_v():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/identity/IdentityTestSuite/003/test.xsd",
        is_valid=True,
        instance="sunData/combined/identity/IdentityTestSuite/003/test.1.v.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_identitytestsuitetest003_test_2_v():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/identity/IdentityTestSuite/003/test.xsd",
        is_valid=True,
        instance="sunData/combined/identity/IdentityTestSuite/003/test.2.v.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_identitytestsuitetest003_test_3_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/identity/IdentityTestSuite/003/test.xsd",
        is_valid=True,
        instance="sunData/combined/identity/IdentityTestSuite/003/test.3.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_identitytestsuitetest002_test_1_v():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/identity/IdentityTestSuite/002/test.xsd",
        is_valid=True,
        instance="sunData/combined/identity/IdentityTestSuite/002/test.1.v.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_identitytestsuitetest002_test_2_v():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/identity/IdentityTestSuite/002/test.xsd",
        is_valid=True,
        instance="sunData/combined/identity/IdentityTestSuite/002/test.2.v.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_identitytestsuitetest002_test_3_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/identity/IdentityTestSuite/002/test.xsd",
        is_valid=True,
        instance="sunData/combined/identity/IdentityTestSuite/002/test.3.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_identitytestsuitetest001_test_1_v():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/identity/IdentityTestSuite/001/test.xsd",
        is_valid=True,
        instance="sunData/combined/identity/IdentityTestSuite/001/test.1.v.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_identitytestsuitetest001_test_2_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/identity/IdentityTestSuite/001/test.xsd",
        is_valid=True,
        instance="sunData/combined/identity/IdentityTestSuite/001/test.2.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test009_test_13_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/009/test.xsd",
        is_valid=True,
        instance="sunData/combined/009/test.13.n.xml",
        instance_is_valid=False,
        class_name="Prohibit",
        version="1.0",
    )


def test_test009_test_8_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/009/test.xsd",
        is_valid=True,
        instance="sunData/combined/009/test.8.n.xml",
        instance_is_valid=False,
        class_name="Override",
        version="1.0",
    )


def test_test009_test_1_v():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/009/test.xsd",
        is_valid=True,
        instance="sunData/combined/009/test.1.v.xml",
        instance_is_valid=True,
        class_name="Base",
        version="1.0",
    )


def test_test009_test_10_v():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/009/test.xsd",
        is_valid=True,
        instance="sunData/combined/009/test.10.v.xml",
        instance_is_valid=True,
        class_name="Add",
        version="1.0",
    )


def test_test009_test_11_v():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/009/test.xsd",
        is_valid=True,
        instance="sunData/combined/009/test.11.v.xml",
        instance_is_valid=True,
        class_name="Prohibit",
        version="1.0",
    )


def test_test009_test_12_v():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/009/test.xsd",
        is_valid=True,
        instance="sunData/combined/009/test.12.v.xml",
        instance_is_valid=True,
        class_name="Prohibit",
        version="1.0",
    )


def test_test009_test_2_v():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/009/test.xsd",
        is_valid=True,
        instance="sunData/combined/009/test.2.v.xml",
        instance_is_valid=True,
        class_name="Base",
        version="1.0",
    )


def test_test009_test_3_v():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/009/test.xsd",
        is_valid=True,
        instance="sunData/combined/009/test.3.v.xml",
        instance_is_valid=True,
        class_name="Default",
        version="1.0",
    )


def test_test009_test_4_v():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/009/test.xsd",
        is_valid=True,
        instance="sunData/combined/009/test.4.v.xml",
        instance_is_valid=True,
        class_name="Default",
        version="1.0",
    )


def test_test009_test_5_v():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/009/test.xsd",
        is_valid=True,
        instance="sunData/combined/009/test.5.v.xml",
        instance_is_valid=True,
        class_name="Override",
        version="1.0",
    )


def test_test009_test_6_v():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/009/test.xsd",
        is_valid=True,
        instance="sunData/combined/009/test.6.v.xml",
        instance_is_valid=True,
        class_name="Override",
        version="1.0",
    )


def test_test009_test_7_v():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/009/test.xsd",
        is_valid=True,
        instance="sunData/combined/009/test.7.v.xml",
        instance_is_valid=True,
        class_name="Override",
        version="1.0",
    )


def test_test009_test_9_v():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/009/test.xsd",
        is_valid=True,
        instance="sunData/combined/009/test.9.v.xml",
        instance_is_valid=True,
        class_name="Add",
        version="1.0",
    )


def test_test008_test_1_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/008/test.xsd",
        is_valid=True,
        instance="sunData/combined/008/test.1.n.xml",
        instance_is_valid=False,
        class_name="Extension",
        version="1.0",
    )


def test_test008_test_10_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/008/test.xsd",
        is_valid=True,
        instance="sunData/combined/008/test.10.n.xml",
        instance_is_valid=False,
        class_name="Alias",
        version="1.0",
    )


def test_test008_test_11_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/008/test.xsd",
        is_valid=True,
        instance="sunData/combined/008/test.11.n.xml",
        instance_is_valid=False,
        class_name="Alias",
        version="1.0",
    )


def test_test008_test_12_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/008/test.xsd",
        is_valid=True,
        instance="sunData/combined/008/test.12.n.xml",
        instance_is_valid=False,
        class_name="Alias",
        version="1.0",
    )


def test_test008_test_5_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/008/test.xsd",
        is_valid=True,
        instance="sunData/combined/008/test.5.n.xml",
        instance_is_valid=False,
        class_name="Restriction",
        version="1.0",
    )


def test_test008_test_7_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/008/test.xsd",
        is_valid=True,
        instance="sunData/combined/008/test.7.n.xml",
        instance_is_valid=False,
        class_name="Restriction",
        version="1.0",
    )


def test_test008_test_8_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/008/test.xsd",
        is_valid=True,
        instance="sunData/combined/008/test.8.n.xml",
        instance_is_valid=False,
        class_name="Restriction",
        version="1.0",
    )


def test_test008_test_9_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/008/test.xsd",
        is_valid=True,
        instance="sunData/combined/008/test.9.n.xml",
        instance_is_valid=False,
        class_name="Alias",
        version="1.0",
    )


def test_test008_test_2_v():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/008/test.xsd",
        is_valid=True,
        instance="sunData/combined/008/test.2.v.xml",
        instance_is_valid=True,
        class_name="Extension",
        version="1.0",
    )


def test_test008_test_3_v():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/008/test.xsd",
        is_valid=True,
        instance="sunData/combined/008/test.3.v.xml",
        instance_is_valid=True,
        class_name="Extension",
        version="1.0",
    )


def test_test008_test_4_v():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/008/test.xsd",
        is_valid=True,
        instance="sunData/combined/008/test.4.v.xml",
        instance_is_valid=True,
        class_name="Extension",
        version="1.0",
    )


def test_test008_test_6_v():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/008/test.xsd",
        is_valid=True,
        instance="sunData/combined/008/test.6.v.xml",
        instance_is_valid=True,
        class_name="Restriction",
        version="1.0",
    )


def test_test007_test_1_v():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/007/test.xsd",
        is_valid=True,
        instance="sunData/combined/007/test.1.v.xml",
        instance_is_valid=True,
        class_name="Emptywc",
        version="1.0",
    )


def test_test007_test_6_v():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/007/test.xsd",
        is_valid=True,
        instance="sunData/combined/007/test.6.v.xml",
        instance_is_valid=True,
        class_name="JustA",
        version="1.0",
    )


def test_test007_test_2_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/007/test.xsd",
        is_valid=True,
        instance="sunData/combined/007/test.2.n.xml",
        instance_is_valid=False,
        class_name="Emptywc",
        version="1.0",
    )


def test_test007_test_3_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/007/test.xsd",
        is_valid=True,
        instance="sunData/combined/007/test.3.n.xml",
        instance_is_valid=False,
        class_name="Emptywc",
        version="1.0",
    )


def test_test007_test_4_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/007/test.xsd",
        is_valid=True,
        instance="sunData/combined/007/test.4.n.xml",
        instance_is_valid=False,
        class_name="Emptywc",
        version="1.0",
    )


def test_test007_test_5_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/007/test.xsd",
        is_valid=True,
        instance="sunData/combined/007/test.5.n.xml",
        instance_is_valid=False,
        class_name="JustA",
        version="1.0",
    )


def test_test007_test_7_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/007/test.xsd",
        is_valid=True,
        instance="sunData/combined/007/test.7.n.xml",
        instance_is_valid=False,
        class_name="JustA",
        version="1.0",
    )


def test_test007_test_8_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/007/test.xsd",
        is_valid=True,
        instance="sunData/combined/007/test.8.n.xml",
        instance_is_valid=False,
        class_name="JustA",
        version="1.0",
    )


@pytest.mark.xfail
def test_test006_test_1_v():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.1.v.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_10_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.10.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_11_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.11.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_12_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.12.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_13_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.13.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_14_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.14.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_15_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.15.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_16_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.16.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_17_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.17.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_18_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.18.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_19_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.19.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_test006_test_2_v():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.2.v.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_20_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.20.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_21_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.21.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_22_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.22.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_23_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.23.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_24_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.24.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_25_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.25.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_26_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.26.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_27_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.27.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_28_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.28.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_29_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.29.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_3_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.3.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_30_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.30.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_31_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.31.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_32_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.32.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_33_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.33.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_34_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.34.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_4_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.4.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_5_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.5.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_6_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.6.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_7_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.7.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_8_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.8.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test006_test_9_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/006/test.xsd",
        is_valid=True,
        instance="sunData/combined/006/test.9.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test005_test_1_v():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/005/test.xsd",
        is_valid=True,
        instance="sunData/combined/005/test.1.v.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_test005_test_2_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/005/test.xsd",
        is_valid=True,
        instance="sunData/combined/005/test.2.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test005_test_3_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/005/test.xsd",
        is_valid=True,
        instance="sunData/combined/005/test.3.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test005_test_4_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/005/test.xsd",
        is_valid=True,
        instance="sunData/combined/005/test.4.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test005_test_5_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/005/test.xsd",
        is_valid=True,
        instance="sunData/combined/005/test.5.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test004_test_1_v():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/004/test.xsd",
        is_valid=True,
        instance="sunData/combined/004/test.1.v.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_test004_test_2_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/004/test.xsd",
        is_valid=True,
        instance="sunData/combined/004/test.2.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test004_test_3_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/004/test.xsd",
        is_valid=True,
        instance="sunData/combined/004/test.3.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test004_test_4_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/004/test.xsd",
        is_valid=True,
        instance="sunData/combined/004/test.4.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test004_test_5_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/004/test.xsd",
        is_valid=True,
        instance="sunData/combined/004/test.5.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test003_test_1_v():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/003/test.xsd",
        is_valid=True,
        instance="sunData/combined/003/test.1.v.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_test003_test_2_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/003/test.xsd",
        is_valid=True,
        instance="sunData/combined/003/test.2.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test003_test_3_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/003/test.xsd",
        is_valid=True,
        instance="sunData/combined/003/test.3.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test003_test_4_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/003/test.xsd",
        is_valid=True,
        instance="sunData/combined/003/test.4.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test003_test_5_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/003/test.xsd",
        is_valid=True,
        instance="sunData/combined/003/test.5.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test002_test_1_v():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/002/test.xsd",
        is_valid=True,
        instance="sunData/combined/002/test.1.v.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_test002_test_2_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/002/test.xsd",
        is_valid=True,
        instance="sunData/combined/002/test.2.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test002_test_3_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/002/test.xsd",
        is_valid=True,
        instance="sunData/combined/002/test.3.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test002_test_4_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/002/test.xsd",
        is_valid=True,
        instance="sunData/combined/002/test.4.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test002_test_5_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/002/test.xsd",
        is_valid=True,
        instance="sunData/combined/002/test.5.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_test001_test_1_v():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/001/test.xsd",
        is_valid=True,
        instance="sunData/combined/001/test.1.v.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_test001_test_2_n():
    """
    test
    """
    assert_bindings(
        schema="sunData/combined/001/test.xsd",
        is_valid=True,
        instance="sunData/combined/001/test.2.n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_annotation00101m4_positive():
    """
    machine-targeted  annotation for an attribute group definition (valid
    schema) Annotations provide for human- and machine-targeted
    annotations of schema components.                               In the
    test the machine-targeted annotation                               is
    provided for an attribute group definition.
    """
    assert_bindings(
        schema="sunData/AGroupDef/annotation/annotation00101m/annotation00101m4.xsd",
        is_valid=True,
        instance="sunData/AGroupDef/annotation/annotation00101m/annotation00101m4_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_annotation00101m1_positive():
    """
    human-targeted  annotation for an attribute group definition (valid
    schema) Annotations provide for human- and machine-targeted
    annotations of schema components.                               In the
    test the human-targeted annotation                               is
    provided for an attribute group definition.
    """
    assert_bindings(
        schema="sunData/AGroupDef/annotation/annotation00101m/annotation00101m1.xsd",
        is_valid=True,
        instance="sunData/AGroupDef/annotation/annotation00101m/annotation00101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_ag_targetns00101m1_p_positive():
    """
    Attribute group reference with QName. (valid schema) Attribute Group
    use should has proper namespace prefix in the ref value
    to be resolved to its declaration.
    """
    assert_bindings(
        schema="sunData/AGroupDef/AG_targetNS/AG_targetNS00101m/AG_targetNS00101m1_p.xsd",
        is_valid=True,
        instance="sunData/AGroupDef/AG_targetNS/AG_targetNS00101m/AG_targetNS00101m1.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_ag_name00101m1_p_positive():
    """
    Attribute group declaration. (valid schema) Attribute Group use should
    has proper ref value to be resolved to its declaration.
    """
    assert_bindings(
        schema="sunData/AGroupDef/AG_name/AG_name00101m/AG_name00101m1_p.xsd",
        is_valid=True,
        instance="sunData/AGroupDef/AG_name/AG_name00101m/AG_name00101m1.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_ag_attrwcard00101m1_positive():
    """
    Attribute wildcard is declared in attribute group.  (valid schema)
    According to declared attribute wildcard content of the attributes in
    the                                   document should not be
    processed.
    """
    assert_bindings(
        schema="sunData/AGroupDef/AG_attrWCard/AG_attrWCard00101m/AG_attrWCard00101m1.xsd",
        is_valid=True,
        instance="sunData/AGroupDef/AG_attrWCard/AG_attrWCard00101m/AG_attrWCard00101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_ag_attrusens00101m1_p_positive():
    """
    Attribute is declared in attribute group by reference with QName.
    (valid schema) Attribute Use should has proper namespace prefix in the
    ref value                                   to be resolved to its
    declaration.
    """
    assert_bindings(
        schema="sunData/AGroupDef/AG_attrUse/AG_attrUseNS00101m/AG_attrUseNS00101m1_p.xsd",
        is_valid=True,
        instance="sunData/AGroupDef/AG_attrUse/AG_attrUseNS00101m/AG_attrUseNS00101m1.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_valconstr00201m3_positive():
    """
    Attribute with 'default' value and "optional" 'use' is declared
    entirely within element declaration (valid schema) If 'default' and
    'use' are both present,                                   'use' must
    have the actual value 'optional'.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_valConstr/AD_valConstr00201m/AD_valConstr00201m3.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_valConstr/AD_valConstr00201m/AD_valConstr00201m3_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_valconstr00101m_ad_val_constr00101m1_p():
    """
    Attribute with fixed value is declared within element by reference
    (valid schema) Attribute declared with fixed value may not have
    another value in an instance document.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_valConstr/AD_valConstr00101m/AD_valConstr00101m.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_valConstr/AD_valConstr00101m/AD_valConstr00101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_valconstr00101m_ad_val_constr00101m1_n():
    """
    Attribute with fixed value is declared within element by reference
    (valid schema) Attribute declared with fixed value may not have
    another value in an instance document.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_valConstr/AD_valConstr00101m/AD_valConstr00101m.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_valConstr/AD_valConstr00101m/AD_valConstr00101m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_ad_valconstr00101m_ad_val_constr00101m2_p():
    """
    Attribute with fixed value is declared within element by reference
    (valid schema) Attribute declared with fixed value may not have
    another value in an instance document.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_valConstr/AD_valConstr00101m/AD_valConstr00101m.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_valConstr/AD_valConstr00101m/AD_valConstr00101m2_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_valconstr00101m_ad_val_constr00101m2_n():
    """
    Attribute with fixed value is declared within element by reference
    (valid schema) Attribute declared with fixed value may not have
    another value in an instance document.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_valConstr/AD_valConstr00101m/AD_valConstr00101m.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_valConstr/AD_valConstr00101m/AD_valConstr00101m2_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_ad_type00102m_ad_type00102m1_p():
    """
    Attribute with restriction type is declared within element by
    reference  (valid schema) The value of the attribute should conform to
    restrictions declared in type of the attribute.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_type/AD_type00102m/AD_type00102m.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_type/AD_type00102m/AD_type00102m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_type00102m_ad_type00102m1_n():
    """
    Attribute with restriction type is declared within element by
    reference  (valid schema) The value of the attribute should conform to
    restrictions declared in type of the attribute.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_type/AD_type00102m/AD_type00102m.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_type/AD_type00102m/AD_type00102m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_ad_type00102m_ad_type00102m2_p():
    """
    Attribute with restriction type is declared within element by
    reference  (valid schema) The value of the attribute should conform to
    restrictions declared in type of the attribute.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_type/AD_type00102m/AD_type00102m.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_type/AD_type00102m/AD_type00102m2_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_type00102m_ad_type00102m2_n():
    """
    Attribute with restriction type is declared within element by
    reference  (valid schema) The value of the attribute should conform to
    restrictions declared in type of the attribute.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_type/AD_type00102m/AD_type00102m.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_type/AD_type00102m/AD_type00102m2_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_ad_type00101m_ad_type00101m1_p():
    """
    Attribute declared within element by reference (valid schema) The
    value of the attribute should conform to declared type of the
    attribute.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_type/AD_type00101m/AD_type00101m.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_type/AD_type00101m/AD_type00101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_type00101m_ad_type00101m1_n():
    """
    Attribute declared within element by reference (valid schema) The
    value of the attribute should conform to declared type of the
    attribute.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_type/AD_type00101m/AD_type00101m.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_type/AD_type00101m/AD_type00101m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_ad_type00101m_ad_type00101m2_p():
    """
    Attribute declared within element by reference (valid schema) The
    value of the attribute should conform to declared type of the
    attribute.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_type/AD_type00101m/AD_type00101m.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_type/AD_type00101m/AD_type00101m2_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_type00101m_ad_type00101m2_n():
    """
    Attribute declared within element by reference (valid schema) The
    value of the attribute should conform to declared type of the
    attribute.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_type/AD_type00101m/AD_type00101m.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_type/AD_type00101m/AD_type00101m2_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_ad_targetns00101m_ad_target_ns00101m1_p():
    """
    Attribute explicitly declared qualified. (valid schema) Attribute
    explicitly declared qualified should be used with NSName.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_targetNS/AD_targetNS00101m/AD_targetNS00101m.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_targetNS/AD_targetNS00101m/AD_targetNS00101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_targetns00101m_ad_target_ns00101m1_n():
    """
    Attribute explicitly declared qualified. (valid schema) Attribute
    explicitly declared qualified should be used with NSName.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_targetNS/AD_targetNS00101m/AD_targetNS00101m.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_targetNS/AD_targetNS00101m/AD_targetNS00101m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_ad_targetns00101m_ad_target_ns00101m2_n():
    """
    Attribute explicitly declared qualified. (valid schema) Attribute
    explicitly declared qualified should be used with NSName.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_targetNS/AD_targetNS00101m/AD_targetNS00101m.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_targetNS/AD_targetNS00101m/AD_targetNS00101m2_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_ad_targetns00101m_ad_target_ns00101m3_p():
    """
    Attribute explicitly declared qualified. (valid schema) Attribute
    explicitly declared qualified should be used with NSName.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_targetNS/AD_targetNS00101m/AD_targetNS00101m.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_targetNS/AD_targetNS00101m/AD_targetNS00101m3_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_targetns00101m_ad_target_ns00101m3_n():
    """
    Attribute explicitly declared qualified. (valid schema) Attribute
    explicitly declared qualified should be used with NSName.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_targetNS/AD_targetNS00101m/AD_targetNS00101m.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_targetNS/AD_targetNS00101m/AD_targetNS00101m3_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_ad_scope00101m1_positive():
    """
    Attribute declared with global scope (valid schema) Attribute declared
    with global scope can be referenced in any declaration in the schema.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_scope/AD_scope00101m/AD_scope00101m1.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_scope/AD_scope00101m/AD_scope00101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00118_ad_name00118_p():
    """
    Attribute names contain an uncased letter followed by upper or lower
    case letter. (valid schema) Declare an element with two attributes of
    type int. Name them using
    Unicode letter #x01BB which is neither upper nor lower.
    The document AD_name00118_p.xml sets all the attributes.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00118/AD_name00118.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00118/AD_name00118_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00115_ad_name00115_p():
    """
    Attribute names contain only punctuation characters and digits. (valid
    schema) Declare an element with two attributes of type int. Name the
    first one                                      as "_-." and the second
    one as "_-0.".
    The document AD_name00115_p.xml sets the attributes to 0 and 1
    respectively.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00115/AD_name00115.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00115/AD_name00115_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00114_ad_name00114_p():
    """
    Attribute names contain lower case and upper case letters and non-
    letter characters. (valid schema) Declare an element with several
    attributes of type int. Name them as follows:
    "aaaa",  "bbbB",  "ccCc",  "ddDD",  "eEee",
    "fFfF",  "pPPp",  "gGGG",  "Hhhh",  "IiiI",  "JjJj",
    "KkKK",  "LLll",  "MMmM",  "NNNn",  "OOOO",
    "bbb0",  "cc0c",  "dd00",  "e0ee",  "f0f0",  "p00p",  "g000",
    "bbb_",  "cc_c",  "dd__",  "e_ee",  "f_f_",  "p__p",  "g___",
    "H111",  "I11I",  "J1J1",  "K1KK",  "LL11",  "MM1M",  "NNN1",
    "H---",  "I--I",  "J-J-",  "K-KK",  "LL--",  "MM-M",  "NNN-".
    The document AD_name00114_p.xml sets all the attributes.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00114/AD_name00114.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00114/AD_name00114_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00113_ad_name00113_p():
    """
    Attribute names contain digits followed by a non-digit characters.
    (valid schema) Declare an element with three attributes of type int.
    Name them as follows:
    "aa111a2Aa", "aa22B3c", "aa3-4_".
    The document AD_name00113_p.xml sets the attributes to 0, 1 and 2
    respectively.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00113/AD_name00113.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00113/AD_name00113_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00112_ad_name00112_p():
    r"""
    Attribute name contains 7 punctuation characters. (valid schema)
    Declare an element with two attributes of type int. Name the first one
    using 7 punctuation characters:
    hyphen ('-', \u002D, HYPHEN-MINUS), period ('.', \u002E, FULL STOP),
    underscore ('_', \u005F, LOW LINE),
    dot ('.', \u00B7, MIDDLE DOT), \u0387, GREEK ANO TELEIA,
    \u06DD, ARABIC END OF AYAH and \u06DE, ARABIC START OF RUB EL HIZB.
    Name the                                       second attribute with
    the same name except the characters described.
    The document AD_name00112_p.xml sets the attributes to 0 and 1
    respectively.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00112/AD_name00112.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00112/AD_name00112_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00111_ad_name00111_p():
    r"""
    Attribute names contain several punctuation characters. (valid schema)
    Declare an element with several attributes of type int. Name the
    attributes                                      using 7 punctuation
    characters:                                       hyphen ('-', \u002D,
    HYPHEN-MINUS), period ('.', \u002E, FULL STOP),
    underscore ('_', \u005F, LOW LINE),
    dot ('.', \u00B7, MIDDLE DOT), \u0387, GREEK ANO TELEIA,
    \u06DD, ARABIC END OF AYAH and \u06DE, ARABIC START OF RUB EL HIZB.
    The document AD_name00111_p.xml sets the attributes to 0, 1, 2, ..., 6
    respectively.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00111/AD_name00111.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00111/AD_name00111_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00110m9_positive():
    """
    Attributes have names that end with the combining characters 0x0f39,
    0x0f3e, 0x0f3f, 0x0f71, 0x0f7a, 0x0f84, 0x0f86, 0x0f86, 0x0f87,
    0x0f90, 0x0f92, 0x0f95, 0x0f97, 0x0f99, 0x0fa3, 0x0fad, 0x0fb1,
    0x0fb4, 0x0fb7, 0x0fb9 (valid schema) Declare 20 local string
    attributes with the names that end with the following
    combining characters: 0x0f39, 0x0f3e, 0x0f3f, 0x0f71, 0x0f7a, 0x0f84,
    0x0f86, 0x0f86, 0x0f87, 0x0f90, 0x0f92, 0x0f95, 0x0f97, 0x0f99,
    0x0fa3, 0x0fad, 0x0fb1, 0x0fb4, 0x0fb7, 0x0fb9 respectively. The
    document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00110m/AD_name00110m9.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00110m/AD_name00110m9_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00110m8_positive():
    """
    Attributes have names that end with the combining characters 0x0e31,
    0x0e34, 0x0e37, 0x0e3a, 0x0e47, 0x0e4a, 0x0e4e, 0x0eb1, 0x0eb4,
    0x0eb6, 0x0eb9, 0x0ebb, 0x0ebb, 0x0ebc, 0x0ec8, 0x0eca, 0x0ecd,
    0x0f18, 0x0f18, 0x0f19, 0x0f35, 0x0f37 (valid schema) Declare 22 local
    string attributes with the names that end with the following
    combining characters: 0x0e31, 0x0e34, 0x0e37, 0x0e3a, 0x0e47, 0x0e4a,
    0x0e4e, 0x0eb1, 0x0eb4, 0x0eb6, 0x0eb9, 0x0ebb, 0x0ebb, 0x0ebc,
    0x0ec8, 0x0eca, 0x0ecd, 0x0f18, 0x0f18, 0x0f19, 0x0f35, 0x0f37
    respectively. The document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00110m/AD_name00110m8.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00110m/AD_name00110m8_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00110m7_positive():
    """
    Attributes have names that end with the combining characters 0x0c82,
    0x0c82, 0x0c83, 0x0cbe, 0x0cc1, 0x0cc4, 0x0cc6, 0x0cc7, 0x0cc8,
    0x0cca, 0x0ccb, 0x0ccd, 0x0cd5, 0x0cd5, 0x0cd6, 0x0d02, 0x0d02,
    0x0d03, 0x0d3e, 0x0d40, 0x0d43, 0x0d46, 0x0d47, 0x0d48, 0x0d4a,
    0x0d4b, 0x0d4d, 0x0d57 (valid schema) Declare 28 local string
    attributes with the names that end with the following
    combining characters: 0x0c82, 0x0c82, 0x0c83, 0x0cbe, 0x0cc1, 0x0cc4,
    0x0cc6, 0x0cc7, 0x0cc8, 0x0cca, 0x0ccb, 0x0ccd, 0x0cd5, 0x0cd5,
    0x0cd6, 0x0d02, 0x0d02, 0x0d03, 0x0d3e, 0x0d40, 0x0d43, 0x0d46,
    0x0d47, 0x0d48, 0x0d4a, 0x0d4b, 0x0d4d, 0x0d57 respectively. The
    document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00110m/AD_name00110m7.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00110m/AD_name00110m7_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00110m6_positive():
    """
    Attributes have names that end with the combining characters 0x0b82,
    0x0b82, 0x0b83, 0x0bbe, 0x0bc0, 0x0bc2, 0x0bc6, 0x0bc7, 0x0bc8,
    0x0bca, 0x0bcb, 0x0bcd, 0x0bd7, 0x0c01, 0x0c02, 0x0c03, 0x0c3e,
    0x0c41, 0x0c44, 0x0c46, 0x0c47, 0x0c48, 0x0c4a, 0x0c4b, 0x0c4d,
    0x0c55, 0x0c55, 0x0c56 (valid schema) Declare 28 local string
    attributes with the names that end with the following
    combining characters: 0x0b82, 0x0b82, 0x0b83, 0x0bbe, 0x0bc0, 0x0bc2,
    0x0bc6, 0x0bc7, 0x0bc8, 0x0bca, 0x0bcb, 0x0bcd, 0x0bd7, 0x0c01,
    0x0c02, 0x0c03, 0x0c3e, 0x0c41, 0x0c44, 0x0c46, 0x0c47, 0x0c48,
    0x0c4a, 0x0c4b, 0x0c4d, 0x0c55, 0x0c55, 0x0c56 respectively. The
    document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00110m/AD_name00110m6.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00110m/AD_name00110m6_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00110m5_positive():
    """
    Attributes have names that end with the combining characters 0x0abc,
    0x0abe, 0x0ac1, 0x0ac5, 0x0ac7, 0x0ac8, 0x0ac9, 0x0acb, 0x0acc,
    0x0acd, 0x0b01, 0x0b02, 0x0b03, 0x0b3c, 0x0b3e, 0x0b40, 0x0b43,
    0x0b47, 0x0b47, 0x0b48, 0x0b4b, 0x0b4c, 0x0b4d, 0x0b56, 0x0b56, 0x0b57
    (valid schema) Declare 26 local string attributes with the names that
    end with the following                               combining
    characters: 0x0abc, 0x0abe, 0x0ac1, 0x0ac5, 0x0ac7, 0x0ac8, 0x0ac9,
    0x0acb, 0x0acc, 0x0acd, 0x0b01, 0x0b02, 0x0b03, 0x0b3c, 0x0b3e,
    0x0b40, 0x0b43, 0x0b47, 0x0b47, 0x0b48, 0x0b4b, 0x0b4c, 0x0b4d,
    0x0b56, 0x0b56, 0x0b57 respectively. The document set their values to
    0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00110m/AD_name00110m5.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00110m/AD_name00110m5_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00110m4_positive():
    """
    Attributes have names that end with the combining characters 0x09e2,
    0x09e2, 0x09e3, 0x0a02, 0x0a3c, 0x0a3e, 0x0a3f, 0x0a40, 0x0a41,
    0x0a42, 0x0a47, 0x0a47, 0x0a48, 0x0a4b, 0x0a4c, 0x0a4d, 0x0a70,
    0x0a70, 0x0a71, 0x0a81, 0x0a82, 0x0a83 (valid schema) Declare 22 local
    string attributes with the names that end with the following
    combining characters: 0x09e2, 0x09e2, 0x09e3, 0x0a02, 0x0a3c, 0x0a3e,
    0x0a3f, 0x0a40, 0x0a41, 0x0a42, 0x0a47, 0x0a47, 0x0a48, 0x0a4b,
    0x0a4c, 0x0a4d, 0x0a70, 0x0a70, 0x0a71, 0x0a81, 0x0a82, 0x0a83
    respectively. The document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00110m/AD_name00110m4.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00110m/AD_name00110m4_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00110m3_positive():
    """
    Attributes have names that end with the combining characters 0x0951,
    0x0952, 0x0954, 0x0962, 0x0962, 0x0963, 0x0981, 0x0982, 0x0983,
    0x09bc, 0x09be, 0x09bf, 0x09c0, 0x09c2, 0x09c4, 0x09c7, 0x09c7,
    0x09c8, 0x09cb, 0x09cc, 0x09cd, 0x09d7 (valid schema) Declare 22 local
    string attributes with the names that end with the following
    combining characters: 0x0951, 0x0952, 0x0954, 0x0962, 0x0962, 0x0963,
    0x0981, 0x0982, 0x0983, 0x09bc, 0x09be, 0x09bf, 0x09c0, 0x09c2,
    0x09c4, 0x09c7, 0x09c7, 0x09c8, 0x09cb, 0x09cc, 0x09cd, 0x09d7
    respectively. The document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00110m/AD_name00110m3.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00110m/AD_name00110m3_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00110m2_positive():
    """
    Attributes have names that end with the combining characters 0x0670,
    0x06d6, 0x06d9, 0x06dc, 0x06dd, 0x06de, 0x06df, 0x06e0, 0x06e2,
    0x06e4, 0x06e7, 0x06e7, 0x06e8, 0x06ea, 0x06eb, 0x06ed, 0x0901,
    0x0902, 0x0903, 0x093c, 0x093e, 0x0945, 0x094c, 0x094d (valid schema)
    Declare 24 local string attributes with the names that end with the
    following                               combining characters: 0x0670,
    0x06d6, 0x06d9, 0x06dc, 0x06dd, 0x06de, 0x06df, 0x06e0, 0x06e2,
    0x06e4, 0x06e7, 0x06e7, 0x06e8, 0x06ea, 0x06eb, 0x06ed, 0x0901,
    0x0902, 0x0903, 0x093c, 0x093e, 0x0945, 0x094c, 0x094d respectively.
    The document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00110m/AD_name00110m2.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00110m/AD_name00110m2_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00110m10_positive():
    """
    Attributes have names that end with the combining characters 0x20d0,
    0x20d6, 0x20dc, 0x20e1, 0x302a, 0x302c, 0x302f, 0x3099, 0x309a (valid
    schema) Declare 9 local string attributes with the names that end with
    the following                               combining characters:
    0x20d0, 0x20d6, 0x20dc, 0x20e1, 0x302a, 0x302c, 0x302f, 0x3099, 0x309a
    respectively. The document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00110m/AD_name00110m10.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00110m/AD_name00110m10_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00110m1_positive():
    """
    Attributes have names that end with the combining characters 0x0300,
    0x0322, 0x0344, 0x0360, 0x0360, 0x0361, 0x0483, 0x0484, 0x0486,
    0x0591, 0x0599, 0x05a1, 0x05a3, 0x05ae, 0x05b9, 0x05bb, 0x05bc,
    0x05bd, 0x05bf, 0x05c1, 0x05c1, 0x05c2, 0x05c4, 0x064b, 0x064e, 0x0652
    (valid schema) Declare 26 local string attributes with the names that
    end with the following                               combining
    characters: 0x0300, 0x0322, 0x0344, 0x0360, 0x0360, 0x0361, 0x0483,
    0x0484, 0x0486, 0x0591, 0x0599, 0x05a1, 0x05a3, 0x05ae, 0x05b9,
    0x05bb, 0x05bc, 0x05bd, 0x05bf, 0x05c1, 0x05c1, 0x05c2, 0x05c4,
    0x064b, 0x064e, 0x0652 respectively. The document set their values to
    0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00110m/AD_name00110m1.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00110m/AD_name00110m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00109m2_positive():
    """
    Attributes have names that end with the digit characters 0x0ce6,
    0x0cea, 0x0cef, 0x0d66, 0x0d6a, 0x0d6f, 0x0e50, 0x0e54, 0x0e59,
    0x0ed0, 0x0ed4, 0x0ed9, 0x0f20, 0x0f24, 0x0f29 (valid schema) Declare
    15 local string attributes with the names that end with the following
    digit characters: 0x0ce6, 0x0cea, 0x0cef, 0x0d66, 0x0d6a, 0x0d6f,
    0x0e50, 0x0e54, 0x0e59, 0x0ed0, 0x0ed4, 0x0ed9, 0x0f20, 0x0f24, 0x0f29
    respectively. The document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00109m/AD_name00109m2.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00109m/AD_name00109m2_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00109m1_positive():
    """
    Attributes have names that end with the digit characters 0x0030,
    0x0034, 0x0039, 0x0660, 0x0664, 0x0669, 0x06f0, 0x06f4, 0x06f9,
    0x0966, 0x096a, 0x096f, 0x09e6, 0x09ea, 0x09ef, 0x0a66, 0x0a6a,
    0x0a6f, 0x0ae6, 0x0aea, 0x0aef, 0x0b66, 0x0b6a, 0x0b6f, 0x0be7,
    0x0beb, 0x0bef, 0x0c66, 0x0c6a, 0x0c6f (valid schema) Declare 30 local
    string attributes with the names that end with the following
    digit characters: 0x0030, 0x0034, 0x0039, 0x0660, 0x0664, 0x0669,
    0x06f0, 0x06f4, 0x06f9, 0x0966, 0x096a, 0x096f, 0x09e6, 0x09ea,
    0x09ef, 0x0a66, 0x0a6a, 0x0a6f, 0x0ae6, 0x0aea, 0x0aef, 0x0b66,
    0x0b6a, 0x0b6f, 0x0be7, 0x0beb, 0x0bef, 0x0c66, 0x0c6a, 0x0c6f
    respectively. The document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00109m/AD_name00109m1.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00109m/AD_name00109m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00108m9_positive():
    """
    Attributes have names that end with the basic characters 0x0a8f,
    0x0a90, 0x0a91, 0x0a93, 0x0a9d, 0x0aa8, 0x0aaa, 0x0aad, 0x0ab0,
    0x0ab2, 0x0ab2, 0x0ab3, 0x0ab5, 0x0ab7, 0x0ab9, 0x0abd, 0x0ae0,
    0x0b05, 0x0b08, 0x0b0c, 0x0b0f, 0x0b0f, 0x0b10, 0x0b13, 0x0b1d, 0x0b28
    (valid schema) Declare 26 local string attributes with the names that
    end with the following                               basic characters:
    0x0a8f, 0x0a90, 0x0a91, 0x0a93, 0x0a9d, 0x0aa8, 0x0aaa, 0x0aad,
    0x0ab0, 0x0ab2, 0x0ab2, 0x0ab3, 0x0ab5, 0x0ab7, 0x0ab9, 0x0abd,
    0x0ae0, 0x0b05, 0x0b08, 0x0b0c, 0x0b0f, 0x0b0f, 0x0b10, 0x0b13,
    0x0b1d, 0x0b28 respectively. The document set their values to 0, 1 or
    2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m9.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m9_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00108m8_positive():
    """
    Attributes have names that end with the basic characters 0x0a13,
    0x0a1d, 0x0a28, 0x0a2a, 0x0a2d, 0x0a30, 0x0a32, 0x0a32, 0x0a33,
    0x0a35, 0x0a35, 0x0a36, 0x0a38, 0x0a38, 0x0a39, 0x0a59, 0x0a5a,
    0x0a5c, 0x0a5e, 0x0a72, 0x0a73, 0x0a74, 0x0a85, 0x0a88, 0x0a8b, 0x0a8d
    (valid schema) Declare 26 local string attributes with the names that
    end with the following                               basic characters:
    0x0a13, 0x0a1d, 0x0a28, 0x0a2a, 0x0a2d, 0x0a30, 0x0a32, 0x0a32,
    0x0a33, 0x0a35, 0x0a35, 0x0a36, 0x0a38, 0x0a38, 0x0a39, 0x0a59,
    0x0a5a, 0x0a5c, 0x0a5e, 0x0a72, 0x0a73, 0x0a74, 0x0a85, 0x0a88,
    0x0a8b, 0x0a8d respectively. The document set their values to 0, 1 or
    2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m8.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m8_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00108m7_positive():
    """
    Attributes have names that end with the basic characters 0x098f,
    0x098f, 0x0990, 0x0993, 0x099d, 0x09a8, 0x09aa, 0x09ad, 0x09b0,
    0x09b2, 0x09b6, 0x09b7, 0x09b9, 0x09dc, 0x09dc, 0x09dd, 0x09df,
    0x09e0, 0x09e1, 0x09f0, 0x09f0, 0x09f1, 0x0a05, 0x0a07, 0x0a0a,
    0x0a0f, 0x0a0f, 0x0a10 (valid schema) Declare 28 local string
    attributes with the names that end with the following
    basic characters: 0x098f, 0x098f, 0x0990, 0x0993, 0x099d, 0x09a8,
    0x09aa, 0x09ad, 0x09b0, 0x09b2, 0x09b6, 0x09b7, 0x09b9, 0x09dc,
    0x09dc, 0x09dd, 0x09df, 0x09e0, 0x09e1, 0x09f0, 0x09f0, 0x09f1,
    0x0a05, 0x0a07, 0x0a0a, 0x0a0f, 0x0a0f, 0x0a10 respectively. The
    document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m7.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m7_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00108m6_positive():
    """
    Attributes have names that end with the basic characters 0x0671,
    0x0694, 0x06b7, 0x06ba, 0x06bc, 0x06be, 0x06c0, 0x06c7, 0x06ce,
    0x06d0, 0x06d1, 0x06d3, 0x06d5, 0x06e5, 0x06e5, 0x06e6, 0x0905,
    0x091f, 0x0939, 0x093d, 0x0958, 0x095c, 0x0961, 0x0985, 0x0988, 0x098c
    (valid schema) Declare 26 local string attributes with the names that
    end with the following                               basic characters:
    0x0671, 0x0694, 0x06b7, 0x06ba, 0x06bc, 0x06be, 0x06c0, 0x06c7,
    0x06ce, 0x06d0, 0x06d1, 0x06d3, 0x06d5, 0x06e5, 0x06e5, 0x06e6,
    0x0905, 0x091f, 0x0939, 0x093d, 0x0958, 0x095c, 0x0961, 0x0985,
    0x0988, 0x098c respectively. The document set their values to 0, 1 or
    2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m6.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m6_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00108m5_positive():
    """
    Attributes have names that end with the basic characters 0x04d0,
    0x04dd, 0x04eb, 0x04ee, 0x04f1, 0x04f5, 0x04f8, 0x04f8, 0x04f9,
    0x0531, 0x0543, 0x0556, 0x0559, 0x0561, 0x0573, 0x0586, 0x05d0,
    0x05dd, 0x05ea, 0x05f0, 0x05f1, 0x05f2, 0x0621, 0x062d, 0x063a,
    0x0641, 0x0645, 0x064a (valid schema) Declare 28 local string
    attributes with the names that end with the following
    basic characters: 0x04d0, 0x04dd, 0x04eb, 0x04ee, 0x04f1, 0x04f5,
    0x04f8, 0x04f8, 0x04f9, 0x0531, 0x0543, 0x0556, 0x0559, 0x0561,
    0x0573, 0x0586, 0x05d0, 0x05dd, 0x05ea, 0x05f0, 0x05f1, 0x05f2,
    0x0621, 0x062d, 0x063a, 0x0641, 0x0645, 0x064a respectively. The
    document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m5.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m5_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00108m4_positive():
    """
    Attributes have names that end with the basic characters 0x03d0,
    0x03d3, 0x03d6, 0x03e2, 0x03e9, 0x03f1, 0x0401, 0x0406, 0x040c,
    0x040e, 0x042e, 0x044f, 0x0451, 0x0456, 0x045c, 0x045e, 0x046f,
    0x0481, 0x0490, 0x04a7, 0x04bf, 0x04c1, 0x04c2, 0x04c4, 0x04c7,
    0x04c7, 0x04c8, 0x04cb, 0x04cb, 0x04cc (valid schema) Declare 30 local
    string attributes with the names that end with the following
    basic characters: 0x03d0, 0x03d3, 0x03d6, 0x03e2, 0x03e9, 0x03f1,
    0x0401, 0x0406, 0x040c, 0x040e, 0x042e, 0x044f, 0x0451, 0x0456,
    0x045c, 0x045e, 0x046f, 0x0481, 0x0490, 0x04a7, 0x04bf, 0x04c1,
    0x04c2, 0x04c4, 0x04c7, 0x04c7, 0x04c8, 0x04cb, 0x04cb, 0x04cc
    respectively. The document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m4.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m4_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00108m3_positive():
    """
    Attributes have names that end with the basic characters 0x0276,
    0x027a, 0x027f, 0x0281, 0x0294, 0x02a8, 0x02bb, 0x02be, 0x02c1,
    0x0386, 0x0388, 0x0389, 0x038a, 0x038c, 0x038e, 0x038e, 0x038f,
    0x0391, 0x0399, 0x03a1, 0x03a3, 0x03a9, 0x03af, 0x03b1, 0x03bf, 0x03ce
    (valid schema) Declare 26 local string attributes with the names that
    end with the following                               basic characters:
    0x0276, 0x027a, 0x027f, 0x0281, 0x0294, 0x02a8, 0x02bb, 0x02be,
    0x02c1, 0x0386, 0x0388, 0x0389, 0x038a, 0x038c, 0x038e, 0x038e,
    0x038f, 0x0391, 0x0399, 0x03a1, 0x03a3, 0x03a9, 0x03af, 0x03b1,
    0x03bf, 0x03ce respectively. The document set their values to 0, 1 or
    2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m3.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m3_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00108m21_positive():
    """
    Attributes have names that end with the basic characters 0x1fe8,
    0x1fea, 0x1fec, 0x1ff8, 0x1ff9, 0x1ffb, 0x2180, 0x2181, 0x2182,
    0x3041, 0x306a, 0x3094, 0x30a1, 0x30cd, 0x30fa, 0x3105, 0x3118,
    0x312c, 0xac00, 0xc1d1, 0xd7a3 (valid schema) Declare 21 local string
    attributes with the names that end with the following
    basic characters: 0x1fe8, 0x1fea, 0x1fec, 0x1ff8, 0x1ff9, 0x1ffb,
    0x2180, 0x2181, 0x2182, 0x3041, 0x306a, 0x3094, 0x30a1, 0x30cd,
    0x30fa, 0x3105, 0x3118, 0x312c, 0xac00, 0xc1d1, 0xd7a3 respectively.
    The document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m21.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m21_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00108m20_positive():
    """
    Attributes have names that end with the basic characters 0x1f5b,
    0x1f5d, 0x1f5f, 0x1f6e, 0x1f7d, 0x1fb0, 0x1fb0, 0x1fb1, 0x1fb8,
    0x1fb9, 0x1fbb, 0x1fc8, 0x1fc9, 0x1fcb, 0x1fd0, 0x1fd0, 0x1fd1,
    0x1fd8, 0x1fd9, 0x1fdb, 0x1fe0, 0x1fe0, 0x1fe1, 0x1fe5 (valid schema)
    Declare 24 local string attributes with the names that end with the
    following                               basic characters: 0x1f5b,
    0x1f5d, 0x1f5f, 0x1f6e, 0x1f7d, 0x1fb0, 0x1fb0, 0x1fb1, 0x1fb8,
    0x1fb9, 0x1fbb, 0x1fc8, 0x1fc9, 0x1fcb, 0x1fd0, 0x1fd0, 0x1fd1,
    0x1fd8, 0x1fd9, 0x1fdb, 0x1fe0, 0x1fe0, 0x1fe1, 0x1fe5 respectively.
    The document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m20.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m20_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00108m2_positive():
    """
    Attributes have names that end with the basic characters 0x014a,
    0x0164, 0x017e, 0x0180, 0x018a, 0x0194, 0x0196, 0x019d, 0x01a5,
    0x01a7, 0x01a8, 0x01a9, 0x01ab, 0x01b4, 0x01bd, 0x01c0, 0x01c1,
    0x01c3, 0x01cd, 0x01de, 0x01ef, 0x01f4, 0x01f4, 0x01f5, 0x01fa,
    0x0208, 0x0217, 0x0250, 0x0262, 0x0274 (valid schema) Declare 30 local
    string attributes with the names that end with the following
    basic characters: 0x014a, 0x0164, 0x017e, 0x0180, 0x018a, 0x0194,
    0x0196, 0x019d, 0x01a5, 0x01a7, 0x01a8, 0x01a9, 0x01ab, 0x01b4,
    0x01bd, 0x01c0, 0x01c1, 0x01c3, 0x01cd, 0x01de, 0x01ef, 0x01f4,
    0x01f4, 0x01f5, 0x01fa, 0x0208, 0x0217, 0x0250, 0x0262, 0x0274
    respectively. The document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m2.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m2_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00108m19_positive():
    """
    Attributes have names that end with the basic characters 0x1ea0,
    0x1ecc, 0x1ef9, 0x1f00, 0x1f0a, 0x1f15, 0x1f18, 0x1f1a, 0x1f1d,
    0x1f20, 0x1f32, 0x1f45, 0x1f48, 0x1f4a, 0x1f4d, 0x1f51, 0x1f53,
    0x1f55, 0x1f57, 0x1f59 (valid schema) Declare 20 local string
    attributes with the names that end with the following
    basic characters: 0x1ea0, 0x1ecc, 0x1ef9, 0x1f00, 0x1f0a, 0x1f15,
    0x1f18, 0x1f1a, 0x1f1d, 0x1f20, 0x1f32, 0x1f45, 0x1f48, 0x1f4a,
    0x1f4d, 0x1f51, 0x1f53, 0x1f55, 0x1f57, 0x1f59 respectively. The
    document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m19.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m19_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00108m18_positive():
    """
    Attributes have names that end with the basic characters 0x11ab,
    0x11ae, 0x11ae, 0x11af, 0x11b7, 0x11b7, 0x11b8, 0x11ba, 0x11bc,
    0x11bf, 0x11c2, 0x11eb, 0x11f0, 0x11f9, 0x1e00, 0x1e4a, 0x1e95, 0x1e9b
    (valid schema) Declare 18 local string attributes with the names that
    end with the following                               basic characters:
    0x11ab, 0x11ae, 0x11ae, 0x11af, 0x11b7, 0x11b7, 0x11b8, 0x11ba,
    0x11bc, 0x11bf, 0x11c2, 0x11eb, 0x11f0, 0x11f9, 0x1e00, 0x1e4a,
    0x1e95, 0x1e9b respectively. The document set their values to 0, 1 or
    2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m18.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m18_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00108m17_positive():
    """
    Attributes have names that end with the basic characters 0x115f,
    0x1160, 0x1161, 0x1163, 0x1165, 0x1167, 0x1169, 0x116d, 0x116d,
    0x116e, 0x1172, 0x1172, 0x1173, 0x1175, 0x119e, 0x11a8 (valid schema)
    Declare 16 local string attributes with the names that end with the
    following                               basic characters: 0x115f,
    0x1160, 0x1161, 0x1163, 0x1165, 0x1167, 0x1169, 0x116d, 0x116d,
    0x116e, 0x1172, 0x1172, 0x1173, 0x1175, 0x119e, 0x11a8 respectively.
    The document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m17.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m17_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00108m16_positive():
    """
    Attributes have names that end with the basic characters 0x110b,
    0x110b, 0x110c, 0x110e, 0x1110, 0x1112, 0x113c, 0x113e, 0x1140,
    0x114c, 0x114e, 0x1150, 0x1154, 0x1154, 0x1155, 0x1159 (valid schema)
    Declare 16 local string attributes with the names that end with the
    following                               basic characters: 0x110b,
    0x110b, 0x110c, 0x110e, 0x1110, 0x1112, 0x113c, 0x113e, 0x1140,
    0x114c, 0x114e, 0x1150, 0x1154, 0x1154, 0x1155, 0x1159 respectively.
    The document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m16.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m16_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00108m15_positive():
    """
    Attributes have names that end with the basic characters 0x0eb0,
    0x0eb2, 0x0eb2, 0x0eb3, 0x0ebd, 0x0ec0, 0x0ec2, 0x0ec4, 0x0f40,
    0x0f43, 0x0f47, 0x0f49, 0x0f59, 0x0f69, 0x1100, 0x1102, 0x1102,
    0x1103, 0x1105, 0x1106, 0x1107, 0x1109 (valid schema) Declare 22 local
    string attributes with the names that end with the following
    basic characters: 0x0eb0, 0x0eb2, 0x0eb2, 0x0eb3, 0x0ebd, 0x0ec0,
    0x0ec2, 0x0ec4, 0x0f40, 0x0f43, 0x0f47, 0x0f49, 0x0f59, 0x0f69,
    0x1100, 0x1102, 0x1102, 0x1103, 0x1105, 0x1106, 0x1107, 0x1109
    respectively. The document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m15.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m15_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00108m14_positive():
    """
    Attributes have names that end with the basic characters 0x0e87,
    0x0e87, 0x0e88, 0x0e8a, 0x0e8d, 0x0e94, 0x0e95, 0x0e97, 0x0e99,
    0x0e9c, 0x0e9f, 0x0ea1, 0x0ea2, 0x0ea3, 0x0ea5, 0x0ea7, 0x0eaa,
    0x0eaa, 0x0eab, 0x0ead, 0x0ead, 0x0eae (valid schema) Declare 22 local
    string attributes with the names that end with the following
    basic characters: 0x0e87, 0x0e87, 0x0e88, 0x0e8a, 0x0e8d, 0x0e94,
    0x0e95, 0x0e97, 0x0e99, 0x0e9c, 0x0e9f, 0x0ea1, 0x0ea2, 0x0ea3,
    0x0ea5, 0x0ea7, 0x0eaa, 0x0eaa, 0x0eab, 0x0ead, 0x0ead, 0x0eae
    respectively. The document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m14.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m14_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00108m13_positive():
    """
    Attributes have names that end with the basic characters 0x0d0e,
    0x0d0f, 0x0d10, 0x0d12, 0x0d1d, 0x0d28, 0x0d2a, 0x0d31, 0x0d39,
    0x0d60, 0x0d60, 0x0d61, 0x0e01, 0x0e17, 0x0e2e, 0x0e30, 0x0e32,
    0x0e32, 0x0e33, 0x0e40, 0x0e42, 0x0e45, 0x0e81, 0x0e81, 0x0e82, 0x0e84
    (valid schema) Declare 26 local string attributes with the names that
    end with the following                               basic characters:
    0x0d0e, 0x0d0f, 0x0d10, 0x0d12, 0x0d1d, 0x0d28, 0x0d2a, 0x0d31,
    0x0d39, 0x0d60, 0x0d60, 0x0d61, 0x0e01, 0x0e17, 0x0e2e, 0x0e30,
    0x0e32, 0x0e32, 0x0e33, 0x0e40, 0x0e42, 0x0e45, 0x0e81, 0x0e81,
    0x0e82, 0x0e84 respectively. The document set their values to 0, 1 or
    2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m13.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m13_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00108m12_positive():
    """
    Attributes have names that end with the basic characters 0x0c35,
    0x0c37, 0x0c39, 0x0c60, 0x0c60, 0x0c61, 0x0c85, 0x0c88, 0x0c8c,
    0x0c8e, 0x0c8f, 0x0c90, 0x0c92, 0x0c9d, 0x0ca8, 0x0caa, 0x0cae,
    0x0cb3, 0x0cb5, 0x0cb7, 0x0cb9, 0x0cde, 0x0ce0, 0x0ce0, 0x0ce1,
    0x0d05, 0x0d08, 0x0d0c (valid schema) Declare 28 local string
    attributes with the names that end with the following
    basic characters: 0x0c35, 0x0c37, 0x0c39, 0x0c60, 0x0c60, 0x0c61,
    0x0c85, 0x0c88, 0x0c8c, 0x0c8e, 0x0c8f, 0x0c90, 0x0c92, 0x0c9d,
    0x0ca8, 0x0caa, 0x0cae, 0x0cb3, 0x0cb5, 0x0cb7, 0x0cb9, 0x0cde,
    0x0ce0, 0x0ce0, 0x0ce1, 0x0d05, 0x0d08, 0x0d0c respectively. The
    document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m12.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m12_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00108m11_positive():
    """
    Attributes have names that end with the basic characters 0x0b9c,
    0x0b9e, 0x0b9e, 0x0b9f, 0x0ba3, 0x0ba3, 0x0ba4, 0x0ba8, 0x0ba9,
    0x0baa, 0x0bae, 0x0bb1, 0x0bb5, 0x0bb7, 0x0bb8, 0x0bb9, 0x0c05,
    0x0c08, 0x0c0c, 0x0c0e, 0x0c0f, 0x0c10, 0x0c12, 0x0c1d, 0x0c28,
    0x0c2a, 0x0c2e, 0x0c33 (valid schema) Declare 28 local string
    attributes with the names that end with the following
    basic characters: 0x0b9c, 0x0b9e, 0x0b9e, 0x0b9f, 0x0ba3, 0x0ba3,
    0x0ba4, 0x0ba8, 0x0ba9, 0x0baa, 0x0bae, 0x0bb1, 0x0bb5, 0x0bb7,
    0x0bb8, 0x0bb9, 0x0c05, 0x0c08, 0x0c0c, 0x0c0e, 0x0c0f, 0x0c10,
    0x0c12, 0x0c1d, 0x0c28, 0x0c2a, 0x0c2e, 0x0c33 respectively. The
    document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m11.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m11_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00108m10_positive():
    """
    Attributes have names that end with the basic characters 0x0b2a,
    0x0b2d, 0x0b30, 0x0b32, 0x0b32, 0x0b33, 0x0b36, 0x0b37, 0x0b39,
    0x0b3d, 0x0b5c, 0x0b5c, 0x0b5d, 0x0b5f, 0x0b60, 0x0b61, 0x0b85,
    0x0b87, 0x0b8a, 0x0b8e, 0x0b8f, 0x0b90, 0x0b92, 0x0b93, 0x0b95,
    0x0b99, 0x0b99, 0x0b9a (valid schema) Declare 28 local string
    attributes with the names that end with the following
    basic characters: 0x0b2a, 0x0b2d, 0x0b30, 0x0b32, 0x0b32, 0x0b33,
    0x0b36, 0x0b37, 0x0b39, 0x0b3d, 0x0b5c, 0x0b5c, 0x0b5d, 0x0b5f,
    0x0b60, 0x0b61, 0x0b85, 0x0b87, 0x0b8a, 0x0b8e, 0x0b8f, 0x0b90,
    0x0b92, 0x0b93, 0x0b95, 0x0b99, 0x0b99, 0x0b9a respectively. The
    document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m10.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m10_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00108m1_positive():
    """
    Attributes have names that end with the basic characters 0x0041,
    0x004d, 0x005a, 0x0061, 0x0064, 0x0068, 0x006a, 0x0072, 0x007a,
    0x00c0, 0x00cb, 0x00d6, 0x00d8, 0x00db, 0x00de, 0x00e0, 0x00eb,
    0x00f6, 0x00f8, 0x00fb, 0x00ff, 0x0100, 0x0118, 0x0131, 0x0134,
    0x0139, 0x013e, 0x0141, 0x0144, 0x0148 (valid schema) Declare 30 local
    string attributes with the names that end with the following
    basic characters: 0x0041, 0x004d, 0x005a, 0x0061, 0x0064, 0x0068,
    0x006a, 0x0072, 0x007a, 0x00c0, 0x00cb, 0x00d6, 0x00d8, 0x00db,
    0x00de, 0x00e0, 0x00eb, 0x00f6, 0x00f8, 0x00fb, 0x00ff, 0x0100,
    0x0118, 0x0131, 0x0134, 0x0139, 0x013e, 0x0141, 0x0144, 0x0148
    respectively. The document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m1.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00108m/AD_name00108m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00107m1_positive():
    """
    Attributes have names that end with the ideographic characters 0x4e00,
    0x76d2, 0x9fa5, 0x3007, 0x3021, 0x3025, 0x3029 (valid schema) Declare
    7 local integer attributes with the names that end with the following
    ideographic characters: 0x4e00, 0x76d2, 0x9fa5, 0x3007, 0x3021,
    0x3025, 0x3029 respectively. The document set their values to 0, 1 or
    2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00107m/AD_name00107m1.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00107m/AD_name00107m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00106m1_positive():
    """
    Attributes have names that end with the underscore, dot and minus
    characters 0x005f, 0x002e, 0x002d (valid schema) Declare 3 local
    integer attributes with the names that end with the following
    underscore, dot and minus characters: 0x005f, 0x002e, 0x002d
    respectively. The document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00106m/AD_name00106m1.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00106m/AD_name00106m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00105m1_positive():
    """
    Attribute has name that begins with the underscore character 0x005f
    (valid schema) Declare one local integer attribute with the name that
    begins with the                               underscore character
    0x005f. The document set the attribute value to 0.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00105m/AD_name00105m1.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00105m/AD_name00105m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00104m9_positive():
    """
    Attributes have names that begin with the basic characters 0x0a8f,
    0x0a90, 0x0a91, 0x0a93, 0x0a9d, 0x0aa8, 0x0aaa, 0x0aad, 0x0ab0,
    0x0ab2, 0x0ab2, 0x0ab3, 0x0ab5, 0x0ab7, 0x0ab9, 0x0abd, 0x0ae0,
    0x0b05, 0x0b08, 0x0b0c, 0x0b0f, 0x0b0f, 0x0b10, 0x0b13, 0x0b1d, 0x0b28
    (valid schema) Declare 26 local integer attributes with the names that
    begin with the following                               basic
    characters: 0x0a8f, 0x0a90, 0x0a91, 0x0a93, 0x0a9d, 0x0aa8, 0x0aaa,
    0x0aad, 0x0ab0, 0x0ab2, 0x0ab2, 0x0ab3, 0x0ab5, 0x0ab7, 0x0ab9,
    0x0abd, 0x0ae0, 0x0b05, 0x0b08, 0x0b0c, 0x0b0f, 0x0b0f, 0x0b10,
    0x0b13, 0x0b1d, 0x0b28 respectively. The document set their values to
    0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m9.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m9_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00104m8_positive():
    """
    Attributes have names that begin with the basic characters 0x0a13,
    0x0a1d, 0x0a28, 0x0a2a, 0x0a2d, 0x0a30, 0x0a32, 0x0a32, 0x0a33,
    0x0a35, 0x0a35, 0x0a36, 0x0a38, 0x0a38, 0x0a39, 0x0a59, 0x0a5a,
    0x0a5c, 0x0a5e, 0x0a72, 0x0a73, 0x0a74, 0x0a85, 0x0a88, 0x0a8b, 0x0a8d
    (valid schema) Declare 26 local integer attributes with the names that
    begin with the following                               basic
    characters: 0x0a13, 0x0a1d, 0x0a28, 0x0a2a, 0x0a2d, 0x0a30, 0x0a32,
    0x0a32, 0x0a33, 0x0a35, 0x0a35, 0x0a36, 0x0a38, 0x0a38, 0x0a39,
    0x0a59, 0x0a5a, 0x0a5c, 0x0a5e, 0x0a72, 0x0a73, 0x0a74, 0x0a85,
    0x0a88, 0x0a8b, 0x0a8d respectively. The document set their values to
    0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m8.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m8_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00104m7_positive():
    """
    Attributes have names that begin with the basic characters 0x098f,
    0x098f, 0x0990, 0x0993, 0x099d, 0x09a8, 0x09aa, 0x09ad, 0x09b0,
    0x09b2, 0x09b6, 0x09b7, 0x09b9, 0x09dc, 0x09dc, 0x09dd, 0x09df,
    0x09e0, 0x09e1, 0x09f0, 0x09f0, 0x09f1, 0x0a05, 0x0a07, 0x0a0a,
    0x0a0f, 0x0a0f, 0x0a10 (valid schema) Declare 28 local integer
    attributes with the names that begin with the following
    basic characters: 0x098f, 0x098f, 0x0990, 0x0993, 0x099d, 0x09a8,
    0x09aa, 0x09ad, 0x09b0, 0x09b2, 0x09b6, 0x09b7, 0x09b9, 0x09dc,
    0x09dc, 0x09dd, 0x09df, 0x09e0, 0x09e1, 0x09f0, 0x09f0, 0x09f1,
    0x0a05, 0x0a07, 0x0a0a, 0x0a0f, 0x0a0f, 0x0a10 respectively. The
    document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m7.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m7_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00104m6_positive():
    """
    Attributes have names that begin with the basic characters 0x0671,
    0x0694, 0x06b7, 0x06ba, 0x06bc, 0x06be, 0x06c0, 0x06c7, 0x06ce,
    0x06d0, 0x06d1, 0x06d3, 0x06d5, 0x06e5, 0x06e5, 0x06e6, 0x0905,
    0x091f, 0x0939, 0x093d, 0x0958, 0x095c, 0x0961, 0x0985, 0x0988, 0x098c
    (valid schema) Declare 26 local integer attributes with the names that
    begin with the following                               basic
    characters: 0x0671, 0x0694, 0x06b7, 0x06ba, 0x06bc, 0x06be, 0x06c0,
    0x06c7, 0x06ce, 0x06d0, 0x06d1, 0x06d3, 0x06d5, 0x06e5, 0x06e5,
    0x06e6, 0x0905, 0x091f, 0x0939, 0x093d, 0x0958, 0x095c, 0x0961,
    0x0985, 0x0988, 0x098c respectively. The document set their values to
    0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m6.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m6_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00104m5_positive():
    """
    Attributes have names that begin with the basic characters 0x04d0,
    0x04dd, 0x04eb, 0x04ee, 0x04f1, 0x04f5, 0x04f8, 0x04f8, 0x04f9,
    0x0531, 0x0543, 0x0556, 0x0559, 0x0561, 0x0573, 0x0586, 0x05d0,
    0x05dd, 0x05ea, 0x05f0, 0x05f1, 0x05f2, 0x0621, 0x062d, 0x063a,
    0x0641, 0x0645, 0x064a (valid schema) Declare 28 local integer
    attributes with the names that begin with the following
    basic characters: 0x04d0, 0x04dd, 0x04eb, 0x04ee, 0x04f1, 0x04f5,
    0x04f8, 0x04f8, 0x04f9, 0x0531, 0x0543, 0x0556, 0x0559, 0x0561,
    0x0573, 0x0586, 0x05d0, 0x05dd, 0x05ea, 0x05f0, 0x05f1, 0x05f2,
    0x0621, 0x062d, 0x063a, 0x0641, 0x0645, 0x064a respectively. The
    document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m5.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m5_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00104m4_positive():
    """
    Attributes have names that begin with the basic characters 0x03d0,
    0x03d3, 0x03d6, 0x03e2, 0x03e9, 0x03f1, 0x0401, 0x0406, 0x040c,
    0x040e, 0x042e, 0x044f, 0x0451, 0x0456, 0x045c, 0x045e, 0x046f,
    0x0481, 0x0490, 0x04a7, 0x04bf, 0x04c1, 0x04c2, 0x04c4, 0x04c7,
    0x04c7, 0x04c8, 0x04cb, 0x04cb, 0x04cc (valid schema) Declare 30 local
    integer attributes with the names that begin with the following
    basic characters: 0x03d0, 0x03d3, 0x03d6, 0x03e2, 0x03e9, 0x03f1,
    0x0401, 0x0406, 0x040c, 0x040e, 0x042e, 0x044f, 0x0451, 0x0456,
    0x045c, 0x045e, 0x046f, 0x0481, 0x0490, 0x04a7, 0x04bf, 0x04c1,
    0x04c2, 0x04c4, 0x04c7, 0x04c7, 0x04c8, 0x04cb, 0x04cb, 0x04cc
    respectively. The document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m4.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m4_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00104m3_positive():
    """
    Attributes have names that begin with the basic characters 0x0276,
    0x027a, 0x027f, 0x0281, 0x0294, 0x02a8, 0x02bb, 0x02be, 0x02c1,
    0x0386, 0x0388, 0x0389, 0x038a, 0x038c, 0x038e, 0x038e, 0x038f,
    0x0391, 0x0399, 0x03a1, 0x03a3, 0x03a9, 0x03af, 0x03b1, 0x03bf, 0x03ce
    (valid schema) Declare 26 local integer attributes with the names that
    begin with the following                               basic
    characters: 0x0276, 0x027a, 0x027f, 0x0281, 0x0294, 0x02a8, 0x02bb,
    0x02be, 0x02c1, 0x0386, 0x0388, 0x0389, 0x038a, 0x038c, 0x038e,
    0x038e, 0x038f, 0x0391, 0x0399, 0x03a1, 0x03a3, 0x03a9, 0x03af,
    0x03b1, 0x03bf, 0x03ce respectively. The document set their values to
    0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m3.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m3_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00104m21_positive():
    """
    Attributes have names that begin with the basic characters 0x1fe8,
    0x1fea, 0x1fec, 0x1ff8, 0x1ff9, 0x1ffb, 0x2180, 0x2181, 0x2182,
    0x3041, 0x306a, 0x3094, 0x30a1, 0x30cd, 0x30fa, 0x3105, 0x3118,
    0x312c, 0xac00, 0xc1d1, 0xd7a3 (valid schema) Declare 21 local integer
    attributes with the names that begin with the following
    basic characters: 0x1fe8, 0x1fea, 0x1fec, 0x1ff8, 0x1ff9, 0x1ffb,
    0x2180, 0x2181, 0x2182, 0x3041, 0x306a, 0x3094, 0x30a1, 0x30cd,
    0x30fa, 0x3105, 0x3118, 0x312c, 0xac00, 0xc1d1, 0xd7a3 respectively.
    The document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m21.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m21_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00104m20_positive():
    """
    Attributes have names that begin with the basic characters 0x1f5b,
    0x1f5d, 0x1f5f, 0x1f6e, 0x1f7d, 0x1fb0, 0x1fb0, 0x1fb1, 0x1fb8,
    0x1fb9, 0x1fbb, 0x1fc8, 0x1fc9, 0x1fcb, 0x1fd0, 0x1fd0, 0x1fd1,
    0x1fd8, 0x1fd9, 0x1fdb, 0x1fe0, 0x1fe0, 0x1fe1, 0x1fe5 (valid schema)
    Declare 24 local integer attributes with the names that begin with the
    following                               basic characters: 0x1f5b,
    0x1f5d, 0x1f5f, 0x1f6e, 0x1f7d, 0x1fb0, 0x1fb0, 0x1fb1, 0x1fb8,
    0x1fb9, 0x1fbb, 0x1fc8, 0x1fc9, 0x1fcb, 0x1fd0, 0x1fd0, 0x1fd1,
    0x1fd8, 0x1fd9, 0x1fdb, 0x1fe0, 0x1fe0, 0x1fe1, 0x1fe5 respectively.
    The document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m20.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m20_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00104m2_positive():
    """
    Attributes have names that begin with the basic characters 0x014a,
    0x0164, 0x017e, 0x0180, 0x018a, 0x0194, 0x0196, 0x019d, 0x01a5,
    0x01a7, 0x01a8, 0x01a9, 0x01ab, 0x01b4, 0x01bd, 0x01c0, 0x01c1,
    0x01c3, 0x01cd, 0x01de, 0x01ef, 0x01f4, 0x01f4, 0x01f5, 0x01fa,
    0x0208, 0x0217, 0x0250, 0x0262, 0x0274 (valid schema) Declare 30 local
    integer attributes with the names that begin with the following
    basic characters: 0x014a, 0x0164, 0x017e, 0x0180, 0x018a, 0x0194,
    0x0196, 0x019d, 0x01a5, 0x01a7, 0x01a8, 0x01a9, 0x01ab, 0x01b4,
    0x01bd, 0x01c0, 0x01c1, 0x01c3, 0x01cd, 0x01de, 0x01ef, 0x01f4,
    0x01f4, 0x01f5, 0x01fa, 0x0208, 0x0217, 0x0250, 0x0262, 0x0274
    respectively. The document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m2.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m2_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00104m19_positive():
    """
    Attributes have names that begin with the basic characters 0x1ea0,
    0x1ecc, 0x1ef9, 0x1f00, 0x1f0a, 0x1f15, 0x1f18, 0x1f1a, 0x1f1d,
    0x1f20, 0x1f32, 0x1f45, 0x1f48, 0x1f4a, 0x1f4d, 0x1f51, 0x1f53,
    0x1f55, 0x1f57, 0x1f59 (valid schema) Declare 20 local integer
    attributes with the names that begin with the following
    basic characters: 0x1ea0, 0x1ecc, 0x1ef9, 0x1f00, 0x1f0a, 0x1f15,
    0x1f18, 0x1f1a, 0x1f1d, 0x1f20, 0x1f32, 0x1f45, 0x1f48, 0x1f4a,
    0x1f4d, 0x1f51, 0x1f53, 0x1f55, 0x1f57, 0x1f59 respectively. The
    document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m19.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m19_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00104m18_positive():
    """
    Attributes have names that begin with the basic characters 0x11ab,
    0x11ae, 0x11ae, 0x11af, 0x11b7, 0x11b7, 0x11b8, 0x11ba, 0x11bc,
    0x11bf, 0x11c2, 0x11eb, 0x11f0, 0x11f9, 0x1e00, 0x1e4a, 0x1e95, 0x1e9b
    (valid schema) Declare 18 local integer attributes with the names that
    begin with the following                               basic
    characters: 0x11ab, 0x11ae, 0x11ae, 0x11af, 0x11b7, 0x11b7, 0x11b8,
    0x11ba, 0x11bc, 0x11bf, 0x11c2, 0x11eb, 0x11f0, 0x11f9, 0x1e00,
    0x1e4a, 0x1e95, 0x1e9b respectively. The document set their values to
    0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m18.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m18_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00104m17_positive():
    """
    Attributes have names that begin with the basic characters 0x115f,
    0x1160, 0x1161, 0x1163, 0x1165, 0x1167, 0x1169, 0x116d, 0x116d,
    0x116e, 0x1172, 0x1172, 0x1173, 0x1175, 0x119e, 0x11a8 (valid schema)
    Declare 16 local integer attributes with the names that begin with the
    following                               basic characters: 0x115f,
    0x1160, 0x1161, 0x1163, 0x1165, 0x1167, 0x1169, 0x116d, 0x116d,
    0x116e, 0x1172, 0x1172, 0x1173, 0x1175, 0x119e, 0x11a8 respectively.
    The document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m17.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m17_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00104m16_positive():
    """
    Attributes have names that begin with the basic characters 0x110b,
    0x110b, 0x110c, 0x110e, 0x1110, 0x1112, 0x113c, 0x113e, 0x1140,
    0x114c, 0x114e, 0x1150, 0x1154, 0x1154, 0x1155, 0x1159 (valid schema)
    Declare 16 local integer attributes with the names that begin with the
    following                               basic characters: 0x110b,
    0x110b, 0x110c, 0x110e, 0x1110, 0x1112, 0x113c, 0x113e, 0x1140,
    0x114c, 0x114e, 0x1150, 0x1154, 0x1154, 0x1155, 0x1159 respectively.
    The document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m16.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m16_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00104m15_positive():
    """
    Attributes have names that begin with the basic characters 0x0eb0,
    0x0eb2, 0x0eb2, 0x0eb3, 0x0ebd, 0x0ec0, 0x0ec2, 0x0ec4, 0x0f40,
    0x0f43, 0x0f47, 0x0f49, 0x0f59, 0x0f69, 0x1100, 0x1102, 0x1102,
    0x1103, 0x1105, 0x1106, 0x1107, 0x1109 (valid schema) Declare 22 local
    integer attributes with the names that begin with the following
    basic characters: 0x0eb0, 0x0eb2, 0x0eb2, 0x0eb3, 0x0ebd, 0x0ec0,
    0x0ec2, 0x0ec4, 0x0f40, 0x0f43, 0x0f47, 0x0f49, 0x0f59, 0x0f69,
    0x1100, 0x1102, 0x1102, 0x1103, 0x1105, 0x1106, 0x1107, 0x1109
    respectively. The document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m15.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m15_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00104m14_positive():
    """
    Attributes have names that begin with the basic characters 0x0e87,
    0x0e87, 0x0e88, 0x0e8a, 0x0e8d, 0x0e94, 0x0e95, 0x0e97, 0x0e99,
    0x0e9c, 0x0e9f, 0x0ea1, 0x0ea2, 0x0ea3, 0x0ea5, 0x0ea7, 0x0eaa,
    0x0eaa, 0x0eab, 0x0ead, 0x0ead, 0x0eae (valid schema) Declare 22 local
    integer attributes with the names that begin with the following
    basic characters: 0x0e87, 0x0e87, 0x0e88, 0x0e8a, 0x0e8d, 0x0e94,
    0x0e95, 0x0e97, 0x0e99, 0x0e9c, 0x0e9f, 0x0ea1, 0x0ea2, 0x0ea3,
    0x0ea5, 0x0ea7, 0x0eaa, 0x0eaa, 0x0eab, 0x0ead, 0x0ead, 0x0eae
    respectively. The document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m14.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m14_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00104m13_positive():
    """
    Attributes have names that begin with the basic characters 0x0d0e,
    0x0d0f, 0x0d10, 0x0d12, 0x0d1d, 0x0d28, 0x0d2a, 0x0d31, 0x0d39,
    0x0d60, 0x0d60, 0x0d61, 0x0e01, 0x0e17, 0x0e2e, 0x0e30, 0x0e32,
    0x0e32, 0x0e33, 0x0e40, 0x0e42, 0x0e45, 0x0e81, 0x0e81, 0x0e82, 0x0e84
    (valid schema) Declare 26 local integer attributes with the names that
    begin with the following                               basic
    characters: 0x0d0e, 0x0d0f, 0x0d10, 0x0d12, 0x0d1d, 0x0d28, 0x0d2a,
    0x0d31, 0x0d39, 0x0d60, 0x0d60, 0x0d61, 0x0e01, 0x0e17, 0x0e2e,
    0x0e30, 0x0e32, 0x0e32, 0x0e33, 0x0e40, 0x0e42, 0x0e45, 0x0e81,
    0x0e81, 0x0e82, 0x0e84 respectively. The document set their values to
    0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m13.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m13_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00104m12_positive():
    """
    Attributes have names that begin with the basic characters 0x0c35,
    0x0c37, 0x0c39, 0x0c60, 0x0c60, 0x0c61, 0x0c85, 0x0c88, 0x0c8c,
    0x0c8e, 0x0c8f, 0x0c90, 0x0c92, 0x0c9d, 0x0ca8, 0x0caa, 0x0cae,
    0x0cb3, 0x0cb5, 0x0cb7, 0x0cb9, 0x0cde, 0x0ce0, 0x0ce0, 0x0ce1,
    0x0d05, 0x0d08, 0x0d0c (valid schema) Declare 28 local integer
    attributes with the names that begin with the following
    basic characters: 0x0c35, 0x0c37, 0x0c39, 0x0c60, 0x0c60, 0x0c61,
    0x0c85, 0x0c88, 0x0c8c, 0x0c8e, 0x0c8f, 0x0c90, 0x0c92, 0x0c9d,
    0x0ca8, 0x0caa, 0x0cae, 0x0cb3, 0x0cb5, 0x0cb7, 0x0cb9, 0x0cde,
    0x0ce0, 0x0ce0, 0x0ce1, 0x0d05, 0x0d08, 0x0d0c respectively. The
    document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m12.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m12_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00104m11_positive():
    """
    Attributes have names that begin with the basic characters 0x0b9c,
    0x0b9e, 0x0b9e, 0x0b9f, 0x0ba3, 0x0ba3, 0x0ba4, 0x0ba8, 0x0ba9,
    0x0baa, 0x0bae, 0x0bb1, 0x0bb5, 0x0bb7, 0x0bb8, 0x0bb9, 0x0c05,
    0x0c08, 0x0c0c, 0x0c0e, 0x0c0f, 0x0c10, 0x0c12, 0x0c1d, 0x0c28,
    0x0c2a, 0x0c2e, 0x0c33 (valid schema) Declare 28 local integer
    attributes with the names that begin with the following
    basic characters: 0x0b9c, 0x0b9e, 0x0b9e, 0x0b9f, 0x0ba3, 0x0ba3,
    0x0ba4, 0x0ba8, 0x0ba9, 0x0baa, 0x0bae, 0x0bb1, 0x0bb5, 0x0bb7,
    0x0bb8, 0x0bb9, 0x0c05, 0x0c08, 0x0c0c, 0x0c0e, 0x0c0f, 0x0c10,
    0x0c12, 0x0c1d, 0x0c28, 0x0c2a, 0x0c2e, 0x0c33 respectively. The
    document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m11.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m11_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00104m10_positive():
    """
    Attributes have names that begin with the basic characters 0x0b2a,
    0x0b2d, 0x0b30, 0x0b32, 0x0b32, 0x0b33, 0x0b36, 0x0b37, 0x0b39,
    0x0b3d, 0x0b5c, 0x0b5c, 0x0b5d, 0x0b5f, 0x0b60, 0x0b61, 0x0b85,
    0x0b87, 0x0b8a, 0x0b8e, 0x0b8f, 0x0b90, 0x0b92, 0x0b93, 0x0b95,
    0x0b99, 0x0b99, 0x0b9a (valid schema) Declare 28 local integer
    attributes with the names that begin with the following
    basic characters: 0x0b2a, 0x0b2d, 0x0b30, 0x0b32, 0x0b32, 0x0b33,
    0x0b36, 0x0b37, 0x0b39, 0x0b3d, 0x0b5c, 0x0b5c, 0x0b5d, 0x0b5f,
    0x0b60, 0x0b61, 0x0b85, 0x0b87, 0x0b8a, 0x0b8e, 0x0b8f, 0x0b90,
    0x0b92, 0x0b93, 0x0b95, 0x0b99, 0x0b99, 0x0b9a respectively. The
    document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m10.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m10_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00104m1_positive():
    """
    Attributes have names that begin with the basic characters 0x0041,
    0x004d, 0x005a, 0x0061, 0x0064, 0x0068, 0x006a, 0x0072, 0x007a,
    0x00c0, 0x00cb, 0x00d6, 0x00d8, 0x00db, 0x00de, 0x00e0, 0x00eb,
    0x00f6, 0x00f8, 0x00fb, 0x00ff, 0x0100, 0x0118, 0x0131, 0x0134,
    0x0139, 0x013e, 0x0141, 0x0144, 0x0148 (valid schema) Declare 30 local
    integer attributes with the names that begin with the following
    basic characters: 0x0041, 0x004d, 0x005a, 0x0061, 0x0064, 0x0068,
    0x006a, 0x0072, 0x007a, 0x00c0, 0x00cb, 0x00d6, 0x00d8, 0x00db,
    0x00de, 0x00e0, 0x00eb, 0x00f6, 0x00f8, 0x00fb, 0x00ff, 0x0100,
    0x0118, 0x0131, 0x0134, 0x0139, 0x013e, 0x0141, 0x0144, 0x0148
    respectively. The document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m1.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00104m/AD_name00104m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00103m2_positive():
    """
    Attributes have names that end with the extender characters 0x30fc,
    0x30fd, 0x30fe (valid schema) Declare 3 local string attributes with
    the names that end with the following
    extender characters: 0x30fc, 0x30fd, 0x30fe respectively. The document
    set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00103m/AD_name00103m2.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00103m/AD_name00103m2_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00103m1_positive():
    """
    Attributes have names that end with the extender characters 0x00b7,
    0x02d0, 0x02d1, 0x0387, 0x0640, 0x0e46, 0x0ec6, 0x3005, 0x3031,
    0x3033, 0x3035, 0x309d, 0x309d, 0x309e (valid schema) Declare 14 local
    string attributes with the names that end with the following
    extender characters: 0x00b7, 0x02d0, 0x02d1, 0x0387, 0x0640, 0x0e46,
    0x0ec6, 0x3005, 0x3031, 0x3033, 0x3035, 0x309d, 0x309d, 0x309e
    respectively. The document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00103m/AD_name00103m1.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00103m/AD_name00103m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00102m1_positive():
    """
    Attributes have names that begin with the ideographic characters
    0x4e00, 0x76d2, 0x9fa5, 0x3007, 0x3021, 0x3025, 0x3029 (valid schema)
    Declare 7 local integer attributes with the names that begin with the
    following                               ideographic characters:
    0x4e00, 0x76d2, 0x9fa5, 0x3007, 0x3021, 0x3025, 0x3029 respectively.
    The document set their values to 0, 1 or 2.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00102m/AD_name00102m1.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00102m/AD_name00102m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00101m4_positive():
    """
    Attribute in schema with "qualified" default form (valid schema)
    Attribute which has no explicitly declared form should be used in
    default for the schema form only.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00101m/AD_name00101m4.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00101m/AD_name00101m4_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00101m4_negative():
    """
    Attribute in schema with "qualified" default form (valid schema)
    Attribute which has no explicitly declared form should be used in
    default for the schema form only.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00101m/AD_name00101m4.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00101m/AD_name00101m4_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00101m3_positive():
    """
    Attribute explicitly declared "unqualified" while default form is
    "qualified" (valid schema) Attribute with explicitly declared form
    should be used in this form only.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00101m/AD_name00101m3.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00101m/AD_name00101m3_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00101m3_negative():
    """
    Attribute explicitly declared "unqualified" while default form is
    "qualified" (valid schema) Attribute with explicitly declared form
    should be used in this form only.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00101m/AD_name00101m3.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00101m/AD_name00101m3_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00101m2_positive():
    """
    Attribute in schema with "unqualified" default form (valid schema)
    Attribute which has no explicitly declared form should be used in
    default for the schema form only.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00101m/AD_name00101m2.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00101m/AD_name00101m2_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00101m2_negative():
    """
    Attribute in schema with "unqualified" default form (valid schema)
    Attribute which has no explicitly declared form should be used in
    default for the schema form only.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00101m/AD_name00101m2.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00101m/AD_name00101m2_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00101m1_positive():
    """
    Attribute explicitly declared "qualified" while default form is
    "unqualified" (valid schema) Attribute with explicitly declared form
    should be used in this form only.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00101m/AD_name00101m1.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00101m/AD_name00101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_name00101m1_negative():
    """
    Attribute explicitly declared "qualified" while default form is
    "unqualified" (valid schema) Attribute with explicitly declared form
    should be used in this form only.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_name/AD_name00101m/AD_name00101m1.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_name/AD_name00101m/AD_name00101m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_ad_annotation00101m2_positive():
    """
    machine-targeted annotation  for attribute declarations (valid schema)
    Annotations provide for human- and machine-targeted annotations of
    schema components.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_annotation/AD_annotation00101m/AD_annotation00101m2.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_annotation/AD_annotation00101m/AD_annotation00101m2_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_ad_annotation00101m1_positive():
    """
    human-targeted annotation  for attribute declarations (valid schema)
    Annotations provide for human- and machine-targeted annotations of
    schema components.
    """
    assert_bindings(
        schema="sunData/AttrDecl/AD_annotation/AD_annotation00101m/AD_annotation00101m1.xsd",
        is_valid=True,
        instance="sunData/AttrDecl/AD_annotation/AD_annotation00101m/AD_annotation00101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_au_valconstr00101m1_positive():
    """
    Attribute with fixed value is declared within element by reference
    (valid schema) Attribute declared with fixed value may not have
    another value in an instance document.
    """
    assert_bindings(
        schema="sunData/AttrUse/AU_valConstr/AU_valConstr00101m/AU_valConstr00101m1.xsd",
        is_valid=True,
        instance="sunData/AttrUse/AU_valConstr/AU_valConstr00101m/AU_valConstr00101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_au_valconstr00101m1_negative():
    """
    Attribute with fixed value is declared within element by reference
    (valid schema) Attribute declared with fixed value may not have
    another value in an instance document.
    """
    assert_bindings(
        schema="sunData/AttrUse/AU_valConstr/AU_valConstr00101m/AU_valConstr00101m1.xsd",
        is_valid=True,
        instance="sunData/AttrUse/AU_valConstr/AU_valConstr00101m/AU_valConstr00101m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_au_required00101m1_positive():
    """
    Attribute use is declared required.  (valid schema) Element whose
    attribute use is declared required should has the attribute specified.
    """
    assert_bindings(
        schema="sunData/AttrUse/AU_required/AU_required00101m/AU_required00101m1.xsd",
        is_valid=True,
        instance="sunData/AttrUse/AU_required/AU_required00101m/AU_required00101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_au_required00101m1_negative():
    """
    Attribute use is declared required.  (valid schema) Element whose
    attribute use is declared required should has the attribute specified.
    """
    assert_bindings(
        schema="sunData/AttrUse/AU_required/AU_required00101m/AU_required00101m1.xsd",
        is_valid=True,
        instance="sunData/AttrUse/AU_required/AU_required00101m/AU_required00101m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_au_attrdecl00101m1_p_positive():
    """
    Attribute declaration is resolved for attribute use. (valid schema)
    Attribute use should has proper ref value to be resolved to its
    declaration.
    """
    assert_bindings(
        schema="sunData/AttrUse/AU_attrDecl/AU_attrDecl00101m/AU_attrDecl00101m1_p.xsd",
        is_valid=True,
        instance="sunData/AttrUse/AU_attrDecl/AU_attrDecl00101m/AU_attrDecl00101m1.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_targetns00101m_target_ns00101m1_p():
    """
    Simple types are identified by their {name} and {target namespace}.
    (valid schema) Simple types are identified by their {name} and {target
    namespace}.
    """
    assert_bindings(
        schema="sunData/CType/targetNS/targetNS00101m/targetNS00101m.xsd",
        is_valid=True,
        instance="sunData/CType/targetNS/targetNS00101m/targetNS00101m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_targetns00101m_target_ns00101m1_n():
    """
    Simple types are identified by their {name} and {target namespace}.
    (valid schema) Simple types are identified by their {name} and {target
    namespace}.
    """
    assert_bindings(
        schema="sunData/CType/targetNS/targetNS00101m/targetNS00101m.xsd",
        is_valid=True,
        instance="sunData/CType/targetNS/targetNS00101m/targetNS00101m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_psubstitutions00104m_p_substitutions00104m1_p():
    """
    {prohibited substitutions} is #all (valid schema) {prohibited
    substitutions} determine whether an element declaration appearing
    in a *content model* is prevented from additionally *validating*
    element items with an xsi:type (p.2.6.1) attribute.
    """
    assert_bindings(
        schema="sunData/CType/pSubstitutions/pSubstitutions00104m/pSubstitutions00104m.xsd",
        is_valid=True,
        instance="sunData/CType/pSubstitutions/pSubstitutions00104m/pSubstitutions00104m1_p.xml",
        instance_is_valid=True,
        class_name="E",
        version="1.0",
    )


def test_psubstitutions00104m_p_substitutions00104m1_n():
    """
    {prohibited substitutions} is #all (valid schema) {prohibited
    substitutions} determine whether an element declaration appearing
    in a *content model* is prevented from additionally *validating*
    element items with an xsi:type (p.2.6.1) attribute.
    """
    assert_bindings(
        schema="sunData/CType/pSubstitutions/pSubstitutions00104m/pSubstitutions00104m.xsd",
        is_valid=True,
        instance="sunData/CType/pSubstitutions/pSubstitutions00104m/pSubstitutions00104m1_n.xml",
        instance_is_valid=False,
        class_name="E",
        version="1.0",
    )


def test_psubstitutions00104m_p_substitutions00104m2_p():
    """
    {prohibited substitutions} is #all (valid schema) {prohibited
    substitutions} determine whether an element declaration appearing
    in a *content model* is prevented from additionally *validating*
    element items with an xsi:type (p.2.6.1) attribute.
    """
    assert_bindings(
        schema="sunData/CType/pSubstitutions/pSubstitutions00104m/pSubstitutions00104m.xsd",
        is_valid=True,
        instance="sunData/CType/pSubstitutions/pSubstitutions00104m/pSubstitutions00104m2_p.xml",
        instance_is_valid=True,
        class_name="E",
        version="1.0",
    )


def test_psubstitutions00104m_p_substitutions00104m2_n():
    """
    {prohibited substitutions} is #all (valid schema) {prohibited
    substitutions} determine whether an element declaration appearing
    in a *content model* is prevented from additionally *validating*
    element items with an xsi:type (p.2.6.1) attribute.
    """
    assert_bindings(
        schema="sunData/CType/pSubstitutions/pSubstitutions00104m/pSubstitutions00104m.xsd",
        is_valid=True,
        instance="sunData/CType/pSubstitutions/pSubstitutions00104m/pSubstitutions00104m2_n.xml",
        instance_is_valid=False,
        class_name="E",
        version="1.0",
    )


@pytest.mark.xfail
def test_psubstitutions00103m_p_substitutions00103m1_p():
    """
    {prohibited substitutions} is restriction (valid schema) {prohibited
    substitutions} determine whether an element declaration appearing
    in a *content model* is prevented from additionally *validating*
    element items with an xsi:type (p.2.6.1) attribute.
    """
    assert_bindings(
        schema="sunData/CType/pSubstitutions/pSubstitutions00103m/pSubstitutions00103m.xsd",
        is_valid=True,
        instance="sunData/CType/pSubstitutions/pSubstitutions00103m/pSubstitutions00103m1_p.xml",
        instance_is_valid=True,
        class_name="E",
        version="1.0",
    )


def test_psubstitutions00103m_p_substitutions00103m1_n():
    """
    {prohibited substitutions} is restriction (valid schema) {prohibited
    substitutions} determine whether an element declaration appearing
    in a *content model* is prevented from additionally *validating*
    element items with an xsi:type (p.2.6.1) attribute.
    """
    assert_bindings(
        schema="sunData/CType/pSubstitutions/pSubstitutions00103m/pSubstitutions00103m.xsd",
        is_valid=True,
        instance="sunData/CType/pSubstitutions/pSubstitutions00103m/pSubstitutions00103m1_n.xml",
        instance_is_valid=False,
        class_name="E",
        version="1.0",
    )


def test_psubstitutions00103m_p_substitutions00103m2_p():
    """
    {prohibited substitutions} is restriction (valid schema) {prohibited
    substitutions} determine whether an element declaration appearing
    in a *content model* is prevented from additionally *validating*
    element items with an xsi:type (p.2.6.1) attribute.
    """
    assert_bindings(
        schema="sunData/CType/pSubstitutions/pSubstitutions00103m/pSubstitutions00103m.xsd",
        is_valid=True,
        instance="sunData/CType/pSubstitutions/pSubstitutions00103m/pSubstitutions00103m2_p.xml",
        instance_is_valid=True,
        class_name="E",
        version="1.0",
    )


def test_psubstitutions00103m_p_substitutions00103m2_n():
    """
    {prohibited substitutions} is restriction (valid schema) {prohibited
    substitutions} determine whether an element declaration appearing
    in a *content model* is prevented from additionally *validating*
    element items with an xsi:type (p.2.6.1) attribute.
    """
    assert_bindings(
        schema="sunData/CType/pSubstitutions/pSubstitutions00103m/pSubstitutions00103m.xsd",
        is_valid=True,
        instance="sunData/CType/pSubstitutions/pSubstitutions00103m/pSubstitutions00103m2_n.xml",
        instance_is_valid=False,
        class_name="E",
        version="1.0",
    )


def test_psubstitutions00102m_p_substitutions00102m1_p():
    """
    {prohibited substitutions} is extension (valid schema) {prohibited
    substitutions} determine whether an element declaration appearing
    in a *content model* is prevented from additionally *validating*
    element items with an xsi:type (p.2.6.1) attribute.
    """
    assert_bindings(
        schema="sunData/CType/pSubstitutions/pSubstitutions00102m/pSubstitutions00102m.xsd",
        is_valid=True,
        instance="sunData/CType/pSubstitutions/pSubstitutions00102m/pSubstitutions00102m1_p.xml",
        instance_is_valid=True,
        class_name="E",
        version="1.0",
    )


def test_psubstitutions00102m_p_substitutions00102m1_n():
    """
    {prohibited substitutions} is extension (valid schema) {prohibited
    substitutions} determine whether an element declaration appearing
    in a *content model* is prevented from additionally *validating*
    element items with an xsi:type (p.2.6.1) attribute.
    """
    assert_bindings(
        schema="sunData/CType/pSubstitutions/pSubstitutions00102m/pSubstitutions00102m.xsd",
        is_valid=True,
        instance="sunData/CType/pSubstitutions/pSubstitutions00102m/pSubstitutions00102m1_n.xml",
        instance_is_valid=False,
        class_name="E",
        version="1.0",
    )


def test_psubstitutions00102m_p_substitutions00102m2_p():
    """
    {prohibited substitutions} is extension (valid schema) {prohibited
    substitutions} determine whether an element declaration appearing
    in a *content model* is prevented from additionally *validating*
    element items with an xsi:type (p.2.6.1) attribute.
    """
    assert_bindings(
        schema="sunData/CType/pSubstitutions/pSubstitutions00102m/pSubstitutions00102m.xsd",
        is_valid=True,
        instance="sunData/CType/pSubstitutions/pSubstitutions00102m/pSubstitutions00102m2_p.xml",
        instance_is_valid=True,
        class_name="E",
        version="1.0",
    )


def test_psubstitutions00102m_p_substitutions00102m2_n():
    """
    {prohibited substitutions} is extension (valid schema) {prohibited
    substitutions} determine whether an element declaration appearing
    in a *content model* is prevented from additionally *validating*
    element items with an xsi:type (p.2.6.1) attribute.
    """
    assert_bindings(
        schema="sunData/CType/pSubstitutions/pSubstitutions00102m/pSubstitutions00102m.xsd",
        is_valid=True,
        instance="sunData/CType/pSubstitutions/pSubstitutions00102m/pSubstitutions00102m2_n.xml",
        instance_is_valid=False,
        class_name="E",
        version="1.0",
    )


@pytest.mark.xfail
def test_psubstitutions00101m_p_substitutions00101m1_p():
    """
    {prohibited substitutions} is empty (valid schema) If {prohibited
    substitutions} is empty, then all substitutions are allowed.
    """
    assert_bindings(
        schema="sunData/CType/pSubstitutions/pSubstitutions00101m/pSubstitutions00101m.xsd",
        is_valid=True,
        instance="sunData/CType/pSubstitutions/pSubstitutions00101m/pSubstitutions00101m1_p.xml",
        instance_is_valid=True,
        class_name="E",
        version="1.0",
    )


def test_psubstitutions00101m_p_substitutions00101m1_n():
    """
    {prohibited substitutions} is empty (valid schema) If {prohibited
    substitutions} is empty, then all substitutions are allowed.
    """
    assert_bindings(
        schema="sunData/CType/pSubstitutions/pSubstitutions00101m/pSubstitutions00101m.xsd",
        is_valid=True,
        instance="sunData/CType/pSubstitutions/pSubstitutions00101m/pSubstitutions00101m1_n.xml",
        instance_is_valid=False,
        class_name="E",
        version="1.0",
    )


def test_psubstitutions00101m_p_substitutions00101m2_p():
    """
    {prohibited substitutions} is empty (valid schema) If {prohibited
    substitutions} is empty, then all substitutions are allowed.
    """
    assert_bindings(
        schema="sunData/CType/pSubstitutions/pSubstitutions00101m/pSubstitutions00101m.xsd",
        is_valid=True,
        instance="sunData/CType/pSubstitutions/pSubstitutions00101m/pSubstitutions00101m2_p.xml",
        instance_is_valid=True,
        class_name="E",
        version="1.0",
    )


def test_psubstitutions00101m_p_substitutions00101m2_n():
    """
    {prohibited substitutions} is empty (valid schema) If {prohibited
    substitutions} is empty, then all substitutions are allowed.
    """
    assert_bindings(
        schema="sunData/CType/pSubstitutions/pSubstitutions00101m/pSubstitutions00101m.xsd",
        is_valid=True,
        instance="sunData/CType/pSubstitutions/pSubstitutions00101m/pSubstitutions00101m2_n.xml",
        instance_is_valid=False,
        class_name="E",
        version="1.0",
    )


def test_name00101m_name00101m1_p():
    """
    Simple types are identified by their {name} and {target namespace}.
    (valid schema) Simple types are identified by their {name} and {target
    namespace}.
    """
    assert_bindings(
        schema="sunData/CType/name/name00101m/name00101m.xsd",
        is_valid=True,
        instance="sunData/CType/name/name00101m/name00101m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_name00101m_name00101m1_n():
    """
    Simple types are identified by their {name} and {target namespace}.
    (valid schema) Simple types are identified by their {name} and {target
    namespace}.
    """
    assert_bindings(
        schema="sunData/CType/name/name00101m/name00101m.xsd",
        is_valid=True,
        instance="sunData/CType/name/name00101m/name00101m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_final00101m3_positive():
    """
    the value is restriction (valid schema) The explicit values extension,
    and restriction prevent further derivations by
    extension and restriction respectively. If all values are specified,
    then                                the complex type is said to be
    final, because no further derivations are possible.
    """
    assert_bindings(
        schema="sunData/CType/final/final00101m/final00101m3.xsd",
        is_valid=True,
        instance="sunData/CType/final/final00101m/final00101m3_p.xml",
        instance_is_valid=True,
        class_name="B",
        version="1.0",
    )


def test_final00101m3_negative():
    """
    the value is restriction (valid schema) The explicit values extension,
    and restriction prevent further derivations by
    extension and restriction respectively. If all values are specified,
    then                                the complex type is said to be
    final, because no further derivations are possible.
    """
    assert_bindings(
        schema="sunData/CType/final/final00101m/final00101m3.xsd",
        is_valid=True,
        instance="sunData/CType/final/final00101m/final00101m3_n.xml",
        instance_is_valid=False,
        class_name="B",
        version="1.0",
    )


def test_derivationmethod00102m2_positive():
    """
    extension of the type int by adding the attribute 't' of the type int
    (valid schema) Schema Component Constraint: Derivation Valid
    (Extension).                              If the {base type
    definition} is a simple type definition.
    """
    assert_bindings(
        schema="sunData/CType/derivationMethod/derivationMethod00102m/derivationMethod00102m2.xsd",
        is_valid=True,
        instance="sunData/CType/derivationMethod/derivationMethod00102m/derivationMethod00102m2_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_derivationmethod00102m2_negative():
    """
    extension of the type int by adding the attribute 't' of the type int
    (valid schema) Schema Component Constraint: Derivation Valid
    (Extension).                              If the {base type
    definition} is a simple type definition.
    """
    assert_bindings(
        schema="sunData/CType/derivationMethod/derivationMethod00102m/derivationMethod00102m2.xsd",
        is_valid=True,
        instance="sunData/CType/derivationMethod/derivationMethod00102m/derivationMethod00102m2_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_derivationmethod00102m1_positive():
    """
    extension of the type int (valid schema) Schema Component Constraint:
    Derivation Valid (Extension).                              If the
    {base type definition} is a simple type definition.
    """
    assert_bindings(
        schema="sunData/CType/derivationMethod/derivationMethod00102m/derivationMethod00102m1.xsd",
        is_valid=True,
        instance="sunData/CType/derivationMethod/derivationMethod00102m/derivationMethod00102m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_derivationmethod00102m1_negative():
    """
    extension of the type int (valid schema) Schema Component Constraint:
    Derivation Valid (Extension).                              If the
    {base type definition} is a simple type definition.
    """
    assert_bindings(
        schema="sunData/CType/derivationMethod/derivationMethod00102m/derivationMethod00102m1.xsd",
        is_valid=True,
        instance="sunData/CType/derivationMethod/derivationMethod00102m/derivationMethod00102m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_derivationmethod00101m2_positive():
    """
    items: 1.1, 1.2, 1.3, 1.4.2.1, 1.4.2.2.1 (valid schema) Schema
    Component Constraint: Derivation Valid (Extension).
    The {base type definition} is a complex type definition.
    """
    assert_bindings(
        schema="sunData/CType/derivationMethod/derivationMethod00101m/derivationMethod00101m2.xsd",
        is_valid=True,
        instance="sunData/CType/derivationMethod/derivationMethod00101m/derivationMethod00101m2_p.xml",
        instance_is_valid=True,
        class_name="B",
        version="1.0",
    )


def test_derivationmethod00101m2_negative():
    """
    items: 1.1, 1.2, 1.3, 1.4.2.1, 1.4.2.2.1 (valid schema) Schema
    Component Constraint: Derivation Valid (Extension).
    The {base type definition} is a complex type definition.
    """
    assert_bindings(
        schema="sunData/CType/derivationMethod/derivationMethod00101m/derivationMethod00101m2.xsd",
        is_valid=True,
        instance="sunData/CType/derivationMethod/derivationMethod00101m/derivationMethod00101m2_n.xml",
        instance_is_valid=False,
        class_name="B",
        version="1.0",
    )


def test_derivationmethod00101m1_positive():
    """
    items: 1.1, 1.2, 1.3, 1.4.1 (valid schema) Schema Component
    Constraint: Derivation Valid (Extension).
    The {base type definition} is a complex type definition.
    """
    assert_bindings(
        schema="sunData/CType/derivationMethod/derivationMethod00101m/derivationMethod00101m1.xsd",
        is_valid=True,
        instance="sunData/CType/derivationMethod/derivationMethod00101m/derivationMethod00101m1_p.xml",
        instance_is_valid=True,
        class_name="B",
        version="1.0",
    )


def test_derivationmethod00101m1_negative():
    """
    items: 1.1, 1.2, 1.3, 1.4.1 (valid schema) Schema Component
    Constraint: Derivation Valid (Extension).
    The {base type definition} is a complex type definition.
    """
    assert_bindings(
        schema="sunData/CType/derivationMethod/derivationMethod00101m/derivationMethod00101m1.xsd",
        is_valid=True,
        instance="sunData/CType/derivationMethod/derivationMethod00101m/derivationMethod00101m1_n.xml",
        instance_is_valid=False,
        class_name="B",
        version="1.0",
    )


def test_contenttype00401m_content_type00401m1_p():
    """
    An mixed content type (valid schema) A mixed {content type}
    *validates* elements whose element [children]
    (i.e. specifically ignoring other [children] such as character
    information                                items) conform to the
    supplied *content model*.
    """
    assert_bindings(
        schema="sunData/CType/contentType/contentType00401m/contentType00401m.xsd",
        is_valid=True,
        instance="sunData/CType/contentType/contentType00401m/contentType00401m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_contenttype00401m_content_type00401m1_n():
    """
    An mixed content type (valid schema) A mixed {content type}
    *validates* elements whose element [children]
    (i.e. specifically ignoring other [children] such as character
    information                                items) conform to the
    supplied *content model*.
    """
    assert_bindings(
        schema="sunData/CType/contentType/contentType00401m/contentType00401m.xsd",
        is_valid=True,
        instance="sunData/CType/contentType/contentType00401m/contentType00401m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_contenttype00301m_content_type00301m1_p():
    """
    An element-only content type (valid schema) An element-only {content
    type} *validates* elements with [children] that
    conform to the supplied *content model*.
    """
    assert_bindings(
        schema="sunData/CType/contentType/contentType00301m/contentType00301m.xsd",
        is_valid=True,
        instance="sunData/CType/contentType/contentType00301m/contentType00301m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_contenttype00301m_content_type00301m1_n():
    """
    An element-only content type (valid schema) An element-only {content
    type} *validates* elements with [children] that
    conform to the supplied *content model*.
    """
    assert_bindings(
        schema="sunData/CType/contentType/contentType00301m/contentType00301m.xsd",
        is_valid=True,
        instance="sunData/CType/contentType/contentType00301m/contentType00301m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_contenttype00201m_content_type00201m1_p():
    """
    A simple content type (valid schema) A {content type} which is a
    Simple Type Definition (2.2.1.2) *validates*
    elements with character-only [children].
    """
    assert_bindings(
        schema="sunData/CType/contentType/contentType00201m/contentType00201m.xsd",
        is_valid=True,
        instance="sunData/CType/contentType/contentType00201m/contentType00201m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_contenttype00201m_content_type00201m1_n():
    """
    A simple content type (valid schema) A {content type} which is a
    Simple Type Definition (2.2.1.2) *validates*
    elements with character-only [children].
    """
    assert_bindings(
        schema="sunData/CType/contentType/contentType00201m/contentType00201m.xsd",
        is_valid=True,
        instance="sunData/CType/contentType/contentType00201m/contentType00201m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_contenttype00101m_content_type00101m1_p():
    """
    An empty content type (valid schema) A {content type} with the
    distinguished value empty *validates* elements with
    no character or element information item [children].
    """
    assert_bindings(
        schema="sunData/CType/contentType/contentType00101m/contentType00101m.xsd",
        is_valid=True,
        instance="sunData/CType/contentType/contentType00101m/contentType00101m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_contenttype00101m_content_type00101m1_n():
    """
    An empty content type (valid schema) A {content type} with the
    distinguished value empty *validates* elements with
    no character or element information item [children].
    """
    assert_bindings(
        schema="sunData/CType/contentType/contentType00101m/contentType00101m.xsd",
        is_valid=True,
        instance="sunData/CType/contentType/contentType00101m/contentType00101m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_basetd00101m4_positive():
    """
    restriction of complex content (valid schema) The type definition
    resolved to by the actual value of the base [attribute].
    """
    assert_bindings(
        schema="sunData/CType/baseTD/baseTD00101m/baseTD00101m4.xsd",
        is_valid=True,
        instance="sunData/CType/baseTD/baseTD00101m/baseTD00101m4_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_basetd00101m4_negative():
    """
    restriction of complex content (valid schema) The type definition
    resolved to by the actual value of the base [attribute].
    """
    assert_bindings(
        schema="sunData/CType/baseTD/baseTD00101m/baseTD00101m4.xsd",
        is_valid=True,
        instance="sunData/CType/baseTD/baseTD00101m/baseTD00101m4_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_basetd00101m3_positive():
    """
    extention of complex content (valid schema) The type definition
    resolved to by the actual value of the base [attribute].
    """
    assert_bindings(
        schema="sunData/CType/baseTD/baseTD00101m/baseTD00101m3.xsd",
        is_valid=True,
        instance="sunData/CType/baseTD/baseTD00101m/baseTD00101m3_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_basetd00101m3_negative():
    """
    extention of complex content (valid schema) The type definition
    resolved to by the actual value of the base [attribute].
    """
    assert_bindings(
        schema="sunData/CType/baseTD/baseTD00101m/baseTD00101m3.xsd",
        is_valid=True,
        instance="sunData/CType/baseTD/baseTD00101m/baseTD00101m3_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_basetd00101m2_positive():
    """
    extention of simple content (valid schema) The type definition
    resolved to by the actual value of the base [attribute].
    """
    assert_bindings(
        schema="sunData/CType/baseTD/baseTD00101m/baseTD00101m2.xsd",
        is_valid=True,
        instance="sunData/CType/baseTD/baseTD00101m/baseTD00101m2_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_basetd00101m2_negative():
    """
    extention of simple content (valid schema) The type definition
    resolved to by the actual value of the base [attribute].
    """
    assert_bindings(
        schema="sunData/CType/baseTD/baseTD00101m/baseTD00101m2.xsd",
        is_valid=True,
        instance="sunData/CType/baseTD/baseTD00101m/baseTD00101m2_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_basetd00101m1_positive():
    """
    restriction of simple content (valid schema) The type definition
    resolved to by the actual value of the base [attribute].
    """
    assert_bindings(
        schema="sunData/CType/baseTD/baseTD00101m/baseTD00101m1.xsd",
        is_valid=True,
        instance="sunData/CType/baseTD/baseTD00101m/baseTD00101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_basetd00101m1_negative():
    """
    restriction of simple content (valid schema) The type definition
    resolved to by the actual value of the base [attribute].
    """
    assert_bindings(
        schema="sunData/CType/baseTD/baseTD00101m/baseTD00101m1.xsd",
        is_valid=True,
        instance="sunData/CType/baseTD/baseTD00101m/baseTD00101m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_attributeuses00101m1_positive():
    """
    <attribute> [children] (valid schema) The set of attribute uses
    corresponding to the <attribute> [children].
    """
    assert_bindings(
        schema="sunData/CType/attributeUses/attributeUses00101m/attributeUses00101m1.xsd",
        is_valid=True,
        instance="sunData/CType/attributeUses/attributeUses00101m/attributeUses00101m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_attributeuses00101m1_negative():
    """
    <attribute> [children] (valid schema) The set of attribute uses
    corresponding to the <attribute> [children].
    """
    assert_bindings(
        schema="sunData/CType/attributeUses/attributeUses00101m/attributeUses00101m1.xsd",
        is_valid=True,
        instance="sunData/CType/attributeUses/attributeUses00101m/attributeUses00101m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_attrwildcard00101m1_positive():
    """
    type definition with any attributes (valid schema) any: [attributes]
    can include attributes with any qualified or unqualified name.
    """
    assert_bindings(
        schema="sunData/CType/attrWildcard/attrWildcard00101m/attrWildcard00101m1.xsd",
        is_valid=True,
        instance="sunData/CType/attrWildcard/attrWildcard00101m/attrWildcard00101m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_annotation00101m2_positive():
    """
    machine-targeted annotation  for complex type definition (valid
    schema) Annotations provide for human- and machine-targeted
    annotations of schema components.
    """
    assert_bindings(
        schema="sunData/CType/annotation/annotation00101m/annotation00101m2.xsd",
        is_valid=True,
        instance="sunData/CType/annotation/annotation00101m/annotation00101m2_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_annotation00101m1_positive_355():
    """
    human-targeted annotation  for complex type definition (valid schema)
    Annotations provide for human- and machine-targeted annotations of
    schema components.
    """
    assert_bindings(
        schema="sunData/CType/annotation/annotation00101m/annotation00101m1.xsd",
        is_valid=True,
        instance="sunData/CType/annotation/annotation00101m/annotation00101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_abstract00101m2_negative():
    """
    declaration of element of abstract type (valid schema) Complex types
    for which {abstract} is true must not be used as the
    {type definition} for the *validation* of element information items.
    """
    assert_bindings(
        schema="sunData/CType/abstract/abstract00101m/abstract00101m2.xsd",
        is_valid=True,
        instance="sunData/CType/abstract/abstract00101m/abstract00101m2_n.xml",
        instance_is_valid=False,
        class_name="B",
        version="1.0",
    )


def test_abstract00101m1_positive():
    """
    abstract type extension (valid schema) Abstract complex types can be
    used as {base type definition}s.
    """
    assert_bindings(
        schema="sunData/CType/abstract/abstract00101m/abstract00101m1.xsd",
        is_valid=True,
        instance="sunData/CType/abstract/abstract00101m/abstract00101m1_p.xml",
        instance_is_valid=True,
        class_name="B",
        version="1.0",
    )


def test_abstract00101m1_negative():
    """
    abstract type extension (valid schema) Abstract complex types can be
    used as {base type definition}s.
    """
    assert_bindings(
        schema="sunData/CType/abstract/abstract00101m/abstract00101m1.xsd",
        is_valid=True,
        instance="sunData/CType/abstract/abstract00101m/abstract00101m1_n.xml",
        instance_is_valid=False,
        class_name="B",
        version="1.0",
    )


def test_valueconstraint01101m4_negative():
    """
    default value is invalid for the local type definition (valid schema)
    For a string to be a valid default with respect to a type definition,
    if the type definition is a simple type definition, then the
    string must be valid with respect to that definition.
    In the test the default value is invalid for the local type
    definition.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint01101m/valueConstraint01101m4.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint01101m/valueConstraint01101m4_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint01101m3_positive():
    """
    default value is valid (valid schema) For a string to be a valid
    default with respect to a type definition,
    if the type definition is a simple type definition, then the
    string must be valid with respect to that definition.
    In the test the default value is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint01101m/valueConstraint01101m3.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint01101m/valueConstraint01101m3_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint01101m2_negative():
    """
    fixed value is invalid for the local type definition (valid schema)
    For a string to be a valid default with respect to a type definition,
    if the type definition is a simple type definition, then the
    string must be valid with respect to that definition.
    In the test the fixed value is invalid for the local type definition.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint01101m/valueConstraint01101m2.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint01101m/valueConstraint01101m2_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint01101m1_positive():
    """
    fixed value is valid (valid schema) For a string to be a valid default
    with respect to a type definition,                              if the
    type definition is a simple type definition, then the
    string must be valid with respect to that definition.
    In the test the fixed value is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint01101m/valueConstraint01101m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint01101m/valueConstraint01101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint01001m8_positive():
    """
    default value constraint with string type (valid schema) Declare an
    element. Specify the following: type="xsd:string" default="alpha".
    Check that the declaration is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint01001m/valueConstraint01001m8.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint01001m/valueConstraint01001m8_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint01001m7_positive():
    """
    fixed value constraint with string type (valid schema) Declare an
    element. Specify the following: type="xsd:string" fixed="alpha".
    Check that the declaration is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint01001m/valueConstraint01001m7.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint01001m/valueConstraint01001m7_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint01001m4_positive():
    """
    no value constraint with a type derived from ID (valid schema) Declare
    an element. Specify the following: type="derivedFromID".
    Check that the declaration is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint01001m/valueConstraint01001m4.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint01001m/valueConstraint01001m4_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint01001m1_positive():
    """
    no value constraint with ID type (valid schema) Declare an element.
    Specify the following: type="xsd:ID".
    Check that the declaration is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint01001m/valueConstraint01001m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint01001m/valueConstraint01001m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint00901m1_positive():
    """
    value of simple content type must match the fixed value (valid schema)
    If the {content type} of the actual type definition is a simple type
    definition, then the actual value of the item must match the
    canonical lexical representation of the {value constraint} value
    In the test, the value of the item does not match the
    specified fixed value.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00901m/valueConstraint00901m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00901m/valueConstraint00901m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint00901m1_negative():
    """
    value of simple content type must match the fixed value (valid schema)
    If the {content type} of the actual type definition is a simple type
    definition, then the actual value of the item must match the
    canonical lexical representation of the {value constraint} value
    In the test, the value of the item does not match the
    specified fixed value.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00901m/valueConstraint00901m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00901m/valueConstraint00901m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint00801m1_positive():
    """
    value of mixed content type must match the fixed value (valid schema)
    If the {content type} of the actual type definition is mixed,
    then the initial value of the item must match the canonical lexical
    representation of the {value constraint} value.
    In the test, the value of the item does not match the
    specified fixed value.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00801m/valueConstraint00801m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00801m/valueConstraint00801m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint00801m1_negative():
    """
    value of mixed content type must match the fixed value (valid schema)
    If the {content type} of the actual type definition is mixed,
    then the initial value of the item must match the canonical lexical
    representation of the {value constraint} value.
    In the test, the value of the item does not match the
    specified fixed value.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00801m/valueConstraint00801m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00801m/valueConstraint00801m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint00701m1_positive():
    """
    fixed value constraint forbids element children (valid schema) If
    there is a fixed {value constraint}                               the
    element information item must have no element information item
    children.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00701m/valueConstraint00701m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00701m/valueConstraint00701m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint00701m1_negative():
    """
    fixed value constraint forbids element children (valid schema) If
    there is a fixed {value constraint}                               the
    element information item must have no element information item
    children.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00701m/valueConstraint00701m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00701m/valueConstraint00701m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint00601m7_positive():
    """
    default value a derived type is valid (valid schema) The element
    information item with the lexical
    representation of the {value constraint} value used as
    its normalized value must be valid with respect to the
    actual type definition .                               In the test the
    default value a derived type is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00601m/valueConstraint00601m7.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00601m/valueConstraint00601m7_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint00601m5_positive():
    """
    fixed value of a derived type is valid (valid schema) The element
    information item with the lexical
    representation of the {value constraint} value used as
    its normalized value must be valid with respect to the
    actual type definition .                               In the test the
    fixed value of a derived type is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00601m/valueConstraint00601m5.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00601m/valueConstraint00601m5_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint00601m3_positive():
    """
    default value of built-in type is valid (valid schema) The element
    information item with the lexical
    representation of the {value constraint} value used as
    its normalized value must be valid with respect to the
    actual type definition .                               In the test the
    default value of built-in type is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00601m/valueConstraint00601m3.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00601m/valueConstraint00601m3_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint00601m1_positive():
    """
    fixed value of built-in type is valid (valid schema) The element
    information item with the lexical
    representation of the {value constraint} value used as
    its normalized value must be valid with respect to the
    actual type definition .                               In the test the
    fixed value of built-in type is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00601m/valueConstraint00601m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00601m/valueConstraint00601m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint00501m6_negative():
    """
    default value is invalid for the local type definition (valid schema)
    If the declaration has a {value constraint},
    the item has neither element nor character [children] and
    xsi:nil  is not specified, the  actual type definition
    is a  local type definition  then the lexical
    representation of the {value constraint} value
    must be a valid default for the  actual type definition .
    In the test the default value is invalid for the local type
    definition.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00501m/valueConstraint00501m6.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00501m/valueConstraint00501m6_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_valueconstraint00501m5_positive():
    """
    default value is valid (valid schema) If the declaration has a {value
    constraint},                               the item has neither
    element nor character [children] and
    xsi:nil  is not specified, the  actual type definition
    is a  local type definition  then the lexical
    representation of the {value constraint} value
    must be a valid default for the  actual type definition .
    In the test the default value is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00501m/valueConstraint00501m5.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00501m/valueConstraint00501m5_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_valueconstraint00501m4_positive():
    """
    default value is valid (valid schema) If the declaration has a {value
    constraint},                               the item has neither
    element nor character [children] and
    xsi:nil  is not specified, the  actual type definition
    is a  local type definition  then the lexical
    representation of the {value constraint} value
    must be a valid default for the  actual type definition .
    In the test the default value is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00501m/valueConstraint00501m4.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00501m/valueConstraint00501m4_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint00501m3_negative():
    """
    fixed value is invalid for the local type definition (valid schema) If
    the declaration has a {value constraint},
    the item has neither element nor character [children] and
    xsi:nil  is not specified, the  actual type definition
    is a  local type definition  then the lexical
    representation of the {value constraint} value
    must be a valid default for the  actual type definition .
    In the test the fixed value is invalid for the local type definition.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00501m/valueConstraint00501m3.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00501m/valueConstraint00501m3_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_valueconstraint00501m2_positive():
    """
    fixed value is valid (valid schema) If the declaration has a {value
    constraint},                               the item has neither
    element nor character [children] and
    xsi:nil  is not specified, the  actual type definition
    is a  local type definition  then the lexical
    representation of the {value constraint} value
    must be a valid default for the  actual type definition .
    In the test the fixed value is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00501m/valueConstraint00501m2.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00501m/valueConstraint00501m2_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_valueconstraint00501m1_positive():
    """
    fixed value is valid (valid schema) If the declaration has a {value
    constraint},                               the item has neither
    element nor character [children] and
    xsi:nil  is not specified, the  actual type definition
    is a  local type definition  then the lexical
    representation of the {value constraint} value
    must be a valid default for the  actual type definition .
    In the test the fixed value is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00501m/valueConstraint00501m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00501m/valueConstraint00501m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint00402m9_positive():
    """
    fixed value is set for anySimpleType (valid schema) Declare an
    element. Set type="xsd:anySimpleType" fixed="alpha".
    Check that the schema is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00402m/valueConstraint00402m9.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00402m/valueConstraint00402m9_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint00402m7_positive():
    """
    fixed value is set for a simple type (valid schema) Declare an
    element. Set type="answer" fixed="true".
    The content type of type  answer  allows only "true".
    Check that the schema is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00402m/valueConstraint00402m7.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00402m/valueConstraint00402m7_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint00402m5_positive():
    """
    fixed value is set for a complex type with a simple content (valid
    schema) Declare an element. Set type="answer" fixed="true".
    The content type of type  answer  is  boolean .
    Check that the schema is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00402m/valueConstraint00402m5.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00402m/valueConstraint00402m5_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint00402m4_positive():
    """
    fixed value is set for anyType (valid schema) Declare an element. Set
    type="xsd:anyType" fixed="alpha".
    Check that the schema is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00402m/valueConstraint00402m4.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00402m/valueConstraint00402m4_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint00402m3_positive():
    """
    fixed value is set for ur-type (valid schema) Declare an element. Set
    fixed="alpha".
    Check that the schema is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00402m/valueConstraint00402m3.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00402m/valueConstraint00402m3_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint00402m1_positive():
    """
    fixed value is set for type boolean (valid schema) Declare an element.
    Set type="xsd:boolean" fixed="true".
    Check that the schema is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00402m/valueConstraint00402m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00402m/valueConstraint00402m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint00401m9_positive():
    """
    default value is set for anySimpleType (valid schema) Declare an
    element. Set type="xsd:anySimpleType" default="alpha".
    Check that the schema is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00401m/valueConstraint00401m9.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00401m/valueConstraint00401m9_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint00401m7_positive():
    """
    default value is set for a simple type (valid schema) Declare an
    element. Set type="answer" default="true".
    The content type of type  answer  allows only "true".
    Check that the schema is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00401m/valueConstraint00401m7.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00401m/valueConstraint00401m7_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint00401m5_positive():
    """
    default value is set for a complex type with a simple content (valid
    schema) Declare an element. Set type="answer" default="true".
    The content type of type  answer  is  boolean .
    Check that the schema is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00401m/valueConstraint00401m5.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00401m/valueConstraint00401m5_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint00401m4_positive():
    """
    default value is set for anyType (valid schema) Declare an element.
    Set type="xsd:anyType" default="alpha".
    Check that the schema is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00401m/valueConstraint00401m4.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00401m/valueConstraint00401m4_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint00401m3_positive():
    """
    default value is set for ur-type (valid schema) Declare an element.
    Set default="alpha".
    Check that the schema is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00401m/valueConstraint00401m3.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00401m/valueConstraint00401m3_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint00401m1_positive():
    """
    default value is set for type boolean (valid schema) Declare an
    element. Set type="xsd:boolean" default="true".
    Check that the schema is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00401m/valueConstraint00401m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00401m/valueConstraint00401m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint00301m2_positive():
    """
    only fixed is present (valid schema) Define an element. Set fixed="0".
    Check that the schema is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00301m/valueConstraint00301m2.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00301m/valueConstraint00301m2_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint00301m1_positive():
    """
    only default is present (valid schema) Define an element. Set
    default="0".                              Check that the schema is
    valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00301m/valueConstraint00301m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00301m/valueConstraint00301m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_valueconstraint00201m_value_constraint00201m1_p():
    """
    Validation of the fixed value attribute. (valid schema) Define an
    elements with fixed value defined. Ensure
    that the value may be empty or, otherwise, must be
    equal to that defined.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00201m/valueConstraint00201m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00201m/valueConstraint00201m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint00201m_value_constraint00201m1_n():
    """
    Validation of the fixed value attribute. (valid schema) Define an
    elements with fixed value defined. Ensure
    that the value may be empty or, otherwise, must be
    equal to that defined.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00201m/valueConstraint00201m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00201m/valueConstraint00201m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_valueconstraint00101m1_positive():
    """
    Validation of the default value attribute (positive case). (valid
    schema) Define an elements with default value defined. Ensure
    that the value is validated.
    """
    assert_bindings(
        schema="sunData/ElemDecl/valueConstraint/valueConstraint00101m/valueConstraint00101m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/valueConstraint/valueConstraint00101m/valueConstraint00101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_typedef01501m1_positive():
    """
    value must be valid with respect to the type definition (valid schema)
    If the type definition is a complex type definition,
    then the element information item must be valid with respect to the
    type definition.                              Negative case uses
    invalid value.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef01501m/typeDef01501m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef01501m/typeDef01501m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_typedef01501m1_negative():
    """
    value must be valid with respect to the type definition (valid schema)
    If the type definition is a complex type definition,
    then the element information item must be valid with respect to the
    type definition.                              Negative case uses
    invalid value.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef01501m/typeDef01501m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef01501m/typeDef01501m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_typedef01401m1_positive():
    """
    normalized value must be valid with respect to the type definition
    (valid schema) If the element information item of a simple type is not
    nil, then                              its normalized value must be
    valid with respect to the type definition.
    Negative case uses invalid value.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef01401m/typeDef01401m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef01401m/typeDef01401m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_typedef01401m1_negative():
    """
    normalized value must be valid with respect to the type definition
    (valid schema) If the element information item of a simple type is not
    nil, then                              its normalized value must be
    valid with respect to the type definition.
    Negative case uses invalid value.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef01401m/typeDef01401m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef01401m/typeDef01401m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_typedef01301m1_positive():
    """
    trying to use element children in the element of a simple type (valid
    schema) The element information item must have no element information
    item children                              if it has a simple type.
    Negative case uses an element of type  xsd:anySimpleType
    with children elements.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef01301m/typeDef01301m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef01301m/typeDef01301m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_typedef01301m1_negative():
    """
    trying to use element children in the element of a simple type (valid
    schema) The element information item must have no element information
    item children                              if it has a simple type.
    Negative case uses an element of type  xsd:anySimpleType
    with children elements.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef01301m/typeDef01301m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef01301m/typeDef01301m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_typedef01202m1_positive():
    """
    element of a simple type has noNamespaceSchemaLocation, type and nil
    attributes (valid schema) If the type definition is a simple type
    definition, then                              the element information
    item's attributes must be empty,
    excepting those whose namespace name is identical to
    http://www.w3.org/2001/XMLSchema-instance and whose local name
    is one of  type ,  nil ,  schemaLocation  or
    noNamespaceSchemaLocation .                               The negative
    case uses an element with an extra attribute.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef01202m/typeDef01202m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef01202m/typeDef01202m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_typedef01202m1_negative():
    """
    element of a simple type has noNamespaceSchemaLocation, type and nil
    attributes (valid schema) If the type definition is a simple type
    definition, then                              the element information
    item's attributes must be empty,
    excepting those whose namespace name is identical to
    http://www.w3.org/2001/XMLSchema-instance and whose local name
    is one of  type ,  nil ,  schemaLocation  or
    noNamespaceSchemaLocation .                               The negative
    case uses an element with an extra attribute.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef01202m/typeDef01202m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef01202m/typeDef01202m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_typedef01201m1_positive():
    """
    element of a simple type has schemaLocation, type and nil attributes
    (valid schema) If the type definition is a simple type definition,
    then                              the element information item's
    attributes must be empty,                               excepting
    those whose namespace name is identical to
    http://www.w3.org/2001/XMLSchema-instance and whose local name
    is one of  type ,  nil ,  schemaLocation  or
    noNamespaceSchemaLocation .                               The negative
    case uses an element with an extra attribute.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef01201m/typeDef01201m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef01201m/typeDef01201m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_typedef01201m1_negative():
    """
    element of a simple type has schemaLocation, type and nil attributes
    (valid schema) If the type definition is a simple type definition,
    then                              the element information item's
    attributes must be empty,                               excepting
    those whose namespace name is identical to
    http://www.w3.org/2001/XMLSchema-instance and whose local name
    is one of  type ,  nil ,  schemaLocation  or
    noNamespaceSchemaLocation .                               The negative
    case uses an element with an extra attribute.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef01201m/typeDef01201m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef01201m/typeDef01201m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_typedef01101m1_positive():
    """
    actual type must not be abstract (valid schema) For an element to be
    locally valid its type must not be  abstract .
    Negative case uses local type definition with a type that is  abstract
    .
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef01101m/typeDef01101m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef01101m/typeDef01101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_typedef01101m1_negative():
    """
    actual type must not be abstract (valid schema) For an element to be
    locally valid its type must not be  abstract .
    Negative case uses local type definition with a type that is  abstract
    .
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef01101m/typeDef01101m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef01101m/typeDef01101m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_typedef00901m1_positive():
    """
    the element information item must be valid with respect to the actual
    type definition (valid schema) The element information item must be
    valid with respect to                               the actual type
    definition. In the test the actual type definition is
    a local type definition.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef00901m/typeDef00901m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef00901m/typeDef00901m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_typedef00901m1_negative():
    """
    the element information item must be valid with respect to the actual
    type definition (valid schema) The element information item must be
    valid with respect to                               the actual type
    definition. In the test the actual type definition is
    a local type definition.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef00901m/typeDef00901m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef00901m/typeDef00901m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_typedef00802m2_negative():
    """
    local type is 'dissalowed' (valid schema) If it is a simple type
    definition, the  local type definition
    must be validly derived from the {type definition} given the
    {disallowed substitutions}.                                 In the
    test the local type is 'dissalowed'.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef00802m/typeDef00802m2.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef00802m/typeDef00802m2_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_typedef00802m1_positive():
    """
    local type definition is validly derived from simpleType (valid
    schema) If it is a simple type definition, the  local type definition
    must be validly derived from the {type definition} given the
    {disallowed substitutions}.                                 In the
    test the local type definition is validly derived from simpleType.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef00802m/typeDef00802m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef00802m/typeDef00802m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_typedef00802m1_negative():
    """
    local type definition is validly derived from simpleType (valid
    schema) If it is a simple type definition, the  local type definition
    must be validly derived from the {type definition} given the
    {disallowed substitutions}.                                 In the
    test the local type definition is validly derived from simpleType.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef00802m/typeDef00802m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef00802m/typeDef00802m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_typedef00801m3_negative():
    """
    local type is 'dissalowed' (valid schema) If it is a complex type
    definition, the  local type definition
    must be validly derived from the {type definition} given the union of
    the {disallowed substitutions} and the {type definition}'s
    {prohibited substitutions}.                                 In the
    test the local type is 'dissalowed'.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef00801m/typeDef00801m3.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef00801m/typeDef00801m3_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_typedef00801m2_negative():
    """
    local type is 'prohibited' (valid schema) If it is a complex type
    definition, the  local type definition
    must be validly derived from the {type definition} given the union of
    the {disallowed substitutions} and the {type definition}'s
    {prohibited substitutions}.                                 In the
    test the local type is 'prohibited'.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef00801m/typeDef00801m2.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef00801m/typeDef00801m2_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_typedef00801m1_positive():
    """
    local type definition is validly derived from complexType (valid
    schema) If it is a complex type definition, the  local type definition
    must be validly derived from the {type definition} given the union of
    the {disallowed substitutions} and the {type definition}'s
    {prohibited substitutions}.                                 In the
    test the local type definition is validly derived from complexType.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef00801m/typeDef00801m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef00801m/typeDef00801m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_typedef00701m_type_def00701m1_p():
    """
    local name and namespace name of the xsi:type must resolve to a type
    definition (valid schema) Use  xsi:type  attribute
    set to a value that has both local and namespace names.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef00701m/typeDef00701m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef00701m/typeDef00701m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_typedef00701m_type_def00701m1_n():
    """
    local name and namespace name of the xsi:type must resolve to a type
    definition (valid schema) Use  xsi:type  attribute
    set to a value that has both local and namespace names.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef00701m/typeDef00701m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef00701m/typeDef00701m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_typedef00601m_type_def00601m1_p():
    """
    a normalized value of the type attribute must be valid (valid schema)
    Specify a type of an element by means of the  type  attribute
    set to a value that is not normalized.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef00601m/typeDef00601m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef00601m/typeDef00601m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_typedef00502m1_positive():
    """
    simpleType and type are mutually exclusive (valid schema) Declare an
    element using  type .                               Declare another
    element with a  simpleType .                               Ensure the
    schema is valid
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef00502m/typeDef00502m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef00502m/typeDef00502m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_typedef00501m1_positive():
    """
    complexType and type are mutually exclusive (valid schema) Declare an
    element using  type .                               Declare another
    element with a  complexType .                               Ensure the
    schema is valid
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef00501m/typeDef00501m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef00501m/typeDef00501m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_typedef00403m_type_def00403m1_p():
    """
    Various setting of the {type definition} property. (valid schema) For
    complete declarations, top-level or local, the  type  attribute
    is used when the declaration can use a built-in or pre-declared type
    definition. Otherwise an anonymous <simpleType> or <complexType> is
    provided inline
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef00403m/typeDef00403m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef00403m/typeDef00403m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_typedef00402m_type_def00402m1_p():
    """
    Eelements within complexType. (valid schema) Eelements within
    complexType  produce either particles which contain
    global element declarations (if there's a ref attribute) or
    local declarations otherwise.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef00402m/typeDef00402m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef00402m/typeDef00402m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_typedef00402m_type_def00402m1_n():
    """
    Eelements within complexType. (valid schema) Eelements within
    complexType  produce either particles which contain
    global element declarations (if there's a ref attribute) or
    local declarations otherwise.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef00402m/typeDef00402m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef00402m/typeDef00402m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_typedef00401m_type_def00401m1_p():
    """
    Eelements within group. (valid schema) Eelements within  group
    produce either particles which contain
    global element declarations (if there's a ref attribute) or
    local declarations otherwise.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef00401m/typeDef00401m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef00401m/typeDef00401m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_typedef00401m_type_def00401m1_n():
    """
    Eelements within group. (valid schema) Eelements within  group
    produce either particles which contain
    global element declarations (if there's a ref attribute) or
    local declarations otherwise.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef00401m/typeDef00401m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef00401m/typeDef00401m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_typedef00301m_type_def00301m1_p():
    """
    The {type definition} property is specified by reference. (valid
    schema) Declare a global element with a certain type.
    Declare another element. Specify the type by reference.
    Ensure the value is validated according to the type.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef00301m/typeDef00301m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef00301m/typeDef00301m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_typedef00301m_type_def00301m1_n():
    """
    The {type definition} property is specified by reference. (valid
    schema) Declare a global element with a certain type.
    Declare another element. Specify the type by reference.
    Ensure the value is validated according to the type.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef00301m/typeDef00301m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef00301m/typeDef00301m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_typedef00205m_type_def00205m1_p():
    """
    default type is used to define {type definition} property. (valid
    schema) Define an element with the default type. Define another
    element of type anyType. Ensure the anyType element may
    substitute for the default type one.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef00205m/typeDef00205m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef00205m/typeDef00205m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_typedef00204m_type_def00204m1_p():
    """
    type attribute is used to define {type definition} property. (valid
    schema) Define an element by means of the substitutionGroup
    attribute. Ensure the value is validated according to
    the type.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef00204m/typeDef00204m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef00204m/typeDef00204m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_typedef00204m_type_def00204m1_n():
    """
    type attribute is used to define {type definition} property. (valid
    schema) Define an element by means of the substitutionGroup
    attribute. Ensure the value is validated according to
    the type.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef00204m/typeDef00204m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef00204m/typeDef00204m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_typedef00203m_type_def00203m1_p():
    """
    type attribute is used to define {type definition} property. (valid
    schema) Define an element by means of type attribute. Ensure
    the value is validated according to the type.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef00203m/typeDef00203m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef00203m/typeDef00203m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_typedef00203m_type_def00203m1_n():
    """
    type attribute is used to define {type definition} property. (valid
    schema) Define an element by means of type attribute. Ensure
    the value is validated according to the type.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef00203m/typeDef00203m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef00203m/typeDef00203m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_typedef00202m_type_def00202m1_p():
    """
    complexType is used to define {type definition} property. (valid
    schema) Define an element with a complexType. Ensure
    the value is validated according to the type.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef00202m/typeDef00202m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef00202m/typeDef00202m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_typedef00202m_type_def00202m1_n():
    """
    complexType is used to define {type definition} property. (valid
    schema) Define an element with a complexType. Ensure
    the value is validated according to the type.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef00202m/typeDef00202m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef00202m/typeDef00202m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_typedef00201m_type_def00201m1_p():
    """
    simpleType is used to define {type definition} property. (valid
    schema) Define an element with a simpleType. Ensure
    the value is validated according to the type.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef00201m/typeDef00201m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef00201m/typeDef00201m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_typedef00201m_type_def00201m1_n():
    """
    simpleType is used to define {type definition} property. (valid
    schema) Define an element with a simpleType. Ensure
    the value is validated according to the type.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef00201m/typeDef00201m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef00201m/typeDef00201m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_typedef00101m_type_def00101m1_p():
    """
    General check of the {type definition} property. (valid schema) Define
    an element with a certain type. Ensure
    the value is validated according to the type.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef00101m/typeDef00101m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef00101m/typeDef00101m1_p.xml",
        instance_is_valid=True,
        class_name="Answer",
        version="1.0",
    )


def test_typedef00101m_type_def00101m1_n():
    """
    General check of the {type definition} property. (valid schema) Define
    an element with a certain type. Ensure
    the value is validated according to the type.
    """
    assert_bindings(
        schema="sunData/ElemDecl/typeDef/typeDef00101m/typeDef00101m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/typeDef/typeDef00101m/typeDef00101m1_n.xml",
        instance_is_valid=False,
        class_name="Answer",
        version="1.0",
    )


@pytest.mark.xfail
def test_term00101m_term00101m1_p():
    """
    The (top-level) element declaration resolved to by the actual value of
    the ref attribute. (valid schema) Declare one local element that
    refers to a global one.                               Check that the
    element is validated according to the type of
    the referred element.
    """
    assert_bindings(
        schema="sunData/ElemDecl/term/term00101m/term00101m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/term/term00101m/term00101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_term00101m_term00101m1_n():
    """
    The (top-level) element declaration resolved to by the actual value of
    the ref attribute. (valid schema) Declare one local element that
    refers to a global one.                               Check that the
    element is validated according to the type of
    the referred element.
    """
    assert_bindings(
        schema="sunData/ElemDecl/term/term00101m/term00101m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/term/term00101m/term00101m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_targetns00402m_target_ns00402m1_p():
    """
    Global elements must be qualified. (valid schema) If {target
    namespace} is  absent , element information items
    validated by a top-level declaration must be unqualified.
    """
    assert_bindings(
        schema="sunData/ElemDecl/targetNS/targetNS00402m/targetNS00402m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/targetNS/targetNS00402m/targetNS00402m1_p.xml",
        instance_is_valid=True,
        class_name="Global",
        version="1.0",
    )


def test_targetns00402m_target_ns00402m1_n():
    """
    Global elements must be qualified. (valid schema) If {target
    namespace} is  absent , element information items
    validated by a top-level declaration must be unqualified.
    """
    assert_bindings(
        schema="sunData/ElemDecl/targetNS/targetNS00402m/targetNS00402m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/targetNS/targetNS00402m/targetNS00402m1_n.xml",
        instance_is_valid=False,
        class_name="Global",
        version="1.0",
    )


def test_targetns00401m_target_ns00401m1_p():
    """
    Global elements must be qualified. (valid schema) Element information
    items validated by a top-level declaration must
    be qualified with the {target namespace} of that declaration.
    """
    assert_bindings(
        schema="sunData/ElemDecl/targetNS/targetNS00401m/targetNS00401m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/targetNS/targetNS00401m/targetNS00401m1_p.xml",
        instance_is_valid=True,
        class_name="Global",
        version="1.0",
    )


def test_targetns00401m_target_ns00401m1_n():
    """
    Global elements must be qualified. (valid schema) Element information
    items validated by a top-level declaration must
    be qualified with the {target namespace} of that declaration.
    """
    assert_bindings(
        schema="sunData/ElemDecl/targetNS/targetNS00401m/targetNS00401m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/targetNS/targetNS00401m/targetNS00401m1_n.xml",
        instance_is_valid=False,
        class_name="Global",
        version="1.0",
    )


def test_targetns00303m3_positive():
    """
    The form attribute is omitted, the elementFormDefault is set to
    unqualified. (valid schema) Omit the form attribute of the local
    element declaration.                               Set the
    elementFormDefault to  unqualified .
    """
    assert_bindings(
        schema="sunData/ElemDecl/targetNS/targetNS00303m/targetNS00303m3.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/targetNS/targetNS00303m/targetNS00303m3_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_targetns00303m3_negative():
    """
    The form attribute is omitted, the elementFormDefault is set to
    unqualified. (valid schema) Omit the form attribute of the local
    element declaration.                               Set the
    elementFormDefault to  unqualified .
    """
    assert_bindings(
        schema="sunData/ElemDecl/targetNS/targetNS00303m/targetNS00303m3.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/targetNS/targetNS00303m/targetNS00303m3_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_targetns00303m2_positive():
    """
    The form attribute is set to unqualified, the elementFormDefault is
    set to unqualified. (valid schema) Set the form attribute of the local
    element declaration to  unqualified .                              Set
    the elementFormDefault to  unqualified .
    """
    assert_bindings(
        schema="sunData/ElemDecl/targetNS/targetNS00303m/targetNS00303m2.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/targetNS/targetNS00303m/targetNS00303m2_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_targetns00303m2_negative():
    """
    The form attribute is set to unqualified, the elementFormDefault is
    set to unqualified. (valid schema) Set the form attribute of the local
    element declaration to  unqualified .                              Set
    the elementFormDefault to  unqualified .
    """
    assert_bindings(
        schema="sunData/ElemDecl/targetNS/targetNS00303m/targetNS00303m2.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/targetNS/targetNS00303m/targetNS00303m2_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_targetns00303m1_positive():
    """
    The form attribute is set to qualified, the elementFormDefault is set
    to unqualified. (valid schema) Set the form attribute of the local
    element declaration to  qualified .                              Set
    the elementFormDefault to  unqualified .
    """
    assert_bindings(
        schema="sunData/ElemDecl/targetNS/targetNS00303m/targetNS00303m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/targetNS/targetNS00303m/targetNS00303m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_targetns00303m1_negative():
    """
    The form attribute is set to qualified, the elementFormDefault is set
    to unqualified. (valid schema) Set the form attribute of the local
    element declaration to  qualified .                              Set
    the elementFormDefault to  unqualified .
    """
    assert_bindings(
        schema="sunData/ElemDecl/targetNS/targetNS00303m/targetNS00303m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/targetNS/targetNS00303m/targetNS00303m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_targetns00302m3_positive():
    """
    The form attribute is omitted, the elementFormDefault is set to
    qualified. (valid schema) Omit the form attribute of the local element
    declaration.                               Set the elementFormDefault
    to  qualified .
    """
    assert_bindings(
        schema="sunData/ElemDecl/targetNS/targetNS00302m/targetNS00302m3.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/targetNS/targetNS00302m/targetNS00302m3_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_targetns00302m3_negative():
    """
    The form attribute is omitted, the elementFormDefault is set to
    qualified. (valid schema) Omit the form attribute of the local element
    declaration.                               Set the elementFormDefault
    to  qualified .
    """
    assert_bindings(
        schema="sunData/ElemDecl/targetNS/targetNS00302m/targetNS00302m3.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/targetNS/targetNS00302m/targetNS00302m3_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_targetns00302m2_positive():
    """
    The form attribute is set to unqualified, the elementFormDefault is
    set to qualified. (valid schema) Set the form attribute of the local
    element declaration to  unqualified .                              Set
    the elementFormDefault to  qualified .
    """
    assert_bindings(
        schema="sunData/ElemDecl/targetNS/targetNS00302m/targetNS00302m2.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/targetNS/targetNS00302m/targetNS00302m2_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_targetns00302m2_negative():
    """
    The form attribute is set to unqualified, the elementFormDefault is
    set to qualified. (valid schema) Set the form attribute of the local
    element declaration to  unqualified .                              Set
    the elementFormDefault to  qualified .
    """
    assert_bindings(
        schema="sunData/ElemDecl/targetNS/targetNS00302m/targetNS00302m2.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/targetNS/targetNS00302m/targetNS00302m2_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_targetns00302m1_positive():
    """
    The form attribute is set to qualified, the elementFormDefault is set
    to qualified. (valid schema) Set the form attribute of the local
    element declaration to  qualified .                              Set
    the elementFormDefault to  qualified .
    """
    assert_bindings(
        schema="sunData/ElemDecl/targetNS/targetNS00302m/targetNS00302m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/targetNS/targetNS00302m/targetNS00302m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_targetns00302m1_negative():
    """
    The form attribute is set to qualified, the elementFormDefault is set
    to qualified. (valid schema) Set the form attribute of the local
    element declaration to  qualified .                              Set
    the elementFormDefault to  qualified .
    """
    assert_bindings(
        schema="sunData/ElemDecl/targetNS/targetNS00302m/targetNS00302m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/targetNS/targetNS00302m/targetNS00302m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_targetns00301m3_positive():
    """
    Both the form and elementFormDefault attributes are omitted.  (valid
    schema) Omit the form attribute of the local element declaration.
    Omit the elementFormDefault attribute.
    """
    assert_bindings(
        schema="sunData/ElemDecl/targetNS/targetNS00301m/targetNS00301m3.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/targetNS/targetNS00301m/targetNS00301m3_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_targetns00301m3_negative():
    """
    Both the form and elementFormDefault attributes are omitted.  (valid
    schema) Omit the form attribute of the local element declaration.
    Omit the elementFormDefault attribute.
    """
    assert_bindings(
        schema="sunData/ElemDecl/targetNS/targetNS00301m/targetNS00301m3.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/targetNS/targetNS00301m/targetNS00301m3_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_targetns00301m2_positive():
    """
    The form attribute is set to unqualified. The elementFormDefault
    attribute is omitted. (valid schema) Set the form attribute of the
    local element declaration to  unqualified .
    Omit the elementFormDefault attribute.
    """
    assert_bindings(
        schema="sunData/ElemDecl/targetNS/targetNS00301m/targetNS00301m2.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/targetNS/targetNS00301m/targetNS00301m2_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_targetns00301m2_negative():
    """
    The form attribute is set to unqualified. The elementFormDefault
    attribute is omitted. (valid schema) Set the form attribute of the
    local element declaration to  unqualified .
    Omit the elementFormDefault attribute.
    """
    assert_bindings(
        schema="sunData/ElemDecl/targetNS/targetNS00301m/targetNS00301m2.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/targetNS/targetNS00301m/targetNS00301m2_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_targetns00301m1_positive():
    """
    The form attribute is set to qualified. The elementFormDefault
    attribute is omitted. (valid schema) Set the form attribute of the
    local element declaration to  qualified .
    Omit the elementFormDefault attribute.
    """
    assert_bindings(
        schema="sunData/ElemDecl/targetNS/targetNS00301m/targetNS00301m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/targetNS/targetNS00301m/targetNS00301m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_targetns00301m1_negative():
    """
    The form attribute is set to qualified. The elementFormDefault
    attribute is omitted. (valid schema) Set the form attribute of the
    local element declaration to  qualified .
    Omit the elementFormDefault attribute.
    """
    assert_bindings(
        schema="sunData/ElemDecl/targetNS/targetNS00301m/targetNS00301m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/targetNS/targetNS00301m/targetNS00301m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_targetns00201m_target_ns00201m1_p():
    """
    Absent values of {target namespace} validate unqualified items. (valid
    schema) Define unqualified element.
    """
    assert_bindings(
        schema="sunData/ElemDecl/targetNS/targetNS00201m/targetNS00201m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/targetNS/targetNS00201m/targetNS00201m1_p.xml",
        instance_is_valid=True,
        class_name="Number",
        version="1.0",
    )


def test_targetns00201m_target_ns00201m1_n():
    """
    Absent values of {target namespace} validate unqualified items. (valid
    schema) Define unqualified element.
    """
    assert_bindings(
        schema="sunData/ElemDecl/targetNS/targetNS00201m/targetNS00201m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/targetNS/targetNS00201m/targetNS00201m1_n.xml",
        instance_is_valid=False,
        class_name="Number",
        version="1.0",
    )


@pytest.mark.xfail
def test_targetns00101m_target_ns00101m1_p_469():
    """
    Different target namespaces. (valid schema) Define two elements with
    the same name in two different
    Namespaces. Make their content types incompatible.
    Check that validation takes into account the
    property {target namespace}.
    """
    assert_bindings(
        schema="sunData/ElemDecl/targetNS/targetNS00101m/targetNS00101m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/targetNS/targetNS00101m/targetNS00101m1_p.xml",
        instance_is_valid=True,
        class_name="Number",
        version="1.0",
    )


def test_substgrpexcl00402m7_positive():
    """
    Various subsets of values for the final attribute. (valid schema)
    Various subsets of the final attribute values are used for a number of
    elemen declarations.
    """
    assert_bindings(
        schema="sunData/ElemDecl/substGroupExclusions/substGrpExcl00402m/substGrpExcl00402m7.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/substGroupExclusions/substGrpExcl00402m/substGrpExcl00402m7_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_substgrpexcl00401m6_positive():
    """
    Rule out restriction extension (valid schema) Set finalDefault
    attribute to "restriction extension"
    """
    assert_bindings(
        schema="sunData/ElemDecl/substGroupExclusions/substGrpExcl00401m/substGrpExcl00401m6.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/substGroupExclusions/substGrpExcl00401m/substGrpExcl00401m6_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_substgrpexcl00401m5_positive():
    """
    Rule out extension restriction (valid schema) Set finalDefault
    attribute to "extension restriction"
    """
    assert_bindings(
        schema="sunData/ElemDecl/substGroupExclusions/substGrpExcl00401m/substGrpExcl00401m5.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/substGroupExclusions/substGrpExcl00401m/substGrpExcl00401m5_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_substgrpexcl00401m4_positive():
    """
    Rule out extension (valid schema) Set finalDefault attribute to
    "extension"
    """
    assert_bindings(
        schema="sunData/ElemDecl/substGroupExclusions/substGrpExcl00401m/substGrpExcl00401m4.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/substGroupExclusions/substGrpExcl00401m/substGrpExcl00401m4_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_substgrpexcl00401m3_positive():
    """
    Rule out restriction (valid schema) Set finalDefault attribute to
    "restriction"
    """
    assert_bindings(
        schema="sunData/ElemDecl/substGroupExclusions/substGrpExcl00401m/substGrpExcl00401m3.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/substGroupExclusions/substGrpExcl00401m/substGrpExcl00401m3_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_substgrpexcl00401m2_positive():
    """
    Rule out #all (valid schema) Set finalDefault attribute to "#all"
    """
    assert_bindings(
        schema="sunData/ElemDecl/substGroupExclusions/substGrpExcl00401m/substGrpExcl00401m2.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/substGroupExclusions/substGrpExcl00401m/substGrpExcl00401m2_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_substgrpexcl00401m1_positive():
    """
    Rule out nothing (valid schema) Omit the finalDefault attribute.
    """
    assert_bindings(
        schema="sunData/ElemDecl/substGroupExclusions/substGrpExcl00401m/substGrpExcl00401m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/substGroupExclusions/substGrpExcl00401m/substGrpExcl00401m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_substgrpexcl00303m3_positive():
    """
    Rule out both restriction and extension substitutions (positive case).
    (valid schema) Define one element within a substitution group headed
    by                              another element. The elements have the
    type extended                              from the type of the head
    element.                              Try to rule out both restriction
    and extension                              by means of {substitution
    group exclusions} property                               of the head
    element declaration. Try to substitute the
    head with the first element.
    """
    assert_bindings(
        schema="sunData/ElemDecl/substGroupExclusions/substGrpExcl00303m/substGrpExcl00303m3.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/substGroupExclusions/substGrpExcl00303m/substGrpExcl00303m3_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_substgrpexcl00303m1_positive():
    """
    Rule out both restriction and extension substitutions (positive case).
    (valid schema) Define one element within a substitution group headed
    by                              another element. The elements have the
    type extended                              from the type of the head
    element.                              Try to rule out both restriction
    and extension                              by means of {substitution
    group exclusions} property                               of the head
    element declaration. Try to substitute the
    head with the first element.
    """
    assert_bindings(
        schema="sunData/ElemDecl/substGroupExclusions/substGrpExcl00303m/substGrpExcl00303m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/substGroupExclusions/substGrpExcl00303m/substGrpExcl00303m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_substgrpexcl00301m3_positive():
    """
    Rule out both restriction and extension substitutions (positive case).
    (valid schema) Define one element within a substitution group headed
    by                              another element. The elements have the
    same type.                              Try to rule out both
    restriction and extension                              by means of
    {substitution group exclusions} property
    of the head element declaration. Try to substitute the
    head with the first element.
    """
    assert_bindings(
        schema="sunData/ElemDecl/substGroupExclusions/substGrpExcl00301m/substGrpExcl00301m3.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/substGroupExclusions/substGrpExcl00301m/substGrpExcl00301m3_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_substgrpexcl00301m1_positive():
    """
    Rule out both restriction and extension substitutions (positive case).
    (valid schema) Define one element within a substitution group headed
    by                              another element. The elements have the
    same type.                              Try to rule out both
    restriction and extension                              by means of
    {substitution group exclusions} property
    of the head element declaration. Try to substitute the
    head with the first element.
    """
    assert_bindings(
        schema="sunData/ElemDecl/substGroupExclusions/substGrpExcl00301m/substGrpExcl00301m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/substGroupExclusions/substGrpExcl00301m/substGrpExcl00301m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_substgrpexcl00202m1_positive():
    """
    Rule out extension substitutions (positive case). (valid schema)
    Define three elements within one substitution group.
    The first has the same type, the second is derived
    as restriction and the third derived as extension.
    All the elments are the memebers of the substitution
    group. Try to rule out extension                              by means
    of {substitution group exclusions} property
    of the head element declaration.
    """
    assert_bindings(
        schema="sunData/ElemDecl/substGroupExclusions/substGrpExcl00202m/substGrpExcl00202m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/substGroupExclusions/substGrpExcl00202m/substGrpExcl00202m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_substgrpaffil00201m_subst_grp_affil00201m1_p():
    """
    Substitution group memebership is transitive but not symmetric. (valid
    schema) Define an element within a substitution group
    of another one. Then the last one within another
    group. Check the following:                                1. the
    first element substitutes the element of
    the second group                               2. the second element
    doesn't substitute                                  the first one
    """
    assert_bindings(
        schema="sunData/ElemDecl/substGroupAffilation/substGrpAffil00201m/substGrpAffil00201m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/substGroupAffilation/substGrpAffil00201m/substGrpAffil00201m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_substgrpaffil00201m_subst_grp_affil00201m1_n():
    """
    Substitution group memebership is transitive but not symmetric. (valid
    schema) Define an element within a substitution group
    of another one. Then the last one within another
    group. Check the following:                                1. the
    first element substitutes the element of
    the second group                               2. the second element
    doesn't substitute                                  the first one
    """
    assert_bindings(
        schema="sunData/ElemDecl/substGroupAffilation/substGrpAffil00201m/substGrpAffil00201m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/substGroupAffilation/substGrpAffil00201m/substGrpAffil00201m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_substgrpaffil00101m_subst_grp_affil00101m1_p():
    """
    General check of the {substitution group affiliation} property. (valid
    schema) Define two elements within one substitution group
    and one outside the group.
    """
    assert_bindings(
        schema="sunData/ElemDecl/substGroupAffilation/substGrpAffil00101m/substGrpAffil00101m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/substGroupAffilation/substGrpAffil00101m/substGrpAffil00101m1_p.xml",
        instance_is_valid=True,
        class_name="BookStore",
        version="1.0",
    )


def test_substgrpaffil00101m_subst_grp_affil00101m1_n():
    """
    General check of the {substitution group affiliation} property. (valid
    schema) Define two elements within one substitution group
    and one outside the group.
    """
    assert_bindings(
        schema="sunData/ElemDecl/substGroupAffilation/substGrpAffil00101m/substGrpAffil00101m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/substGroupAffilation/substGrpAffil00101m/substGrpAffil00101m1_n.xml",
        instance_is_valid=False,
        class_name="BookStore",
        version="1.0",
    )


def test_scope00301m_scope00301m1_p():
    """
    Scope of a named group. (valid schema) Define a group with two
    elements. Use the group in a
    complexType.
    """
    assert_bindings(
        schema="sunData/ElemDecl/scope/scope00301m/scope00301m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/scope/scope00301m/scope00301m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_scope00201m1_positive():
    """
    Locally scoped element (positive case). (valid schema) Using localy
    scoped element within the complex type.
    """
    assert_bindings(
        schema="sunData/ElemDecl/scope/scope00201m/scope00201m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/scope/scope00201m/scope00201m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_scope00101m_scope00101m1_p():
    """
    General check of the {scope} property. (valid schema) Define one
    global element and one local.
    """
    assert_bindings(
        schema="sunData/ElemDecl/scope/scope00101m/scope00101m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/scope/scope00101m/scope00101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_nillable00401m2_positive():
    """
    there may be a fixed {value constraint} along with nillable set to
    true (valid schema) Declare a nillable element. The the second variant
    declares the element to have fixed value.
    """
    assert_bindings(
        schema="sunData/ElemDecl/nillable/nillable00401m/nillable00401m2.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/nillable/nillable00401m/nillable00401m2_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_nillable00401m1_positive():
    """
    there may be a fixed {value constraint} along with nillable set to
    true (valid schema) Declare a nillable element. The the second variant
    declares the element to have fixed value.
    """
    assert_bindings(
        schema="sunData/ElemDecl/nillable/nillable00401m/nillable00401m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/nillable/nillable00401m/nillable00401m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_nillable00302m_nillable00302m1_p():
    """
    the element information item must have no element information children
    if nil is specified (valid schema) Declare a nillable element of a
    complex type. Set the element to be  nil .
    Negative case tries to have children.
    """
    assert_bindings(
        schema="sunData/ElemDecl/nillable/nillable00302m/nillable00302m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/nillable/nillable00302m/nillable00302m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_nillable00302m_nillable00302m1_n():
    """
    the element information item must have no element information children
    if nil is specified (valid schema) Declare a nillable element of a
    complex type. Set the element to be  nil .
    Negative case tries to have children.
    """
    assert_bindings(
        schema="sunData/ElemDecl/nillable/nillable00302m/nillable00302m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/nillable/nillable00302m/nillable00302m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_nillable00301m_nillable00301m1_p():
    """
    the element information item must have no character if nil is
    specified (valid schema) Declare a nillable element. Set the element
    to be  nil .                              Negative case tries to have
    characters.
    """
    assert_bindings(
        schema="sunData/ElemDecl/nillable/nillable00301m/nillable00301m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/nillable/nillable00301m/nillable00301m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_nillable00301m_nillable00301m1_n():
    """
    the element information item must have no character if nil is
    specified (valid schema) Declare a nillable element. Set the element
    to be  nil .                              Negative case tries to have
    characters.
    """
    assert_bindings(
        schema="sunData/ElemDecl/nillable/nillable00301m/nillable00301m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/nillable/nillable00301m/nillable00301m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_nillable00201m_nillable00201m1_n():
    """
    nillable=false and xsi:nil=true (valid schema) Declare a non-nillable
    element.  Try xsi:nil="true".The test is negative.
    """
    assert_bindings(
        schema="sunData/ElemDecl/nillable/nillable00201m/nillable00201m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/nillable/nillable00201m/nillable00201m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_nillable00201m_nillable00201m2_n():
    """
    nillable=false and xsi:nil=true (valid schema) Declare a non-nillable
    element.  Try xsi:nil="true".The test is negative.
    """
    assert_bindings(
        schema="sunData/ElemDecl/nillable/nillable00201m/nillable00201m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/nillable/nillable00201m/nillable00201m2_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_nillable00201m_nillable00201m3_p():
    """
    nillable=false and xsi:nil=true (valid schema) Declare a non-nillable
    element.  Try xsi:nil="true".The test is negative.
    """
    assert_bindings(
        schema="sunData/ElemDecl/nillable/nillable00201m/nillable00201m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/nillable/nillable00201m/nillable00201m3_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_nillable00102m_nillable00102m1_p():
    """
    xsi:nil=false (valid schema) Define nillable element with content type
    which requires                               content. Try
    xsi:nil=false.
    """
    assert_bindings(
        schema="sunData/ElemDecl/nillable/nillable00102m/nillable00102m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/nillable/nillable00102m/nillable00102m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_nillable00102m_nillable00102m1_n():
    """
    xsi:nil=false (valid schema) Define nillable element with content type
    which requires                               content. Try
    xsi:nil=false.
    """
    assert_bindings(
        schema="sunData/ElemDecl/nillable/nillable00102m/nillable00102m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/nillable/nillable00102m/nillable00102m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_nillable00101m2_negative():
    """
    nillable=false (negative case) (valid schema) Define nillable element
    with content type which requires
    content. Try nillable=false.
    """
    assert_bindings(
        schema="sunData/ElemDecl/nillable/nillable00101m/nillable00101m2.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/nillable/nillable00101m/nillable00101m2_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_nillable00101m1_positive():
    """
    nillable=false (positive case) (valid schema) Define nillable element
    with content type which requires
    content. Try nillable=false.
    """
    assert_bindings(
        schema="sunData/ElemDecl/nillable/nillable00101m/nillable00101m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/nillable/nillable00101m/nillable00101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_name00805_name00805_p():
    """
    Element names contain only punctuation characters and digits. (valid
    schema) Declare an element with a sequence of two integer elements.
    Name the first one                                      as "_-." and
    the second one as "_-0.".
    The document name00805_p.xml sets the attributes to 0 and 1
    respectively.
    """
    assert_bindings(
        schema="sunData/ElemDecl/name/name008/name00805/name00805.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/name/name008/name00805/name00805_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_name00804_name00804_p():
    """
    Element names contain lower case and upper case letters and non-letter
    characters. (valid schema) Declare an element with a sequence of
    integer elements. Name them as follows:
    "aaaa",  "bbbB",  "ccCc",  "ddDD",  "eEee",
    "fFfF",  "pPPp",  "gGGG",  "Hhhh",  "IiiI",  "JjJj",
    "KkKK",  "LLll",  "MMmM",  "NNNn",  "OOOO",
    "bbb0",  "cc0c",  "dd00",  "e0ee",  "f0f0",  "p00p",  "g000",
    "bbb_",  "cc_c",  "dd__",  "e_ee",  "f_f_",  "p__p",  "g___",
    "H111",  "I11I",  "J1J1",  "K1KK",  "LL11",  "MM1M",  "NNN1",
    "H---",  "I--I",  "J-J-",  "K-KK",  "LL--",  "MM-M",  "NNN-".
    The document name00804_p.xml sets all the elements.
    """
    assert_bindings(
        schema="sunData/ElemDecl/name/name008/name00804/name00804.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/name/name008/name00804/name00804_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_name00803_name00803_p():
    """
    Element names contain digits followed by a non-digit characters.
    (valid schema) Declare an element with a sequence of three integer
    elements. Name them                                       as follows:
    "aa111a2Aa", "aa22B3c", "aa3-4_".
    The document name00803_p.xml sets the elements to 0, 1 and 2
    respectively.
    """
    assert_bindings(
        schema="sunData/ElemDecl/name/name008/name00803/name00803.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/name/name008/name00803/name00803_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_name00802_name00802_p():
    r"""
    Element name contains 7 punctuation characters. (valid schema) Declare
    an element with a sequence of two int elements. Name the first one
    using 7 punctuation characters:
    hyphen ('-', \u002D, HYPHEN-MINUS), period ('.', \u002E, FULL STOP),
    underscore ('_', \u005F, LOW LINE),
    dot ('.', \u00B7, MIDDLE DOT), \u0387, GREEK ANO TELEIA,
    \u06DD, ARABIC END OF AYAH and \u06DE, ARABIC START OF RUB EL HIZB.
    Name the                                       second element with the
    same name except the characters described.
    The document name00802_p.xml sets the elements to 0 and 1
    respectively.
    """
    assert_bindings(
        schema="sunData/ElemDecl/name/name008/name00802/name00802.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/name/name008/name00802/name00802_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_name00801_name00801_p():
    r"""
    Element names contain several punctuation characters. (valid schema)
    Declare an element with a sequence of elements of type int. Name the
    elements                                      using 7 punctuation
    characters:                                       hyphen ('-', \u002D,
    HYPHEN-MINUS), period ('.', \u002E, FULL STOP),
    underscore ('_', \u005F, LOW LINE),
    dot ('.', \u00B7, MIDDLE DOT), \u0387, GREEK ANO TELEIA,
    \u06DD, ARABIC END OF AYAH and \u06DE, ARABIC START OF RUB EL HIZB.
    The document name00801_p.xml sets the elements to 0, 1, 2, ..., 6
    respectively.
    """
    assert_bindings(
        schema="sunData/ElemDecl/name/name008/name00801/name00801.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/name/name008/name00801/name00801_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_name00601m_name00601m1_p():
    """
    The declaration must not be absent (valid schema) Declare an element
    root .                               Use element information item with
    respect to the element declaration.                              The
    negative case uses undeclared element.
    """
    assert_bindings(
        schema="sunData/ElemDecl/name/name00601m/name00601m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/name/name00601m/name00601m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_name00601m_name00601m1_n():
    """
    The declaration must not be absent (valid schema) Declare an element
    root .                               Use element information item with
    respect to the element declaration.                              The
    negative case uses undeclared element.
    """
    assert_bindings(
        schema="sunData/ElemDecl/name/name00601m/name00601m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/name/name00601m/name00601m1_n.xml",
        instance_is_valid=False,
        class_name="Toor",
        version="1.0",
    )


def test_name00505m1_positive():
    """
    element declaration with keyref (valid schema) Declare an element with
    keyref .
    Check that the schema is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/name/name00505m/name00505m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/name/name00505m/name00505m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_name00504m3_positive():
    """
    element declaration with unique (valid schema) Declare an element with
    unique .
    Check that the schema is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/name/name00504m/name00504m3.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/name/name00504m/name00504m3_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_name00504m1_positive():
    """
    element declaration with key (valid schema) Declare an element with
    key .                                                            Check
    that the schema is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/name/name00504m/name00504m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/name/name00504m/name00504m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_name00503m1_positive():
    """
    element declaration with simple type (valid schema) Declare an element
    using inline simple type definition.
    Check that the schema is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/name/name00503m/name00503m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/name/name00503m/name00503m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_name00502m1_positive():
    """
    element declaration with complex type (valid schema) Declare an
    element using inline complex type definition.
    Check that the schema is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/name/name00502m/name00502m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/name/name00502m/name00502m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_name00501m9_positive():
    """
    block is present (valid schema) Declare an element. Set name ="Local"
    block="#all" type="xsd:boolean".                              Check
    that the schema is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/name/name00501m/name00501m9.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/name/name00501m/name00501m9_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_name00501m7_positive():
    """
    form is present (valid schema) Declare an element. Set name ="Local"
    form="qualified" type="xsd:boolean".
    Check that the schema is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/name/name00501m/name00501m7.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/name/name00501m/name00501m7_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_name00501m5_positive():
    """
    fixed is present (valid schema) Declare an element. Set name ="Local"
    fixed="true" type="xsd:boolean".                              Check
    that the schema is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/name/name00501m/name00501m5.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/name/name00501m/name00501m5_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_name00501m3_positive():
    """
    default is present (valid schema) Declare an element. Set name
    ="Local" default="true" type="xsd:boolean".
    Check that the schema is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/name/name00501m/name00501m3.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/name/name00501m/name00501m3_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_name00501m15_positive():
    """
    id and ref are present (valid schema) Declare an element. Set
    ref="Main" id="X123".                              Check that the
    schema is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/name/name00501m/name00501m15.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/name/name00501m/name00501m15_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_name00501m14_positive():
    """
    maxOccurs and ref are present (valid schema) Declare an element. Set
    ref="Main" maxOccurs="unbounded".                              Check
    that the schema is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/name/name00501m/name00501m14.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/name/name00501m/name00501m14_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_name00501m13_positive():
    """
    minOccurs and ref are present (valid schema) Declare an element. Set
    ref="Main" minOccurs="0".                              Check that the
    schema is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/name/name00501m/name00501m13.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/name/name00501m/name00501m13_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_name00501m11_positive():
    """
    type is present (valid schema) Declare an element. Set name ="Local"
    type="xsd:boolean".                              Check that the schema
    is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/name/name00501m/name00501m11.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/name/name00501m/name00501m11_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_name00501m1_positive():
    """
    nillable is present (valid schema) Declare an element. Set name
    ="Local" nillable="true" type="xsd:boolean".
    Check that the schema is valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/name/name00501m/name00501m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/name/name00501m/name00501m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_name00401m2_positive():
    """
    the root attribute is set (valid schema) Declare an element. Set
    ref="root".                              Check that the schema is
    valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/name/name00401m/name00401m2.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/name/name00401m/name00401m2_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_name00401m1_positive():
    """
    the name attribute is set (valid schema) Declare an element. Set
    name="Local".                              Check that the schema is
    valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/name/name00401m/name00401m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/name/name00401m/name00401m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_name00301m1_positive():
    """
    Local element names do not clash. (valid schema) Declare two local
    elements with the same name but in different
    scope.
    """
    assert_bindings(
        schema="sunData/ElemDecl/name/name00301m/name00301m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/name/name00301m/name00301m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_name00201m2_positive():
    """
    simpleType definitions and element  declarations have different symbol
    spaces. (valid schema) Declare an element. Define a
    simpleType  with the same name.                              Check
    that there is no name clash.
    """
    assert_bindings(
        schema="sunData/ElemDecl/name/name00201m/name00201m2.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/name/name00201m/name00201m2_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_name00201m1_positive():
    """
    complexType definitions and element  declarations have different
    symbol spaces. (valid schema) Declare an element. Define a
    complexType  with the same name.                              Check
    that there is no name clash.
    """
    assert_bindings(
        schema="sunData/ElemDecl/name/name00201m/name00201m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/name/name00201m/name00201m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_name00101m_name00101m1_p_528():
    """
    General check of the {name} property. (valid schema) Define two
    elements with incompatible types. Check that the
    elements are validated properly.
    """
    assert_bindings(
        schema="sunData/ElemDecl/name/name00101m/name00101m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/name/name00101m/name00101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_name00101m_name00101m1_n_529():
    """
    General check of the {name} property. (valid schema) Define two
    elements with incompatible types. Check that the
    elements are validated properly.
    """
    assert_bindings(
        schema="sunData/ElemDecl/name/name00101m/name00101m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/name/name00101m/name00101m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_minoccurs00201m_min_occurs00201m1_p():
    """
    Default value of the {minOccurs} property when the ref attribute is
    used. (valid schema) Declare a local element with a reference to a
    global one. Omit minOccurs                               attribute.
    Check that the value of the {minOccurs} property is 1.
    """
    assert_bindings(
        schema="sunData/ElemDecl/minOccurs/minOccurs00201m/minOccurs00201m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/minOccurs/minOccurs00201m/minOccurs00201m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_minoccurs00201m_min_occurs00201m1_n():
    """
    Default value of the {minOccurs} property when the ref attribute is
    used. (valid schema) Declare a local element with a reference to a
    global one. Omit minOccurs                               attribute.
    Check that the value of the {minOccurs} property is 1.
    """
    assert_bindings(
        schema="sunData/ElemDecl/minOccurs/minOccurs00201m/minOccurs00201m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/minOccurs/minOccurs00201m/minOccurs00201m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_minoccurs00101m_min_occurs00101m1_p():
    """
    Default value of the {minOccurs} property. (valid schema) Define one
    global element and one local. Omit minOccurs attribute. Check that
    the value of the {minOccurs} property is 1.
    """
    assert_bindings(
        schema="sunData/ElemDecl/minOccurs/minOccurs00101m/minOccurs00101m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/minOccurs/minOccurs00101m/minOccurs00101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_minoccurs00101m_min_occurs00101m1_n():
    """
    Default value of the {minOccurs} property. (valid schema) Define one
    global element and one local. Omit minOccurs attribute. Check that
    the value of the {minOccurs} property is 1.
    """
    assert_bindings(
        schema="sunData/ElemDecl/minOccurs/minOccurs00101m/minOccurs00101m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/minOccurs/minOccurs00101m/minOccurs00101m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_maxoccurs00201m_max_occurs00201m1_p():
    """
    Default value of the {maxOccurs} property when the ref attribute is
    used. (valid schema) Define one local that refers to a global one.
    Omit maxOccurs attribute.                               Check that the
    value of the {maxOccurs} property is 1.
    """
    assert_bindings(
        schema="sunData/ElemDecl/maxOccurs/maxOccurs00201m/maxOccurs00201m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/maxOccurs/maxOccurs00201m/maxOccurs00201m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_maxoccurs00201m_max_occurs00201m1_n():
    """
    Default value of the {maxOccurs} property when the ref attribute is
    used. (valid schema) Define one local that refers to a global one.
    Omit maxOccurs attribute.                               Check that the
    value of the {maxOccurs} property is 1.
    """
    assert_bindings(
        schema="sunData/ElemDecl/maxOccurs/maxOccurs00201m/maxOccurs00201m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/maxOccurs/maxOccurs00201m/maxOccurs00201m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_maxoccurs00101m_max_occurs00101m1_p():
    """
    Default value of the {maxOccurs} property. (valid schema) Define one
    global element and one local. Omit maxOccurs attribute. Check that
    the value of the {maxOccurs} property is 1.
    """
    assert_bindings(
        schema="sunData/ElemDecl/maxOccurs/maxOccurs00101m/maxOccurs00101m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/maxOccurs/maxOccurs00101m/maxOccurs00101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_maxoccurs00101m_max_occurs00101m1_n():
    """
    Default value of the {maxOccurs} property. (valid schema) Define one
    global element and one local. Omit maxOccurs attribute. Check that
    the value of the {maxOccurs} property is 1.
    """
    assert_bindings(
        schema="sunData/ElemDecl/maxOccurs/maxOccurs00101m/maxOccurs00101m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/maxOccurs/maxOccurs00101m/maxOccurs00101m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_idconstrdefs00501m_id_constr_defs00501m1_p():
    """
    there must be no multiply-defined ID (valid schema) Declare an
    attribute of a type derived from ID.
    Ensure that two element information items
    may not have that attributes with the same values.
    """
    assert_bindings(
        schema="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00501m/idConstrDefs00501m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00501m/idConstrDefs00501m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_idconstrdefs00501m_id_constr_defs00501m1_n():
    """
    there must be no multiply-defined ID (valid schema) Declare an
    attribute of a type derived from ID.
    Ensure that two element information items
    may not have that attributes with the same values.
    """
    assert_bindings(
        schema="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00501m/idConstrDefs00501m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00501m/idConstrDefs00501m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_idconstrdefs00403m_id_constr_defs00403m1_p():
    """
    derived IDREFS must refer to IDs that are defined (valid schema)
    Declare an attribute of a type derived from ID.
    Declare an attribute of a type derived from IDREFS.
    Ensure that the second attribute is not allowed to refer to a values
    that are not defined by the first attribute.
    """
    assert_bindings(
        schema="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00403m/idConstrDefs00403m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00403m/idConstrDefs00403m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_idconstrdefs00403m_id_constr_defs00403m1_n():
    """
    derived IDREFS must refer to IDs that are defined (valid schema)
    Declare an attribute of a type derived from ID.
    Declare an attribute of a type derived from IDREFS.
    Ensure that the second attribute is not allowed to refer to a values
    that are not defined by the first attribute.
    """
    assert_bindings(
        schema="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00403m/idConstrDefs00403m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00403m/idConstrDefs00403m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_idconstrdefs00402m_id_constr_defs00402m1_p():
    """
    derived IDREF must refer to an ID that is defined (valid schema)
    Declare an attribute of a type derived from ID.
    Declare an attribute of a type derived from IDREF.
    Ensure that the second attribute is not allowed to refer to a value
    that is not defined by the first attribute.
    """
    assert_bindings(
        schema="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00402m/idConstrDefs00402m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00402m/idConstrDefs00402m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_idconstrdefs00402m_id_constr_defs00402m1_n():
    """
    derived IDREF must refer to an ID that is defined (valid schema)
    Declare an attribute of a type derived from ID.
    Declare an attribute of a type derived from IDREF.
    Ensure that the second attribute is not allowed to refer to a value
    that is not defined by the first attribute.
    """
    assert_bindings(
        schema="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00402m/idConstrDefs00402m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00402m/idConstrDefs00402m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_idconstrdefs00401m_id_constr_defs00401m1_p():
    """
    derived IDREF must refer to an ID that is defined (cyclic) (valid
    schema) Declare an attribute of a type derived from ID.
    Declare an attribute of a type derived from IDREF.
    Ensure that the second attribute is allowed to refer to a value
    that is defined by the first attribute defined in the same
    element information item.
    """
    assert_bindings(
        schema="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00401m/idConstrDefs00401m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00401m/idConstrDefs00401m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_idconstrdefs00302m_id_constr_defs00302m1_p():
    """
    all attributes of type ID, IDREF, IDREFS are valid (valid schema) All
    ID, IDREF and IDREFS attributes are valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00302m/idConstrDefs00302m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00302m/idConstrDefs00302m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_idconstrdefs00302m_id_constr_defs00302m2_n():
    """
    all attributes of type ID, IDREF, IDREFS are valid (valid schema) All
    ID, IDREF and IDREFS attributes are valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00302m/idConstrDefs00302m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00302m/idConstrDefs00302m2_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_idconstrdefs00302m_id_constr_defs00302m3_n():
    """
    all attributes of type ID, IDREF, IDREFS are valid (valid schema) All
    ID, IDREF and IDREFS attributes are valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00302m/idConstrDefs00302m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00302m/idConstrDefs00302m3_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_idconstrdefs00302m_id_constr_defs00302m4_n():
    """
    all attributes of type ID, IDREF, IDREFS are valid (valid schema) All
    ID, IDREF and IDREFS attributes are valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00302m/idConstrDefs00302m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00302m/idConstrDefs00302m4_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_idconstrdefs00301m_id_constr_defs00301m1_p():
    """
    all ID, IDREF, IDREFS are valid (valid schema) All ID, IDREF and
    IDREFS values are valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00301m/idConstrDefs00301m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00301m/idConstrDefs00301m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_idconstrdefs00301m_id_constr_defs00301m2_n():
    """
    all ID, IDREF, IDREFS are valid (valid schema) All ID, IDREF and
    IDREFS values are valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00301m/idConstrDefs00301m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00301m/idConstrDefs00301m2_n.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_idconstrdefs00301m_id_constr_defs00301m3_n():
    """
    all ID, IDREF, IDREFS are valid (valid schema) All ID, IDREF and
    IDREFS values are valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00301m/idConstrDefs00301m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00301m/idConstrDefs00301m3_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_idconstrdefs00301m_id_constr_defs00301m4_n():
    """
    all ID, IDREF, IDREFS are valid (valid schema) All ID, IDREF and
    IDREFS values are valid.
    """
    assert_bindings(
        schema="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00301m/idConstrDefs00301m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00301m/idConstrDefs00301m4_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_idconstrdefs00204m_id_constr_defs00204m1_p():
    """
    keyref must refer to a key that is defined (valid schema) Define a key
    identity constraint. Define a keyref to that key.
    Ensure that the keyref field is not allowed to refer to a
    key that is not defined.
    """
    assert_bindings(
        schema="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00204m/idConstrDefs00204m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00204m/idConstrDefs00204m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_idconstrdefs00204m_id_constr_defs00204m1_n():
    """
    keyref must refer to a key that is defined (valid schema) Define a key
    identity constraint. Define a keyref to that key.
    Ensure that the keyref field is not allowed to refer to a
    key that is not defined.
    """
    assert_bindings(
        schema="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00204m/idConstrDefs00204m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00204m/idConstrDefs00204m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_idconstrdefs00203m_id_constr_defs00203m1_p():
    """
    there must be no uniqueness violations (valid schema) Define a
    uniqueness identity constraint with two fields.
    Ensure that the constraint prevents one pair of values to be
    defined twice.
    """
    assert_bindings(
        schema="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00203m/idConstrDefs00203m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00203m/idConstrDefs00203m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_idconstrdefs00203m_id_constr_defs00203m1_n():
    """
    there must be no uniqueness violations (valid schema) Define a
    uniqueness identity constraint with two fields.
    Ensure that the constraint prevents one pair of values to be
    defined twice.
    """
    assert_bindings(
        schema="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00203m/idConstrDefs00203m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00203m/idConstrDefs00203m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_idconstrdefs00202m_id_constr_defs00202m1_p():
    """
    there must be no multiply-defined ID (valid schema) Define a key
    identity constraint with two fields.
    Ensure that the constraint prevents one key to be
    defined twice.
    """
    assert_bindings(
        schema="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00202m/idConstrDefs00202m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00202m/idConstrDefs00202m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_idconstrdefs00202m_id_constr_defs00202m1_n():
    """
    there must be no multiply-defined ID (valid schema) Define a key
    identity constraint with two fields.
    Ensure that the constraint prevents one key to be
    defined twice.
    """
    assert_bindings(
        schema="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00202m/idConstrDefs00202m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00202m/idConstrDefs00202m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_idconstrdefs00201m_id_constr_defs00201m1_p():
    """
    all kinds of identity constraint are not violated (valid schema)
    Define and check key, keyref and uniqueness among values of elements.
    In the test all kinds of identity constraint are not violated.
    """
    assert_bindings(
        schema="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00201m/idConstrDefs00201m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00201m/idConstrDefs00201m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_idconstrdefs00201m_id_constr_defs00201m2_n():
    """
    all kinds of identity constraint are not violated (valid schema)
    Define and check key, keyref and uniqueness among values of elements.
    In the test all kinds of identity constraint are not violated.
    """
    assert_bindings(
        schema="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00201m/idConstrDefs00201m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00201m/idConstrDefs00201m2_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_idconstrdefs00201m_id_constr_defs00201m3_n():
    """
    all kinds of identity constraint are not violated (valid schema)
    Define and check key, keyref and uniqueness among values of elements.
    In the test all kinds of identity constraint are not violated.
    """
    assert_bindings(
        schema="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00201m/idConstrDefs00201m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00201m/idConstrDefs00201m3_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_idconstrdefs00201m_id_constr_defs00201m4_n():
    """
    all kinds of identity constraint are not violated (valid schema)
    Define and check key, keyref and uniqueness among values of elements.
    In the test all kinds of identity constraint are not violated.
    """
    assert_bindings(
        schema="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00201m/idConstrDefs00201m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00201m/idConstrDefs00201m4_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_idconstrdefs00101m_id_constr_defs00101m1_p():
    """
    Uniqueness among values of elements. (valid schema) Define and check a
    uniqueness among values of elements.
    """
    assert_bindings(
        schema="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00101m/idConstrDefs00101m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00101m/idConstrDefs00101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_idconstrdefs00101m_id_constr_defs00101m1_n():
    """
    Uniqueness among values of elements. (valid schema) Define and check a
    uniqueness among values of elements.
    """
    assert_bindings(
        schema="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00101m/idConstrDefs00101m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/identityConstraintDefs/idConstrDefs00101m/idConstrDefs00101m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_disallowedsubst00503m5_negative():
    """
    derived by restriction: prohibiting substitutions contains '#all'
    (valid schema) Two elements are declared. The second one has type
    derived by restriction from type of the first element.
    Prohibiting substitutions of the first element's type contain '#all',
    so the second element is not substitutable for the first one.
    """
    assert_bindings(
        schema="sunData/ElemDecl/disallowedSubst/disallowedSubst00503m/disallowedSubst00503m5.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/disallowedSubst/disallowedSubst00503m/disallowedSubst00503m5_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_disallowedsubst00503m4_negative():
    """
    derived by restriction: prohibiting substitutions contains
    'restriction extension' (valid schema) Two elements are declared. The
    second one has type derived by restriction from type of the first
    element.                              Prohibiting substitutions of the
    first element's type contain 'restriction extension', so the second
    element is not substitutable for the first one.
    """
    assert_bindings(
        schema="sunData/ElemDecl/disallowedSubst/disallowedSubst00503m/disallowedSubst00503m4.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/disallowedSubst/disallowedSubst00503m/disallowedSubst00503m4_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_disallowedsubst00503m3_negative():
    """
    derived by restriction: prohibiting substitutions contains
    'restriction' (valid schema) Two elements are declared. The second one
    has type derived by restriction from type of the first element.
    Prohibiting substitutions of the first element's type contain
    'restriction', so the second element is not substitutable for the
    first one.
    """
    assert_bindings(
        schema="sunData/ElemDecl/disallowedSubst/disallowedSubst00503m/disallowedSubst00503m3.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/disallowedSubst/disallowedSubst00503m/disallowedSubst00503m3_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_disallowedsubst00503m2_positive():
    """
    derived by restriction: prohibiting substitutions contains 'extension'
    (valid schema) Two elements are declared. The second one has type
    derived by restriction from type of the first element.
    Prohibiting substitutions of the first element's type contain
    'extension', so the second element is substitutable for the first one.
    """
    assert_bindings(
        schema="sunData/ElemDecl/disallowedSubst/disallowedSubst00503m/disallowedSubst00503m2.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/disallowedSubst/disallowedSubst00503m/disallowedSubst00503m2_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_disallowedsubst00503m1_positive():
    """
    derived by restriction: prohibiting substitutions is empty (valid
    schema) Two elements are declared. The second one has type derived by
    restriction from type of the first element.
    Prohibiting substitutions of the first element's type is empty, so the
    second element is substitutable for the first one.
    """
    assert_bindings(
        schema="sunData/ElemDecl/disallowedSubst/disallowedSubst00503m/disallowedSubst00503m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/disallowedSubst/disallowedSubst00503m/disallowedSubst00503m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_disallowedsubst00502m4_negative():
    """
    complex type substitution: extension and restriction are blocked
    (valid schema) Two elements are declared. The second one has type
    derived by extension from type of the first element.
    Blockong constraints of the first element contain 'restriction
    extension', so the second element is not substitutable for the first
    one.
    """
    assert_bindings(
        schema="sunData/ElemDecl/disallowedSubst/disallowedSubst00502m/disallowedSubst00502m4.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/disallowedSubst/disallowedSubst00502m/disallowedSubst00502m4_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_disallowedsubst00502m3_negative():
    """
    complex type substitution: extension is blocked (valid schema) Two
    elements are declared. The second one has type derived by extension
    from type of the first element.                              Blockong
    constraints of the first element contain 'extension', so the second
    element is not substitutable for the first one.
    """
    assert_bindings(
        schema="sunData/ElemDecl/disallowedSubst/disallowedSubst00502m/disallowedSubst00502m3.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/disallowedSubst/disallowedSubst00502m/disallowedSubst00502m3_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_disallowedsubst00502m2_positive():
    """
    complex type substitution: restriction is blocked (valid schema) Two
    elements are declared. The second one has type derived by extension
    from type of the first element.                              Blockong
    constraints of the first element contain 'restriction', so the second
    element is substitutable for the first one.
    """
    assert_bindings(
        schema="sunData/ElemDecl/disallowedSubst/disallowedSubst00502m/disallowedSubst00502m2.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/disallowedSubst/disallowedSubst00502m/disallowedSubst00502m2_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_disallowedsubst00502m1_positive():
    """
    complex type substitution: no blocking constraints (valid schema) Two
    elements are declared. The second one has type derived by extension
    from type of the first element.                              Blockong
    constraints of the first element is empty, so the second element is
    substitutable for the first one.
    """
    assert_bindings(
        schema="sunData/ElemDecl/disallowedSubst/disallowedSubst00502m/disallowedSubst00502m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/disallowedSubst/disallowedSubst00502m/disallowedSubst00502m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_disallowedsubst00501m2_negative():
    """
    restriction is blocked (valid schema) Two elements are declared. The
    second one has type derived by restriction from type of the first
    element.                              Blockong constraints of the
    first element contain 'restriction', so the second element is not
    substitutable for the first one.
    """
    assert_bindings(
        schema="sunData/ElemDecl/disallowedSubst/disallowedSubst00501m/disallowedSubst00501m2.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/disallowedSubst/disallowedSubst00501m/disallowedSubst00501m2_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_disallowedsubst00501m1_positive():
    """
    no blocking constraints (valid schema) Two elements are declared. The
    second one has type derived by restriction from type of the first
    element.                              Blockong constraints of the
    first element is empty, so the second element is substitutable for the
    first one.
    """
    assert_bindings(
        schema="sunData/ElemDecl/disallowedSubst/disallowedSubst00501m/disallowedSubst00501m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/disallowedSubst/disallowedSubst00501m/disallowedSubst00501m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_disallowedsubst00401m2_negative():
    """
    substitution is disallowed (valid schema) The blocking constraint must
    not contain substitution for an                               element
    declaration to be validly substituteable for another element
    declaration.                                In the test any
    substitution for element  Head  is
    disallowed.
    """
    assert_bindings(
        schema="sunData/ElemDecl/disallowedSubst/disallowedSubst00401m/disallowedSubst00401m2.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/disallowedSubst/disallowedSubst00401m/disallowedSubst00401m2_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_disallowedsubst00401m1_positive():
    """
    substitution is allowed (valid schema) The blocking constraint must
    not contain substitution for an                               element
    declaration to be validly substituteable for another element
    declaration.                                In the test any
    substitution for element  Head  is
    allowed.
    """
    assert_bindings(
        schema="sunData/ElemDecl/disallowedSubst/disallowedSubst00401m/disallowedSubst00401m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/disallowedSubst/disallowedSubst00401m/disallowedSubst00401m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_disallowedsubst00301m2_negative():
    """
    substitution is disallowed (valid schema) The blocking constraint must
    not contain substitution for an                               element
    declaration to be validly substituteable for another element
    declaration.                                In the test any
    substitution for element  Head  is
    disallowed.
    """
    assert_bindings(
        schema="sunData/ElemDecl/disallowedSubst/disallowedSubst00301m/disallowedSubst00301m2.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/disallowedSubst/disallowedSubst00301m/disallowedSubst00301m2_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_disallowedsubst00301m1_positive():
    """
    substitution is allowed (valid schema) The blocking constraint must
    not contain substitution for an                               element
    declaration to be validly substituteable for another element
    declaration.                                In the test any
    substitution for element  Head  is
    allowed.
    """
    assert_bindings(
        schema="sunData/ElemDecl/disallowedSubst/disallowedSubst00301m/disallowedSubst00301m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/disallowedSubst/disallowedSubst00301m/disallowedSubst00301m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_disallowedsubst00202m12_positive():
    """
    Various subsets of blocking values. (valid schema) Various subsets of
    blocking values are used for a number of
    elemen declarations.
    """
    assert_bindings(
        schema="sunData/ElemDecl/disallowedSubst/disallowedSubst00202m/disallowedSubst00202m12.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/disallowedSubst/disallowedSubst00202m/disallowedSubst00202m12_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_disallowedsubst00106m2_negative():
    """
    Blocking any extension (negative case) (valid schema) Define an
    element within a substitution group headed
    by another element. The first element has a type
    extended from the type of the head. Block (disallow)
    an extension of the head. Try to substitute
    the head element with the first one.
    """
    assert_bindings(
        schema="sunData/ElemDecl/disallowedSubst/disallowedSubst00106m/disallowedSubst00106m2.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/disallowedSubst/disallowedSubst00106m/disallowedSubst00106m2_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_disallowedsubst00106m1_positive():
    """
    Blocking any extension (positive case) (valid schema) Define an
    element within a substitution group headed
    by another element. The first element has a type
    extended from the type of the head. Block (disallow)
    an extension of the head. Try to substitute
    the head element with the first one.
    """
    assert_bindings(
        schema="sunData/ElemDecl/disallowedSubst/disallowedSubst00106m/disallowedSubst00106m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/disallowedSubst/disallowedSubst00106m/disallowedSubst00106m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_disallowedsubst00105m_disallowed_subst00105m1_p():
    """
    Blocking any extension. (valid schema) Define an element within a
    substitution group headed                               by another
    element. The first element has a type
    extended from the type of the head. Block (disallow)
    an extension of the head. Try to substitute
    the head element with the first one.
    """
    assert_bindings(
        schema="sunData/ElemDecl/disallowedSubst/disallowedSubst00105m/disallowedSubst00105m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/disallowedSubst/disallowedSubst00105m/disallowedSubst00105m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_disallowedsubst00105m_disallowed_subst00105m1_n():
    """
    Blocking any extension. (valid schema) Define an element within a
    substitution group headed                               by another
    element. The first element has a type
    extended from the type of the head. Block (disallow)
    an extension of the head. Try to substitute
    the head element with the first one.
    """
    assert_bindings(
        schema="sunData/ElemDecl/disallowedSubst/disallowedSubst00105m/disallowedSubst00105m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/disallowedSubst/disallowedSubst00105m/disallowedSubst00105m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_disallowedsubst00102m2_negative():
    """
    Blocking any substitution (negative case) (valid schema) Define an
    element within a substitution group
    headed by another element. The elements have the same
    type. Block (disallow) a substitution of the head. Try
    to substitute the head element with the first one.
    """
    assert_bindings(
        schema="sunData/ElemDecl/disallowedSubst/disallowedSubst00102m/disallowedSubst00102m2.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/disallowedSubst/disallowedSubst00102m/disallowedSubst00102m2_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_disallowedsubst00102m1_positive():
    """
    Blocking any substitution (positive case) (valid schema) Define an
    element within a substitution group
    headed by another element. The elements have the same
    type. Block (disallow) a substitution of the head. Try
    to substitute the head element with the first one.
    """
    assert_bindings(
        schema="sunData/ElemDecl/disallowedSubst/disallowedSubst00102m/disallowedSubst00102m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/disallowedSubst/disallowedSubst00102m/disallowedSubst00102m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_disallowedsubst00101m_disallowed_subst00101m1_p():
    """
    Blocking any substitution. (valid schema) Define an element within a
    substitution group                              headed by another
    element. The elements have the same
    type. Block (disallow) a substitution of the head. Try
    to substitute the head element with the first one.
    """
    assert_bindings(
        schema="sunData/ElemDecl/disallowedSubst/disallowedSubst00101m/disallowedSubst00101m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/disallowedSubst/disallowedSubst00101m/disallowedSubst00101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_disallowedsubst00101m_disallowed_subst00101m1_n():
    """
    Blocking any substitution. (valid schema) Define an element within a
    substitution group                              headed by another
    element. The elements have the same
    type. Block (disallow) a substitution of the head. Try
    to substitute the head element with the first one.
    """
    assert_bindings(
        schema="sunData/ElemDecl/disallowedSubst/disallowedSubst00101m/disallowedSubst00101m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/disallowedSubst/disallowedSubst00101m/disallowedSubst00101m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_annotation00101m3_positive():
    """
    machine-targeted  annotation for element declaration (valid schema)
    Annotations provide for human- and machine-targeted
    annotations of schema components.                               In the
    test the machine-targeted annotation                               is
    provided for an element declaration.
    """
    assert_bindings(
        schema="sunData/ElemDecl/annotation/annotation00101m/annotation00101m3.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/annotation/annotation00101m/annotation00101m3_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_annotation00101m1_positive_590():
    """
    human-targeted  annotation for element declaration (valid schema)
    Annotations provide for human- and machine-targeted
    annotations of schema components.                               In the
    test the human-targeted annotation                               is
    provided for an element declaration.
    """
    assert_bindings(
        schema="sunData/ElemDecl/annotation/annotation00101m/annotation00101m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/annotation/annotation00101m/annotation00101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_abstract00201m3_positive():
    """
    use default value of the attribute abstract  (valid schema) Declare an
    element with default value of the attribute abstract.
    Try to use it in the xml document.
    """
    assert_bindings(
        schema="sunData/ElemDecl/abstract/abstract00201m/abstract00201m3.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/abstract/abstract00201m/abstract00201m3_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_abstract00201m2_positive():
    """
    use abstarct explicitly set to false  (valid schema) Declare an
    element with abstarct explicitly set to false.
    Try to use it in the xml document.
    """
    assert_bindings(
        schema="sunData/ElemDecl/abstract/abstract00201m/abstract00201m2.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/abstract/abstract00201m/abstract00201m2_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_abstract00201m1_negative():
    """
    use abstarct explicitly set to true  (valid schema) Declare an element
    with abstarct explicitly set to true.                              Try
    to use it in the xml document.
    """
    assert_bindings(
        schema="sunData/ElemDecl/abstract/abstract00201m/abstract00201m1.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/abstract/abstract00201m/abstract00201m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_abstract00101m_abstract00101m1_p():
    """
    Abstract declarations may not be used to validate element content.
    (valid schema) Define an element within a substitution group
    headed by another element which is abstract. The elements
    have the same type. Try to substitute the head element
    with the first one. Try to use the head itself.
    """
    assert_bindings(
        schema="sunData/ElemDecl/abstract/abstract00101m/abstract00101m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/abstract/abstract00101m/abstract00101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_abstract00101m_abstract00101m1_n():
    """
    Abstract declarations may not be used to validate element content.
    (valid schema) Define an element within a substitution group
    headed by another element which is abstract. The elements
    have the same type. Try to substitute the head element
    with the first one. Try to use the head itself.
    """
    assert_bindings(
        schema="sunData/ElemDecl/abstract/abstract00101m/abstract00101m.xsd",
        is_valid=True,
        instance="sunData/ElemDecl/abstract/abstract00101m/abstract00101m1_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_targetns00101m1_positive():
    """
    Identity-constraint definition identities must be unique: different
    namespaces  (valid schema) Declare an element. Define a key identity
    constraint and a keyref to that key inside the
    element declaration. Declare another element with the same key and
    keyref.                              Check that if the second element
    declaration is in the same namespace,
    that the schema is invalid, otherwise it is valid.
    """
    assert_bindings(
        schema="sunData/IdConstrDefs/targetNS/targetNS00101m/targetNS00101m1.xsd",
        is_valid=True,
        instance="sunData/IdConstrDefs/targetNS/targetNS00101m/targetNS00101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_name00201m1_positive_597():
    """
    constraints have separate symbol space (valid schema) With the same
    name declare a global element, a local element, an attribute, define a
    type                               and a constraint. Check that there
    is no name clash.
    """
    assert_bindings(
        schema="sunData/IdConstrDefs/name/name00201m/name00201m1.xsd",
        is_valid=True,
        instance="sunData/IdConstrDefs/name/name00201m/name00201m1_p.xml",
        instance_is_valid=True,
        class_name="Name",
        version="1.0",
    )


def test_name00101m1_positive():
    """
    In one namespace Identity-constraint definition names must be unique:
    the names are KEY0 and KEY1  (valid schema) Declare an element. Define
    a key identity constraint.                               Define
    another key identity constraint with
    another name.                              Check that the schema is
    valid.
    """
    assert_bindings(
        schema="sunData/IdConstrDefs/name/name00101m/name00101m1.xsd",
        is_valid=True,
        instance="sunData/IdConstrDefs/name/name00101m/name00101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_fields00203m5_negative():
    """
    values of the fields are checked for equality:  string(3.0) compares
    with string(3.0) (valid schema) The equality and inequality conditions
    appealed to in checking these
    constraints apply to the value of the fields selected, so that for
    example                               3.0 and 3 would be conflicting
    keys if they were both number, but                               non-
    conflicting if they were both strings, or one was a string and
    one a number.                               In the test the fields
    have local type string and                              values "3.0"
    and "3.0".
    """
    assert_bindings(
        schema="sunData/IdConstrDefs/fields/fields00203m/fields00203m5.xsd",
        is_valid=True,
        instance="sunData/IdConstrDefs/fields/fields00203m/fields00203m5_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_fields00203m4_positive():
    """
    values of the fields are checked for equality:  string(3.0) compares
    with string(3) (valid schema) The equality and inequality conditions
    appealed to in checking these
    constraints apply to the value of the fields selected, so that for
    example                               3.0 and 3 would be conflicting
    keys if they were both number, but                               non-
    conflicting if they were both strings, or one was a string and
    one a number.                               In the test the fields
    have local type string and                              values "3.0"
    and "3".
    """
    assert_bindings(
        schema="sunData/IdConstrDefs/fields/fields00203m/fields00203m4.xsd",
        is_valid=True,
        instance="sunData/IdConstrDefs/fields/fields00203m/fields00203m4_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_fields00203m3_negative():
    """
    values of the fields are checked for equality:  decimal(3.0) compares
    with decimal(3.0) (valid schema) The equality and inequality
    conditions appealed to in checking these
    constraints apply to the value of the fields selected, so that for
    example                               3.0 and 3 would be conflicting
    keys if they were both number, but                               non-
    conflicting if they were both strings, or one was a string and
    one a number.                               In the test the fields
    have local type decimal and                              values "3.0"
    and "3.0".
    """
    assert_bindings(
        schema="sunData/IdConstrDefs/fields/fields00203m/fields00203m3.xsd",
        is_valid=True,
        instance="sunData/IdConstrDefs/fields/fields00203m/fields00203m3_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_fields00203m2_negative():
    """
    values of the fields are checked for equality:  decimal(3.0) compares
    with decimal(3) (valid schema) The equality and inequality conditions
    appealed to in checking these
    constraints apply to the value of the fields selected, so that for
    example                               3.0 and 3 would be conflicting
    keys if they were both number, but                               non-
    conflicting if they were both strings, or one was a string and
    one a number.                               In the test the fields
    have local type decimal and                              values "3.0"
    and "3".
    """
    assert_bindings(
        schema="sunData/IdConstrDefs/fields/fields00203m/fields00203m2.xsd",
        is_valid=True,
        instance="sunData/IdConstrDefs/fields/fields00203m/fields00203m2_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_fields00203m1_positive():
    """
    values of the fields are checked for equality:  decimal(3.0) compares
    with decimal(-3) (valid schema) The equality and inequality conditions
    appealed to in checking these
    constraints apply to the value of the fields selected, so that for
    example                               3.0 and 3 would be conflicting
    keys if they were both number, but                               non-
    conflicting if they were both strings, or one was a string and
    one a number.                               In the test the fields
    have local type decimal and                              values "3.0"
    and "-3".
    """
    assert_bindings(
        schema="sunData/IdConstrDefs/fields/fields00203m/fields00203m1.xsd",
        is_valid=True,
        instance="sunData/IdConstrDefs/fields/fields00203m/fields00203m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_fields00202m5_negative():
    """
    values of the fields are checked for equality:  string(3.0) compares
    with string(3.0) (valid schema) The equality and inequality conditions
    appealed to in checking these
    constraints apply to the value of the fields selected, so that for
    example                               3.0 and 3 would be conflicting
    keys if they were both number, but                               non-
    conflicting if they were both strings, or one was a string and
    one a number.                               In the test the first
    field of type string has value "3.0". The
    second field of type string has value "3.0".
    """
    assert_bindings(
        schema="sunData/IdConstrDefs/fields/fields00202m/fields00202m5.xsd",
        is_valid=True,
        instance="sunData/IdConstrDefs/fields/fields00202m/fields00202m5_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_fields00202m4_positive():
    """
    values of the fields are checked for equality:  string(3.0) compares
    with string(3) (valid schema) The equality and inequality conditions
    appealed to in checking these
    constraints apply to the value of the fields selected, so that for
    example                               3.0 and 3 would be conflicting
    keys if they were both number, but                               non-
    conflicting if they were both strings, or one was a string and
    one a number.                               In the test the first
    field of type string has value "3.0". The
    second field of type string has value "3".
    """
    assert_bindings(
        schema="sunData/IdConstrDefs/fields/fields00202m/fields00202m4.xsd",
        is_valid=True,
        instance="sunData/IdConstrDefs/fields/fields00202m/fields00202m4_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_fields00202m3_positive():
    """
    values of the fields are checked for equality:  string(3.0) compares
    with decimal(3.0) (valid schema) The equality and inequality
    conditions appealed to in checking these
    constraints apply to the value of the fields selected, so that for
    example                               3.0 and 3 would be conflicting
    keys if they were both number, but                               non-
    conflicting if they were both strings, or one was a string and
    one a number.                               In the test the first
    field of type string has value "3.0". The
    second field of type decimal has value "3.0".
    """
    assert_bindings(
        schema="sunData/IdConstrDefs/fields/fields00202m/fields00202m3.xsd",
        is_valid=True,
        instance="sunData/IdConstrDefs/fields/fields00202m/fields00202m3_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_fields00202m2_positive():
    """
    values of the fields are checked for equality:  string(3.0) compares
    with decimal(3) (valid schema) The equality and inequality conditions
    appealed to in checking these
    constraints apply to the value of the fields selected, so that for
    example                               3.0 and 3 would be conflicting
    keys if they were both number, but                               non-
    conflicting if they were both strings, or one was a string and
    one a number.                               In the test the first
    field of type string has value "3.0". The
    second field of type decimal has value "3".
    """
    assert_bindings(
        schema="sunData/IdConstrDefs/fields/fields00202m/fields00202m2.xsd",
        is_valid=True,
        instance="sunData/IdConstrDefs/fields/fields00202m/fields00202m2_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_fields00202m1_positive():
    """
    values of the fields are checked for equality:  string(3.0) compares
    with decimal(-3) (valid schema) The equality and inequality conditions
    appealed to in checking these
    constraints apply to the value of the fields selected, so that for
    example                               3.0 and 3 would be conflicting
    keys if they were both number, but                               non-
    conflicting if they were both strings, or one was a string and
    one a number.                               In the test the first
    field of type string has value "3.0". The
    second field of type decimal has value "-3".
    """
    assert_bindings(
        schema="sunData/IdConstrDefs/fields/fields00202m/fields00202m1.xsd",
        is_valid=True,
        instance="sunData/IdConstrDefs/fields/fields00202m/fields00202m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_fields00201m5_negative():
    """
    values of the fields are checked for equality:  type is string, values
    are 3.0 and 3.0 (valid schema) The equality and inequality conditions
    appealed to in checking these
    constraints apply to the value of the fields selected, so that for
    example                               3.0 and 3 would be conflicting
    keys if they were both number, but                               non-
    conflicting if they were both strings, or one was a string and
    one a number.                               In the test the fields of
    type string have values 3.0 and                               3.0.
    """
    assert_bindings(
        schema="sunData/IdConstrDefs/fields/fields00201m/fields00201m5.xsd",
        is_valid=True,
        instance="sunData/IdConstrDefs/fields/fields00201m/fields00201m5_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_fields00201m4_positive():
    """
    values of the fields are checked for equality:  type is string, values
    are 3.0 and 3 (valid schema) The equality and inequality conditions
    appealed to in checking these
    constraints apply to the value of the fields selected, so that for
    example                               3.0 and 3 would be conflicting
    keys if they were both number, but                               non-
    conflicting if they were both strings, or one was a string and
    one a number.                               In the test the fields of
    type string have values 3.0 and                               3.
    """
    assert_bindings(
        schema="sunData/IdConstrDefs/fields/fields00201m/fields00201m4.xsd",
        is_valid=True,
        instance="sunData/IdConstrDefs/fields/fields00201m/fields00201m4_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_fields00201m3_negative():
    """
    values of the fields are checked for equality:  type is decimal,
    values are 3.0 and 3.0 (valid schema) The equality and inequality
    conditions appealed to in checking these
    constraints apply to the value of the fields selected, so that for
    example                               3.0 and 3 would be conflicting
    keys if they were both number, but                               non-
    conflicting if they were both strings, or one was a string and
    one a number.                               In the test the fields of
    type decimal have values 3.0 and                               3.0.
    """
    assert_bindings(
        schema="sunData/IdConstrDefs/fields/fields00201m/fields00201m3.xsd",
        is_valid=True,
        instance="sunData/IdConstrDefs/fields/fields00201m/fields00201m3_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_fields00201m2_negative():
    """
    values of the fields are checked for equality:  type is decimal,
    values are 3.0 and 3 (valid schema) The equality and inequality
    conditions appealed to in checking these
    constraints apply to the value of the fields selected, so that for
    example                               3.0 and 3 would be conflicting
    keys if they were both number, but                               non-
    conflicting if they were both strings, or one was a string and
    one a number.                               In the test the fields of
    type decimal have values 3.0 and                               3.
    """
    assert_bindings(
        schema="sunData/IdConstrDefs/fields/fields00201m/fields00201m2.xsd",
        is_valid=True,
        instance="sunData/IdConstrDefs/fields/fields00201m/fields00201m2_n.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_fields00201m1_positive():
    """
    values of the fields are checked for equality:  type is decimal,
    values are 3.0 and -3 (valid schema) The equality and inequality
    conditions appealed to in checking these
    constraints apply to the value of the fields selected, so that for
    example                               3.0 and 3 would be conflicting
    keys if they were both number, but                               non-
    conflicting if they were both strings, or one was a string and
    one a number.                               In the test the fields of
    type decimal have values 3.0 and                               -3.
    """
    assert_bindings(
        schema="sunData/IdConstrDefs/fields/fields00201m/fields00201m1.xsd",
        is_valid=True,
        instance="sunData/IdConstrDefs/fields/fields00201m/fields00201m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_fields00101m1_positive():
    """
    fields may have different types (valid schema) Define a uniqueness
    constraint with fields of different types.
    """
    assert_bindings(
        schema="sunData/IdConstrDefs/fields/fields00101m/fields00101m1.xsd",
        is_valid=True,
        instance="sunData/IdConstrDefs/fields/fields00101m/fields00101m1_p.xml",
        instance_is_valid=True,
        class_name="People",
        version="1.0",
    )


def test_annotation00101m4_positive_615():
    """
    machine-targeted  annotation for an Identity-constraint Definition
    (valid schema) Annotations provide for human- and machine-targeted
    annotations of schema components.                               In the
    test the machine-targeted annotation                               is
    provided for an Identity-constraint Definition.
    """
    assert_bindings(
        schema="sunData/IdConstrDefs/annotation/annotation00101m/annotation00101m4.xsd",
        is_valid=True,
        instance="sunData/IdConstrDefs/annotation/annotation00101m/annotation00101m4_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_annotation00101m1_positive_616():
    """
    human-targeted  annotation for an Identity-constraint Definition
    (valid schema) Annotations provide for human- and machine-targeted
    annotations of schema components.                               In the
    test the human-targeted annotation                               is
    provided for an Identity-constraint Definition.
    """
    assert_bindings(
        schema="sunData/IdConstrDefs/annotation/annotation00101m/annotation00101m1.xsd",
        is_valid=True,
        instance="sunData/IdConstrDefs/annotation/annotation00101m/annotation00101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_particles00305m1_positive():
    """
    {particles}: 1 <any> (valid schema) The {particles} of 'sequence' must
    be one of <element>, <group>,                               <choice>,
    <sequence> <any>.
    """
    assert_bindings(
        schema="sunData/MGroup/particles/particles00305m/particles00305m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/particles/particles00305m/particles00305m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_particles00305m1_negative():
    """
    {particles}: 1 <any> (valid schema) The {particles} of 'sequence' must
    be one of <element>, <group>,                               <choice>,
    <sequence> <any>.
    """
    assert_bindings(
        schema="sunData/MGroup/particles/particles00305m/particles00305m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/particles/particles00305m/particles00305m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_particles00304m1_positive():
    """
    {particles}: 2 <sequence> (valid schema) The {particles} of 'sequence'
    must be one of <element>, <group>,
    <choice>, <sequence> <any>.
    """
    assert_bindings(
        schema="sunData/MGroup/particles/particles00304m/particles00304m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/particles/particles00304m/particles00304m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_particles00304m1_negative():
    """
    {particles}: 2 <sequence> (valid schema) The {particles} of 'sequence'
    must be one of <element>, <group>,
    <choice>, <sequence> <any>.
    """
    assert_bindings(
        schema="sunData/MGroup/particles/particles00304m/particles00304m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/particles/particles00304m/particles00304m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_particles00303m1_positive():
    """
    {particles}: 2 <choice> (valid schema) The {particles} of 'sequence'
    must be one of <element>, <group>,
    <choice>, <sequence> <any>.
    """
    assert_bindings(
        schema="sunData/MGroup/particles/particles00303m/particles00303m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/particles/particles00303m/particles00303m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_particles00303m1_negative():
    """
    {particles}: 2 <choice> (valid schema) The {particles} of 'sequence'
    must be one of <element>, <group>,
    <choice>, <sequence> <any>.
    """
    assert_bindings(
        schema="sunData/MGroup/particles/particles00303m/particles00303m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/particles/particles00303m/particles00303m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


@pytest.mark.xfail
def test_particles00302m1_positive():
    """
    {particles}: 2 <group> (valid schema) The {particles} of 'sequence'
    must be one of <element>, <group>,
    <choice>, <sequence> <any>.
    """
    assert_bindings(
        schema="sunData/MGroup/particles/particles00302m/particles00302m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/particles/particles00302m/particles00302m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_particles00302m1_negative():
    """
    {particles}: 2 <group> (valid schema) The {particles} of 'sequence'
    must be one of <element>, <group>,
    <choice>, <sequence> <any>.
    """
    assert_bindings(
        schema="sunData/MGroup/particles/particles00302m/particles00302m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/particles/particles00302m/particles00302m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_particles00301m1_positive():
    """
    {particles}: 2 <element> (valid schema) The {particles} of 'sequence'
    must be one of <element>, <group>,
    <choice>, <sequence> <any>.
    """
    assert_bindings(
        schema="sunData/MGroup/particles/particles00301m/particles00301m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/particles/particles00301m/particles00301m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_particles00301m1_negative():
    """
    {particles}: 2 <element> (valid schema) The {particles} of 'sequence'
    must be one of <element>, <group>,
    <choice>, <sequence> <any>.
    """
    assert_bindings(
        schema="sunData/MGroup/particles/particles00301m/particles00301m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/particles/particles00301m/particles00301m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_particles00205m1_positive():
    """
    {particles}: 1 <any> (valid schema) The {particles} of 'choice' must
    be one of <element>, <group>,                               <choice>,
    <sequence> <any>.
    """
    assert_bindings(
        schema="sunData/MGroup/particles/particles00205m/particles00205m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/particles/particles00205m/particles00205m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_particles00205m1_negative():
    """
    {particles}: 1 <any> (valid schema) The {particles} of 'choice' must
    be one of <element>, <group>,                               <choice>,
    <sequence> <any>.
    """
    assert_bindings(
        schema="sunData/MGroup/particles/particles00205m/particles00205m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/particles/particles00205m/particles00205m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_particles00204m1_positive():
    """
    {particles}: 2 <sequence> (valid schema) The {particles} of 'choice'
    must be one of <element>, <group>,
    <choice>, <sequence> <any>.
    """
    assert_bindings(
        schema="sunData/MGroup/particles/particles00204m/particles00204m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/particles/particles00204m/particles00204m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_particles00204m1_negative():
    """
    {particles}: 2 <sequence> (valid schema) The {particles} of 'choice'
    must be one of <element>, <group>,
    <choice>, <sequence> <any>.
    """
    assert_bindings(
        schema="sunData/MGroup/particles/particles00204m/particles00204m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/particles/particles00204m/particles00204m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_particles00203m1_positive():
    """
    {particles}: 2 <choice> (valid schema) The {particles} of 'choice'
    must be one of <element>, <group>,
    <choice>, <sequence> <any>.
    """
    assert_bindings(
        schema="sunData/MGroup/particles/particles00203m/particles00203m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/particles/particles00203m/particles00203m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_particles00203m1_negative():
    """
    {particles}: 2 <choice> (valid schema) The {particles} of 'choice'
    must be one of <element>, <group>,
    <choice>, <sequence> <any>.
    """
    assert_bindings(
        schema="sunData/MGroup/particles/particles00203m/particles00203m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/particles/particles00203m/particles00203m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_particles00202m1_positive():
    """
    {particles}: 2 <group> (valid schema) The {particles} of 'choice' must
    be one of <element>, <group>,                               <choice>,
    <sequence> <any>.
    """
    assert_bindings(
        schema="sunData/MGroup/particles/particles00202m/particles00202m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/particles/particles00202m/particles00202m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_particles00202m1_negative():
    """
    {particles}: 2 <group> (valid schema) The {particles} of 'choice' must
    be one of <element>, <group>,                               <choice>,
    <sequence> <any>.
    """
    assert_bindings(
        schema="sunData/MGroup/particles/particles00202m/particles00202m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/particles/particles00202m/particles00202m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_particles00201m1_positive():
    """
    {particles}: 2 <element> (valid schema) The {particles} of 'choice'
    must be one of <element>, <group>,
    <choice>, <sequence> <any>.
    """
    assert_bindings(
        schema="sunData/MGroup/particles/particles00201m/particles00201m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/particles/particles00201m/particles00201m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_particles00201m1_negative():
    """
    {particles}: 2 <element> (valid schema) The {particles} of 'choice'
    must be one of <element>, <group>,
    <choice>, <sequence> <any>.
    """
    assert_bindings(
        schema="sunData/MGroup/particles/particles00201m/particles00201m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/particles/particles00201m/particles00201m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_particles00101m2_positive():
    """
    {particles}: 2 <element> (valid schema) The {particles} of 'all' must
    be <element>.
    """
    assert_bindings(
        schema="sunData/MGroup/particles/particles00101m/particles00101m2.xsd",
        is_valid=True,
        instance="sunData/MGroup/particles/particles00101m/particles00101m2_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_particles00101m2_negative():
    """
    {particles}: 2 <element> (valid schema) The {particles} of 'all' must
    be <element>.
    """
    assert_bindings(
        schema="sunData/MGroup/particles/particles00101m/particles00101m2.xsd",
        is_valid=True,
        instance="sunData/MGroup/particles/particles00101m/particles00101m2_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_particles00101m1_positive():
    """
    {particles}: 1 <element> (valid schema) The {particles} of 'all' must
    be <element>.
    """
    assert_bindings(
        schema="sunData/MGroup/particles/particles00101m/particles00101m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/particles/particles00101m/particles00101m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_particles00101m1_negative():
    """
    {particles}: 1 <element> (valid schema) The {particles} of 'all' must
    be <element>.
    """
    assert_bindings(
        schema="sunData/MGroup/particles/particles00101m/particles00101m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/particles/particles00101m/particles00101m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_compositor00203m1_positive():
    """
    An empty all (valid schema) The XMLSchema specification allows an
    empty all.
    """
    assert_bindings(
        schema="sunData/MGroup/compositor/compositor00203m/compositor00203m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/compositor/compositor00203m/compositor00203m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_compositor00202m1_positive():
    """
    An empty choice (valid schema) The XMLSchema specification allows an
    empty choice.
    """
    assert_bindings(
        schema="sunData/MGroup/compositor/compositor00202m/compositor00202m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/compositor/compositor00202m/compositor00202m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_compositor00201m1_positive():
    """
    An empty sequence (valid schema) The XMLSchema specification allows an
    empty sequence.
    """
    assert_bindings(
        schema="sunData/MGroup/compositor/compositor00201m/compositor00201m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/compositor/compositor00201m/compositor00201m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_compositor00103m1_positive():
    """
    The {compositor} is all, {particles} are element declarations (valid
    schema) Validation Rule: Element Sequence Valid case #3
    """
    assert_bindings(
        schema="sunData/MGroup/compositor/compositor00103m/compositor00103m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/compositor/compositor00103m/compositor00103m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_compositor00103m1_negative():
    """
    The {compositor} is all, {particles} are element declarations (valid
    schema) Validation Rule: Element Sequence Valid case #3
    """
    assert_bindings(
        schema="sunData/MGroup/compositor/compositor00103m/compositor00103m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/compositor/compositor00103m/compositor00103m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_compositor00102m1_positive():
    """
    The {compositor} is choice, {particles} are element declarations
    (valid schema) Validation Rule: Element Sequence Valid case #2
    """
    assert_bindings(
        schema="sunData/MGroup/compositor/compositor00102m/compositor00102m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/compositor/compositor00102m/compositor00102m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_compositor00102m1_negative():
    """
    The {compositor} is choice, {particles} are element declarations
    (valid schema) Validation Rule: Element Sequence Valid case #2
    """
    assert_bindings(
        schema="sunData/MGroup/compositor/compositor00102m/compositor00102m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/compositor/compositor00102m/compositor00102m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_compositor00101m1_positive():
    """
    The {compositor} is <sequence> of 3 elements, {particles} are element
    declarations (valid schema) Validation Rule: Element Sequence Valid
    case #1
    """
    assert_bindings(
        schema="sunData/MGroup/compositor/compositor00101m/compositor00101m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/compositor/compositor00101m/compositor00101m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_compositor00101m1_negative():
    """
    The {compositor} is <sequence> of 3 elements, {particles} are element
    declarations (valid schema) Validation Rule: Element Sequence Valid
    case #1
    """
    assert_bindings(
        schema="sunData/MGroup/compositor/compositor00101m/compositor00101m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/compositor/compositor00101m/compositor00101m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_annotation00101m7_positive():
    """
    human-targeted  annotation for a model group schema component (choice)
    (valid schema) Annotations provide for human- and machine-targeted
    annotations of schema components.                               In the
    test the human-targeted annotation                               is
    provided for a model group schema component (choice).
    """
    assert_bindings(
        schema="sunData/MGroup/annotation/annotation00101m/annotation00101m7.xsd",
        is_valid=True,
        instance="sunData/MGroup/annotation/annotation00101m/annotation00101m7_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_annotation00101m4_positive_651():
    """
    machine-targeted  annotation for a model group schema component (all)
    (valid schema) Annotations provide for human- and machine-targeted
    annotations of schema components.                               In the
    test the machine-targeted annotation                               is
    provided for a model group schema component (all).
    """
    assert_bindings(
        schema="sunData/MGroup/annotation/annotation00101m/annotation00101m4.xsd",
        is_valid=True,
        instance="sunData/MGroup/annotation/annotation00101m/annotation00101m4_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_annotation00101m16_positive():
    """
    machine-targeted  annotation for a model group schema component
    (sequence) (valid schema) Annotations provide for human- and machine-
    targeted                               annotations of schema
    components.                               In the test the machine-
    targeted annotation                               is provided for a
    model group schema component (sequence).
    """
    assert_bindings(
        schema="sunData/MGroup/annotation/annotation00101m/annotation00101m16.xsd",
        is_valid=True,
        instance="sunData/MGroup/annotation/annotation00101m/annotation00101m16_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_annotation00101m13_positive():
    """
    human-targeted  annotation for a model group schema component
    (sequence) (valid schema) Annotations provide for human- and machine-
    targeted                               annotations of schema
    components.                               In the test the human-
    targeted annotation                               is provided for a
    model group schema component (sequence).
    """
    assert_bindings(
        schema="sunData/MGroup/annotation/annotation00101m/annotation00101m13.xsd",
        is_valid=True,
        instance="sunData/MGroup/annotation/annotation00101m/annotation00101m13_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_annotation00101m10_positive():
    """
    machine-targeted  annotation for a model group schema component
    (choice) (valid schema) Annotations provide for human- and machine-
    targeted                               annotations of schema
    components.                               In the test the machine-
    targeted annotation                               is provided for a
    model group schema component (choice).
    """
    assert_bindings(
        schema="sunData/MGroup/annotation/annotation00101m/annotation00101m10.xsd",
        is_valid=True,
        instance="sunData/MGroup/annotation/annotation00101m/annotation00101m10_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_annotation00101m1_positive_655():
    """
    human-targeted  annotation for a model group schema component (all)
    (valid schema) Annotations provide for human- and machine-targeted
    annotations of schema components.                               In the
    test the human-targeted annotation                               is
    provided for a model group schema component (all).
    """
    assert_bindings(
        schema="sunData/MGroup/annotation/annotation00101m/annotation00101m1.xsd",
        is_valid=True,
        instance="sunData/MGroup/annotation/annotation00101m/annotation00101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_targetns00101m2_positive():
    """
    Use the model group definition defined in other namespace (valid
    schema) Model group definitions are identified by their {name} and
    {target namespace};                               model group
    identities must be unique within an *XML Schema*.
    """
    assert_bindings(
        schema="sunData/MGroupDef/targetNS/targetNS00101m/targetNS00101m2.xsd",
        is_valid=True,
        instance="sunData/MGroupDef/targetNS/targetNS00101m/targetNS00101m2_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_targetns00101m2_negative():
    """
    Use the model group definition defined in other namespace (valid
    schema) Model group definitions are identified by their {name} and
    {target namespace};                               model group
    identities must be unique within an *XML Schema*.
    """
    assert_bindings(
        schema="sunData/MGroupDef/targetNS/targetNS00101m/targetNS00101m2.xsd",
        is_valid=True,
        instance="sunData/MGroupDef/targetNS/targetNS00101m/targetNS00101m2_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_targetns00101m1_positive_658():
    """
    The auxiliary schema for targetNS00101m2.xsd (valid schema) Model
    group definitions are identified by their {name} and {target
    namespace};                               model group identities must
    be unique within an *XML Schema*.
    """
    assert_bindings(
        schema="sunData/MGroupDef/targetNS/targetNS00101m/targetNS00101m1.xsd",
        is_valid=True,
        instance="sunData/MGroupDef/targetNS/targetNS00101m/targetNS00101m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_targetns00101m1_negative():
    """
    The auxiliary schema for targetNS00101m2.xsd (valid schema) Model
    group definitions are identified by their {name} and {target
    namespace};                               model group identities must
    be unique within an *XML Schema*.
    """
    assert_bindings(
        schema="sunData/MGroupDef/targetNS/targetNS00101m/targetNS00101m1.xsd",
        is_valid=True,
        instance="sunData/MGroupDef/targetNS/targetNS00101m/targetNS00101m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_name00101m1_positive_660():
    """
    Identify a model group definition by name (valid schema) Model group
    definitions are identified by their {name} and {target namespace};
    model group identities must be unique within an *XML Schema*.
    """
    assert_bindings(
        schema="sunData/MGroupDef/name/name00101m/name00101m1.xsd",
        is_valid=True,
        instance="sunData/MGroupDef/name/name00101m/name00101m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_name00101m1_negative():
    """
    Identify a model group definition by name (valid schema) Model group
    definitions are identified by their {name} and {target namespace};
    model group identities must be unique within an *XML Schema*.
    """
    assert_bindings(
        schema="sunData/MGroupDef/name/name00101m/name00101m1.xsd",
        is_valid=True,
        instance="sunData/MGroupDef/name/name00101m/name00101m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_modelgroup00101m3_positive():
    """
    A model group is <sequence> (valid schema) A model group which is the
    {term} of a particle corresponding to the <all>,
    <choice> or <sequence> among the [children].
    """
    assert_bindings(
        schema="sunData/MGroupDef/modelGroup/modelGroup00101m/modelGroup00101m3.xsd",
        is_valid=True,
        instance="sunData/MGroupDef/modelGroup/modelGroup00101m/modelGroup00101m3_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_modelgroup00101m3_negative():
    """
    A model group is <sequence> (valid schema) A model group which is the
    {term} of a particle corresponding to the <all>,
    <choice> or <sequence> among the [children].
    """
    assert_bindings(
        schema="sunData/MGroupDef/modelGroup/modelGroup00101m/modelGroup00101m3.xsd",
        is_valid=True,
        instance="sunData/MGroupDef/modelGroup/modelGroup00101m/modelGroup00101m3_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_modelgroup00101m2_positive():
    """
    A model group is <choice> (valid schema) A model group which is the
    {term} of a particle corresponding to the <all>,
    <choice> or <sequence> among the [children].
    """
    assert_bindings(
        schema="sunData/MGroupDef/modelGroup/modelGroup00101m/modelGroup00101m2.xsd",
        is_valid=True,
        instance="sunData/MGroupDef/modelGroup/modelGroup00101m/modelGroup00101m2_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_modelgroup00101m2_negative():
    """
    A model group is <choice> (valid schema) A model group which is the
    {term} of a particle corresponding to the <all>,
    <choice> or <sequence> among the [children].
    """
    assert_bindings(
        schema="sunData/MGroupDef/modelGroup/modelGroup00101m/modelGroup00101m2.xsd",
        is_valid=True,
        instance="sunData/MGroupDef/modelGroup/modelGroup00101m/modelGroup00101m2_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_modelgroup00101m1_positive():
    """
    A model group is <all> (valid schema) A model group which is the
    {term} of a particle corresponding to the <all>,
    <choice> or <sequence> among the [children].
    """
    assert_bindings(
        schema="sunData/MGroupDef/modelGroup/modelGroup00101m/modelGroup00101m1.xsd",
        is_valid=True,
        instance="sunData/MGroupDef/modelGroup/modelGroup00101m/modelGroup00101m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_modelgroup00101m1_negative():
    """
    A model group is <all> (valid schema) A model group which is the
    {term} of a particle corresponding to the <all>,
    <choice> or <sequence> among the [children].
    """
    assert_bindings(
        schema="sunData/MGroupDef/modelGroup/modelGroup00101m/modelGroup00101m1.xsd",
        is_valid=True,
        instance="sunData/MGroupDef/modelGroup/modelGroup00101m/modelGroup00101m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_annotation00101m4_positive_668():
    """
    machine-targeted  annotation for a model group definition (valid
    schema) Annotations provide for human- and machine-targeted
    annotations of schema components.                               In the
    test the machine-targeted annotation                               is
    provided for a model group definition.
    """
    assert_bindings(
        schema="sunData/MGroupDef/annotation/annotation00101m/annotation00101m4.xsd",
        is_valid=True,
        instance="sunData/MGroupDef/annotation/annotation00101m/annotation00101m4_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_annotation00101m1_positive_669():
    """
    human-targeted  annotation for a model group definition (valid schema)
    Annotations provide for human- and machine-targeted
    annotations of schema components.                               In the
    test the human-targeted annotation                               is
    provided for a model group definition.
    """
    assert_bindings(
        schema="sunData/MGroupDef/annotation/annotation00101m/annotation00101m1.xsd",
        is_valid=True,
        instance="sunData/MGroupDef/annotation/annotation00101m/annotation00101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_targetns00101m2_positive_670():
    """
    Use of the notation declared in the namespace 'tck_test' (valid
    schema) Notation declarations are referenced in the course of
    *validating* strings as                               members of the
    NOTATION simple type.
    """
    assert_bindings(
        schema="sunData/Notation/targetNS/targetNS00101m/targetNS00101m2.xsd",
        is_valid=True,
        instance="sunData/Notation/targetNS/targetNS00101m/targetNS00101m2_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_targetns00101m1_positive_671():
    """
    Declaration of the notation with the name 'png' and the namespace
    'tck_test' (valid schema) The property {name} is represented as the
    value of the name [attribute].
    """
    assert_bindings(
        schema="sunData/Notation/targetNS/targetNS00101m/targetNS00101m1.xsd",
        is_valid=True,
        instance="sunData/Notation/targetNS/targetNS00101m/targetNS00101m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_systemid00201m1_positive():
    """
    Declare a notation without the {system identifier} (valid schema) The
    property {system identifier} is optional.
    """
    assert_bindings(
        schema="sunData/Notation/systemId/systemId00201m/systemId00201m1.xsd",
        is_valid=True,
        instance="sunData/Notation/systemId/systemId00201m/systemId00201m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_systemid00101m1_positive():
    """
    Declare a notation with the {system identifier} 'sdtimage' (valid
    schema) The property {system identifier} is represented as the actual
    value of                               the system [attribute].
    """
    assert_bindings(
        schema="sunData/Notation/systemId/systemId00101m/systemId00101m1.xsd",
        is_valid=True,
        instance="sunData/Notation/systemId/systemId00101m/systemId00101m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_publicid00101m1_positive():
    """
    Declare a notation with the {public identifier} 'image/png' (valid
    schema) The property {public identifier} is represented as the actual
    value of                               the public [attribute].
    """
    assert_bindings(
        schema="sunData/Notation/publicId/publicId00101m/publicId00101m1.xsd",
        is_valid=True,
        instance="sunData/Notation/publicId/publicId00101m/publicId00101m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_name00101m1_positive_675():
    """
    Use the declared notation with the name 'png' (valid schema) Notation
    declarations are referenced in the course of *validating* strings as
    members of the NOTATION simple type. A schema is invalid if it is
    contain a                               referebce to undeclared
    notation.
    """
    assert_bindings(
        schema="sunData/Notation/name/name00101m/name00101m1.xsd",
        is_valid=True,
        instance="sunData/Notation/name/name00101m/name00101m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_annotation00101m3_positive_676():
    """
    machine-targeted  annotation for a notation declaration (valid schema)
    Annotations provide for human- and machine-targeted
    annotations of schema components.                               In the
    test the machine-targeted annotation                               is
    provided for a notation declaration.
    """
    assert_bindings(
        schema="sunData/Notation/annotation/annotation00101m/annotation00101m3.xsd",
        is_valid=True,
        instance="sunData/Notation/annotation/annotation00101m/annotation00101m3_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_annotation00101m1_positive_677():
    """
    human-targeted  annotation for a notation declaration (valid schema)
    Annotations provide for human- and machine-targeted
    annotations of schema components.                               In the
    test the human-targeted annotation                               is
    provided for a notation declaration.
    """
    assert_bindings(
        schema="sunData/Notation/annotation/annotation00101m/annotation00101m1.xsd",
        is_valid=True,
        instance="sunData/Notation/annotation/annotation00101m/annotation00101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_variety00101m2_positive():
    """
    The {variety} is atomic (valid schema) If the {variety} is atomic,
    then all of the following must be true:
    1. The {base type definition} must be an atomic simple type definition
    or a built-in primitive datatype.                                 2.
    The {final} of the {base type definition} must not contain
    restriction.                                  3. For each facet in the
    {facets} there must be a facet of the same kind
    in the {facets} of the {base type definition} of whose {value} the
    facet                                    in question's {value} must be
    a valid restriction as defined in
    [XML Schemas: Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_variety/ST_variety00101m/ST_variety00101m2.xsd",
        is_valid=True,
        instance="sunData/SType/ST_variety/ST_variety00101m/ST_variety00101m2_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_variety00101m2_negative():
    """
    The {variety} is atomic (valid schema) If the {variety} is atomic,
    then all of the following must be true:
    1. The {base type definition} must be an atomic simple type definition
    or a built-in primitive datatype.                                 2.
    The {final} of the {base type definition} must not contain
    restriction.                                  3. For each facet in the
    {facets} there must be a facet of the same kind
    in the {facets} of the {base type definition} of whose {value} the
    facet                                    in question's {value} must be
    a valid restriction as defined in
    [XML Schemas: Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_variety/ST_variety00101m/ST_variety00101m2.xsd",
        is_valid=True,
        instance="sunData/SType/ST_variety/ST_variety00101m/ST_variety00101m2_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_variety00101m1_positive():
    """
    The {variety} is atomic (valid schema) If the {variety} is atomic,
    then all of the following must be true:
    1. The {base type definition} must be an atomic simple type definition
    or a built-in primitive datatype.                                 2.
    The {final} of the {base type definition} must not contain
    restriction.                                  3. For each facet in the
    {facets} there must be a facet of the same kind
    in the {facets} of the {base type definition} of whose {value} the
    facet                                    in question's {value} must be
    a valid restriction as defined in
    [XML Schemas: Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_variety/ST_variety00101m/ST_variety00101m1.xsd",
        is_valid=True,
        instance="sunData/SType/ST_variety/ST_variety00101m/ST_variety00101m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_variety00101m1_negative():
    """
    The {variety} is atomic (valid schema) If the {variety} is atomic,
    then all of the following must be true:
    1. The {base type definition} must be an atomic simple type definition
    or a built-in primitive datatype.                                 2.
    The {final} of the {base type definition} must not contain
    restriction.                                  3. For each facet in the
    {facets} there must be a facet of the same kind
    in the {facets} of the {base type definition} of whose {value} the
    facet                                    in question's {value} must be
    a valid restriction as defined in
    [XML Schemas: Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_variety/ST_variety00101m/ST_variety00101m1.xsd",
        is_valid=True,
        instance="sunData/SType/ST_variety/ST_variety00101m/ST_variety00101m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


@pytest.mark.xfail
def test_st_targetns00201m_st_target_ns00201m1_p():
    """
    reference to type (valid schema) Simple type {name}s and {target
    namespace}s are provided for reference from instances.
    """
    assert_bindings(
        schema="sunData/SType/ST_targetNS/ST_targetNS00201m/ST_targetNS00201m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_targetNS/ST_targetNS00201m/ST_targetNS00201m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


@pytest.mark.xfail
def test_st_targetns00101m_st_target_ns00101m1_p():
    """
    Identify the type by their {name} and {target namespace} (valid
    schema) Simple types are identified by their {name} and {target
    namespace}.
    """
    assert_bindings(
        schema="sunData/SType/ST_targetNS/ST_targetNS00101m/ST_targetNS00101m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_targetNS/ST_targetNS00101m/ST_targetNS00101m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


@pytest.mark.xfail
def test_st_targetns00101m_st_target_ns00101m1_n():
    """
    Identify the type by their {name} and {target namespace} (valid
    schema) Simple types are identified by their {name} and {target
    namespace}.
    """
    assert_bindings(
        schema="sunData/SType/ST_targetNS/ST_targetNS00101m/ST_targetNS00101m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_targetNS/ST_targetNS00101m/ST_targetNS00101m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


@pytest.mark.xfail
def test_st_targetns00101m_st_target_ns00101m2_p():
    """
    Identify the type by their {name} and {target namespace} (valid
    schema) Simple types are identified by their {name} and {target
    namespace}.
    """
    assert_bindings(
        schema="sunData/SType/ST_targetNS/ST_targetNS00101m/ST_targetNS00101m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_targetNS/ST_targetNS00101m/ST_targetNS00101m2_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


@pytest.mark.xfail
def test_st_targetns00101m_st_target_ns00101m2_n():
    """
    Identify the type by their {name} and {target namespace} (valid
    schema) Simple types are identified by their {name} and {target
    namespace}.
    """
    assert_bindings(
        schema="sunData/SType/ST_targetNS/ST_targetNS00101m/ST_targetNS00101m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_targetNS/ST_targetNS00101m/ST_targetNS00101m2_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


@pytest.mark.xfail
def test_st_name00401m_st_name00401m1_p():
    """
    Simple type {name}s is provided for reference (valid schema) Simple
    type {name}s is provided for reference from instances.
    """
    assert_bindings(
        schema="sunData/SType/ST_name/ST_name00401m/ST_name00401m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_name/ST_name00401m/ST_name00401m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_name00101m_st_name00101m1_p():
    """
    Simple types are identified by their {name} and {target namespace}.
    (valid schema) Simple types are identified by their {name} and {target
    namespace}.
    """
    assert_bindings(
        schema="sunData/SType/ST_name/ST_name00101m/ST_name00101m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_name/ST_name00101m/ST_name00101m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_name00101m_st_name00101m1_n():
    """
    Simple types are identified by their {name} and {target namespace}.
    (valid schema) Simple types are identified by their {name} and {target
    namespace}.
    """
    assert_bindings(
        schema="sunData/SType/ST_name/ST_name00101m/ST_name00101m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_name/ST_name00101m/ST_name00101m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_final00103m3_positive():
    """
    derivation by list (valid schema) The explicit value union prevents
    further use in constructing unions.
    """
    assert_bindings(
        schema="sunData/SType/ST_final/ST_final00103m/ST_final00103m3.xsd",
        is_valid=True,
        instance="sunData/SType/ST_final/ST_final00103m/ST_final00103m3_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_final00103m3_negative():
    """
    derivation by list (valid schema) The explicit value union prevents
    further use in constructing unions.
    """
    assert_bindings(
        schema="sunData/SType/ST_final/ST_final00103m/ST_final00103m3.xsd",
        is_valid=True,
        instance="sunData/SType/ST_final/ST_final00103m/ST_final00103m3_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_final00103m2_positive():
    """
    derivation by restriction (valid schema) The explicit value union
    prevents further use in constructing unions.
    """
    assert_bindings(
        schema="sunData/SType/ST_final/ST_final00103m/ST_final00103m2.xsd",
        is_valid=True,
        instance="sunData/SType/ST_final/ST_final00103m/ST_final00103m2_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_final00103m2_negative():
    """
    derivation by restriction (valid schema) The explicit value union
    prevents further use in constructing unions.
    """
    assert_bindings(
        schema="sunData/SType/ST_final/ST_final00103m/ST_final00103m2.xsd",
        is_valid=True,
        instance="sunData/SType/ST_final/ST_final00103m/ST_final00103m2_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_final00102m6_positive():
    """
    derivation by union (valid schema) The explicit value list prevents
    further use in constructing lists.
    """
    assert_bindings(
        schema="sunData/SType/ST_final/ST_final00102m/ST_final00102m6.xsd",
        is_valid=True,
        instance="sunData/SType/ST_final/ST_final00102m/ST_final00102m6_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_final00102m6_negative():
    """
    derivation by union (valid schema) The explicit value list prevents
    further use in constructing lists.
    """
    assert_bindings(
        schema="sunData/SType/ST_final/ST_final00102m/ST_final00102m6.xsd",
        is_valid=True,
        instance="sunData/SType/ST_final/ST_final00102m/ST_final00102m6_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_final00102m5_positive():
    """
    derivation by union (valid schema) The explicit value list prevents
    further use in constructing lists.
    """
    assert_bindings(
        schema="sunData/SType/ST_final/ST_final00102m/ST_final00102m5.xsd",
        is_valid=True,
        instance="sunData/SType/ST_final/ST_final00102m/ST_final00102m5_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_final00102m5_negative():
    """
    derivation by union (valid schema) The explicit value list prevents
    further use in constructing lists.
    """
    assert_bindings(
        schema="sunData/SType/ST_final/ST_final00102m/ST_final00102m5.xsd",
        is_valid=True,
        instance="sunData/SType/ST_final/ST_final00102m/ST_final00102m5_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_final00102m4_positive():
    """
    derivation by union (valid schema) The explicit value list prevents
    further use in constructing lists.
    """
    assert_bindings(
        schema="sunData/SType/ST_final/ST_final00102m/ST_final00102m4.xsd",
        is_valid=True,
        instance="sunData/SType/ST_final/ST_final00102m/ST_final00102m4_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_final00102m4_negative():
    """
    derivation by union (valid schema) The explicit value list prevents
    further use in constructing lists.
    """
    assert_bindings(
        schema="sunData/SType/ST_final/ST_final00102m/ST_final00102m4.xsd",
        is_valid=True,
        instance="sunData/SType/ST_final/ST_final00102m/ST_final00102m4_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_final00102m3_positive():
    """
    derivation by union (valid schema) The explicit value list prevents
    further use in constructing lists.
    """
    assert_bindings(
        schema="sunData/SType/ST_final/ST_final00102m/ST_final00102m3.xsd",
        is_valid=True,
        instance="sunData/SType/ST_final/ST_final00102m/ST_final00102m3_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_final00102m3_negative():
    """
    derivation by union (valid schema) The explicit value list prevents
    further use in constructing lists.
    """
    assert_bindings(
        schema="sunData/SType/ST_final/ST_final00102m/ST_final00102m3.xsd",
        is_valid=True,
        instance="sunData/SType/ST_final/ST_final00102m/ST_final00102m3_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_final00102m2_positive():
    """
    derivation by restriction (valid schema) The explicit value list
    prevents further use in constructing lists.
    """
    assert_bindings(
        schema="sunData/SType/ST_final/ST_final00102m/ST_final00102m2.xsd",
        is_valid=True,
        instance="sunData/SType/ST_final/ST_final00102m/ST_final00102m2_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_final00102m2_negative():
    """
    derivation by restriction (valid schema) The explicit value list
    prevents further use in constructing lists.
    """
    assert_bindings(
        schema="sunData/SType/ST_final/ST_final00102m/ST_final00102m2.xsd",
        is_valid=True,
        instance="sunData/SType/ST_final/ST_final00102m/ST_final00102m2_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_final00101m6_positive():
    """
    derivation by union (valid schema) The explicit value restriction
    prevents further derivations by restriction (to yield a simple type).
    """
    assert_bindings(
        schema="sunData/SType/ST_final/ST_final00101m/ST_final00101m6.xsd",
        is_valid=True,
        instance="sunData/SType/ST_final/ST_final00101m/ST_final00101m6_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_final00101m6_negative():
    """
    derivation by union (valid schema) The explicit value restriction
    prevents further derivations by restriction (to yield a simple type).
    """
    assert_bindings(
        schema="sunData/SType/ST_final/ST_final00101m/ST_final00101m6.xsd",
        is_valid=True,
        instance="sunData/SType/ST_final/ST_final00101m/ST_final00101m6_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_final00101m5_positive():
    """
    derivation by union (valid schema) The explicit value restriction
    prevents further derivations by restriction (to yield a simple type).
    """
    assert_bindings(
        schema="sunData/SType/ST_final/ST_final00101m/ST_final00101m5.xsd",
        is_valid=True,
        instance="sunData/SType/ST_final/ST_final00101m/ST_final00101m5_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_final00101m5_negative():
    """
    derivation by union (valid schema) The explicit value restriction
    prevents further derivations by restriction (to yield a simple type).
    """
    assert_bindings(
        schema="sunData/SType/ST_final/ST_final00101m/ST_final00101m5.xsd",
        is_valid=True,
        instance="sunData/SType/ST_final/ST_final00101m/ST_final00101m5_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_final00101m4_positive():
    """
    derivation by union (valid schema) The explicit value restriction
    prevents further derivations by restriction (to yield a simple type).
    """
    assert_bindings(
        schema="sunData/SType/ST_final/ST_final00101m/ST_final00101m4.xsd",
        is_valid=True,
        instance="sunData/SType/ST_final/ST_final00101m/ST_final00101m4_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_final00101m4_negative():
    """
    derivation by union (valid schema) The explicit value restriction
    prevents further derivations by restriction (to yield a simple type).
    """
    assert_bindings(
        schema="sunData/SType/ST_final/ST_final00101m/ST_final00101m4.xsd",
        is_valid=True,
        instance="sunData/SType/ST_final/ST_final00101m/ST_final00101m4_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_final00101m3_positive():
    """
    derivation by union (valid schema) The explicit value restriction
    prevents further derivations by restriction (to yield a simple type).
    """
    assert_bindings(
        schema="sunData/SType/ST_final/ST_final00101m/ST_final00101m3.xsd",
        is_valid=True,
        instance="sunData/SType/ST_final/ST_final00101m/ST_final00101m3_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_final00101m3_negative():
    """
    derivation by union (valid schema) The explicit value restriction
    prevents further derivations by restriction (to yield a simple type).
    """
    assert_bindings(
        schema="sunData/SType/ST_final/ST_final00101m/ST_final00101m3.xsd",
        is_valid=True,
        instance="sunData/SType/ST_final/ST_final00101m/ST_final00101m3_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_final00101m2_positive():
    """
    derivation by list (valid schema) The explicit value restriction
    prevents further derivations by restriction (to yield a simple type).
    """
    assert_bindings(
        schema="sunData/SType/ST_final/ST_final00101m/ST_final00101m2.xsd",
        is_valid=True,
        instance="sunData/SType/ST_final/ST_final00101m/ST_final00101m2_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_final00101m2_negative():
    """
    derivation by list (valid schema) The explicit value restriction
    prevents further derivations by restriction (to yield a simple type).
    """
    assert_bindings(
        schema="sunData/SType/ST_final/ST_final00101m/ST_final00101m2.xsd",
        is_valid=True,
        instance="sunData/SType/ST_final/ST_final00101m/ST_final00101m2_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00608_st_facets00608_p():
    """
    Enumeration values contain an uncased letter followed by upper or
    lower case letter. (valid schema) Declare a simple type based on
    NCName and restricted with enumeration
    values that contain one Unicode letter #x01BB which is neither upper
    nor lower.
    The document ST_facets00608_p.xml uses all the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00608/ST_facets00608.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00608/ST_facets00608_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00605_st_facets00605_p():
    """
    Enumeration values contain only punctuation characters and digits.
    (valid schema) Declare a simple type based on NCName and restricted
    with 2 enumeration                                      values "_-."
    and "_-0.".
    The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00605/ST_facets00605.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00605/ST_facets00605_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00604_st_facets00604_p():
    """
    Enumeration values contain lower case and upper case letters and non-
    letter characters. (valid schema) Declare a simple type based on
    NCName and restricted with several enumeration
    values that contain lower case and upper case letters and non-letter
    characters:                                      "aaaa",  "bbbB",
    "ccCc",  "ddDD",  "eEee",
    "fFfF",  "pPPp",  "gGGG",  "Hhhh",  "IiiI",  "JjJj",
    "KkKK",  "LLll",  "MMmM",  "NNNn",  "OOOO",
    "bbb0",  "cc0c",  "dd00",  "e0ee",  "f0f0",  "p00p",  "g000",
    "bbb_",  "cc_c",  "dd__",  "e_ee",  "f_f_",  "p__p",  "g___",
    "H111",  "I11I",  "J1J1",  "K1KK",  "LL11",  "MM1M",  "NNN1",
    "H---",  "I--I",  "J-J-",  "K-KK",  "LL--",  "MM-M",  "NNN-".
    The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00604/ST_facets00604.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00604/ST_facets00604_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00603_st_facets00603_p():
    """
    Enumeration values contain digits followed by a non-digit characters.
    (valid schema) Declare a simple type based on NCName and restricted
    with 3 enumeration                                      values
    "aa111a2Aa", "aa22B3c" and "aa3-4_".
    The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00603/ST_facets00603.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00603/ST_facets00603_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00602_st_facets00602_p():
    """
    Enumeration values contain several punctuation characters. (valid
    schema) Declare a simple type based on NCName and restricted with 2
    enumeration                                      values
    "a&#x002D;1&#x002E;2&#x005F;3&#x00B7;4&#x0387;5&#x06DD;6&#x06DE;" and
    "a1_2_3_4_5_6".
    The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00602/ST_facets00602.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00602/ST_facets00602_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00601_st_facets00601_p():
    r"""
    Enumeration values contain several punctuation characters. (valid
    schema) Declare a simple type based on NCName and restricted with 7
    enumeration                                       values that has the
    following punctuation characters:
    hyphen ('-', \u002D, HYPHEN-MINUS), period ('.', \u002E, FULL STOP),
    underscore ('_', \u005F, LOW LINE),
    dot ('.', \u00B7, MIDDLE DOT), \u0387, GREEK ANO TELEIA,
    \u06DD, ARABIC END OF AYAH and \u06DE, ARABIC START OF RUB EL HIZB.
    The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00601/ST_facets00601.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00601/ST_facets00601_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00506m2_positive():
    """
    Enumeration values end with the extender characters 0x30fc, 0x30fd,
    0x30fe (valid schema) Declare a simple type based on NCName and
    restricted with 3 enumeration values
    that end with the extender characters 0x30fc, 0x30fd, 0x30fe. The
    document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00506m/ST_facets00506m2.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00506m/ST_facets00506m2_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00506m1_positive():
    """
    Enumeration values end with the extender characters 0x00b7, 0x02d0,
    0x02d1, 0x0387, 0x0640, 0x0e46, 0x0ec6, 0x3005, 0x3031, 0x3033,
    0x3035, 0x309d, 0x309d, 0x309e (valid schema) Declare a simple type
    based on NCName and restricted with 14 enumeration values
    that end with the extender characters 0x00b7, 0x02d0, 0x02d1, 0x0387,
    0x0640, 0x0e46, 0x0ec6, 0x3005, 0x3031, 0x3033, 0x3035, 0x309d,
    0x309d, 0x309e. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00506m/ST_facets00506m1.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00506m/ST_facets00506m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00505m9_positive():
    """
    Enumeration values end with the combining characters 0x0f39, 0x0f3e,
    0x0f3f, 0x0f71, 0x0f7a, 0x0f84, 0x0f86, 0x0f86, 0x0f87, 0x0f90,
    0x0f92, 0x0f95, 0x0f97, 0x0f99, 0x0fa3, 0x0fad, 0x0fb1, 0x0fb4,
    0x0fb7, 0x0fb9 (valid schema) Declare a simple type based on NCName
    and restricted with 20 enumeration values
    that end with the combining characters 0x0f39, 0x0f3e, 0x0f3f, 0x0f71,
    0x0f7a, 0x0f84, 0x0f86, 0x0f86, 0x0f87, 0x0f90, 0x0f92, 0x0f95,
    0x0f97, 0x0f99, 0x0fa3, 0x0fad, 0x0fb1, 0x0fb4, 0x0fb7, 0x0fb9. The
    document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00505m/ST_facets00505m9.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00505m/ST_facets00505m9_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00505m8_positive():
    """
    Enumeration values end with the combining characters 0x0e31, 0x0e34,
    0x0e37, 0x0e3a, 0x0e47, 0x0e4a, 0x0e4e, 0x0eb1, 0x0eb4, 0x0eb6,
    0x0eb9, 0x0ebb, 0x0ebb, 0x0ebc, 0x0ec8, 0x0eca, 0x0ecd, 0x0f18,
    0x0f18, 0x0f19, 0x0f35, 0x0f37 (valid schema) Declare a simple type
    based on NCName and restricted with 22 enumeration values
    that end with the combining characters 0x0e31, 0x0e34, 0x0e37, 0x0e3a,
    0x0e47, 0x0e4a, 0x0e4e, 0x0eb1, 0x0eb4, 0x0eb6, 0x0eb9, 0x0ebb,
    0x0ebb, 0x0ebc, 0x0ec8, 0x0eca, 0x0ecd, 0x0f18, 0x0f18, 0x0f19,
    0x0f35, 0x0f37. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00505m/ST_facets00505m8.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00505m/ST_facets00505m8_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00505m7_positive():
    """
    Enumeration values end with the combining characters 0x0c82, 0x0c82,
    0x0c83, 0x0cbe, 0x0cc1, 0x0cc4, 0x0cc6, 0x0cc7, 0x0cc8, 0x0cca,
    0x0ccb, 0x0ccd, 0x0cd5, 0x0cd5, 0x0cd6, 0x0d02, 0x0d02, 0x0d03,
    0x0d3e, 0x0d40, 0x0d43, 0x0d46, 0x0d47, 0x0d48, 0x0d4a, 0x0d4b,
    0x0d4d, 0x0d57 (valid schema) Declare a simple type based on NCName
    and restricted with 28 enumeration values
    that end with the combining characters 0x0c82, 0x0c82, 0x0c83, 0x0cbe,
    0x0cc1, 0x0cc4, 0x0cc6, 0x0cc7, 0x0cc8, 0x0cca, 0x0ccb, 0x0ccd,
    0x0cd5, 0x0cd5, 0x0cd6, 0x0d02, 0x0d02, 0x0d03, 0x0d3e, 0x0d40,
    0x0d43, 0x0d46, 0x0d47, 0x0d48, 0x0d4a, 0x0d4b, 0x0d4d, 0x0d57. The
    document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00505m/ST_facets00505m7.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00505m/ST_facets00505m7_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00505m6_positive():
    """
    Enumeration values end with the combining characters 0x0b82, 0x0b82,
    0x0b83, 0x0bbe, 0x0bc0, 0x0bc2, 0x0bc6, 0x0bc7, 0x0bc8, 0x0bca,
    0x0bcb, 0x0bcd, 0x0bd7, 0x0c01, 0x0c02, 0x0c03, 0x0c3e, 0x0c41,
    0x0c44, 0x0c46, 0x0c47, 0x0c48, 0x0c4a, 0x0c4b, 0x0c4d, 0x0c55,
    0x0c55, 0x0c56 (valid schema) Declare a simple type based on NCName
    and restricted with 28 enumeration values
    that end with the combining characters 0x0b82, 0x0b82, 0x0b83, 0x0bbe,
    0x0bc0, 0x0bc2, 0x0bc6, 0x0bc7, 0x0bc8, 0x0bca, 0x0bcb, 0x0bcd,
    0x0bd7, 0x0c01, 0x0c02, 0x0c03, 0x0c3e, 0x0c41, 0x0c44, 0x0c46,
    0x0c47, 0x0c48, 0x0c4a, 0x0c4b, 0x0c4d, 0x0c55, 0x0c55, 0x0c56. The
    document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00505m/ST_facets00505m6.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00505m/ST_facets00505m6_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00505m5_positive():
    """
    Enumeration values end with the combining characters 0x0abc, 0x0abe,
    0x0ac1, 0x0ac5, 0x0ac7, 0x0ac8, 0x0ac9, 0x0acb, 0x0acc, 0x0acd,
    0x0b01, 0x0b02, 0x0b03, 0x0b3c, 0x0b3e, 0x0b40, 0x0b43, 0x0b47,
    0x0b47, 0x0b48, 0x0b4b, 0x0b4c, 0x0b4d, 0x0b56, 0x0b56, 0x0b57 (valid
    schema) Declare a simple type based on NCName and restricted with 26
    enumeration values                               that end with the
    combining characters 0x0abc, 0x0abe, 0x0ac1, 0x0ac5, 0x0ac7, 0x0ac8,
    0x0ac9, 0x0acb, 0x0acc, 0x0acd, 0x0b01, 0x0b02, 0x0b03, 0x0b3c,
    0x0b3e, 0x0b40, 0x0b43, 0x0b47, 0x0b47, 0x0b48, 0x0b4b, 0x0b4c,
    0x0b4d, 0x0b56, 0x0b56, 0x0b57. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00505m/ST_facets00505m5.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00505m/ST_facets00505m5_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00505m4_positive():
    """
    Enumeration values end with the combining characters 0x09e2, 0x09e2,
    0x09e3, 0x0a02, 0x0a3c, 0x0a3e, 0x0a3f, 0x0a40, 0x0a41, 0x0a42,
    0x0a47, 0x0a47, 0x0a48, 0x0a4b, 0x0a4c, 0x0a4d, 0x0a70, 0x0a70,
    0x0a71, 0x0a81, 0x0a82, 0x0a83 (valid schema) Declare a simple type
    based on NCName and restricted with 22 enumeration values
    that end with the combining characters 0x09e2, 0x09e2, 0x09e3, 0x0a02,
    0x0a3c, 0x0a3e, 0x0a3f, 0x0a40, 0x0a41, 0x0a42, 0x0a47, 0x0a47,
    0x0a48, 0x0a4b, 0x0a4c, 0x0a4d, 0x0a70, 0x0a70, 0x0a71, 0x0a81,
    0x0a82, 0x0a83. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00505m/ST_facets00505m4.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00505m/ST_facets00505m4_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00505m3_positive():
    """
    Enumeration values end with the combining characters 0x0951, 0x0952,
    0x0954, 0x0962, 0x0962, 0x0963, 0x0981, 0x0982, 0x0983, 0x09bc,
    0x09be, 0x09bf, 0x09c0, 0x09c2, 0x09c4, 0x09c7, 0x09c7, 0x09c8,
    0x09cb, 0x09cc, 0x09cd, 0x09d7 (valid schema) Declare a simple type
    based on NCName and restricted with 22 enumeration values
    that end with the combining characters 0x0951, 0x0952, 0x0954, 0x0962,
    0x0962, 0x0963, 0x0981, 0x0982, 0x0983, 0x09bc, 0x09be, 0x09bf,
    0x09c0, 0x09c2, 0x09c4, 0x09c7, 0x09c7, 0x09c8, 0x09cb, 0x09cc,
    0x09cd, 0x09d7. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00505m/ST_facets00505m3.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00505m/ST_facets00505m3_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00505m2_positive():
    """
    Enumeration values end with the combining characters 0x0670, 0x06d6,
    0x06d9, 0x06dc, 0x06dd, 0x06de, 0x06df, 0x06e0, 0x06e2, 0x06e4,
    0x06e7, 0x06e7, 0x06e8, 0x06ea, 0x06eb, 0x06ed, 0x0901, 0x0902,
    0x0903, 0x093c, 0x093e, 0x0945, 0x094c, 0x094d (valid schema) Declare
    a simple type based on NCName and restricted with 24 enumeration
    values                               that end with the combining
    characters 0x0670, 0x06d6, 0x06d9, 0x06dc, 0x06dd, 0x06de, 0x06df,
    0x06e0, 0x06e2, 0x06e4, 0x06e7, 0x06e7, 0x06e8, 0x06ea, 0x06eb,
    0x06ed, 0x0901, 0x0902, 0x0903, 0x093c, 0x093e, 0x0945, 0x094c,
    0x094d. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00505m/ST_facets00505m2.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00505m/ST_facets00505m2_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00505m10_positive():
    """
    Enumeration values end with the combining characters 0x20d0, 0x20d6,
    0x20dc, 0x20e1, 0x302a, 0x302c, 0x302f, 0x3099, 0x309a (valid schema)
    Declare a simple type based on NCName and restricted with 9
    enumeration values                               that end with the
    combining characters 0x20d0, 0x20d6, 0x20dc, 0x20e1, 0x302a, 0x302c,
    0x302f, 0x3099, 0x309a. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00505m/ST_facets00505m10.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00505m/ST_facets00505m10_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00505m1_positive():
    """
    Enumeration values end with the combining characters 0x0300, 0x0322,
    0x0344, 0x0360, 0x0360, 0x0361, 0x0483, 0x0484, 0x0486, 0x0591,
    0x0599, 0x05a1, 0x05a3, 0x05ae, 0x05b9, 0x05bb, 0x05bc, 0x05bd,
    0x05bf, 0x05c1, 0x05c1, 0x05c2, 0x05c4, 0x064b, 0x064e, 0x0652 (valid
    schema) Declare a simple type based on NCName and restricted with 26
    enumeration values                               that end with the
    combining characters 0x0300, 0x0322, 0x0344, 0x0360, 0x0360, 0x0361,
    0x0483, 0x0484, 0x0486, 0x0591, 0x0599, 0x05a1, 0x05a3, 0x05ae,
    0x05b9, 0x05bb, 0x05bc, 0x05bd, 0x05bf, 0x05c1, 0x05c1, 0x05c2,
    0x05c4, 0x064b, 0x064e, 0x0652. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00505m/ST_facets00505m1.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00505m/ST_facets00505m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00504m2_positive():
    """
    Enumeration values end with the digit characters 0x0ce6, 0x0cea,
    0x0cef, 0x0d66, 0x0d6a, 0x0d6f, 0x0e50, 0x0e54, 0x0e59, 0x0ed0,
    0x0ed4, 0x0ed9, 0x0f20, 0x0f24, 0x0f29 (valid schema) Declare a simple
    type based on NCName and restricted with 15 enumeration values
    that end with the digit characters 0x0ce6, 0x0cea, 0x0cef, 0x0d66,
    0x0d6a, 0x0d6f, 0x0e50, 0x0e54, 0x0e59, 0x0ed0, 0x0ed4, 0x0ed9,
    0x0f20, 0x0f24, 0x0f29. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00504m/ST_facets00504m2.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00504m/ST_facets00504m2_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00504m1_positive():
    """
    Enumeration values end with the digit characters 0x0030, 0x0034,
    0x0039, 0x0660, 0x0664, 0x0669, 0x06f0, 0x06f4, 0x06f9, 0x0966,
    0x096a, 0x096f, 0x09e6, 0x09ea, 0x09ef, 0x0a66, 0x0a6a, 0x0a6f,
    0x0ae6, 0x0aea, 0x0aef, 0x0b66, 0x0b6a, 0x0b6f, 0x0be7, 0x0beb,
    0x0bef, 0x0c66, 0x0c6a, 0x0c6f (valid schema) Declare a simple type
    based on NCName and restricted with 30 enumeration values
    that end with the digit characters 0x0030, 0x0034, 0x0039, 0x0660,
    0x0664, 0x0669, 0x06f0, 0x06f4, 0x06f9, 0x0966, 0x096a, 0x096f,
    0x09e6, 0x09ea, 0x09ef, 0x0a66, 0x0a6a, 0x0a6f, 0x0ae6, 0x0aea,
    0x0aef, 0x0b66, 0x0b6a, 0x0b6f, 0x0be7, 0x0beb, 0x0bef, 0x0c66,
    0x0c6a, 0x0c6f. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00504m/ST_facets00504m1.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00504m/ST_facets00504m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00503m1_positive():
    """
    Enumeration values end with the characters 0x005f, 0x002e, 0x002d
    (valid schema) Declare a simple type based on NCName and restricted
    with 3 enumeration values                               that end with
    the characters 0x005f, 0x002e, 0x002d. The document uses each of the
    values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00503m/ST_facets00503m1.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00503m/ST_facets00503m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00502m1_positive():
    """
    Enumeration values end with the ideographic characters 0x4e00, 0x76d2,
    0x9fa5, 0x3007, 0x3021, 0x3025, 0x3029 (valid schema) Declare a simple
    type based on NCName and restricted with 7 enumeration values
    that end with the ideographic characters 0x4e00, 0x76d2, 0x9fa5,
    0x3007, 0x3021, 0x3025, 0x3029. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00502m/ST_facets00502m1.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00502m/ST_facets00502m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00501m9_positive():
    """
    Enumeration values end with the basic characters 0x0a8f, 0x0a90,
    0x0a91, 0x0a93, 0x0a9d, 0x0aa8, 0x0aaa, 0x0aad, 0x0ab0, 0x0ab2,
    0x0ab2, 0x0ab3, 0x0ab5, 0x0ab7, 0x0ab9, 0x0abd, 0x0ae0, 0x0b05,
    0x0b08, 0x0b0c, 0x0b0f, 0x0b0f, 0x0b10, 0x0b13, 0x0b1d, 0x0b28 (valid
    schema) Declare a simple type based on NCName and restricted with 26
    enumeration values                               that end with the
    basic characters 0x0a8f, 0x0a90, 0x0a91, 0x0a93, 0x0a9d, 0x0aa8,
    0x0aaa, 0x0aad, 0x0ab0, 0x0ab2, 0x0ab2, 0x0ab3, 0x0ab5, 0x0ab7,
    0x0ab9, 0x0abd, 0x0ae0, 0x0b05, 0x0b08, 0x0b0c, 0x0b0f, 0x0b0f,
    0x0b10, 0x0b13, 0x0b1d, 0x0b28. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m9.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m9_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00501m8_positive():
    """
    Enumeration values end with the basic characters 0x0a13, 0x0a1d,
    0x0a28, 0x0a2a, 0x0a2d, 0x0a30, 0x0a32, 0x0a32, 0x0a33, 0x0a35,
    0x0a35, 0x0a36, 0x0a38, 0x0a38, 0x0a39, 0x0a59, 0x0a5a, 0x0a5c,
    0x0a5e, 0x0a72, 0x0a73, 0x0a74, 0x0a85, 0x0a88, 0x0a8b, 0x0a8d (valid
    schema) Declare a simple type based on NCName and restricted with 26
    enumeration values                               that end with the
    basic characters 0x0a13, 0x0a1d, 0x0a28, 0x0a2a, 0x0a2d, 0x0a30,
    0x0a32, 0x0a32, 0x0a33, 0x0a35, 0x0a35, 0x0a36, 0x0a38, 0x0a38,
    0x0a39, 0x0a59, 0x0a5a, 0x0a5c, 0x0a5e, 0x0a72, 0x0a73, 0x0a74,
    0x0a85, 0x0a88, 0x0a8b, 0x0a8d. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m8.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m8_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00501m7_positive():
    """
    Enumeration values end with the basic characters 0x098f, 0x098f,
    0x0990, 0x0993, 0x099d, 0x09a8, 0x09aa, 0x09ad, 0x09b0, 0x09b2,
    0x09b6, 0x09b7, 0x09b9, 0x09dc, 0x09dc, 0x09dd, 0x09df, 0x09e0,
    0x09e1, 0x09f0, 0x09f0, 0x09f1, 0x0a05, 0x0a07, 0x0a0a, 0x0a0f,
    0x0a0f, 0x0a10 (valid schema) Declare a simple type based on NCName
    and restricted with 28 enumeration values
    that end with the basic characters 0x098f, 0x098f, 0x0990, 0x0993,
    0x099d, 0x09a8, 0x09aa, 0x09ad, 0x09b0, 0x09b2, 0x09b6, 0x09b7,
    0x09b9, 0x09dc, 0x09dc, 0x09dd, 0x09df, 0x09e0, 0x09e1, 0x09f0,
    0x09f0, 0x09f1, 0x0a05, 0x0a07, 0x0a0a, 0x0a0f, 0x0a0f, 0x0a10. The
    document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m7.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m7_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00501m6_positive():
    """
    Enumeration values end with the basic characters 0x0671, 0x0694,
    0x06b7, 0x06ba, 0x06bc, 0x06be, 0x06c0, 0x06c7, 0x06ce, 0x06d0,
    0x06d1, 0x06d3, 0x06d5, 0x06e5, 0x06e5, 0x06e6, 0x0905, 0x091f,
    0x0939, 0x093d, 0x0958, 0x095c, 0x0961, 0x0985, 0x0988, 0x098c (valid
    schema) Declare a simple type based on NCName and restricted with 26
    enumeration values                               that end with the
    basic characters 0x0671, 0x0694, 0x06b7, 0x06ba, 0x06bc, 0x06be,
    0x06c0, 0x06c7, 0x06ce, 0x06d0, 0x06d1, 0x06d3, 0x06d5, 0x06e5,
    0x06e5, 0x06e6, 0x0905, 0x091f, 0x0939, 0x093d, 0x0958, 0x095c,
    0x0961, 0x0985, 0x0988, 0x098c. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m6.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m6_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00501m5_positive():
    """
    Enumeration values end with the basic characters 0x04d0, 0x04dd,
    0x04eb, 0x04ee, 0x04f1, 0x04f5, 0x04f8, 0x04f8, 0x04f9, 0x0531,
    0x0543, 0x0556, 0x0559, 0x0561, 0x0573, 0x0586, 0x05d0, 0x05dd,
    0x05ea, 0x05f0, 0x05f1, 0x05f2, 0x0621, 0x062d, 0x063a, 0x0641,
    0x0645, 0x064a (valid schema) Declare a simple type based on NCName
    and restricted with 28 enumeration values
    that end with the basic characters 0x04d0, 0x04dd, 0x04eb, 0x04ee,
    0x04f1, 0x04f5, 0x04f8, 0x04f8, 0x04f9, 0x0531, 0x0543, 0x0556,
    0x0559, 0x0561, 0x0573, 0x0586, 0x05d0, 0x05dd, 0x05ea, 0x05f0,
    0x05f1, 0x05f2, 0x0621, 0x062d, 0x063a, 0x0641, 0x0645, 0x064a. The
    document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m5.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m5_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00501m4_positive():
    """
    Enumeration values end with the basic characters 0x03d0, 0x03d3,
    0x03d6, 0x03e2, 0x03e9, 0x03f1, 0x0401, 0x0406, 0x040c, 0x040e,
    0x042e, 0x044f, 0x0451, 0x0456, 0x045c, 0x045e, 0x046f, 0x0481,
    0x0490, 0x04a7, 0x04bf, 0x04c1, 0x04c2, 0x04c4, 0x04c7, 0x04c7,
    0x04c8, 0x04cb, 0x04cb, 0x04cc (valid schema) Declare a simple type
    based on NCName and restricted with 30 enumeration values
    that end with the basic characters 0x03d0, 0x03d3, 0x03d6, 0x03e2,
    0x03e9, 0x03f1, 0x0401, 0x0406, 0x040c, 0x040e, 0x042e, 0x044f,
    0x0451, 0x0456, 0x045c, 0x045e, 0x046f, 0x0481, 0x0490, 0x04a7,
    0x04bf, 0x04c1, 0x04c2, 0x04c4, 0x04c7, 0x04c7, 0x04c8, 0x04cb,
    0x04cb, 0x04cc. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m4.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m4_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00501m3_positive():
    """
    Enumeration values end with the basic characters 0x0276, 0x027a,
    0x027f, 0x0281, 0x0294, 0x02a8, 0x02bb, 0x02be, 0x02c1, 0x0386,
    0x0388, 0x0389, 0x038a, 0x038c, 0x038e, 0x038e, 0x038f, 0x0391,
    0x0399, 0x03a1, 0x03a3, 0x03a9, 0x03af, 0x03b1, 0x03bf, 0x03ce (valid
    schema) Declare a simple type based on NCName and restricted with 26
    enumeration values                               that end with the
    basic characters 0x0276, 0x027a, 0x027f, 0x0281, 0x0294, 0x02a8,
    0x02bb, 0x02be, 0x02c1, 0x0386, 0x0388, 0x0389, 0x038a, 0x038c,
    0x038e, 0x038e, 0x038f, 0x0391, 0x0399, 0x03a1, 0x03a3, 0x03a9,
    0x03af, 0x03b1, 0x03bf, 0x03ce. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m3.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m3_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00501m21_positive():
    """
    Enumeration values end with the basic characters 0x1fe8, 0x1fea,
    0x1fec, 0x1ff8, 0x1ff9, 0x1ffb, 0x2180, 0x2181, 0x2182, 0x3041,
    0x306a, 0x3094, 0x30a1, 0x30cd, 0x30fa, 0x3105, 0x3118, 0x312c,
    0xac00, 0xc1d1, 0xd7a3 (valid schema) Declare a simple type based on
    NCName and restricted with 21 enumeration values
    that end with the basic characters 0x1fe8, 0x1fea, 0x1fec, 0x1ff8,
    0x1ff9, 0x1ffb, 0x2180, 0x2181, 0x2182, 0x3041, 0x306a, 0x3094,
    0x30a1, 0x30cd, 0x30fa, 0x3105, 0x3118, 0x312c, 0xac00, 0xc1d1,
    0xd7a3. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m21.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m21_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00501m20_positive():
    """
    Enumeration values end with the basic characters 0x1f5b, 0x1f5d,
    0x1f5f, 0x1f6e, 0x1f7d, 0x1fb0, 0x1fb0, 0x1fb1, 0x1fb8, 0x1fb9,
    0x1fbb, 0x1fc8, 0x1fc9, 0x1fcb, 0x1fd0, 0x1fd0, 0x1fd1, 0x1fd8,
    0x1fd9, 0x1fdb, 0x1fe0, 0x1fe0, 0x1fe1, 0x1fe5 (valid schema) Declare
    a simple type based on NCName and restricted with 24 enumeration
    values                               that end with the basic
    characters 0x1f5b, 0x1f5d, 0x1f5f, 0x1f6e, 0x1f7d, 0x1fb0, 0x1fb0,
    0x1fb1, 0x1fb8, 0x1fb9, 0x1fbb, 0x1fc8, 0x1fc9, 0x1fcb, 0x1fd0,
    0x1fd0, 0x1fd1, 0x1fd8, 0x1fd9, 0x1fdb, 0x1fe0, 0x1fe0, 0x1fe1,
    0x1fe5. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m20.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m20_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00501m2_positive():
    """
    Enumeration values end with the basic characters 0x014a, 0x0164,
    0x017e, 0x0180, 0x018a, 0x0194, 0x0196, 0x019d, 0x01a5, 0x01a7,
    0x01a8, 0x01a9, 0x01ab, 0x01b4, 0x01bd, 0x01c0, 0x01c1, 0x01c3,
    0x01cd, 0x01de, 0x01ef, 0x01f4, 0x01f4, 0x01f5, 0x01fa, 0x0208,
    0x0217, 0x0250, 0x0262, 0x0274 (valid schema) Declare a simple type
    based on NCName and restricted with 30 enumeration values
    that end with the basic characters 0x014a, 0x0164, 0x017e, 0x0180,
    0x018a, 0x0194, 0x0196, 0x019d, 0x01a5, 0x01a7, 0x01a8, 0x01a9,
    0x01ab, 0x01b4, 0x01bd, 0x01c0, 0x01c1, 0x01c3, 0x01cd, 0x01de,
    0x01ef, 0x01f4, 0x01f4, 0x01f5, 0x01fa, 0x0208, 0x0217, 0x0250,
    0x0262, 0x0274. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m2.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m2_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00501m19_positive():
    """
    Enumeration values end with the basic characters 0x1ea0, 0x1ecc,
    0x1ef9, 0x1f00, 0x1f0a, 0x1f15, 0x1f18, 0x1f1a, 0x1f1d, 0x1f20,
    0x1f32, 0x1f45, 0x1f48, 0x1f4a, 0x1f4d, 0x1f51, 0x1f53, 0x1f55,
    0x1f57, 0x1f59 (valid schema) Declare a simple type based on NCName
    and restricted with 20 enumeration values
    that end with the basic characters 0x1ea0, 0x1ecc, 0x1ef9, 0x1f00,
    0x1f0a, 0x1f15, 0x1f18, 0x1f1a, 0x1f1d, 0x1f20, 0x1f32, 0x1f45,
    0x1f48, 0x1f4a, 0x1f4d, 0x1f51, 0x1f53, 0x1f55, 0x1f57, 0x1f59. The
    document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m19.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m19_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00501m18_positive():
    """
    Enumeration values end with the basic characters 0x11ab, 0x11ae,
    0x11ae, 0x11af, 0x11b7, 0x11b7, 0x11b8, 0x11ba, 0x11bc, 0x11bf,
    0x11c2, 0x11eb, 0x11f0, 0x11f9, 0x1e00, 0x1e4a, 0x1e95, 0x1e9b (valid
    schema) Declare a simple type based on NCName and restricted with 18
    enumeration values                               that end with the
    basic characters 0x11ab, 0x11ae, 0x11ae, 0x11af, 0x11b7, 0x11b7,
    0x11b8, 0x11ba, 0x11bc, 0x11bf, 0x11c2, 0x11eb, 0x11f0, 0x11f9,
    0x1e00, 0x1e4a, 0x1e95, 0x1e9b. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m18.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m18_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00501m17_positive():
    """
    Enumeration values end with the basic characters 0x115f, 0x1160,
    0x1161, 0x1163, 0x1165, 0x1167, 0x1169, 0x116d, 0x116d, 0x116e,
    0x1172, 0x1172, 0x1173, 0x1175, 0x119e, 0x11a8 (valid schema) Declare
    a simple type based on NCName and restricted with 16 enumeration
    values                               that end with the basic
    characters 0x115f, 0x1160, 0x1161, 0x1163, 0x1165, 0x1167, 0x1169,
    0x116d, 0x116d, 0x116e, 0x1172, 0x1172, 0x1173, 0x1175, 0x119e,
    0x11a8. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m17.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m17_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00501m16_positive():
    """
    Enumeration values end with the basic characters 0x110b, 0x110b,
    0x110c, 0x110e, 0x1110, 0x1112, 0x113c, 0x113e, 0x1140, 0x114c,
    0x114e, 0x1150, 0x1154, 0x1154, 0x1155, 0x1159 (valid schema) Declare
    a simple type based on NCName and restricted with 16 enumeration
    values                               that end with the basic
    characters 0x110b, 0x110b, 0x110c, 0x110e, 0x1110, 0x1112, 0x113c,
    0x113e, 0x1140, 0x114c, 0x114e, 0x1150, 0x1154, 0x1154, 0x1155,
    0x1159. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m16.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m16_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00501m15_positive():
    """
    Enumeration values end with the basic characters 0x0eb0, 0x0eb2,
    0x0eb2, 0x0eb3, 0x0ebd, 0x0ec0, 0x0ec2, 0x0ec4, 0x0f40, 0x0f43,
    0x0f47, 0x0f49, 0x0f59, 0x0f69, 0x1100, 0x1102, 0x1102, 0x1103,
    0x1105, 0x1106, 0x1107, 0x1109 (valid schema) Declare a simple type
    based on NCName and restricted with 22 enumeration values
    that end with the basic characters 0x0eb0, 0x0eb2, 0x0eb2, 0x0eb3,
    0x0ebd, 0x0ec0, 0x0ec2, 0x0ec4, 0x0f40, 0x0f43, 0x0f47, 0x0f49,
    0x0f59, 0x0f69, 0x1100, 0x1102, 0x1102, 0x1103, 0x1105, 0x1106,
    0x1107, 0x1109. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m15.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m15_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00501m14_positive():
    """
    Enumeration values end with the basic characters 0x0e87, 0x0e87,
    0x0e88, 0x0e8a, 0x0e8d, 0x0e94, 0x0e95, 0x0e97, 0x0e99, 0x0e9c,
    0x0e9f, 0x0ea1, 0x0ea2, 0x0ea3, 0x0ea5, 0x0ea7, 0x0eaa, 0x0eaa,
    0x0eab, 0x0ead, 0x0ead, 0x0eae (valid schema) Declare a simple type
    based on NCName and restricted with 22 enumeration values
    that end with the basic characters 0x0e87, 0x0e87, 0x0e88, 0x0e8a,
    0x0e8d, 0x0e94, 0x0e95, 0x0e97, 0x0e99, 0x0e9c, 0x0e9f, 0x0ea1,
    0x0ea2, 0x0ea3, 0x0ea5, 0x0ea7, 0x0eaa, 0x0eaa, 0x0eab, 0x0ead,
    0x0ead, 0x0eae. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m14.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m14_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00501m13_positive():
    """
    Enumeration values end with the basic characters 0x0d0e, 0x0d0f,
    0x0d10, 0x0d12, 0x0d1d, 0x0d28, 0x0d2a, 0x0d31, 0x0d39, 0x0d60,
    0x0d60, 0x0d61, 0x0e01, 0x0e17, 0x0e2e, 0x0e30, 0x0e32, 0x0e32,
    0x0e33, 0x0e40, 0x0e42, 0x0e45, 0x0e81, 0x0e81, 0x0e82, 0x0e84 (valid
    schema) Declare a simple type based on NCName and restricted with 26
    enumeration values                               that end with the
    basic characters 0x0d0e, 0x0d0f, 0x0d10, 0x0d12, 0x0d1d, 0x0d28,
    0x0d2a, 0x0d31, 0x0d39, 0x0d60, 0x0d60, 0x0d61, 0x0e01, 0x0e17,
    0x0e2e, 0x0e30, 0x0e32, 0x0e32, 0x0e33, 0x0e40, 0x0e42, 0x0e45,
    0x0e81, 0x0e81, 0x0e82, 0x0e84. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m13.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m13_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00501m12_positive():
    """
    Enumeration values end with the basic characters 0x0c35, 0x0c37,
    0x0c39, 0x0c60, 0x0c60, 0x0c61, 0x0c85, 0x0c88, 0x0c8c, 0x0c8e,
    0x0c8f, 0x0c90, 0x0c92, 0x0c9d, 0x0ca8, 0x0caa, 0x0cae, 0x0cb3,
    0x0cb5, 0x0cb7, 0x0cb9, 0x0cde, 0x0ce0, 0x0ce0, 0x0ce1, 0x0d05,
    0x0d08, 0x0d0c (valid schema) Declare a simple type based on NCName
    and restricted with 28 enumeration values
    that end with the basic characters 0x0c35, 0x0c37, 0x0c39, 0x0c60,
    0x0c60, 0x0c61, 0x0c85, 0x0c88, 0x0c8c, 0x0c8e, 0x0c8f, 0x0c90,
    0x0c92, 0x0c9d, 0x0ca8, 0x0caa, 0x0cae, 0x0cb3, 0x0cb5, 0x0cb7,
    0x0cb9, 0x0cde, 0x0ce0, 0x0ce0, 0x0ce1, 0x0d05, 0x0d08, 0x0d0c. The
    document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m12.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m12_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00501m11_positive():
    """
    Enumeration values end with the basic characters 0x0b9c, 0x0b9e,
    0x0b9e, 0x0b9f, 0x0ba3, 0x0ba3, 0x0ba4, 0x0ba8, 0x0ba9, 0x0baa,
    0x0bae, 0x0bb1, 0x0bb5, 0x0bb7, 0x0bb8, 0x0bb9, 0x0c05, 0x0c08,
    0x0c0c, 0x0c0e, 0x0c0f, 0x0c10, 0x0c12, 0x0c1d, 0x0c28, 0x0c2a,
    0x0c2e, 0x0c33 (valid schema) Declare a simple type based on NCName
    and restricted with 28 enumeration values
    that end with the basic characters 0x0b9c, 0x0b9e, 0x0b9e, 0x0b9f,
    0x0ba3, 0x0ba3, 0x0ba4, 0x0ba8, 0x0ba9, 0x0baa, 0x0bae, 0x0bb1,
    0x0bb5, 0x0bb7, 0x0bb8, 0x0bb9, 0x0c05, 0x0c08, 0x0c0c, 0x0c0e,
    0x0c0f, 0x0c10, 0x0c12, 0x0c1d, 0x0c28, 0x0c2a, 0x0c2e, 0x0c33. The
    document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m11.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m11_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00501m10_positive():
    """
    Enumeration values end with the basic characters 0x0b2a, 0x0b2d,
    0x0b30, 0x0b32, 0x0b32, 0x0b33, 0x0b36, 0x0b37, 0x0b39, 0x0b3d,
    0x0b5c, 0x0b5c, 0x0b5d, 0x0b5f, 0x0b60, 0x0b61, 0x0b85, 0x0b87,
    0x0b8a, 0x0b8e, 0x0b8f, 0x0b90, 0x0b92, 0x0b93, 0x0b95, 0x0b99,
    0x0b99, 0x0b9a (valid schema) Declare a simple type based on NCName
    and restricted with 28 enumeration values
    that end with the basic characters 0x0b2a, 0x0b2d, 0x0b30, 0x0b32,
    0x0b32, 0x0b33, 0x0b36, 0x0b37, 0x0b39, 0x0b3d, 0x0b5c, 0x0b5c,
    0x0b5d, 0x0b5f, 0x0b60, 0x0b61, 0x0b85, 0x0b87, 0x0b8a, 0x0b8e,
    0x0b8f, 0x0b90, 0x0b92, 0x0b93, 0x0b95, 0x0b99, 0x0b99, 0x0b9a. The
    document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m10.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m10_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00501m1_positive():
    """
    Enumeration values end with the basic characters 0x0041, 0x004d,
    0x005a, 0x0061, 0x0064, 0x0068, 0x006a, 0x0072, 0x007a, 0x00c0,
    0x00cb, 0x00d6, 0x00d8, 0x00db, 0x00de, 0x00e0, 0x00eb, 0x00f6,
    0x00f8, 0x00fb, 0x00ff, 0x0100, 0x0118, 0x0131, 0x0134, 0x0139,
    0x013e, 0x0141, 0x0144, 0x0148 (valid schema) Declare a simple type
    based on NCName and restricted with 30 enumeration values
    that end with the basic characters 0x0041, 0x004d, 0x005a, 0x0061,
    0x0064, 0x0068, 0x006a, 0x0072, 0x007a, 0x00c0, 0x00cb, 0x00d6,
    0x00d8, 0x00db, 0x00de, 0x00e0, 0x00eb, 0x00f6, 0x00f8, 0x00fb,
    0x00ff, 0x0100, 0x0118, 0x0131, 0x0134, 0x0139, 0x013e, 0x0141,
    0x0144, 0x0148. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m1.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00501m/ST_facets00501m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00403m1_positive():
    """
    Enumeration value begins with the underscore character 0x005f (valid
    schema) Declare a simple type based on NCName and restricted with an
    enumeration value                              that begins with the
    underscore character 0x005f. The document uses the value.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00403m/ST_facets00403m1.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00403m/ST_facets00403m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00402m1_positive():
    """
    Enumeration values begin with the ideographic characters 0x4e00,
    0x76d2, 0x9fa5, 0x3007, 0x3021, 0x3025, 0x3029 (valid schema) Declare
    a simple type based on NCName and restricted with 7 enumeration values
    that begin with the ideographic characters 0x4e00, 0x76d2, 0x9fa5,
    0x3007, 0x3021, 0x3025, 0x3029. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00402m/ST_facets00402m1.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00402m/ST_facets00402m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00401m9_positive():
    """
    Enumeration values begin with the basic characters 0x0a8f, 0x0a90,
    0x0a91, 0x0a93, 0x0a9d, 0x0aa8, 0x0aaa, 0x0aad, 0x0ab0, 0x0ab2,
    0x0ab2, 0x0ab3, 0x0ab5, 0x0ab7, 0x0ab9, 0x0abd, 0x0ae0, 0x0b05,
    0x0b08, 0x0b0c, 0x0b0f, 0x0b0f, 0x0b10, 0x0b13, 0x0b1d, 0x0b28 (valid
    schema) Declare a simple type based on NCName and restricted with 26
    enumeration values                               that begin with the
    basic characters 0x0a8f, 0x0a90, 0x0a91, 0x0a93, 0x0a9d, 0x0aa8,
    0x0aaa, 0x0aad, 0x0ab0, 0x0ab2, 0x0ab2, 0x0ab3, 0x0ab5, 0x0ab7,
    0x0ab9, 0x0abd, 0x0ae0, 0x0b05, 0x0b08, 0x0b0c, 0x0b0f, 0x0b0f,
    0x0b10, 0x0b13, 0x0b1d, 0x0b28. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m9.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m9_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00401m8_positive():
    """
    Enumeration values begin with the basic characters 0x0a13, 0x0a1d,
    0x0a28, 0x0a2a, 0x0a2d, 0x0a30, 0x0a32, 0x0a32, 0x0a33, 0x0a35,
    0x0a35, 0x0a36, 0x0a38, 0x0a38, 0x0a39, 0x0a59, 0x0a5a, 0x0a5c,
    0x0a5e, 0x0a72, 0x0a73, 0x0a74, 0x0a85, 0x0a88, 0x0a8b, 0x0a8d (valid
    schema) Declare a simple type based on NCName and restricted with 26
    enumeration values                               that begin with the
    basic characters 0x0a13, 0x0a1d, 0x0a28, 0x0a2a, 0x0a2d, 0x0a30,
    0x0a32, 0x0a32, 0x0a33, 0x0a35, 0x0a35, 0x0a36, 0x0a38, 0x0a38,
    0x0a39, 0x0a59, 0x0a5a, 0x0a5c, 0x0a5e, 0x0a72, 0x0a73, 0x0a74,
    0x0a85, 0x0a88, 0x0a8b, 0x0a8d. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m8.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m8_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00401m7_positive():
    """
    Enumeration values begin with the basic characters 0x098f, 0x098f,
    0x0990, 0x0993, 0x099d, 0x09a8, 0x09aa, 0x09ad, 0x09b0, 0x09b2,
    0x09b6, 0x09b7, 0x09b9, 0x09dc, 0x09dc, 0x09dd, 0x09df, 0x09e0,
    0x09e1, 0x09f0, 0x09f0, 0x09f1, 0x0a05, 0x0a07, 0x0a0a, 0x0a0f,
    0x0a0f, 0x0a10 (valid schema) Declare a simple type based on NCName
    and restricted with 28 enumeration values
    that begin with the basic characters 0x098f, 0x098f, 0x0990, 0x0993,
    0x099d, 0x09a8, 0x09aa, 0x09ad, 0x09b0, 0x09b2, 0x09b6, 0x09b7,
    0x09b9, 0x09dc, 0x09dc, 0x09dd, 0x09df, 0x09e0, 0x09e1, 0x09f0,
    0x09f0, 0x09f1, 0x0a05, 0x0a07, 0x0a0a, 0x0a0f, 0x0a0f, 0x0a10. The
    document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m7.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m7_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00401m6_positive():
    """
    Enumeration values begin with the basic characters 0x0671, 0x0694,
    0x06b7, 0x06ba, 0x06bc, 0x06be, 0x06c0, 0x06c7, 0x06ce, 0x06d0,
    0x06d1, 0x06d3, 0x06d5, 0x06e5, 0x06e5, 0x06e6, 0x0905, 0x091f,
    0x0939, 0x093d, 0x0958, 0x095c, 0x0961, 0x0985, 0x0988, 0x098c (valid
    schema) Declare a simple type based on NCName and restricted with 26
    enumeration values                               that begin with the
    basic characters 0x0671, 0x0694, 0x06b7, 0x06ba, 0x06bc, 0x06be,
    0x06c0, 0x06c7, 0x06ce, 0x06d0, 0x06d1, 0x06d3, 0x06d5, 0x06e5,
    0x06e5, 0x06e6, 0x0905, 0x091f, 0x0939, 0x093d, 0x0958, 0x095c,
    0x0961, 0x0985, 0x0988, 0x098c. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m6.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m6_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00401m5_positive():
    """
    Enumeration values begin with the basic characters 0x04d0, 0x04dd,
    0x04eb, 0x04ee, 0x04f1, 0x04f5, 0x04f8, 0x04f8, 0x04f9, 0x0531,
    0x0543, 0x0556, 0x0559, 0x0561, 0x0573, 0x0586, 0x05d0, 0x05dd,
    0x05ea, 0x05f0, 0x05f1, 0x05f2, 0x0621, 0x062d, 0x063a, 0x0641,
    0x0645, 0x064a (valid schema) Declare a simple type based on NCName
    and restricted with 28 enumeration values
    that begin with the basic characters 0x04d0, 0x04dd, 0x04eb, 0x04ee,
    0x04f1, 0x04f5, 0x04f8, 0x04f8, 0x04f9, 0x0531, 0x0543, 0x0556,
    0x0559, 0x0561, 0x0573, 0x0586, 0x05d0, 0x05dd, 0x05ea, 0x05f0,
    0x05f1, 0x05f2, 0x0621, 0x062d, 0x063a, 0x0641, 0x0645, 0x064a. The
    document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m5.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m5_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00401m4_positive():
    """
    Enumeration values begin with the basic characters 0x03d0, 0x03d3,
    0x03d6, 0x03e2, 0x03e9, 0x03f1, 0x0401, 0x0406, 0x040c, 0x040e,
    0x042e, 0x044f, 0x0451, 0x0456, 0x045c, 0x045e, 0x046f, 0x0481,
    0x0490, 0x04a7, 0x04bf, 0x04c1, 0x04c2, 0x04c4, 0x04c7, 0x04c7,
    0x04c8, 0x04cb, 0x04cb, 0x04cc (valid schema) Declare a simple type
    based on NCName and restricted with 30 enumeration values
    that begin with the basic characters 0x03d0, 0x03d3, 0x03d6, 0x03e2,
    0x03e9, 0x03f1, 0x0401, 0x0406, 0x040c, 0x040e, 0x042e, 0x044f,
    0x0451, 0x0456, 0x045c, 0x045e, 0x046f, 0x0481, 0x0490, 0x04a7,
    0x04bf, 0x04c1, 0x04c2, 0x04c4, 0x04c7, 0x04c7, 0x04c8, 0x04cb,
    0x04cb, 0x04cc. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m4.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m4_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00401m3_positive():
    """
    Enumeration values begin with the basic characters 0x0276, 0x027a,
    0x027f, 0x0281, 0x0294, 0x02a8, 0x02bb, 0x02be, 0x02c1, 0x0386,
    0x0388, 0x0389, 0x038a, 0x038c, 0x038e, 0x038e, 0x038f, 0x0391,
    0x0399, 0x03a1, 0x03a3, 0x03a9, 0x03af, 0x03b1, 0x03bf, 0x03ce (valid
    schema) Declare a simple type based on NCName and restricted with 26
    enumeration values                               that begin with the
    basic characters 0x0276, 0x027a, 0x027f, 0x0281, 0x0294, 0x02a8,
    0x02bb, 0x02be, 0x02c1, 0x0386, 0x0388, 0x0389, 0x038a, 0x038c,
    0x038e, 0x038e, 0x038f, 0x0391, 0x0399, 0x03a1, 0x03a3, 0x03a9,
    0x03af, 0x03b1, 0x03bf, 0x03ce. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m3.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m3_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00401m21_positive():
    """
    Enumeration values begin with the basic characters 0x1fe8, 0x1fea,
    0x1fec, 0x1ff8, 0x1ff9, 0x1ffb, 0x2180, 0x2181, 0x2182, 0x3041,
    0x306a, 0x3094, 0x30a1, 0x30cd, 0x30fa, 0x3105, 0x3118, 0x312c,
    0xac00, 0xc1d1, 0xd7a3 (valid schema) Declare a simple type based on
    NCName and restricted with 21 enumeration values
    that begin with the basic characters 0x1fe8, 0x1fea, 0x1fec, 0x1ff8,
    0x1ff9, 0x1ffb, 0x2180, 0x2181, 0x2182, 0x3041, 0x306a, 0x3094,
    0x30a1, 0x30cd, 0x30fa, 0x3105, 0x3118, 0x312c, 0xac00, 0xc1d1,
    0xd7a3. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m21.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m21_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00401m20_positive():
    """
    Enumeration values begin with the basic characters 0x1f5b, 0x1f5d,
    0x1f5f, 0x1f6e, 0x1f7d, 0x1fb0, 0x1fb0, 0x1fb1, 0x1fb8, 0x1fb9,
    0x1fbb, 0x1fc8, 0x1fc9, 0x1fcb, 0x1fd0, 0x1fd0, 0x1fd1, 0x1fd8,
    0x1fd9, 0x1fdb, 0x1fe0, 0x1fe0, 0x1fe1, 0x1fe5 (valid schema) Declare
    a simple type based on NCName and restricted with 24 enumeration
    values                               that begin with the basic
    characters 0x1f5b, 0x1f5d, 0x1f5f, 0x1f6e, 0x1f7d, 0x1fb0, 0x1fb0,
    0x1fb1, 0x1fb8, 0x1fb9, 0x1fbb, 0x1fc8, 0x1fc9, 0x1fcb, 0x1fd0,
    0x1fd0, 0x1fd1, 0x1fd8, 0x1fd9, 0x1fdb, 0x1fe0, 0x1fe0, 0x1fe1,
    0x1fe5. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m20.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m20_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00401m2_positive():
    """
    Enumeration values begin with the basic characters 0x014a, 0x0164,
    0x017e, 0x0180, 0x018a, 0x0194, 0x0196, 0x019d, 0x01a5, 0x01a7,
    0x01a8, 0x01a9, 0x01ab, 0x01b4, 0x01bd, 0x01c0, 0x01c1, 0x01c3,
    0x01cd, 0x01de, 0x01ef, 0x01f4, 0x01f4, 0x01f5, 0x01fa, 0x0208,
    0x0217, 0x0250, 0x0262, 0x0274 (valid schema) Declare a simple type
    based on NCName and restricted with 30 enumeration values
    that begin with the basic characters 0x014a, 0x0164, 0x017e, 0x0180,
    0x018a, 0x0194, 0x0196, 0x019d, 0x01a5, 0x01a7, 0x01a8, 0x01a9,
    0x01ab, 0x01b4, 0x01bd, 0x01c0, 0x01c1, 0x01c3, 0x01cd, 0x01de,
    0x01ef, 0x01f4, 0x01f4, 0x01f5, 0x01fa, 0x0208, 0x0217, 0x0250,
    0x0262, 0x0274. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m2.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m2_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00401m19_positive():
    """
    Enumeration values begin with the basic characters 0x1ea0, 0x1ecc,
    0x1ef9, 0x1f00, 0x1f0a, 0x1f15, 0x1f18, 0x1f1a, 0x1f1d, 0x1f20,
    0x1f32, 0x1f45, 0x1f48, 0x1f4a, 0x1f4d, 0x1f51, 0x1f53, 0x1f55,
    0x1f57, 0x1f59 (valid schema) Declare a simple type based on NCName
    and restricted with 20 enumeration values
    that begin with the basic characters 0x1ea0, 0x1ecc, 0x1ef9, 0x1f00,
    0x1f0a, 0x1f15, 0x1f18, 0x1f1a, 0x1f1d, 0x1f20, 0x1f32, 0x1f45,
    0x1f48, 0x1f4a, 0x1f4d, 0x1f51, 0x1f53, 0x1f55, 0x1f57, 0x1f59. The
    document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m19.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m19_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00401m18_positive():
    """
    Enumeration values begin with the basic characters 0x11ab, 0x11ae,
    0x11ae, 0x11af, 0x11b7, 0x11b7, 0x11b8, 0x11ba, 0x11bc, 0x11bf,
    0x11c2, 0x11eb, 0x11f0, 0x11f9, 0x1e00, 0x1e4a, 0x1e95, 0x1e9b (valid
    schema) Declare a simple type based on NCName and restricted with 18
    enumeration values                               that begin with the
    basic characters 0x11ab, 0x11ae, 0x11ae, 0x11af, 0x11b7, 0x11b7,
    0x11b8, 0x11ba, 0x11bc, 0x11bf, 0x11c2, 0x11eb, 0x11f0, 0x11f9,
    0x1e00, 0x1e4a, 0x1e95, 0x1e9b. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m18.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m18_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00401m17_positive():
    """
    Enumeration values begin with the basic characters 0x115f, 0x1160,
    0x1161, 0x1163, 0x1165, 0x1167, 0x1169, 0x116d, 0x116d, 0x116e,
    0x1172, 0x1172, 0x1173, 0x1175, 0x119e, 0x11a8 (valid schema) Declare
    a simple type based on NCName and restricted with 16 enumeration
    values                               that begin with the basic
    characters 0x115f, 0x1160, 0x1161, 0x1163, 0x1165, 0x1167, 0x1169,
    0x116d, 0x116d, 0x116e, 0x1172, 0x1172, 0x1173, 0x1175, 0x119e,
    0x11a8. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m17.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m17_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00401m16_positive():
    """
    Enumeration values begin with the basic characters 0x110b, 0x110b,
    0x110c, 0x110e, 0x1110, 0x1112, 0x113c, 0x113e, 0x1140, 0x114c,
    0x114e, 0x1150, 0x1154, 0x1154, 0x1155, 0x1159 (valid schema) Declare
    a simple type based on NCName and restricted with 16 enumeration
    values                               that begin with the basic
    characters 0x110b, 0x110b, 0x110c, 0x110e, 0x1110, 0x1112, 0x113c,
    0x113e, 0x1140, 0x114c, 0x114e, 0x1150, 0x1154, 0x1154, 0x1155,
    0x1159. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m16.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m16_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00401m15_positive():
    """
    Enumeration values begin with the basic characters 0x0eb0, 0x0eb2,
    0x0eb2, 0x0eb3, 0x0ebd, 0x0ec0, 0x0ec2, 0x0ec4, 0x0f40, 0x0f43,
    0x0f47, 0x0f49, 0x0f59, 0x0f69, 0x1100, 0x1102, 0x1102, 0x1103,
    0x1105, 0x1106, 0x1107, 0x1109 (valid schema) Declare a simple type
    based on NCName and restricted with 22 enumeration values
    that begin with the basic characters 0x0eb0, 0x0eb2, 0x0eb2, 0x0eb3,
    0x0ebd, 0x0ec0, 0x0ec2, 0x0ec4, 0x0f40, 0x0f43, 0x0f47, 0x0f49,
    0x0f59, 0x0f69, 0x1100, 0x1102, 0x1102, 0x1103, 0x1105, 0x1106,
    0x1107, 0x1109. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m15.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m15_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00401m14_positive():
    """
    Enumeration values begin with the basic characters 0x0e87, 0x0e87,
    0x0e88, 0x0e8a, 0x0e8d, 0x0e94, 0x0e95, 0x0e97, 0x0e99, 0x0e9c,
    0x0e9f, 0x0ea1, 0x0ea2, 0x0ea3, 0x0ea5, 0x0ea7, 0x0eaa, 0x0eaa,
    0x0eab, 0x0ead, 0x0ead, 0x0eae (valid schema) Declare a simple type
    based on NCName and restricted with 22 enumeration values
    that begin with the basic characters 0x0e87, 0x0e87, 0x0e88, 0x0e8a,
    0x0e8d, 0x0e94, 0x0e95, 0x0e97, 0x0e99, 0x0e9c, 0x0e9f, 0x0ea1,
    0x0ea2, 0x0ea3, 0x0ea5, 0x0ea7, 0x0eaa, 0x0eaa, 0x0eab, 0x0ead,
    0x0ead, 0x0eae. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m14.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m14_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00401m13_positive():
    """
    Enumeration values begin with the basic characters 0x0d0e, 0x0d0f,
    0x0d10, 0x0d12, 0x0d1d, 0x0d28, 0x0d2a, 0x0d31, 0x0d39, 0x0d60,
    0x0d60, 0x0d61, 0x0e01, 0x0e17, 0x0e2e, 0x0e30, 0x0e32, 0x0e32,
    0x0e33, 0x0e40, 0x0e42, 0x0e45, 0x0e81, 0x0e81, 0x0e82, 0x0e84 (valid
    schema) Declare a simple type based on NCName and restricted with 26
    enumeration values                               that begin with the
    basic characters 0x0d0e, 0x0d0f, 0x0d10, 0x0d12, 0x0d1d, 0x0d28,
    0x0d2a, 0x0d31, 0x0d39, 0x0d60, 0x0d60, 0x0d61, 0x0e01, 0x0e17,
    0x0e2e, 0x0e30, 0x0e32, 0x0e32, 0x0e33, 0x0e40, 0x0e42, 0x0e45,
    0x0e81, 0x0e81, 0x0e82, 0x0e84. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m13.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m13_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00401m12_positive():
    """
    Enumeration values begin with the basic characters 0x0c35, 0x0c37,
    0x0c39, 0x0c60, 0x0c60, 0x0c61, 0x0c85, 0x0c88, 0x0c8c, 0x0c8e,
    0x0c8f, 0x0c90, 0x0c92, 0x0c9d, 0x0ca8, 0x0caa, 0x0cae, 0x0cb3,
    0x0cb5, 0x0cb7, 0x0cb9, 0x0cde, 0x0ce0, 0x0ce0, 0x0ce1, 0x0d05,
    0x0d08, 0x0d0c (valid schema) Declare a simple type based on NCName
    and restricted with 28 enumeration values
    that begin with the basic characters 0x0c35, 0x0c37, 0x0c39, 0x0c60,
    0x0c60, 0x0c61, 0x0c85, 0x0c88, 0x0c8c, 0x0c8e, 0x0c8f, 0x0c90,
    0x0c92, 0x0c9d, 0x0ca8, 0x0caa, 0x0cae, 0x0cb3, 0x0cb5, 0x0cb7,
    0x0cb9, 0x0cde, 0x0ce0, 0x0ce0, 0x0ce1, 0x0d05, 0x0d08, 0x0d0c. The
    document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m12.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m12_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00401m11_positive():
    """
    Enumeration values begin with the basic characters 0x0b9c, 0x0b9e,
    0x0b9e, 0x0b9f, 0x0ba3, 0x0ba3, 0x0ba4, 0x0ba8, 0x0ba9, 0x0baa,
    0x0bae, 0x0bb1, 0x0bb5, 0x0bb7, 0x0bb8, 0x0bb9, 0x0c05, 0x0c08,
    0x0c0c, 0x0c0e, 0x0c0f, 0x0c10, 0x0c12, 0x0c1d, 0x0c28, 0x0c2a,
    0x0c2e, 0x0c33 (valid schema) Declare a simple type based on NCName
    and restricted with 28 enumeration values
    that begin with the basic characters 0x0b9c, 0x0b9e, 0x0b9e, 0x0b9f,
    0x0ba3, 0x0ba3, 0x0ba4, 0x0ba8, 0x0ba9, 0x0baa, 0x0bae, 0x0bb1,
    0x0bb5, 0x0bb7, 0x0bb8, 0x0bb9, 0x0c05, 0x0c08, 0x0c0c, 0x0c0e,
    0x0c0f, 0x0c10, 0x0c12, 0x0c1d, 0x0c28, 0x0c2a, 0x0c2e, 0x0c33. The
    document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m11.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m11_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00401m10_positive():
    """
    Enumeration values begin with the basic characters 0x0b2a, 0x0b2d,
    0x0b30, 0x0b32, 0x0b32, 0x0b33, 0x0b36, 0x0b37, 0x0b39, 0x0b3d,
    0x0b5c, 0x0b5c, 0x0b5d, 0x0b5f, 0x0b60, 0x0b61, 0x0b85, 0x0b87,
    0x0b8a, 0x0b8e, 0x0b8f, 0x0b90, 0x0b92, 0x0b93, 0x0b95, 0x0b99,
    0x0b99, 0x0b9a (valid schema) Declare a simple type based on NCName
    and restricted with 28 enumeration values
    that begin with the basic characters 0x0b2a, 0x0b2d, 0x0b30, 0x0b32,
    0x0b32, 0x0b33, 0x0b36, 0x0b37, 0x0b39, 0x0b3d, 0x0b5c, 0x0b5c,
    0x0b5d, 0x0b5f, 0x0b60, 0x0b61, 0x0b85, 0x0b87, 0x0b8a, 0x0b8e,
    0x0b8f, 0x0b90, 0x0b92, 0x0b93, 0x0b95, 0x0b99, 0x0b99, 0x0b9a. The
    document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m10.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m10_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00401m1_positive():
    """
    Enumeration values begin with the basic characters 0x0041, 0x004d,
    0x005a, 0x0061, 0x0064, 0x0068, 0x006a, 0x0072, 0x007a, 0x00c0,
    0x00cb, 0x00d6, 0x00d8, 0x00db, 0x00de, 0x00e0, 0x00eb, 0x00f6,
    0x00f8, 0x00fb, 0x00ff, 0x0100, 0x0118, 0x0131, 0x0134, 0x0139,
    0x013e, 0x0141, 0x0144, 0x0148 (valid schema) Declare a simple type
    based on NCName and restricted with 30 enumeration values
    that begin with the basic characters 0x0041, 0x004d, 0x005a, 0x0061,
    0x0064, 0x0068, 0x006a, 0x0072, 0x007a, 0x00c0, 0x00cb, 0x00d6,
    0x00d8, 0x00db, 0x00de, 0x00e0, 0x00eb, 0x00f6, 0x00f8, 0x00fb,
    0x00ff, 0x0100, 0x0118, 0x0131, 0x0134, 0x0139, 0x013e, 0x0141,
    0x0144, 0x0148. The document uses each of the values.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m1.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00401m/ST_facets00401m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_st_facets00301m_st_facets00301m1_p():
    """
    Enumeration facet restricts string type (valid schema) Base type
    string restricted with two enumeration values '3.14' and 'int'.
    Negative document tries to use value '3,14'.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00301m/ST_facets00301m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00301m/ST_facets00301m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00301m_st_facets00301m1_n():
    """
    Enumeration facet restricts string type (valid schema) Base type
    string restricted with two enumeration values '3.14' and 'int'.
    Negative document tries to use value '3,14'.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00301m/ST_facets00301m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00301m/ST_facets00301m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m9_positive():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m9.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m9_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m9_negative():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m9.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m9_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m8_positive():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m8.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m8_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m8_negative():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m8.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m8_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m7_positive():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m7.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m7_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m7_negative():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m7.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m7_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m6_positive():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m6.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m6_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m6_negative():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m6.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m6_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m5_positive():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m5.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m5_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m5_negative():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m5.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m5_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m4_positive():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m4.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m4_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m4_negative():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m4.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m4_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m3_positive():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m3.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m3_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m3_negative():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m3.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m3_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m2_positive():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m2.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m2_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m2_negative():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m2.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m2_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m16_positive():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m16.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m16_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m16_negative():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m16.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m16_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m15_positive():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m15.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m15_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m15_negative():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m15.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m15_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m14_positive():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m14.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m14_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m14_negative():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m14.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m14_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m13_positive():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m13.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m13_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m13_negative():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m13.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m13_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m12_positive():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m12.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m12_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m12_negative():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m12.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m12_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m11_positive():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m11.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m11_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m11_negative():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m11.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m11_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m10_positive():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m10.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m10_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m10_negative():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m10.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m10_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m1_positive():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m1.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00201m1_negative():
    """
    maxExclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m1.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00201m/ST_facets00201m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00124m1_positive():
    """
    maxInclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00124m/ST_facets00124m1.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00124m/ST_facets00124m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00124m1_negative():
    """
    maxInclusive facet (valid schema) {facets} for each simple type
    definition are selected from those defined in [XML Schemas:
    Datatypes].
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00124m/ST_facets00124m1.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00124m/ST_facets00124m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00123m_st_facets00123m1_p():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00123m/ST_facets00123m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00123m/ST_facets00123m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00123m_st_facets00123m1_n():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00123m/ST_facets00123m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00123m/ST_facets00123m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00122m_st_facets00122m1_p():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00122m/ST_facets00122m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00122m/ST_facets00122m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00122m_st_facets00122m1_n():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00122m/ST_facets00122m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00122m/ST_facets00122m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00121m_st_facets00121m1_p():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00121m/ST_facets00121m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00121m/ST_facets00121m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00121m_st_facets00121m1_n():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00121m/ST_facets00121m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00121m/ST_facets00121m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00120m_st_facets00120m1_p():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00120m/ST_facets00120m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00120m/ST_facets00120m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00120m_st_facets00120m1_n():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00120m/ST_facets00120m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00120m/ST_facets00120m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00119m_st_facets00119m1_p():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00119m/ST_facets00119m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00119m/ST_facets00119m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00119m_st_facets00119m1_n():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00119m/ST_facets00119m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00119m/ST_facets00119m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00118m_st_facets00118m1_p():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00118m/ST_facets00118m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00118m/ST_facets00118m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00118m_st_facets00118m1_n():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00118m/ST_facets00118m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00118m/ST_facets00118m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00117m_st_facets00117m1_p():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00117m/ST_facets00117m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00117m/ST_facets00117m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00117m_st_facets00117m1_n():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00117m/ST_facets00117m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00117m/ST_facets00117m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00116m_st_facets00116m1_p():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00116m/ST_facets00116m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00116m/ST_facets00116m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00116m_st_facets00116m1_n():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00116m/ST_facets00116m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00116m/ST_facets00116m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00115m_st_facets00115m1_p():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00115m/ST_facets00115m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00115m/ST_facets00115m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00115m_st_facets00115m1_n():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00115m/ST_facets00115m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00115m/ST_facets00115m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00114m_st_facets00114m1_p():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00114m/ST_facets00114m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00114m/ST_facets00114m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00114m_st_facets00114m1_n():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00114m/ST_facets00114m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00114m/ST_facets00114m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00113m_st_facets00113m1_p():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00113m/ST_facets00113m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00113m/ST_facets00113m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00113m_st_facets00113m1_n():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00113m/ST_facets00113m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00113m/ST_facets00113m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00112m_st_facets00112m1_p():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00112m/ST_facets00112m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00112m/ST_facets00112m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00112m_st_facets00112m1_n():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00112m/ST_facets00112m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00112m/ST_facets00112m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00111m_st_facets00111m1_p():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00111m/ST_facets00111m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00111m/ST_facets00111m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00111m_st_facets00111m1_n():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00111m/ST_facets00111m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00111m/ST_facets00111m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00110m_st_facets00110m1_p():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00110m/ST_facets00110m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00110m/ST_facets00110m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00110m_st_facets00110m1_n():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00110m/ST_facets00110m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00110m/ST_facets00110m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00109m_st_facets00109m1_p():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00109m/ST_facets00109m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00109m/ST_facets00109m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00109m_st_facets00109m1_n():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00109m/ST_facets00109m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00109m/ST_facets00109m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00108m_st_facets00108m1_p():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00108m/ST_facets00108m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00108m/ST_facets00108m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00108m_st_facets00108m1_n():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00108m/ST_facets00108m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00108m/ST_facets00108m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00107m_st_facets00107m1_p():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00107m/ST_facets00107m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00107m/ST_facets00107m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00107m_st_facets00107m1_n():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00107m/ST_facets00107m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00107m/ST_facets00107m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00106m_st_facets00106m1_p():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00106m/ST_facets00106m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00106m/ST_facets00106m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00106m_st_facets00106m1_n():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00106m/ST_facets00106m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00106m/ST_facets00106m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00105m_st_facets00105m1_p():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00105m/ST_facets00105m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00105m/ST_facets00105m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00105m_st_facets00105m1_n():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00105m/ST_facets00105m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00105m/ST_facets00105m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00104m_st_facets00104m1_p():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00104m/ST_facets00104m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00104m/ST_facets00104m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00104m_st_facets00104m1_n():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00104m/ST_facets00104m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00104m/ST_facets00104m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00103m_st_facets00103m1_p():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00103m/ST_facets00103m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00103m/ST_facets00103m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00103m_st_facets00103m1_n():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00103m/ST_facets00103m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00103m/ST_facets00103m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00102m_st_facets00102m1_p():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00102m/ST_facets00102m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00102m/ST_facets00102m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00102m_st_facets00102m1_n():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00102m/ST_facets00102m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00102m/ST_facets00102m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00101m_st_facets00101m1_p():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00101m/ST_facets00101m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00101m/ST_facets00101m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00101m_st_facets00101m1_n():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00101m/ST_facets00101m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00101m/ST_facets00101m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00101m_st_facets00101m2_p():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00101m/ST_facets00101m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00101m/ST_facets00101m2_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_facets00101m_st_facets00101m3_p():
    """
    {facets} restriction (valid schema) The {facets} of R constitute a
    restriction of the {facets} of B with respect to S.
    """
    assert_bindings(
        schema="sunData/SType/ST_facets/ST_facets00101m/ST_facets00101m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_facets/ST_facets00101m/ST_facets00101m3_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_basetd00302m_st_base_td00302m1_p():
    """
    the 'union' alternative is chosen (valid schema) If the 'list' or
    'union' alternative is chosen, then the *simple ur-type definition*.
    """
    assert_bindings(
        schema="sunData/SType/ST_baseTD/ST_baseTD00302m/ST_baseTD00302m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_baseTD/ST_baseTD00302m/ST_baseTD00302m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_basetd00302m_st_base_td00302m1_n():
    """
    the 'union' alternative is chosen (valid schema) If the 'list' or
    'union' alternative is chosen, then the *simple ur-type definition*.
    """
    assert_bindings(
        schema="sunData/SType/ST_baseTD/ST_baseTD00302m/ST_baseTD00302m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_baseTD/ST_baseTD00302m/ST_baseTD00302m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_basetd00302m_st_base_td00302m2_p():
    """
    the 'union' alternative is chosen (valid schema) If the 'list' or
    'union' alternative is chosen, then the *simple ur-type definition*.
    """
    assert_bindings(
        schema="sunData/SType/ST_baseTD/ST_baseTD00302m/ST_baseTD00302m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_baseTD/ST_baseTD00302m/ST_baseTD00302m2_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_basetd00302m_st_base_td00302m2_n():
    """
    the 'union' alternative is chosen (valid schema) If the 'list' or
    'union' alternative is chosen, then the *simple ur-type definition*.
    """
    assert_bindings(
        schema="sunData/SType/ST_baseTD/ST_baseTD00302m/ST_baseTD00302m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_baseTD/ST_baseTD00302m/ST_baseTD00302m2_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_basetd00302m_st_base_td00302m3_n():
    """
    the 'union' alternative is chosen (valid schema) If the 'list' or
    'union' alternative is chosen, then the *simple ur-type definition*.
    """
    assert_bindings(
        schema="sunData/SType/ST_baseTD/ST_baseTD00302m/ST_baseTD00302m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_baseTD/ST_baseTD00302m/ST_baseTD00302m3_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_basetd00301m_st_base_td00301m1_p():
    """
    the 'list' alternative is chosen (valid schema) If the 'list' or
    'union' alternative is chosen, then the *simple ur-type definition*.
    """
    assert_bindings(
        schema="sunData/SType/ST_baseTD/ST_baseTD00301m/ST_baseTD00301m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_baseTD/ST_baseTD00301m/ST_baseTD00301m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_basetd00301m_st_base_td00301m1_n():
    """
    the 'list' alternative is chosen (valid schema) If the 'list' or
    'union' alternative is chosen, then the *simple ur-type definition*.
    """
    assert_bindings(
        schema="sunData/SType/ST_baseTD/ST_baseTD00301m/ST_baseTD00301m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_baseTD/ST_baseTD00301m/ST_baseTD00301m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_basetd00201m_st_base_td00201m1_p():
    """
    The base type is defined by the type of 'simpleType' among the
    [children] of 'restriction' (valid schema) If the base [attribute] is
    absent the type definition corresponding to
    the 'simpleType' among the [children] of 'restriction'.
    """
    assert_bindings(
        schema="sunData/SType/ST_baseTD/ST_baseTD00201m/ST_baseTD00201m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_baseTD/ST_baseTD00201m/ST_baseTD00201m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_basetd00201m_st_base_td00201m1_n():
    """
    The base type is defined by the type of 'simpleType' among the
    [children] of 'restriction' (valid schema) If the base [attribute] is
    absent the type definition corresponding to
    the 'simpleType' among the [children] of 'restriction'.
    """
    assert_bindings(
        schema="sunData/SType/ST_baseTD/ST_baseTD00201m/ST_baseTD00201m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_baseTD/ST_baseTD00201m/ST_baseTD00201m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_basetd00101m_st_base_td00101m1_p():
    """
    The value of the base [attribute] specifies the base type definition
    (valid schema) If the 'restriction' alternative is chosen, then the
    type                                  definition *resolved* to by the
    *actual value* of the base [attribute]
    of 'restriction'.
    """
    assert_bindings(
        schema="sunData/SType/ST_baseTD/ST_baseTD00101m/ST_baseTD00101m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_baseTD/ST_baseTD00101m/ST_baseTD00101m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_basetd00101m_st_base_td00101m1_n():
    """
    The value of the base [attribute] specifies the base type definition
    (valid schema) If the 'restriction' alternative is chosen, then the
    type                                  definition *resolved* to by the
    *actual value* of the base [attribute]
    of 'restriction'.
    """
    assert_bindings(
        schema="sunData/SType/ST_baseTD/ST_baseTD00101m/ST_baseTD00101m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_baseTD/ST_baseTD00101m/ST_baseTD00101m1_n.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_st_basetd00101m_st_base_td00101m2_p():
    """
    The value of the base [attribute] specifies the base type definition
    (valid schema) If the 'restriction' alternative is chosen, then the
    type                                  definition *resolved* to by the
    *actual value* of the base [attribute]
    of 'restriction'.
    """
    assert_bindings(
        schema="sunData/SType/ST_baseTD/ST_baseTD00101m/ST_baseTD00101m.xsd",
        is_valid=True,
        instance="sunData/SType/ST_baseTD/ST_baseTD00101m/ST_baseTD00101m2_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_annotation00101m2_positive():
    """
    machine-targeted annotation (valid schema) Annotations provide for
    human- and machine-targeted annotations of schema components.
    """
    assert_bindings(
        schema="sunData/SType/ST_annotation/ST_annotation00101m/ST_annotation00101m2.xsd",
        is_valid=True,
        instance="sunData/SType/ST_annotation/ST_annotation00101m/ST_annotation00101m2_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_st_annotation00101m1_positive():
    """
    human-targeted annotation (valid schema) Annotations provide for
    human- and machine-targeted annotations of schema components.
    """
    assert_bindings(
        schema="sunData/SType/ST_annotation/ST_annotation00101m/ST_annotation00101m1.xsd",
        is_valid=True,
        instance="sunData/SType/ST_annotation/ST_annotation00101m/ST_annotation00101m1_p.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_annotations00101m6_positive():
    """
    machine-targeted placed at the end annotation for the schema itself
    (valid schema) Annotations provide for human- and machine-targeted
    annotations of schema components.                               In the
    test the machine-targeted annotation                               is
    provided for the schema itself.                              The
    annotation is placed at the end.
    """
    assert_bindings(
        schema="sunData/Schema/annotations/annotations00101m/annotations00101m6.xsd",
        is_valid=True,
        instance="sunData/Schema/annotations/annotations00101m/annotations00101m6_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_annotations00101m5_positive():
    """
    machine-targeted double annotation for the schema itself (valid
    schema) Annotations provide for human- and machine-targeted
    annotations of schema components.                               In the
    test the machine-targeted annotation                               is
    provided for the schema itself.                              The
    annotation is specified twice.
    """
    assert_bindings(
        schema="sunData/Schema/annotations/annotations00101m/annotations00101m5.xsd",
        is_valid=True,
        instance="sunData/Schema/annotations/annotations00101m/annotations00101m5_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_annotations00101m4_positive():
    """
    machine-targeted  annotation for the schema itself (valid schema)
    Annotations provide for human- and machine-targeted
    annotations of schema components.                               In the
    test the machine-targeted annotation                               is
    provided for the schema itself.
    """
    assert_bindings(
        schema="sunData/Schema/annotations/annotations00101m/annotations00101m4.xsd",
        is_valid=True,
        instance="sunData/Schema/annotations/annotations00101m/annotations00101m4_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_annotations00101m3_positive():
    """
    human-targeted placed at the end annotation for the schema itself
    (valid schema) Annotations provide for human- and machine-targeted
    annotations of schema components.                               In the
    test the human-targeted annotation                               is
    provided for the schema itself.                              The
    annotation is placed at the end.
    """
    assert_bindings(
        schema="sunData/Schema/annotations/annotations00101m/annotations00101m3.xsd",
        is_valid=True,
        instance="sunData/Schema/annotations/annotations00101m/annotations00101m3_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_annotations00101m2_positive():
    """
    human-targeted double annotation for the schema itself (valid schema)
    Annotations provide for human- and machine-targeted
    annotations of schema components.                               In the
    test the human-targeted annotation                               is
    provided for the schema itself.                              The
    annotation is specified twice.
    """
    assert_bindings(
        schema="sunData/Schema/annotations/annotations00101m/annotations00101m2.xsd",
        is_valid=True,
        instance="sunData/Schema/annotations/annotations00101m/annotations00101m2_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_annotations00101m1_positive():
    """
    human-targeted  annotation for the schema itself (valid schema)
    Annotations provide for human- and machine-targeted
    annotations of schema components.                               In the
    test the human-targeted annotation                               is
    provided for the schema itself.
    """
    assert_bindings(
        schema="sunData/Schema/annotations/annotations00101m/annotations00101m1.xsd",
        is_valid=True,
        instance="sunData/Schema/annotations/annotations00101m/annotations00101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_pscontents00302m2_positive():
    """
    processContents='lax' and the declaration is not available (valid
    schema) {process contents} controls the impact on *assessment* of the
    information items                               allowed by wildcards,
    as follows:
    lax                                     If the item, or any items
    among its [children] if it's an element information
    item, has a uniquely determined declaration available, it must be
    *valid* with                                     respect to that
    definition, that is, *validate* where you can, don't worry when you
    can't.
    """
    assert_bindings(
        schema="sunData/Wildcard/psContents/psContents00302m/psContents00302m2.xsd",
        is_valid=True,
        instance="sunData/Wildcard/psContents/psContents00302m/psContents00302m2_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_pscontents00302m2_negative():
    """
    processContents='lax' and the declaration is not available (valid
    schema) {process contents} controls the impact on *assessment* of the
    information items                               allowed by wildcards,
    as follows:
    lax                                     If the item, or any items
    among its [children] if it's an element information
    item, has a uniquely determined declaration available, it must be
    *valid* with                                     respect to that
    definition, that is, *validate* where you can, don't worry when you
    can't.
    """
    assert_bindings(
        schema="sunData/Wildcard/psContents/psContents00302m/psContents00302m2.xsd",
        is_valid=True,
        instance="sunData/Wildcard/psContents/psContents00302m/psContents00302m2_n.xml",
        instance_is_valid=False,
        class_name="",
        version="1.0",
    )


def test_pscontents00302m1_positive():
    """
    processContents='lax' and the declaration is available (valid schema)
    {process contents} controls the impact on *assessment* of the
    information items                               allowed by wildcards,
    as follows:
    lax                                     If the item, or any items
    among its [children] if it's an element information
    item, has a uniquely determined declaration available, it must be
    *valid* with                                     respect to that
    definition, that is, *validate* where you can, don't worry when you
    can't.
    """
    assert_bindings(
        schema="sunData/Wildcard/psContents/psContents00302m/psContents00302m1.xsd",
        is_valid=True,
        instance="sunData/Wildcard/psContents/psContents00302m/psContents00302m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_pscontents00302m1_negative():
    """
    processContents='lax' and the declaration is available (valid schema)
    {process contents} controls the impact on *assessment* of the
    information items                               allowed by wildcards,
    as follows:
    lax                                     If the item, or any items
    among its [children] if it's an element information
    item, has a uniquely determined declaration available, it must be
    *valid* with                                     respect to that
    definition, that is, *validate* where you can, don't worry when you
    can't.
    """
    assert_bindings(
        schema="sunData/Wildcard/psContents/psContents00302m/psContents00302m1.xsd",
        is_valid=True,
        instance="sunData/Wildcard/psContents/psContents00302m/psContents00302m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_pscontents00301m2_positive():
    """
    processContents='lax' and the declaration is not available (valid
    schema) {process contents} controls the impact on *assessment* of the
    information items                               allowed by wildcards,
    as follows:
    lax                                     If the item, or any items
    among its [children] if it's an element information
    item, has a uniquely determined declaration available, it must be
    *valid* with                                     respect to that
    definition, that is, *validate* where you can, don't worry when you
    can't.
    """
    assert_bindings(
        schema="sunData/Wildcard/psContents/psContents00301m/psContents00301m2.xsd",
        is_valid=True,
        instance="sunData/Wildcard/psContents/psContents00301m/psContents00301m2_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_pscontents00301m2_negative():
    """
    processContents='lax' and the declaration is not available (valid
    schema) {process contents} controls the impact on *assessment* of the
    information items                               allowed by wildcards,
    as follows:
    lax                                     If the item, or any items
    among its [children] if it's an element information
    item, has a uniquely determined declaration available, it must be
    *valid* with                                     respect to that
    definition, that is, *validate* where you can, don't worry when you
    can't.
    """
    assert_bindings(
        schema="sunData/Wildcard/psContents/psContents00301m/psContents00301m2.xsd",
        is_valid=True,
        instance="sunData/Wildcard/psContents/psContents00301m/psContents00301m2_n.xml",
        instance_is_valid=False,
        class_name="",
        version="1.0",
    )


def test_pscontents00301m1_positive():
    """
    processContents='lax' and the declaration is available (valid schema)
    {process contents} controls the impact on *assessment* of the
    information items                               allowed by wildcards,
    as follows:
    lax                                     If the item, or any items
    among its [children] if it's an element information
    item, has a uniquely determined declaration available, it must be
    *valid* with                                     respect to that
    definition, that is, *validate* where you can, don't worry when you
    can't.
    """
    assert_bindings(
        schema="sunData/Wildcard/psContents/psContents00301m/psContents00301m1.xsd",
        is_valid=True,
        instance="sunData/Wildcard/psContents/psContents00301m/psContents00301m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_pscontents00301m1_negative():
    """
    processContents='lax' and the declaration is available (valid schema)
    {process contents} controls the impact on *assessment* of the
    information items                               allowed by wildcards,
    as follows:
    lax                                     If the item, or any items
    among its [children] if it's an element information
    item, has a uniquely determined declaration available, it must be
    *valid* with                                     respect to that
    definition, that is, *validate* where you can, don't worry when you
    can't.
    """
    assert_bindings(
        schema="sunData/Wildcard/psContents/psContents00301m/psContents00301m1.xsd",
        is_valid=True,
        instance="sunData/Wildcard/psContents/psContents00301m/psContents00301m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_pscontents00202m1_positive():
    """
    processContents='skip' (valid schema) {process contents} controls the
    impact on *assessment* of the information items
    allowed by wildcards, as follows:
    skip                                     No constraints at all: the
    item must simply be well-formed XML.
    """
    assert_bindings(
        schema="sunData/Wildcard/psContents/psContents00202m/psContents00202m1.xsd",
        is_valid=True,
        instance="sunData/Wildcard/psContents/psContents00202m/psContents00202m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_pscontents00201m1_positive():
    """
    processContents='skip' (valid schema) {process contents} controls the
    impact on *assessment* of the information items
    allowed by wildcards, as follows:
    skip                                     No constraints at all: the
    item must simply be well-formed XML.
    """
    assert_bindings(
        schema="sunData/Wildcard/psContents/psContents00201m/psContents00201m1.xsd",
        is_valid=True,
        instance="sunData/Wildcard/psContents/psContents00201m/psContents00201m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_pscontents00201m1_negative():
    """
    processContents='skip' (valid schema) {process contents} controls the
    impact on *assessment* of the information items
    allowed by wildcards, as follows:
    skip                                     No constraints at all: the
    item must simply be well-formed XML.
    """
    assert_bindings(
        schema="sunData/Wildcard/psContents/psContents00201m/psContents00201m1.xsd",
        is_valid=True,
        instance="sunData/Wildcard/psContents/psContents00201m/psContents00201m1_n.xml",
        instance_is_valid=False,
        class_name="",
        version="1.0",
    )


def test_pscontents00102m2_negative():
    """
    processContents='strict' and the declaration is not available (valid
    schema) {process contents} controls the impact on *assessment* of the
    information items                               allowed by wildcards,
    as follows:
    strict                                     There must be a top-level
    declaration for the item available, or the item
    must have an xsi:type, and the item must be *valid* as appropriate.
    """
    assert_bindings(
        schema="sunData/Wildcard/psContents/psContents00102m/psContents00102m2.xsd",
        is_valid=True,
        instance="sunData/Wildcard/psContents/psContents00102m/psContents00102m2_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_pscontents00102m1_positive():
    """
    processContents='strict' and the declaration is available (valid
    schema) {process contents} controls the impact on *assessment* of the
    information items                               allowed by wildcards,
    as follows:
    strict                                     There must be a top-level
    declaration for the item available, or the item
    must have an xsi:type, and the item must be *valid* as appropriate.
    """
    assert_bindings(
        schema="sunData/Wildcard/psContents/psContents00102m/psContents00102m1.xsd",
        is_valid=True,
        instance="sunData/Wildcard/psContents/psContents00102m/psContents00102m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_pscontents00102m1_negative():
    """
    processContents='strict' and the declaration is available (valid
    schema) {process contents} controls the impact on *assessment* of the
    information items                               allowed by wildcards,
    as follows:
    strict                                     There must be a top-level
    declaration for the item available, or the item
    must have an xsi:type, and the item must be *valid* as appropriate.
    """
    assert_bindings(
        schema="sunData/Wildcard/psContents/psContents00102m/psContents00102m1.xsd",
        is_valid=True,
        instance="sunData/Wildcard/psContents/psContents00102m/psContents00102m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_pscontents00101m2_negative():
    """
    processContents='strict' and the declaration is not available (valid
    schema) {process contents} controls the impact on *assessment* of the
    information items                               allowed by wildcards,
    as follows:
    strict                                     There must be a top-level
    declaration for the item available, or the item
    must have an xsi:type, and the item must be *valid* as appropriate.
    """
    assert_bindings(
        schema="sunData/Wildcard/psContents/psContents00101m/psContents00101m2.xsd",
        is_valid=True,
        instance="sunData/Wildcard/psContents/psContents00101m/psContents00101m2_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_pscontents00101m1_positive():
    """
    processContents='strict' and the declaration is available (valid
    schema) {process contents} controls the impact on *assessment* of the
    information items                               allowed by wildcards,
    as follows:
    strict                                     There must be a top-level
    declaration for the item available, or the item
    must have an xsi:type, and the item must be *valid* as appropriate.
    """
    assert_bindings(
        schema="sunData/Wildcard/psContents/psContents00101m/psContents00101m1.xsd",
        is_valid=True,
        instance="sunData/Wildcard/psContents/psContents00101m/psContents00101m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_pscontents00101m1_negative():
    """
    processContents='strict' and the declaration is available (valid
    schema) {process contents} controls the impact on *assessment* of the
    information items                               allowed by wildcards,
    as follows:
    strict                                     There must be a top-level
    declaration for the item available, or the item
    must have an xsi:type, and the item must be *valid* as appropriate.
    """
    assert_bindings(
        schema="sunData/Wildcard/psContents/psContents00101m/psContents00101m1.xsd",
        is_valid=True,
        instance="sunData/Wildcard/psContents/psContents00101m/psContents00101m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_nsconstraint00302m1_positive():
    """
    namespace='ns_test1 ns_test2' (valid schema) {namespace constraint}
    provides for *validation* of attribute and element items that:
    4. (a set whose members are either namespace names or *absent*) have
    any of the specified                                    namespaces
    and/or, if *absent* is included in the set, are unqualified.
    """
    assert_bindings(
        schema="sunData/Wildcard/nsConstraint/nsConstraint00302m/nsConstraint00302m1.xsd",
        is_valid=True,
        instance="sunData/Wildcard/nsConstraint/nsConstraint00302m/nsConstraint00302m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_nsconstraint00302m1_negative():
    """
    namespace='ns_test1 ns_test2' (valid schema) {namespace constraint}
    provides for *validation* of attribute and element items that:
    4. (a set whose members are either namespace names or *absent*) have
    any of the specified                                    namespaces
    and/or, if *absent* is included in the set, are unqualified.
    """
    assert_bindings(
        schema="sunData/Wildcard/nsConstraint/nsConstraint00302m/nsConstraint00302m1.xsd",
        is_valid=True,
        instance="sunData/Wildcard/nsConstraint/nsConstraint00302m/nsConstraint00302m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_nsconstraint00301m1_positive():
    """
    namespace='ns_test1 ns_test2' (valid schema) {namespace constraint}
    provides for *validation* of attribute and element items that:
    4. (a set whose members are either namespace names or *absent*) have
    any of the specified                                    namespaces
    and/or, if *absent* is included in the set, are unqualified.
    """
    assert_bindings(
        schema="sunData/Wildcard/nsConstraint/nsConstraint00301m/nsConstraint00301m1.xsd",
        is_valid=True,
        instance="sunData/Wildcard/nsConstraint/nsConstraint00301m/nsConstraint00301m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_nsconstraint00301m1_negative():
    """
    namespace='ns_test1 ns_test2' (valid schema) {namespace constraint}
    provides for *validation* of attribute and element items that:
    4. (a set whose members are either namespace names or *absent*) have
    any of the specified                                    namespaces
    and/or, if *absent* is included in the set, are unqualified.
    """
    assert_bindings(
        schema="sunData/Wildcard/nsConstraint/nsConstraint00301m/nsConstraint00301m1.xsd",
        is_valid=True,
        instance="sunData/Wildcard/nsConstraint/nsConstraint00301m/nsConstraint00301m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_nsconstraint00202m1_positive():
    """
    namespace='##other' (valid schema) {namespace constraint} provides for
    *validation* of attribute and element items that:
    2. (not and a namespace name) have any namespace other than the
    specified namespace                                     name;
    """
    assert_bindings(
        schema="sunData/Wildcard/nsConstraint/nsConstraint00202m/nsConstraint00202m1.xsd",
        is_valid=True,
        instance="sunData/Wildcard/nsConstraint/nsConstraint00202m/nsConstraint00202m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_nsconstraint00202m1_negative():
    """
    namespace='##other' (valid schema) {namespace constraint} provides for
    *validation* of attribute and element items that:
    2. (not and a namespace name) have any namespace other than the
    specified namespace                                     name;
    """
    assert_bindings(
        schema="sunData/Wildcard/nsConstraint/nsConstraint00202m/nsConstraint00202m1.xsd",
        is_valid=True,
        instance="sunData/Wildcard/nsConstraint/nsConstraint00202m/nsConstraint00202m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_nsconstraint00201m1_positive():
    """
    namespace='##other' (valid schema) {namespace constraint} provides for
    *validation* of attribute and element items that:
    2. (not and a namespace name) have any namespace other than the
    specified namespace                                     name;
    """
    assert_bindings(
        schema="sunData/Wildcard/nsConstraint/nsConstraint00201m/nsConstraint00201m1.xsd",
        is_valid=True,
        instance="sunData/Wildcard/nsConstraint/nsConstraint00201m/nsConstraint00201m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_nsconstraint00201m1_negative():
    """
    namespace='##other' (valid schema) {namespace constraint} provides for
    *validation* of attribute and element items that:
    2. (not and a namespace name) have any namespace other than the
    specified namespace                                     name;
    """
    assert_bindings(
        schema="sunData/Wildcard/nsConstraint/nsConstraint00201m/nsConstraint00201m1.xsd",
        is_valid=True,
        instance="sunData/Wildcard/nsConstraint/nsConstraint00201m/nsConstraint00201m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_nsconstraint00102m2_positive():
    """
    default value of 'namespace' is '##any' (valid schema) {namespace
    constraint} provides for *validation* of attribute and element items
    that:                                 1. (any) have any namespace or
    are not namespace qualified;
    """
    assert_bindings(
        schema="sunData/Wildcard/nsConstraint/nsConstraint00102m/nsConstraint00102m2.xsd",
        is_valid=True,
        instance="sunData/Wildcard/nsConstraint/nsConstraint00102m/nsConstraint00102m2_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_nsconstraint00102m1_positive():
    """
    namespace='##any' (valid schema) {namespace constraint} provides for
    *validation* of attribute and element items that:
    1. (any) have any namespace or are not namespace qualified;
    """
    assert_bindings(
        schema="sunData/Wildcard/nsConstraint/nsConstraint00102m/nsConstraint00102m1.xsd",
        is_valid=True,
        instance="sunData/Wildcard/nsConstraint/nsConstraint00102m/nsConstraint00102m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_nsconstraint00101m2_positive():
    """
    default value of 'namespace' is '##any' (valid schema) {namespace
    constraint} provides for *validation* of attribute and element items
    that:                                 1. (any) have any namespace or
    are not namespace qualified;
    """
    assert_bindings(
        schema="sunData/Wildcard/nsConstraint/nsConstraint00101m/nsConstraint00101m2.xsd",
        is_valid=True,
        instance="sunData/Wildcard/nsConstraint/nsConstraint00101m/nsConstraint00101m2_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_nsconstraint00101m2_negative():
    """
    default value of 'namespace' is '##any' (valid schema) {namespace
    constraint} provides for *validation* of attribute and element items
    that:                                 1. (any) have any namespace or
    are not namespace qualified;
    """
    assert_bindings(
        schema="sunData/Wildcard/nsConstraint/nsConstraint00101m/nsConstraint00101m2.xsd",
        is_valid=True,
        instance="sunData/Wildcard/nsConstraint/nsConstraint00101m/nsConstraint00101m2_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_nsconstraint00101m1_positive():
    """
    namespace='##any' (valid schema) {namespace constraint} provides for
    *validation* of attribute and element items that:
    1. (any) have any namespace or are not namespace qualified;
    """
    assert_bindings(
        schema="sunData/Wildcard/nsConstraint/nsConstraint00101m/nsConstraint00101m1.xsd",
        is_valid=True,
        instance="sunData/Wildcard/nsConstraint/nsConstraint00101m/nsConstraint00101m1_p.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.0",
    )


def test_nsconstraint00101m1_negative():
    """
    namespace='##any' (valid schema) {namespace constraint} provides for
    *validation* of attribute and element items that:
    1. (any) have any namespace or are not namespace qualified;
    """
    assert_bindings(
        schema="sunData/Wildcard/nsConstraint/nsConstraint00101m/nsConstraint00101m1.xsd",
        is_valid=True,
        instance="sunData/Wildcard/nsConstraint/nsConstraint00101m/nsConstraint00101m1_n.xml",
        instance_is_valid=False,
        class_name="A",
        version="1.0",
    )


def test_annotation00101m7_positive_915():
    """
    machine-targeted  annotation for a wildcard schema component (any)
    (valid schema) Annotations provide for human- and machine-targeted
    annotations of schema components.                               In the
    test the machine-targeted annotation                               is
    provided for a wildcard schema component (any).
    """
    assert_bindings(
        schema="sunData/Wildcard/annotation/annotation00101m/annotation00101m7.xsd",
        is_valid=True,
        instance="sunData/Wildcard/annotation/annotation00101m/annotation00101m7_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_annotation00101m5_positive():
    """
    human-targeted  annotation for a wildcard schema component (any)
    (valid schema) Annotations provide for human- and machine-targeted
    annotations of schema components.                               In the
    test the human-targeted annotation                               is
    provided for a wildcard schema component (any).
    """
    assert_bindings(
        schema="sunData/Wildcard/annotation/annotation00101m/annotation00101m5.xsd",
        is_valid=True,
        instance="sunData/Wildcard/annotation/annotation00101m/annotation00101m5_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_annotation00101m3_positive_917():
    """
    machine-targeted  annotation for a wildcard schema component
    (anyAttribute) (valid schema) Annotations provide for human- and
    machine-targeted                               annotations of schema
    components.                               In the test the machine-
    targeted annotation                               is provided for a
    wildcard schema component (anyAttribute).
    """
    assert_bindings(
        schema="sunData/Wildcard/annotation/annotation00101m/annotation00101m3.xsd",
        is_valid=True,
        instance="sunData/Wildcard/annotation/annotation00101m/annotation00101m3_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_annotation00101m1_positive_918():
    """
    human-targeted  annotation for a wildcard schema component
    (anyAttribute) (valid schema) Annotations provide for human- and
    machine-targeted                               annotations of schema
    components.                               In the test the human-
    targeted annotation                               is provided for a
    wildcard schema component (anyAttribute).
    """
    assert_bindings(
        schema="sunData/Wildcard/annotation/annotation00101m/annotation00101m1.xsd",
        is_valid=True,
        instance="sunData/Wildcard/annotation/annotation00101m/annotation00101m1_p.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )
