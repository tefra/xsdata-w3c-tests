import pytest

from tests.utils import assert_bindings


def test_member_type024_member_type024_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Attribute of union of user defined
    typees(mybool,myint,mystring) with default value
    """
    assert_bindings(
        schema="msData/additional/memberType024.xsd",
        instance="msData/additional/memberType024.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_member_type023_member_type023_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Attribute of union of user defined
    typees(mybool,myint,mystring)
    """
    assert_bindings(
        schema="msData/additional/memberType023.xsd",
        instance="msData/additional/memberType023.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_member_type022_member_type022_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Element of union of user defined
    typees(mybool,myint,mystring) with default value
    """
    assert_bindings(
        schema="msData/additional/memberType022.xsd",
        instance="msData/additional/memberType022.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_member_type021_member_type021_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Element of union of user defined
    typees(mybool,myint,mystring)
    """
    assert_bindings(
        schema="msData/additional/memberType021.xsd",
        instance="msData/additional/memberType021.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_member_type008_member_type008_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Element with default value and xsi:type: membertype
    of union(bool,int,string)
    """
    assert_bindings(
        schema="msData/additional/memberType003.xsd",
        instance="msData/additional/memberType008.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_member_type007_member_type007_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Element with xsi:type: membertype of
    union(bool,int,string)
    """
    assert_bindings(
        schema="msData/additional/memberType001.xsd",
        instance="msData/additional/memberType007.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_member_type006_member_type006_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Element with xsi:type: membertype of
    union(bool,int,string)
    """
    assert_bindings(
        schema="msData/additional/memberType001.xsd",
        instance="msData/additional/memberType006.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_member_type005_member_type005_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Attribute with default value: membertype of
    union(bool,int,string)
    """
    assert_bindings(
        schema="msData/additional/memberType004.xsd",
        instance="msData/additional/memberType005.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_member_type004_member_type004_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Element with default value: membertype of
    union(bool,int,string)
    """
    assert_bindings(
        schema="msData/additional/memberType003.xsd",
        instance="msData/additional/memberType004.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_member_type003_member_type003_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Attribute: membertype of union(bool,int,string)
    """
    assert_bindings(
        schema="msData/additional/memberType002.xsd",
        instance="msData/additional/memberType003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_member_type002_member_type002_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Element: membertype of union(bool,int,string)
    """
    assert_bindings(
        schema="msData/additional/memberType001.xsd",
        instance="msData/additional/memberType002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_member_type001_member_type001_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Element : membertype of union(bool,int,string)
    """
    assert_bindings(
        schema="msData/additional/memberType001.xsd",
        instance="msData/additional/memberType001.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default079_is_default079_v(mode, save_output):
    """
    TEST :Adhoc XSD: : multiple 'fixed' constraints
    """
    assert_bindings(
        schema="msData/additional/isdefault079.xsd",
        instance="msData/additional/isdefault079.xml",
        class_name="Regvaluemodopset",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default078_is_default078_v(mode, save_output):
    """
    TEST :Adhoc XSD: : map xml namespace in the instance to be able to
    insert default attributes from xml namespace
    """
    assert_bindings(
        schema="msData/additional/isdefault078.xsd",
        instance="msData/additional/isdefault078.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default076_is_default076_v(mode, save_output):
    """
    TEST :Adhoc XSD: : fixed value on mixed content
    """
    assert_bindings(
        schema="msData/additional/isdefault076.xsd",
        instance="msData/additional/isdefault075.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default075_is_default075_v(mode, save_output):
    """
    TEST :Adhoc XSD: : default value on mixed content
    """
    assert_bindings(
        schema="msData/additional/isdefault075.xsd",
        instance="msData/additional/isdefault075.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default074_is_default074_v(mode, save_output):
    """
    TEST :Adhoc XSD: : attribute of type xs:anySimpleType with a default
    and fixed value
    """
    assert_bindings(
        schema="msData/additional/isdefault074.xsd",
        instance="msData/additional/isdefault074.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default073_is_default073_v(mode, save_output):
    """
    TEST :Adhoc XSD: : element of type xs:anyType with a default and fixed
    value
    """
    assert_bindings(
        schema="msData/additional/isdefault073.xsd",
        instance="msData/additional/isdefault073.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default072_is_default072_v(mode, save_output):
    """
    TEST :Adhoc XSD: : While adding default attributes with
    form="qualified", should lookup all prefixes for its namespace
    """
    assert_bindings(
        schema="msData/additional/isdefault072.xsd",
        instance="msData/additional/isdefault072.xml",
        class_name="Array",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default071_is_default071_v(mode, save_output):
    """
    TEST :Adhoc XSD: : element of type xs:anyType with value not matching
    the fixed value in the schema should error(valid)
    """
    assert_bindings(
        schema="msData/additional/isdefault070.xsd",
        instance="msData/additional/isdefault071.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default060_1_is_default060_1_v(mode, save_output):
    """
    TEST :Adhoc XSD: : test empty element typed as xsd:int with default
    value set in schema.
    """
    assert_bindings(
        schema="msData/additional/test95960_1.xsd",
        instance="msData/additional/test95960_1.xml",
        class_name="Employees",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default068_is_default068_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Attributes: IsDefault(fixed) Local Element with no
    attributes, schema HAS targetNamespace
    """
    assert_bindings(
        schema="msData/additional/isdefault062.xsd",
        instance="msData/additional/isdefault068.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default067_is_default067_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Attributes: IsDefault(fixed) Local Element with all
    attributes, schema HAS targetNamespace
    """
    assert_bindings(
        schema="msData/additional/isdefault062.xsd",
        instance="msData/additional/isdefault067.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default066_is_default066_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Attributes: IsDefault(fixed) no attributes on root
    element (empty element WITH end tag), schema HAS targetNamespace
    """
    assert_bindings(
        schema="msData/additional/isdefault061.xsd",
        instance="msData/additional/isdefault066.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default065_is_default065_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Attributes: IsDefault(fixed) No attributes on root
    element(empty element no end tag), schema HAS targetNamespace
    """
    assert_bindings(
        schema="msData/additional/isdefault061.xsd",
        instance="msData/additional/isdefault065.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default061_is_default061_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Attributes: IsDefault(fixed) attributes on root
    element, schema HAS targetNamespace
    """
    assert_bindings(
        schema="msData/additional/isdefault061.xsd",
        instance="msData/additional/isdefault061.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default058_is_default058_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Attributes: IsDefault(fixed) Local Element with no
    attributes, schema has no targetNamespace
    """
    assert_bindings(
        schema="msData/additional/isdefault052.xsd",
        instance="msData/additional/isdefault058.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default057_is_default057_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Attributes: IsDefault(fixed) Local Element with all
    attributes, schema has no targetNamespace
    """
    assert_bindings(
        schema="msData/additional/isdefault052.xsd",
        instance="msData/additional/isdefault057.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default056_is_default056_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Attributes: IsDefault(fixed) no attributes on root
    element (empty element WITH end tag), schema has no targetNamespace
    """
    assert_bindings(
        schema="msData/additional/isdefault051.xsd",
        instance="msData/additional/isdefault056.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default055_is_default055_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Attributes: IsDefault(fixed) No attributes on root
    element(empty element no end tag), schema has no targetNamespace
    """
    assert_bindings(
        schema="msData/additional/isdefault051.xsd",
        instance="msData/additional/isdefault055.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default051_is_default051_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Attributes: IsDefault(fixed) attributes on root
    element, schema has no targetNamespace
    """
    assert_bindings(
        schema="msData/additional/isdefault051.xsd",
        instance="msData/additional/isdefault051.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default028_is_default028_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(default) a sequence with elements
    with invalid values
    """
    assert_bindings(
        schema="msData/additional/isdefault004.xsd",
        instance="msData/additional/isdefault028.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default027_is_default027_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(default) a sequence with elements
    with fixed values present
    """
    assert_bindings(
        schema="msData/additional/isdefault004.xsd",
        instance="msData/additional/isdefault027.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default026_is_default026_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(default) a sequence with elements
    with start and end tags
    """
    assert_bindings(
        schema="msData/additional/isdefault004.xsd",
        instance="msData/additional/isdefault026.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default025_is_default025_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(default) a sequence with elements
    with no end tags
    """
    assert_bindings(
        schema="msData/additional/isdefault004.xsd",
        instance="msData/additional/isdefault025.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default024_is_default024_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(default) for Element with invalid
    value
    """
    assert_bindings(
        schema="msData/additional/isdefault003.xsd",
        instance="msData/additional/isdefault024.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default023_is_default023_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(default) for Empty Element with
    fixed value already present
    """
    assert_bindings(
        schema="msData/additional/isdefault003.xsd",
        instance="msData/additional/isdefault023.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default022_is_default022_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(default) for Empty Element with
    start and end tag
    """
    assert_bindings(
        schema="msData/additional/isdefault003.xsd",
        instance="msData/additional/isdefault022.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default021_is_default021_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(default) for Empty Element with no
    end tag
    """
    assert_bindings(
        schema="msData/additional/isdefault003.xsd",
        instance="msData/additional/isdefault021.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default007_is_default007_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(fixed) a sequence with elements
    with fixed values present
    """
    assert_bindings(
        schema="msData/additional/isdefault002.xsd",
        instance="msData/additional/isdefault007.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default006_is_default006_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(fixed) a sequence with elements
    with start and end tags
    """
    assert_bindings(
        schema="msData/additional/isdefault002.xsd",
        instance="msData/additional/isdefault006.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default005_is_default005_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(fixed) a sequence with elements
    with no end tags
    """
    assert_bindings(
        schema="msData/additional/isdefault002.xsd",
        instance="msData/additional/isdefault005.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default003_is_default003_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(fixed) for Empty Element with fixed
    value already present
    """
    assert_bindings(
        schema="msData/additional/isdefault001.xsd",
        instance="msData/additional/isdefault003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default002_is_default002_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(fixed) for Empty Element with start
    and end tag
    """
    assert_bindings(
        schema="msData/additional/isdefault001.xsd",
        instance="msData/additional/isdefault002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_is_default001_is_default001_v(mode, save_output):
    """
    TEST :Adhoc XSD: : Check IsDefault(fixed) for Empty Element with no
    end tag
    """
    assert_bindings(
        schema="msData/additional/isdefault001.xsd",
        instance="msData/additional/isdefault001.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_d004a_add_d004a_v(mode, save_output):
    """
    TEST :Adhoc XSD: : SAMPLE: xsd 1.0 Sturcture spec : the ipo.xsd with a
    simplify version of ipo.xml with the xsi:type
    """
    assert_bindings(
        schema="msData/additional/ipo.xsd",
        instance="msData/additional/ipo.xml",
        class_name="PurchaseOrder",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_d004_add_d004_v(mode, save_output):
    """
    TEST :Adhoc XSD: : SAMPLE: xsd 1.0 Sturcture spec : the ipo.xsd with a
    simplify version of ipo.xml without the xsi:type
    """
    assert_bindings(
        schema="msData/additional/ipo_s1.xsd",
        instance="msData/additional/ipo_s1.xml",
        class_name="PurchaseOrder",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_d002_add_d002_v(mode, save_output):
    """
    TEST :Adhoc XSD: : xsd 1.0 Prima: the po.xml and po.xsd declared as
    targetNamespace 'foo'
    """
    assert_bindings(
        schema="msData/additional/po.xsd",
        instance="msData/additional/po.xml",
        class_name="PurchaseOrder",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_d001_add_d001_v(mode, save_output):
    """
    TEST :Adhoc XSD: : xsd 1.0 Prima: the po.xml and po.xsd without
    targetNamespace
    """
    assert_bindings(
        schema="msData/additional/po1.xsd",
        instance="msData/additional/po1.xml",
        class_name="PurchaseOrder",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b198d_add_b198d_v(mode, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test with minLength
    facet(2)
    """
    assert_bindings(
        schema="msData/additional/minLength.xsd",
        instance="msData/additional/minLength2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b198c_add_b198c_v(mode, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test with minLength
    facet(1)
    """
    assert_bindings(
        schema="msData/additional/minLength.xsd",
        instance="msData/additional/minLength1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b197c_add_b197c_v(mode, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test with enumeration
    value(3)
    """
    assert_bindings(
        schema="msData/additional/enum1.xsd",
        instance="msData/additional/enum1c.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b197a_add_b197a_v(mode, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test with enumeration
    value(1)
    """
    assert_bindings(
        schema="msData/additional/enum1.xsd",
        instance="msData/additional/enum1a.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b196h_add_b196h_v(mode, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test with fixed
    value(8)
    """
    assert_bindings(
        schema="msData/additional/fixed2.xsd",
        instance="msData/additional/fixed1d.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b196f_add_b196f_v(mode, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test with fixed
    value(6)
    """
    assert_bindings(
        schema="msData/additional/fixed2.xsd",
        instance="msData/additional/fixed1b.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b196c_add_b196c_v(mode, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test with fixed
    value(3)
    """
    assert_bindings(
        schema="msData/additional/fixed1.xsd",
        instance="msData/additional/fixed1c.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b196a_add_b196a_v(mode, save_output):
    """
    TEST :Adhoc XSD: : zero width unicode characeter test with fixed
    value(1)
    """
    assert_bindings(
        schema="msData/additional/fixed1.xsd",
        instance="msData/additional/fixed1a.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b187_add_b187_v(mode, save_output):
    """
    TEST :Adhoc XSD: : XSD: Support user specified schema for
    http://www.w3.org/XML/1998/namespace namespace
    """
    assert_bindings(
        schema="msData/additional/test264908_1.xsd",
        instance="msData/additional/test264908_1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b182_add_b182_v(mode, save_output):
    """
    TEST :Adhoc XSD: : id="schemaLocation for schema whose targetNamespace
    is the XSD namespace"
    """
    assert_bindings(
        schema="msData/additional/test111871.xsd",
        instance="msData/additional/test111871.xml",
        class_name="Title",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b176_add_b176_v(mode, save_output):
    """
    TEST :Adhoc XSD: : id="102850" description="valid but ambigous schema"
    """
    assert_bindings(
        schema="msData/additional/test102850_1.xsd",
        instance="msData/additional/test102850_1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b174_add_b174_v(mode, save_output):
    """
    TEST :Adhoc XSD: : id="102433" description="Validation of xml
    instances should be namespace strict"
    """
    assert_bindings(
        schema="msData/additional/test102433.xsd",
        instance="msData/additional/test102433_5.xml",
        class_name="Bar",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b169_1_add_b169_1_v(mode, save_output):
    """
    TEST :Adhoc XSD: : id="243307" description="test valid document with
    inline schema"
    """
    assert_bindings(
        schema="msData/additional/test93490_16.xsd",
        instance="msData/additional/test93490_16.xml",
        class_name="MapInfo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b148_add_b148_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b145_add_b145_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b140_add_b140_v(mode, save_output):
    """
    TEST :Adhoc XSD: : id="78000" description="any and
    processContents='skip'"
    """
    assert_bindings(
        schema="msData/additional/test78000a.xsd",
        instance="msData/additional/test78000.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b136_add_b136_v(mode, save_output):
    """
    TEST :Adhoc XSD: : id="84188" description="XSD: Attribute with
    use=prohibited and wildcard"
    """
    assert_bindings(
        schema="msData/additional/test84188.xsd",
        instance="msData/additional/test84188.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b135_add_b135_v(mode, save_output):
    """
    TEST :Adhoc XSD: : id="81662" description="xsd: test element matching
    global declaration via xsd:any."
    """
    assert_bindings(
        schema="msData/additional/test81662.xsd",
        instance="msData/additional/test81662.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b132_add_b132_v(mode, save_output):
    """
    TEST :Adhoc XSD: : id="66745" description="xsd validation:xsd
    substitutionGroup "
    """
    assert_bindings(
        schema="msData/additional/test66745_a.xsd",
        instance="msData/additional/test66745.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="single-package",
    )


def test_add_b131_add_b131_v(mode, save_output):
    """
    TEST :Adhoc XSD: : id="76423" description="test validation of keys
    when default namespace is '' and more than one key is defined"
    """
    assert_bindings(
        schema="msData/additional/test76423.xsd",
        instance="msData/additional/test76423.xml",
        class_name="Jsml",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b130_add_b130_v(mode, save_output):
    """
    TEST :Adhoc XSD: : id="78162" description="attribute on xsd:any
    processContents=skip"
    """
    assert_bindings(
        schema="msData/additional/test78126.xsd",
        instance="msData/additional/test78126.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b129_add_b129_v(mode, save_output):
    """
    TEST :Adhoc XSD: : id="74834" description="validate xml data when it
    has a decimal digit of .0"
    """
    assert_bindings(
        schema="msData/additional/test74834.xsd",
        instance="msData/additional/test74834.xml",
        class_name="Datafile",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b125_add_b125_v(mode, save_output):
    """
    TEST :Adhoc XSD: : id="78898" description="xsd: wildcard: content type
    with namespace=##any and processContent=skip"
    """
    assert_bindings(
        schema="msData/additional/test78898.xsd",
        instance="msData/additional/test78898.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b122_add_b122_v(mode, save_output):
    """
    TEST :Adhoc XSD: : id="78910" description="xsd: wildcard: content type
    with namespace=##any and processContent=skip"
    """
    assert_bindings(
        schema="msData/additional/addB122.xsd",
        instance="msData/additional/addB122.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b116_add_b116_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b104_add_b104_v(mode, save_output):
    """
    TEST :Adhoc XSD: : test attribute normalization of fixed value of an
    attribute value
    """
    assert_bindings(
        schema="msData/additional/addB104.xsd",
        instance="msData/additional/addB104.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b096_add_b096_v(mode, save_output):
    """
    TEST :Adhoc XSD: : id="61053" description="xsd: test 'group' reference
    is used, and content model is explicitly declared using 'sequence'."
    """
    assert_bindings(
        schema="msData/additional/addB096.xsd",
        instance="msData/additional/addB096.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b090_add_b090_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b088_add_b088_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b084_add_b084_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b076_add_b076_v(mode, save_output):
    """
    TEST :Adhoc XSD: : id="75028"
    """
    assert_bindings(
        schema="msData/additional/addB076.xsd",
        instance="msData/additional/addB076.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b068_add_b068_i(mode, save_output):
    """
    TEST :Adhoc XSD: : id="73986" description="xsd: length of QName" TSTF
    ruled that 1.0 says all QNames satisfy all length-related tests
    """
    assert_bindings(
        schema="msData/additional/test73986.xsd",
        instance="msData/additional/test73986_2.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b067_add_b067_v(mode, save_output):
    """
    TEST :Adhoc XSD: : id="73986" description="xsd: length of QName"
    """
    assert_bindings(
        schema="msData/additional/test73986.xsd",
        instance="msData/additional/test73986.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b059_add_b059_v(mode, save_output):
    r"""
    TEST :Adhoc XSD: : id="73666" description="xsd: Regular Expression:
    test pattern '(\n|\s)+b' and value ' b'"
    """
    assert_bindings(
        schema="msData/additional/test73666.xsd",
        instance="msData/additional/test73666.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b058_add_b058_v(mode, save_output):
    r"""
    TEST :Adhoc XSD: : id="73665" description="xsd: Regular Expression:
    test checking for '\C' non-character correctly, test with value='?'"
    """
    assert_bindings(
        schema="msData/additional/test73665.xsd",
        instance="msData/additional/test73665.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b056_add_b056_v(mode, save_output):
    r"""
    TEST :Adhoc XSD: : id="73715" description="xsd: Regular Expression:
    preprocess pattern '\\c' should match '\c'"
    """
    assert_bindings(
        schema="msData/additional/test73715.xsd",
        instance="msData/additional/test73715v.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b054_add_b054_v(mode, save_output):
    """
    TEST :Adhoc XSD: : id="70948" description="xsd:invalid facets on
    simpleContent restriction with simpleType child should work"
    """
    assert_bindings(
        schema="msData/additional/test70948.xsd",
        instance="msData/additional/test70948.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b047_add_b047_v(mode, save_output):
    """
    TEST :Adhoc XSD: : id="72597" description="xsd: valid xml and xsd"
    """
    assert_bindings(
        schema="msData/additional/test72597.xsd",
        instance="msData/additional/test72597.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b046_add_b046_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b040_add_b040_v(mode, save_output):
    """
    TEST :Adhoc XSD: : id="72049" description="xsd: schemaLocation with
    more than one pair of namespace+schemalocation "
    """
    assert_bindings(
        schema="msData/additional/test72049_a.xsd",
        instance="msData/additional/test72049.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b034_add_b034_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b31_add_b31_v(mode, save_output):
    """
    TEST :Adhoc XSD: : another test
    """
    assert_bindings(
        schema="msData/additional/test69277.xsd",
        instance="msData/additional/test69277.xml",
        class_name="Elt1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b028_add_b028_v(mode, save_output):
    """
    TEST :Adhoc XSD: : XSD: xsi:type when derived from xsi:type
    """
    assert_bindings(
        schema="msData/additional/test69846.xsd",
        instance="msData/additional/test69846.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b019_add_b019_v(mode, save_output):
    """
    TEST :Adhoc XSD: : id="68938" description="xsd: fractional digit and
    total digit are not checking correcting in XSD datatypes"
    """
    assert_bindings(
        schema="msData/additional/test68938.xsd",
        instance="msData/additional/test68938.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_b012_add_b012_v(mode, save_output):
    """
    TEST :Adhoc XSD: : id="67500" title="xsd: checking QName datatype
    correctly for the namespace declared on the same element"
    """
    assert_bindings(
        schema="msData/additional/test67500.xsd",
        instance="msData/additional/test67500.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_c001_add_c001_v(mode, save_output):
    """
    TEST :Adhoc XSD: : use of xml:base
    """
    assert_bindings(
        schema="msData/additional/adhocAddC001.xsd",
        instance="msData/additional/adhocAddC001.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_add_a005_add_a005_v(mode, save_output):
    """
    TEST :Adhoc XSD: : substitution group usage in the same XSD file with
    instance XML
    """
    assert_bindings(
        schema="msData/additional/adhocAddB001.xsd",
        instance="msData/additional/adhocAddB001.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_attg_d036_attg_d036_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_attg_d034_attg_d034_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_attg_d033_attg_d033_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_attg_d032_attg_d032_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_attg_d031_attg_d031_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_attg_d029_attg_d029_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_attg_d027_attg_d027_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_attg_d025_attg_d025_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_attg_d022_attg_d022_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_attg_d021_attg_d021_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_attg_d020_attg_d020_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_attg_d019_attg_d019_v(mode, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : Basic
    AttributeGroup with anyAttribute (w/ annotation)
    """
    assert_bindings(
        schema="msData/attributeGroup/attgD019.xsd",
        instance="msData/attributeGroup/attgD019.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_attg_d018_attg_d018_v(mode, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : Basic
    AttributeGroup with anyAttribute (w/ id)
    """
    assert_bindings(
        schema="msData/attributeGroup/attgD018.xsd",
        instance="msData/attributeGroup/attgD018.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_attg_d005_attg_d005_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_attg_d004_attg_d004_v(mode, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : attributeGroup
    with just another attributeGroup, the xml has the attributes
    """
    assert_bindings(
        schema="msData/attributeGroup/attgD004.xsd",
        instance="msData/attributeGroup/attgD004.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


@pytest.mark.skip(reason="Stack abuse")
def test_attg_d003_attg_d003_v(mode, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (ID) : attributeGroup
    with 2000 attribute decl as child, the xml has the 2000 attributes
    """
    assert_bindings(
        schema="msData/attributeGroup/attgD003.xsd",
        instance="msData/attributeGroup/attgD003.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_attg_c038_attg_c038_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_attg_c037_attg_c037_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_attg_c036_attg_c036_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_attg_c035_attg_c035_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_attg_c026_attg_c026_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_attg_c024_attg_c024_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_attg_c010_attg_c010a(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_attg_c007_attg_c007_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_z015_att_z015_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_z014b_att_z014b_i(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_z014a_att_z014a_i(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_z007v_att_z007v_v(mode, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : XSD:
    insertion of prohibited attribute in a derived type
    """
    assert_bindings(
        schema="msData/attribute/attZ007.xsd",
        instance="msData/attribute/attZ007v.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_z005_att_z005_v(mode, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : XSD: default
    value of attribute
    """
    assert_bindings(
        schema="msData/attribute/attZ005.xsd",
        instance="msData/attribute/attZ005.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_z002_att_z002_v(mode, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : prohibited
    attribute
    """
    assert_bindings(
        schema="msData/attribute/attZ002.xsd",
        instance="msData/attribute/attZ002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_q019_att_q019_v(mode, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : two
    attribute, same loca name, from different namespace on same element
    """
    assert_bindings(
        schema="msData/attribute/attQ019.xsd",
        instance="msData/attribute/attQ019.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_q014_att_q014_v(mode, save_output):
    r"""
    TEST :Syntax Checking for Attribute Declaration (form) :
    Attribute\attribute decl under extension element
    """
    assert_bindings(
        schema="msData/attribute/attQ014.xsd",
        instance="msData/attribute/attQ014.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_q003_att_q003_v(mode, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : parent is
    complexType, Attr Decl, followed by Attr Group, follow by Attr
    """
    assert_bindings(
        schema="msData/attribute/attQ003.xsd",
        instance="msData/attribute/attQ003.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_p032_att_p032_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_p031_att_p031_i(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_p029_att_p029_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_p028_att_p028_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_p026_att_p026_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_p025_att_p025_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_p024_att_p024_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_p023_att_p023_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_p022_att_p022_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_p021_att_p021_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_p019_att_p019_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_p017_att_p017_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_p015_att_p015_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_p013_att_p013_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_p011_att_p011_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_p007_att_p007_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_p004_att_p004_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_mc009_att_mc009_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_mc008_att_mc008_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_mc007_att_mc007_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_mc006_att_mc006_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_mc005_att_mc005_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_mc004_att_mc004_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_mb009_att_mb009_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_mb008_att_mb008_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_mb007_att_mb007_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_mb006_att_mb006_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_mb005_att_mb005_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_mb004_att_mb004_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_ma004_att_ma004_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_ma003_att_ma003_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_o011_att_o011_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_o010_att_o010_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_o009_att_o009_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_o007_att_o007_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_o006_att_o006_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_lc006_att_lc006_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_lc004_att_lc004_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_lc003_att_lc003_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_lc002_att_lc002_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_lc001_att_lc001_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_lb006_att_lb006_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_lb004_att_lb004_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_lb003_att_lb003_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_lb002_att_lb002_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_lb001_att_lb001_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_la006_att_la006_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_la004_att_la004_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_la003_att_la003_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_la002_att_la002_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_la001_att_la001_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_i003_att_i003_v(mode, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Basic
    attribute with annotation followed by simpleType content
    """
    assert_bindings(
        schema="msData/attribute/attI003.xsd",
        instance="msData/attribute/attI003.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_j018_att_j018_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_j007_att_j007_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_j006_att_j006_v(mode, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : xml doc
    specify the attribute, use = 'optional'
    """
    assert_bindings(
        schema="msData/attribute/attJ006.xsd",
        instance="msData/attribute/attJ006.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_j005_att_j005_v(mode, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : xml doc do
    not specify the attribute, use = 'optional'
    """
    assert_bindings(
        schema="msData/attribute/attJ005.xsd",
        instance="msData/attribute/attJ005.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_j004_att_j004_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_j001_att_j001_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_f003_att_f003_v(mode, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Test
    attribute declaration with optional attribute use = 'required'
    """
    assert_bindings(
        schema="msData/attribute/attF003.xsd",
        instance="msData/attribute/attF003.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_f002_att_f002_v(mode, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Test
    attribute declaration with optional attribute use = 'optional'
    """
    assert_bindings(
        schema="msData/attribute/attF002.xsd",
        instance="msData/attribute/attF002.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_e001_att_e001_v(mode, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Local
    attribute declaration ref='global attribute name'
    """
    assert_bindings(
        schema="msData/attribute/attE001.xsd",
        instance="msData/attribute/attE001.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_d007_att_d007_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_d004_att_d004_v(mode, save_output):
    """
    TEST :Syntax Checking for Attribute Declaration (form) : Global
    attribute declaration type='simpleType with a list of number'
    """
    assert_bindings(
        schema="msData/attribute/attD004.xsd",
        instance="msData/attribute/attD004.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_att_d003_att_d003_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_z013b_ct_z013b_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : fixed
    value on mixed type element (2)
    """
    assert_bindings(
        schema="msData/complexType/ctZ013.xsd",
        instance="msData/complexType/ctZ013b.xml",
        class_name="E",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_z013a_ct_z013a_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : fixed
    value on mixed type element (1)
    """
    assert_bindings(
        schema="msData/complexType/ctZ013.xsd",
        instance="msData/complexType/ctZ013a.xml",
        class_name="E",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_z011_b_ct_z011_b_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    "anyType" in instance document using xsi:type(2)
    """
    assert_bindings(
        schema="msData/complexType/ctZ011.xsd",
        instance="msData/complexType/ctZ011.xml",
        class_name="A",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_z009_d_ct_z009_d_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Ambiguous but valid content models (6)
    """
    assert_bindings(
        schema="msData/complexType/ctZ009_d.xsd",
        instance="msData/complexType/ctZ009_d.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_z009_b_ct_z009_b_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Ambiguous but valid content models (4)
    """
    assert_bindings(
        schema="msData/complexType/ctZ009_a.xsd",
        instance="msData/complexType/ctZ009_b.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_z009_a_ct_z009_a_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Ambiguous but valid content models (3)
    """
    assert_bindings(
        schema="msData/complexType/ctZ009_a.xsd",
        instance="msData/complexType/ctZ009_a.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_z009_ct_z009_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Ambiguous but valid content models (2)
    """
    assert_bindings(
        schema="msData/complexType/ctZ009.xsd",
        instance="msData/complexType/ctZ009.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_z008_ct_z008_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Ambiguous but valid content models
    """
    assert_bindings(
        schema="msData/complexType/ctZ008.xsd",
        instance="msData/complexType/ctZ008.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_z007_ct_z007_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : Derived
    types validated as base type when substitution group used
    """
    assert_bindings(
        schema="msData/complexType/ctZ007_a.xsd",
        instance="msData/complexType/ctZ007.xml",
        class_name="Customers",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="single-package",
    )


def test_ct_z006_ct_z006_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Inderterminstic schemas
    """
    assert_bindings(
        schema="msData/complexType/ctZ006.xsd",
        instance="msData/complexType/ctZ006.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_z003_ct_z003_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_z001_ct_z001_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    extensions to xsd:anyType in substitution groups
    """
    assert_bindings(
        schema="msData/complexType/75039.xsd",
        instance="msData/complexType/75039.xml",
        class_name="BagOfHeads",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_o006_ct_o006_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_o003_ct_o003_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_o001_ct_o001_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    derivation=restriction. final base type not restriction
    """
    assert_bindings(
        schema="msData/complexType/ctO001.xsd",
        instance="msData/complexType/ctO001.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_n004_ct_n004_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_n003_ct_n003_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_n001_ct_n001_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    derivation=extension. final of base type not extension
    """
    assert_bindings(
        schema="msData/complexType/ctN001.xsd",
        instance="msData/complexType/ctN001.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_m002_ct_m002_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexType with base type a simpleType. derivation = extension
    """
    assert_bindings(
        schema="msData/complexType/ctM002.xsd",
        instance="msData/complexType/ctM002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_l022_ct_l022_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : ability
    to use abstract complexType as xsi:type using inline schemas
    """
    assert_bindings(
        schema="msData/complexType/test67200.xsd",
        instance="msData/complexType/test67200.xml",
        class_name="Elt1",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_l021_ct_l021_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_l019_ct_l019_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_l018_ct_l018_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_l017_ct_l017_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_l016_ct_l016_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_l015_ct_l015_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_l014_ct_l014_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    has attributes defined. instance document has attributes
    """
    assert_bindings(
        schema="msData/complexType/ctL014.xsd",
        instance="msData/complexType/ctL014.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_l011_ct_l011_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    is mixed. instance document elements in same order as type definition
    """
    assert_bindings(
        schema="msData/complexType/ctL011.xsd",
        instance="msData/complexType/ctL011.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_l008_ct_l008_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_l007_ct_l007_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    is element only. instance document element only whitespace
    """
    assert_bindings(
        schema="msData/complexType/ctL007.xsd",
        instance="msData/complexType/ctL007.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_l005_ct_l005_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    is element only. instance document element has element children
    """
    assert_bindings(
        schema="msData/complexType/ctL005.xsd",
        instance="msData/complexType/ctL005.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_l003_ct_l003_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    is empty. instance document element is empty
    """
    assert_bindings(
        schema="msData/complexType/ctL003.xsd",
        instance="msData/complexType/ctL003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_k001_ct_k001_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_j001_ct_j001_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent with base = a complexType definition
    """
    assert_bindings(
        schema="msData/complexType/ctJ001.xsd",
        instance="msData/complexType/ctJ001.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_i050_ct_i050_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_i047_ct_i047_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_i046_ct_i046_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_i044_ct_i044_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_i043_ct_i043_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_i041_ct_i041_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_i040_ct_i040_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_i037_ct_i037_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_i036_ct_i036_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_i034_ct_i034_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_i033_ct_i033_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_i029_ct_i029_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_i028_ct_i028_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_i027_ct_i027_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_i026_ct_i026_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_i025_ct_i025_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_i023_ct_i023_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : schema
    with finalDefault = 'extension' , derived complexType by restriction
    """
    assert_bindings(
        schema="msData/complexType/ctI023.xsd",
        instance="msData/complexType/ctI023.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_i022_ct_i022_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_i021_ct_i021_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : schema
    with finalDefault = 'restriction' , derived complexType by extension
    """
    assert_bindings(
        schema="msData/complexType/ctI021.xsd",
        instance="msData/complexType/ctI021.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_i019_ct_i019_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_i018_ct_i018_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_i015_ct_i015_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : schema
    with finalDefault = '' , derived complexType by extension
    """
    assert_bindings(
        schema="msData/complexType/ctI015.xsd",
        instance="msData/complexType/ctI015.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_i014_ct_i014_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : schema
    with finalDefault = '' , derived complexType by restriction
    """
    assert_bindings(
        schema="msData/complexType/ctI014.xsd",
        instance="msData/complexType/ctI014.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_i010_ct_i010_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_i009_ct_i009_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_i005_ct_i005_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_i004_ct_i004_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_i003_ct_i003_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_h082_ct_h082_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_h071_ct_h071_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with anyAttribute
    """
    assert_bindings(
        schema="msData/complexType/ctH071.xsd",
        instance="msData/complexType/ctH071.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_h069_ct_h069_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_h068_ct_h068_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_h067_ct_h067_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_h066_ct_h066_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_h060_ct_h060_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with attributeGroup
    """
    assert_bindings(
        schema="msData/complexType/ctH060.xsd",
        instance="msData/complexType/ctH060.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_h058_ct_h058_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_h057_ct_h057_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_h056_ct_h056_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_h055_ct_h055_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_h049_ct_h049_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with attribute
    """
    assert_bindings(
        schema="msData/complexType/ctH049.xsd",
        instance="msData/complexType/ctH049.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_h047_ct_h047_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_h046_ct_h046_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_h045_ct_h045_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_h044_ct_h044_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_h043_ct_h043_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_h037_ct_h037_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with sequence
    """
    assert_bindings(
        schema="msData/complexType/ctH037.xsd",
        instance="msData/complexType/ctH037.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_h035_ct_h035_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_h034_ct_h034_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_h033_ct_h033_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_h032_ct_h032_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_h031_ct_h031_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_h025_ct_h025_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with choice
    """
    assert_bindings(
        schema="msData/complexType/ctH025.xsd",
        instance="msData/complexType/ctH025.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_h011_ct_h011_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_h010_ct_h010_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_h009_ct_h009_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_h008_ct_h008_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_h007_ct_h007_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_h001_ct_h001_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of extension and content with group
    """
    assert_bindings(
        schema="msData/complexType/ctH001.xsd",
        instance="msData/complexType/ctH001.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g071_ct_g071_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with anyAttribute
    """
    assert_bindings(
        schema="msData/complexType/ctG071.xsd",
        instance="msData/complexType/ctG071.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g069_ct_g069_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g068_ct_g068_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g067_ct_g067_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g066_ct_g066_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g060_ct_g060_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with attributeGroup
    """
    assert_bindings(
        schema="msData/complexType/ctG060.xsd",
        instance="msData/complexType/ctG060.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g058_ct_g058_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g057_ct_g057_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g056_ct_g056_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g055_ct_g055_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g049_ct_g049_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with attribute
    """
    assert_bindings(
        schema="msData/complexType/ctG049.xsd",
        instance="msData/complexType/ctG049.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g047_ct_g047_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g046_ct_g046_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g045_ct_g045_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g044_ct_g044_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g043_ct_g043_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g037_ct_g037_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with sequence
    """
    assert_bindings(
        schema="msData/complexType/ctG037.xsd",
        instance="msData/complexType/ctG037.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g035_ct_g035_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g034_ct_g034_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g033_ct_g033_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g032_ct_g032_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g031_ct_g031_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g025_ct_g025_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with choice
    """
    assert_bindings(
        schema="msData/complexType/ctG025.xsd",
        instance="msData/complexType/ctG025.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g023_ct_g023_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g022_ct_g022_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g021_ct_g021_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g020_ct_g020_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g019_ct_g019_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g013_ct_g013_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent, content of restriction and content with all
    """
    assert_bindings(
        schema="msData/complexType/ctG013.xsd",
        instance="msData/complexType/ctG013.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g011_ct_g011_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g010_ct_g010_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g009_ct_g009_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g008_ct_g008_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g007_ct_g007_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_g001_ct_g001_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_f014_ct_f014_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent and content of extension
    """
    assert_bindings(
        schema="msData/complexType/ctF014.xsd",
        instance="msData/complexType/ctF014.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_f013_ct_f013_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    complexContent and content of annotation and restriction
    """
    assert_bindings(
        schema="msData/complexType/ctF013.xsd",
        instance="msData/complexType/ctF013.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_f011_ct_f011_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_f010_ct_f010_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_f007_ct_f007_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_f001_ct_f001_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    comlexContent with optional attribute id = 'foo123'
    """
    assert_bindings(
        schema="msData/complexType/ctF001.xsd",
        instance="msData/complexType/ctF001.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_e019_ct_e019_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Chameleon case for simpleContent restriction
    """
    assert_bindings(
        schema="msData/complexType/ctE019_a.xsd",
        instance="msData/complexType/ctE019.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_e018_ct_e018_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Chameleon case for simpleContent extension
    """
    assert_bindings(
        schema="msData/complexType/ctE018_a.xsd",
        instance="msData/complexType/ctE018.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_e017_ct_e017_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_e010_ct_e010_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_e008_ct_e008_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_e007_ct_e007_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_e006_ct_e006_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_e002_ct_e002_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_e001_ct_e001_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of extension and base='xsd:string'
    """
    assert_bindings(
        schema="msData/complexType/ctE001.xsd",
        instance="msData/complexType/ctE001.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_d035_ct_d035_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_d033_ct_d033_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of anyAttribute
    """
    assert_bindings(
        schema="msData/complexType/ctD033.xsd",
        instance="msData/complexType/ctD033.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_d032_ct_d032_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_d031_ct_d031_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of attributeGroup
    """
    assert_bindings(
        schema="msData/complexType/ctD031.xsd",
        instance="msData/complexType/ctD031.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_d030_ct_d030_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of two attributes
    """
    assert_bindings(
        schema="msData/complexType/ctD030.xsd",
        instance="msData/complexType/ctD030.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_d029_ct_d029_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of attribute
    """
    assert_bindings(
        schema="msData/complexType/ctD029.xsd",
        instance="msData/complexType/ctD029.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_d028_ct_d028_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of two facets
    """
    assert_bindings(
        schema="msData/complexType/ctD028.xsd",
        instance="msData/complexType/ctD028.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_d027_ct_d027_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of whiteSpace
    """
    assert_bindings(
        schema="msData/complexType/ctD027.xsd",
        instance="msData/complexType/ctD027.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_d026_ct_d026_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of fractionDigits
    """
    assert_bindings(
        schema="msData/complexType/ctD026.xsd",
        instance="msData/complexType/ctD026.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_d025_ct_d025_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of totalDigits
    """
    assert_bindings(
        schema="msData/complexType/ctD025.xsd",
        instance="msData/complexType/ctD025.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_d023_ct_d023_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of pattern
    """
    assert_bindings(
        schema="msData/complexType/ctD023.xsd",
        instance="msData/complexType/ctD023.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_d022_ct_d022_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of minLength
    """
    assert_bindings(
        schema="msData/complexType/ctD022.xsd",
        instance="msData/complexType/ctD022.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_d021_ct_d021_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of minInclusive
    """
    assert_bindings(
        schema="msData/complexType/ctD021.xsd",
        instance="msData/complexType/ctD021.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_d020_ct_d020_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of minExclusive
    """
    assert_bindings(
        schema="msData/complexType/ctD020.xsd",
        instance="msData/complexType/ctD020.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_d019_ct_d019_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of maxLength
    """
    assert_bindings(
        schema="msData/complexType/ctD019.xsd",
        instance="msData/complexType/ctD019.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_d018_ct_d018_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of maxInclusive
    """
    assert_bindings(
        schema="msData/complexType/ctD018.xsd",
        instance="msData/complexType/ctD018.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_d017_ct_d017_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of maxExclusive
    """
    assert_bindings(
        schema="msData/complexType/ctD017.xsd",
        instance="msData/complexType/ctD017.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_d016_ct_d016_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of length
    """
    assert_bindings(
        schema="msData/complexType/ctD016.xsd",
        instance="msData/complexType/ctD016.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_d015_ct_d015_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of enumeration
    """
    assert_bindings(
        schema="msData/complexType/ctD015.xsd",
        instance="msData/complexType/ctD015.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_d012_ct_d012_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_d010_ct_d010_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_d008_ct_d008_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of simpleType
    """
    assert_bindings(
        schema="msData/complexType/ctD008.xsd",
        instance="msData/complexType/ctD008.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_d006_ct_d006_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and content of annotation
    """
    assert_bindings(
        schema="msData/complexType/ctD006.xsd",
        instance="msData/complexType/ctD006.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_d005_ct_d005_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and empty content
    """
    assert_bindings(
        schema="msData/complexType/ctD005.xsd",
        instance="msData/complexType/ctD005.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_d002_ct_d002_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent, content of restriction and base = defined complex type
    """
    assert_bindings(
        schema="msData/complexType/ctD002.xsd",
        instance="msData/complexType/ctD002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_c012_ct_c012_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent and content of annotation and extension
    """
    assert_bindings(
        schema="msData/complexType/ctC012.xsd",
        instance="msData/complexType/ctC012.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_c008_ct_c008_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent and content of extension
    """
    assert_bindings(
        schema="msData/complexType/ctC008.xsd",
        instance="msData/complexType/ctC008.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_c007_ct_c007_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent and content of annotation and restriction
    """
    assert_bindings(
        schema="msData/complexType/ctC007.xsd",
        instance="msData/complexType/ctC007.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_c006_ct_c006_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    attribute with non-schema namespace
    """
    assert_bindings(
        schema="msData/complexType/ctC006.xsd",
        instance="msData/complexType/ctC006.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_c001_ct_c001_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    simpleContent with optional attribute id = 'foo123'
    """
    assert_bindings(
        schema="msData/complexType/ctC001.xsd",
        instance="msData/complexType/ctC001.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b113_ct_b113_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with anyAttribute
    """
    assert_bindings(
        schema="msData/complexType/ctB113.xsd",
        instance="msData/complexType/ctB113.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b111_ct_b111_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with attributeGroup then anyAttribute
    """
    assert_bindings(
        schema="msData/complexType/ctB111.xsd",
        instance="msData/complexType/ctB111.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b110_ct_b110_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with attributeGroup then attributeGroup
    """
    assert_bindings(
        schema="msData/complexType/ctB110.xsd",
        instance="msData/complexType/ctB110.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b109_ct_b109_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with attributeGroup then two attributes
    """
    assert_bindings(
        schema="msData/complexType/ctB109.xsd",
        instance="msData/complexType/ctB109.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b108_ct_b108_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with attributeGroup then attribute
    """
    assert_bindings(
        schema="msData/complexType/ctB108.xsd",
        instance="msData/complexType/ctB108.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b100_ct_b100_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with attributeGroup
    """
    assert_bindings(
        schema="msData/complexType/ctB100.xsd",
        instance="msData/complexType/ctB100.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b098_ct_b098_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with attribute then anyAttribute
    """
    assert_bindings(
        schema="msData/complexType/ctB098.xsd",
        instance="msData/complexType/ctB098.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b097_ct_b097_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with attribute then two attributeGroups
    """
    assert_bindings(
        schema="msData/complexType/ctB097.xsd",
        instance="msData/complexType/ctB097.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b096_ct_b096_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with attribute then attributeGroup
    """
    assert_bindings(
        schema="msData/complexType/ctB096.xsd",
        instance="msData/complexType/ctB096.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b095_ct_b095_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with attribute then attribute
    """
    assert_bindings(
        schema="msData/complexType/ctB095.xsd",
        instance="msData/complexType/ctB095.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b087_ct_b087_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with attribute
    """
    assert_bindings(
        schema="msData/complexType/ctB087.xsd",
        instance="msData/complexType/ctB087.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b085_ct_b085_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with sequence then anyAttribute
    """
    assert_bindings(
        schema="msData/complexType/ctB085.xsd",
        instance="msData/complexType/ctB085.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b084_ct_b084_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with sequence then two attributeGroups
    """
    assert_bindings(
        schema="msData/complexType/ctB084.xsd",
        instance="msData/complexType/ctB084.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b083_ct_b083_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with sequence then attributeGroup
    """
    assert_bindings(
        schema="msData/complexType/ctB083.xsd",
        instance="msData/complexType/ctB083.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b082_ct_b082_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with sequence then two attributes
    """
    assert_bindings(
        schema="msData/complexType/ctB082.xsd",
        instance="msData/complexType/ctB082.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b081_ct_b081_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with sequence then attribute
    """
    assert_bindings(
        schema="msData/complexType/ctB081.xsd",
        instance="msData/complexType/ctB081.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b073_ct_b073_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with sequence
    """
    assert_bindings(
        schema="msData/complexType/ctB073.xsd",
        instance="msData/complexType/ctB073.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b071_ct_b071_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with choice then anyAttribute
    """
    assert_bindings(
        schema="msData/complexType/ctB071.xsd",
        instance="msData/complexType/ctB071.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b070_ct_b070_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with choice then two attributeGroups
    """
    assert_bindings(
        schema="msData/complexType/ctB070.xsd",
        instance="msData/complexType/ctB070.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b069_ct_b069_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with choice then attributeGroup
    """
    assert_bindings(
        schema="msData/complexType/ctB069.xsd",
        instance="msData/complexType/ctB069.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b068_ct_b068_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with choice then two attributes
    """
    assert_bindings(
        schema="msData/complexType/ctB068.xsd",
        instance="msData/complexType/ctB068.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b067_ct_b067_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with choice then attribute
    """
    assert_bindings(
        schema="msData/complexType/ctB067.xsd",
        instance="msData/complexType/ctB067.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b059_ct_b059_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with choice
    """
    assert_bindings(
        schema="msData/complexType/ctB059.xsd",
        instance="msData/complexType/ctB059.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b057_ct_b057_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with all then anyAttribute
    """
    assert_bindings(
        schema="msData/complexType/ctB057.xsd",
        instance="msData/complexType/ctB057.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b056_ct_b056_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with all then two attributeGroups
    """
    assert_bindings(
        schema="msData/complexType/ctB056.xsd",
        instance="msData/complexType/ctB056.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b055_ct_b055_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with all then attributeGroup
    """
    assert_bindings(
        schema="msData/complexType/ctB055.xsd",
        instance="msData/complexType/ctB055.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b054_ct_b054_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with all then two attributes
    """
    assert_bindings(
        schema="msData/complexType/ctB054.xsd",
        instance="msData/complexType/ctB054.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b053_ct_b053_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with all then attribute
    """
    assert_bindings(
        schema="msData/complexType/ctB053.xsd",
        instance="msData/complexType/ctB053.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b045_ct_b045_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with all
    """
    assert_bindings(
        schema="msData/complexType/ctB045.xsd",
        instance="msData/complexType/ctB045.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b043_ct_b043_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with group then anyAttribute
    """
    assert_bindings(
        schema="msData/complexType/ctB043.xsd",
        instance="msData/complexType/ctB043.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b042_ct_b042_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with group then two attributeGroups
    """
    assert_bindings(
        schema="msData/complexType/ctB042.xsd",
        instance="msData/complexType/ctB042.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b041_ct_b041_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with group then attributeGroup
    """
    assert_bindings(
        schema="msData/complexType/ctB041.xsd",
        instance="msData/complexType/ctB041.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b040_ct_b040_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with group then two attributes
    """
    assert_bindings(
        schema="msData/complexType/ctB040.xsd",
        instance="msData/complexType/ctB040.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b039_ct_b039_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with group then attribute
    """
    assert_bindings(
        schema="msData/complexType/ctB039.xsd",
        instance="msData/complexType/ctB039.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b031_ct_b031_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with group
    """
    assert_bindings(
        schema="msData/complexType/ctB031.xsd",
        instance="msData/complexType/ctB031.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b017_ct_b017_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with complexContent
    """
    assert_bindings(
        schema="msData/complexType/ctB017.xsd",
        instance="msData/complexType/ctB017.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b003_ct_b003_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    with simpleContent
    """
    assert_bindings(
        schema="msData/complexType/ctB003.xsd",
        instance="msData/complexType/ctB003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_b001_ct_b001_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration : content
    of single annotation
    """
    assert_bindings(
        schema="msData/complexType/ctB001.xsd",
        instance="msData/complexType/ctB001.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_a049_ct_a049_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    attribute with non-schema namespace
    """
    assert_bindings(
        schema="msData/complexType/ctA049.xsd",
        instance="msData/complexType/ctA049.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_a048_ct_a048_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute name = '_1'
    """
    assert_bindings(
        schema="msData/complexType/ctA048.xsd",
        instance="msData/complexType/ctA048.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_a047_ct_a047_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute name = '_foo'
    """
    assert_bindings(
        schema="msData/complexType/ctA047.xsd",
        instance="msData/complexType/ctA047.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_a045_ct_a045_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute name = 'xmlns'
    """
    assert_bindings(
        schema="msData/complexType/ctA045.xsd",
        instance="msData/complexType/ctA045.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_a041_ct_a041_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute name = 'fooType'
    """
    assert_bindings(
        schema="msData/complexType/ctA041.xsd",
        instance="msData/complexType/ctA041.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_a037_ct_a037_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute mixed = '0'
    """
    assert_bindings(
        schema="msData/complexType/ctA037.xsd",
        instance="msData/complexType/ctA037.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_a035_ct_a035_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute mixed = '1'
    """
    assert_bindings(
        schema="msData/complexType/ctA035.xsd",
        instance="msData/complexType/ctA035.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_a034_ct_a034_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute mixed = 'false'
    """
    assert_bindings(
        schema="msData/complexType/ctA034.xsd",
        instance="msData/complexType/ctA034.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_a033_ct_a033_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute mixed = 'true'
    """
    assert_bindings(
        schema="msData/complexType/ctA033.xsd",
        instance="msData/complexType/ctA033.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_a032_ct_a032_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_a027_ct_a027_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute id = 'foo123'
    """
    assert_bindings(
        schema="msData/complexType/ctA027.xsd",
        instance="msData/complexType/ctA027.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_a026_ct_a026_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute final = ''
    """
    assert_bindings(
        schema="msData/complexType/ctA026.xsd",
        instance="msData/complexType/ctA026.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_a022_ct_a022_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute final = 'extension restriction'
    """
    assert_bindings(
        schema="msData/complexType/ctA022.xsd",
        instance="msData/complexType/ctA022.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_a021_ct_a021_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute final = 'restriction extension'
    """
    assert_bindings(
        schema="msData/complexType/ctA021.xsd",
        instance="msData/complexType/ctA021.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_a020_ct_a020_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute final = 'restriction'
    """
    assert_bindings(
        schema="msData/complexType/ctA020.xsd",
        instance="msData/complexType/ctA020.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_a019_ct_a019_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute final = 'extension'
    """
    assert_bindings(
        schema="msData/complexType/ctA019.xsd",
        instance="msData/complexType/ctA019.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_a018_ct_a018_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute final = '#all'
    """
    assert_bindings(
        schema="msData/complexType/ctA018.xsd",
        instance="msData/complexType/ctA018.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_a017_ct_a017_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute block = ''
    """
    assert_bindings(
        schema="msData/complexType/ctA017.xsd",
        instance="msData/complexType/ctA017.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_a013_ct_a013_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute block = 'extension restriction'
    """
    assert_bindings(
        schema="msData/complexType/ctA013.xsd",
        instance="msData/complexType/ctA013.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_a012_ct_a012_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute block = 'restriction extension'
    """
    assert_bindings(
        schema="msData/complexType/ctA012.xsd",
        instance="msData/complexType/ctA012.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_a011_ct_a011_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute block = 'restriction'
    """
    assert_bindings(
        schema="msData/complexType/ctA011.xsd",
        instance="msData/complexType/ctA011.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_a010_ct_a010_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute block = 'extension'
    """
    assert_bindings(
        schema="msData/complexType/ctA010.xsd",
        instance="msData/complexType/ctA010.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_a009_ct_a009_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute block = '#all'
    """
    assert_bindings(
        schema="msData/complexType/ctA009.xsd",
        instance="msData/complexType/ctA009.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_a005_ct_a005_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute abstract = '0'
    """
    assert_bindings(
        schema="msData/complexType/ctA005.xsd",
        instance="msData/complexType/ctA005.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_a003_ct_a003_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute abstract = '1'
    """
    assert_bindings(
        schema="msData/complexType/ctA003.xsd",
        instance="msData/complexType/ctA003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_a002_ct_a002_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute abstract = 'true'
    """
    assert_bindings(
        schema="msData/complexType/ctA002.xsd",
        instance="msData/complexType/ctA002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ct_a001_ct_a001_v(mode, save_output):
    """
    TEST :Syntax Checking for top level complexType Declaration :
    Declaration with optional attribute abstract = 'false'
    """
    assert_bindings(
        schema="msData/complexType/ctA001.xsd",
        instance="msData/complexType/ctA001.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_dt_z107447_a_2245_dt_z107447_a_2245_i(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_dt_z107447_1_2244_dt_z107447_1_2244_v(mode, save_output):
    """
    TEST :Facet Schemas for string : XSD:whitespace handling for xs:token
    should be collapse(1)
    """
    assert_bindings(
        schema="msData/datatypes/test107447.xsd",
        instance="msData/datatypes/test107447_1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_dt_z107447_2243_dt_z107447_2243_v(mode, save_output):
    """
    TEST :Facet Schemas for string : XSD:whitespace handling for xs:token
    should be collapse.
    """
    assert_bindings(
        schema="msData/datatypes/test107447.xsd",
        instance="msData/datatypes/test107447.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_id_test70681_2241_id_test70681_2241_v(mode, save_output):
    """
    TEST :Facet Schemas for string : ID/IDREF should not allow heading or
    trailing whitespace like NCNAME
    """
    assert_bindings(
        schema="msData/datatypes/datatypes.xsd",
        instance="msData/datatypes/ID_test70681.xml",
        class_name="Data",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_id_test64335_2240_id_test64335_2240_v(mode, save_output):
    """
    TEST :Facet Schemas for string : ID data type validation
    """
    assert_bindings(
        schema="msData/datatypes/ID_test64335.xsd",
        instance="msData/datatypes/ID_test64335.xml",
        class_name="Products",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_positive_integer005_2239_positive_integer005_2239_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=12345678901234567890123456789
    """
    assert_bindings(
        schema="msData/datatypes/positiveInteger.xsd",
        instance="msData/datatypes/positiveInteger005.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_positive_integer004_2238_positive_integer004_2238_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=+1
    """
    assert_bindings(
        schema="msData/datatypes/positiveInteger.xsd",
        instance="msData/datatypes/positiveInteger004.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_byte007_2234_unsigned_byte007_2234_v(mode, save_output):
    """
    TEST :Facet Schemas for string : test for simpleType list of
    unsignedByte
    """
    assert_bindings(
        schema="msData/datatypes/unsignedByte007.xsd",
        instance="msData/datatypes/unsignedByte007.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_byte005_2232_unsigned_byte005_2232_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=255
    """
    assert_bindings(
        schema="msData/datatypes/unsignedByte.xsd",
        instance="msData/datatypes/unsignedByte005.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_byte004_2231_unsigned_byte004_2231_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=1
    """
    assert_bindings(
        schema="msData/datatypes/unsignedByte.xsd",
        instance="msData/datatypes/unsignedByte004.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_byte003_2230_unsigned_byte003_2230_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=0
    """
    assert_bindings(
        schema="msData/datatypes/unsignedByte.xsd",
        instance="msData/datatypes/unsignedByte003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_short007_2227_unsigned_short007_2227_v(mode, save_output):
    """
    TEST :Facet Schemas for string : test for simpleType list of
    unsignedShort
    """
    assert_bindings(
        schema="msData/datatypes/unsignedShort007.xsd",
        instance="msData/datatypes/unsignedShort007.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_short005_2225_unsigned_short005_2225_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=65535
    """
    assert_bindings(
        schema="msData/datatypes/unsignedShort.xsd",
        instance="msData/datatypes/unsignedShort005.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_short004_2224_unsigned_short004_2224_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=1
    """
    assert_bindings(
        schema="msData/datatypes/unsignedShort.xsd",
        instance="msData/datatypes/unsignedShort004.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_short003_2223_unsigned_short003_2223_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=0
    """
    assert_bindings(
        schema="msData/datatypes/unsignedShort.xsd",
        instance="msData/datatypes/unsignedShort003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_int007_2220_unsigned_int007_2220_v(mode, save_output):
    """
    TEST :Facet Schemas for string : test for simpleType list of
    unsignedInt
    """
    assert_bindings(
        schema="msData/datatypes/unsignedInt007.xsd",
        instance="msData/datatypes/unsignedInt007.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_int005_2218_unsigned_int005_2218_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=4294967295
    """
    assert_bindings(
        schema="msData/datatypes/unsignedInt.xsd",
        instance="msData/datatypes/unsignedInt005.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_int004_2217_unsigned_int004_2217_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=1
    """
    assert_bindings(
        schema="msData/datatypes/unsignedInt.xsd",
        instance="msData/datatypes/unsignedInt004.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_int003_2216_unsigned_int003_2216_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=0
    """
    assert_bindings(
        schema="msData/datatypes/unsignedInt.xsd",
        instance="msData/datatypes/unsignedInt003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_long007_2213_unsigned_long007_2213_v(mode, save_output):
    """
    TEST :Facet Schemas for string : test for simpleType list of
    unsignedLong
    """
    assert_bindings(
        schema="msData/datatypes/unsignedLong007.xsd",
        instance="msData/datatypes/unsignedLong007.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_long005_2211_unsigned_long005_2211_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=18446744073709551615
    """
    assert_bindings(
        schema="msData/datatypes/unsignedLong.xsd",
        instance="msData/datatypes/unsignedLong005.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_long004_2210_unsigned_long004_2210_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=1
    """
    assert_bindings(
        schema="msData/datatypes/unsignedLong.xsd",
        instance="msData/datatypes/unsignedLong004.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_long003_2209_unsigned_long003_2209_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=0
    """
    assert_bindings(
        schema="msData/datatypes/unsignedLong.xsd",
        instance="msData/datatypes/unsignedLong003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_negative_integer005_2206_non_negative_integer005_2206_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=12345678901234567890123456789
    """
    assert_bindings(
        schema="msData/datatypes/nonNegativeInteger.xsd",
        instance="msData/datatypes/nonNegativeInteger005.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_negative_integer004_2205_non_negative_integer004_2205_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=+1
    """
    assert_bindings(
        schema="msData/datatypes/nonNegativeInteger.xsd",
        instance="msData/datatypes/nonNegativeInteger004.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_negative_integer003_2204_non_negative_integer003_2204_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=0
    """
    assert_bindings(
        schema="msData/datatypes/nonNegativeInteger.xsd",
        instance="msData/datatypes/nonNegativeInteger003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_byte009_2201_byte009_2201_v(mode, save_output):
    """
    TEST :Facet Schemas for string : Test simpleType List of byte
    """
    assert_bindings(
        schema="msData/datatypes/byte009.xsd",
        instance="msData/datatypes/byte009.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_byte007_2199_byte007_2199_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-128
    """
    assert_bindings(
        schema="msData/datatypes/byte.xsd",
        instance="msData/datatypes/byte007.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_byte005_2197_byte005_2197_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=127
    """
    assert_bindings(
        schema="msData/datatypes/byte.xsd",
        instance="msData/datatypes/byte005.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_byte004_2196_byte004_2196_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=+1
    """
    assert_bindings(
        schema="msData/datatypes/byte.xsd",
        instance="msData/datatypes/byte004.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_byte003_2195_byte003_2195_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=0
    """
    assert_bindings(
        schema="msData/datatypes/byte.xsd",
        instance="msData/datatypes/byte003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_byte002_2194_byte002_2194_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-1
    """
    assert_bindings(
        schema="msData/datatypes/byte.xsd",
        instance="msData/datatypes/byte002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_short009_2192_short009_2192_v(mode, save_output):
    """
    TEST :Facet Schemas for string : test for simpleType list of short
    """
    assert_bindings(
        schema="msData/datatypes/short009.xsd",
        instance="msData/datatypes/short009.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_short007_2190_short007_2190_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-32768
    """
    assert_bindings(
        schema="msData/datatypes/short.xsd",
        instance="msData/datatypes/short007.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_short005_2188_short005_2188_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=32767
    """
    assert_bindings(
        schema="msData/datatypes/short.xsd",
        instance="msData/datatypes/short005.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_short004_2187_short004_2187_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=+1
    """
    assert_bindings(
        schema="msData/datatypes/short.xsd",
        instance="msData/datatypes/short004.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_short003_2186_short003_2186_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=0
    """
    assert_bindings(
        schema="msData/datatypes/short.xsd",
        instance="msData/datatypes/short003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_short002_2185_short002_2185_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-1
    """
    assert_bindings(
        schema="msData/datatypes/short.xsd",
        instance="msData/datatypes/short002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_int007_2182_int007_2182_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-2147483648
    """
    assert_bindings(
        schema="msData/datatypes/int.xsd",
        instance="msData/datatypes/int007.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_int005_2180_int005_2180_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=2147483647
    """
    assert_bindings(
        schema="msData/datatypes/int.xsd",
        instance="msData/datatypes/int005.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_int004_2179_int004_2179_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=+1
    """
    assert_bindings(
        schema="msData/datatypes/int.xsd",
        instance="msData/datatypes/int004.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_int003_2178_int003_2178_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=0
    """
    assert_bindings(
        schema="msData/datatypes/int.xsd",
        instance="msData/datatypes/int003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_int002_2177_int002_2177_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-1
    """
    assert_bindings(
        schema="msData/datatypes/int.xsd",
        instance="msData/datatypes/int002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_long009_2175_long009_2175_v(mode, save_output):
    """
    TEST :Facet Schemas for string : Test for simpleType list of Long
    """
    assert_bindings(
        schema="msData/datatypes/long009.xsd",
        instance="msData/datatypes/long009.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_long007_2173_long007_2173_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=9223372036854775807
    """
    assert_bindings(
        schema="msData/datatypes/long.xsd",
        instance="msData/datatypes/long007.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_long005_2171_long005_2171_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-9223372036854775808
    """
    assert_bindings(
        schema="msData/datatypes/long.xsd",
        instance="msData/datatypes/long005.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_long004_2170_long004_2170_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=+1
    """
    assert_bindings(
        schema="msData/datatypes/long.xsd",
        instance="msData/datatypes/long004.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_long003_2169_long003_2169_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=0
    """
    assert_bindings(
        schema="msData/datatypes/long.xsd",
        instance="msData/datatypes/long003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_long002_2168_long002_2168_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-1
    """
    assert_bindings(
        schema="msData/datatypes/long.xsd",
        instance="msData/datatypes/long002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_negative_integer005_2166_negative_integer005_2166_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-12345678901234567890123456789
    """
    assert_bindings(
        schema="msData/datatypes/negativeInteger.xsd",
        instance="msData/datatypes/negativeInteger005.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_negative_integer002_2163_negative_integer002_2163_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-1
    """
    assert_bindings(
        schema="msData/datatypes/negativeInteger.xsd",
        instance="msData/datatypes/negativeInteger002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_positive_integer005_2161_non_positive_integer005_2161_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-12345678901234567890123456789
    """
    assert_bindings(
        schema="msData/datatypes/nonPositiveInteger.xsd",
        instance="msData/datatypes/nonPositiveInteger005.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_positive_integer003_2159_non_positive_integer003_2159_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=0
    """
    assert_bindings(
        schema="msData/datatypes/nonPositiveInteger.xsd",
        instance="msData/datatypes/nonPositiveInteger003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_positive_integer002_2158_non_positive_integer002_2158_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-1
    """
    assert_bindings(
        schema="msData/datatypes/nonPositiveInteger.xsd",
        instance="msData/datatypes/nonPositiveInteger002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_integer011_2151_integer011_2151_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=12345678901234567890123456789
    """
    assert_bindings(
        schema="msData/datatypes/integer.xsd",
        instance="msData/datatypes/integer011.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_integer010_2150_integer010_2150_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=10000000
    """
    assert_bindings(
        schema="msData/datatypes/integer.xsd",
        instance="msData/datatypes/integer010.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_integer009_2149_integer009_2149_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=12678967543233
    """
    assert_bindings(
        schema="msData/datatypes/integer.xsd",
        instance="msData/datatypes/integer009.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_integer008_2148_integer008_2148_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=1
    """
    assert_bindings(
        schema="msData/datatypes/integer.xsd",
        instance="msData/datatypes/integer008.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_integer007_2147_integer007_2147_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-1
    """
    assert_bindings(
        schema="msData/datatypes/integer.xsd",
        instance="msData/datatypes/integer007.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_integer005_2145_integer005_2145_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-0
    """
    assert_bindings(
        schema="msData/datatypes/integer.xsd",
        instance="msData/datatypes/integer005.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_integer004_2144_integer004_2144_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=+0
    """
    assert_bindings(
        schema="msData/datatypes/integer.xsd",
        instance="msData/datatypes/integer004.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ncname007_2136_ncname007_2136_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=fo_124-.sda3
    """
    assert_bindings(
        schema="msData/datatypes/NCName.xsd",
        instance="msData/datatypes/NCName007.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ncname003_2132_ncname003_2132_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=fo124
    """
    assert_bindings(
        schema="msData/datatypes/NCName.xsd",
        instance="msData/datatypes/NCName003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ncname002_2131_ncname002_2131_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=_foo
    """
    assert_bindings(
        schema="msData/datatypes/NCName.xsd",
        instance="msData/datatypes/NCName002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_name016_2127_name016_2127_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=fo:fo_124-.s:da3
    """
    assert_bindings(
        schema="msData/datatypes/Name.xsd",
        instance="msData/datatypes/Name016.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_name015_2126_name015_2126_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=fo:fo_124-.sda3
    """
    assert_bindings(
        schema="msData/datatypes/Name.xsd",
        instance="msData/datatypes/Name015.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_name013_2124_name013_2124_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=fo:.foo
    """
    assert_bindings(
        schema="msData/datatypes/Name.xsd",
        instance="msData/datatypes/Name013.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_name012_2123_name012_2123_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=fo:1fo
    """
    assert_bindings(
        schema="msData/datatypes/Name.xsd",
        instance="msData/datatypes/Name012.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_name011_2122_name011_2122_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=fo:fo124
    """
    assert_bindings(
        schema="msData/datatypes/Name.xsd",
        instance="msData/datatypes/Name011.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_name010_2121_name010_2121_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=fo:_foo
    """
    assert_bindings(
        schema="msData/datatypes/Name.xsd",
        instance="msData/datatypes/Name010.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_name009_2120_name009_2120_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=:foo
    """
    assert_bindings(
        schema="msData/datatypes/Name.xsd",
        instance="msData/datatypes/Name009.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_name008_2119_name008_2119_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=fo:foo
    """
    assert_bindings(
        schema="msData/datatypes/Name.xsd",
        instance="msData/datatypes/Name008.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_name007_2118_name007_2118_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=fo_124-.sda3
    """
    assert_bindings(
        schema="msData/datatypes/Name.xsd",
        instance="msData/datatypes/Name007.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_name003_2114_name003_2114_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=fo124
    """
    assert_bindings(
        schema="msData/datatypes/Name.xsd",
        instance="msData/datatypes/Name003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_name002_2113_name002_2113_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=_foo
    """
    assert_bindings(
        schema="msData/datatypes/Name.xsd",
        instance="msData/datatypes/Name002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_language009_2110_language009_2110_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=X-2o
    """
    assert_bindings(
        schema="msData/datatypes/language.xsd",
        instance="msData/datatypes/language009.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_language007_2108_language007_2108_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=I-en-us
    """
    assert_bindings(
        schema="msData/datatypes/language.xsd",
        instance="msData/datatypes/language007.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_language006_2107_language006_2107_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=spanish
    """
    assert_bindings(
        schema="msData/datatypes/language.xsd",
        instance="msData/datatypes/language006.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_language005_2106_language005_2106_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=en
    """
    assert_bindings(
        schema="msData/datatypes/language.xsd",
        instance="msData/datatypes/language005.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_language004_2105_language004_2105_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=en-us
    """
    assert_bindings(
        schema="msData/datatypes/language.xsd",
        instance="msData/datatypes/language004.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_language003_2104_language003_2104_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=EN-US
    """
    assert_bindings(
        schema="msData/datatypes/language.xsd",
        instance="msData/datatypes/language003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_language002_2103_language002_2103_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=EN
    """
    assert_bindings(
        schema="msData/datatypes/language.xsd",
        instance="msData/datatypes/language002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_token004_2101_token004_2101_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=a b
    """
    assert_bindings(
        schema="msData/datatypes/token.xsd",
        instance="msData/datatypes/token004.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_token003_2100_token003_2100_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=a b
    """
    assert_bindings(
        schema="msData/datatypes/token.xsd",
        instance="msData/datatypes/token003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_token002_2099_token002_2099_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=a b
    """
    assert_bindings(
        schema="msData/datatypes/token.xsd",
        instance="msData/datatypes/token002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_token001_2098_token001_2098_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/token.xsd",
        instance="msData/datatypes/token001.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_normalized_string003_2097_normalized_string003_2097_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=test line
    """
    assert_bindings(
        schema="msData/datatypes/normalizedString.xsd",
        instance="msData/datatypes/normalizedString003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_normalized_string002_2096_normalized_string002_2096_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=test line
    """
    assert_bindings(
        schema="msData/datatypes/normalizedString.xsd",
        instance="msData/datatypes/normalizedString002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_normalized_string001_2095_normalized_string001_2095_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/normalizedString.xsd",
        instance="msData/datatypes/normalizedString001.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_qname006_2089_qname006_2089_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=fo:foo
    """
    assert_bindings(
        schema="msData/datatypes/QName.xsd",
        instance="msData/datatypes/QName006.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_qname003_2086_qname003_2086_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=fo124
    """
    assert_bindings(
        schema="msData/datatypes/QName.xsd",
        instance="msData/datatypes/QName003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_qname002_2085_qname002_2085_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=_foo
    """
    assert_bindings(
        schema="msData/datatypes/QName.xsd",
        instance="msData/datatypes/QName002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_any_uri011_2083_any_uri011_2083_v(mode, save_output):
    """
    TEST :Facet Schemas for string : test for simpleType list of anyURI
    """
    assert_bindings(
        schema="msData/datatypes/anyURI011.xsd",
        instance="msData/datatypes/anyURI011.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_any_uri010_2082_any_uri010_2082_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=C:/TestSuites/XSD%20Spec/CR-
    xmlschema-2-20001024.htm#dc-minInclusive
    """
    assert_bindings(
        schema="msData/datatypes/anyURI.xsd",
        instance="msData/datatypes/anyURI010.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_any_uri009_2081_any_uri009_2081_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_any_uri008_2080_any_uri008_2080_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=telnet://melvyl.ucop.edu/
    """
    assert_bindings(
        schema="msData/datatypes/anyURI.xsd",
        instance="msData/datatypes/anyURI008.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_any_uri007_2079_any_uri007_2079_v(mode, save_output):
    """
    TEST :Facet Schemas for string :
    value=news:comp.infosystems.www.servers.unix
    """
    assert_bindings(
        schema="msData/datatypes/anyURI.xsd",
        instance="msData/datatypes/anyURI007.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_any_uri006_2078_any_uri006_2078_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=gopher://spinaltap.micro.umn.ed
    u/00/Weather/California/Los%20Angeles
    """
    assert_bindings(
        schema="msData/datatypes/anyURI.xsd",
        instance="msData/datatypes/anyURI006.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_any_uri005_2077_any_uri005_2077_v(mode, save_output):
    """
    TEST :Facet Schemas for string :
    value=ftp://ftp.is.co.za/rfc/rfc1808.txt
    """
    assert_bindings(
        schema="msData/datatypes/anyURI.xsd",
        instance="msData/datatypes/anyURI005.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_any_uri004_2076_any_uri004_2076_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_any_uri003_2075_any_uri003_2075_v(mode, save_output):
    """
    TEST :Facet Schemas for string :
    value=http://www.w3.org/1999/XMLSchema
    """
    assert_bindings(
        schema="msData/datatypes/anyURI.xsd",
        instance="msData/datatypes/anyURI003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_any_uri002_2074_any_uri002_2074_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=mailto:davebrow@microsoft.com
    """
    assert_bindings(
        schema="msData/datatypes/anyURI.xsd",
        instance="msData/datatypes/anyURI002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_any_uri001_2073_any_uri001_2073_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/anyURI.xsd",
        instance="msData/datatypes/anyURI001.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_base64_binary002_2072_base64_binary002_2072_v(mode, save_output):
    """
    TEST :Facet Schemas for string : test for simpleType list of
    base64Binary
    """
    assert_bindings(
        schema="msData/datatypes/base64Binary002.xsd",
        instance="msData/datatypes/base64Binary002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_base64_binary001_2071_base64_binary001_2071_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/base64Binary.xsd",
        instance="msData/datatypes/base64Binary001.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_hex_binary002_2068_hex_binary002_2068_v(mode, save_output):
    """
    TEST :Facet Schemas for string : test for simpleType List of hexBinary
    """
    assert_bindings(
        schema="msData/datatypes/hexBinary002.xsd",
        instance="msData/datatypes/hexBinary002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_hex_binary001_2067_hex_binary001_2067_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/hexBinary.xsd",
        instance="msData/datatypes/hexBinary001.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_g_month004_2063_g_month004_2063_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=- -05- - -05:00
    """
    assert_bindings(
        schema="msData/datatypes/gMonth.xsd",
        instance="msData/datatypes/gMonth004.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_g_month002_2061_g_month002_2061_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=- -03- -
    """
    assert_bindings(
        schema="msData/datatypes/gMonth.xsd",
        instance="msData/datatypes/gMonth002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_g_day003_2057_g_day003_2057_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=- - -15-05:00
    """
    assert_bindings(
        schema="msData/datatypes/gDay.xsd",
        instance="msData/datatypes/gDay003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_g_day002_2056_g_day002_2056_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=- - -29
    """
    assert_bindings(
        schema="msData/datatypes/gDay.xsd",
        instance="msData/datatypes/gDay002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_g_day001_2055_g_day001_2055_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=- - -15
    """
    assert_bindings(
        schema="msData/datatypes/gDay.xsd",
        instance="msData/datatypes/gDay001.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_g_month_day004_2052_g_month_day004_2052_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=- -02-29
    """
    assert_bindings(
        schema="msData/datatypes/gMonthDay.xsd",
        instance="msData/datatypes/gMonthDay004.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_g_month_day003_2051_g_month_day003_2051_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=- -03-15-05:00
    """
    assert_bindings(
        schema="msData/datatypes/gMonthDay.xsd",
        instance="msData/datatypes/gMonthDay003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_g_month_day002_2050_g_month_day002_2050_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=- -03-15
    """
    assert_bindings(
        schema="msData/datatypes/gMonthDay.xsd",
        instance="msData/datatypes/gMonthDay002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_g_year006_2048_g_year006_2048_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=1999-05:00
    """
    assert_bindings(
        schema="msData/datatypes/gYear.xsd",
        instance="msData/datatypes/gYear006.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_g_year002_2046_g_year002_2046_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=2000
    """
    assert_bindings(
        schema="msData/datatypes/gYear.xsd",
        instance="msData/datatypes/gYear002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_g_year_month003_2042_g_year_month003_2042_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=1999-10-05:00
    """
    assert_bindings(
        schema="msData/datatypes/gYearMonth.xsd",
        instance="msData/datatypes/gYearMonth003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_g_year_month002_2041_g_year_month002_2041_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=1999-10
    """
    assert_bindings(
        schema="msData/datatypes/gYearMonth.xsd",
        instance="msData/datatypes/gYearMonth002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_date010_2038_date010_2038_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=2000-10-05-05:00
    """
    assert_bindings(
        schema="msData/datatypes/date.xsd",
        instance="msData/datatypes/date010.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_date005_2035_date005_2035_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=2000-02-29
    """
    assert_bindings(
        schema="msData/datatypes/date.xsd",
        instance="msData/datatypes/date005.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_date002_2032_date002_2032_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=1999-05-31
    """
    assert_bindings(
        schema="msData/datatypes/date.xsd",
        instance="msData/datatypes/date002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_time013_2021_time013_2021_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=13:20:00.34
    """
    assert_bindings(
        schema="msData/datatypes/time.xsd",
        instance="msData/datatypes/time013.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_time012_2020_time012_2020_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=13:20:00
    """
    assert_bindings(
        schema="msData/datatypes/time.xsd",
        instance="msData/datatypes/time012.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_time011_2019_time011_2019_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=13:20:00Z
    """
    assert_bindings(
        schema="msData/datatypes/time.xsd",
        instance="msData/datatypes/time011.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_time009_2018_time009_2018_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=13:20:00+05:59
    """
    assert_bindings(
        schema="msData/datatypes/time.xsd",
        instance="msData/datatypes/time009.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_time008_2017_time008_2017_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=13:20:00-05:59
    """
    assert_bindings(
        schema="msData/datatypes/time.xsd",
        instance="msData/datatypes/time008.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_time007_2016_time007_2016_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=13:20:00+05:00
    """
    assert_bindings(
        schema="msData/datatypes/time.xsd",
        instance="msData/datatypes/time007.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_time006_2015_time006_2015_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=13:20:00-05:00
    """
    assert_bindings(
        schema="msData/datatypes/time.xsd",
        instance="msData/datatypes/time006.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_time005_2014_time005_2014_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=13:20:00+05:00
    """
    assert_bindings(
        schema="msData/datatypes/time.xsd",
        instance="msData/datatypes/time005.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_time004_2013_time004_2013_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=13:20:00-05:00
    """
    assert_bindings(
        schema="msData/datatypes/time.xsd",
        instance="msData/datatypes/time004.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_date_time011_2008_date_time011_2008_i(mode, save_output):
    """
    TEST :Facet Schemas for string : value=0000-01-01T00:00:00 Year zero
    is allowed in dates in XSD 1.1 - MHK
    """
    assert_bindings(
        schema="msData/datatypes/dateTime.xsd",
        instance="msData/datatypes/dateTime011.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_date_time010_2007_date_time010_2007_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=1999-05-31T13:20:00Z
    """
    assert_bindings(
        schema="msData/datatypes/dateTime.xsd",
        instance="msData/datatypes/dateTime010.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_date_time008_2006_date_time008_2006_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=1999-05-31T13:20:00-5:45
    """
    assert_bindings(
        schema="msData/datatypes/dateTime.xsd",
        instance="msData/datatypes/dateTime008.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_date_time007_2005_date_time007_2005_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=1999-05-31T13:20:00+5:45
    """
    assert_bindings(
        schema="msData/datatypes/dateTime.xsd",
        instance="msData/datatypes/dateTime007.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_date_time006_2004_date_time006_2004_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=1999-05-31T13:20:00+05:00
    """
    assert_bindings(
        schema="msData/datatypes/dateTime.xsd",
        instance="msData/datatypes/dateTime006.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_date_time005_2003_date_time005_2003_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=1999-05-31T13:20:00-05:00
    """
    assert_bindings(
        schema="msData/datatypes/dateTime.xsd",
        instance="msData/datatypes/dateTime005.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_date_time003_2001_date_time003_2001_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=1985-04-12T10:30:00
    """
    assert_bindings(
        schema="msData/datatypes/dateTime.xsd",
        instance="msData/datatypes/dateTime003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_date_time002_2000_date_time002_2000_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=1999-05-31T13:20:00-05:00
    """
    assert_bindings(
        schema="msData/datatypes/dateTime.xsd",
        instance="msData/datatypes/dateTime002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_duration027_1995_duration027_1995_v(mode, save_output):
    """
    TEST :Facet Schemas for string : Test for simpleType of duration
    """
    assert_bindings(
        schema="msData/datatypes/duration027.xsd",
        instance="msData/datatypes/duration027.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_duration026_1994_duration026_1994_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=P2000Y2M29DT10H30M
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration026.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_duration025_1993_duration025_1993_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=P1Y2M15DT11H60M
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration025.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_duration024_1992_duration024_1992_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=P1Y2M15DT25H30M
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration024.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_duration023_1991_duration023_1991_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=P1Y2M32DT12H30M
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration023.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_duration022_1990_duration022_1990_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=P1Y13M15DT12H30M
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration022.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_duration020_1988_duration020_1988_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=P0Y0M0DT0H0M0.0001S
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration020.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_duration019_1987_duration019_1987_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=P0Y0M0D
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration019.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_duration018_1986_duration018_1986_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=PT31S
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration018.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_duration017_1985_duration017_1985_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=PT31M
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration017.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_duration016_1984_duration016_1984_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=PT31H
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration016.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_duration014_1982_duration014_1982_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=P0Y0M3D
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration014.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_duration012_1980_duration012_1980_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=PT2153.5S
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration012.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_duration009_1977_duration009_1977_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-P1347M
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration009.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_duration007_1975_duration007_1975_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=P0Y1347M0D
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration007.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_duration006_1974_duration006_1974_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=P0Y1347M
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration006.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_duration005_1973_duration005_1973_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=P1Y2MT2H
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration005.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_duration004_1972_duration004_1972_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=P1347M
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration004.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_duration003_1971_duration003_1971_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=P1347Y
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_duration002_1970_duration002_1970_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=P1Y2M3DT10H30M
    """
    assert_bindings(
        schema="msData/datatypes/duration.xsd",
        instance="msData/datatypes/duration002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_double030_1968_double030_1968_v(mode, save_output):
    """
    TEST :Facet Schemas for string : all valid double values
    """
    assert_bindings(
        schema="msData/datatypes/double030.xsd",
        instance="msData/datatypes/double030.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_double028_1966_double028_1966_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=2.22e-308
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double028.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_double027_1965_double027_1965_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=8.98e307
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double027.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_double021_1959_double021_1959_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=NaN
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double021.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_double020_1958_double020_1958_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-INF
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double020.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_double019_1957_double019_1957_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=INF
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double019.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_double018_1956_double018_1956_i(mode, save_output):
    """
    TEST :Facet Schemas for string : value=+INF Becomes valid in XSD 1.1 -
    MHK
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double018.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_double017_1955_double017_1955_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-1E4
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double017.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_double014_1952_double014_1952_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=+1
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double014.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_double013_1951_double013_1951_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=1
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double013.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_double012_1950_double012_1950_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-1
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double012.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_double011_1949_double011_1949_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-1.0
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double011.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_double010_1948_double010_1948_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-0.0
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double010.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_double009_1947_double009_1947_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=+0.0
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double009.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_double008_1946_double008_1946_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-0
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double008.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_double007_1945_double007_1945_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=+0
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double007.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_double006_1944_double006_1944_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=3.14159
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double006.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_double005_1943_double005_1943_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-3.14159
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double005.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_double004_1942_double004_1942_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=1e2
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double004.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_double003_1941_double003_1941_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=1E2
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_double002_1940_double002_1940_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=1.0
    """
    assert_bindings(
        schema="msData/datatypes/double.xsd",
        instance="msData/datatypes/double002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_float039_1938_float039_1938_v(mode, save_output):
    """
    TEST :Facet Schemas for string : all valid float values
    """
    assert_bindings(
        schema="msData/datatypes/float039.xsd",
        instance="msData/datatypes/float039.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_float038_1937_float038_1937_v(mode, save_output):
    """
    TEST :Facet Schemas for string : Test for simpleType of float
    """
    assert_bindings(
        schema="msData/datatypes/float038.xsd",
        instance="msData/datatypes/float038.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_float034_1933_float034_1933_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=00.00
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float034.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_float033_1932_float033_1932_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=021.22
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float033.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_float032_1931_float032_1931_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=00.121
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float032.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_float031_1930_float031_1930_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=3.4e38
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float031.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_float030_1929_float030_1929_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=2.3e-38
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float030.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_float029_1928_float029_1928_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=12.78E-2
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float029.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_float028_1927_float028_1927_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=1267.43233E12
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float028.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_float021_1920_float021_1920_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=NaN
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float021.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_float020_1919_float020_1919_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-INF
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float020.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_float019_1918_float019_1918_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=INF
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float019.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_float018_1917_float018_1917_i(mode, save_output):
    """
    TEST :Facet Schemas for string : value=+INF Becomes valid in XSD 1.1 -
    MHK
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float018.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_float017_1916_float017_1916_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-1E4
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float017.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_float014_1913_float014_1913_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=+1
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float014.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_float013_1912_float013_1912_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=1
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float013.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_float012_1911_float012_1911_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-1
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float012.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_float011_1910_float011_1910_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-1.0
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float011.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_float010_1909_float010_1909_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-0.0
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float010.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_float009_1908_float009_1908_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=+0.0
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float009.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_float008_1907_float008_1907_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-0
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float008.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_float007_1906_float007_1906_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=+0
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float007.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_float006_1905_float006_1905_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=3.14159
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float006.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_float005_1904_float005_1904_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-3.14159
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float005.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_float004_1903_float004_1903_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=1e2
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float004.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_float003_1902_float003_1902_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=1E2
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_float002_1901_float002_1901_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=1.0
    """
    assert_bindings(
        schema="msData/datatypes/float.xsd",
        instance="msData/datatypes/float002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_decimal016_1890_decimal016_1890_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=12345678901234567890123456789
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal016.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_decimal015_1889_decimal015_1889_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=9876543210987654321098765432
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal015.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_decimal014_1888_decimal014_1888_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=987654321098765432
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal014.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_decimal013_1887_decimal013_1887_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=100000.00
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal013.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_decimal012_1886_decimal012_1886_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=12678967.543233
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal012.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_decimal011_1885_decimal011_1885_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=+1
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal011.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_decimal010_1884_decimal010_1884_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=1
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal010.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_decimal009_1883_decimal009_1883_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-1
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal009.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_decimal008_1882_decimal008_1882_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-1.0
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal008.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_decimal007_1881_decimal007_1881_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-0.0
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal007.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_decimal006_1880_decimal006_1880_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=+0.0
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal006.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_decimal005_1879_decimal005_1879_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-0
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal005.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_decimal004_1878_decimal004_1878_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=+0
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal004.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_decimal003_1877_decimal003_1877_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=3.14159
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_decimal002_1876_decimal002_1876_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=-3.14159
    """
    assert_bindings(
        schema="msData/datatypes/decimal.xsd",
        instance="msData/datatypes/decimal002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_boolean018_1874_boolean018_1874_v(mode, save_output):
    """
    TEST :Facet Schemas for string : Test simpleType list with boolean
    """
    assert_bindings(
        schema="msData/datatypes/boolean018.xsd",
        instance="msData/datatypes/boolean018.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_boolean005_1861_boolean005_1861_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=0
    """
    assert_bindings(
        schema="msData/datatypes/boolean.xsd",
        instance="msData/datatypes/boolean005.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_boolean004_1860_boolean004_1860_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=false
    """
    assert_bindings(
        schema="msData/datatypes/boolean.xsd",
        instance="msData/datatypes/boolean004.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_boolean003_1859_boolean003_1859_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=1
    """
    assert_bindings(
        schema="msData/datatypes/boolean.xsd",
        instance="msData/datatypes/boolean003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_boolean002_1858_boolean002_1858_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=true
    """
    assert_bindings(
        schema="msData/datatypes/boolean.xsd",
        instance="msData/datatypes/boolean002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_string006_1856_string006_1856_v(mode, save_output):
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
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_string005_1855_string005_1855_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=#x20 | #xD | #xA | [a-zA-Z0-9]
    | [-'()+,./:=?;!*#@$_%]
    """
    assert_bindings(
        schema="msData/datatypes/string.xsd",
        instance="msData/datatypes/string005.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_string004_1854_string004_1854_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=sdflhksdgh;let vm'peoaivm'weiv'
    """
    assert_bindings(
        schema="msData/datatypes/string.xsd",
        instance="msData/datatypes/string004.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_string003_1853_string003_1853_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=!$%%*))*(
    """
    assert_bindings(
        schema="msData/datatypes/string.xsd",
        instance="msData/datatypes/string003.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_string002_1852_string002_1852_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=a_?>
    """
    assert_bindings(
        schema="msData/datatypes/string.xsd",
        instance="msData/datatypes/string002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_string001_1851_string001_1851_v(mode, save_output):
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/string.xsd",
        instance="msData/datatypes/string001.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_positive_integer_total_digits003_1849_positive_integer_total_digits003_1849_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=4 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_totalDigits003.xsd",
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_totalDigits003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_positive_integer_total_digits002_1848_positive_integer_total_digits002_1848_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=3 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_totalDigits002.xsd",
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_totalDigits002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_positive_integer_min_exclusive005_1846_positive_integer_min_exclusive005_1846_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_minExclusive005.xsd",
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_minExclusive005.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_positive_integer_min_exclusive004_1845_positive_integer_min_exclusive004_1845_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_minExclusive004.xsd",
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_minExclusive004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_positive_integer_min_exclusive003_1844_positive_integer_min_exclusive003_1844_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_minExclusive003.xsd",
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_minExclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_positive_integer_min_inclusive005_1841_positive_integer_min_inclusive005_1841_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_minInclusive005.xsd",
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_minInclusive005.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_positive_integer_min_inclusive004_1840_positive_integer_min_inclusive004_1840_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_minInclusive004.xsd",
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_minInclusive004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_positive_integer_min_inclusive003_1839_positive_integer_min_inclusive003_1839_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_minInclusive003.xsd",
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_minInclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_positive_integer_min_inclusive001_1837_positive_integer_min_inclusive001_1837_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_minInclusive001.xsd",
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_minInclusive001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_positive_integer_max_exclusive003_1836_positive_integer_max_exclusive003_1836_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_maxExclusive003.xsd",
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_maxExclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_positive_integer_max_inclusive003_1833_positive_integer_max_inclusive003_1833_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_maxInclusive003.xsd",
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_maxInclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_positive_integer_max_inclusive001_1831_positive_integer_max_inclusive001_1831_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_maxInclusive001.xsd",
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_maxInclusive001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_positive_integer_enumeration004_1830_positive_integer_enumeration004_1830_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=567 1 234
    and document value=567
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_enumeration004.xsd",
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_enumeration004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_positive_integer_enumeration002_1828_positive_integer_enumeration002_1828_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=567 and
    document value=567
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_enumeration002.xsd",
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_enumeration002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_positive_integer_pattern001_1826_positive_integer_pattern001_1826_v(mode, save_output):
    r"""
    TEST :Facet Schemas for string : facet=pattern and value=\p{Nd}{1,3}
    and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_pattern001.xsd",
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_pattern001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_byte_total_digits003_1825_unsigned_byte_total_digits003_1825_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=4 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_totalDigits003.xsd",
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_totalDigits003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_byte_total_digits002_1824_unsigned_byte_total_digits002_1824_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=3 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_totalDigits002.xsd",
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_totalDigits002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_byte_min_exclusive005_1822_unsigned_byte_min_exclusive005_1822_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_minExclusive005.xsd",
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_minExclusive005.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_byte_min_exclusive004_1821_unsigned_byte_min_exclusive004_1821_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_minExclusive004.xsd",
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_minExclusive004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_byte_min_exclusive003_1820_unsigned_byte_min_exclusive003_1820_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_minExclusive003.xsd",
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_minExclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_byte_min_inclusive005_1817_unsigned_byte_min_inclusive005_1817_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_minInclusive005.xsd",
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_minInclusive005.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_byte_min_inclusive004_1816_unsigned_byte_min_inclusive004_1816_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_minInclusive004.xsd",
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_minInclusive004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_byte_min_inclusive003_1815_unsigned_byte_min_inclusive003_1815_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_minInclusive003.xsd",
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_minInclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_byte_min_inclusive001_1813_unsigned_byte_min_inclusive001_1813_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_minInclusive001.xsd",
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_minInclusive001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_byte_max_exclusive003_1812_unsigned_byte_max_exclusive003_1812_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_maxExclusive003.xsd",
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_maxExclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_byte_max_inclusive003_1809_unsigned_byte_max_inclusive003_1809_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_maxInclusive003.xsd",
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_maxInclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_byte_max_inclusive001_1807_unsigned_byte_max_inclusive001_1807_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_maxInclusive001.xsd",
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_maxInclusive001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_byte_enumeration004_1806_unsigned_byte_enumeration004_1806_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 1 234
    and document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_enumeration004.xsd",
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_enumeration004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_byte_enumeration002_1804_unsigned_byte_enumeration002_1804_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 and
    document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_enumeration002.xsd",
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_enumeration002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_byte_pattern001_1802_unsigned_byte_pattern001_1802_v(mode, save_output):
    r"""
    TEST :Facet Schemas for string : facet=pattern and value=\p{Nd}{1,3}
    and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_pattern001.xsd",
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_pattern001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_short_total_digits003_1801_unsigned_short_total_digits003_1801_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=4 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_totalDigits003.xsd",
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_totalDigits003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_short_total_digits002_1800_unsigned_short_total_digits002_1800_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=3 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_totalDigits002.xsd",
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_totalDigits002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_short_min_exclusive005_1798_unsigned_short_min_exclusive005_1798_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_minExclusive005.xsd",
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_minExclusive005.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_short_min_exclusive004_1797_unsigned_short_min_exclusive004_1797_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_minExclusive004.xsd",
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_minExclusive004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_short_min_exclusive003_1796_unsigned_short_min_exclusive003_1796_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_minExclusive003.xsd",
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_minExclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_short_min_inclusive005_1793_unsigned_short_min_inclusive005_1793_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_minInclusive005.xsd",
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_minInclusive005.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_short_min_inclusive004_1792_unsigned_short_min_inclusive004_1792_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_minInclusive004.xsd",
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_minInclusive004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_short_min_inclusive003_1791_unsigned_short_min_inclusive003_1791_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_minInclusive003.xsd",
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_minInclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_short_min_inclusive001_1789_unsigned_short_min_inclusive001_1789_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_minInclusive001.xsd",
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_minInclusive001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_short_max_exclusive003_1788_unsigned_short_max_exclusive003_1788_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_maxExclusive003.xsd",
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_maxExclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_short_max_inclusive003_1785_unsigned_short_max_inclusive003_1785_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_maxInclusive003.xsd",
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_maxInclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_short_max_inclusive001_1783_unsigned_short_max_inclusive001_1783_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_maxInclusive001.xsd",
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_maxInclusive001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_short_enumeration004_1782_unsigned_short_enumeration004_1782_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 1 234
    and document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_enumeration004.xsd",
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_enumeration004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_short_enumeration002_1780_unsigned_short_enumeration002_1780_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 and
    document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_enumeration002.xsd",
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_enumeration002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_short_pattern001_1778_unsigned_short_pattern001_1778_v(mode, save_output):
    r"""
    TEST :Facet Schemas for string : facet=pattern and value=\p{Nd}{1,3}
    and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_pattern001.xsd",
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_pattern001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_int_total_digits003_1777_unsigned_int_total_digits003_1777_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=4 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_totalDigits003.xsd",
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_totalDigits003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_int_total_digits002_1776_unsigned_int_total_digits002_1776_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=3 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_totalDigits002.xsd",
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_totalDigits002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_int_min_exclusive005_1774_unsigned_int_min_exclusive005_1774_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_minExclusive005.xsd",
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_minExclusive005.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_int_min_exclusive004_1773_unsigned_int_min_exclusive004_1773_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_minExclusive004.xsd",
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_minExclusive004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_int_min_exclusive003_1772_unsigned_int_min_exclusive003_1772_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_minExclusive003.xsd",
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_minExclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_int_min_inclusive005_1769_unsigned_int_min_inclusive005_1769_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_minInclusive005.xsd",
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_minInclusive005.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_int_min_inclusive004_1768_unsigned_int_min_inclusive004_1768_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_minInclusive004.xsd",
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_minInclusive004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_int_min_inclusive003_1767_unsigned_int_min_inclusive003_1767_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_minInclusive003.xsd",
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_minInclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_int_min_inclusive001_1765_unsigned_int_min_inclusive001_1765_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_minInclusive001.xsd",
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_minInclusive001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_int_max_exclusive003_1764_unsigned_int_max_exclusive003_1764_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_maxExclusive003.xsd",
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_maxExclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_int_max_inclusive003_1761_unsigned_int_max_inclusive003_1761_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_maxInclusive003.xsd",
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_maxInclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_int_max_inclusive001_1759_unsigned_int_max_inclusive001_1759_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_maxInclusive001.xsd",
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_maxInclusive001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_int_enumeration004_1758_unsigned_int_enumeration004_1758_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 1 234
    and document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_enumeration004.xsd",
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_enumeration004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_int_enumeration002_1756_unsigned_int_enumeration002_1756_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 and
    document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_enumeration002.xsd",
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_enumeration002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_int_pattern001_1754_unsigned_int_pattern001_1754_v(mode, save_output):
    r"""
    TEST :Facet Schemas for string : facet=pattern and value=\p{Nd}{1,3}
    and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_pattern001.xsd",
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_pattern001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_long_total_digits003_1753_unsigned_long_total_digits003_1753_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=4 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_totalDigits003.xsd",
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_totalDigits003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_long_total_digits002_1752_unsigned_long_total_digits002_1752_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=3 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_totalDigits002.xsd",
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_totalDigits002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_long_min_exclusive005_1750_unsigned_long_min_exclusive005_1750_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_minExclusive005.xsd",
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_minExclusive005.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_long_min_exclusive004_1749_unsigned_long_min_exclusive004_1749_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_minExclusive004.xsd",
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_minExclusive004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_long_min_exclusive003_1748_unsigned_long_min_exclusive003_1748_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_minExclusive003.xsd",
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_minExclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_long_min_inclusive005_1745_unsigned_long_min_inclusive005_1745_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_minInclusive005.xsd",
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_minInclusive005.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_long_min_inclusive004_1744_unsigned_long_min_inclusive004_1744_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_minInclusive004.xsd",
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_minInclusive004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_long_min_inclusive003_1743_unsigned_long_min_inclusive003_1743_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_minInclusive003.xsd",
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_minInclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_long_min_inclusive001_1741_unsigned_long_min_inclusive001_1741_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_minInclusive001.xsd",
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_minInclusive001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_long_max_exclusive003_1740_unsigned_long_max_exclusive003_1740_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_maxExclusive003.xsd",
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_maxExclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_long_max_inclusive003_1737_unsigned_long_max_inclusive003_1737_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_maxInclusive003.xsd",
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_maxInclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_long_max_inclusive001_1735_unsigned_long_max_inclusive001_1735_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_maxInclusive001.xsd",
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_maxInclusive001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_long_enumeration004_1734_unsigned_long_enumeration004_1734_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 1 234
    and document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_enumeration004.xsd",
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_enumeration004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_long_enumeration002_1732_unsigned_long_enumeration002_1732_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 and
    document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_enumeration002.xsd",
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_enumeration002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_unsigned_long_pattern001_1730_unsigned_long_pattern001_1730_v(mode, save_output):
    r"""
    TEST :Facet Schemas for string : facet=pattern and value=\p{Nd}{1,3}
    and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_pattern001.xsd",
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_pattern001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_negative_integer_total_digits003_1729_non_negative_integer_total_digits003_1729_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=4 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_totalDigits003.xsd",
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_totalDigits003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_negative_integer_total_digits002_1728_non_negative_integer_total_digits002_1728_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=3 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_totalDigits002.xsd",
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_totalDigits002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_negative_integer_min_exclusive005_1726_non_negative_integer_min_exclusive005_1726_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minExclusive005.xsd",
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minExclusive005.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_negative_integer_min_exclusive004_1725_non_negative_integer_min_exclusive004_1725_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minExclusive004.xsd",
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minExclusive004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_negative_integer_min_exclusive003_1724_non_negative_integer_min_exclusive003_1724_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minExclusive003.xsd",
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minExclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_negative_integer_min_inclusive005_1721_non_negative_integer_min_inclusive005_1721_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minInclusive005.xsd",
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minInclusive005.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_negative_integer_min_inclusive004_1720_non_negative_integer_min_inclusive004_1720_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minInclusive004.xsd",
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minInclusive004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_negative_integer_min_inclusive003_1719_non_negative_integer_min_inclusive003_1719_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minInclusive003.xsd",
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minInclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_negative_integer_min_inclusive001_1717_non_negative_integer_min_inclusive001_1717_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minInclusive001.xsd",
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minInclusive001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_negative_integer_max_exclusive003_1716_non_negative_integer_max_exclusive003_1716_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_maxExclusive003.xsd",
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_maxExclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_negative_integer_max_inclusive003_1713_non_negative_integer_max_inclusive003_1713_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_maxInclusive003.xsd",
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_maxInclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_negative_integer_max_inclusive001_1711_non_negative_integer_max_inclusive001_1711_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_maxInclusive001.xsd",
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_maxInclusive001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_negative_integer_enumeration004_1710_non_negative_integer_enumeration004_1710_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=456 789 0
    and document value=456
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_enumeration004.xsd",
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_enumeration004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_negative_integer_enumeration002_1708_non_negative_integer_enumeration002_1708_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=456 and
    document value=456
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_enumeration002.xsd",
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_enumeration002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_negative_integer_pattern001_1706_non_negative_integer_pattern001_1706_v(mode, save_output):
    r"""
    TEST :Facet Schemas for string : facet=pattern and value=\p{Nd}{1,3}
    and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_pattern001.xsd",
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_pattern001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_byte_total_digits003_1705_byte_total_digits003_1705_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=4 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_totalDigits003.xsd",
        instance="msData/datatypes/Facets/byte/byte_totalDigits003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_byte_total_digits002_1704_byte_total_digits002_1704_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=3 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_totalDigits002.xsd",
        instance="msData/datatypes/Facets/byte/byte_totalDigits002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_byte_min_exclusive005_1702_byte_min_exclusive005_1702_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_minExclusive005.xsd",
        instance="msData/datatypes/Facets/byte/byte_minExclusive005.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_byte_min_exclusive004_1701_byte_min_exclusive004_1701_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_minExclusive004.xsd",
        instance="msData/datatypes/Facets/byte/byte_minExclusive004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_byte_min_exclusive003_1700_byte_min_exclusive003_1700_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_minExclusive003.xsd",
        instance="msData/datatypes/Facets/byte/byte_minExclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_byte_min_inclusive005_1697_byte_min_inclusive005_1697_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_minInclusive005.xsd",
        instance="msData/datatypes/Facets/byte/byte_minInclusive005.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_byte_min_inclusive004_1696_byte_min_inclusive004_1696_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_minInclusive004.xsd",
        instance="msData/datatypes/Facets/byte/byte_minInclusive004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_byte_min_inclusive003_1695_byte_min_inclusive003_1695_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_minInclusive003.xsd",
        instance="msData/datatypes/Facets/byte/byte_minInclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_byte_min_inclusive001_1693_byte_min_inclusive001_1693_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_minInclusive001.xsd",
        instance="msData/datatypes/Facets/byte/byte_minInclusive001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_byte_max_exclusive003_1692_byte_max_exclusive003_1692_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_maxExclusive003.xsd",
        instance="msData/datatypes/Facets/byte/byte_maxExclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_byte_max_inclusive003_1689_byte_max_inclusive003_1689_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_maxInclusive003.xsd",
        instance="msData/datatypes/Facets/byte/byte_maxInclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_byte_max_inclusive001_1687_byte_max_inclusive001_1687_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_maxInclusive001.xsd",
        instance="msData/datatypes/Facets/byte/byte_maxInclusive001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_byte_enumeration004_1686_byte_enumeration004_1686_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=-1 0 1
    and document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_enumeration004.xsd",
        instance="msData/datatypes/Facets/byte/byte_enumeration004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_byte_enumeration002_1684_byte_enumeration002_1684_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 and
    document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_enumeration002.xsd",
        instance="msData/datatypes/Facets/byte/byte_enumeration002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_byte_pattern001_1682_byte_pattern001_1682_v(mode, save_output):
    r"""
    TEST :Facet Schemas for string : facet=pattern and value=\p{Nd}{1,3}
    and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_pattern001.xsd",
        instance="msData/datatypes/Facets/byte/byte_pattern001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_short_total_digits003_1681_short_total_digits003_1681_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=4 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_totalDigits003.xsd",
        instance="msData/datatypes/Facets/short/short_totalDigits003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_short_total_digits002_1680_short_total_digits002_1680_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=3 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_totalDigits002.xsd",
        instance="msData/datatypes/Facets/short/short_totalDigits002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_short_min_exclusive005_1678_short_min_exclusive005_1678_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_minExclusive005.xsd",
        instance="msData/datatypes/Facets/short/short_minExclusive005.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_short_min_exclusive004_1677_short_min_exclusive004_1677_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_minExclusive004.xsd",
        instance="msData/datatypes/Facets/short/short_minExclusive004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_short_min_exclusive003_1676_short_min_exclusive003_1676_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_minExclusive003.xsd",
        instance="msData/datatypes/Facets/short/short_minExclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_short_min_inclusive005_1673_short_min_inclusive005_1673_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_minInclusive005.xsd",
        instance="msData/datatypes/Facets/short/short_minInclusive005.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_short_min_inclusive004_1672_short_min_inclusive004_1672_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_minInclusive004.xsd",
        instance="msData/datatypes/Facets/short/short_minInclusive004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_short_min_inclusive003_1671_short_min_inclusive003_1671_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_minInclusive003.xsd",
        instance="msData/datatypes/Facets/short/short_minInclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_short_min_inclusive001_1669_short_min_inclusive001_1669_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_minInclusive001.xsd",
        instance="msData/datatypes/Facets/short/short_minInclusive001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_short_max_exclusive003_1668_short_max_exclusive003_1668_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_maxExclusive003.xsd",
        instance="msData/datatypes/Facets/short/short_maxExclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_short_max_inclusive003_1665_short_max_inclusive003_1665_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_maxInclusive003.xsd",
        instance="msData/datatypes/Facets/short/short_maxInclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_short_max_inclusive001_1663_short_max_inclusive001_1663_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_maxInclusive001.xsd",
        instance="msData/datatypes/Facets/short/short_maxInclusive001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_short_enumeration004_1662_short_enumeration004_1662_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=-1 0 1
    and document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_enumeration004.xsd",
        instance="msData/datatypes/Facets/short/short_enumeration004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_short_enumeration002_1660_short_enumeration002_1660_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 and
    document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_enumeration002.xsd",
        instance="msData/datatypes/Facets/short/short_enumeration002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_short_pattern001_1658_short_pattern001_1658_v(mode, save_output):
    r"""
    TEST :Facet Schemas for string : facet=pattern and value=\p{Nd}{1,3}
    and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_pattern001.xsd",
        instance="msData/datatypes/Facets/short/short_pattern001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_int_total_digits003_1656_int_total_digits003_1656_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=4 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_totalDigits003.xsd",
        instance="msData/datatypes/Facets/int/int_totalDigits003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_int_total_digits002_1655_int_total_digits002_1655_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=3 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_totalDigits002.xsd",
        instance="msData/datatypes/Facets/int/int_totalDigits002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_int_min_exclusive005_1653_int_min_exclusive005_1653_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_minExclusive005.xsd",
        instance="msData/datatypes/Facets/int/int_minExclusive005.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_int_min_exclusive004_1652_int_min_exclusive004_1652_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_minExclusive004.xsd",
        instance="msData/datatypes/Facets/int/int_minExclusive004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_int_min_exclusive003_1651_int_min_exclusive003_1651_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_minExclusive003.xsd",
        instance="msData/datatypes/Facets/int/int_minExclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_int_min_inclusive005_1648_int_min_inclusive005_1648_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_minInclusive005.xsd",
        instance="msData/datatypes/Facets/int/int_minInclusive005.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_int_min_inclusive004_1647_int_min_inclusive004_1647_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_minInclusive004.xsd",
        instance="msData/datatypes/Facets/int/int_minInclusive004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_int_min_inclusive003_1646_int_min_inclusive003_1646_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_minInclusive003.xsd",
        instance="msData/datatypes/Facets/int/int_minInclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_int_min_inclusive001_1644_int_min_inclusive001_1644_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_minInclusive001.xsd",
        instance="msData/datatypes/Facets/int/int_minInclusive001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_int_max_exclusive003_1643_int_max_exclusive003_1643_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_maxExclusive003.xsd",
        instance="msData/datatypes/Facets/int/int_maxExclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_int_max_inclusive003_1640_int_max_inclusive003_1640_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_maxInclusive003.xsd",
        instance="msData/datatypes/Facets/int/int_maxInclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_int_max_inclusive001_1638_int_max_inclusive001_1638_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_maxInclusive001.xsd",
        instance="msData/datatypes/Facets/int/int_maxInclusive001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_int_enumeration004_1637_int_enumeration004_1637_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=-1 0 1
    and document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_enumeration004.xsd",
        instance="msData/datatypes/Facets/int/int_enumeration004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_int_enumeration002_1635_int_enumeration002_1635_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 and
    document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_enumeration002.xsd",
        instance="msData/datatypes/Facets/int/int_enumeration002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_int_pattern001_1633_int_pattern001_1633_v(mode, save_output):
    r"""
    TEST :Facet Schemas for string : facet=pattern and value=\p{Nd}{1,3}
    and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_pattern001.xsd",
        instance="msData/datatypes/Facets/int/int_pattern001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_long_total_digits003_1632_long_total_digits003_1632_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=4 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_totalDigits003.xsd",
        instance="msData/datatypes/Facets/long/long_totalDigits003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_long_total_digits002_1631_long_total_digits002_1631_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=3 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_totalDigits002.xsd",
        instance="msData/datatypes/Facets/long/long_totalDigits002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_long_min_exclusive005_1629_long_min_exclusive005_1629_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_minExclusive005.xsd",
        instance="msData/datatypes/Facets/long/long_minExclusive005.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_long_min_exclusive004_1628_long_min_exclusive004_1628_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_minExclusive004.xsd",
        instance="msData/datatypes/Facets/long/long_minExclusive004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_long_min_exclusive003_1627_long_min_exclusive003_1627_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_minExclusive003.xsd",
        instance="msData/datatypes/Facets/long/long_minExclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_long_min_inclusive005_1624_long_min_inclusive005_1624_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_minInclusive005.xsd",
        instance="msData/datatypes/Facets/long/long_minInclusive005.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_long_min_inclusive004_1623_long_min_inclusive004_1623_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_minInclusive004.xsd",
        instance="msData/datatypes/Facets/long/long_minInclusive004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_long_min_inclusive003_1622_long_min_inclusive003_1622_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_minInclusive003.xsd",
        instance="msData/datatypes/Facets/long/long_minInclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_long_min_inclusive001_1620_long_min_inclusive001_1620_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_minInclusive001.xsd",
        instance="msData/datatypes/Facets/long/long_minInclusive001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_long_max_exclusive003_1619_long_max_exclusive003_1619_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_maxExclusive003.xsd",
        instance="msData/datatypes/Facets/long/long_maxExclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_long_max_inclusive003_1616_long_max_inclusive003_1616_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_maxInclusive003.xsd",
        instance="msData/datatypes/Facets/long/long_maxInclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_long_max_inclusive001_1614_long_max_inclusive001_1614_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_maxInclusive001.xsd",
        instance="msData/datatypes/Facets/long/long_maxInclusive001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_long_enumeration004_1613_long_enumeration004_1613_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=-1 0 1
    and document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_enumeration004.xsd",
        instance="msData/datatypes/Facets/long/long_enumeration004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_long_enumeration002_1611_long_enumeration002_1611_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 and
    document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_enumeration002.xsd",
        instance="msData/datatypes/Facets/long/long_enumeration002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_long_pattern001_1609_long_pattern001_1609_v(mode, save_output):
    r"""
    TEST :Facet Schemas for string : facet=pattern and value=\p{Nd}{1,3}
    and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_pattern001.xsd",
        instance="msData/datatypes/Facets/long/long_pattern001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_negative_integer_total_digits003_1608_negative_integer_total_digits003_1608_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=4 and
    document value=-123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_totalDigits003.xsd",
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_totalDigits003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_negative_integer_total_digits002_1607_negative_integer_total_digits002_1607_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=3 and
    document value=-123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_totalDigits002.xsd",
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_totalDigits002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_negative_integer_min_exclusive005_1605_negative_integer_min_exclusive005_1605_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=-7 and
    facet=maxExclusive and value=-1) and document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_minExclusive005.xsd",
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_minExclusive005.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_negative_integer_min_exclusive004_1604_negative_integer_min_exclusive004_1604_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=-7 and
    facet=maxInclusive and value=-1) and document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_minExclusive004.xsd",
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_minExclusive004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_negative_integer_min_exclusive003_1603_negative_integer_min_exclusive003_1603_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=-7 and
    document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_minExclusive003.xsd",
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_minExclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_negative_integer_min_inclusive005_1600_negative_integer_min_inclusive005_1600_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=-7 and
    facet=maxExclusive and value=-1) and document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_minInclusive005.xsd",
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_minInclusive005.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_negative_integer_min_inclusive004_1599_negative_integer_min_inclusive004_1599_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=-7 and
    facet=maxInclusive and value=-1) and document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_minInclusive004.xsd",
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_minInclusive004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_negative_integer_min_inclusive003_1598_negative_integer_min_inclusive003_1598_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=-7 and
    document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_minInclusive003.xsd",
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_minInclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_negative_integer_min_inclusive001_1596_negative_integer_min_inclusive001_1596_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=-7 and
    document value=-7
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_minInclusive001.xsd",
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_minInclusive001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_negative_integer_max_exclusive003_1595_negative_integer_max_exclusive003_1595_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=-1 and
    document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_maxExclusive003.xsd",
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_maxExclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_negative_integer_max_inclusive003_1592_negative_integer_max_inclusive003_1592_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=-1 and
    document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_maxInclusive003.xsd",
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_maxInclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_negative_integer_max_inclusive001_1590_negative_integer_max_inclusive001_1590_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=-7 and
    document value=-7
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_maxInclusive001.xsd",
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_maxInclusive001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_negative_integer_enumeration004_1589_negative_integer_enumeration004_1589_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=-456 -789
    -1 and document value=-456
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_enumeration004.xsd",
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_enumeration004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_negative_integer_enumeration002_1587_negative_integer_enumeration002_1587_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=-456 and
    document value=-456
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_enumeration002.xsd",
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_enumeration002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_negative_integer_pattern001_1585_negative_integer_pattern001_1585_v(mode, save_output):
    r"""
    TEST :Facet Schemas for string : facet=pattern and value=-\p{Nd}{1,3}
    and document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_pattern001.xsd",
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_pattern001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_positive_integer_total_digits003_1584_non_positive_integer_total_digits003_1584_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=4 and
    document value=-123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_totalDigits003.xsd",
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_totalDigits003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_positive_integer_total_digits002_1583_non_positive_integer_total_digits002_1583_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=3 and
    document value=-123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_totalDigits002.xsd",
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_totalDigits002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_positive_integer_min_exclusive005_1581_non_positive_integer_min_exclusive005_1581_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=-7 and
    facet=maxExclusive and value=-1) and document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minExclusive005.xsd",
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minExclusive005.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_positive_integer_min_exclusive004_1580_non_positive_integer_min_exclusive004_1580_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=-7 and
    facet=maxInclusive and value=-1) and document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minExclusive004.xsd",
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minExclusive004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_positive_integer_min_exclusive003_1579_non_positive_integer_min_exclusive003_1579_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=-7 and
    document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minExclusive003.xsd",
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minExclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_positive_integer_min_inclusive005_1576_non_positive_integer_min_inclusive005_1576_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=-7 and
    facet=maxExclusive and value=-1) and document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minInclusive005.xsd",
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minInclusive005.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_positive_integer_min_inclusive004_1575_non_positive_integer_min_inclusive004_1575_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=-7 and
    facet=maxInclusive and value=-1) and document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minInclusive004.xsd",
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minInclusive004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_positive_integer_min_inclusive003_1574_non_positive_integer_min_inclusive003_1574_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=-7 and
    document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minInclusive003.xsd",
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minInclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_positive_integer_min_inclusive001_1572_non_positive_integer_min_inclusive001_1572_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=-7 and
    document value=-7
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minInclusive001.xsd",
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minInclusive001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_positive_integer_max_exclusive003_1571_non_positive_integer_max_exclusive003_1571_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=-1 and
    document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_maxExclusive003.xsd",
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_maxExclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_positive_integer_max_inclusive003_1568_non_positive_integer_max_inclusive003_1568_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=-1 and
    document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_maxInclusive003.xsd",
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_maxInclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_positive_integer_max_inclusive001_1566_non_positive_integer_max_inclusive001_1566_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=-7 and
    document value=-7
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_maxInclusive001.xsd",
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_maxInclusive001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_positive_integer_enumeration004_1565_non_positive_integer_enumeration004_1565_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=-456 -789
    0 and document value=-456
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_enumeration004.xsd",
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_enumeration004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_positive_integer_enumeration002_1563_non_positive_integer_enumeration002_1563_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=-456 and
    document value=-456
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_enumeration002.xsd",
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_enumeration002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_non_positive_integer_pattern001_1561_non_positive_integer_pattern001_1561_v(mode, save_output):
    r"""
    TEST :Facet Schemas for string : facet=pattern and value=-\p{Nd}{1,3}
    and document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_pattern001.xsd",
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_pattern001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_integer_total_digits003_1560_integer_total_digits003_1560_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=4 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_totalDigits003.xsd",
        instance="msData/datatypes/Facets/integer/integer_totalDigits003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_integer_total_digits002_1559_integer_total_digits002_1559_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=3 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_totalDigits002.xsd",
        instance="msData/datatypes/Facets/integer/integer_totalDigits002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_integer_min_exclusive005_1557_integer_min_exclusive005_1557_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_minExclusive005.xsd",
        instance="msData/datatypes/Facets/integer/integer_minExclusive005.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_integer_min_exclusive004_1556_integer_min_exclusive004_1556_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_minExclusive004.xsd",
        instance="msData/datatypes/Facets/integer/integer_minExclusive004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_integer_min_exclusive003_1555_integer_min_exclusive003_1555_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_minExclusive003.xsd",
        instance="msData/datatypes/Facets/integer/integer_minExclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_integer_min_inclusive005_1552_integer_min_inclusive005_1552_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_minInclusive005.xsd",
        instance="msData/datatypes/Facets/integer/integer_minInclusive005.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_integer_min_inclusive004_1551_integer_min_inclusive004_1551_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_minInclusive004.xsd",
        instance="msData/datatypes/Facets/integer/integer_minInclusive004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_integer_min_inclusive003_1550_integer_min_inclusive003_1550_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_minInclusive003.xsd",
        instance="msData/datatypes/Facets/integer/integer_minInclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_integer_min_inclusive001_1548_integer_min_inclusive001_1548_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_minInclusive001.xsd",
        instance="msData/datatypes/Facets/integer/integer_minInclusive001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_integer_max_exclusive003_1547_integer_max_exclusive003_1547_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_maxExclusive003.xsd",
        instance="msData/datatypes/Facets/integer/integer_maxExclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_integer_max_inclusive003_1544_integer_max_inclusive003_1544_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_maxInclusive003.xsd",
        instance="msData/datatypes/Facets/integer/integer_maxInclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_integer_max_inclusive001_1542_integer_max_inclusive001_1542_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_maxInclusive001.xsd",
        instance="msData/datatypes/Facets/integer/integer_maxInclusive001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_integer_enumeration004_1541_integer_enumeration004_1541_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=123 456
    789 and document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_enumeration004.xsd",
        instance="msData/datatypes/Facets/integer/integer_enumeration004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_integer_enumeration002_1539_integer_enumeration002_1539_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=123 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_enumeration002.xsd",
        instance="msData/datatypes/Facets/integer/integer_enumeration002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_integer_pattern001_1537_integer_pattern001_1537_v(mode, save_output):
    r"""
    TEST :Facet Schemas for string : facet=pattern and value=\p{Nd}{1,3}
    and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_pattern001.xsd",
        instance="msData/datatypes/Facets/integer/integer_pattern001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_idref_enumeration004_1536_idref_enumeration004_1536_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    foo123 fu1 and document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREF/IDREF_enumeration004.xsd",
        instance="msData/datatypes/Facets/IDREF/IDREF_enumeration004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_idref_enumeration002_1534_idref_enumeration002_1534_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREF/IDREF_enumeration002.xsd",
        instance="msData/datatypes/Facets/IDREF/IDREF_enumeration002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_idref_pattern001_1532_idref_pattern001_1532_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=pattern and value=[a-z]{3} and
    document value=abc
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREF/IDREF_pattern001.xsd",
        instance="msData/datatypes/Facets/IDREF/IDREF_pattern001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_idref_max_length003_1531_idref_max_length003_1531_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxLength and value=6 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREF/IDREF_maxLength003.xsd",
        instance="msData/datatypes/Facets/IDREF/IDREF_maxLength003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_idref_max_length002_1530_idref_max_length002_1530_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREF/IDREF_maxLength002.xsd",
        instance="msData/datatypes/Facets/IDREF/IDREF_maxLength002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_idref_min_length004_1528_idref_min_length004_1528_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minLength and value=4 and
    facet=maxLength and value=6) and document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREF/IDREF_minLength004.xsd",
        instance="msData/datatypes/Facets/IDREF/IDREF_minLength004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_idref_min_length002_1526_idref_min_length002_1526_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREF/IDREF_minLength002.xsd",
        instance="msData/datatypes/Facets/IDREF/IDREF_minLength002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_idref_min_length001_1525_idref_min_length001_1525_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minLength and value=4 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREF/IDREF_minLength001.xsd",
        instance="msData/datatypes/Facets/IDREF/IDREF_minLength001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_idref_length002_1523_idref_length002_1523_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=length and value=5 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREF/IDREF_length002.xsd",
        instance="msData/datatypes/Facets/IDREF/IDREF_length002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_id_enumeration004_1521_id_enumeration004_1521_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    foo123 fu1 and document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/ID/ID_enumeration004.xsd",
        instance="msData/datatypes/Facets/ID/ID_enumeration004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_id_enumeration002_1519_id_enumeration002_1519_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/ID/ID_enumeration002.xsd",
        instance="msData/datatypes/Facets/ID/ID_enumeration002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_id_pattern001_1517_id_pattern001_1517_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=pattern and value=[a-z]{3} and
    document value=abc
    """
    assert_bindings(
        schema="msData/datatypes/Facets/ID/ID_pattern001.xsd",
        instance="msData/datatypes/Facets/ID/ID_pattern001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_id_max_length003_1516_id_max_length003_1516_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxLength and value=6 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/ID/ID_maxLength003.xsd",
        instance="msData/datatypes/Facets/ID/ID_maxLength003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_id_max_length002_1515_id_max_length002_1515_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/ID/ID_maxLength002.xsd",
        instance="msData/datatypes/Facets/ID/ID_maxLength002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_id_min_length004_1513_id_min_length004_1513_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minLength and value=4 and
    facet=maxLength and value=6) and document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/ID/ID_minLength004.xsd",
        instance="msData/datatypes/Facets/ID/ID_minLength004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_id_min_length002_1511_id_min_length002_1511_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/ID/ID_minLength002.xsd",
        instance="msData/datatypes/Facets/ID/ID_minLength002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_id_min_length001_1510_id_min_length001_1510_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minLength and value=4 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/ID/ID_minLength001.xsd",
        instance="msData/datatypes/Facets/ID/ID_minLength001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_id_length002_1508_id_length002_1508_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=length and value=5 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/ID/ID_length002.xsd",
        instance="msData/datatypes/Facets/ID/ID_length002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ncname_enumeration004_1506_ncname_enumeration004_1506_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    foo123 fu1 and document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NCName/NCName_enumeration004.xsd",
        instance="msData/datatypes/Facets/NCName/NCName_enumeration004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ncname_enumeration002_1504_ncname_enumeration002_1504_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NCName/NCName_enumeration002.xsd",
        instance="msData/datatypes/Facets/NCName/NCName_enumeration002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ncname_pattern001_1502_ncname_pattern001_1502_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=pattern and value=[a-z]{3} and
    document value=abc
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NCName/NCName_pattern001.xsd",
        instance="msData/datatypes/Facets/NCName/NCName_pattern001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ncname_max_length003_1501_ncname_max_length003_1501_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxLength and value=6 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NCName/NCName_maxLength003.xsd",
        instance="msData/datatypes/Facets/NCName/NCName_maxLength003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ncname_max_length002_1500_ncname_max_length002_1500_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NCName/NCName_maxLength002.xsd",
        instance="msData/datatypes/Facets/NCName/NCName_maxLength002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ncname_min_length004_1498_ncname_min_length004_1498_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minLength and value=4 and
    facet=maxLength and value=6) and document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NCName/NCName_minLength004.xsd",
        instance="msData/datatypes/Facets/NCName/NCName_minLength004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ncname_min_length002_1496_ncname_min_length002_1496_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NCName/NCName_minLength002.xsd",
        instance="msData/datatypes/Facets/NCName/NCName_minLength002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ncname_min_length001_1495_ncname_min_length001_1495_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minLength and value=4 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NCName/NCName_minLength001.xsd",
        instance="msData/datatypes/Facets/NCName/NCName_minLength001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_ncname_length002_1493_ncname_length002_1493_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=length and value=5 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NCName/NCName_length002.xsd",
        instance="msData/datatypes/Facets/NCName/NCName_length002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_name_enumeration004_1491_name_enumeration004_1491_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    foo123 fu1 and document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/Name/Name_enumeration004.xsd",
        instance="msData/datatypes/Facets/Name/Name_enumeration004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_name_enumeration002_1489_name_enumeration002_1489_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/Name/Name_enumeration002.xsd",
        instance="msData/datatypes/Facets/Name/Name_enumeration002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_name_pattern001_1487_name_pattern001_1487_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=pattern and value=[a-z]{3} and
    document value=abc
    """
    assert_bindings(
        schema="msData/datatypes/Facets/Name/Name_pattern001.xsd",
        instance="msData/datatypes/Facets/Name/Name_pattern001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_name_max_length003_1486_name_max_length003_1486_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxLength and value=6 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/Name/Name_maxLength003.xsd",
        instance="msData/datatypes/Facets/Name/Name_maxLength003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_name_max_length002_1485_name_max_length002_1485_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/Name/Name_maxLength002.xsd",
        instance="msData/datatypes/Facets/Name/Name_maxLength002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_name_min_length004_1483_name_min_length004_1483_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minLength and value=4 and
    facet=maxLength and value=6) and document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/Name/Name_minLength004.xsd",
        instance="msData/datatypes/Facets/Name/Name_minLength004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_name_min_length002_1481_name_min_length002_1481_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/Name/Name_minLength002.xsd",
        instance="msData/datatypes/Facets/Name/Name_minLength002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_name_min_length001_1480_name_min_length001_1480_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minLength and value=4 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/Name/Name_minLength001.xsd",
        instance="msData/datatypes/Facets/Name/Name_minLength001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_name_length002_1478_name_length002_1478_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=length and value=5 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/Name/Name_length002.xsd",
        instance="msData/datatypes/Facets/Name/Name_length002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_nmtokens_pattern001_1475_nmtokens_pattern001_1475_v(mode, save_output):
    """
    TEST :Facet Schemas for string : XSD: NMTOKENS, IDREFS, and ENTITIES
    now allow the pattern facet
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKENS/NMTOKENS_pattern001.xsd",
        instance="msData/datatypes/Facets/NMTOKENS/NMTOKENS_pattern001.xml",
        class_name="Foo",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_nmtokens_enumeration004_1474_nmtokens_enumeration004_1474_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    foo123 fu1 and document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKENS/NMTOKENS_enumeration004.xsd",
        instance="msData/datatypes/Facets/NMTOKENS/NMTOKENS_enumeration004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_nmtokens_enumeration002_1472_nmtokens_enumeration002_1472_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKENS/NMTOKENS_enumeration002.xsd",
        instance="msData/datatypes/Facets/NMTOKENS/NMTOKENS_enumeration002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_nmtokens_max_length003_1470_nmtokens_max_length003_1470_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxLength and value=6 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKENS/NMTOKENS_maxLength003.xsd",
        instance="msData/datatypes/Facets/NMTOKENS/NMTOKENS_maxLength003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_nmtokens_max_length002_1469_nmtokens_max_length002_1469_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKENS/NMTOKENS_maxLength002.xsd",
        instance="msData/datatypes/Facets/NMTOKENS/NMTOKENS_maxLength002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_nmtokens_min_length002_1465_nmtokens_min_length002_1465_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKENS/NMTOKENS_minLength002.xsd",
        instance="msData/datatypes/Facets/NMTOKENS/NMTOKENS_minLength002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_nmtokens_length002_1462_nmtokens_length002_1462_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=length and value=5 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKENS/NMTOKENS_length002.xsd",
        instance="msData/datatypes/Facets/NMTOKENS/NMTOKENS_length002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_nmtoken_enumeration004_1460_nmtoken_enumeration004_1460_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    foo123 fu1 and document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKEN/NMTOKEN_enumeration004.xsd",
        instance="msData/datatypes/Facets/NMTOKEN/NMTOKEN_enumeration004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_nmtoken_enumeration002_1458_nmtoken_enumeration002_1458_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKEN/NMTOKEN_enumeration002.xsd",
        instance="msData/datatypes/Facets/NMTOKEN/NMTOKEN_enumeration002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_nmtoken_pattern001_1456_nmtoken_pattern001_1456_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=pattern and value=[a-z]{3} and
    document value=abc
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKEN/NMTOKEN_pattern001.xsd",
        instance="msData/datatypes/Facets/NMTOKEN/NMTOKEN_pattern001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_nmtoken_max_length003_1455_nmtoken_max_length003_1455_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxLength and value=6 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKEN/NMTOKEN_maxLength003.xsd",
        instance="msData/datatypes/Facets/NMTOKEN/NMTOKEN_maxLength003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_nmtoken_max_length002_1454_nmtoken_max_length002_1454_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKEN/NMTOKEN_maxLength002.xsd",
        instance="msData/datatypes/Facets/NMTOKEN/NMTOKEN_maxLength002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_nmtoken_min_length004_1452_nmtoken_min_length004_1452_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minLength and value=4 and
    facet=maxLength and value=6) and document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKEN/NMTOKEN_minLength004.xsd",
        instance="msData/datatypes/Facets/NMTOKEN/NMTOKEN_minLength004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_nmtoken_min_length002_1450_nmtoken_min_length002_1450_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKEN/NMTOKEN_minLength002.xsd",
        instance="msData/datatypes/Facets/NMTOKEN/NMTOKEN_minLength002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_nmtoken_min_length001_1449_nmtoken_min_length001_1449_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minLength and value=4 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKEN/NMTOKEN_minLength001.xsd",
        instance="msData/datatypes/Facets/NMTOKEN/NMTOKEN_minLength001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_nmtoken_length002_1447_nmtoken_length002_1447_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=length and value=5 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKEN/NMTOKEN_length002.xsd",
        instance="msData/datatypes/Facets/NMTOKEN/NMTOKEN_length002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_idrefs_enumeration004_1445_idrefs_enumeration004_1445_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    foo123 fu1 and document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREFS/IDREFS_enumeration004.xsd",
        instance="msData/datatypes/Facets/IDREFS/IDREFS_enumeration004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_idrefs_enumeration002_1443_idrefs_enumeration002_1443_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREFS/IDREFS_enumeration002.xsd",
        instance="msData/datatypes/Facets/IDREFS/IDREFS_enumeration002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_idrefs_max_length003_1441_idrefs_max_length003_1441_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxLength and value=2 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREFS/IDREFS_maxLength003.xsd",
        instance="msData/datatypes/Facets/IDREFS/IDREFS_maxLength003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_idrefs_max_length002_1440_idrefs_max_length002_1440_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxLength and value=1 and
    document value=more
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREFS/IDREFS_maxLength002.xsd",
        instance="msData/datatypes/Facets/IDREFS/IDREFS_maxLength002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_idrefs_min_length004_1438_idrefs_min_length004_1438_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minLength and value=4 and
    facet=maxLength and value=6) and document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREFS/IDREFS_minLength004.xsd",
        instance="msData/datatypes/Facets/IDREFS/IDREFS_minLength004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_idrefs_min_length002_1436_idrefs_min_length002_1436_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minLength and value=2 and
    document value="more foofo"
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREFS/IDREFS_minLength002.xsd",
        instance="msData/datatypes/Facets/IDREFS/IDREFS_minLength002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_idrefs_min_length001_1435_idrefs_min_length001_1435_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minLength and value=1 and
    document value="foofo more"
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREFS/IDREFS_minLength001.xsd",
        instance="msData/datatypes/Facets/IDREFS/IDREFS_minLength001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_idrefs_length002_1433_idrefs_length002_1433_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=length and value=2 and document
    value="foofo more"
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREFS/IDREFS_length002.xsd",
        instance="msData/datatypes/Facets/IDREFS/IDREFS_length002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_language_enumeration004_1431_language_enumeration004_1431_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=en fr de
    and document value=en
    """
    assert_bindings(
        schema="msData/datatypes/Facets/language/language_enumeration004.xsd",
        instance="msData/datatypes/Facets/language/language_enumeration004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_language_enumeration002_1429_language_enumeration002_1429_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=en and
    document value=en
    """
    assert_bindings(
        schema="msData/datatypes/Facets/language/language_enumeration002.xsd",
        instance="msData/datatypes/Facets/language/language_enumeration002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_language_pattern001_1427_language_pattern001_1427_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=pattern and value=en-[a-z]{2}
    and document value=en-xx
    """
    assert_bindings(
        schema="msData/datatypes/Facets/language/language_pattern001.xsd",
        instance="msData/datatypes/Facets/language/language_pattern001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_language_max_length003_1426_language_max_length003_1426_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxLength and value=6 and
    document value=en-xx
    """
    assert_bindings(
        schema="msData/datatypes/Facets/language/language_maxLength003.xsd",
        instance="msData/datatypes/Facets/language/language_maxLength003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_language_max_length002_1425_language_max_length002_1425_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxLength and value=5 and
    document value=en-xx
    """
    assert_bindings(
        schema="msData/datatypes/Facets/language/language_maxLength002.xsd",
        instance="msData/datatypes/Facets/language/language_maxLength002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_language_min_length004_1423_language_min_length004_1423_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minLength and value=4 and
    facet=maxLength and value=6) and document value=en-xx
    """
    assert_bindings(
        schema="msData/datatypes/Facets/language/language_minLength004.xsd",
        instance="msData/datatypes/Facets/language/language_minLength004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_language_min_length002_1421_language_min_length002_1421_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minLength and value=5 and
    document value=en-xx
    """
    assert_bindings(
        schema="msData/datatypes/Facets/language/language_minLength002.xsd",
        instance="msData/datatypes/Facets/language/language_minLength002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_language_min_length001_1420_language_min_length001_1420_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minLength and value=4 and
    document value=en-xx
    """
    assert_bindings(
        schema="msData/datatypes/Facets/language/language_minLength001.xsd",
        instance="msData/datatypes/Facets/language/language_minLength001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_language_length002_1418_language_length002_1418_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=length and value=5 and document
    value=en-xx
    """
    assert_bindings(
        schema="msData/datatypes/Facets/language/language_length002.xsd",
        instance="msData/datatypes/Facets/language/language_length002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_token_enumeration004_1416_token_enumeration004_1416_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    foo123 fu1 and document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/token/token_enumeration004.xsd",
        instance="msData/datatypes/Facets/token/token_enumeration004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_token_enumeration002_1414_token_enumeration002_1414_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/token/token_enumeration002.xsd",
        instance="msData/datatypes/Facets/token/token_enumeration002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_token_pattern001_1412_token_pattern001_1412_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=pattern and value=[a-z]{3} and
    document value=abc
    """
    assert_bindings(
        schema="msData/datatypes/Facets/token/token_pattern001.xsd",
        instance="msData/datatypes/Facets/token/token_pattern001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_token_max_length003_1411_token_max_length003_1411_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxLength and value=6 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/token/token_maxLength003.xsd",
        instance="msData/datatypes/Facets/token/token_maxLength003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_token_max_length002_1410_token_max_length002_1410_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/token/token_maxLength002.xsd",
        instance="msData/datatypes/Facets/token/token_maxLength002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_token_min_length004_1408_token_min_length004_1408_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minLength and value=4 and
    facet=maxLength and value=6) and document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/token/token_minLength004.xsd",
        instance="msData/datatypes/Facets/token/token_minLength004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_token_min_length002_1406_token_min_length002_1406_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/token/token_minLength002.xsd",
        instance="msData/datatypes/Facets/token/token_minLength002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_token_min_length001_1405_token_min_length001_1405_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minLength and value=4 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/token/token_minLength001.xsd",
        instance="msData/datatypes/Facets/token/token_minLength001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_token_length002_1403_token_length002_1403_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=length and value=5 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/token/token_length002.xsd",
        instance="msData/datatypes/Facets/token/token_length002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_normalized_string_enumeration004_1401_normalized_string_enumeration004_1401_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    foo123 fu1 and document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/normalizedString/normalizedString_enumeration004.xsd",
        instance="msData/datatypes/Facets/normalizedString/normalizedString_enumeration004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_normalized_string_enumeration002_1399_normalized_string_enumeration002_1399_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/normalizedString/normalizedString_enumeration002.xsd",
        instance="msData/datatypes/Facets/normalizedString/normalizedString_enumeration002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_normalized_string_pattern001_1397_normalized_string_pattern001_1397_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=pattern and value=[a-z]{3} and
    document value=abc
    """
    assert_bindings(
        schema="msData/datatypes/Facets/normalizedString/normalizedString_pattern001.xsd",
        instance="msData/datatypes/Facets/normalizedString/normalizedString_pattern001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_normalized_string_max_length003_1396_normalized_string_max_length003_1396_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxLength and value=6 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/normalizedString/normalizedString_maxLength003.xsd",
        instance="msData/datatypes/Facets/normalizedString/normalizedString_maxLength003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_normalized_string_max_length002_1395_normalized_string_max_length002_1395_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/normalizedString/normalizedString_maxLength002.xsd",
        instance="msData/datatypes/Facets/normalizedString/normalizedString_maxLength002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_normalized_string_min_length004_1393_normalized_string_min_length004_1393_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minLength and value=4 and
    facet=maxLength and value=6) and document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/normalizedString/normalizedString_minLength004.xsd",
        instance="msData/datatypes/Facets/normalizedString/normalizedString_minLength004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_normalized_string_min_length002_1391_normalized_string_min_length002_1391_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/normalizedString/normalizedString_minLength002.xsd",
        instance="msData/datatypes/Facets/normalizedString/normalizedString_minLength002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_normalized_string_min_length001_1390_normalized_string_min_length001_1390_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minLength and value=4 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/normalizedString/normalizedString_minLength001.xsd",
        instance="msData/datatypes/Facets/normalizedString/normalizedString_minLength001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_normalized_string_length002_1388_normalized_string_length002_1388_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=length and value=5 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/normalizedString/normalizedString_length002.xsd",
        instance="msData/datatypes/Facets/normalizedString/normalizedString_length002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_notation_enumeration004_1386_notation_enumeration004_1386_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    foo123 fu1 and document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NOTATION/NOTATION_enumeration004.xsd",
        instance="msData/datatypes/Facets/NOTATION/NOTATION_enumeration004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_notation_enumeration002_1384_notation_enumeration002_1384_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NOTATION/NOTATION_enumeration002.xsd",
        instance="msData/datatypes/Facets/NOTATION/NOTATION_enumeration002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_notation_pattern001_1382_notation_pattern001_1382_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=pattern and value=[a-z]{3} and
    document value=abc
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NOTATION/NOTATION_pattern001.xsd",
        instance="msData/datatypes/Facets/NOTATION/NOTATION_pattern001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_notation_max_length003_1381_notation_max_length003_1381_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxLength and value=6 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NOTATION/NOTATION_maxLength003.xsd",
        instance="msData/datatypes/Facets/NOTATION/NOTATION_maxLength003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_notation_max_length002_1380_notation_max_length002_1380_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NOTATION/NOTATION_maxLength002.xsd",
        instance="msData/datatypes/Facets/NOTATION/NOTATION_maxLength002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_notation_max_length001_1379_notation_max_length001_1379_i(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxLength and value=4 and
    document value=foofo TSTF ruled that 1.0 says all QNames satisfy all
    length-related tess
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NOTATION/NOTATION_maxLength001.xsd",
        instance="msData/datatypes/Facets/NOTATION/NOTATION_maxLength001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_notation_min_length004_1378_notation_min_length004_1378_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minLength and value=4 and
    facet=maxLength and value=6) and document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NOTATION/NOTATION_minLength004.xsd",
        instance="msData/datatypes/Facets/NOTATION/NOTATION_minLength004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_notation_min_length003_1377_notation_min_length003_1377_i(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minLength and value=6 and
    document value=foofo TSTF ruled that 1.0 says all QNames satisfy all
    length-related tess
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NOTATION/NOTATION_minLength003.xsd",
        instance="msData/datatypes/Facets/NOTATION/NOTATION_minLength003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_notation_min_length002_1376_notation_min_length002_1376_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NOTATION/NOTATION_minLength002.xsd",
        instance="msData/datatypes/Facets/NOTATION/NOTATION_minLength002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_notation_min_length001_1375_notation_min_length001_1375_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minLength and value=4 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NOTATION/NOTATION_minLength001.xsd",
        instance="msData/datatypes/Facets/NOTATION/NOTATION_minLength001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_notation_length003_1374_notation_length003_1374_i(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=length and value=6 and document
    value=foofo TSTF ruled that 1.0 says all QNames satisfy all length-
    related tess
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NOTATION/NOTATION_length003.xsd",
        instance="msData/datatypes/Facets/NOTATION/NOTATION_length003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_notation_length002_1373_notation_length002_1373_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=length and value=5 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NOTATION/NOTATION_length002.xsd",
        instance="msData/datatypes/Facets/NOTATION/NOTATION_length002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_notation_length001_1372_notation_length001_1372_i(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=length and value=4 and document
    value=foofo TSTF ruled that 1.0 says all QNames satisfy all length-
    related tess
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NOTATION/NOTATION_length001.xsd",
        instance="msData/datatypes/Facets/NOTATION/NOTATION_length001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_qname_enumeration004_1371_qname_enumeration004_1371_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo:fo
    foo:foo123 foo:fu1 and document value=foo:fo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/QName/QName_enumeration004.xsd",
        instance="msData/datatypes/Facets/QName/QName_enumeration004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_qname_enumeration002_1369_qname_enumeration002_1369_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo:fo
    and document value=foo:fo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/QName/QName_enumeration002.xsd",
        instance="msData/datatypes/Facets/QName/QName_enumeration002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_qname_pattern001_1367_qname_pattern001_1367_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=pattern and value=[a-z]{3} and
    document value=abc
    """
    assert_bindings(
        schema="msData/datatypes/Facets/QName/QName_pattern001.xsd",
        instance="msData/datatypes/Facets/QName/QName_pattern001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_qname_max_length003_1366_qname_max_length003_1366_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxLength and value=6 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/QName/QName_maxLength003.xsd",
        instance="msData/datatypes/Facets/QName/QName_maxLength003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_qname_max_length002_1365_qname_max_length002_1365_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/QName/QName_maxLength002.xsd",
        instance="msData/datatypes/Facets/QName/QName_maxLength002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_qname_max_length001_1364_qname_max_length001_1364_i(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxLength and value=4 and
    document value=foofo TSTF ruled that 1.0 says all QNames satisfy all
    length-related tess
    """
    assert_bindings(
        schema="msData/datatypes/Facets/QName/QName_maxLength001.xsd",
        instance="msData/datatypes/Facets/QName/QName_maxLength001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_qname_min_length004_1363_qname_min_length004_1363_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minLength and value=4 and
    facet=maxLength and value=6) and document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/QName/QName_minLength004.xsd",
        instance="msData/datatypes/Facets/QName/QName_minLength004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_qname_min_length003_1362_qname_min_length003_1362_i(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minLength and value=6 and
    document value=foofo TSTF ruled that 1.0 says all QNames satisfy all
    length-related tess
    """
    assert_bindings(
        schema="msData/datatypes/Facets/QName/QName_minLength003.xsd",
        instance="msData/datatypes/Facets/QName/QName_minLength003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_qname_min_length002_1361_qname_min_length002_1361_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/QName/QName_minLength002.xsd",
        instance="msData/datatypes/Facets/QName/QName_minLength002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_qname_min_length001_1360_qname_min_length001_1360_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minLength and value=4 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/QName/QName_minLength001.xsd",
        instance="msData/datatypes/Facets/QName/QName_minLength001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_qname_length003_1359_qname_length003_1359_i(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=length and value=6 and document
    value=foofo TSTF ruled that 1.0 says all QNames satisfy all length-
    related tess
    """
    assert_bindings(
        schema="msData/datatypes/Facets/QName/QName_length003.xsd",
        instance="msData/datatypes/Facets/QName/QName_length003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_qname_length002_1358_qname_length002_1358_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=length and value=5 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/QName/QName_length002.xsd",
        instance="msData/datatypes/Facets/QName/QName_length002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_qname_length001_1357_qname_length001_1357_i(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=length and value=4 and document
    value=foofo TSTF ruled that 1.0 says all QNames satisfy all length-
    related tess
    """
    assert_bindings(
        schema="msData/datatypes/Facets/QName/QName_length001.xsd",
        instance="msData/datatypes/Facets/QName/QName_length001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_any_uri_b004_1354_any_uri_b004_1354_v(mode, save_output):
    """
    TEST :Facet Schemas for string : enumeration of many anyURI: a b c d e
    f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0 + - _ @
    ! ~ ? ., instance has . @ TSTF ruled that strictly speaking, per 1.0,
    the schema contains one or more invalid anyURIs In XSD 1.1, any
    sequence of characters is allowed in xs:anyURI, so the schema becomes
    valid - MHK
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_b004.xsd",
        instance="msData/datatypes/Facets/anyURI/anyURI_b004.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_any_uri_b002_1353_any_uri_b002_1353_v(mode, save_output):
    """
    TEST :Facet Schemas for string : enum of anyURI: with dbcs char, and
    instance has valid dbcs char
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_b002.xsd",
        instance="msData/datatypes/Facets/anyURI/anyURI_b002.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_any_uri_a002_1337_any_uri_a002_1337_v(mode, save_output):
    """
    TEST :Facet Schemas for string : test that dbcs charanters are allowed
    as anyURI in, any, anyAttribute, notation, appinfo, documentation,
    schema, include, redefine, import
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_a002.xsd",
        instance="msData/datatypes/Facets/anyURI/anyURI_a002.xml",
        class_name="Bar",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_any_uri_a001_1336_any_uri_a001_1336_v(mode, save_output):
    """
    TEST :Facet Schemas for string : test that the numbers are allowed as
    anyURI in, any, anyAttribute, notation, appinfo, documentation,
    schema, include, redefine, import TSTF ruled that strictly speaking,
    per 1.0, the schema contains one or more invalid anyURIs
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_a001.xsd",
        instance="msData/datatypes/Facets/anyURI/anyURI_a001.xml",
        class_name="Bar",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_any_uri_enumeration004_1335_any_uri_enumeration004_1335_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    http://www.microsoft.com mailto:davebrow@microsoft.com and document
    value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_enumeration004.xsd",
        instance="msData/datatypes/Facets/anyURI/anyURI_enumeration004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_any_uri_enumeration002_1333_any_uri_enumeration002_1333_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_enumeration002.xsd",
        instance="msData/datatypes/Facets/anyURI/anyURI_enumeration002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_any_uri_max_length003_1331_any_uri_max_length003_1331_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxLength and value=6 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_maxLength003.xsd",
        instance="msData/datatypes/Facets/anyURI/anyURI_maxLength003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_any_uri_max_length002_1330_any_uri_max_length002_1330_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_maxLength002.xsd",
        instance="msData/datatypes/Facets/anyURI/anyURI_maxLength002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_any_uri_min_length004_1328_any_uri_min_length004_1328_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minLength and value=4 and
    facet=maxLength and value=6) and document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_minLength004.xsd",
        instance="msData/datatypes/Facets/anyURI/anyURI_minLength004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_any_uri_min_length002_1326_any_uri_min_length002_1326_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_minLength002.xsd",
        instance="msData/datatypes/Facets/anyURI/anyURI_minLength002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_any_uri_min_length001_1325_any_uri_min_length001_1325_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minLength and value=4 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_minLength001.xsd",
        instance="msData/datatypes/Facets/anyURI/anyURI_minLength001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_any_uri_length002_1323_any_uri_length002_1323_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=length and value=5 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_length002.xsd",
        instance="msData/datatypes/Facets/anyURI/anyURI_length002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_base64_binary_enumeration002_1320_base64_binary_enumeration002_1320_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=MS0yLTM=
    and document value=MS0yLTM=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/base64Binary/base64Binary_enumeration002.xsd",
        instance="msData/datatypes/Facets/base64Binary/base64Binary_enumeration002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_base64_binary_min_length004_1315_base64_binary_min_length004_1315_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minLength and value=4 and
    facet=maxLength and value=6) and document value=MS0yLTM=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/base64Binary/base64Binary_minLength004.xsd",
        instance="msData/datatypes/Facets/base64Binary/base64Binary_minLength004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_base64_binary_min_length002_1313_base64_binary_min_length002_1313_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minLength and value=5 and
    document value=MS0yLTM=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/base64Binary/base64Binary_minLength002.xsd",
        instance="msData/datatypes/Facets/base64Binary/base64Binary_minLength002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_base64_binary_min_length001_1312_base64_binary_min_length001_1312_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minLength and value=4 and
    document value=MS0yLTM=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/base64Binary/base64Binary_minLength001.xsd",
        instance="msData/datatypes/Facets/base64Binary/base64Binary_minLength001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_base64_binary_length002_1310_base64_binary_length002_1310_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=length and value=5 and document
    value=MS0yLTM=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/base64Binary/base64Binary_length002.xsd",
        instance="msData/datatypes/Facets/base64Binary/base64Binary_length002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_hex_binary_enumeration004_1308_hex_binary_enumeration004_1308_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=adf789
    abcedf 0123456789 and document value=adf789
    """
    assert_bindings(
        schema="msData/datatypes/Facets/hexBinary/hexBinary_enumeration004.xsd",
        instance="msData/datatypes/Facets/hexBinary/hexBinary_enumeration004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_hex_binary_enumeration002_1306_hex_binary_enumeration002_1306_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=enumeration and value=adf789
    and document value=adf789
    """
    assert_bindings(
        schema="msData/datatypes/Facets/hexBinary/hexBinary_enumeration002.xsd",
        instance="msData/datatypes/Facets/hexBinary/hexBinary_enumeration002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_hex_binary_max_length003_1304_hex_binary_max_length003_1304_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxLength and value=6 and
    document value=abcde
    """
    assert_bindings(
        schema="msData/datatypes/Facets/hexBinary/hexBinary_maxLength003.xsd",
        instance="msData/datatypes/Facets/hexBinary/hexBinary_maxLength003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_hex_binary_max_length002_1303_hex_binary_max_length002_1303_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxLength and value=5 and
    document value=abcde
    """
    assert_bindings(
        schema="msData/datatypes/Facets/hexBinary/hexBinary_maxLength002.xsd",
        instance="msData/datatypes/Facets/hexBinary/hexBinary_maxLength002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_hex_binary_max_length001_1302_hex_binary_max_length001_1302_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=maxLength and value=4 and
    document value=abcde
    """
    assert_bindings(
        schema="msData/datatypes/Facets/hexBinary/hexBinary_maxLength001.xsd",
        instance="msData/datatypes/Facets/hexBinary/hexBinary_maxLength001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_hex_binary_min_length004_1301_hex_binary_min_length004_1301_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minLength and value=4 and
    facet=maxLength and value=6) and document value=abcdef1234 (let's try
    5 Octets [ab cd ef 12 34]
    """
    assert_bindings(
        schema="msData/datatypes/Facets/hexBinary/hexBinary_minLength004.xsd",
        instance="msData/datatypes/Facets/hexBinary/hexBinary_minLength004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_hex_binary_min_length002_1299_hex_binary_min_length002_1299_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minLength and value=5 and
    document value=abcdef123456. Let's try 6 Octets [ab cd ef 12 34 56]
    """
    assert_bindings(
        schema="msData/datatypes/Facets/hexBinary/hexBinary_minLength002.xsd",
        instance="msData/datatypes/Facets/hexBinary/hexBinary_minLength002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_hex_binary_min_length001_1298_hex_binary_min_length001_1298_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minLength and value=4 and
    document value=abcdefab 4 Octets are [ab cd ef ab]
    """
    assert_bindings(
        schema="msData/datatypes/Facets/hexBinary/hexBinary_minLength001.xsd",
        instance="msData/datatypes/Facets/hexBinary/hexBinary_minLength001.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_hex_binary_length002_1296_hex_binary_length002_1296_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=length and value=5 and document
    value=abcdefabcd where 5 Octets are [ab cd ef ab cd]
    """
    assert_bindings(
        schema="msData/datatypes/Facets/hexBinary/hexBinary_length002.xsd",
        instance="msData/datatypes/Facets/hexBinary/hexBinary_length002.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_g_day_min_exclusive005_1273_g_day_min_exclusive005_1273_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=- - -01
    and facet=maxExclusive and value=- - -30) and document value=- - -15
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gDay/gDay_minExclusive005.xsd",
        instance="msData/datatypes/Facets/gDay/gDay_minExclusive005.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_g_day_min_exclusive004_1272_g_day_min_exclusive004_1272_v(mode, save_output):
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=- - -01
    and facet=maxInclusive and value=- - -30) and document value=- - -15
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gDay/gDay_minExclusive004.xsd",
        instance="msData/datatypes/Facets/gDay/gDay_minExclusive004.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )


def test_g_day_min_exclusive003_1271_g_day_min_exclusive003_1271_v(mode, save_output):
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=- - -01
    and document value=- - -15
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gDay/gDay_minExclusive003.xsd",
        instance="msData/datatypes/Facets/gDay/gDay_minExclusive003.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        structure_style="filenames",
    )
