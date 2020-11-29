import pytest

from tests.utils import assert_bindings


def test_member_type024_member_type024_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Attribute of union of user defined
    typees(mybool,myint,mystring) with default value
    """
    assert_bindings(
        schema="msData/additional/memberType024.xsd",
        instance="msData/additional/memberType024.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_member_type023_member_type023_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Attribute of union of user defined
    typees(mybool,myint,mystring)
    """
    assert_bindings(
        schema="msData/additional/memberType023.xsd",
        instance="msData/additional/memberType023.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_member_type022_member_type022_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Element of union of user defined
    typees(mybool,myint,mystring) with default value
    """
    assert_bindings(
        schema="msData/additional/memberType022.xsd",
        instance="msData/additional/memberType022.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_member_type021_member_type021_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Element of union of user defined
    typees(mybool,myint,mystring)
    """
    assert_bindings(
        schema="msData/additional/memberType021.xsd",
        instance="msData/additional/memberType021.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_member_type008_member_type008_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Element with default value and xsi:type: membertype
    of union(bool,int,string)
    """
    assert_bindings(
        schema="msData/additional/memberType003.xsd",
        instance="msData/additional/memberType008.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_member_type007_member_type007_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Element with xsi:type: membertype of
    union(bool,int,string)
    """
    assert_bindings(
        schema="msData/additional/memberType001.xsd",
        instance="msData/additional/memberType007.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_member_type006_member_type006_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Element with xsi:type: membertype of
    union(bool,int,string)
    """
    assert_bindings(
        schema="msData/additional/memberType001.xsd",
        instance="msData/additional/memberType006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_member_type005_member_type005_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Attribute with default value: membertype of
    union(bool,int,string)
    """
    assert_bindings(
        schema="msData/additional/memberType004.xsd",
        instance="msData/additional/memberType005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_member_type004_member_type004_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Element with default value: membertype of
    union(bool,int,string)
    """
    assert_bindings(
        schema="msData/additional/memberType003.xsd",
        instance="msData/additional/memberType004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_member_type003_member_type003_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Attribute: membertype of union(bool,int,string)
    """
    assert_bindings(
        schema="msData/additional/memberType002.xsd",
        instance="msData/additional/memberType003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_member_type002_member_type002_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Element: membertype of union(bool,int,string)
    """
    assert_bindings(
        schema="msData/additional/memberType001.xsd",
        instance="msData/additional/memberType002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_member_type001_member_type001_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Element : membertype of union(bool,int,string)
    """
    assert_bindings(
        schema="msData/additional/memberType001.xsd",
        instance="msData/additional/memberType001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default079_is_default079_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : multiple 'fixed' constraints
    """
    assert_bindings(
        schema="msData/additional/isdefault079.xsd",
        instance="msData/additional/isdefault079.xml",
        class_name="Regvaluemodopset",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default078_is_default078_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : map xml namespace in the instance to be able to
    insert default attributes from xml namespace
    """
    assert_bindings(
        schema="msData/additional/isdefault078.xsd",
        instance="msData/additional/isdefault078.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_is_default077_is_default077_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : fixed value on mixed content with invalid value in
    XML
    """
    assert_bindings(
        schema="msData/additional/isdefault076.xsd",
        instance="msData/additional/isdefault076.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default076_is_default076_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : fixed value on mixed content
    """
    assert_bindings(
        schema="msData/additional/isdefault076.xsd",
        instance="msData/additional/isdefault075.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default075_is_default075_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : default value on mixed content
    """
    assert_bindings(
        schema="msData/additional/isdefault075.xsd",
        instance="msData/additional/isdefault075.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default074_is_default074_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : attribute of type xs:anySimpleType with a default
    and fixed value
    """
    assert_bindings(
        schema="msData/additional/isdefault074.xsd",
        instance="msData/additional/isdefault074.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default073_is_default073_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : element of type xs:anyType with a default and fixed
    value
    """
    assert_bindings(
        schema="msData/additional/isdefault073.xsd",
        instance="msData/additional/isdefault073.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default072_is_default072_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : While adding default attributes with
    form="qualified", should lookup all prefixes for its namespace
    """
    assert_bindings(
        schema="msData/additional/isdefault072.xsd",
        instance="msData/additional/isdefault072.xml",
        class_name="Array",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default071_is_default071_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : element of type xs:anyType with value not matching
    the fixed value in the schema should error(valid)
    """
    assert_bindings(
        schema="msData/additional/isdefault070.xsd",
        instance="msData/additional/isdefault071.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_is_default070_is_default070_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : element of type xs:anyType with value not matching
    the fixed value in the schema should error(invalid)
    """
    assert_bindings(
        schema="msData/additional/isdefault070.xsd",
        instance="msData/additional/isdefault070.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default060_1_is_default060_1_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : test empty element typed as xsd:int with default
    value set in schema.
    """
    assert_bindings(
        schema="msData/additional/test95960_1.xsd",
        instance="msData/additional/test95960_1.xml",
        class_name="Employees",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default068_is_default068_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Attributes: IsDefault(fixed) Local Element with no
    attributes, schema HAS targetNamespace
    """
    assert_bindings(
        schema="msData/additional/isdefault062.xsd",
        instance="msData/additional/isdefault068.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default067_is_default067_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Attributes: IsDefault(fixed) Local Element with all
    attributes, schema HAS targetNamespace
    """
    assert_bindings(
        schema="msData/additional/isdefault062.xsd",
        instance="msData/additional/isdefault067.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default066_is_default066_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Attributes: IsDefault(fixed) no attributes on root
    element (empty element WITH end tag), schema HAS targetNamespace
    """
    assert_bindings(
        schema="msData/additional/isdefault061.xsd",
        instance="msData/additional/isdefault066.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default065_is_default065_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Attributes: IsDefault(fixed) No attributes on root
    element(empty element no end tag), schema HAS targetNamespace
    """
    assert_bindings(
        schema="msData/additional/isdefault061.xsd",
        instance="msData/additional/isdefault065.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_is_default064_is_default064_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : Attributes: IsDefault(fixed) attributes on root
    element, schema HAS targetNamespace, one invalid(3)
    """
    assert_bindings(
        schema="msData/additional/isdefault061.xsd",
        instance="msData/additional/isdefault064.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_is_default063_is_default063_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : Attributes: IsDefault(fixed) attributes on root
    element, schema HAS targetNamespace, one invalid(2)
    """
    assert_bindings(
        schema="msData/additional/isdefault061.xsd",
        instance="msData/additional/isdefault063.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_is_default062_is_default062_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : Attributes: IsDefault(fixed) attributes on root
    element, schema HAS targetNamespace, one invalid(1)
    """
    assert_bindings(
        schema="msData/additional/isdefault061.xsd",
        instance="msData/additional/isdefault062.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default061_is_default061_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Attributes: IsDefault(fixed) attributes on root
    element, schema HAS targetNamespace
    """
    assert_bindings(
        schema="msData/additional/isdefault061.xsd",
        instance="msData/additional/isdefault061.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default058_is_default058_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Attributes: IsDefault(fixed) Local Element with no
    attributes, schema has no targetNamespace
    """
    assert_bindings(
        schema="msData/additional/isdefault052.xsd",
        instance="msData/additional/isdefault058.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default057_is_default057_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Attributes: IsDefault(fixed) Local Element with all
    attributes, schema has no targetNamespace
    """
    assert_bindings(
        schema="msData/additional/isdefault052.xsd",
        instance="msData/additional/isdefault057.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default056_is_default056_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Attributes: IsDefault(fixed) no attributes on root
    element (empty element WITH end tag), schema has no targetNamespace
    """
    assert_bindings(
        schema="msData/additional/isdefault051.xsd",
        instance="msData/additional/isdefault056.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default055_is_default055_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Attributes: IsDefault(fixed) No attributes on root
    element(empty element no end tag), schema has no targetNamespace
    """
    assert_bindings(
        schema="msData/additional/isdefault051.xsd",
        instance="msData/additional/isdefault055.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_is_default054_is_default054_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : Attributes: IsDefault(fixed) attributes on root
    element, schema has no targetNamespace, one invalid(3)
    """
    assert_bindings(
        schema="msData/additional/isdefault051.xsd",
        instance="msData/additional/isdefault054.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_is_default053_is_default053_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : Attributes: IsDefault(fixed) attributes on root
    element, schema has no targetNamespace, one invalid(2)
    """
    assert_bindings(
        schema="msData/additional/isdefault051.xsd",
        instance="msData/additional/isdefault053.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_is_default052_is_default052_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : Attributes: IsDefault(fixed) attributes on root
    element, schema has no targetNamespace, one invalid(1)
    """
    assert_bindings(
        schema="msData/additional/isdefault051.xsd",
        instance="msData/additional/isdefault052.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default051_is_default051_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Attributes: IsDefault(fixed) attributes on root
    element, schema has no targetNamespace
    """
    assert_bindings(
        schema="msData/additional/isdefault051.xsd",
        instance="msData/additional/isdefault051.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default028_is_default028_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(default) a sequence with elements
    with invalid values
    """
    assert_bindings(
        schema="msData/additional/isdefault004.xsd",
        instance="msData/additional/isdefault028.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default027_is_default027_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(default) a sequence with elements
    with fixed values present
    """
    assert_bindings(
        schema="msData/additional/isdefault004.xsd",
        instance="msData/additional/isdefault027.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default026_is_default026_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(default) a sequence with elements
    with start and end tags
    """
    assert_bindings(
        schema="msData/additional/isdefault004.xsd",
        instance="msData/additional/isdefault026.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default025_is_default025_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(default) a sequence with elements
    with no end tags
    """
    assert_bindings(
        schema="msData/additional/isdefault004.xsd",
        instance="msData/additional/isdefault025.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default024_is_default024_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(default) for Element with invalid
    value
    """
    assert_bindings(
        schema="msData/additional/isdefault003.xsd",
        instance="msData/additional/isdefault024.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default023_is_default023_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(default) for Empty Element with
    fixed value already present
    """
    assert_bindings(
        schema="msData/additional/isdefault003.xsd",
        instance="msData/additional/isdefault023.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default022_is_default022_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(default) for Empty Element with
    start and end tag
    """
    assert_bindings(
        schema="msData/additional/isdefault003.xsd",
        instance="msData/additional/isdefault022.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default021_is_default021_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(default) for Empty Element with no
    end tag
    """
    assert_bindings(
        schema="msData/additional/isdefault003.xsd",
        instance="msData/additional/isdefault021.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_is_default011_is_default011_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(fixed) a sequence with elements
    with one invalid value(3)
    """
    assert_bindings(
        schema="msData/additional/isdefault002.xsd",
        instance="msData/additional/isdefault011.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_is_default010_is_default010_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(fixed) a sequence with elements
    with one invalid value (2)
    """
    assert_bindings(
        schema="msData/additional/isdefault002.xsd",
        instance="msData/additional/isdefault010.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_is_default009_is_default009_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(fixed) a sequence with elements
    with one invalid value(1)
    """
    assert_bindings(
        schema="msData/additional/isdefault002.xsd",
        instance="msData/additional/isdefault009.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_is_default008_is_default008_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(fixed) a sequence with elements
    with invalid values
    """
    assert_bindings(
        schema="msData/additional/isdefault002.xsd",
        instance="msData/additional/isdefault008.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default007_is_default007_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(fixed) a sequence with elements
    with fixed values present
    """
    assert_bindings(
        schema="msData/additional/isdefault002.xsd",
        instance="msData/additional/isdefault007.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default006_is_default006_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(fixed) a sequence with elements
    with start and end tags
    """
    assert_bindings(
        schema="msData/additional/isdefault002.xsd",
        instance="msData/additional/isdefault006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default005_is_default005_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(fixed) a sequence with elements
    with no end tags
    """
    assert_bindings(
        schema="msData/additional/isdefault002.xsd",
        instance="msData/additional/isdefault005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_is_default004_is_default004_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(fixed) for Element with invalid
    value
    """
    assert_bindings(
        schema="msData/additional/isdefault001.xsd",
        instance="msData/additional/isdefault004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default003_is_default003_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(fixed) for Empty Element with fixed
    value already present
    """
    assert_bindings(
        schema="msData/additional/isdefault001.xsd",
        instance="msData/additional/isdefault003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default002_is_default002_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(fixed) for Empty Element with start
    and end tag
    """
    assert_bindings(
        schema="msData/additional/isdefault001.xsd",
        instance="msData/additional/isdefault002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_is_default001_is_default001_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(fixed) for Empty Element with no
    end tag
    """
    assert_bindings(
        schema="msData/additional/isdefault001.xsd",
        instance="msData/additional/isdefault001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_d004a_add_d004a_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : SAMPLE: xsd 1.0 Sturcture spec : the ipo.xsd with a
    simplify version of ipo.xml with the xsi:type
    """
    assert_bindings(
        schema="msData/additional/ipo.xsd",
        instance="msData/additional/ipo.xml",
        class_name="PurchaseOrder",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_d004_add_d004_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : SAMPLE: xsd 1.0 Sturcture spec : the ipo.xsd with a
    simplify version of ipo.xml without the xsi:type
    """
    assert_bindings(
        schema="msData/additional/ipo_s1.xsd",
        instance="msData/additional/ipo_s1.xml",
        class_name="PurchaseOrder",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_d002_add_d002_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : xsd 1.0 Prima: the po.xml and po.xsd declared as
    targetNamespace 'foo'
    """
    assert_bindings(
        schema="msData/additional/po.xsd",
        instance="msData/additional/po.xml",
        class_name="PurchaseOrder",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_d001_add_d001_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : xsd 1.0 Prima: the po.xml and po.xsd without
    targetNamespace
    """
    assert_bindings(
        schema="msData/additional/po1.xsd",
        instance="msData/additional/po1.xml",
        class_name="PurchaseOrder",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_add_b202b_add_b202b_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test datatype parsing
    -datetime
    """
    assert_bindings(
        schema="",
        instance="msData/additional/datetime.xml",
        class_name="A",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_add_b202a_add_b202a_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test datatype parsing
    - hexbin
    """
    assert_bindings(
        schema="",
        instance="msData/additional/hexbin.xml",
        class_name="A",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b201_add_b201_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test namespace decl
    """
    assert_bindings(
        schema="msData/additional/ns.xsd",
        instance="msData/additional/ns.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b200c_add_b200c_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test identity
    constraints(3)
    """
    assert_bindings(
        schema="msData/additional/idc.xsd",
        instance="msData/additional/idc3.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b200b_add_b200b_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test identity
    constraints(2)
    """
    assert_bindings(
        schema="msData/additional/idc.xsd",
        instance="msData/additional/idc2.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b200a_add_b200a_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test identity
    constraints(1)
    """
    assert_bindings(
        schema="msData/additional/idc.xsd",
        instance="msData/additional/idc1.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_add_b199_add_b199_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test with xsi type
    """
    assert_bindings(
        schema="",
        instance="msData/additional/xsiType.xml",
        class_name="A",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b198d_add_b198d_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test with minLength
    facet(2)
    """
    assert_bindings(
        schema="msData/additional/minLength.xsd",
        instance="msData/additional/minLength2.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b198c_add_b198c_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test with minLength
    facet(1)
    """
    assert_bindings(
        schema="msData/additional/minLength.xsd",
        instance="msData/additional/minLength1.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b198b_add_b198b_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test with maxLength
    facet(2)
    """
    assert_bindings(
        schema="msData/additional/maxLength.xsd",
        instance="msData/additional/maxLength2.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b198a_add_b198a_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test with maxLength
    facet(1)
    """
    assert_bindings(
        schema="msData/additional/maxLength.xsd",
        instance="msData/additional/maxLength1.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b197f_add_b197f_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test with enumeration
    value(6)
    """
    assert_bindings(
        schema="msData/additional/enum2.xsd",
        instance="msData/additional/enum1c.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b197e_add_b197e_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test with enumeration
    value(5)
    """
    assert_bindings(
        schema="msData/additional/enum2.xsd",
        instance="msData/additional/enum1a.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b197d_add_b197d_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test with enumeration
    value(4)
    """
    assert_bindings(
        schema="msData/additional/enum1.xsd",
        instance="msData/additional/enum1d.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b197c_add_b197c_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test with enumeration
    value(3)
    """
    assert_bindings(
        schema="msData/additional/enum1.xsd",
        instance="msData/additional/enum1c.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b197b_add_b197b_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test with enumeration
    value(2)
    """
    assert_bindings(
        schema="msData/additional/enum1.xsd",
        instance="msData/additional/enum1b.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b197a_add_b197a_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test with enumeration
    value(1)
    """
    assert_bindings(
        schema="msData/additional/enum1.xsd",
        instance="msData/additional/enum1a.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b196l_add_b196l_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test with fixed
    value(12)
    """
    assert_bindings(
        schema="msData/additional/fixed2.xsd",
        instance="msData/additional/fixed3b.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b196k_add_b196k_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test with fixed
    value(11)
    """
    assert_bindings(
        schema="msData/additional/fixed2.xsd",
        instance="msData/additional/fixed3a.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b196j_add_b196j_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test with fixed
    value(10)
    """
    assert_bindings(
        schema="msData/additional/fixed2.xsd",
        instance="msData/additional/fixed2b.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b196i_add_b196i_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test with fixed
    value(9)
    """
    assert_bindings(
        schema="msData/additional/fixed2.xsd",
        instance="msData/additional/fixed2a.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b196h_add_b196h_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test with fixed
    value(8)
    """
    assert_bindings(
        schema="msData/additional/fixed2.xsd",
        instance="msData/additional/fixed1d.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b196g_add_b196g_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test with fixed
    value(7)
    """
    assert_bindings(
        schema="msData/additional/fixed2.xsd",
        instance="msData/additional/fixed1c.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b196f_add_b196f_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test with fixed
    value(6)
    """
    assert_bindings(
        schema="msData/additional/fixed2.xsd",
        instance="msData/additional/fixed1b.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b196e_add_b196e_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test with fixed
    value(5)
    """
    assert_bindings(
        schema="msData/additional/fixed2.xsd",
        instance="msData/additional/fixed1a.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b196d_add_b196d_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test with fixed
    value(4)
    """
    assert_bindings(
        schema="msData/additional/fixed1.xsd",
        instance="msData/additional/fixed1d.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b196c_add_b196c_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test with fixed
    value(3)
    """
    assert_bindings(
        schema="msData/additional/fixed1.xsd",
        instance="msData/additional/fixed1c.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b196b_add_b196b_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test with fixed
    value(2)
    """
    assert_bindings(
        schema="msData/additional/fixed1.xsd",
        instance="msData/additional/fixed1b.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b196a_add_b196a_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test with fixed
    value(1)
    """
    assert_bindings(
        schema="msData/additional/fixed1.xsd",
        instance="msData/additional/fixed1a.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_add_b191_add_b191_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : XSD: During validation of an element schemas in
    schemaLocation and noNamespaceSchemaLocation hints should be compiled
    together TSTF agreed that an un-imported NS used in a QName is a
    schema error
    """
    assert_bindings(
        schema="",
        instance="msData/additional/addB191.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b188_add_b188_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : XSD: Support user specified schema for
    http://www.w3.org/XML/1998/namespace namespace
    """
    assert_bindings(
        schema="msData/additional/test264908_1.xsd",
        instance="msData/additional/test264908_1i.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.xfail
def test_add_b187_add_b187_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : XSD: Support user specified schema for
    http://www.w3.org/XML/1998/namespace namespace
    """
    assert_bindings(
        schema="msData/additional/test264908_1.xsd",
        instance="msData/additional/test264908_1.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b182_add_b182_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="schemaLocation for schema whose targetNamespace
    is the XSD namespace"
    """
    assert_bindings(
        schema="msData/additional/test111871.xsd",
        instance="msData/additional/test111871.xml",
        class_name="Title",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_add_b181_add_b181_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="validating an invalid xsd type"
    """
    assert_bindings(
        schema="",
        instance="msData/additional/test109017.xml",
        class_name="Assembly",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b176_add_b176_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="102850" description="valid but ambigous schema"
    """
    assert_bindings(
        schema="msData/additional/test102850_1.xsd",
        instance="msData/additional/test102850_1.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b175_add_b175_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="102433" description="Validation of xml
    instances should be namespace strict"
    """
    assert_bindings(
        schema="msData/additional/test102433.xsd",
        instance="msData/additional/test102433_6.xml",
        class_name="Foo",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b174_add_b174_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="102433" description="Validation of xml
    instances should be namespace strict"
    """
    assert_bindings(
        schema="msData/additional/test102433.xsd",
        instance="msData/additional/test102433_5.xml",
        class_name="Bar",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b173_add_b173_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="102433" description="Validation of xml
    instances should be namespace strict"
    """
    assert_bindings(
        schema="msData/additional/test102433.xsd",
        instance="msData/additional/test102433_4.xml",
        class_name="Foo",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b172_add_b172_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="102433" description="Validation of xml
    instances should be namespace strict"
    """
    assert_bindings(
        schema="msData/additional/test102433.xsd",
        instance="msData/additional/test102433_3.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b171_add_b171_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="102433" description="Validation of xml
    instances should be namespace strict"
    """
    assert_bindings(
        schema="msData/additional/test102433.xsd",
        instance="msData/additional/test102433_2.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b170_add_b170_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="102433" description="Validation of xml
    instances should be namespace strict"
    """
    assert_bindings(
        schema="msData/additional/test102433.xsd",
        instance="msData/additional/test102433_1.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b169_1_add_b169_1_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="243307" description="test valid document with
    inline schema"
    """
    assert_bindings(
        schema="msData/additional/test93490_16.xsd",
        instance="msData/additional/test93490_16.xml",
        class_name="MapInfo",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_add_b169_add_b169_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="93490" description="test schema location or
    inline schema seen after item from schema target namespace seen"
    """
    assert_bindings(
        schema="",
        instance="msData/additional/test93490_15.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_add_b168_add_b168_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="93490" description="test schema location or
    inline schema seen after item from schema target namespace seen"
    """
    assert_bindings(
        schema="",
        instance="msData/additional/test93490_14.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_add_b167_add_b167_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="93490" description="test schema location or
    inline schema seen after item from schema target namespace seen" WG
    decided that although perhaps misleading, this test is OK
    """
    assert_bindings(
        schema="",
        instance="msData/additional/test93490_13.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_add_b166_add_b166_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="93490" description="test schema location or
    inline schema seen after item from schema target namespace seen"
    """
    assert_bindings(
        schema="",
        instance="msData/additional/test93490_12.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_add_b165_add_b165_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="93490" description="test schema location or
    inline schema seen after item from schema target namespace seen"
    """
    assert_bindings(
        schema="",
        instance="msData/additional/test93490_11.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_add_b164_add_b164_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="93490" description="test schema location or
    inline schema seen after item from schema target namespace seen"
    """
    assert_bindings(
        schema="",
        instance="msData/additional/test93490_10.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_add_b163_add_b163_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="93490" description="test schema location or
    inline schema seen after item from schema target namespace seen"
    """
    assert_bindings(
        schema="",
        instance="msData/additional/test93490_9.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_add_b162_add_b162_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="93490" description="test schema location or
    inline schema seen after item from schema target namespace seen"
    """
    assert_bindings(
        schema="",
        instance="msData/additional/test93490_8.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_add_b161_add_b161_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="93490" description="test schema location or
    inline schema seen after item from schema target namespace seen"
    """
    assert_bindings(
        schema="",
        instance="msData/additional/test93490_7.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_add_b160_add_b160_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="93490" description="test schema location or
    inline schema seen after item from schema target namespace seen"
    """
    assert_bindings(
        schema="",
        instance="msData/additional/test93490_6.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_add_b159_add_b159_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="93490" description="test schema location or
    inline schema seen after item from schema target namespace seen"
    """
    assert_bindings(
        schema="",
        instance="msData/additional/test93490_5.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_add_b158_add_b158_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="93490" description="test schema location or
    inline schema seen after item from schema target namespace seen" See
    also bug 9158 and 15863
    """
    assert_bindings(
        schema="",
        instance="msData/additional/test93490_4.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_add_b157_add_b157_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="93490" description="test schema location or
    inline schema seen after item from schema target namespace seen"
    """
    assert_bindings(
        schema="",
        instance="msData/additional/test93490_3.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_add_b156_add_b156_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="93490" description="test schema location or
    inline schema seen after item from schema target namespace seen" See
    also bug 9158 and 15863
    """
    assert_bindings(
        schema="",
        instance="msData/additional/test93490_2.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_add_b155_add_b155_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="93490" description="test schema location or
    inline schema seen after item from schema target namespace seen"
    """
    assert_bindings(
        schema="",
        instance="msData/additional/test93490_1.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b149_add_b149_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="97822" description="complexContent element with
    fixed value that has the same name as base element does not validate
    against invalid data"
    """
    assert_bindings(
        schema="msData/additional/test97822.xsd",
        instance="msData/additional/test97822.xml",
        class_name="Root1",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b148_add_b148_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="93276" description="XSD: should not overwrite
    the default namespace with the included targetNamespace for
    xsd:include"
    """
    assert_bindings(
        schema="msData/additional/test93276.xsd",
        instance="msData/additional/test93276.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_test93160_test93160_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : Whitespace is collapsed for element with type
    xs:anySimpleType
    """
    assert_bindings(
        schema="msData/additional/test93160.xsd",
        instance="msData/additional/test93160.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b145_add_b145_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="87395" description="validateElement on XSD with
    ID enumeration .." Added a wrapper element in response to bug 10100
    because ID-valued elements are not allowed at the outermost level -
    MHK 2010-07-10
    """
    assert_bindings(
        schema="msData/additional/test87395.xsd",
        instance="msData/additional/test87395.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b143_add_b143_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="83452" description="Invalid lexical hexBinary
    value of 'abcde' should be rejected, hexBinary should be even in
    length."
    """
    assert_bindings(
        schema="msData/additional/test83452.xsd",
        instance="msData/additional/test83452.xml",
        class_name="Test",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_add_b142_add_b142_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="84613" description="validation xml with inline
    schema"
    """
    assert_bindings(
        schema="",
        instance="msData/additional/test84613.xml",
        class_name="Envelope",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b140_add_b140_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="78000" description="any and
    processContents='skip'"
    """
    assert_bindings(
        schema="msData/additional/test78000a.xsd",
        instance="msData/additional/test78000.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_add_b139_add_b139_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="84002" description="validating an XSD with
    empty value in a nsmespace declaration, xmlns=''"
    """
    assert_bindings(
        schema="",
        instance="msData/additional/test84002_b.xml",
        class_name="A",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_add_b138_add_b138_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="84002" description="validating an XSD with
    empty value in a nsmespace declaration, xmlns=''"
    """
    assert_bindings(
        schema="",
        instance="msData/additional/test84002_a.xml",
        class_name="A",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b136_add_b136_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="84188" description="XSD: Attribute with
    use=prohibited and wildcard"
    """
    assert_bindings(
        schema="msData/additional/test84188.xsd",
        instance="msData/additional/test84188.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b135_add_b135_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="81662" description="xsd: test element matching
    global declaration via xsd:any."
    """
    assert_bindings(
        schema="msData/additional/test81662.xsd",
        instance="msData/additional/test81662.xml",
        class_name="Test",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_add_b134_add_b134_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="72131" description="XSD: test xml includes xsd
    in the attribute xsi:noNamespaceSchemaLocation"
    """
    assert_bindings(
        schema="",
        instance="msData/additional/test72131.xml",
        class_name="OrdersByCustomer",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b132_add_b132_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="66745" description="xsd validation:xsd
    substitutionGroup "
    """
    assert_bindings(
        schema="msData/additional/test66745_a.xsd",
        instance="msData/additional/test66745.xml",
        class_name="Foo",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b131_add_b131_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="76423" description="test validation of keys
    when default namespace is '' and more than one key is defined"
    """
    assert_bindings(
        schema="msData/additional/test76423.xsd",
        instance="msData/additional/test76423.xml",
        class_name="Jsml",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b130_add_b130_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="78162" description="attribute on xsd:any
    processContents=skip"
    """
    assert_bindings(
        schema="msData/additional/test78126.xsd",
        instance="msData/additional/test78126.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b129_add_b129_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="74834" description="validate xml data when it
    has a decimal digit of .0"
    """
    assert_bindings(
        schema="msData/additional/test74834.xsd",
        instance="msData/additional/test74834.xml",
        class_name="Datafile",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b125_add_b125_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="78898" description="xsd: wildcard: content type
    with namespace=##any and processContent=skip"
    """
    assert_bindings(
        schema="msData/additional/test78898.xsd",
        instance="msData/additional/test78898.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_add_b124_add_b124_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="79253" description="XSD: validating an XML with
    a not welform XSD?"
    """
    assert_bindings(
        schema="",
        instance="msData/additional/test79253.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b123_add_b123_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="79416" description="xsd: test violation of
    uniqueness in xsd"
    """
    assert_bindings(
        schema="msData/additional/test79416.xsd",
        instance="msData/additional/test79416.xml",
        class_name="Foo",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b122_add_b122_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="78910" description="xsd: wildcard: content type
    with namespace=##any and processContent=skip"
    """
    assert_bindings(
        schema="msData/additional/addB122.xsd",
        instance="msData/additional/addB122.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_add_b120_add_b120_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="73456" description="xsd: test validating an XML
    with invalid XSD."
    """
    assert_bindings(
        schema="",
        instance="msData/additional/test73456.xml",
        class_name="A",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b116_add_b116_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="75092" description="xsd: 'any' with
    processContents=strict: should allow valid content item which has
    xsi:type."
    """
    assert_bindings(
        schema="msData/additional/test75092.xsd",
        instance="msData/additional/test75092.xml",
        class_name="Foo",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b115_add_b115_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="75564" description="xsd: absolute string in
    fixed attribute value, when there are invalid char follow the valud
    value."
    """
    assert_bindings(
        schema="msData/additional/addB115.xsd",
        instance="msData/additional/addB115.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b114_add_b114_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="75808" description="xsd testing"
    """
    assert_bindings(
        schema="msData/additional/addB114.xsd",
        instance="msData/additional/addB114.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b109_add_b109_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : check that the local fixed value must be the same
    as the global fixed value
    """
    assert_bindings(
        schema="msData/additional/addB109.xsd",
        instance="msData/additional/addB109.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b105_add_b105_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : test element's fixed value is not normalized
    """
    assert_bindings(
        schema="msData/additional/addB105.xsd",
        instance="msData/additional/addB105.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b104_add_b104_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : test attribute normalization of fixed value of an
    attribute value
    """
    assert_bindings(
        schema="msData/additional/addB104.xsd",
        instance="msData/additional/addB104.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b102_add_b102_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="60941" description="xsd: particle validation
    rules: test when group's minOccurs=2 and the instant XML has only one
    sequence of group"
    """
    assert_bindings(
        schema="msData/additional/addB102.xsd",
        instance="msData/additional/addB102.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b098_add_b098_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="61115" description="test when the content is
    incomplete."
    """
    assert_bindings(
        schema="msData/additional/addB098.xsd",
        instance="msData/additional/addB098.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b096_add_b096_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="61053" description="xsd: test 'group' reference
    is used, and content model is explicitly declared using 'sequence'."
    """
    assert_bindings(
        schema="msData/additional/addB096.xsd",
        instance="msData/additional/addB096.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b092_add_b092_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="62136" description="xsd: in an 'all' group,
    when element is declared as minOccurs=0, maxOccurs=0, it should not be
    able to appear in instant XML."
    """
    assert_bindings(
        schema="msData/additional/addB092.xsd",
        instance="msData/additional/addB092.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b090_add_b090_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="61911" description="xsd: extension: when
    'choice' is extented from 'any', the one of the item in 'choice'
    should satisfy the content model."
    """
    assert_bindings(
        schema="msData/additional/addB090.xsd",
        instance="msData/additional/addB090.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b088_add_b088_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="61692" description="xsd:
    elementFormDefault=qualified, test elements from imported xsd that are
    not qualified in the instant XML."
    """
    assert_bindings(
        schema="msData/additional/addB088.xsd",
        instance="msData/additional/addB088.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b087_add_b087_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="61692" description="xsd:
    elementFormDefault=qualified, test elements from imported xsd that are
    not qualified in the instant XML."
    """
    assert_bindings(
        schema="msData/additional/addB087.xsd",
        instance="msData/additional/addB087.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b084_add_b084_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="61599" description="xsd:particle: all, test
    only one element declaration, and that element is used in xml
    instant."
    """
    assert_bindings(
        schema="msData/additional/addB084.xsd",
        instance="msData/additional/addB084.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b080_add_b080_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="72554" description="XSD: should disallow
    duplicate ID attributes like DTD and XDR"
    """
    assert_bindings(
        schema="msData/additional/addB080.xsd",
        instance="msData/additional/addB080.xml",
        class_name="Orders",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b076_add_b076_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="75028"
    """
    assert_bindings(
        schema="msData/additional/addB076.xsd",
        instance="msData/additional/addB076.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b075_add_b075_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="75564" description="xsd: we do not check for
    absolute string in fixed attribute value, when there are invalid char
    follow the valud value."
    """
    assert_bindings(
        schema="msData/additional/test75564.xsd",
        instance="msData/additional/test75564.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b069_add_b069_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="63950" description="Validating instance
    document against schema with an integer restriction"
    """
    assert_bindings(
        schema="msData/additional/test63950.xsd",
        instance="msData/additional/test63950.xml",
        class_name="Zip",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b068_add_b068_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="73986" description="xsd: length of QName" TSTF
    ruled that 1.0 says all QNames satisfy all length-related tests
    """
    assert_bindings(
        schema="msData/additional/test73986.xsd",
        instance="msData/additional/test73986_2.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b067_add_b067_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="73986" description="xsd: length of QName"
    """
    assert_bindings(
        schema="msData/additional/test73986.xsd",
        instance="msData/additional/test73986.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b066_add_b066_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="73850" description="xsd: test duplicated ID
    (one is attribute one is element) in instance xml"
    """
    assert_bindings(
        schema="msData/additional/test73850.xsd",
        instance="msData/additional/test73850.xml",
        class_name="A",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b065_add_b065_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="73826" description="xsd: element, when nillable
    is true, there must be no fixed value"
    """
    assert_bindings(
        schema="msData/additional/test73826.xsd",
        instance="msData/additional/test73826.xml",
        class_name="R",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_add_b063_add_b063_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : 72702 - test using or validating a not-wellformed
    XSD
    """
    assert_bindings(
        schema="",
        instance="msData/additional/test72702.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b059_add_b059_v(json_360, save_output):
    r"""
    TEST :Adhoc XSD: : id="73666" description="xsd: Regular Expression:
    test pattern '(\n|\s)+b' and value ' b'"
    """
    assert_bindings(
        schema="msData/additional/test73666.xsd",
        instance="msData/additional/test73666.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b058_add_b058_v(json_360, save_output):
    r"""
    TEST :Adhoc XSD: : id="73665" description="xsd: Regular Expression:
    test checking for '\C' non-character correctly, test with value='?'"
    """
    assert_bindings(
        schema="msData/additional/test73665.xsd",
        instance="msData/additional/test73665.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b057_add_b057_i(json_360, save_output):
    r"""
    TEST :Adhoc XSD: : id="73715" description="xsd: Regular Expression:
    preprocess pattern '\\c' should match '\c'"
    """
    assert_bindings(
        schema="msData/additional/test73715.xsd",
        instance="msData/additional/test73715i.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b056_add_b056_v(json_360, save_output):
    r"""
    TEST :Adhoc XSD: : id="73715" description="xsd: Regular Expression:
    preprocess pattern '\\c' should match '\c'"
    """
    assert_bindings(
        schema="msData/additional/test73715.xsd",
        instance="msData/additional/test73715v.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b054_add_b054_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="70948" description="xsd:invalid facets on
    simpleContent restriction with simpleType child should work"
    """
    assert_bindings(
        schema="msData/additional/test70948.xsd",
        instance="msData/additional/test70948.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b050_add_b050_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="72232" description="xsd: keyref should be able
    to refer to a key defined on the parent element."
    """
    assert_bindings(
        schema="msData/additional/test72232_2.xsd",
        instance="msData/additional/test72232_2.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b049_add_b049_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="72232" description="xsd: keyref should be able
    to refer to a key defined on the parent element." TSTF concluded the
    narrower scope of the keyref means it's invalid Oops, 2010-01-22
    change was mistaken, should have been instance invalid, schema
    restored to validity, instance made invalid
    """
    assert_bindings(
        schema="msData/additional/test72232_1.xsd",
        instance="msData/additional/test72232_1.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b047_add_b047_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="72597" description="xsd: valid xml and xsd"
    """
    assert_bindings(
        schema="msData/additional/test72597.xsd",
        instance="msData/additional/test72597.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b046_add_b046_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="72097" description="xsd: when there is no
    targetNamespace, the XSD file should be allowed to add to any
    namespace"
    """
    assert_bindings(
        schema="msData/additional/test72097.xsd",
        instance="msData/additional/test72097.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b040_add_b040_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="72049" description="xsd: schemaLocation with
    more than one pair of namespace+schemalocation "
    """
    assert_bindings(
        schema="msData/additional/test72049_a.xsd",
        instance="msData/additional/test72049.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b037_add_b037_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="70130" description="XSD:text is not allowed
    when using xsd:any elements."
    """
    assert_bindings(
        schema="msData/additional/test70130.xsd",
        instance="msData/additional/test70130.xml",
        class_name="Type",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b034_add_b034_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="71818" description="xsd: when an attribute is
    prohibited, it should not be allowed in instant XML even if there is
    anyAttriubte declaration."
    """
    assert_bindings(
        schema="msData/additional/test71818.xsd",
        instance="msData/additional/test71818.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b31_add_b31_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : another test
    """
    assert_bindings(
        schema="msData/additional/test69277.xsd",
        instance="msData/additional/test69277.xml",
        class_name="Elt1",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b028_add_b028_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : XSD: xsi:type when derived from xsi:type
    """
    assert_bindings(
        schema="msData/additional/test69846.xsd",
        instance="msData/additional/test69846.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b019_add_b019_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="68938" description="xsd: fractional digit and
    total digit are not checking correcting in XSD datatypes"
    """
    assert_bindings(
        schema="msData/additional/test68938.xsd",
        instance="msData/additional/test68938.xml",
        class_name="Foo",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b013_add_b013_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="67514" title="xsd: when processContents is
    strict, test for element that are not defined in a specified schema."
    """
    assert_bindings(
        schema="msData/additional/test67514.xsd",
        instance="msData/additional/test67514.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_b012_add_b012_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="67500" title="xsd: checking QName datatype
    correctly for the namespace declared on the same element"
    """
    assert_bindings(
        schema="msData/additional/test67500.xsd",
        instance="msData/additional/test67500.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b011_add_b011_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="66541" title="xsd: Regular Expression"
    """
    assert_bindings(
        schema="msData/additional/test66541.xsd",
        instance="msData/additional/test66541.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b003_add_b003_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="63389" title="loading invalid XML with empty
    content"
    """
    assert_bindings(
        schema="msData/additional/test63389.xsd",
        instance="msData/additional/test63389.xml",
        class_name="PurchaseOrder",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_add_b002_add_b002_i(json_360, save_output):
    """
    TEST :Adhoc XSD: : id="63569" title="test restrictions of simple
    types"
    """
    assert_bindings(
        schema="msData/additional/test63569.xsd",
        instance="msData/additional/test63569.xml",
        class_name="Zip",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_c001_add_c001_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : use of xml:base
    """
    assert_bindings(
        schema="msData/additional/adhocAddC001.xsd",
        instance="msData/additional/adhocAddC001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_add_a008_add_a008_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : uses substitution Element from the importing XSD(2)
    """
    assert_bindings(
        schema="",
        instance="msData/additional/adhocAddB004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_adda007_adda007_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : uses substitution Element from the importing XSD
    """
    assert_bindings(
        schema="",
        instance="msData/additional/adhocAddB003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_add_a006_add_a006_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : xsd: when both the imported and importing XSDs are
    added to schema collection, the instance XML uses substitution Element
    from the importing XSD to a root element declared in imported XSD.
    """
    assert_bindings(
        schema="",
        instance="msData/additional/adhocAddB002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_add_a005_add_a005_v(json_360, save_output):
    """
    TEST :Adhoc XSD: : substitution group usage in the same XSD file with
    instance XML
    """
    assert_bindings(
        schema="msData/additional/adhocAddB001.xsd",
        instance="msData/additional/adhocAddB001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_attg_z001_attg_z001_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : xsd: global
    attribute reference in attributeGroup should be invalid if not
    qualified in the instance. (attributeFormDefault is qualified).
    """
    assert_bindings(
        schema="msData/attributeGroup/attgZ001.xsd",
        instance="msData/attributeGroup/attgZ001.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_attg_d042_attg_d042_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : AttributeGroup
    (w/ namespace=other, processContents=##strict), the xml has the
    attribute instance which conatins invalid attribute against schema
    """
    assert_bindings(
        schema="msData/attributeGroup/attgD042.xsd",
        instance="msData/attributeGroup/attgD042.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_attg_d036_attg_d036_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : complexType's
    AttributeGroup with reference to attributeGroup from 'redefine', where
    there is an attribute declared as int, with value="37", the xml has
    the attribute instance which "37"
    """
    assert_bindings(
        schema="msData/attributeGroup/attgD036.xsd",
        instance="msData/attributeGroup/attgD036.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_attg_d035_attg_d035_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : complexType's
    AttributeGroup with reference to attributeGroup from 'redefine', where
    there is an attribute declared as int, with value="37", the xml has
    the attribute instance which "36"
    """
    assert_bindings(
        schema="msData/attributeGroup/attgD035.xsd",
        instance="msData/attributeGroup/attgD035.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_attg_d034_attg_d034_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : AttributeGroup
    (w/ namespace=other, processContents=##strict), the xml has the
    attribute instance which conatins valid elements and attribute against
    schema
    """
    assert_bindings(
        schema="msData/attributeGroup/attgD034.xsd",
        instance="msData/attributeGroup/attgD034.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_attg_d033_attg_d033_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : AttributeGroup
    (w/ namespace=other, processContents=##lax), the xml has the attribute
    instance which conatins invalid attribute against schema
    """
    assert_bindings(
        schema="msData/attributeGroup/attgD033.xsd",
        instance="msData/attributeGroup/attgD033.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_attg_d032_attg_d032_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : AttributeGroup
    (w/ namespace=other, processContents=##lax), the xml has the attribute
    instance which conatins valid elements and attribute against schema
    """
    assert_bindings(
        schema="msData/attributeGroup/attgD032.xsd",
        instance="msData/attributeGroup/attgD032.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_attg_d031_attg_d031_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : AttributeGroup
    (w/ namespace=other, processContents=##skip), the xml has the
    attribute instance which conatins attribute not declared in any schema
    """
    assert_bindings(
        schema="msData/attributeGroup/attgD031.xsd",
        instance="msData/attributeGroup/attgD031.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_attg_d030_attg_d030_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : Basic
    AttributeGroup with anyAttribute (w/ namespace=##targetNamespace), the
    xml has the attribute instance which is of namespace other than
    targetNamespace
    """
    assert_bindings(
        schema="msData/attributeGroup/attgD030.xsd",
        instance="msData/attributeGroup/attgD030.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_attg_d029_attg_d029_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : Basic
    AttributeGroup with anyAttribute (w/ namespace=##targetNamespace), the
    xml has the attribute instance which is of namespace targetNamespace
    """
    assert_bindings(
        schema="msData/attributeGroup/attgD029.xsd",
        instance="msData/attributeGroup/attgD029.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_attg_d028_attg_d028_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : Basic
    AttributeGroup with anyAttribute (w/ namespace="foo"), the xml has the
    attribute instance which is of namespace "bar"
    """
    assert_bindings(
        schema="msData/attributeGroup/attgD028.xsd",
        instance="msData/attributeGroup/attgD028.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_attg_d027_attg_d027_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : Basic
    AttributeGroup with anyAttribute (w/ namespace="foo"), the xml has the
    attribute instance which is of namespace "foo"
    """
    assert_bindings(
        schema="msData/attributeGroup/attgD027.xsd",
        instance="msData/attributeGroup/attgD027.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_attg_d026_attg_d026_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : Basic
    AttributeGroup with anyAttribute (w/ namespace=##local), the xml has
    the attribute instance which is namespace qualified
    """
    assert_bindings(
        schema="msData/attributeGroup/attgD026.xsd",
        instance="msData/attributeGroup/attgD026.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_attg_d025_attg_d025_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : Basic
    AttributeGroup with anyAttribute (w/ namespace=##local), the xml has
    the attribute instance which is namespace UNqualified
    """
    assert_bindings(
        schema="msData/attributeGroup/attgD025.xsd",
        instance="msData/attributeGroup/attgD025.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_attg_d024_attg_d024_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : Basic
    AttributeGroup with anyAttribute (w/ namespace=##any), the xml has the
    attribute instance which fall under targetNS, but not defiled in the
    schema
    """
    assert_bindings(
        schema="msData/attributeGroup/attgD024.xsd",
        instance="msData/attributeGroup/attgD024.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_attg_d023_attg_d023_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : Basic
    AttributeGroup with anyAttribute (w/ namespace=##other), the xml has
    the attribute instance with namespace same as the targetNamdspace of
    the xsd
    """
    assert_bindings(
        schema="msData/attributeGroup/attgD023.xsd",
        instance="msData/attributeGroup/attgD023.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_attg_d022_attg_d022_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : Basic
    AttributeGroup with anyAttribute (w/ namespace=##other), the xml has
    the attribute instance with namespace different from the
    targetNamdspace of the xsd
    """
    assert_bindings(
        schema="msData/attributeGroup/attgD022.xsd",
        instance="msData/attributeGroup/attgD022.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_attg_d021_attg_d021_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : Basic
    AttributeGroup with anyAttribute (w/ namespace=##any), the xml has the
    attribute instance with "foo" as its namespace
    """
    assert_bindings(
        schema="msData/attributeGroup/attgD021.xsd",
        instance="msData/attributeGroup/attgD021.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_attg_d020_attg_d020_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : Basic
    AttributeGroup with anyAttribute (w/ namespace=##any), the xml has the
    attribute instance with no namespace
    """
    assert_bindings(
        schema="msData/attributeGroup/attgD020.xsd",
        instance="msData/attributeGroup/attgD020.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_attg_d019_attg_d019_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : Basic
    AttributeGroup with anyAttribute (w/ annotation)
    """
    assert_bindings(
        schema="msData/attributeGroup/attgD019.xsd",
        instance="msData/attributeGroup/attgD019.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_attg_d018_attg_d018_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : Basic
    AttributeGroup with anyAttribute (w/ id)
    """
    assert_bindings(
        schema="msData/attributeGroup/attgD018.xsd",
        instance="msData/attributeGroup/attgD018.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_attg_d005_attg_d005_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : attributeGroup
    with child in the sequence of ( att, attg, att, attg, att), the xml
    has the attributes
    """
    assert_bindings(
        schema="msData/attributeGroup/attgD005.xsd",
        instance="msData/attributeGroup/attgD005.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_attg_d004_attg_d004_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : attributeGroup
    with just another attributeGroup, the xml has the attributes
    """
    assert_bindings(
        schema="msData/attributeGroup/attgD004.xsd",
        instance="msData/attributeGroup/attgD004.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_attg_d003_attg_d003_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : attributeGroup
    with 2000 attribute decl as child, the xml has the 2000 attributes
    """
    assert_bindings(
        schema="msData/attributeGroup/attgD003.xsd",
        instance="msData/attributeGroup/attgD003.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_attg_c038_attg_c038_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : Test
    attributeGroup declaration: can only reference global attributeGroup
    parent is redefine, ref='name of attribute group declared inside a
    redefine'
    """
    assert_bindings(
        schema="msData/attributeGroup/attgC038.xsd",
        instance="msData/attributeGroup/attgC038.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_attg_c037_attg_c037_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : Test
    attributeGroup declaration: can only reference global attributeGroup
    parent is redefine, ref='name of global attribute group declared at
    the end of xsd'
    """
    assert_bindings(
        schema="msData/attributeGroup/attgC037.xsd",
        instance="msData/attributeGroup/attgC037.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_attg_c036_attg_c036_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : Test
    attributeGroup declaration: parent is redefine, ref='name of a global
    attribute group from included xsd'
    """
    assert_bindings(
        schema="msData/attributeGroup/attgC036.xsd",
        instance="msData/attributeGroup/attgC036.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_attg_c035_attg_c035_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : Test
    attributeGroup declaration: parent is redefine, ref='name of a global
    attribute group from imported xsd'
    """
    assert_bindings(
        schema="msData/attributeGroup/attgC035.xsd",
        instance="msData/attributeGroup/attgC035.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_attg_c026_attg_c026_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : Test
    attributeGroup declaration: parent is extension, ref='name of a global
    attribute group from included xsd'
    """
    assert_bindings(
        schema="msData/attributeGroup/attgC026.xsd",
        instance="msData/attributeGroup/attgC026.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_attg_c025_attg_c025_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : Test
    attributeGroup declaration: parent is extension, ref='name of a global
    attribute group from included xsd'
    """
    assert_bindings(
        schema="msData/attributeGroup/attgC025.xsd",
        instance="msData/attributeGroup/attgC025.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_attg_c024_attg_c024_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : Test
    attributeGroup declaration: parent is extension, ref='name of a global
    attribute group from imported xsd'
    """
    assert_bindings(
        schema="msData/attributeGroup/attgC024.xsd",
        instance="msData/attributeGroup/attgC024.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_attg_c010_attg_c010a(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : Test
    attributeGroup declaration: self referencing, name="test", has child
    attributeGroup that also has, parent is attributeGroup, ref='test'
    """
    assert_bindings(
        schema="msData/attributeGroup/attgC010.xsd",
        instance="msData/attributeGroup/attgC010a.xml",
        class_name="T",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_attg_c010_attg_c010b(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : Test
    attributeGroup declaration: self referencing, name="test", has child
    attributeGroup that also has, parent is attributeGroup, ref='test'
    """
    assert_bindings(
        schema="msData/attributeGroup/attgC010.xsd",
        instance="msData/attributeGroup/attgC010b.xml",
        class_name="T",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_attg_c007_attg_c007_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : Test
    attributeGroup declaration: can only reference global attributeGroup
    parent is attributeGroup, ref='name of attribute group declared inside
    a redefine', and xml instant has value same as what is defined as
    fixed in the redefined attributeGroup.
    """
    assert_bindings(
        schema="msData/attributeGroup/attgC007.xsd",
        instance="msData/attributeGroup/attgC007.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_attg_c006_attg_c006_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : Test
    attributeGroup declaration: can only reference global attributeGroup
    parent is attributeGroup, ref='name of attribute group declared inside
    a redefine', and xml instant has value different what is defined as
    fixed in the redefined attributeGroup.
    """
    assert_bindings(
        schema="msData/attributeGroup/attgC006.xsd",
        instance="msData/attributeGroup/attgC006.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_z015_att_z015_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : XSD: a
    prohibited attribute should not be in the attribute uses of an
    attributeGroup TSTF concluded the test is correct
    """
    assert_bindings(
        schema="msData/attribute/attZ015.xsd",
        instance="msData/attribute/attZ015.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_z014b_att_z014b_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : XSD: No more
    than one attribute of type ID should be validated per Element(2)
    Multiple ID attributes on an element become legal in XSD 1.1 - MHK
    """
    assert_bindings(
        schema="msData/attribute/attZ014b.xsd",
        instance="msData/attribute/attZ014b.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_z014a_att_z014a_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : XSD: No more
    than one attribute of type ID should be validated per Element(1)
    Multiple ID attributes on an element become legal in XSD 1.1 - MHK
    """
    assert_bindings(
        schema="msData/attribute/attZ014a.xsd",
        instance="msData/attribute/attZ014a.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_z009_att_z009_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : when more
    than one xsi attribute encountered in an invalid file
    """
    assert_bindings(
        schema="msData/attribute/attZ009.xsd",
        instance="msData/attribute/attZ009.xml",
        class_name="MyFields",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_z007i_att_z007i_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : XSD:
    insertion of prohibited attribute in a derived type
    """
    assert_bindings(
        schema="msData/attribute/attZ007.xsd",
        instance="msData/attribute/attZ007i.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_z007v_att_z007v_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : XSD:
    insertion of prohibited attribute in a derived type
    """
    assert_bindings(
        schema="msData/attribute/attZ007.xsd",
        instance="msData/attribute/attZ007v.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_z005_att_z005_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : XSD: default
    value of attribute
    """
    assert_bindings(
        schema="msData/attribute/attZ005.xsd",
        instance="msData/attribute/attZ005.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_z002_att_z002_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : prohibited
    attribute
    """
    assert_bindings(
        schema="msData/attribute/attZ002.xsd",
        instance="msData/attribute/attZ002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_z001_att_z001_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Redefine and
    restriction of attribute
    """
    assert_bindings(
        schema="msData/attribute/attZ001.xsd",
        instance="msData/attribute/attZ001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_q019_att_q019_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : two
    attribute, same loca name, from different namespace on same element
    """
    assert_bindings(
        schema="msData/attribute/attQ019.xsd",
        instance="msData/attribute/attQ019.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_q014_att_q014_v(json_360, save_output):
    r"""
    TEST :Syntax Checking for Attribute Declaration (form) :
    Attribute\attribute decl under extension element
    """
    assert_bindings(
        schema="msData/attribute/attQ014.xsd",
        instance="msData/attribute/attQ014.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_q003_att_q003_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : parent is
    complexType, Attr Decl, followed by Attr Group, follow by Attr
    """
    assert_bindings(
        schema="msData/attribute/attQ003.xsd",
        instance="msData/attribute/attQ003.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_p032_att_p032_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Test that
    attributes from imported schema (global, attribute Group, complexTyped
    and simpleTyped) are recognized
    """
    assert_bindings(
        schema="msData/attribute/attP032.xsd",
        instance="msData/attribute/attP032.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_p031_att_p031_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) :
    use=prohibited, fixed="37" (must not appear in xml instant, attribute
    does appear in the instant XML (attribute not exist in instant doc)
    """
    assert_bindings(
        schema="msData/attribute/attP031.xsd",
        instance="msData/attribute/attP031.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_p029_att_p029_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) :
    use=prohibited, fixed="37" (must not appear in xml instant, attribute
    does not appear in the instant XML (attribute not exist in instant
    doc) use=prohibited, fixed=X is not allowed in XSD 1.1. See bug 14245
    """
    assert_bindings(
        schema="msData/attribute/attP029.xsd",
        instance="msData/attribute/attP029.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_p028_att_p028_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) :
    use=prohibited, default="37" (must not appear in xml instant,
    attribute does not appear in the instant XML (attribute not exist in
    instant doc)
    """
    assert_bindings(
        schema="msData/attribute/attP028.xsd",
        instance="msData/attribute/attP028.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_p027_att_p027_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : name='foo'
    use=optional, default="37" (may appear once, may have any value)
    name='foo1', instant xml value=38
    """
    assert_bindings(
        schema="msData/attribute/attP027.xsd",
        instance="msData/attribute/attP027.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_p026_att_p026_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : use=optional,
    default="37" (may appear once, may have any value), instant xml
    value=38
    """
    assert_bindings(
        schema="msData/attribute/attP026.xsd",
        instance="msData/attribute/attP026.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_p025_att_p025_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : use=optional,
    default="37" (may appear once, may have any value), instant xml
    value=37
    """
    assert_bindings(
        schema="msData/attribute/attP025.xsd",
        instance="msData/attribute/attP025.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_p024_att_p024_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : use=optional,
    default="37" (may appear once, may have any value), instant xml value
    does not appear (this will have the default attribute and value)
    """
    assert_bindings(
        schema="msData/attribute/attP024.xsd",
        instance="msData/attribute/attP024.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_p023_att_p023_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : use=absent,
    default="37" (may appear once, may have any value), instant xml
    value=38
    """
    assert_bindings(
        schema="msData/attribute/attP023.xsd",
        instance="msData/attribute/attP023.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_p022_att_p022_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : use=absent,
    default="37" (may appear once, may have any value), instant xml
    value=37
    """
    assert_bindings(
        schema="msData/attribute/attP022.xsd",
        instance="msData/attribute/attP022.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_p021_att_p021_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : use=absent,
    default="37" (may appear once, may have any value), instant xml value
    does not appear (this will have the default attribute and value)
    """
    assert_bindings(
        schema="msData/attribute/attP021.xsd",
        instance="msData/attribute/attP021.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_p020_att_p020_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : use=optional,
    fixed="37" (may appear once, if appear, value must be "37"), instant
    xml value =38
    """
    assert_bindings(
        schema="msData/attribute/attP020.xsd",
        instance="msData/attribute/attP020.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_p019_att_p019_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : use=optional,
    fixed="37" (may appear once, if appear, value must be "37"), instant
    xml value =37
    """
    assert_bindings(
        schema="msData/attribute/attP019.xsd",
        instance="msData/attribute/attP019.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_p018_att_p018_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : use=optional,
    fixed="37" (may appear once, if appear, value must be "37"), instant
    xml value =36
    """
    assert_bindings(
        schema="msData/attribute/attP018.xsd",
        instance="msData/attribute/attP018.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_p017_att_p017_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : use=optional,
    fixed="37" (may appear once, if appear, value must be "37"), instant
    xml value does not appear (attribute not exist in instant doc)
    """
    assert_bindings(
        schema="msData/attribute/attP017.xsd",
        instance="msData/attribute/attP017.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_p016_att_p016_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : use=absent,
    fixed="37" (may appear once, if appear, value must be "37"), instant
    xml value =38
    """
    assert_bindings(
        schema="msData/attribute/attP016.xsd",
        instance="msData/attribute/attP016.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_p015_att_p015_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : use=absent,
    fixed="37" (may appear once, if appear, value must be "37"), instant
    xml value =37
    """
    assert_bindings(
        schema="msData/attribute/attP015.xsd",
        instance="msData/attribute/attP015.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_p014_att_p014_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : use=absent,
    fixed="37" (may appear once, if appear, value must be "37"), instant
    xml value =36
    """
    assert_bindings(
        schema="msData/attribute/attP014.xsd",
        instance="msData/attribute/attP014.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_p013_att_p013_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : use=absent,
    fixed="37" (may appear once, if appear, value must be "37"), instant
    xml value does not appear (attribute not exist in instant doc)
    """
    assert_bindings(
        schema="msData/attribute/attP013.xsd",
        instance="msData/attribute/attP013.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_p012_att_p012_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : use=required,
    fixed="37" (must appear once, value must be "37"), instant xml value
    =38
    """
    assert_bindings(
        schema="msData/attribute/attP012.xsd",
        instance="msData/attribute/attP012.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_p011_att_p011_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : use=required,
    fixed="37" (must appear once, value must be "37"), instant xml value
    =37
    """
    assert_bindings(
        schema="msData/attribute/attP011.xsd",
        instance="msData/attribute/attP011.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_p010_att_p010_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : use=required,
    fixed="37" (must appear once, value must be "37"), instant xml value
    =36
    """
    assert_bindings(
        schema="msData/attribute/attP010.xsd",
        instance="msData/attribute/attP010.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_p009_att_p009_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : use=required,
    fixed="37" (must appear once, value must be "37"), instant xml value
    does not appear
    """
    assert_bindings(
        schema="msData/attribute/attP009.xsd",
        instance="msData/attribute/attP009.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_p008_att_p008_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : use=required,
    fixed and default are absent (must appear, value can be anything),
    instant xml attribute absent
    """
    assert_bindings(
        schema="msData/attribute/attP008.xsd",
        instance="msData/attribute/attP008.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_p007_att_p007_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : use=required,
    fixed and default are absent (must appear, value can be anything),
    instant xml value=36
    """
    assert_bindings(
        schema="msData/attribute/attP007.xsd",
        instance="msData/attribute/attP007.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_p005_att_p005_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : type="my
    simple type", fixed=conform to the type, and xml instant has the
    attribute with invalid value
    """
    assert_bindings(
        schema="msData/attribute/attP005.xsd",
        instance="msData/attribute/attP005.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_p004_att_p004_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : type="my
    simple type", fixed=conform to the type, and xml instant has the
    attribute with valid value
    """
    assert_bindings(
        schema="msData/attribute/attP004.xsd",
        instance="msData/attribute/attP004.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_att_md011_att_md011_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Attributes
    from xsi ( xml schema instance ) namespace should be validated
    """
    assert_bindings(
        schema="",
        instance="msData/attribute/test108565_11.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_att_md010_att_md010_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Attributes
    from xsi ( xml schema instance ) namespace should be validated
    """
    assert_bindings(
        schema="",
        instance="msData/attribute/test108565_10.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_att_md009_att_md009_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Attributes
    from xsi ( xml schema instance ) namespace should be validated
    """
    assert_bindings(
        schema="",
        instance="msData/attribute/test108565_9.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_att_md008_att_md008_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Attributes
    from xsi ( xml schema instance ) namespace should be validated
    """
    assert_bindings(
        schema="",
        instance="msData/attribute/test108565_8.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_att_md007_att_md007_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Attributes
    from xsi ( xml schema instance ) namespace should be validated
    """
    assert_bindings(
        schema="",
        instance="msData/attribute/test108565_7.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_att_md006_att_md006_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Attributes
    from xsi ( xml schema instance ) namespace should be validated
    """
    assert_bindings(
        schema="",
        instance="msData/attribute/test108565_6.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_att_md005_att_md005_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Attributes
    from xsi ( xml schema instance ) namespace should be validated
    """
    assert_bindings(
        schema="",
        instance="msData/attribute/test108565_5.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_att_md004_att_md004_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Attributes
    from xsi ( xml schema instance ) namespace should be validated
    """
    assert_bindings(
        schema="",
        instance="msData/attribute/test108565_4.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_att_md003_att_md003_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Attributes
    from xsi ( xml schema instance ) namespace should be validated
    """
    assert_bindings(
        schema="",
        instance="msData/attribute/test108565_3.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_att_md002_att_md002_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Attributes
    from xsi ( xml schema instance ) namespace should be validated
    """
    assert_bindings(
        schema="",
        instance="msData/attribute/test108565_2.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_att_md001_att_md001_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Attributes
    from xsi ( xml schema instance ) namespace should be validated
    """
    assert_bindings(
        schema="",
        instance="msData/attribute/test108565_1.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_mc012_att_mc012_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : parent is
    attributeGroup,form=unqualified, attributeFormDefault=qualified,
    attribute in xml doc is qualified with prefix
    """
    assert_bindings(
        schema="msData/attribute/attMc012.xsd",
        instance="msData/attribute/attMc012.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_mc011_att_mc011_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : parent is
    attributeGroup,form=unqualified, attributeFormDefault=unqualified,
    attribute in xml doc is qualified with prefix
    """
    assert_bindings(
        schema="msData/attribute/attMc011.xsd",
        instance="msData/attribute/attMc011.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_mc010_att_mc010_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : parent is
    attributeGroup,form=unqualified, attributeFormDefault=absent,
    attribute in xml doc is qualified with prefix
    """
    assert_bindings(
        schema="msData/attribute/attMc010.xsd",
        instance="msData/attribute/attMc010.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_mc009_att_mc009_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : parent is
    attributeGroup,form=unqualified, attributeFormDefault=qualified,
    attribute in xml doc has no prefix, but the containing element has a
    default namespace declared
    """
    assert_bindings(
        schema="msData/attribute/attMc009.xsd",
        instance="msData/attribute/attMc009.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_mc008_att_mc008_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : parent is
    attributeGroup,form=unqualified, attributeFormDefault=unqualified,
    attribute in xml doc has no prefix, but the containing element has a
    default namespace declared
    """
    assert_bindings(
        schema="msData/attribute/attMc008.xsd",
        instance="msData/attribute/attMc008.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_mc007_att_mc007_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : parent is
    attributeGroup,form=unqualified, attributeFormDefault=absent,
    attribute in xml doc has no prefix, but the containing element has a
    default namespace declared
    """
    assert_bindings(
        schema="msData/attribute/attMc007.xsd",
        instance="msData/attribute/attMc007.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_mc006_att_mc006_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : parent is
    attributeGroup,form=qualified, attributeFormDefault=qualified,
    attribute in xml doc is qualified with prefix
    """
    assert_bindings(
        schema="msData/attribute/attMc006.xsd",
        instance="msData/attribute/attMc006.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_mc005_att_mc005_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : parent is
    attributeGroup,form=qualified, attributeFormDefault=unqualified,
    attribute in xml doc is qualified with prefix
    """
    assert_bindings(
        schema="msData/attribute/attMc005.xsd",
        instance="msData/attribute/attMc005.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_mc004_att_mc004_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : parent is
    attributeGroup,form=qualified, attributeFormDefault=absent, attribute
    in xml doc is qualified with prefix
    """
    assert_bindings(
        schema="msData/attribute/attMc004.xsd",
        instance="msData/attribute/attMc004.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_mc003_att_mc003_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : parent is
    attributeGroup,form=qualified, attributeFormDefault=qualified,
    attribute in xml doc has no prefix, but the containing element has a
    default namespace declared
    """
    assert_bindings(
        schema="msData/attribute/attMc003.xsd",
        instance="msData/attribute/attMc003.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_mc002_att_mc002_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : parent is
    attributeGroup,form=qualified, attributeFormDefault=unqualified,
    attribute in xml doc has no prefix, but the containing element has a
    default namespace declared
    """
    assert_bindings(
        schema="msData/attribute/attMc002.xsd",
        instance="msData/attribute/attMc002.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_mc001_att_mc001_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : parent is
    attributeGroup,form=qualified, attributeFormDefault=absent, attribute
    in xml doc has no prefix, but the containing element has a default
    namespace declared
    """
    assert_bindings(
        schema="msData/attribute/attMc001.xsd",
        instance="msData/attribute/attMc001.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_mb012_att_mb012_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : parent is
    complexType, form=unqualified, attributeFormDefault=qualified,
    attribute in xml doc is qualified with prefix
    """
    assert_bindings(
        schema="msData/attribute/attMb012.xsd",
        instance="msData/attribute/attMb012.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_mb011_att_mb011_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : parent is
    complexType, form=unqualified, attributeFormDefault=unqualified,
    attribute in xml doc is qualified with prefix
    """
    assert_bindings(
        schema="msData/attribute/attMb011.xsd",
        instance="msData/attribute/attMb011.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_mb010_att_mb010_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : parent is
    complexType, form=unqualified, attributeFormDefault=absent, attribute
    in xml doc is qualified with prefix
    """
    assert_bindings(
        schema="msData/attribute/attMb010.xsd",
        instance="msData/attribute/attMb010.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_mb009_att_mb009_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : parent is
    complexType, form=unqualified, attributeFormDefault=qualified,
    attribute in xml doc has no prefix
    """
    assert_bindings(
        schema="msData/attribute/attMb009.xsd",
        instance="msData/attribute/attMb009.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_mb008_att_mb008_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : parent is
    complexType, form=unqualified, attributeFormDefault=unqualified,
    attribute in xml doc has no prefix, but the containing element has a
    default namespace declared
    """
    assert_bindings(
        schema="msData/attribute/attMb008.xsd",
        instance="msData/attribute/attMb008.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_mb007_att_mb007_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : parent is
    complexType, form=unqualified, attributeFormDefault=absent, attribute
    in xml doc has no prefix, but the containing element has a default
    namespace declared
    """
    assert_bindings(
        schema="msData/attribute/attMb007.xsd",
        instance="msData/attribute/attMb007.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_mb006_att_mb006_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : parent is
    complexType, form=qualified, attributeFormDefault=qualified, attribute
    in xml doc is qualified with prefix
    """
    assert_bindings(
        schema="msData/attribute/attMb006.xsd",
        instance="msData/attribute/attMb006.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_mb005_att_mb005_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : parent is
    complexType, form=qualified, attributeFormDefault=unqualified,
    attribute in xml doc is qualified with prefix
    """
    assert_bindings(
        schema="msData/attribute/attMb005.xsd",
        instance="msData/attribute/attMb005.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_mb004_att_mb004_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : parent is
    complexType, form=qualified, attributeFormDefault=absent, attribute in
    xml doc is qualified with prefix
    """
    assert_bindings(
        schema="msData/attribute/attMb004.xsd",
        instance="msData/attribute/attMb004.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_mb003_att_mb003_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : parent is
    complexType, form=qualified, attributeFormDefault=qualified, attribute
    in xml doc has no prefix, but the containing element has a default
    namespace declared
    """
    assert_bindings(
        schema="msData/attribute/attMb003.xsd",
        instance="msData/attribute/attMb003.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_mb002_att_mb002_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : parent is
    complexType, form=qualified, attributeFormDefault=unqualified,
    attribute in xml doc has no prefix, but the containing element has a
    default namespace declared
    """
    assert_bindings(
        schema="msData/attribute/attMb002.xsd",
        instance="msData/attribute/attMb002.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_mb001_att_mb001_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : parent is
    complexType, form=qualified, attributeFormDefault=absent, attribute in
    xml doc has no prefix, but the containing element has a default
    namespace declared
    """
    assert_bindings(
        schema="msData/attribute/attMb001.xsd",
        instance="msData/attribute/attMb001.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_ma004_att_ma004_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : parent is
    schema (ref in complexType and attributeGroup), form=unqualified,
    attributeFormDefault=qualified,attribute in xml doc is qualified with
    prefix
    """
    assert_bindings(
        schema="msData/attribute/attMa004.xsd",
        instance="msData/attribute/attMa004.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_ma003_att_ma003_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : parent is
    schema (ref in complexType and attributeGroup), form=qualified,
    attributeFormDefault=absentattribute in xml doc is qualified with
    prefix
    """
    assert_bindings(
        schema="msData/attribute/attMa003.xsd",
        instance="msData/attribute/attMa003.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_ma002_att_ma002_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : parent is
    schema (ref in complexType and attributeGroup), form=unqualified,
    attributeFormDefault=qualified,attribute in xml doc has no prefix, but
    the containing element has a default namespace declared
    """
    assert_bindings(
        schema="msData/attribute/attMa002.xsd",
        instance="msData/attribute/attMa002.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_ma001_att_ma001_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : parent is
    schema (ref in complexType and attributeGroup), form=qualified,
    attributeFormDefault=absentattribute in xml doc has no prefix, but the
    containing element has a default namespace declared
    """
    assert_bindings(
        schema="msData/attribute/attMa001.xsd",
        instance="msData/attribute/attMa001.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_o012_att_o012_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Validation
    Rule: Attribute Locally Valid (check normalization): type=string,
    fixed="#xd; #xd;A #xa; #xa;B #xd; #xa;" instant xml value='A B'
    """
    assert_bindings(
        schema="msData/attribute/attO012.xsd",
        instance="msData/attribute/attO012.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_o011_att_o011_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Validation
    Rule: Attribute Locally Valid (check normalization): type=string,
    fixed=" -linebreak -tab X -tab -linebreak Y -linebreak Z -linebreak",
    instant xml value=' X Y Z '
    """
    assert_bindings(
        schema="msData/attribute/attO011.xsd",
        instance="msData/attribute/attO011.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_o010_att_o010_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Validation
    Rule: Attribute Locally Valid (check normalization): type=NMTOKENS,
    fixed="#xd; #xd;A #xa; #xa;B #xd; #xa;" instant xml value='#xD #xD A
    #xA #xA B #xD #xA'
    """
    assert_bindings(
        schema="msData/attribute/attO010.xsd",
        instance="msData/attribute/attO010.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_o009_att_o009_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Validation
    Rule: Attribute Locally Valid (check normalization): type=NMTOKENS,
    fixed=" -linebreak -tab X -tab -linebreak Y -linebreak Z -linebreak",
    instant xml value='X Y Z'
    """
    assert_bindings(
        schema="msData/attribute/attO009.xsd",
        instance="msData/attribute/attO009.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_o008_att_o008_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Validation
    Rule: Attribute Locally Valid (check normalization): type=string,
    fixed=' 1 2 3', instant xml value=' 1 2 3'
    """
    assert_bindings(
        schema="msData/attribute/attO008.xsd",
        instance="msData/attribute/attO008.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_o007_att_o007_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Validation
    Rule: Attribute Locally Valid (check normalization): type=string,
    fixed=' 1 2 3', instant xml value=' 1 2 3'
    """
    assert_bindings(
        schema="msData/attribute/attO007.xsd",
        instance="msData/attribute/attO007.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_o006_att_o006_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Validation
    Rule: Attribute Locally Valid (check normalization): type=int, fixed='
    123', instant xml value=' 123 '
    """
    assert_bindings(
        schema="msData/attribute/attO006.xsd",
        instance="msData/attribute/attO006.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_o004_att_o004_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Validation
    Rule: Attribute Locally Valid: type=enumeration, instant xml value
    ='not a enumeration type'
    """
    assert_bindings(
        schema="msData/attribute/attO004.xsd",
        instance="msData/attribute/attO004.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_o001_att_o001_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Validation
    Rule: Attribute Locally Valid: type=int, instant xml value ='abc'
    """
    assert_bindings(
        schema="msData/attribute/attO001.xsd",
        instance="msData/attribute/attO001.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_lc006_att_lc006_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Validation
    Rule: Attribute Locally Valid: Parent is complexType, fixed='abc' ,
    xml instant NOT has the attribute at all,
    """
    assert_bindings(
        schema="msData/attribute/attLc006.xsd",
        instance="msData/attribute/attLc006.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_lc005_att_lc005_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Validation
    Rule: Attribute Locally Valid: Parent is complexType, fixed='abc' ,
    xml instant NOT has the attribute with value='abc',
    """
    assert_bindings(
        schema="msData/attribute/attLc005.xsd",
        instance="msData/attribute/attLc005.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_lc004_att_lc004_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Validation
    Rule: Attribute Locally Valid: Parent is complexType, fixed='abc' ,
    xml instant has the attribute with value='abc',
    """
    assert_bindings(
        schema="msData/attribute/attLc004.xsd",
        instance="msData/attribute/attLc004.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_lc003_att_lc003_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Validation
    Rule: Attribute Locally Valid: Parent is complexType, default='abc' ,
    xml instant NOT has the attribute at all,
    """
    assert_bindings(
        schema="msData/attribute/attLc003.xsd",
        instance="msData/attribute/attLc003.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_lc002_att_lc002_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Validation
    Rule: Attribute Locally Valid: Parent is complexType, default='abc' ,
    xml instant NOT has the attribute with value='abc',
    """
    assert_bindings(
        schema="msData/attribute/attLc002.xsd",
        instance="msData/attribute/attLc002.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_lc001_att_lc001_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Validation
    Rule: Attribute Locally Valid: Parent is complexType, default='abc' ,
    xml instant has the attribute with value='abc',
    """
    assert_bindings(
        schema="msData/attribute/attLc001.xsd",
        instance="msData/attribute/attLc001.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_lb006_att_lb006_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Validation
    Rule: Attribute Locally Valid: Parent is attributeGroup, fixed='abc' ,
    xml instant NOT has the attribute at all,
    """
    assert_bindings(
        schema="msData/attribute/attLb006.xsd",
        instance="msData/attribute/attLb006.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_lb005_att_lb005_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Validation
    Rule: Attribute Locally Valid: Parent is attributeGroup, fixed='abc' ,
    xml instant NOT has the attribute with value='abc',
    """
    assert_bindings(
        schema="msData/attribute/attLb005.xsd",
        instance="msData/attribute/attLb005.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_lb004_att_lb004_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Validation
    Rule: Attribute Locally Valid: Parent is attributeGroup, fixed='abc' ,
    xml instant has the attribute with value='abc',
    """
    assert_bindings(
        schema="msData/attribute/attLb004.xsd",
        instance="msData/attribute/attLb004.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_lb003_att_lb003_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Validation
    Rule: Attribute Locally Valid: Parent is attributeGroup, default='abc'
    , xml instant NOT has the attribute at all,
    """
    assert_bindings(
        schema="msData/attribute/attLb003.xsd",
        instance="msData/attribute/attLb003.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_lb002_att_lb002_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Validation
    Rule: Attribute Locally Valid: Parent is attributeGroup, default='abc'
    , xml instant NOT has the attribute with value='abc',
    """
    assert_bindings(
        schema="msData/attribute/attLb002.xsd",
        instance="msData/attribute/attLb002.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_lb001_att_lb001_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Validation
    Rule: Attribute Locally Valid: Parent is attributeGroup, default='abc'
    , xml instant has the attribute with value='abc',
    """
    assert_bindings(
        schema="msData/attribute/attLb001.xsd",
        instance="msData/attribute/attLb001.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_la006_att_la006_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Validation
    Rule: Attribute Locally Valid: Parent is schema , fixed='abc' , xml
    instant NOT has the attribute at all,
    """
    assert_bindings(
        schema="msData/attribute/attLa006.xsd",
        instance="msData/attribute/attLa006.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_la005_att_la005_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Validation
    Rule: Attribute Locally Valid: Parent is schema , fixed='abc' , xml
    instant NOT has the attribute with value='abc',
    """
    assert_bindings(
        schema="msData/attribute/attLa005.xsd",
        instance="msData/attribute/attLa005.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_la004_att_la004_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Validation
    Rule: Attribute Locally Valid: Parent is schema , fixed='abc' , xml
    instant has the attribute with value='abc',
    """
    assert_bindings(
        schema="msData/attribute/attLa004.xsd",
        instance="msData/attribute/attLa004.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_la003_att_la003_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Validation
    Rule: Attribute Locally Valid: Parent is schema , default='abc' , xml
    instant NOT has the attribute at all,
    """
    assert_bindings(
        schema="msData/attribute/attLa003.xsd",
        instance="msData/attribute/attLa003.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_la002_att_la002_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Validation
    Rule: Attribute Locally Valid: Parent is schema , default='abc' , xml
    instant NOT has the attribute with value='abc',
    """
    assert_bindings(
        schema="msData/attribute/attLa002.xsd",
        instance="msData/attribute/attLa002.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_la001_att_la001_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Validation
    Rule: Attribute Locally Valid: Parent is schema , default='abc' , xml
    instant has the attribute with value='abc',
    """
    assert_bindings(
        schema="msData/attribute/attLa001.xsd",
        instance="msData/attribute/attLa001.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_i003_att_i003_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Basic
    attribute with annotation followed by simpleType content
    """
    assert_bindings(
        schema="msData/attribute/attI003.xsd",
        instance="msData/attribute/attI003.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_j018_att_j018_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Basic
    attribute with parent schema, parent attributeGroup, parent
    complexType (test most of the common type and ref)
    """
    assert_bindings(
        schema="msData/attribute/attJ018.xsd",
        instance="msData/attribute/attJ018.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_j010_att_j010_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : xml doc do
    not specify the attribute, attribute decl under attribute group use =
    'required'
    """
    assert_bindings(
        schema="msData/attribute/attJ010.xsd",
        instance="msData/attribute/attJ010.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_j009_att_j009_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : xml doc do
    not specify the attribute, attribute decl under complexType, use =
    'required'
    """
    assert_bindings(
        schema="msData/attribute/attJ009.xsd",
        instance="msData/attribute/attJ009.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_j008_att_j008_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : xml doc do
    not specify the attribute, attribute decl under schema use =
    'required'
    """
    assert_bindings(
        schema="msData/attribute/attJ008.xsd",
        instance="msData/attribute/attJ008.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_j007_att_j007_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : xml doc
    specify the attribute, for att declared under complexType and
    attributeGroup, use = 'required'
    """
    assert_bindings(
        schema="msData/attribute/attJ007.xsd",
        instance="msData/attribute/attJ007.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_j006_att_j006_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : xml doc
    specify the attribute, use = 'optional'
    """
    assert_bindings(
        schema="msData/attribute/attJ006.xsd",
        instance="msData/attribute/attJ006.xml",
        class_name="Test",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_j005_att_j005_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : xml doc do
    not specify the attribute, use = 'optional'
    """
    assert_bindings(
        schema="msData/attribute/attJ005.xsd",
        instance="msData/attribute/attJ005.xml",
        class_name="Test",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_j004_att_j004_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : xml doc does
    not specify the attribute, attribute decl under attribute group, use =
    'prohibited'
    """
    assert_bindings(
        schema="msData/attribute/attJ004.xsd",
        instance="msData/attribute/attJ004.xml",
        class_name="Test",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_j003_att_j003_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : xml doc
    specify the attribute, attribute decl under complex type, use =
    'prohibited'
    """
    assert_bindings(
        schema="msData/attribute/attJ003.xsd",
        instance="msData/attribute/attJ003.xml",
        class_name="Test",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_j002_att_j002_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : xml doc
    specify the attribute, attribute decl under schema, use = 'prohibited'
    """
    assert_bindings(
        schema="msData/attribute/attJ002.xsd",
        instance="msData/attribute/attJ002.xml",
        class_name="Test",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_j001_att_j001_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : xml doc do
    not specify the attribute, for att declared under schema, complexType
    and attributeGroup, use = 'prohibited'
    """
    assert_bindings(
        schema="msData/attribute/attJ001.xsd",
        instance="msData/attribute/attJ001.xml",
        class_name="Test",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_f003_att_f003_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Test
    attribute declaration with optional attribute use = 'required'
    """
    assert_bindings(
        schema="msData/attribute/attF003.xsd",
        instance="msData/attribute/attF003.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_f002_att_f002_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Test
    attribute declaration with optional attribute use = 'optional'
    """
    assert_bindings(
        schema="msData/attribute/attF002.xsd",
        instance="msData/attribute/attF002.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_att_f001_att_f001_i(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Test
    attribute declaration with optional attribute use = 'prohibited'
    """
    assert_bindings(
        schema="msData/attribute/attF001.xsd",
        instance="msData/attribute/attF001.xml",
        class_name="Test",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_e001_att_e001_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Local
    attribute declaration ref='global attribute name'
    """
    assert_bindings(
        schema="msData/attribute/attE001.xsd",
        instance="msData/attribute/attE001.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_d007_att_d007_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Global
    attribute declaration type='simpleType with a union of two list and a
    atomic simpleType'
    """
    assert_bindings(
        schema="msData/attribute/attD007.xsd",
        instance="msData/attribute/attD007.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_d004_att_d004_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Global
    attribute declaration type='simpleType with a list of number'
    """
    assert_bindings(
        schema="msData/attribute/attD004.xsd",
        instance="msData/attribute/attD004.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_att_d003_att_d003_v(json_360, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Global
    attribute declaration type='simpleType derived by restrictrion from
    another simpleType'
    """
    assert_bindings(
        schema="msData/attribute/attD003.xsd",
        instance="msData/attribute/attD003.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ct_z013e_ct_z013e_i(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : fixed
    value on mixed type element (5)
    """
    assert_bindings(
        schema="msData/complexType/ctZ013.xsd",
        instance="msData/complexType/ctZ013e.xml",
        class_name="E",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ct_z013d_ct_z013d_i(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : fixed
    value on mixed type element (4)
    """
    assert_bindings(
        schema="msData/complexType/ctZ013.xsd",
        instance="msData/complexType/ctZ013d.xml",
        class_name="E",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ct_z013c_ct_z013c_i(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : fixed
    value on mixed type element (3)
    """
    assert_bindings(
        schema="msData/complexType/ctZ013.xsd",
        instance="msData/complexType/ctZ013c.xml",
        class_name="E",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_z013b_ct_z013b_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : fixed
    value on mixed type element (2)
    """
    assert_bindings(
        schema="msData/complexType/ctZ013.xsd",
        instance="msData/complexType/ctZ013b.xml",
        class_name="E",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_z013a_ct_z013a_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : fixed
    value on mixed type element (1)
    """
    assert_bindings(
        schema="msData/complexType/ctZ013.xsd",
        instance="msData/complexType/ctZ013a.xml",
        class_name="E",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_z011_b_ct_z011_b_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    "anyType" in instance document using xsi:type(2)
    """
    assert_bindings(
        schema="msData/complexType/ctZ011.xsd",
        instance="msData/complexType/ctZ011.xml",
        class_name="A",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="No schema")
def test_ct_z011_a_ct_z011_a_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    "anyType" in instance document using xsi:type(1)
    """
    assert_bindings(
        schema="",
        instance="msData/complexType/ctZ011.xml",
        class_name="A",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_z009_d_ct_z009_d_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Ambiguous but valid content models (6)
    """
    assert_bindings(
        schema="msData/complexType/ctZ009_d.xsd",
        instance="msData/complexType/ctZ009_d.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ct_z009_c_ct_z009_c_i(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Ambiguous but valid content models (5)
    """
    assert_bindings(
        schema="msData/complexType/ctZ009_c.xsd",
        instance="msData/complexType/ctZ009_c.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_z009_b_ct_z009_b_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Ambiguous but valid content models (4)
    """
    assert_bindings(
        schema="msData/complexType/ctZ009_a.xsd",
        instance="msData/complexType/ctZ009_b.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_z009_a_ct_z009_a_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Ambiguous but valid content models (3)
    """
    assert_bindings(
        schema="msData/complexType/ctZ009_a.xsd",
        instance="msData/complexType/ctZ009_a.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_z009_ct_z009_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Ambiguous but valid content models (2)
    """
    assert_bindings(
        schema="msData/complexType/ctZ009.xsd",
        instance="msData/complexType/ctZ009.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_z008_ct_z008_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Ambiguous but valid content models
    """
    assert_bindings(
        schema="msData/complexType/ctZ008.xsd",
        instance="msData/complexType/ctZ008.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.xfail
def test_ct_z007_ct_z007_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : Derived
    types validated as base type when substitution group used
    """
    assert_bindings(
        schema="msData/complexType/ctZ007_a.xsd",
        instance="msData/complexType/ctZ007.xml",
        class_name="Customers",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_z006_ct_z006_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Inderterminstic schemas
    """
    assert_bindings(
        schema="msData/complexType/ctZ006.xsd",
        instance="msData/complexType/ctZ006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ct_z005_ct_z005_i(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    id="85834" description="xsd: circular reference of complexType is
    allowed if the content model is not endless."
    """
    assert_bindings(
        schema="msData/complexType/ctZ005.xsd",
        instance="msData/complexType/ctZ005.xml",
        class_name="Foo",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_z003_ct_z003_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    id="85834" description="xsd: circular reference of complexType is
    allowed if the content model is not endless."
    """
    assert_bindings(
        schema="msData/complexType/ctZ003.xsd",
        instance="msData/complexType/ctZ003.xml",
        class_name="Foo",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_z001_ct_z001_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    extensions to xsd:anyType in substitution groups
    """
    assert_bindings(
        schema="msData/complexType/75039.xsd",
        instance="msData/complexType/75039.xml",
        class_name="BagOfHeads",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_o006_ct_o006_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    derivation=restriction. Derived type has Attribute Wildcard. Derived
    wildcard namespace constraint is a subset of base
    """
    assert_bindings(
        schema="msData/complexType/ctO006.xsd",
        instance="msData/complexType/ctO006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_o003_ct_o003_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    derivation=restriction. Attribute wildcard in base type. Derived type
    has attribute that is valid with respect to wildcard
    """
    assert_bindings(
        schema="msData/complexType/ctO003.xsd",
        instance="msData/complexType/ctO003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_o001_ct_o001_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    derivation=restriction. final base type not restriction
    """
    assert_bindings(
        schema="msData/complexType/ctO001.xsd",
        instance="msData/complexType/ctO001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_n004_ct_n004_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    derivation=extension. Attribute wildcard ##any in base type. Derived
    type has wildcard with ##local namespace constraint.
    """
    assert_bindings(
        schema="msData/complexType/ctN004.xsd",
        instance="msData/complexType/ctN004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_n003_ct_n003_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    derivation=extension. Attribute wildcard ##local in base type. Derived
    type has wildcard with ##any namespace constraint.
    """
    assert_bindings(
        schema="msData/complexType/ctN003.xsd",
        instance="msData/complexType/ctN003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_n001_ct_n001_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    derivation=extension. final of base type not extension
    """
    assert_bindings(
        schema="msData/complexType/ctN001.xsd",
        instance="msData/complexType/ctN001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_m002_ct_m002_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexType with base type a simpleType. derivation = extension
    """
    assert_bindings(
        schema="msData/complexType/ctM002.xsd",
        instance="msData/complexType/ctM002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_l022_ct_l022_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : ability
    to use abstract complexType as xsi:type using inline schemas
    """
    assert_bindings(
        schema="msData/complexType/test67200.xsd",
        instance="msData/complexType/test67200.xml",
        class_name="Elt1",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_l021_ct_l021_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    has attribute wildcard, processContents = 'strict' instance document
    has attributes and namespace has definition
    """
    assert_bindings(
        schema="msData/complexType/ctL021.xsd",
        instance="msData/complexType/ctL021.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ct_l020_ct_l020_i(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    has attribute wildcard, processContents = 'strict' instance document
    has attributes but namespace does have definition
    """
    assert_bindings(
        schema="msData/complexType/ctL020.xsd",
        instance="msData/complexType/ctL020.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_l019_ct_l019_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    has attribute wildcard, processContents = 'strict' instance document
    has attributes missing
    """
    assert_bindings(
        schema="msData/complexType/ctL019.xsd",
        instance="msData/complexType/ctL019.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_l018_ct_l018_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    has attribute wildcard, processContents = 'lax' instance document has
    attributes
    """
    assert_bindings(
        schema="msData/complexType/ctL018.xsd",
        instance="msData/complexType/ctL018.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_l017_ct_l017_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    has attribute wildcard, processContents = 'lax' instance document has
    attributes missing
    """
    assert_bindings(
        schema="msData/complexType/ctL017.xsd",
        instance="msData/complexType/ctL017.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_l016_ct_l016_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    has attribute wildcard, processContents = 'skip' instance document has
    attributes
    """
    assert_bindings(
        schema="msData/complexType/ctL016.xsd",
        instance="msData/complexType/ctL016.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_l015_ct_l015_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    has attribute wildcard, processContents = 'skip' instance document has
    attributes missing
    """
    assert_bindings(
        schema="msData/complexType/ctL015.xsd",
        instance="msData/complexType/ctL015.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_l014_ct_l014_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    has attributes defined. instance document has attributes
    """
    assert_bindings(
        schema="msData/complexType/ctL014.xsd",
        instance="msData/complexType/ctL014.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ct_l013_ct_l013_i(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    has attributes defined. instance document has attributes missing
    """
    assert_bindings(
        schema="msData/complexType/ctL013.xsd",
        instance="msData/complexType/ctL013.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ct_l012_ct_l012_i(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    is mixed. instance document elements are in a different order from
    type definition
    """
    assert_bindings(
        schema="msData/complexType/ctL012.xsd",
        instance="msData/complexType/ctL012.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_l011_ct_l011_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    is mixed. instance document elements in same order as type definition
    """
    assert_bindings(
        schema="msData/complexType/ctL011.xsd",
        instance="msData/complexType/ctL011.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ct_l010_ct_l010_i(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    is element only. instance document element has element children not in
    schema
    """
    assert_bindings(
        schema="msData/complexType/ctL010.xsd",
        instance="msData/complexType/ctL010.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ct_l009_ct_l009_i(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    is element only. instance document elements are in a different order
    from type definition
    """
    assert_bindings(
        schema="msData/complexType/ctL009.xsd",
        instance="msData/complexType/ctL009.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_l008_ct_l008_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    is element only. instance document elements in same order as type
    definition
    """
    assert_bindings(
        schema="msData/complexType/ctL008.xsd",
        instance="msData/complexType/ctL008.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_l007_ct_l007_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    is element only. instance document element only whitespace
    """
    assert_bindings(
        schema="msData/complexType/ctL007.xsd",
        instance="msData/complexType/ctL007.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ct_l006_ct_l006_i(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    is element only. instance document element has character information
    """
    assert_bindings(
        schema="msData/complexType/ctL006.xsd",
        instance="msData/complexType/ctL006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_l005_ct_l005_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    is element only. instance document element has element children
    """
    assert_bindings(
        schema="msData/complexType/ctL005.xsd",
        instance="msData/complexType/ctL005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ct_l004_ct_l004_i(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent. instance document element has element children
    """
    assert_bindings(
        schema="msData/complexType/ctL004.xsd",
        instance="msData/complexType/ctL004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_l003_ct_l003_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    is empty. instance document element is empty
    """
    assert_bindings(
        schema="msData/complexType/ctL003.xsd",
        instance="msData/complexType/ctL003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ct_l002_ct_l002_i(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    is empty. instance document element has element children
    """
    assert_bindings(
        schema="msData/complexType/ctL002.xsd",
        instance="msData/complexType/ctL002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ct_l001_ct_l001_i(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    is empty. instance document element has text
    """
    assert_bindings(
        schema="msData/complexType/ctL001.xsd",
        instance="msData/complexType/ctL001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_k001_ct_k001_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent with base = a complexType definition whose parent base
    is a simpleType
    """
    assert_bindings(
        schema="msData/complexType/ctK001.xsd",
        instance="msData/complexType/ctK001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_j001_ct_j001_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent with base = a complexType definition
    """
    assert_bindings(
        schema="msData/complexType/ctJ001.xsd",
        instance="msData/complexType/ctJ001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_i050_ct_i050_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexType with attribute abstract = 'true' , derived complexType
    from abstract used by instance document element
    """
    assert_bindings(
        schema="msData/complexType/ctI050.xsd",
        instance="msData/complexType/ctI050.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ct_i049_ct_i049_i(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexType with attribute abstract = 'true' , instance document
    element has xsi:type as complexType
    """
    assert_bindings(
        schema="msData/complexType/ctI049.xsd",
        instance="msData/complexType/ctI049.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ct_i048_ct_i048_i(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexType with attribute abstract = 'true' , instance document
    element has type as complexType
    """
    assert_bindings(
        schema="msData/complexType/ctI048.xsd",
        instance="msData/complexType/ctI048.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_i047_ct_i047_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : schema
    with blockDefault = 'extension' and block='restriction' , use xsi:type
    of substituted complexType by extension
    """
    assert_bindings(
        schema="msData/complexType/ctI047.xsd",
        instance="msData/complexType/ctI047.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_i046_ct_i046_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : schema
    with blockDefault = 'extension' , use xsi:type of substituted
    complexType by restriction
    """
    assert_bindings(
        schema="msData/complexType/ctI046.xsd",
        instance="msData/complexType/ctI046.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ct_i045_ct_i045_i(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : schema
    with blockDefault = 'extension' , use xsi:type of substituted
    complexType by extension
    """
    assert_bindings(
        schema="msData/complexType/ctI045.xsd",
        instance="msData/complexType/ctI045.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_i044_ct_i044_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : schema
    with blockDefault = 'restriction' and block='extension' , use xsi:type
    of substituted complexType by restriction
    """
    assert_bindings(
        schema="msData/complexType/ctI044.xsd",
        instance="msData/complexType/ctI044.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_i043_ct_i043_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : schema
    with blockDefault = 'restriction' , use xsi:type of substituted
    complexType by extension
    """
    assert_bindings(
        schema="msData/complexType/ctI043.xsd",
        instance="msData/complexType/ctI043.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ct_i042_ct_i042_i(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : schema
    with blockDefault = 'restriction' , use xsi:type of substituted
    complexType by restriction
    """
    assert_bindings(
        schema="msData/complexType/ctI042.xsd",
        instance="msData/complexType/ctI042.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_i041_ct_i041_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : schema
    with blockDefault = '#all' and block='' , use xsi:type of substituted
    complexType by extension
    """
    assert_bindings(
        schema="msData/complexType/ctI041.xsd",
        instance="msData/complexType/ctI041.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_i040_ct_i040_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : schema
    with blockDefault = '#all' and block='' , use xsi:type of substituted
    complexType by restriction
    """
    assert_bindings(
        schema="msData/complexType/ctI040.xsd",
        instance="msData/complexType/ctI040.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ct_i039_ct_i039_i(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : schema
    with blockDefault = '#all' , use xsi:type of substituted complexType
    by extension
    """
    assert_bindings(
        schema="msData/complexType/ctI039.xsd",
        instance="msData/complexType/ctI039.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ct_i038_ct_i038_i(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : schema
    with blockDefault = '#all' , use xsi:type of substituted complexType
    by restriction
    """
    assert_bindings(
        schema="msData/complexType/ctI038.xsd",
        instance="msData/complexType/ctI038.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_i037_ct_i037_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : schema
    with blockDefault = '' , use xsi:type of substituted complexType by
    extension
    """
    assert_bindings(
        schema="msData/complexType/ctI037.xsd",
        instance="msData/complexType/ctI037.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_i036_ct_i036_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : schema
    with blockDefault = '' , use xsi:type of substituted complexType by
    restriction
    """
    assert_bindings(
        schema="msData/complexType/ctI036.xsd",
        instance="msData/complexType/ctI036.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ct_i035_ct_i035_i(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexType with attribute block = 'extension' , use xsi:type of
    substituted complexType by extension
    """
    assert_bindings(
        schema="msData/complexType/ctI035.xsd",
        instance="msData/complexType/ctI035.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_i034_ct_i034_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexType with attribute block = 'extension' , use xsi:type of
    substituted complexType by restriction
    """
    assert_bindings(
        schema="msData/complexType/ctI034.xsd",
        instance="msData/complexType/ctI034.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_i033_ct_i033_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexType with attribute block = 'restriction' , use xsi:type of
    substituted complexType by extension
    """
    assert_bindings(
        schema="msData/complexType/ctI033.xsd",
        instance="msData/complexType/ctI033.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ct_i032_ct_i032_i(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexType with attribute block = 'restriction' , use xsi:type of
    substituted complexType by restriction
    """
    assert_bindings(
        schema="msData/complexType/ctI032.xsd",
        instance="msData/complexType/ctI032.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ct_i031_ct_i031_i(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexType with attribute block = '#all' , use xsi:type of
    substituted complexType by extension
    """
    assert_bindings(
        schema="msData/complexType/ctI031.xsd",
        instance="msData/complexType/ctI031.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ct_i030_ct_i030_i(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexType with attribute block = '#all' , use xsi:type of
    substituted complexType by restriction
    """
    assert_bindings(
        schema="msData/complexType/ctI030.xsd",
        instance="msData/complexType/ctI030.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_i029_ct_i029_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexType with attribute block = '' , use xsi:type of substituted
    complexType by extension
    """
    assert_bindings(
        schema="msData/complexType/ctI029.xsd",
        instance="msData/complexType/ctI029.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_i028_ct_i028_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexType with attribute block = '' , use xsi:type of substituted
    complexType by restriction
    """
    assert_bindings(
        schema="msData/complexType/ctI028.xsd",
        instance="msData/complexType/ctI028.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_i027_ct_i027_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : schema
    with finalDefault = 'restriction extension' and final='extension' ,
    derived complexType by restriction
    """
    assert_bindings(
        schema="msData/complexType/ctI027.xsd",
        instance="msData/complexType/ctI027.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_i026_ct_i026_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : schema
    with finalDefault = 'restriction extension' and final='restriction' ,
    derived complexType by extension
    """
    assert_bindings(
        schema="msData/complexType/ctI026.xsd",
        instance="msData/complexType/ctI026.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_i025_ct_i025_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : schema
    with finalDefault = 'extension' and final='restriction' , derived
    complexType by extension
    """
    assert_bindings(
        schema="msData/complexType/ctI025.xsd",
        instance="msData/complexType/ctI025.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_i023_ct_i023_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : schema
    with finalDefault = 'extension' , derived complexType by restriction
    """
    assert_bindings(
        schema="msData/complexType/ctI023.xsd",
        instance="msData/complexType/ctI023.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_i022_ct_i022_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : schema
    with finalDefault = 'restriction' and final='extension' , derived
    complexType by restriction
    """
    assert_bindings(
        schema="msData/complexType/ctI022.xsd",
        instance="msData/complexType/ctI022.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_i021_ct_i021_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : schema
    with finalDefault = 'restriction' , derived complexType by extension
    """
    assert_bindings(
        schema="msData/complexType/ctI021.xsd",
        instance="msData/complexType/ctI021.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_i019_ct_i019_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : schema
    with finalDefault = '#all' and final='' , derived complexType by
    extension
    """
    assert_bindings(
        schema="msData/complexType/ctI019.xsd",
        instance="msData/complexType/ctI019.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_i018_ct_i018_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : schema
    with finalDefault = '#all' and final='' , derived complexType by
    restriction
    """
    assert_bindings(
        schema="msData/complexType/ctI018.xsd",
        instance="msData/complexType/ctI018.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_i015_ct_i015_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : schema
    with finalDefault = '' , derived complexType by extension
    """
    assert_bindings(
        schema="msData/complexType/ctI015.xsd",
        instance="msData/complexType/ctI015.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_i014_ct_i014_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : schema
    with finalDefault = '' , derived complexType by restriction
    """
    assert_bindings(
        schema="msData/complexType/ctI014.xsd",
        instance="msData/complexType/ctI014.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_i010_ct_i010_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexType with attribute final = 'extension' , derived complexType
    by restriction
    """
    assert_bindings(
        schema="msData/complexType/ctI010.xsd",
        instance="msData/complexType/ctI010.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_i009_ct_i009_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexType with attribute final = 'restriction' , derived complexType
    by extension
    """
    assert_bindings(
        schema="msData/complexType/ctI009.xsd",
        instance="msData/complexType/ctI009.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_i005_ct_i005_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexType with attribute final = '' , derived complexType by
    extension
    """
    assert_bindings(
        schema="msData/complexType/ctI005.xsd",
        instance="msData/complexType/ctI005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_i004_ct_i004_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexType with attribute final = '' , derived complexType by
    restriction
    """
    assert_bindings(
        schema="msData/complexType/ctI004.xsd",
        instance="msData/complexType/ctI004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_i003_ct_i003_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexType with name = 'fooType' , global attribute with
    name='fooType'
    """
    assert_bindings(
        schema="msData/complexType/ctI003.xsd",
        instance="msData/complexType/ctI003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_h082_ct_h082_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with group then
    anyAttribute using a list
    """
    assert_bindings(
        schema="msData/complexType/ctH082.xsd",
        instance="msData/complexType/ctH082.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_h071_ct_h071_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with anyAttribute
    """
    assert_bindings(
        schema="msData/complexType/ctH071.xsd",
        instance="msData/complexType/ctH071.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_h069_ct_h069_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with attributeGroup
    then anyAttribute
    """
    assert_bindings(
        schema="msData/complexType/ctH069.xsd",
        instance="msData/complexType/ctH069.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_h068_ct_h068_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with attributeGroup
    then attributeGroup
    """
    assert_bindings(
        schema="msData/complexType/ctH068.xsd",
        instance="msData/complexType/ctH068.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_h067_ct_h067_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with attributeGroup
    then two attributes
    """
    assert_bindings(
        schema="msData/complexType/ctH067.xsd",
        instance="msData/complexType/ctH067.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_h066_ct_h066_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with attributeGroup
    then attribute
    """
    assert_bindings(
        schema="msData/complexType/ctH066.xsd",
        instance="msData/complexType/ctH066.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_h060_ct_h060_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with attributeGroup
    """
    assert_bindings(
        schema="msData/complexType/ctH060.xsd",
        instance="msData/complexType/ctH060.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_h058_ct_h058_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with attribute then
    anyAttribute
    """
    assert_bindings(
        schema="msData/complexType/ctH058.xsd",
        instance="msData/complexType/ctH058.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_h057_ct_h057_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with attribute then
    two attributeGroups
    """
    assert_bindings(
        schema="msData/complexType/ctH057.xsd",
        instance="msData/complexType/ctH057.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_h056_ct_h056_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with attribute then
    attributeGroup
    """
    assert_bindings(
        schema="msData/complexType/ctH056.xsd",
        instance="msData/complexType/ctH056.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_h055_ct_h055_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with attribute then
    attribute
    """
    assert_bindings(
        schema="msData/complexType/ctH055.xsd",
        instance="msData/complexType/ctH055.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_h049_ct_h049_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with attribute
    """
    assert_bindings(
        schema="msData/complexType/ctH049.xsd",
        instance="msData/complexType/ctH049.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_h047_ct_h047_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with sequence then
    anyAttribute
    """
    assert_bindings(
        schema="msData/complexType/ctH047.xsd",
        instance="msData/complexType/ctH047.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_h046_ct_h046_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with sequence then
    two attributeGroups
    """
    assert_bindings(
        schema="msData/complexType/ctH046.xsd",
        instance="msData/complexType/ctH046.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_h045_ct_h045_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with sequence then
    attributeGroup
    """
    assert_bindings(
        schema="msData/complexType/ctH045.xsd",
        instance="msData/complexType/ctH045.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_h044_ct_h044_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with sequence then
    two attributes
    """
    assert_bindings(
        schema="msData/complexType/ctH044.xsd",
        instance="msData/complexType/ctH044.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_h043_ct_h043_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with sequence then
    attribute
    """
    assert_bindings(
        schema="msData/complexType/ctH043.xsd",
        instance="msData/complexType/ctH043.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_h037_ct_h037_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with sequence
    """
    assert_bindings(
        schema="msData/complexType/ctH037.xsd",
        instance="msData/complexType/ctH037.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_h035_ct_h035_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with choice then
    anyAttribute
    """
    assert_bindings(
        schema="msData/complexType/ctH035.xsd",
        instance="msData/complexType/ctH035.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_h034_ct_h034_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with choice then two
    attributeGroups
    """
    assert_bindings(
        schema="msData/complexType/ctH034.xsd",
        instance="msData/complexType/ctH034.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_h033_ct_h033_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with choice then
    attributeGroup
    """
    assert_bindings(
        schema="msData/complexType/ctH033.xsd",
        instance="msData/complexType/ctH033.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_h032_ct_h032_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with choice then two
    attributes
    """
    assert_bindings(
        schema="msData/complexType/ctH032.xsd",
        instance="msData/complexType/ctH032.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_h031_ct_h031_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with choice then
    attribute
    """
    assert_bindings(
        schema="msData/complexType/ctH031.xsd",
        instance="msData/complexType/ctH031.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_h025_ct_h025_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with choice
    """
    assert_bindings(
        schema="msData/complexType/ctH025.xsd",
        instance="msData/complexType/ctH025.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_h011_ct_h011_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with group then
    anyAttribute
    """
    assert_bindings(
        schema="msData/complexType/ctH011.xsd",
        instance="msData/complexType/ctH011.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_h010_ct_h010_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with group then two
    attributeGroups
    """
    assert_bindings(
        schema="msData/complexType/ctH010.xsd",
        instance="msData/complexType/ctH010.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_h009_ct_h009_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with group then
    attributeGroup
    """
    assert_bindings(
        schema="msData/complexType/ctH009.xsd",
        instance="msData/complexType/ctH009.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_h008_ct_h008_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with group then two
    attributes
    """
    assert_bindings(
        schema="msData/complexType/ctH008.xsd",
        instance="msData/complexType/ctH008.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_h007_ct_h007_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with group then
    attribute
    """
    assert_bindings(
        schema="msData/complexType/ctH007.xsd",
        instance="msData/complexType/ctH007.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_h001_ct_h001_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with group
    """
    assert_bindings(
        schema="msData/complexType/ctH001.xsd",
        instance="msData/complexType/ctH001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g071_ct_g071_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with anyAttribute
    """
    assert_bindings(
        schema="msData/complexType/ctG071.xsd",
        instance="msData/complexType/ctG071.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g069_ct_g069_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with attributeGroup
    then anyAttribute
    """
    assert_bindings(
        schema="msData/complexType/ctG069.xsd",
        instance="msData/complexType/ctG069.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g068_ct_g068_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with attributeGroup
    then attributeGroup
    """
    assert_bindings(
        schema="msData/complexType/ctG068.xsd",
        instance="msData/complexType/ctG068.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g067_ct_g067_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with attributeGroup
    then two attributes
    """
    assert_bindings(
        schema="msData/complexType/ctG067.xsd",
        instance="msData/complexType/ctG067.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g066_ct_g066_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with attributeGroup
    then attribute
    """
    assert_bindings(
        schema="msData/complexType/ctG066.xsd",
        instance="msData/complexType/ctG066.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g060_ct_g060_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with attributeGroup
    """
    assert_bindings(
        schema="msData/complexType/ctG060.xsd",
        instance="msData/complexType/ctG060.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g058_ct_g058_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with attribute then
    anyAttribute
    """
    assert_bindings(
        schema="msData/complexType/ctG058.xsd",
        instance="msData/complexType/ctG058.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g057_ct_g057_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with attribute then
    two attributeGroups
    """
    assert_bindings(
        schema="msData/complexType/ctG057.xsd",
        instance="msData/complexType/ctG057.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g056_ct_g056_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with attribute then
    attributeGroup
    """
    assert_bindings(
        schema="msData/complexType/ctG056.xsd",
        instance="msData/complexType/ctG056.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g055_ct_g055_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with attribute then
    attribute
    """
    assert_bindings(
        schema="msData/complexType/ctG055.xsd",
        instance="msData/complexType/ctG055.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g049_ct_g049_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with attribute
    """
    assert_bindings(
        schema="msData/complexType/ctG049.xsd",
        instance="msData/complexType/ctG049.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g047_ct_g047_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with sequence then
    anyAttribute
    """
    assert_bindings(
        schema="msData/complexType/ctG047.xsd",
        instance="msData/complexType/ctG047.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g046_ct_g046_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with sequence then
    two attributeGroups
    """
    assert_bindings(
        schema="msData/complexType/ctG046.xsd",
        instance="msData/complexType/ctG046.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g045_ct_g045_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with sequence then
    attributeGroup
    """
    assert_bindings(
        schema="msData/complexType/ctG045.xsd",
        instance="msData/complexType/ctG045.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g044_ct_g044_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with sequence then
    two attributes
    """
    assert_bindings(
        schema="msData/complexType/ctG044.xsd",
        instance="msData/complexType/ctG044.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g043_ct_g043_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with sequence then
    attribute
    """
    assert_bindings(
        schema="msData/complexType/ctG043.xsd",
        instance="msData/complexType/ctG043.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g037_ct_g037_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with sequence
    """
    assert_bindings(
        schema="msData/complexType/ctG037.xsd",
        instance="msData/complexType/ctG037.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g035_ct_g035_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with choice then
    anyAttribute
    """
    assert_bindings(
        schema="msData/complexType/ctG035.xsd",
        instance="msData/complexType/ctG035.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g034_ct_g034_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with choice then
    two attributeGroups
    """
    assert_bindings(
        schema="msData/complexType/ctG034.xsd",
        instance="msData/complexType/ctG034.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g033_ct_g033_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with choice then
    attributeGroup
    """
    assert_bindings(
        schema="msData/complexType/ctG033.xsd",
        instance="msData/complexType/ctG033.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g032_ct_g032_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with choice then
    two attributes
    """
    assert_bindings(
        schema="msData/complexType/ctG032.xsd",
        instance="msData/complexType/ctG032.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g031_ct_g031_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with choice then
    attribute
    """
    assert_bindings(
        schema="msData/complexType/ctG031.xsd",
        instance="msData/complexType/ctG031.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g025_ct_g025_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with choice
    """
    assert_bindings(
        schema="msData/complexType/ctG025.xsd",
        instance="msData/complexType/ctG025.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g023_ct_g023_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with all then
    anyAttribute
    """
    assert_bindings(
        schema="msData/complexType/ctG023.xsd",
        instance="msData/complexType/ctG023.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g022_ct_g022_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with all then two
    attributeGroups
    """
    assert_bindings(
        schema="msData/complexType/ctG022.xsd",
        instance="msData/complexType/ctG022.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g021_ct_g021_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with all then
    attributeGroup
    """
    assert_bindings(
        schema="msData/complexType/ctG021.xsd",
        instance="msData/complexType/ctG021.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g020_ct_g020_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with all then two
    attributes
    """
    assert_bindings(
        schema="msData/complexType/ctG020.xsd",
        instance="msData/complexType/ctG020.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g019_ct_g019_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with all then
    attribute
    """
    assert_bindings(
        schema="msData/complexType/ctG019.xsd",
        instance="msData/complexType/ctG019.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g013_ct_g013_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with all
    """
    assert_bindings(
        schema="msData/complexType/ctG013.xsd",
        instance="msData/complexType/ctG013.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g011_ct_g011_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with group then
    anyAttribute TSTF concluded these schemas are OK in 1.0, despite
    violating subsumption
    """
    assert_bindings(
        schema="msData/complexType/ctG011.xsd",
        instance="msData/complexType/ctG011.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g010_ct_g010_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with group then two
    attributeGroups TSTF concluded these schemas are OK in 1.0, despite
    violating subsumption
    """
    assert_bindings(
        schema="msData/complexType/ctG010.xsd",
        instance="msData/complexType/ctG010.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g009_ct_g009_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with group then
    attributeGroup TSTF concluded these schemas are OK in 1.0, despite
    violating subsumption
    """
    assert_bindings(
        schema="msData/complexType/ctG009.xsd",
        instance="msData/complexType/ctG009.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g008_ct_g008_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with group then two
    attributes TSTF concluded these schemas are OK in 1.0, despite
    violating subsumption
    """
    assert_bindings(
        schema="msData/complexType/ctG008.xsd",
        instance="msData/complexType/ctG008.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g007_ct_g007_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with group then
    attribute TSTF concluded these schemas are OK in 1.0, despite
    violating subsumption
    """
    assert_bindings(
        schema="msData/complexType/ctG007.xsd",
        instance="msData/complexType/ctG007.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_g001_ct_g001_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with group TSTF
    concluded these schemas are OK in 1.0, despite violating subsumption
    """
    assert_bindings(
        schema="msData/complexType/ctG001.xsd",
        instance="msData/complexType/ctG001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_f014_ct_f014_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent and content of extension
    """
    assert_bindings(
        schema="msData/complexType/ctF014.xsd",
        instance="msData/complexType/ctF014.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_f013_ct_f013_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent and content of annotation and restriction
    """
    assert_bindings(
        schema="msData/complexType/ctF013.xsd",
        instance="msData/complexType/ctF013.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_f011_ct_f011_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent with optional attribute mixed = 'false' and content of
    extension then content of sequence with elements
    """
    assert_bindings(
        schema="msData/complexType/ctF011.xsd",
        instance="msData/complexType/ctF011.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_f010_ct_f010_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent with optional attribute mixed = 'false' and content of
    extension then empty content
    """
    assert_bindings(
        schema="msData/complexType/ctF010.xsd",
        instance="msData/complexType/ctF010.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_f007_ct_f007_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent with optional attribute mixed = 'false' and content of
    restriction then content of sequence with elements
    """
    assert_bindings(
        schema="msData/complexType/ctF007.xsd",
        instance="msData/complexType/ctF007.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_f001_ct_f001_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    comlexContent with optional attribute id = 'foo123'
    """
    assert_bindings(
        schema="msData/complexType/ctF001.xsd",
        instance="msData/complexType/ctF001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_e019_ct_e019_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Chameleon case for simpleContent restriction
    """
    assert_bindings(
        schema="msData/complexType/ctE019_a.xsd",
        instance="msData/complexType/ctE019.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_e018_ct_e018_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Chameleon case for simpleContent extension
    """
    assert_bindings(
        schema="msData/complexType/ctE018_a.xsd",
        instance="msData/complexType/ctE018.xml",
        class_name="Doc",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_e017_ct_e017_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of extension with base='xsd:string' and content
    of annotation
    """
    assert_bindings(
        schema="msData/complexType/ctE017.xsd",
        instance="msData/complexType/ctE017.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_e010_ct_e010_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of extension with base='xsd:string' and content
    of two attributes
    """
    assert_bindings(
        schema="msData/complexType/ctE010.xsd",
        instance="msData/complexType/ctE010.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_e008_ct_e008_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of extension with base='xsd:string' and content
    of anyAttribute
    """
    assert_bindings(
        schema="msData/complexType/ctE008.xsd",
        instance="msData/complexType/ctE008.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_e007_ct_e007_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of extension with base='xsd:string' and content
    of attributeGroup
    """
    assert_bindings(
        schema="msData/complexType/ctE007.xsd",
        instance="msData/complexType/ctE007.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_e006_ct_e006_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of extension with base='xsd:string' and content
    of attribute
    """
    assert_bindings(
        schema="msData/complexType/ctE006.xsd",
        instance="msData/complexType/ctE006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_e002_ct_e002_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of extension and base = defined complex type
    whose base is simpleType
    """
    assert_bindings(
        schema="msData/complexType/ctE002.xsd",
        instance="msData/complexType/ctE002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_e001_ct_e001_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of extension and base='xsd:string'
    """
    assert_bindings(
        schema="msData/complexType/ctE001.xsd",
        instance="msData/complexType/ctE001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_d035_ct_d035_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction with base='xsd:string' and
    content of length=5 and attribute
    """
    assert_bindings(
        schema="msData/complexType/ctD035.xsd",
        instance="msData/complexType/ctD035.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_d033_ct_d033_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of anyAttribute
    """
    assert_bindings(
        schema="msData/complexType/ctD033.xsd",
        instance="msData/complexType/ctD033.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_d032_ct_d032_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of two
    attributeGroups
    """
    assert_bindings(
        schema="msData/complexType/ctD032.xsd",
        instance="msData/complexType/ctD032.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_d031_ct_d031_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of attributeGroup
    """
    assert_bindings(
        schema="msData/complexType/ctD031.xsd",
        instance="msData/complexType/ctD031.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_d030_ct_d030_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of two attributes
    """
    assert_bindings(
        schema="msData/complexType/ctD030.xsd",
        instance="msData/complexType/ctD030.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_d029_ct_d029_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of attribute
    """
    assert_bindings(
        schema="msData/complexType/ctD029.xsd",
        instance="msData/complexType/ctD029.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_d028_ct_d028_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of two facets
    """
    assert_bindings(
        schema="msData/complexType/ctD028.xsd",
        instance="msData/complexType/ctD028.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_d027_ct_d027_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of whiteSpace
    """
    assert_bindings(
        schema="msData/complexType/ctD027.xsd",
        instance="msData/complexType/ctD027.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_d026_ct_d026_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of fractionDigits
    """
    assert_bindings(
        schema="msData/complexType/ctD026.xsd",
        instance="msData/complexType/ctD026.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_d025_ct_d025_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of totalDigits
    """
    assert_bindings(
        schema="msData/complexType/ctD025.xsd",
        instance="msData/complexType/ctD025.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_d023_ct_d023_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of pattern
    """
    assert_bindings(
        schema="msData/complexType/ctD023.xsd",
        instance="msData/complexType/ctD023.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_d022_ct_d022_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of minLength
    """
    assert_bindings(
        schema="msData/complexType/ctD022.xsd",
        instance="msData/complexType/ctD022.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_d021_ct_d021_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of minInclusive
    """
    assert_bindings(
        schema="msData/complexType/ctD021.xsd",
        instance="msData/complexType/ctD021.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_d020_ct_d020_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of minExclusive
    """
    assert_bindings(
        schema="msData/complexType/ctD020.xsd",
        instance="msData/complexType/ctD020.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_d019_ct_d019_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of maxLength
    """
    assert_bindings(
        schema="msData/complexType/ctD019.xsd",
        instance="msData/complexType/ctD019.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_d018_ct_d018_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of maxInclusive
    """
    assert_bindings(
        schema="msData/complexType/ctD018.xsd",
        instance="msData/complexType/ctD018.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_d017_ct_d017_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of maxExclusive
    """
    assert_bindings(
        schema="msData/complexType/ctD017.xsd",
        instance="msData/complexType/ctD017.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_d016_ct_d016_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of length
    """
    assert_bindings(
        schema="msData/complexType/ctD016.xsd",
        instance="msData/complexType/ctD016.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_d015_ct_d015_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of enumeration
    """
    assert_bindings(
        schema="msData/complexType/ctD015.xsd",
        instance="msData/complexType/ctD015.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_d012_ct_d012_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of simpleType then
    facet
    """
    assert_bindings(
        schema="msData/complexType/ctD012.xsd",
        instance="msData/complexType/ctD012.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_d010_ct_d010_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of annotation then
    simpleType
    """
    assert_bindings(
        schema="msData/complexType/ctD010.xsd",
        instance="msData/complexType/ctD010.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_d008_ct_d008_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of simpleType
    """
    assert_bindings(
        schema="msData/complexType/ctD008.xsd",
        instance="msData/complexType/ctD008.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_d006_ct_d006_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of annotation
    """
    assert_bindings(
        schema="msData/complexType/ctD006.xsd",
        instance="msData/complexType/ctD006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_d005_ct_d005_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and empty content
    """
    assert_bindings(
        schema="msData/complexType/ctD005.xsd",
        instance="msData/complexType/ctD005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_d002_ct_d002_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and base = defined complex type
    """
    assert_bindings(
        schema="msData/complexType/ctD002.xsd",
        instance="msData/complexType/ctD002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_c012_ct_c012_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent and content of annotation and extension
    """
    assert_bindings(
        schema="msData/complexType/ctC012.xsd",
        instance="msData/complexType/ctC012.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_c008_ct_c008_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent and content of extension
    """
    assert_bindings(
        schema="msData/complexType/ctC008.xsd",
        instance="msData/complexType/ctC008.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_c007_ct_c007_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent and content of annotation and restriction
    """
    assert_bindings(
        schema="msData/complexType/ctC007.xsd",
        instance="msData/complexType/ctC007.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_c006_ct_c006_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    attribute with non-schema namespace
    """
    assert_bindings(
        schema="msData/complexType/ctC006.xsd",
        instance="msData/complexType/ctC006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_c001_ct_c001_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent with optional attribute id = 'foo123'
    """
    assert_bindings(
        schema="msData/complexType/ctC001.xsd",
        instance="msData/complexType/ctC001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b113_ct_b113_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with anyAttribute
    """
    assert_bindings(
        schema="msData/complexType/ctB113.xsd",
        instance="msData/complexType/ctB113.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b111_ct_b111_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with attributeGroup then anyAttribute
    """
    assert_bindings(
        schema="msData/complexType/ctB111.xsd",
        instance="msData/complexType/ctB111.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b110_ct_b110_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with attributeGroup then attributeGroup
    """
    assert_bindings(
        schema="msData/complexType/ctB110.xsd",
        instance="msData/complexType/ctB110.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b109_ct_b109_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with attributeGroup then two attributes
    """
    assert_bindings(
        schema="msData/complexType/ctB109.xsd",
        instance="msData/complexType/ctB109.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b108_ct_b108_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with attributeGroup then attribute
    """
    assert_bindings(
        schema="msData/complexType/ctB108.xsd",
        instance="msData/complexType/ctB108.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b100_ct_b100_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with attributeGroup
    """
    assert_bindings(
        schema="msData/complexType/ctB100.xsd",
        instance="msData/complexType/ctB100.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b098_ct_b098_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with attribute then anyAttribute
    """
    assert_bindings(
        schema="msData/complexType/ctB098.xsd",
        instance="msData/complexType/ctB098.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b097_ct_b097_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with attribute then two attributeGroups
    """
    assert_bindings(
        schema="msData/complexType/ctB097.xsd",
        instance="msData/complexType/ctB097.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b096_ct_b096_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with attribute then attributeGroup
    """
    assert_bindings(
        schema="msData/complexType/ctB096.xsd",
        instance="msData/complexType/ctB096.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b095_ct_b095_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with attribute then attribute
    """
    assert_bindings(
        schema="msData/complexType/ctB095.xsd",
        instance="msData/complexType/ctB095.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b087_ct_b087_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with attribute
    """
    assert_bindings(
        schema="msData/complexType/ctB087.xsd",
        instance="msData/complexType/ctB087.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b085_ct_b085_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with sequence then anyAttribute
    """
    assert_bindings(
        schema="msData/complexType/ctB085.xsd",
        instance="msData/complexType/ctB085.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b084_ct_b084_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with sequence then two attributeGroups
    """
    assert_bindings(
        schema="msData/complexType/ctB084.xsd",
        instance="msData/complexType/ctB084.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b083_ct_b083_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with sequence then attributeGroup
    """
    assert_bindings(
        schema="msData/complexType/ctB083.xsd",
        instance="msData/complexType/ctB083.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b082_ct_b082_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with sequence then two attributes
    """
    assert_bindings(
        schema="msData/complexType/ctB082.xsd",
        instance="msData/complexType/ctB082.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b081_ct_b081_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with sequence then attribute
    """
    assert_bindings(
        schema="msData/complexType/ctB081.xsd",
        instance="msData/complexType/ctB081.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b073_ct_b073_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with sequence
    """
    assert_bindings(
        schema="msData/complexType/ctB073.xsd",
        instance="msData/complexType/ctB073.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b071_ct_b071_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with choice then anyAttribute
    """
    assert_bindings(
        schema="msData/complexType/ctB071.xsd",
        instance="msData/complexType/ctB071.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b070_ct_b070_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with choice then two attributeGroups
    """
    assert_bindings(
        schema="msData/complexType/ctB070.xsd",
        instance="msData/complexType/ctB070.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b069_ct_b069_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with choice then attributeGroup
    """
    assert_bindings(
        schema="msData/complexType/ctB069.xsd",
        instance="msData/complexType/ctB069.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b068_ct_b068_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with choice then two attributes
    """
    assert_bindings(
        schema="msData/complexType/ctB068.xsd",
        instance="msData/complexType/ctB068.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b067_ct_b067_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with choice then attribute
    """
    assert_bindings(
        schema="msData/complexType/ctB067.xsd",
        instance="msData/complexType/ctB067.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b059_ct_b059_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with choice
    """
    assert_bindings(
        schema="msData/complexType/ctB059.xsd",
        instance="msData/complexType/ctB059.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b057_ct_b057_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with all then anyAttribute
    """
    assert_bindings(
        schema="msData/complexType/ctB057.xsd",
        instance="msData/complexType/ctB057.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b056_ct_b056_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with all then two attributeGroups
    """
    assert_bindings(
        schema="msData/complexType/ctB056.xsd",
        instance="msData/complexType/ctB056.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b055_ct_b055_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with all then attributeGroup
    """
    assert_bindings(
        schema="msData/complexType/ctB055.xsd",
        instance="msData/complexType/ctB055.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b054_ct_b054_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with all then two attributes
    """
    assert_bindings(
        schema="msData/complexType/ctB054.xsd",
        instance="msData/complexType/ctB054.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b053_ct_b053_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with all then attribute
    """
    assert_bindings(
        schema="msData/complexType/ctB053.xsd",
        instance="msData/complexType/ctB053.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b045_ct_b045_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with all
    """
    assert_bindings(
        schema="msData/complexType/ctB045.xsd",
        instance="msData/complexType/ctB045.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b043_ct_b043_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with group then anyAttribute
    """
    assert_bindings(
        schema="msData/complexType/ctB043.xsd",
        instance="msData/complexType/ctB043.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b042_ct_b042_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with group then two attributeGroups
    """
    assert_bindings(
        schema="msData/complexType/ctB042.xsd",
        instance="msData/complexType/ctB042.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b041_ct_b041_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with group then attributeGroup
    """
    assert_bindings(
        schema="msData/complexType/ctB041.xsd",
        instance="msData/complexType/ctB041.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b040_ct_b040_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with group then two attributes
    """
    assert_bindings(
        schema="msData/complexType/ctB040.xsd",
        instance="msData/complexType/ctB040.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b039_ct_b039_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with group then attribute
    """
    assert_bindings(
        schema="msData/complexType/ctB039.xsd",
        instance="msData/complexType/ctB039.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b031_ct_b031_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with group
    """
    assert_bindings(
        schema="msData/complexType/ctB031.xsd",
        instance="msData/complexType/ctB031.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b017_ct_b017_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with complexContent
    """
    assert_bindings(
        schema="msData/complexType/ctB017.xsd",
        instance="msData/complexType/ctB017.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b003_ct_b003_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with simpleContent
    """
    assert_bindings(
        schema="msData/complexType/ctB003.xsd",
        instance="msData/complexType/ctB003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_b001_ct_b001_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    of single annotation
    """
    assert_bindings(
        schema="msData/complexType/ctB001.xsd",
        instance="msData/complexType/ctB001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_a049_ct_a049_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    attribute with non-schema namespace
    """
    assert_bindings(
        schema="msData/complexType/ctA049.xsd",
        instance="msData/complexType/ctA049.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_a048_ct_a048_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute name = '_1'
    """
    assert_bindings(
        schema="msData/complexType/ctA048.xsd",
        instance="msData/complexType/ctA048.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_a047_ct_a047_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute name = '_foo'
    """
    assert_bindings(
        schema="msData/complexType/ctA047.xsd",
        instance="msData/complexType/ctA047.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_a045_ct_a045_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute name = 'xmlns'
    """
    assert_bindings(
        schema="msData/complexType/ctA045.xsd",
        instance="msData/complexType/ctA045.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_a041_ct_a041_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute name = 'fooType'
    """
    assert_bindings(
        schema="msData/complexType/ctA041.xsd",
        instance="msData/complexType/ctA041.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_a037_ct_a037_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute mixed = '0'
    """
    assert_bindings(
        schema="msData/complexType/ctA037.xsd",
        instance="msData/complexType/ctA037.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_a035_ct_a035_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute mixed = '1'
    """
    assert_bindings(
        schema="msData/complexType/ctA035.xsd",
        instance="msData/complexType/ctA035.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_a034_ct_a034_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute mixed = 'false'
    """
    assert_bindings(
        schema="msData/complexType/ctA034.xsd",
        instance="msData/complexType/ctA034.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_a033_ct_a033_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute mixed = 'true'
    """
    assert_bindings(
        schema="msData/complexType/ctA033.xsd",
        instance="msData/complexType/ctA033.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_a032_ct_a032_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute id = 'foo123' , name
    attribute='foo123'
    """
    assert_bindings(
        schema="msData/complexType/ctA032.xsd",
        instance="msData/complexType/ctA032.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_a027_ct_a027_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute id = 'foo123'
    """
    assert_bindings(
        schema="msData/complexType/ctA027.xsd",
        instance="msData/complexType/ctA027.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_a026_ct_a026_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute final = ''
    """
    assert_bindings(
        schema="msData/complexType/ctA026.xsd",
        instance="msData/complexType/ctA026.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_a022_ct_a022_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute final = 'extension restriction'
    """
    assert_bindings(
        schema="msData/complexType/ctA022.xsd",
        instance="msData/complexType/ctA022.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_a021_ct_a021_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute final = 'restriction extension'
    """
    assert_bindings(
        schema="msData/complexType/ctA021.xsd",
        instance="msData/complexType/ctA021.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_a020_ct_a020_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute final = 'restriction'
    """
    assert_bindings(
        schema="msData/complexType/ctA020.xsd",
        instance="msData/complexType/ctA020.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_a019_ct_a019_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute final = 'extension'
    """
    assert_bindings(
        schema="msData/complexType/ctA019.xsd",
        instance="msData/complexType/ctA019.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_a018_ct_a018_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute final = '#all'
    """
    assert_bindings(
        schema="msData/complexType/ctA018.xsd",
        instance="msData/complexType/ctA018.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_a017_ct_a017_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute block = ''
    """
    assert_bindings(
        schema="msData/complexType/ctA017.xsd",
        instance="msData/complexType/ctA017.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_a013_ct_a013_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute block = 'extension restriction'
    """
    assert_bindings(
        schema="msData/complexType/ctA013.xsd",
        instance="msData/complexType/ctA013.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_a012_ct_a012_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute block = 'restriction extension'
    """
    assert_bindings(
        schema="msData/complexType/ctA012.xsd",
        instance="msData/complexType/ctA012.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_a011_ct_a011_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute block = 'restriction'
    """
    assert_bindings(
        schema="msData/complexType/ctA011.xsd",
        instance="msData/complexType/ctA011.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_a010_ct_a010_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute block = 'extension'
    """
    assert_bindings(
        schema="msData/complexType/ctA010.xsd",
        instance="msData/complexType/ctA010.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_a009_ct_a009_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute block = '#all'
    """
    assert_bindings(
        schema="msData/complexType/ctA009.xsd",
        instance="msData/complexType/ctA009.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_a005_ct_a005_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute abstract = '0'
    """
    assert_bindings(
        schema="msData/complexType/ctA005.xsd",
        instance="msData/complexType/ctA005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_a003_ct_a003_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute abstract = '1'
    """
    assert_bindings(
        schema="msData/complexType/ctA003.xsd",
        instance="msData/complexType/ctA003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_a002_ct_a002_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute abstract = 'true'
    """
    assert_bindings(
        schema="msData/complexType/ctA002.xsd",
        instance="msData/complexType/ctA002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ct_a001_ct_a001_v(json_360, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute abstract = 'false'
    """
    assert_bindings(
        schema="msData/complexType/ctA001.xsd",
        instance="msData/complexType/ctA001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_dt_z86723_2246_dt_z86723_2246_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : Validation: xsi:type with built-in
    types should not allow content other than text.
    """
    assert_bindings(
        schema="msData/datatypes/test86723.xsd",
        instance="msData/datatypes/test86723.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_dt_z107447_a_2245_dt_z107447_a_2245_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : XSD:whitespace handling for xs:token
    should be collapse(2) TSTF says 'fixed' ID attr in schema is invalid,
    instance testing disabled MHK - becomes valid in 1.1, instance test
    reinstated
    """
    assert_bindings(
        schema="msData/datatypes/test107447_a.xsd",
        instance="msData/datatypes/test107447.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_dt_z107447_1_2244_dt_z107447_1_2244_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : XSD:whitespace handling for xs:token
    should be collapse(1)
    """
    assert_bindings(
        schema="msData/datatypes/test107447.xsd",
        instance="msData/datatypes/test107447_1.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_dt_z107447_2243_dt_z107447_2243_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : XSD:whitespace handling for xs:token
    should be collapse.
    """
    assert_bindings(
        schema="msData/datatypes/test107447.xsd",
        instance="msData/datatypes/test107447.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_dt_z100507_2242_dt_z100507_2242_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : xs:ENTITY is not derived from
    xs:NCName, xs:NOTATION is incorrectly derived from xs:QName
    """
    assert_bindings(
        schema="msData/datatypes/test100507.xsd",
        instance="msData/datatypes/test100507.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_id_test70681_2241_id_test70681_2241_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : ID/IDREF should not allow heading or
    trailing whitespace like NCNAME
    """
    assert_bindings(
        schema="msData/datatypes/datatypes.xsd",
        instance="msData/datatypes/ID_test70681.xml",
        class_name="Data",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_id_test64335_2240_id_test64335_2240_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : ID data type validation
    """
    assert_bindings(
        schema="msData/datatypes/ID_test64335.xsd",
        instance="msData/datatypes/ID_test64335.xml",
        class_name="Products",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_positive_integer005_2239_positive_integer005_2239_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=12345678901234567890123456789
    """
    assert_bindings(
        schema="msData/datatypes/positiveInteger.xsd",
        instance="msData/datatypes/positiveInteger005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_positive_integer004_2238_positive_integer004_2238_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=+1
    """
    assert_bindings(
        schema="msData/datatypes/positiveInteger.xsd",
        instance="msData/datatypes/positiveInteger004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_positive_integer003_2237_positive_integer003_2237_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=0
    """
    assert_bindings(
        schema="msData/datatypes/positiveInteger.xsd",
        instance="msData/datatypes/positiveInteger003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_positive_integer002_2236_positive_integer002_2236_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-1
    """
    assert_bindings(
        schema="msData/datatypes/positiveInteger.xsd",
        instance="msData/datatypes/positiveInteger002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_positive_integer001_2235_positive_integer001_2235_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/positiveInteger.xsd",
        instance="msData/datatypes/positiveInteger001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_unsigned_byte007_2234_unsigned_byte007_2234_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : test for simpleType list of
    unsignedByte
    """
    assert_bindings(
        schema="msData/datatypes/unsignedByte007.xsd",
        instance="msData/datatypes/unsignedByte007.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_unsigned_byte006_2233_unsigned_byte006_2233_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=256
    """
    assert_bindings(
        schema="msData/datatypes/unsignedByte.xsd",
        instance="msData/datatypes/unsignedByte006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_unsigned_byte005_2232_unsigned_byte005_2232_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=255
    """
    assert_bindings(
        schema="msData/datatypes/unsignedByte.xsd",
        instance="msData/datatypes/unsignedByte005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_unsigned_byte004_2231_unsigned_byte004_2231_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1
    """
    assert_bindings(
        schema="msData/datatypes/unsignedByte.xsd",
        instance="msData/datatypes/unsignedByte004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_unsigned_byte003_2230_unsigned_byte003_2230_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=0
    """
    assert_bindings(
        schema="msData/datatypes/unsignedByte.xsd",
        instance="msData/datatypes/unsignedByte003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_unsigned_byte002_2229_unsigned_byte002_2229_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-1
    """
    assert_bindings(
        schema="msData/datatypes/unsignedByte.xsd",
        instance="msData/datatypes/unsignedByte002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_unsigned_byte001_2228_unsigned_byte001_2228_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/unsignedByte.xsd",
        instance="msData/datatypes/unsignedByte001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_unsigned_short007_2227_unsigned_short007_2227_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : test for simpleType list of
    unsignedShort
    """
    assert_bindings(
        schema="msData/datatypes/unsignedShort007.xsd",
        instance="msData/datatypes/unsignedShort007.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_unsigned_short006_2226_unsigned_short006_2226_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=65536
    """
    assert_bindings(
        schema="msData/datatypes/unsignedShort.xsd",
        instance="msData/datatypes/unsignedShort006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_unsigned_short005_2225_unsigned_short005_2225_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=65535
    """
    assert_bindings(
        schema="msData/datatypes/unsignedShort.xsd",
        instance="msData/datatypes/unsignedShort005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_unsigned_short004_2224_unsigned_short004_2224_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1
    """
    assert_bindings(
        schema="msData/datatypes/unsignedShort.xsd",
        instance="msData/datatypes/unsignedShort004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_unsigned_short003_2223_unsigned_short003_2223_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=0
    """
    assert_bindings(
        schema="msData/datatypes/unsignedShort.xsd",
        instance="msData/datatypes/unsignedShort003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_unsigned_short002_2222_unsigned_short002_2222_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-1
    """
    assert_bindings(
        schema="msData/datatypes/unsignedShort.xsd",
        instance="msData/datatypes/unsignedShort002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_unsigned_short001_2221_unsigned_short001_2221_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/unsignedShort.xsd",
        instance="msData/datatypes/unsignedShort001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_unsigned_int007_2220_unsigned_int007_2220_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : test for simpleType list of
    unsignedInt
    """
    assert_bindings(
        schema="msData/datatypes/unsignedInt007.xsd",
        instance="msData/datatypes/unsignedInt007.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_unsigned_int006_2219_unsigned_int006_2219_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=4294967296
    """
    assert_bindings(
        schema="msData/datatypes/unsignedInt.xsd",
        instance="msData/datatypes/unsignedInt006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_unsigned_int005_2218_unsigned_int005_2218_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=4294967295
    """
    assert_bindings(
        schema="msData/datatypes/unsignedInt.xsd",
        instance="msData/datatypes/unsignedInt005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_unsigned_int004_2217_unsigned_int004_2217_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1
    """
    assert_bindings(
        schema="msData/datatypes/unsignedInt.xsd",
        instance="msData/datatypes/unsignedInt004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_unsigned_int003_2216_unsigned_int003_2216_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=0
    """
    assert_bindings(
        schema="msData/datatypes/unsignedInt.xsd",
        instance="msData/datatypes/unsignedInt003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_unsigned_int002_2215_unsigned_int002_2215_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-1
    """
    assert_bindings(
        schema="msData/datatypes/unsignedInt.xsd",
        instance="msData/datatypes/unsignedInt002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_unsigned_int001_2214_unsigned_int001_2214_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/unsignedInt.xsd",
        instance="msData/datatypes/unsignedInt001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_unsigned_long007_2213_unsigned_long007_2213_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : test for simpleType list of
    unsignedLong
    """
    assert_bindings(
        schema="msData/datatypes/unsignedLong007.xsd",
        instance="msData/datatypes/unsignedLong007.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_unsigned_long006_2212_unsigned_long006_2212_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=18446744073709551616
    """
    assert_bindings(
        schema="msData/datatypes/unsignedLong.xsd",
        instance="msData/datatypes/unsignedLong006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_unsigned_long005_2211_unsigned_long005_2211_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=18446744073709551615
    """
    assert_bindings(
        schema="msData/datatypes/unsignedLong.xsd",
        instance="msData/datatypes/unsignedLong005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_unsigned_long004_2210_unsigned_long004_2210_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1
    """
    assert_bindings(
        schema="msData/datatypes/unsignedLong.xsd",
        instance="msData/datatypes/unsignedLong004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_unsigned_long003_2209_unsigned_long003_2209_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=0
    """
    assert_bindings(
        schema="msData/datatypes/unsignedLong.xsd",
        instance="msData/datatypes/unsignedLong003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_unsigned_long002_2208_unsigned_long002_2208_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-1
    """
    assert_bindings(
        schema="msData/datatypes/unsignedLong.xsd",
        instance="msData/datatypes/unsignedLong002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_unsigned_long001_2207_unsigned_long001_2207_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/unsignedLong.xsd",
        instance="msData/datatypes/unsignedLong001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_non_negative_integer005_2206_non_negative_integer005_2206_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=12345678901234567890123456789
    """
    assert_bindings(
        schema="msData/datatypes/nonNegativeInteger.xsd",
        instance="msData/datatypes/nonNegativeInteger005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_non_negative_integer004_2205_non_negative_integer004_2205_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=+1
    """
    assert_bindings(
        schema="msData/datatypes/nonNegativeInteger.xsd",
        instance="msData/datatypes/nonNegativeInteger004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_non_negative_integer003_2204_non_negative_integer003_2204_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=0
    """
    assert_bindings(
        schema="msData/datatypes/nonNegativeInteger.xsd",
        instance="msData/datatypes/nonNegativeInteger003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_non_negative_integer002_2203_non_negative_integer002_2203_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-1
    """
    assert_bindings(
        schema="msData/datatypes/nonNegativeInteger.xsd",
        instance="msData/datatypes/nonNegativeInteger002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_non_negative_integer001_2202_non_negative_integer001_2202_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/nonNegativeInteger.xsd",
        instance="msData/datatypes/nonNegativeInteger001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_byte009_2201_byte009_2201_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : Test simpleType List of byte
    """
    assert_bindings(
        schema="msData/datatypes/byte009.xsd",
        instance="msData/datatypes/byte009.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_byte008_2200_byte008_2200_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-129
    """
    assert_bindings(
        schema="msData/datatypes/byte.xsd",
        instance="msData/datatypes/byte008.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_byte007_2199_byte007_2199_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-128
    """
    assert_bindings(
        schema="msData/datatypes/byte.xsd",
        instance="msData/datatypes/byte007.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_byte006_2198_byte006_2198_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=128
    """
    assert_bindings(
        schema="msData/datatypes/byte.xsd",
        instance="msData/datatypes/byte006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_byte005_2197_byte005_2197_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=127
    """
    assert_bindings(
        schema="msData/datatypes/byte.xsd",
        instance="msData/datatypes/byte005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_byte004_2196_byte004_2196_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=+1
    """
    assert_bindings(
        schema="msData/datatypes/byte.xsd",
        instance="msData/datatypes/byte004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_byte003_2195_byte003_2195_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=0
    """
    assert_bindings(
        schema="msData/datatypes/byte.xsd",
        instance="msData/datatypes/byte003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_byte002_2194_byte002_2194_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-1
    """
    assert_bindings(
        schema="msData/datatypes/byte.xsd",
        instance="msData/datatypes/byte002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_byte001_2193_byte001_2193_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/byte.xsd",
        instance="msData/datatypes/byte001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_short009_2192_short009_2192_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : test for simpleType list of short
    """
    assert_bindings(
        schema="msData/datatypes/short009.xsd",
        instance="msData/datatypes/short009.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_short008_2191_short008_2191_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-32769
    """
    assert_bindings(
        schema="msData/datatypes/short.xsd",
        instance="msData/datatypes/short008.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_short007_2190_short007_2190_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-32768
    """
    assert_bindings(
        schema="msData/datatypes/short.xsd",
        instance="msData/datatypes/short007.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_short006_2189_short006_2189_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=32768
    """
    assert_bindings(
        schema="msData/datatypes/short.xsd",
        instance="msData/datatypes/short006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_short005_2188_short005_2188_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=32767
    """
    assert_bindings(
        schema="msData/datatypes/short.xsd",
        instance="msData/datatypes/short005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_short004_2187_short004_2187_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=+1
    """
    assert_bindings(
        schema="msData/datatypes/short.xsd",
        instance="msData/datatypes/short004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_short003_2186_short003_2186_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=0
    """
    assert_bindings(
        schema="msData/datatypes/short.xsd",
        instance="msData/datatypes/short003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_short002_2185_short002_2185_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-1
    """
    assert_bindings(
        schema="msData/datatypes/short.xsd",
        instance="msData/datatypes/short002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_short001_2184_short001_2184_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/short.xsd",
        instance="msData/datatypes/short001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_int008_2183_int008_2183_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-2147483649
    """
    assert_bindings(
        schema="msData/datatypes/int.xsd",
        instance="msData/datatypes/int008.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_int007_2182_int007_2182_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-2147483648
    """
    assert_bindings(
        schema="msData/datatypes/int.xsd",
        instance="msData/datatypes/int007.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_int006_2181_int006_2181_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=2147483648
    """
    assert_bindings(
        schema="msData/datatypes/int.xsd",
        instance="msData/datatypes/int006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_int005_2180_int005_2180_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=2147483647
    """
    assert_bindings(
        schema="msData/datatypes/int.xsd",
        instance="msData/datatypes/int005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_int004_2179_int004_2179_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=+1
    """
    assert_bindings(
        schema="msData/datatypes/int.xsd",
        instance="msData/datatypes/int004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_int003_2178_int003_2178_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=0
    """
    assert_bindings(
        schema="msData/datatypes/int.xsd",
        instance="msData/datatypes/int003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_int002_2177_int002_2177_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-1
    """
    assert_bindings(
        schema="msData/datatypes/int.xsd",
        instance="msData/datatypes/int002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_int001_2176_int001_2176_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/int.xsd",
        instance="msData/datatypes/int001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_long009_2175_long009_2175_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : Test for simpleType list of Long
    """
    assert_bindings(
        schema="msData/datatypes/long009.xsd",
        instance="msData/datatypes/long009.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_long008_2174_long008_2174_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=9223372036854775808
    """
    assert_bindings(
        schema="msData/datatypes/long.xsd",
        instance="msData/datatypes/long008.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_long007_2173_long007_2173_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=9223372036854775807
    """
    assert_bindings(
        schema="msData/datatypes/long.xsd",
        instance="msData/datatypes/long007.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_long006_2172_long006_2172_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-9223372036854775809
    """
    assert_bindings(
        schema="msData/datatypes/long.xsd",
        instance="msData/datatypes/long006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_long005_2171_long005_2171_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-9223372036854775808
    """
    assert_bindings(
        schema="msData/datatypes/long.xsd",
        instance="msData/datatypes/long005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_long004_2170_long004_2170_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=+1
    """
    assert_bindings(
        schema="msData/datatypes/long.xsd",
        instance="msData/datatypes/long004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_long003_2169_long003_2169_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=0
    """
    assert_bindings(
        schema="msData/datatypes/long.xsd",
        instance="msData/datatypes/long003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_long002_2168_long002_2168_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-1
    """
    assert_bindings(
        schema="msData/datatypes/long.xsd",
        instance="msData/datatypes/long002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_long001_2167_long001_2167_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/long.xsd",
        instance="msData/datatypes/long001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_negative_integer005_2166_negative_integer005_2166_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-12345678901234567890123456789
    """
    assert_bindings(
        schema="msData/datatypes/negativeInteger.xsd",
        instance="msData/datatypes/negativeInteger005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_negative_integer004_2165_negative_integer004_2165_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1
    """
    assert_bindings(
        schema="msData/datatypes/negativeInteger.xsd",
        instance="msData/datatypes/negativeInteger004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_negative_integer003_2164_negative_integer003_2164_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=0
    """
    assert_bindings(
        schema="msData/datatypes/negativeInteger.xsd",
        instance="msData/datatypes/negativeInteger003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_negative_integer002_2163_negative_integer002_2163_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-1
    """
    assert_bindings(
        schema="msData/datatypes/negativeInteger.xsd",
        instance="msData/datatypes/negativeInteger002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_negative_integer001_2162_negative_integer001_2162_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/negativeInteger.xsd",
        instance="msData/datatypes/negativeInteger001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_non_positive_integer005_2161_non_positive_integer005_2161_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-12345678901234567890123456789
    """
    assert_bindings(
        schema="msData/datatypes/nonPositiveInteger.xsd",
        instance="msData/datatypes/nonPositiveInteger005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_non_positive_integer004_2160_non_positive_integer004_2160_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1
    """
    assert_bindings(
        schema="msData/datatypes/nonPositiveInteger.xsd",
        instance="msData/datatypes/nonPositiveInteger004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_non_positive_integer003_2159_non_positive_integer003_2159_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=0
    """
    assert_bindings(
        schema="msData/datatypes/nonPositiveInteger.xsd",
        instance="msData/datatypes/nonPositiveInteger003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_non_positive_integer002_2158_non_positive_integer002_2158_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-1
    """
    assert_bindings(
        schema="msData/datatypes/nonPositiveInteger.xsd",
        instance="msData/datatypes/nonPositiveInteger002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_non_positive_integer001_2157_non_positive_integer001_2157_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/nonPositiveInteger.xsd",
        instance="msData/datatypes/nonPositiveInteger001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_integer016_2156_integer016_2156_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=ABCDEF
    """
    assert_bindings(
        schema="msData/datatypes/integer.xsd",
        instance="msData/datatypes/integer016.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_integer015_2155_integer015_2155_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=NaN
    """
    assert_bindings(
        schema="msData/datatypes/integer.xsd",
        instance="msData/datatypes/integer015.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_integer014_2154_integer014_2154_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-INF
    """
    assert_bindings(
        schema="msData/datatypes/integer.xsd",
        instance="msData/datatypes/integer014.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_integer013_2153_integer013_2153_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=INF
    """
    assert_bindings(
        schema="msData/datatypes/integer.xsd",
        instance="msData/datatypes/integer013.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_integer012_2152_integer012_2152_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-1E4
    """
    assert_bindings(
        schema="msData/datatypes/integer.xsd",
        instance="msData/datatypes/integer012.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_integer011_2151_integer011_2151_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=12345678901234567890123456789
    """
    assert_bindings(
        schema="msData/datatypes/integer.xsd",
        instance="msData/datatypes/integer011.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_integer010_2150_integer010_2150_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=10000000
    """
    assert_bindings(
        schema="msData/datatypes/integer.xsd",
        instance="msData/datatypes/integer010.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_integer009_2149_integer009_2149_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=12678967543233
    """
    assert_bindings(
        schema="msData/datatypes/integer.xsd",
        instance="msData/datatypes/integer009.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_integer008_2148_integer008_2148_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1
    """
    assert_bindings(
        schema="msData/datatypes/integer.xsd",
        instance="msData/datatypes/integer008.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_integer007_2147_integer007_2147_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-1
    """
    assert_bindings(
        schema="msData/datatypes/integer.xsd",
        instance="msData/datatypes/integer007.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_integer006_2146_integer006_2146_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=+0.0
    """
    assert_bindings(
        schema="msData/datatypes/integer.xsd",
        instance="msData/datatypes/integer006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_integer005_2145_integer005_2145_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-0
    """
    assert_bindings(
        schema="msData/datatypes/integer.xsd",
        instance="msData/datatypes/integer005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_integer004_2144_integer004_2144_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=+0
    """
    assert_bindings(
        schema="msData/datatypes/integer.xsd",
        instance="msData/datatypes/integer004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_integer003_2143_integer003_2143_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=3.14159
    """
    assert_bindings(
        schema="msData/datatypes/integer.xsd",
        instance="msData/datatypes/integer003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_integer002_2142_integer002_2142_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-3.14159
    """
    assert_bindings(
        schema="msData/datatypes/integer.xsd",
        instance="msData/datatypes/integer002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_integer001_2141_integer001_2141_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/integer.xsd",
        instance="msData/datatypes/integer001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ncname011_2140_ncname011_2140_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=//foo
    """
    assert_bindings(
        schema="msData/datatypes/NCName.xsd",
        instance="msData/datatypes/NCName011.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ncname010_2139_ncname010_2139_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=@test
    """
    assert_bindings(
        schema="msData/datatypes/NCName.xsd",
        instance="msData/datatypes/NCName010.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ncname009_2138_ncname009_2138_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=:foo
    """
    assert_bindings(
        schema="msData/datatypes/NCName.xsd",
        instance="msData/datatypes/NCName009.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ncname008_2137_ncname008_2137_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=fo:foo
    """
    assert_bindings(
        schema="msData/datatypes/NCName.xsd",
        instance="msData/datatypes/NCName008.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ncname007_2136_ncname007_2136_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=fo_124-.sda3
    """
    assert_bindings(
        schema="msData/datatypes/NCName.xsd",
        instance="msData/datatypes/NCName007.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ncname006_2135_ncname006_2135_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-foo
    """
    assert_bindings(
        schema="msData/datatypes/NCName.xsd",
        instance="msData/datatypes/NCName006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ncname005_2134_ncname005_2134_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=.foo
    """
    assert_bindings(
        schema="msData/datatypes/NCName.xsd",
        instance="msData/datatypes/NCName005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ncname004_2133_ncname004_2133_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1fo
    """
    assert_bindings(
        schema="msData/datatypes/NCName.xsd",
        instance="msData/datatypes/NCName004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ncname003_2132_ncname003_2132_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=fo124
    """
    assert_bindings(
        schema="msData/datatypes/NCName.xsd",
        instance="msData/datatypes/NCName003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_ncname002_2131_ncname002_2131_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=_foo
    """
    assert_bindings(
        schema="msData/datatypes/NCName.xsd",
        instance="msData/datatypes/NCName002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_ncname001_2130_ncname001_2130_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/NCName.xsd",
        instance="msData/datatypes/NCName001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_name018_2129_name018_2129_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=//foo
    """
    assert_bindings(
        schema="msData/datatypes/Name.xsd",
        instance="msData/datatypes/Name018.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_name017_2128_name017_2128_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=@test
    """
    assert_bindings(
        schema="msData/datatypes/Name.xsd",
        instance="msData/datatypes/Name017.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_name016_2127_name016_2127_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=fo:fo_124-.s:da3
    """
    assert_bindings(
        schema="msData/datatypes/Name.xsd",
        instance="msData/datatypes/Name016.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_name015_2126_name015_2126_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=fo:fo_124-.sda3
    """
    assert_bindings(
        schema="msData/datatypes/Name.xsd",
        instance="msData/datatypes/Name015.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_name014_2125_name014_2125_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=fo:'-foo
    """
    assert_bindings(
        schema="msData/datatypes/Name.xsd",
        instance="msData/datatypes/Name014.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_name013_2124_name013_2124_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=fo:.foo
    """
    assert_bindings(
        schema="msData/datatypes/Name.xsd",
        instance="msData/datatypes/Name013.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_name012_2123_name012_2123_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=fo:1fo
    """
    assert_bindings(
        schema="msData/datatypes/Name.xsd",
        instance="msData/datatypes/Name012.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_name011_2122_name011_2122_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=fo:fo124
    """
    assert_bindings(
        schema="msData/datatypes/Name.xsd",
        instance="msData/datatypes/Name011.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_name010_2121_name010_2121_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=fo:_foo
    """
    assert_bindings(
        schema="msData/datatypes/Name.xsd",
        instance="msData/datatypes/Name010.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_name009_2120_name009_2120_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=:foo
    """
    assert_bindings(
        schema="msData/datatypes/Name.xsd",
        instance="msData/datatypes/Name009.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_name008_2119_name008_2119_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=fo:foo
    """
    assert_bindings(
        schema="msData/datatypes/Name.xsd",
        instance="msData/datatypes/Name008.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_name007_2118_name007_2118_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=fo_124-.sda3
    """
    assert_bindings(
        schema="msData/datatypes/Name.xsd",
        instance="msData/datatypes/Name007.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_name006_2117_name006_2117_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-foo
    """
    assert_bindings(
        schema="msData/datatypes/Name.xsd",
        instance="msData/datatypes/Name006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_name005_2116_name005_2116_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=.foo
    """
    assert_bindings(
        schema="msData/datatypes/Name.xsd",
        instance="msData/datatypes/Name005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_name004_2115_name004_2115_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1fo
    """
    assert_bindings(
        schema="msData/datatypes/Name.xsd",
        instance="msData/datatypes/Name004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_name003_2114_name003_2114_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=fo124
    """
    assert_bindings(
        schema="msData/datatypes/Name.xsd",
        instance="msData/datatypes/Name003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_name002_2113_name002_2113_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=_foo
    """
    assert_bindings(
        schema="msData/datatypes/Name.xsd",
        instance="msData/datatypes/Name002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_name001_2112_name001_2112_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/Name.xsd",
        instance="msData/datatypes/Name001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_language010_2111_language010_2111_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : xsd:language doesn't quite follow the
    spec syntax
    """
    assert_bindings(
        schema="msData/datatypes/language.xsd",
        instance="msData/datatypes/language010.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_language009_2110_language009_2110_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=X-2o
    """
    assert_bindings(
        schema="msData/datatypes/language.xsd",
        instance="msData/datatypes/language009.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_language008_2109_language008_2109_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1ko
    """
    assert_bindings(
        schema="msData/datatypes/language.xsd",
        instance="msData/datatypes/language008.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_language007_2108_language007_2108_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=I-en-us
    """
    assert_bindings(
        schema="msData/datatypes/language.xsd",
        instance="msData/datatypes/language007.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_language006_2107_language006_2107_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=spanish
    """
    assert_bindings(
        schema="msData/datatypes/language.xsd",
        instance="msData/datatypes/language006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_language005_2106_language005_2106_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=en
    """
    assert_bindings(
        schema="msData/datatypes/language.xsd",
        instance="msData/datatypes/language005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_language004_2105_language004_2105_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=en-us
    """
    assert_bindings(
        schema="msData/datatypes/language.xsd",
        instance="msData/datatypes/language004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_language003_2104_language003_2104_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=EN-US
    """
    assert_bindings(
        schema="msData/datatypes/language.xsd",
        instance="msData/datatypes/language003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_language002_2103_language002_2103_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=EN
    """
    assert_bindings(
        schema="msData/datatypes/language.xsd",
        instance="msData/datatypes/language002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_language001_2102_language001_2102_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/language.xsd",
        instance="msData/datatypes/language001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_token004_2101_token004_2101_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=a b
    """
    assert_bindings(
        schema="msData/datatypes/token.xsd",
        instance="msData/datatypes/token004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_token003_2100_token003_2100_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=a b
    """
    assert_bindings(
        schema="msData/datatypes/token.xsd",
        instance="msData/datatypes/token003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_token002_2099_token002_2099_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=a b
    """
    assert_bindings(
        schema="msData/datatypes/token.xsd",
        instance="msData/datatypes/token002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_token001_2098_token001_2098_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/token.xsd",
        instance="msData/datatypes/token001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_normalized_string003_2097_normalized_string003_2097_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=test line
    """
    assert_bindings(
        schema="msData/datatypes/normalizedString.xsd",
        instance="msData/datatypes/normalizedString003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_normalized_string002_2096_normalized_string002_2096_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=test line
    """
    assert_bindings(
        schema="msData/datatypes/normalizedString.xsd",
        instance="msData/datatypes/normalizedString002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_normalized_string001_2095_normalized_string001_2095_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/normalizedString.xsd",
        instance="msData/datatypes/normalizedString001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_qname011_2094_qname011_2094_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=//foo
    """
    assert_bindings(
        schema="msData/datatypes/QName.xsd",
        instance="msData/datatypes/QName011.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_qname010_2093_qname010_2093_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=@test
    """
    assert_bindings(
        schema="msData/datatypes/QName.xsd",
        instance="msData/datatypes/QName010.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_qname009_2092_qname009_2092_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=xmlns:xsi WG decided on
    2010-02-05 telcon that there is no binding for xmlns as a prefix, so
    these are not valid QNames.
    """
    assert_bindings(
        schema="msData/datatypes/QName.xsd",
        instance="msData/datatypes/QName009.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_qname008_2091_qname008_2091_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=fo:1fo
    """
    assert_bindings(
        schema="msData/datatypes/QName.xsd",
        instance="msData/datatypes/QName008.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_qname007_2090_qname007_2090_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=:foo
    """
    assert_bindings(
        schema="msData/datatypes/QName.xsd",
        instance="msData/datatypes/QName007.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_qname006_2089_qname006_2089_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=fo:foo
    """
    assert_bindings(
        schema="msData/datatypes/QName.xsd",
        instance="msData/datatypes/QName006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_qname005_2088_qname005_2088_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-foo
    """
    assert_bindings(
        schema="msData/datatypes/QName.xsd",
        instance="msData/datatypes/QName005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_qname004_2087_qname004_2087_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1fo
    """
    assert_bindings(
        schema="msData/datatypes/QName.xsd",
        instance="msData/datatypes/QName004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_qname003_2086_qname003_2086_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=fo124
    """
    assert_bindings(
        schema="msData/datatypes/QName.xsd",
        instance="msData/datatypes/QName003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_qname002_2085_qname002_2085_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=_foo
    """
    assert_bindings(
        schema="msData/datatypes/QName.xsd",
        instance="msData/datatypes/QName002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_qname001_2084_qname001_2084_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/QName.xsd",
        instance="msData/datatypes/QName001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_any_uri011_2083_any_uri011_2083_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : test for simpleType list of anyURI
    """
    assert_bindings(
        schema="msData/datatypes/anyURI011.xsd",
        instance="msData/datatypes/anyURI011.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_any_uri010_2082_any_uri010_2082_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=C:/TestSuites/XSD%20Spec/CR-
    xmlschema-2-20001024.htm#dc-minInclusive
    """
    assert_bindings(
        schema="msData/datatypes/anyURI.xsd",
        instance="msData/datatypes/anyURI010.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_any_uri009_2081_any_uri009_2081_v(json_360, save_output):
    """
    TEST :Facet Schemas for string :
    value=file:///C:/TestSuites/XSD%20Spec/CR-xmlschema-2-20001024.htm#dc-
    minInclusive
    """
    assert_bindings(
        schema="msData/datatypes/anyURI.xsd",
        instance="msData/datatypes/anyURI009.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_any_uri008_2080_any_uri008_2080_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=telnet://melvyl.ucop.edu/
    """
    assert_bindings(
        schema="msData/datatypes/anyURI.xsd",
        instance="msData/datatypes/anyURI008.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_any_uri007_2079_any_uri007_2079_v(json_360, save_output):
    """
    TEST :Facet Schemas for string :
    value=news:comp.infosystems.www.servers.unix
    """
    assert_bindings(
        schema="msData/datatypes/anyURI.xsd",
        instance="msData/datatypes/anyURI007.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_any_uri006_2078_any_uri006_2078_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=gopher://spinaltap.micro.umn.ed
    u/00/Weather/California/Los%20Angeles
    """
    assert_bindings(
        schema="msData/datatypes/anyURI.xsd",
        instance="msData/datatypes/anyURI006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_any_uri005_2077_any_uri005_2077_v(json_360, save_output):
    """
    TEST :Facet Schemas for string :
    value=ftp://ftp.is.co.za/rfc/rfc1808.txt
    """
    assert_bindings(
        schema="msData/datatypes/anyURI.xsd",
        instance="msData/datatypes/anyURI005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_any_uri004_2076_any_uri004_2076_v(json_360, save_output):
    """
    TEST :Facet Schemas for string :
    value=http://www.w3.org/XML/Group/xmlschema-
    current/datatypes/datatypes.html#uriReference
    """
    assert_bindings(
        schema="msData/datatypes/anyURI.xsd",
        instance="msData/datatypes/anyURI004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_any_uri003_2075_any_uri003_2075_v(json_360, save_output):
    """
    TEST :Facet Schemas for string :
    value=http://www.w3.org/1999/XMLSchema
    """
    assert_bindings(
        schema="msData/datatypes/anyURI.xsd",
        instance="msData/datatypes/anyURI003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_any_uri002_2074_any_uri002_2074_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=mailto:davebrow@microsoft.com
    """
    assert_bindings(
        schema="msData/datatypes/anyURI.xsd",
        instance="msData/datatypes/anyURI002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_any_uri001_2073_any_uri001_2073_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/anyURI.xsd",
        instance="msData/datatypes/anyURI001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_base64_binary002_2072_base64_binary002_2072_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : test for simpleType list of
    base64Binary
    """
    assert_bindings(
        schema="msData/datatypes/base64Binary002.xsd",
        instance="msData/datatypes/base64Binary002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_base64_binary001_2071_base64_binary001_2071_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/base64Binary.xsd",
        instance="msData/datatypes/base64Binary001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_hex_binary004_2070_hex_binary004_2070_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : Test for HexBinary value with
    whitespace
    """
    assert_bindings(
        schema="msData/datatypes/hexBinary.xsd",
        instance="msData/datatypes/hexBinary004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_hex_binary003_2069_hex_binary003_2069_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : Test for HexBinary value with
    whitespace TSTF ruled that spec. disallows space in hexBinary
    """
    assert_bindings(
        schema="msData/datatypes/hexBinary.xsd",
        instance="msData/datatypes/hexBinary003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_hex_binary002_2068_hex_binary002_2068_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : test for simpleType List of hexBinary
    """
    assert_bindings(
        schema="msData/datatypes/hexBinary002.xsd",
        instance="msData/datatypes/hexBinary002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_hex_binary001_2067_hex_binary001_2067_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/hexBinary.xsd",
        instance="msData/datatypes/hexBinary001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_g_month007_2066_g_month007_2066_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=- -15- -
    """
    assert_bindings(
        schema="msData/datatypes/gMonth.xsd",
        instance="msData/datatypes/gMonth007.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_g_month006_2065_g_month006_2065_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=- -3- -
    """
    assert_bindings(
        schema="msData/datatypes/gMonth.xsd",
        instance="msData/datatypes/gMonth006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_g_month005_2064_g_month005_2064_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1999-05-10
    """
    assert_bindings(
        schema="msData/datatypes/gMonth.xsd",
        instance="msData/datatypes/gMonth005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_g_month004_2063_g_month004_2063_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=- -05- - -05:00
    """
    assert_bindings(
        schema="msData/datatypes/gMonth.xsd",
        instance="msData/datatypes/gMonth004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_g_month003_2062_g_month003_2062_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1999-05- -
    """
    assert_bindings(
        schema="msData/datatypes/gMonth.xsd",
        instance="msData/datatypes/gMonth003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_g_month002_2061_g_month002_2061_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=- -03- -
    """
    assert_bindings(
        schema="msData/datatypes/gMonth.xsd",
        instance="msData/datatypes/gMonth002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_g_month001_2060_g_month001_2060_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/gMonth.xsd",
        instance="msData/datatypes/gMonth001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_g_day005_2059_g_day005_2059_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/gDay.xsd",
        instance="msData/datatypes/gDay005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_g_day004_2058_g_day004_2058_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=- -15
    """
    assert_bindings(
        schema="msData/datatypes/gDay.xsd",
        instance="msData/datatypes/gDay004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_g_day003_2057_g_day003_2057_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=- - -15-05:00
    """
    assert_bindings(
        schema="msData/datatypes/gDay.xsd",
        instance="msData/datatypes/gDay003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_g_day002_2056_g_day002_2056_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=- - -29
    """
    assert_bindings(
        schema="msData/datatypes/gDay.xsd",
        instance="msData/datatypes/gDay002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_g_day001_2055_g_day001_2055_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=- - -15
    """
    assert_bindings(
        schema="msData/datatypes/gDay.xsd",
        instance="msData/datatypes/gDay001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_g_month_day006_2054_g_month_day006_2054_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : gMonthDay should disallow "--02-30"
    and "--02-31"
    """
    assert_bindings(
        schema="msData/datatypes/datatypes.xsd",
        instance="msData/datatypes/gMonthDay006.xml",
        class_name="Data",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_g_month_day005_2053_g_month_day005_2053_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=- - -03-15
    """
    assert_bindings(
        schema="msData/datatypes/gMonthDay.xsd",
        instance="msData/datatypes/gMonthDay005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_g_month_day004_2052_g_month_day004_2052_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=- -02-29
    """
    assert_bindings(
        schema="msData/datatypes/gMonthDay.xsd",
        instance="msData/datatypes/gMonthDay004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_g_month_day003_2051_g_month_day003_2051_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=- -03-15-05:00
    """
    assert_bindings(
        schema="msData/datatypes/gMonthDay.xsd",
        instance="msData/datatypes/gMonthDay003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_g_month_day002_2050_g_month_day002_2050_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=- -03-15
    """
    assert_bindings(
        schema="msData/datatypes/gMonthDay.xsd",
        instance="msData/datatypes/gMonthDay002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_g_month_day001_2049_g_month_day001_2049_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/gMonthDay.xsd",
        instance="msData/datatypes/gMonthDay001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_g_year006_2048_g_year006_2048_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1999-05:00
    """
    assert_bindings(
        schema="msData/datatypes/gYear.xsd",
        instance="msData/datatypes/gYear006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_g_year005_2047_g_year005_2047_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=2000-00
    """
    assert_bindings(
        schema="msData/datatypes/gYear.xsd",
        instance="msData/datatypes/gYear005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_g_year002_2046_g_year002_2046_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=2000
    """
    assert_bindings(
        schema="msData/datatypes/gYear.xsd",
        instance="msData/datatypes/gYear002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_g_year001_2045_g_year001_2045_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/gYear.xsd",
        instance="msData/datatypes/gYear001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_g_year_month006_2044_g_year_month006_2044_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=99-10
    """
    assert_bindings(
        schema="msData/datatypes/gYearMonth.xsd",
        instance="msData/datatypes/gYearMonth006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_g_year_month004_2043_g_year_month004_2043_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1999-15
    """
    assert_bindings(
        schema="msData/datatypes/gYearMonth.xsd",
        instance="msData/datatypes/gYearMonth004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_g_year_month003_2042_g_year_month003_2042_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1999-10-05:00
    """
    assert_bindings(
        schema="msData/datatypes/gYearMonth.xsd",
        instance="msData/datatypes/gYearMonth003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_g_year_month002_2041_g_year_month002_2041_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1999-10
    """
    assert_bindings(
        schema="msData/datatypes/gYearMonth.xsd",
        instance="msData/datatypes/gYearMonth002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_g_year_month001_2040_g_year_month001_2040_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/gYearMonth.xsd",
        instance="msData/datatypes/gYearMonth001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_date011_2039_date011_2039_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=123456
    """
    assert_bindings(
        schema="msData/datatypes/date.xsd",
        instance="msData/datatypes/date011.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_date010_2038_date010_2038_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=2000-10-05-05:00
    """
    assert_bindings(
        schema="msData/datatypes/date.xsd",
        instance="msData/datatypes/date010.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_date009_2037_date009_2037_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=2000-13-14
    """
    assert_bindings(
        schema="msData/datatypes/date.xsd",
        instance="msData/datatypes/date009.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_date006_2036_date006_2036_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=01-01-01
    """
    assert_bindings(
        schema="msData/datatypes/date.xsd",
        instance="msData/datatypes/date006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_date005_2035_date005_2035_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=2000-02-29
    """
    assert_bindings(
        schema="msData/datatypes/date.xsd",
        instance="msData/datatypes/date005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_date004_2034_date004_2034_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1999-02-29
    """
    assert_bindings(
        schema="msData/datatypes/date.xsd",
        instance="msData/datatypes/date004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_date003_2033_date003_2033_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1999-05-32
    """
    assert_bindings(
        schema="msData/datatypes/date.xsd",
        instance="msData/datatypes/date003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_date002_2032_date002_2032_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1999-05-31
    """
    assert_bindings(
        schema="msData/datatypes/date.xsd",
        instance="msData/datatypes/date002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_date001_2031_date001_2031_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/date.xsd",
        instance="msData/datatypes/date001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_time022_2030_time022_2030_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=+13:20:00
    """
    assert_bindings(
        schema="msData/datatypes/time.xsd",
        instance="msData/datatypes/time022.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_time021_2029_time021_2029_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-13:20:00
    """
    assert_bindings(
        schema="msData/datatypes/time.xsd",
        instance="msData/datatypes/time021.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_time020_2028_time020_2028_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=0:0:00
    """
    assert_bindings(
        schema="msData/datatypes/time.xsd",
        instance="msData/datatypes/time020.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_time019_2027_time019_2027_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=0:20:00
    """
    assert_bindings(
        schema="msData/datatypes/time.xsd",
        instance="msData/datatypes/time019.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_time018_2026_time018_2026_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=25:20:00
    """
    assert_bindings(
        schema="msData/datatypes/time.xsd",
        instance="msData/datatypes/time018.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_time017_2025_time017_2025_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=13:60:00
    """
    assert_bindings(
        schema="msData/datatypes/time.xsd",
        instance="msData/datatypes/time017.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_time016_2024_time016_2024_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=13:20:60
    """
    assert_bindings(
        schema="msData/datatypes/time.xsd",
        instance="msData/datatypes/time016.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_time015_2023_time015_2023_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=13.4:20:00
    """
    assert_bindings(
        schema="msData/datatypes/time.xsd",
        instance="msData/datatypes/time015.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_time014_2022_time014_2022_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=13:20.4:00
    """
    assert_bindings(
        schema="msData/datatypes/time.xsd",
        instance="msData/datatypes/time014.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_time013_2021_time013_2021_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=13:20:00.34
    """
    assert_bindings(
        schema="msData/datatypes/time.xsd",
        instance="msData/datatypes/time013.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_time012_2020_time012_2020_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=13:20:00
    """
    assert_bindings(
        schema="msData/datatypes/time.xsd",
        instance="msData/datatypes/time012.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_time011_2019_time011_2019_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=13:20:00Z
    """
    assert_bindings(
        schema="msData/datatypes/time.xsd",
        instance="msData/datatypes/time011.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_time009_2018_time009_2018_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=13:20:00+05:59
    """
    assert_bindings(
        schema="msData/datatypes/time.xsd",
        instance="msData/datatypes/time009.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_time008_2017_time008_2017_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=13:20:00-05:59
    """
    assert_bindings(
        schema="msData/datatypes/time.xsd",
        instance="msData/datatypes/time008.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_time007_2016_time007_2016_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=13:20:00+05:00
    """
    assert_bindings(
        schema="msData/datatypes/time.xsd",
        instance="msData/datatypes/time007.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_time006_2015_time006_2015_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=13:20:00-05:00
    """
    assert_bindings(
        schema="msData/datatypes/time.xsd",
        instance="msData/datatypes/time006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_time005_2014_time005_2014_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=13:20:00+05:00
    """
    assert_bindings(
        schema="msData/datatypes/time.xsd",
        instance="msData/datatypes/time005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_time004_2013_time004_2013_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=13:20:00-05:00
    """
    assert_bindings(
        schema="msData/datatypes/time.xsd",
        instance="msData/datatypes/time004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_time003_2012_time003_2012_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1985-04-12T10:30
    """
    assert_bindings(
        schema="msData/datatypes/time.xsd",
        instance="msData/datatypes/time003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_time002_2011_time002_2011_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1999-05-31T13:20:00-05:00
    """
    assert_bindings(
        schema="msData/datatypes/time.xsd",
        instance="msData/datatypes/time002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_time001_2010_time001_2010_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/time.xsd",
        instance="msData/datatypes/time001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_date_time013_2009_date_time013_2009_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : should we allow '+'(plus sign)
    preceding datetime/date?
    """
    assert_bindings(
        schema="msData/datatypes/datatypes.xsd",
        instance="msData/datatypes/dateTime013.xml",
        class_name="Data",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_date_time011_2008_date_time011_2008_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=0000-01-01T00:00:00 Year zero
    is allowed in dates in XSD 1.1 - MHK
    """
    assert_bindings(
        schema="msData/datatypes/dateTime.xsd",
        instance="msData/datatypes/dateTime011.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_date_time010_2007_date_time010_2007_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1999-05-31T13:20:00Z
    """
    assert_bindings(
        schema="msData/datatypes/dateTime.xsd",
        instance="msData/datatypes/dateTime010.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_date_time008_2006_date_time008_2006_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1999-05-31T13:20:00-5:45
    """
    assert_bindings(
        schema="msData/datatypes/dateTime.xsd",
        instance="msData/datatypes/dateTime008.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_date_time007_2005_date_time007_2005_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1999-05-31T13:20:00+5:45
    """
    assert_bindings(
        schema="msData/datatypes/dateTime.xsd",
        instance="msData/datatypes/dateTime007.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_date_time006_2004_date_time006_2004_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1999-05-31T13:20:00+05:00
    """
    assert_bindings(
        schema="msData/datatypes/dateTime.xsd",
        instance="msData/datatypes/dateTime006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_date_time005_2003_date_time005_2003_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1999-05-31T13:20:00-05:00
    """
    assert_bindings(
        schema="msData/datatypes/dateTime.xsd",
        instance="msData/datatypes/dateTime005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_date_time004_2002_date_time004_2002_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1985-102T23:50:30
    """
    assert_bindings(
        schema="msData/datatypes/dateTime.xsd",
        instance="msData/datatypes/dateTime004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_date_time003_2001_date_time003_2001_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1985-04-12T10:30:00
    """
    assert_bindings(
        schema="msData/datatypes/dateTime.xsd",
        instance="msData/datatypes/dateTime003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_date_time002_2000_date_time002_2000_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1999-05-31T13:20:00-05:00
    """
    assert_bindings(
        schema="msData/datatypes/dateTime.xsd",
        instance="msData/datatypes/dateTime002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_date_time001_1999_date_time001_1999_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/dateTime.xsd",
        instance="msData/datatypes/dateTime001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_duration030_1998_duration030_1998_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : For duration, the number and its
    corresponding designator better be pair
    """
    assert_bindings(
        schema="msData/datatypes/datatypes.xsd",
        instance="msData/datatypes/duration030.xml",
        class_name="Data",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_duration029_1997_duration029_1997_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : For duration, the designator 'T'
    shall be absent if all of the time items are absent
    """
    assert_bindings(
        schema="msData/datatypes/datatypes.xsd",
        instance="msData/datatypes/duration029.xml",
        class_name="Data",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_duration028_1996_duration028_1996_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : string 'P' for duration should raise
    error
    """
    assert_bindings(
        schema="msData/datatypes/datatypes.xsd",
        instance="msData/datatypes/duration028.xml",
        class_name="Data",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_duration027_1995_duration027_1995_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : Test for simpleType of duration
    """
    assert_bindings(
        schema="msData/datatypes/duration027.xsd",
        instance="msData/datatypes/duration027.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_duration026_1994_duration026_1994_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=P2000Y2M29DT10H30M
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration026.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_duration025_1993_duration025_1993_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=P1Y2M15DT11H60M
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration025.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_duration024_1992_duration024_1992_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=P1Y2M15DT25H30M
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration024.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_duration023_1991_duration023_1991_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=P1Y2M32DT12H30M
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration023.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_duration022_1990_duration022_1990_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=P1Y13M15DT12H30M
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration022.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_duration021_1989_duration021_1989_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=P0Y0M0DT0H-0M0.0001S
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration021.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_duration020_1988_duration020_1988_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=P0Y0M0DT0H0M0.0001S
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration020.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_duration019_1987_duration019_1987_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=P0Y0M0D
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration019.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_duration018_1986_duration018_1986_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=PT31S
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration018.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_duration017_1985_duration017_1985_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=PT31M
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration017.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_duration016_1984_duration016_1984_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=PT31H
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration016.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_duration015_1983_duration015_1983_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=T312H
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration015.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_duration014_1982_duration014_1982_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=P0Y0M3D
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration014.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_duration013_1981_duration013_1981_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1234Y
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration013.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_duration012_1980_duration012_1980_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=PT2153.5S
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration012.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_duration011_1979_duration011_1979_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=P200.5Y
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration011.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_duration010_1978_duration010_1978_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=P1Y2MT
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration010.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_duration009_1977_duration009_1977_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-P1347M
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration009.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_duration008_1976_duration008_1976_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=P-1347M
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration008.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_duration007_1975_duration007_1975_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=P0Y1347M0D
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration007.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_duration006_1974_duration006_1974_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=P0Y1347M
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_duration005_1973_duration005_1973_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=P1Y2MT2H
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_duration004_1972_duration004_1972_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=P1347M
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_duration003_1971_duration003_1971_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=P1347Y
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_duration002_1970_duration002_1970_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=P1Y2M3DT10H30M
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_duration001_1969_duration001_1969_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_double030_1968_double030_1968_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : all valid double values
    """
    assert_bindings(
        schema="msData/datatypes/double030.xsd",
        instance="msData/datatypes/double030.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_double029_1967_double029_1967_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=ABCDEF
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double029.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_double028_1966_double028_1966_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=2.22e-308
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double028.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_double027_1965_double027_1965_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=8.98e307
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double027.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_double026_1964_double026_1964_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=NAN
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double026.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_double025_1963_double025_1963_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=nan
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double025.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_double024_1962_double024_1962_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=inf
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double024.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_double023_1961_double023_1961_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-NaN
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double023.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_double022_1960_double022_1960_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=+NaN
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double022.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_double021_1959_double021_1959_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=NaN
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double021.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_double020_1958_double020_1958_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-INF
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double020.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_double019_1957_double019_1957_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=INF
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double019.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_double018_1956_double018_1956_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=+INF Becomes valid in XSD 1.1 -
    MHK
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double018.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_double017_1955_double017_1955_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-1E4
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double017.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_double016_1954_double016_1954_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=E
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double016.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_double015_1953_double015_1953_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=e
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double015.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_double014_1952_double014_1952_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=+1
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double014.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_double013_1951_double013_1951_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double013.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_double012_1950_double012_1950_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-1
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double012.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_double011_1949_double011_1949_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-1.0
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double011.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_double010_1948_double010_1948_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-0.0
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double010.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_double009_1947_double009_1947_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=+0.0
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double009.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_double008_1946_double008_1946_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-0
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double008.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_double007_1945_double007_1945_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=+0
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double007.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_double006_1944_double006_1944_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=3.14159
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_double005_1943_double005_1943_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-3.14159
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_double004_1942_double004_1942_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1e2
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_double003_1941_double003_1941_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1E2
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_double002_1940_double002_1940_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1.0
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_double001_1939_double001_1939_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_float039_1938_float039_1938_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : all valid float values
    """
    assert_bindings(
        schema="msData/datatypes/float039.xsd",
        instance="msData/datatypes/float039.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_float038_1937_float038_1937_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : Test for simpleType of float
    """
    assert_bindings(
        schema="msData/datatypes/float038.xsd",
        instance="msData/datatypes/float038.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_float037_1936_float037_1936_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=ABCDEF
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float037.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_float036_1935_float036_1935_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=13.1513.561
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float036.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_float035_1934_float035_1934_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-1E4.4
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float035.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_float034_1933_float034_1933_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=00.00
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float034.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_float033_1932_float033_1932_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=021.22
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float033.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_float032_1931_float032_1931_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=00.121
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float032.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_float031_1930_float031_1930_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=3.4e38
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float031.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_float030_1929_float030_1929_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=2.3e-38
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float030.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_float029_1928_float029_1928_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=12.78E-2
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float029.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_float028_1927_float028_1927_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1267.43233E12
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float028.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_float027_1926_float027_1926_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1267.432x10
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float027.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_float026_1925_float026_1925_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=NAN
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float026.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_float025_1924_float025_1924_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=nan
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float025.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_float024_1923_float024_1923_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=inf
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float024.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_float023_1922_float023_1922_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-NaN
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float023.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_float022_1921_float022_1921_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=+NaN
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float022.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_float021_1920_float021_1920_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=NaN
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float021.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_float020_1919_float020_1919_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-INF
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float020.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_float019_1918_float019_1918_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=INF
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float019.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_float018_1917_float018_1917_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=+INF Becomes valid in XSD 1.1 -
    MHK
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float018.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_float017_1916_float017_1916_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-1E4
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float017.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_float016_1915_float016_1915_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=E
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float016.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_float015_1914_float015_1914_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=e
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float015.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_float014_1913_float014_1913_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=+1
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float014.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_float013_1912_float013_1912_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float013.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_float012_1911_float012_1911_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-1
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float012.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_float011_1910_float011_1910_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-1.0
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float011.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_float010_1909_float010_1909_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-0.0
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float010.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_float009_1908_float009_1908_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=+0.0
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float009.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_float008_1907_float008_1907_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-0
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float008.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_float007_1906_float007_1906_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=+0
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float007.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_float006_1905_float006_1905_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=3.14159
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_float005_1904_float005_1904_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-3.14159
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_float004_1903_float004_1903_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1e2
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_float003_1902_float003_1902_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1E2
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_float002_1901_float002_1901_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1.0
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_float001_1900_float001_1900_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_decimal025_1899_decimal025_1899_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=123.456E4
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal025.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_decimal024_1898_decimal024_1898_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=ABCDEF
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal024.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_decimal023_1897_decimal023_1897_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=13.1513.561
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal023.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_decimal022_1896_decimal022_1896_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=NaN
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal022.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_decimal021_1895_decimal021_1895_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-INF
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal021.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_decimal020_1894_decimal020_1894_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=INF
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal020.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_decimal019_1893_decimal019_1893_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-1E4
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal019.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_decimal018_1892_decimal018_1892_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=E
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal018.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_decimal017_1891_decimal017_1891_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=e
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal017.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_decimal016_1890_decimal016_1890_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=12345678901234567890123456789
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal016.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_decimal015_1889_decimal015_1889_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=9876543210987654321098765432
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal015.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_decimal014_1888_decimal014_1888_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=987654321098765432
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal014.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_decimal013_1887_decimal013_1887_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=100000.00
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal013.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_decimal012_1886_decimal012_1886_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=12678967.543233
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal012.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_decimal011_1885_decimal011_1885_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=+1
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal011.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_decimal010_1884_decimal010_1884_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal010.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_decimal009_1883_decimal009_1883_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-1
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal009.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_decimal008_1882_decimal008_1882_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-1.0
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal008.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_decimal007_1881_decimal007_1881_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-0.0
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal007.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_decimal006_1880_decimal006_1880_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=+0.0
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_decimal005_1879_decimal005_1879_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-0
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_decimal004_1878_decimal004_1878_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=+0
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_decimal003_1877_decimal003_1877_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=3.14159
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_decimal002_1876_decimal002_1876_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-3.14159
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_decimal001_1875_decimal001_1875_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_boolean018_1874_boolean018_1874_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : Test simpleType list with boolean
    """
    assert_bindings(
        schema="msData/datatypes/boolean018.xsd",
        instance="msData/datatypes/boolean018.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_boolean017_1873_boolean017_1873_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=F
    """
    assert_bindings(
        schema="msData/datatypes/boolean.xsd",
        instance="msData/datatypes/boolean017.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_boolean016_1872_boolean016_1872_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=T
    """
    assert_bindings(
        schema="msData/datatypes/boolean.xsd",
        instance="msData/datatypes/boolean016.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_boolean015_1871_boolean015_1871_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=f
    """
    assert_bindings(
        schema="msData/datatypes/boolean.xsd",
        instance="msData/datatypes/boolean015.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_boolean014_1870_boolean014_1870_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=t
    """
    assert_bindings(
        schema="msData/datatypes/boolean.xsd",
        instance="msData/datatypes/boolean014.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_boolean013_1869_boolean013_1869_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=FALSE
    """
    assert_bindings(
        schema="msData/datatypes/boolean.xsd",
        instance="msData/datatypes/boolean013.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_boolean012_1868_boolean012_1868_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=TRUE
    """
    assert_bindings(
        schema="msData/datatypes/boolean.xsd",
        instance="msData/datatypes/boolean012.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_boolean011_1867_boolean011_1867_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=True
    """
    assert_bindings(
        schema="msData/datatypes/boolean.xsd",
        instance="msData/datatypes/boolean011.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_boolean010_1866_boolean010_1866_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=False
    """
    assert_bindings(
        schema="msData/datatypes/boolean.xsd",
        instance="msData/datatypes/boolean010.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_boolean009_1865_boolean009_1865_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=+0
    """
    assert_bindings(
        schema="msData/datatypes/boolean.xsd",
        instance="msData/datatypes/boolean009.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_boolean008_1864_boolean008_1864_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-0
    """
    assert_bindings(
        schema="msData/datatypes/boolean.xsd",
        instance="msData/datatypes/boolean008.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_boolean007_1863_boolean007_1863_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=-1
    """
    assert_bindings(
        schema="msData/datatypes/boolean.xsd",
        instance="msData/datatypes/boolean007.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_boolean006_1862_boolean006_1862_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=+1
    """
    assert_bindings(
        schema="msData/datatypes/boolean.xsd",
        instance="msData/datatypes/boolean006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_boolean005_1861_boolean005_1861_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=0
    """
    assert_bindings(
        schema="msData/datatypes/boolean.xsd",
        instance="msData/datatypes/boolean005.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_boolean004_1860_boolean004_1860_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=false
    """
    assert_bindings(
        schema="msData/datatypes/boolean.xsd",
        instance="msData/datatypes/boolean004.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_boolean003_1859_boolean003_1859_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=1
    """
    assert_bindings(
        schema="msData/datatypes/boolean.xsd",
        instance="msData/datatypes/boolean003.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_boolean002_1858_boolean002_1858_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=true
    """
    assert_bindings(
        schema="msData/datatypes/boolean.xsd",
        instance="msData/datatypes/boolean002.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


@pytest.mark.skip(reason="Invalid instance")
def test_boolean001_1857_boolean001_1857_i(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/boolean.xsd",
        instance="msData/datatypes/boolean001.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )


def test_string006_1856_string006_1856_v(json_360, save_output):
    """
    TEST :Facet Schemas for string : value=BaseChar ::= [#x0041-#x005A] |
    [#x0061-#x007A] | [#x00C0-#x00D6] | [#x00D8-#x00F6] | [#x00F8-#x00FF]
    | [#x0100-#x0131] | [#x0134-#x013E] | [#x0141-#x0148] |
    [#x014A-#x017E] | [#x0180-#x01C3] | [#x01CD-#x01F0] | [#x01F4-#x01F5]
    | [#x01FA-#x0217] | [#x0250-#x02A8] | [#x02BB-#x02C1] | #x0386 |
    [#x0388-#x038A] | #x038C | [#x038E-#x03A1] | [#x03A3-#x03CE] |
    [#x03D0-#x03D6] | #x03DA | #x03DC | #x03DE | #x03E0 | [#x03E2-#x03F3]
    | [#x0401-#x040C] | [#x040E-#x044F] | [#x0451-#x045C] |
    [#x045E-#x0481] | [#x0490-#x04C4] | [#x04C7-#x04C8] | [#x04CB-#x04CC]
    | [#x04D0-#x04EB] | [#x04EE-#x04F5] | [#x04F8-#x04F9] |
    [#x0531-#x0556] | #x0559 | [#x0561-#x0586] | [#x05D0-#x05EA] |
    [#x05F0-#x05F2] | [#x0621-#x063A] | [#x0641-#x064A] | [#x0671-#x06B7]
    | [#x06BA-#x06BE] | [#x06C0-#x06CE] | [#x06D0-#x06D3] | #x06D5 |
    [#x06E5-#x06E6] | [#x0905-#x0939] | #x093D | [#x0958-#x0961] |
    [#x0985-#x098C] | [#x098F-#x0990] | [#x0993-#x09A8] | [#x09AA-#x09B0]
    | #x09B2 | [#x09B6-#x09B9] | [#x09DC-#x09DD] | [#x09DF-#x09E1] |
    [#x09F0-#x09F1
    """
    assert_bindings(
        schema="msData/datatypes/string.xsd",
        instance="msData/datatypes/string006.xml",
        class_name="Root",
        version="1.1",
        json_360=json_360,
        save_output=save_output,
    )
