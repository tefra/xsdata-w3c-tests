import pytest

from tests.utils import assert_bindings


@pytest.mark.schema11
def test_s3_3_6ii03_s3_3_6ii03i():
    """
    Tests notQName in allgroup
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_3_6/s3_3_6ii03.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_3_6/s3_3_6ii03.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_6ii02_s3_3_6ii02i():
    """
    Tests notNamespace in all group
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_3_6/s3_3_6ii02.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_3_6/s3_3_6ii02.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_6ii01_s3_3_6ii01i():
    """
    maxOccurs may now be >1 in all group
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_3_6/s3_3_6ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_3_6/s3_3_6ii01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_6v05_s3_3_6v05i():
    """
    Tests maxOccurs > 1 for elements within all group
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_6/s3_3_6v05.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_6/s3_3_6v05.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_6v04_s3_3_6v04i():
    """
    Tests restriction of all group
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_6/s3_3_6v04.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_6/s3_3_6v04.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_6v01_s3_3_6v01i():
    """
    Wildcards are now allowed in xs:all
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_6/s3_3_6v01.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_6/s3_3_6v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


def test_s3_10_6ii04_s3_10_6v04i():
    """
    Tests namespace attribute on xs:anyAttribute
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_10_6/s3_10_6ii04.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_10_6/s3_10_6ii04.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_s3_10_6ii03_s3_10_6v03i():
    """
    Tests namespace attribute on xs:anyAttribute
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_10_6/s3_10_6ii03.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_10_6/s3_10_6ii03.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_s3_10_6ii02_s3_10_6v02i():
    """
    Tests notQName and notNamespace list in xs:anyAttribute
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_10_6/s3_10_6ii02.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_10_6/s3_10_6ii02.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_s3_10_6ii01_s3_10_6v01i():
    """
    Tests notQName on xs:anyAttribute
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_10_6/s3_10_6ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_10_6/s3_10_6ii01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.schema11
def test_s3_10_6v03_s3_10_6v03i():
    """
    Tests namespace attribute on xs:anyAttribute
    """
    assert_bindings(
        schema="ibmData/valid/S3_10_6/s3_10_6v03.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_10_6/s3_10_6v03.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_10_6v02_s3_10_6v02i():
    """
    Tests namespace attribute on xs:anyAttribute
    """
    assert_bindings(
        schema="ibmData/valid/S3_10_6/s3_10_6v02.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_10_6/s3_10_6v02.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_10_6v01_s3_10_6v01i():
    """
    Tests notQName on xs:anyAttribute
    """
    assert_bindings(
        schema="ibmData/valid/S3_10_6/s3_10_6v01.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_10_6/s3_10_6v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_035_assert_035_2():
    """
    An example demonstrating constraining the cardinality of schema
    xs:list, and defining assertion on items                         of
    the schema xs:list.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/list_union/listunion6.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/list_union/listunion6_1.xml",
        instance_is_valid=True,
        class_name="ListType",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_035_assert_035_3():
    """
    An example demonstrating constraining the cardinality of schema
    xs:list, and defining assertion on items                         of
    the schema xs:list.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/list_union/listunion6.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/list_union/listunion6_2.xml",
        instance_is_valid=False,
        class_name="ListType",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_034_assert_034_3():
    """
    An example demonstrating assertion defined in simple schema type,
    which is itemType of xs:list schema component.
    This example defines an schema simpleType for an XML attribute.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/list_union/listunion5.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/list_union/listunion5_2.xml",
        instance_is_valid=False,
        class_name="Example",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_033_assert_033_2():
    """
    Demonstrating assertions on memberTypes of xs:union.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/list_union/listunion4.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/list_union/listunion3_1.xml",
        instance_is_valid=True,
        class_name="Example",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_032_assert_032_2():
    """
    This is similar to example "assert_031", but here both of memberTypes
    of union have assertions specified on them.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/list_union/listunion3.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/list_union/listunion3_1.xml",
        instance_is_valid=True,
        class_name="Example",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_032_assert_032_3():
    """
    This is similar to example "assert_031", but here both of memberTypes
    of union have assertions specified on them.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/list_union/listunion3.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/list_union/listunion3_2.xml",
        instance_is_valid=False,
        class_name="Example",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_031_assert_031_2():
    """
    An example demonstrating XSD 1.1 assertions evaluation on a simple
    type value, when the simpleType is a                          union
    type, and one of memberTypes of union specifies assertions.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/list_union/listunion2.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/list_union/listunion2_1.xml",
        instance_is_valid=True,
        class_name="Example",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_031_assert_031_3():
    """
    An example demonstrating XSD 1.1 assertions evaluation on a simple
    type value, when the simpleType is a                          union
    type, and one of memberTypes of union specifies assertions.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/list_union/listunion2.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/list_union/listunion2_2.xml",
        instance_is_valid=False,
        class_name="Example",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_031_assert_031_4():
    """
    An example demonstrating XSD 1.1 assertions evaluation on a simple
    type value, when the simpleType is a                          union
    type, and one of memberTypes of union specifies assertions.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/list_union/listunion2.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/list_union/listunion2_3.xml",
        instance_is_valid=True,
        class_name="Example",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_031_assert_031_5():
    """
    An example demonstrating XSD 1.1 assertions evaluation on a simple
    type value, when the simpleType is a                          union
    type, and one of memberTypes of union specifies assertions.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/list_union/listunion2.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/list_union/listunion2_4.xml",
        instance_is_valid=False,
        class_name="Example",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_030_assert_030_2():
    """
    An example demonstrating XSD 1.1 assertions defined on itemType
    definition of xs:list schema component.                         In
    this scenario assertions must evaluate on all-of list items, and every
    list item must pass the assertions                         test for
    assertion to contribute to XML instance validation.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/list_union/listunion1.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/list_union/listunion1_1.xml",
        instance_is_valid=True,
        class_name="Example",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_030_assert_030_3():
    """
    An example demonstrating XSD 1.1 assertions defined on itemType
    definition of xs:list schema component.                         In
    this scenario assertions must evaluate on all-of list items, and every
    list item must pass the assertions                         test for
    assertion to contribute to XML instance validation.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/list_union/listunion1.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/list_union/listunion1_2.xml",
        instance_is_valid=False,
        class_name="Example",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_029_assert_029_2():
    """
    An example demonstrating XSD 1.1 assertions evaluation, where XML
    schema document declares an XML attribute in a
    namespace, using "targetNamespace" attribute on xs:attribute
    declaration, and an assertion XPath expression makes use
    of namespace qualified attribute node reference.
    There are two XML instance tests in this example (one passes and the
    other fails wrt XSD 1.1 assertions, due to varying
    data in XML instance documents).
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/namespace/ns5.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/namespace/ns5_1.xml",
        instance_is_valid=True,
        class_name="X",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_029_assert_029_3():
    """
    An example demonstrating XSD 1.1 assertions evaluation, where XML
    schema document declares an XML attribute in a
    namespace, using "targetNamespace" attribute on xs:attribute
    declaration, and an assertion XPath expression makes use
    of namespace qualified attribute node reference.
    There are two XML instance tests in this example (one passes and the
    other fails wrt XSD 1.1 assertions, due to varying
    data in XML instance documents).
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/namespace/ns5.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/namespace/ns5_2.xml",
        instance_is_valid=False,
        class_name="X",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_028_assert_028_2():
    """
    An example demonstrating XSD 1.1 assertions evaluation, where an
    assertion checks for in-scope namespace prefixes
    on XML element.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/namespace/ns4.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/namespace/ns4.xml",
        instance_is_valid=True,
        class_name="X",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_027_assert_027_2():
    """
    An example demonstrating XSD 1.1 assertions evaluation when XML
    document is an namespace, and assertions perform
    namespace URI comparisons on element nodes.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/namespace/ns3.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/namespace/ns3.xml",
        instance_is_valid=True,
        class_name="X",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_026_assert_026_2():
    """
    An example demonstrating XSD 1.1 assertions evaluation when outermost
    element in an XML document is in an namespace, while
    inner ones are not, and there are few assertions defined on the schema
    type involved.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/namespace/ns2.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/namespace/ns2.xml",
        instance_is_valid=True,
        class_name="X",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_025_assert_025_2():
    """
    An example demonstrating XSD 1.1 assertions evaluation using xs:assert
    instruction, when xs:assert has attribute
    "xpathDefaultNamespace".
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/namespace/ns1.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/namespace/ns1.xml",
        instance_is_valid=True,
        class_name="X",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_024_assert_024_2():
    """
    An example demonstrating assertions evaluation, with xs:string schema
    type when white-space normalization must not happen
    on the data. The validation in this example would succeed, since an
    assertion normalizes the data value with "normalize-space"
    XPath function before equality comparison.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/whitespace/test5.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/whitespace/test3.xml",
        instance_is_valid=True,
        class_name="X",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_023_assert_023_2():
    """
    An example demonstrating assertions evaluation, with xs:string schema
    type when white-space normalization must not happen
    on the data. The example demonstrates ignoring of comments within XML
    elements (which have simple XML schema values), for
    findings value of assertions XPath 2.0 context variable $value. This
    test is similar to test "assert_022" but the validation
    fails in this case, since the schema type of XML element is xs:string.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/whitespace/test4.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/whitespace/test3.xml",
        instance_is_valid=False,
        class_name="X",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_022_assert_022_2():
    """
    An example demonstrating assertions evaluation, with a numeric schema
    type when white-space normalization                         must
    happen on the data. The example demonstrates ignoring of comments
    within XML elements (which have simple schema values),
    for findings value of assertions XPath 2.0 context variable $value.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/whitespace/test3.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/whitespace/test3.xml",
        instance_is_valid=True,
        class_name="X",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_021_assert_021_2():
    """
    An example demonstrating assertions evaluation, with a xs:string
    schema type when white-space normalization
    must not happen on the data.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/whitespace/test2.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/whitespace/test1.xml",
        instance_is_valid=False,
        class_name="X",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_020_assert_020_2():
    """
    An example demonstrating assertions evaluation, with a numeric schema
    type when white-space normalization                         must
    happen on the data.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/whitespace/test1.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/whitespace/test1.xml",
        instance_is_valid=True,
        class_name="X",
        version="1.1",
    )


@pytest.mark.schema11
@pytest.mark.xfail
def test_assert_019_assert_019_2():
    """
    A sample "purchase order" instance validation with an XML schema,
    using XSD 1.1 assertions.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/po_sample/po.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/po_sample/po.xml",
        instance_is_valid=True,
        class_name="Order",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_018_assert_018_2():
    """
    This is similar to test 'assert_017', but element a's schema type in
    xs:group definition here has an                         additional
    assertion.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/test18.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/test18_1.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_018_assert_018_3():
    """
    This is similar to test 'assert_017', but element a's schema type in
    xs:group definition here has an                         additional
    assertion.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/test18.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/test18_2.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_017_assert_017_2():
    """
    An assertions example, where an XML schema xs:group definition is
    reused in different schema types,                         and
    cardinality of element particles in different types is controlled via
    schema assertions.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/test17.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/test17.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_016_assert_016_2():
    """
    Describing both xs:assert & xs:assertion on complexType ->
    simpleContent -> restriction.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/test16.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/test16.xml",
        instance_is_valid=True,
        class_name="A",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_015_assert_015_2():
    """
    Describing relatively involved assertions. Assertions are described in
    the data file                         itself at
    xs:assert/xs:annotation.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/test15.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/test15.xml",
        instance_is_valid=True,
        class_name="Example",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_014_assert_014_2():
    """
    Assertion defined on attribute's schema type. Uses assertions XPath
    2.0 context variable $value.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/test14.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/test14.xml",
        instance_is_valid=True,
        class_name="Example",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_013_assert_013_2():
    """
    Assertions on a fictitious numerical example.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/test13.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/test13.xml",
        instance_is_valid=True,
        class_name="Example",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_012_assert_012_2():
    """
    Multiple assertions on a complexType, with a fictitious problem
    description.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/test12.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/test12.xml",
        instance_is_valid=True,
        class_name="Shape",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_011_assert_011_2():
    """
    Assertions on complex type, using xpathDefaultNamespace attribute on
    xs:assert.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/test11.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/test11.xml",
        instance_is_valid=True,
        class_name="X",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_010_assert_010_2():
    """
    Assertions on complex type derivations.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/test10.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/test10.xml",
        instance_is_valid=True,
        class_name="Message",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_009_assert_009_2():
    """
    Assertions on simple type, using assertions XPath 2.0 context variable
    $value.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/test9.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/test9.xml",
        instance_is_valid=True,
        class_name="Message",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_008_assert_008_2():
    """
    Assertions on schema "complex type" definitions, having attribute with
    simple content.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/test8.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/test8.xml",
        instance_is_valid=True,
        class_name="Shoesize",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_007_assert_007_2():
    """
    Assertions on schema "simple type" definitions, with inheritance
    relationship.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/test7.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/test7.xml",
        instance_is_valid=True,
        class_name="Message",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_006_assert_006_2():
    """
    Assertions on complexType -> complexContent, with inheritance
    relationship between schema types.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/test6.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/test6.xml",
        instance_is_valid=True,
        class_name="Message",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_005_assert_005_2():
    """
    Multiple assertions on a sample 'simple type'.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/test5.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/test5.xml",
        instance_is_valid=True,
        class_name="Value",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_004_assert_004_2():
    """
    Multiple assertions on a complex type, with a fictitious problem
    description.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/test4.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/test4.xml",
        instance_is_valid=True,
        class_name="Phonebill",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_003_assert_003_2():
    """
    Assertions on a complex type, with relatively bigger content model.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/test3.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/test3.xml",
        instance_is_valid=True,
        class_name="Data",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_002_assert_002_2():
    """
    Assertions demonstrating co-occurence constraints (constraints between
    an attribute value and elements).
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/test2.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/test2_1.xml",
        instance_is_valid=True,
        class_name="Xlist",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_002_assert_002_3():
    """
    Assertions demonstrating co-occurence constraints (constraints between
    an attribute value and elements).
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/test2.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/test2_2.xml",
        instance_is_valid=False,
        class_name="Xlist",
        version="1.1",
    )


@pytest.mark.schema11
def test_assert_001_assert_001_2():
    """
    Assertions demonstrating co-occurence constraints, along with an
    assertion constraining                          element's
    simpleContent value.
    """
    assert_bindings(
        schema="ibmData/mixed/assertions/test1.xsd",
        is_valid=True,
        instance="ibmData/mixed/assertions/test1.xml",
        instance_is_valid=True,
        class_name="X",
        version="1.1",
    )


@pytest.mark.schema11
@pytest.mark.xfail
def test_d4_3_15ii32_d4_3_15ii32i():
    """
    "//" returns empty sequence
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_15/d4_3_15ii32.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_15/d4_3_15ii32.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
@pytest.mark.xfail
def test_d4_3_15ii31_d4_3_15ii31i():
    """
    "//" returns empty sequence
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_15/d4_3_15ii31.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_15/d4_3_15ii31.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15ii30_d4_3_15ii30i():
    """
    assertion on different namespace test case in simpleType/complexType
    impact of xpathDefaultNamespace locally and at schema level
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_15/d4_3_15ii30.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_15/d4_3_15ii30.xml",
        instance_is_valid=False,
        class_name="RootInA",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15ii29_d4_3_15ii29i():
    """
    xpathDefaultNamespace, assertion on different namespace test case in
    simpleType/complexType
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_15/d4_3_15ii29.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_15/d4_3_15ii29.xml",
        instance_is_valid=False,
        class_name="RootInA",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15ii27_d4_3_15ii27i():
    """
    naive xpathDefaultNamespace(with value ##local) test case in
    complexType
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_15/d4_3_15ii27.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_15/d4_3_15ii27.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15ii25_d4_3_15ii25i():
    """
    naive xpathDefaultNamespace(with value ##defaultNamespace) test case
    in complexType
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_15/d4_3_15ii25.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_15/d4_3_15ii25.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15ii24_d4_3_15ii24i():
    """
    naive xpathDefaultNamespace(exact uri of targetNamespace) test case in
    simpleType
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_15/d4_3_15ii24.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_15/d4_3_15ii24.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15ii23_d4_3_15ii23i():
    """
    naive xpathDefaultNamespace (exact uri of targetNamespace) test case
    in complexType
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_15/d4_3_15ii23.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_15/d4_3_15ii23.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15ii22_d4_3_15ii22i():
    """
    naive xpathDefaultNamespace(with value ##targetNamespace) test case in
    simpleType
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_15/d4_3_15ii22.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_15/d4_3_15ii22.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15ii21_d4_3_15ii21i():
    """
    naive xpathDefaultNamespace(with value ##targetNamespace) test case in
    complexType
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_15/d4_3_15ii21.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_15/d4_3_15ii21.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15ii20_d4_3_15ii20i():
    """
    assertions on a simple type definition.
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_15/d4_3_15ii20.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_15/d4_3_15ii20.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15ii19_d4_3_15ii19i():
    """
    assertions on a complex type definition,           having
    simpleContent, assertions from anyAtomicType type.
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_15/d4_3_15ii19.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_15/d4_3_15ii19.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15ii18_d4_3_15ii18i():
    """
    assertions on a complex type definition,         having
    complexContent, assertions from anySimpleType type
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_15/d4_3_15ii18.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_15/d4_3_15ii18.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
@pytest.mark.xfail
def test_d4_3_15ii17_d4_3_15ii17i():
    """
    inability to navigate outside the subtree, assertion on elements with
    derivation by extension
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_15/d4_3_15ii17.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_15/d4_3_15ii17.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
@pytest.mark.xfail
def test_d4_3_15ii15_d4_3_15ii15i():
    """
    inability to navigate outside the subtree, assertion on attributes
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_15/d4_3_15ii15.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_15/d4_3_15ii15.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
@pytest.mark.xfail
def test_d4_3_15ii14_d4_3_15ii14i():
    """
    inability to navigate outside the subtree, assertion on elements
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_15/d4_3_15ii14.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_15/d4_3_15ii14.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15ii13_d4_3_15ii13i():
    """
    dynamic context of the XPath expression, assertion on element
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_15/d4_3_15ii13.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_15/d4_3_15ii13.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
@pytest.mark.xfail
def test_d4_3_15ii12_d4_3_15ii12i():
    """
    inability to navigate outside the subtree, assertion on elements with
    derivation by extension
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_15/d4_3_15ii12.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_15/d4_3_15ii12.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15ii11_d4_3_15ii11i():
    """
    dynamic context of the XPath expression, assertion on attribute
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_15/d4_3_15ii11.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_15/d4_3_15ii11.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15ii10_d4_3_15ii10i():
    """
    ssertions on derived complex type
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_15/d4_3_15ii10.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_15/d4_3_15ii10.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15ii08_d4_3_15ii08i():
    """
    assertions on a complex type definition having simpleContent
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_15/d4_3_15ii08.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_15/d4_3_15ii08.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15ii06_d4_3_15ii06i():
    """
    assertions on a complex type definition,having complexContent,
    assertions from both derived and base type must succeed
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_15/d4_3_15ii06.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_15/d4_3_15ii06.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15ii04_d4_3_15ii04i():
    """
    assertions on a complex type definition. uses multiple asserts
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_15/d4_3_15ii04.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_15/d4_3_15ii04.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15ii03_d4_3_15ii03i():
    """
    assertions on a complex type definition. this schema has a bigger
    content model, with assertions at various levels.
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_15/d4_3_15ii03.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_15/d4_3_15ii03.xml",
        instance_is_valid=False,
        class_name="Data",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15ii02_d4_3_15ii02i():
    """
    Assertions on a complex type definition
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_15/d4_3_15ii02.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_15/d4_3_15ii02.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15ii01_d4_3_15ii01i():
    """
    Assertions on a complex type definition
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_15/d4_3_15ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_15/d4_3_15ii01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15v28_d4_3_15v28i():
    """
    naive xpathDefaultNamespace(with value ##local) test case in
    simpleType
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_15/d4_3_15v28.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_15/d4_3_15v28.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15v27_d4_3_15v27i():
    """
    naive xpathDefaultNamespace(with value ##local) test case in
    complexType
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_15/d4_3_15v27.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_15/d4_3_15v27.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15v26_d4_3_15v26i():
    """
    naive xpathDefaultNamespace(with value ##defaultNamespace) test case
    in simpleType
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_15/d4_3_15v26.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_15/d4_3_15v26.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15v25_d4_3_15v25i():
    """
    naive xpathDefaultNamespace(with value ##defaultNamespace) test case
    in complexTypen
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_15/d4_3_15v25.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_15/d4_3_15v25.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15v24_d4_3_15v24i():
    """
    naive xpathDefaultNamespace(exact uri of targetNamespace) test case in
    simpleType
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_15/d4_3_15v24.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_15/d4_3_15v24.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15v23_d4_3_15v23i():
    """
    naive xpathDefaultNamespace (exact uri of targetNamespace) test case
    in complexType
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_15/d4_3_15v23.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_15/d4_3_15v23.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15v22_d4_3_15v22i():
    """
    naive xpathDefaultNamespace(with value ##targetNamespace) test case in
    simpleType
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_15/d4_3_15v22.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_15/d4_3_15v22.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15v21_d4_3_15v21i():
    """
    naive xpathDefaultNamespace(with value ##targetNamespace) test case in
    complexType
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_15/d4_3_15v21.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_15/d4_3_15v21.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15v19_d4_3_15v19i():
    """
    assertions on a complex type definition,           having
    simpleContent, assertions from anyAtomicType type.
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_15/d4_3_15v19.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_15/d4_3_15v19.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15v18_d4_3_15v18i():
    """
    assertions on a complex type definition,           having
    complexContent, assertions from anySimpleType type.
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_15/d4_3_15v18.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_15/d4_3_15v18.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
@pytest.mark.xfail
def test_d4_3_15v15_d4_3_15v15i():
    """
    inability to navigate outside the subtree, assertion on attributes
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_15/d4_3_15v15.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_15/d4_3_15v15.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
@pytest.mark.xfail
def test_d4_3_15v14_d4_3_15v14i():
    """
    inability to navigate outside the subtree, assertion on elements
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_15/d4_3_15v14.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_15/d4_3_15v14.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15v13_d4_3_15v13i():
    """
    dynamic context of the XPath expression, assertion on element
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_15/d4_3_15v13.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_15/d4_3_15v13.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15v11_d4_3_15v11i():
    """
    dynamic context of the XPath expression, assertion on attribute
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_15/d4_3_15v11.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_15/d4_3_15v11.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15v10_d4_3_15v10i():
    """
    assertions on derived complex type
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_15/d4_3_15v10.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_15/d4_3_15v10.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15v09_d4_3_15v09i():
    """
    assertions on simple type, using variable $value
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_15/d4_3_15v09.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_15/d4_3_15v09.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15v08_d4_3_15v08i():
    """
    assertions on a complex type definition having simpleContent
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_15/d4_3_15v08.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_15/d4_3_15v08.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15v07_d4_3_15v07i():
    """
    assertions on derived simple type definitions,           all baseType
    and derivedType must evaluate to be true
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_15/d4_3_15v07.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_15/d4_3_15v07.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15v06_d4_3_15v06i():
    """
    having complexContent, assertions from both derived and base type must
    succeed
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_15/d4_3_15v06.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_15/d4_3_15v06.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15v05_d4_3_15v05i():
    """
    assertions on a simple type definition
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_15/d4_3_15v05.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_15/d4_3_15v05.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15v04_d4_3_15v04i():
    """
    ssertions on a complex type definition. uses multiple asserts
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_15/d4_3_15v04.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_15/d4_3_15v04.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15v03_d4_3_15v03i():
    """
    assertions on a complex type definition
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_15/d4_3_15v03.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_15/d4_3_15v03.xml",
        instance_is_valid=True,
        class_name="Data",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15v02_d4_3_15v02i():
    """
    Assertions on a complex type definition
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_15/d4_3_15v02.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_15/d4_3_15v02.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_15v01_d4_3_15v01i():
    """
    Assertions on a complex type definition
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_15/d4_3_15v01.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_15/d4_3_15v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s4_2_2ii01_s4_2_2ii01i():
    """
    invalid instance vc: conditional inclusion Testing version
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S4_2_2/s4_2_2ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S4_2_2/s4_2_2ii01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s4_2_2v01_s4_2_2v01i():
    """
    vc: conditional inclusion Testing version
    """
    assert_bindings(
        schema="ibmData/valid/S4_2_2/s4_2_2v01.xsd",
        is_valid=True,
        instance="ibmData/valid/S4_2_2/s4_2_2v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_2_3ii05_s3_2_3ii05i():
    """
    Named identity constraints on local element declarations
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_2_3/s3_2_3ii05.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_2_3/s3_2_3ii05.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_2_3ii04_s3_2_3ii04i():
    """
    Tests the targetNamespace attribute in locally declared element and
    attribute.
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_2_3/s3_2_3ii04.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_2_3/s3_2_3ii04.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_2_3ii02_s3_2_3ii02i():
    """
    Tests for valid derivation of restriction of complexType in other
    namespace.
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_2_3/s3_2_3ii02.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_2_3/s3_2_3ii02.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_2_3ii01_s3_2_3ii01i():
    """
    Tests the targetNamespace attribute in locally declared element and
    attribute.
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_2_3/s3_2_3ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_2_3/s3_2_3ii01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_2_3v04_s3_2_3v04i():
    """
    Tests the targetNamespace attribute in locally declared element and
    attribute.
    """
    assert_bindings(
        schema="ibmData/valid/S3_2_3/s3_2_3v04.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_2_3/s3_2_3v04.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_2_3v01_s3_2_3v01i():
    """
    Tests the targetNamespace attribute in locally declared element and
    attribute.
    """
    assert_bindings(
        schema="ibmData/valid/S3_2_3/s3_2_3v01.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_2_3/s3_2_3v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_3_10v01_d3_3_10v01i():
    """
    A day is a calendar (or "local time") day in each timezone, including
    the timezones outside of +12:00 through -11:59 inclusive.
    """
    assert_bindings(
        schema="ibmData/valid/D3_3_10/d3_3_10v01.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_3_10/d3_3_10v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_28ii01_d3_4_28ii01i():
    """
    invalid dateTimeStamp values;Invalid enumeration values
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D3_4_28/d3_4_28ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D3_4_28/d3_4_28ii01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_28ii01_d3_4_28ii02i():
    """
    invalid dateTimeStamp values;Invalid enumeration values
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D3_4_28/d3_4_28ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D3_4_28/d3_4_28ii02.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_28ii01_d3_4_28ii03i():
    """
    invalid dateTimeStamp values;Invalid enumeration values
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D3_4_28/d3_4_28ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D3_4_28/d3_4_28ii03.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_28ii01_d3_4_28ii04i():
    """
    invalid dateTimeStamp values;Invalid enumeration values
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D3_4_28/d3_4_28ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D3_4_28/d3_4_28ii04.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_28ii01_d3_4_28ii05i():
    """
    invalid dateTimeStamp values;Invalid enumeration values
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D3_4_28/d3_4_28ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D3_4_28/d3_4_28ii05.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_28v10_d3_4_28v10i():
    """
    Additional dateTimeStamp tests, for attributes
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_28/d3_4_28v10.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_28/d3_4_28v10.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_28v09_d3_4_28v09i():
    """
    Tests the simpleType dateTimeStamp and its facets with (min|max)
    (Inclusive|Exclusive) constraint checks in derivations of simpleTypes
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_28/d3_4_28v09.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_28/d3_4_28v09.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_28v08_d3_4_28v08i():
    """
    Tests the simpleType dateTimeStamp and its facets with (min|max)
    (Inclusive|Exclusive) constraint checks in derivations of simpleTypes
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_28/d3_4_28v08.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_28/d3_4_28v08.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_28v07_d3_4_28v07i():
    """
    Tests the simpleType decimal and its facets with (min|max)
    (Inclusive|Exclusive) constraint checks in derivations of simpleTypes
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_28/d3_4_28v07.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_28/d3_4_28v07.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_28v06_d3_4_28v06i():
    """
    Tests the simpleType dateTimeStamp and its facets with (min|max)
    (Inclusive|Exclusive) constraint checks in derivations of simpleTypes
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_28/d3_4_28v06.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_28/d3_4_28v06.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_28v05_d3_4_28v05i():
    """
    Tests the simpleType decimal and its facets
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_28/d3_4_28v05.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_28/d3_4_28v05.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_28v04_d3_4_28v04i():
    """
    Tests the simpleType decimal and its facets, used with unions
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_28/d3_4_28v04.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_28/d3_4_28v04.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_28v03_d3_4_28v03i():
    """
    Tests the simpleType dateTimeStamp and its facets pattern, used in
    lists
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_28/d3_4_28v03.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_28/d3_4_28v03.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_28v02_d3_4_28v02i():
    """
    Tests the simpleType decimal and its facets and its use in attributes
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_28/d3_4_28v02.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_28/d3_4_28v02.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_28v01_d3_4_28v01i():
    """
    Tests the simpleType dateTimeStamp and its facets and its use in
    elements
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_28/d3_4_28v01.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_28/d3_4_28v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_27ii07_d3_4_27ii07i():
    """
    Invalid dayTimeDuration values used with (min|max)
    (Inclusive|Exclusive) constraint checks in derivations of simpleTypes
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D3_4_27/d3_4_27ii07.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D3_4_27/d3_4_27ii07.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_27ii06_d3_4_27ii06i():
    """
    Invalid dayTimeDuration values used in unions
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D3_4_27/d3_4_27ii06.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D3_4_27/d3_4_27ii06.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_27ii05_d3_4_27ii05i():
    """
    Invalid values of dayTimeDuration and invalid instance of its facets
    used in attributes
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D3_4_27/d3_4_27ii05.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D3_4_27/d3_4_27ii05.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_27ii04_d3_4_27ii04i():
    """
    Invalid dayTimeDuration Min/Max Exclusive
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D3_4_27/d3_4_27ii04.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D3_4_27/d3_4_27ii04.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_27ii03_d3_4_27ii03i():
    """
    Invalid dayTimeDuration Min/Max Inclusive
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D3_4_27/d3_4_27ii03.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D3_4_27/d3_4_27ii03.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_27ii02_d3_4_27ii02i():
    """
    Invalid dayTimeDuration enumeration values
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D3_4_27/d3_4_27ii02.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D3_4_27/d3_4_27ii02.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_27ii01_d3_4_27ii01i():
    """
    Invalid dayTimeDuration values
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D3_4_27/d3_4_27ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D3_4_27/d3_4_27ii01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_27v05_d3_4_27v05i():
    """
    Additional tests for dayTimeDuration and its facets with (min|max)
    (Inclusive|Exclusive) constraint checks in derivations of simpleTypes
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_27/d3_4_27v05.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_27/d3_4_27v05.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_27v04_d3_4_27v04i():
    """
    Tests the simpleType dayTimeDuration and its facets with (min|max)
    (Inclusive|Exclusive) constraint checks in derivations of simpleTypes
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_27/d3_4_27v04.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_27/d3_4_27v04.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_27v03_d3_4_27v03i():
    """
    Tests dayTimeDuration used in unions
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_27/d3_4_27v03.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_27/d3_4_27v03.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_27v02_d3_4_27v02i():
    """
    Tests the simpleType dayTimeDuration and its facets and its use in
    attributes
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_27/d3_4_27v02.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_27/d3_4_27v02.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_27v01_d3_4_27v01i():
    """
    Tests the simpleType dayTimeDuration and its facets
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_27/d3_4_27v01.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_27/d3_4_27v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_4_2_4ii11_s3_4_2_4ii11i():
    """
    test defaultAttributesApply is absent, and ref attribute in
    attributeGroup
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_4_2_4/s3_4_2_4ii11.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_4_2_4/s3_4_2_4ii11.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_4_2_4ii10_s3_4_2_4ii10i():
    """
    test defaultAttributesApply = false and override as false
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_4_2_4/s3_4_2_4ii10.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_4_2_4/s3_4_2_4ii10.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_4_2_4ii09_s3_4_2_4ii09i():
    """
    test defaultAttributesApply = false/true/absent across multiple schema
    documents
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_4_2_4/s3_4_2_4ii09.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_4_2_4/s3_4_2_4ii09.xml",
        instance_is_valid=False,
        class_name="RootInA",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_4_2_4ii08_s3_4_2_4ii08i():
    """
    test defaultAttributesApply = false and override as absent
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_4_2_4/s3_4_2_4ii08.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_4_2_4/s3_4_2_4ii08.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_4_2_4ii07_s3_4_2_4ii07i():
    """
    test defaultAttributesApply = false and redefined as absent
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_4_2_4/s3_4_2_4ii07.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_4_2_4/s3_4_2_4ii07.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_4_2_4ii06_s3_4_2_4ii06i():
    """
    test defaultAttributesApply = true and redefined as false
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_4_2_4/s3_4_2_4ii06.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_4_2_4/s3_4_2_4ii06.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_4_2_4ii05_s3_4_2_4ii05i():
    """
    test defaultAttributesApply = false and redefined as true
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_4_2_4/s3_4_2_4ii05.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_4_2_4/s3_4_2_4ii05.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_4_2_4ii03_s3_4_2_4ii03i():
    """
    test defaultAttributesApply = false and redefined as absent
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_4_2_4/s3_4_2_4ii03.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_4_2_4/s3_4_2_4ii03.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_4_2_4ii02_s3_4_2_4ii02i():
    """
    test defaultAttributesApply = false
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_4_2_4/s3_4_2_4ii02.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_4_2_4/s3_4_2_4ii02.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_4_2_4ii01_s3_4_2_4ii01i():
    """
    test defaultAttributesApply = false, across multiple schema documents
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_4_2_4/s3_4_2_4ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_4_2_4/s3_4_2_4ii01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_4_2_4v13_s3_4_2_4v13i():
    """
    test defaultAttributesApply is absent, and ref attribute in
    attributeGroup
    """
    assert_bindings(
        schema="ibmData/valid/S3_4_2_4/s3_4_2_4v13.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_4_2_4/s3_4_2_4v13.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_4_2_4v03_s3_4_2_4v03i():
    """
    test defaultAttributesApply = true
    """
    assert_bindings(
        schema="ibmData/valid/S3_4_2_4/s3_4_2_4v03.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_4_2_4/s3_4_2_4v03.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_4_2_4v02_s3_4_2_4v02i():
    """
    test defaultAttributesApply = false
    """
    assert_bindings(
        schema="ibmData/valid/S3_4_2_4/s3_4_2_4v02.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_4_2_4/s3_4_2_4v02.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_4_2_4v01_s3_4_2_4v01i():
    """
    test defaultAttributesApply is absent
    """
    assert_bindings(
        schema="ibmData/valid/S3_4_2_4/s3_4_2_4v01.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_4_2_4/s3_4_2_4v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s2_7_2ii01_s2_7_2ii01i():
    """
    default values for xsi:nil
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S2_7_2/s2_7_2ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S2_7_2/s2_7_2ii01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


def test_s2_7_2v01_s2_7_2v01i():
    """
    Structures introduces a mechanism for signaling that an element
    must be accepted as 'valid'  when it has no content despite a content
    type which                  does not require or even necessarily allow
    empty content. An element can be 'valid'                   without
    content if it has the attribute xsi:nil  with the value true. An
    element                  so labeled must  be empty, but can carry
    attributes if permitted by the corresponding                  complex
    type.
    """
    assert_bindings(
        schema="ibmData/valid/S2_7_2/s2_7_2v01.xsd",
        is_valid=True,
        instance="ibmData/valid/S2_7_2/s2_7_2v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.schema11
def test_s2_7_1ii02_s2_7_1ii02i():
    """
    When an xsi:type attribute appears on an element, and has a QName as
    its value,  but the QName does not resolve to a known type definition,
    processors are now   required to "fall back" to lax validation, using
    the declared {type definition}    of the governing element declaration
    as the governing type definition.
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S2_7_1/s2_7_1ii02.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S2_7_1/s2_7_1ii02.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s2_7_1ii01_s2_7_1ii01i():
    """
    xsi:type must resolve to a type definition
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S2_7_1/s2_7_1ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S2_7_1/s2_7_1ii01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s2_7_1v01_s2_7_1v01i():
    """
    xsi:type must resolve to a type definition
    """
    assert_bindings(
        schema="ibmData/valid/S2_7_1/s2_7_1v01.xsd",
        is_valid=True,
        instance="ibmData/valid/S2_7_1/s2_7_1v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_3_6v02_d3_3_6v02i():
    """
    Lexical representation +INF for double
    """
    assert_bindings(
        schema="ibmData/valid/D3_3_6/d3_3_6v02.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_3_6/d3_3_6v02.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_3_6v01_d3_3_6v01i():
    """
    Valid test for +0 and -0 bound checking
    """
    assert_bindings(
        schema="ibmData/valid/D3_3_6/d3_3_6v01.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_3_6/d3_3_6v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_8_6ii01_s3_8_6ii01i():
    """
    tighter rule for EDC as regards the type of an element that matches a
    wildcard
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_8_6/s3_8_6ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_8_6/s3_8_6ii01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_8_6v01_s3_8_6v01i():
    """
    tighter rule for EDC as regards the type of an element that matches a
    wildcard
    """
    assert_bindings(
        schema="ibmData/valid/S3_8_6/s3_8_6v01.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_8_6/s3_8_6v01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_16ii07_d4_3_16ii07i():
    """
    Tests the simpleType dateTime and its facet with explicitTimezone
    constraint checks in derivations of simpleTypes
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_16/d4_3_16ii07.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_16/d4_3_16ii07.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_16ii06_d4_3_16ii06i():
    """
    Tests the simpleType dateTime and its facet with explicitTimezone
    constraint checks in derivations of simpleTypes
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_16/d4_3_16ii06.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_16/d4_3_16ii06.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_16ii05_d4_3_16ii05i():
    """
    Tests the simpleType dateTime and its facets, explicitTimezone
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_16/d4_3_16ii05.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_16/d4_3_16ii05.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_16ii04_d4_3_16ii04i():
    """
    Tests the simpleType dateTime and its facets explicitionTimezone, used
    with unions
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_16/d4_3_16ii04.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_16/d4_3_16ii04.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_16ii03_d4_3_16ii03i():
    """
    Tests the simpleType dateTime and its facets explicitTimezone, used in
    lists
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_16/d4_3_16ii03.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_16/d4_3_16ii03.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_16ii02_d4_3_16ii02i():
    """
    Tests the simpleType dateTime and its explicitTimezone facets and its
    use in attributes
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_16/d4_3_16ii02.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_16/d4_3_16ii02.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_16ii01_d4_3_16ii01i():
    """
    invalid dateTime values
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_16/d4_3_16ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_16/d4_3_16ii01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_16v07_d4_3_16v07i():
    """
    Tests the simpleType dateTime and its facets with explicitTimezone
    constraint checks in derivations of simpleTypes
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_16/d4_3_16v07.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_16/d4_3_16v07.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_16v06_d4_3_16v06i():
    """
    Tests the simpleType dateTime and its facet with explicitTimezone
    constraint checks in derivations of simpleTypes
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_16/d4_3_16v06.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_16/d4_3_16v06.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_16v05_d4_3_16v05i():
    """
    Tests the simpleType dateTime and its facets, explicitTimezone
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_16/d4_3_16v05.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_16/d4_3_16v05.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_16v04_d4_3_16v04i():
    """
    Tests the simpleType dateTime and its facet, explicitTimezone used
    with unions
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_16/d4_3_16v04.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_16/d4_3_16v04.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_16v03_d4_3_16v03i():
    """
    Tests the simpleType precisionDecimal and its facet, explicitTimezone,
    used in lists
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_16/d4_3_16v03.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_16/d4_3_16v03.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_16v02_d4_3_16v02i():
    """
    Tests the simpleType dateTime and its facets, explicitTimezone and its
    use in elements
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_16/d4_3_16v02.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_16/d4_3_16v02.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_16v01_d4_3_16v01i():
    """
    Tests the simpleType dateTime and its facets, explicitTimezone and its
    use in elements
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_16/d4_3_16v01.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_16/d4_3_16v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_3_5v02_d3_3_5v02i():
    """
    lexical representation +INF for float
    """
    assert_bindings(
        schema="ibmData/valid/D3_3_5/d3_3_5v02.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_3_5/d3_3_5v02.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_3_5v01_d3_3_5v01i():
    """
    Valid test for +0 and -0 bound checking
    """
    assert_bindings(
        schema="ibmData/valid/D3_3_5/d3_3_5v01.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_3_5/d3_3_5v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_3_11v01_d3_3_11v01i():
    """
    A day is a calendar (or "local time") day in each timezone, including
    the timezones outside of +12:00 through -11:59 inclusive.
    """
    assert_bindings(
        schema="ibmData/valid/D3_3_11/d3_3_11v01.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_3_11/d3_3_11v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_3_12v01_d3_3_12v01i():
    """
    A day is a calendar (or "local time") day in each timezone, including
    the timezones outside of +12:00 through -11:59 inclusive.
    """
    assert_bindings(
        schema="ibmData/valid/D3_3_12/d3_3_12v01.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_3_12/d3_3_12v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_3_13v01_d3_3_13v01i():
    """
    A day is a calendar (or "local time") day in each timezone, including
    the timezones outside of +12:00 through -11:59 inclusive.
    """
    assert_bindings(
        schema="ibmData/valid/D3_3_13/d3_3_13v01.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_3_13/d3_3_13v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_3_14v01_d3_3_14v01i():
    """
    A day is a calendar (or "local time") day in each timezone, including
    the timezones outside of +12:00 through -11:59 inclusive.
    """
    assert_bindings(
        schema="ibmData/valid/D3_3_14/d3_3_14v01.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_3_14/d3_3_14v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4ii27_s3_3_4ii27i():
    """
    ID on root does not denote any element
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_3_4/s3_3_4ii27.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_3_4/s3_3_4ii27.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4ii26_s3_3_4ii26i():
    """
    ID on root does not denote any element
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_3_4/s3_3_4ii26.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_3_4/s3_3_4ii26.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4ii25_s3_3_4ii25i():
    """
    Multiple attributes of type ID with default value
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_3_4/s3_3_4ii25.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_3_4/s3_3_4ii25.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4ii24_s3_3_4ii24i():
    """
    xs:ID/IDREF with default value on attribute
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_3_4/s3_3_4ii24.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_3_4/s3_3_4ii24.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4ii23_s3_3_4ii23i():
    """
    xs:ID with default value on attribute, and xs:IDREF on element with
    invalid value
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_3_4/s3_3_4ii23.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_3_4/s3_3_4ii23.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4ii22_s3_3_4ii22i():
    """
    Multiple attributes of type ID
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_3_4/s3_3_4ii22.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_3_4/s3_3_4ii22.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4ii21_s3_3_4ii21i():
    """
    Multiple attributes of type ID
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_3_4/s3_3_4ii21.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_3_4/s3_3_4ii21.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4ii20_s3_3_4ii20i():
    """
    Multiple attributes of type ID, invalid idref value on element
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_3_4/s3_3_4ii20.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_3_4/s3_3_4ii20.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4ii19_s3_3_4ii19i():
    """
    Multiple attributes of type ID, complexContent, with invalid idref
    value on element
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_3_4/s3_3_4ii19.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_3_4/s3_3_4ii19.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4ii18_s3_3_4ii18i():
    """
    Unions involving ID in elements, invalid idref value on element
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_3_4/s3_3_4ii18.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_3_4/s3_3_4ii18.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4ii17_s3_3_4ii17i():
    """
    Unions involving ID in elements, invalid idref value on attribute
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_3_4/s3_3_4ii17.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_3_4/s3_3_4ii17.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4ii16_s3_3_4ii16i():
    """
    Unions involving ID in attributes, invalid idref value on attribute
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_3_4/s3_3_4ii16.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_3_4/s3_3_4ii16.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4ii15_s3_3_4ii15i():
    """
    Unions involving ID in elements, invalid idref value on element
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_3_4/s3_3_4ii15.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_3_4/s3_3_4ii15.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4ii14_s3_3_4ii14i():
    """
    lists of ID, simpleContent, invalid idref value on element
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_3_4/s3_3_4ii14.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_3_4/s3_3_4ii14.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4ii13_s3_3_4ii13i():
    """
    lists of ID, simpleContent, invalid idref value on attribute
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_3_4/s3_3_4ii13.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_3_4/s3_3_4ii13.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4ii12_s3_3_4ii12i():
    """
    lists of ID, invalid idref value on attribute and element
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_3_4/s3_3_4ii12.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_3_4/s3_3_4ii12.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4ii11_s3_3_4ii11i():
    """
    lists of ID on attributes, invalid idref value on attribute
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_3_4/s3_3_4ii11.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_3_4/s3_3_4ii11.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4ii10_s3_3_4ii10i():
    """
    Unions involving ID
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_3_4/s3_3_4ii10.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_3_4/s3_3_4ii10.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4ii09_s3_3_4ii09i():
    """
    lists of ID, invalid value on idref element
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_3_4/s3_3_4ii09.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_3_4/s3_3_4ii09.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4ii08_s3_3_4ii08i():
    """
    lists of ID, invalid ID value on list of ids
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_3_4/s3_3_4ii08.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_3_4/s3_3_4ii08.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4ii07_s3_3_4ii07i():
    """
    lists of ID, naive test case on elements
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_3_4/s3_3_4ii07.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_3_4/s3_3_4ii07.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4ii06_s3_3_4ii06i():
    """
    xs:ID/IDREF with default value on attribute
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_3_4/s3_3_4ii06.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_3_4/s3_3_4ii06.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4ii05_s3_3_4ii05i():
    """
    xs:ID/IDREF with default value on attribute, invalid id value override
    the default value
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_3_4/s3_3_4ii05.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_3_4/s3_3_4ii05.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4ii04_s3_3_4ii04i():
    """
    xs:ID/IDREF with fixed value on attribute
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_3_4/s3_3_4ii04.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_3_4/s3_3_4ii04.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4ii03_s3_3_4ii03i():
    """
    Multiple attributes of type ID, invalid id value
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_3_4/s3_3_4ii03.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_3_4/s3_3_4ii03.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4ii02_s3_3_4ii02i():
    """
    Multiple attributes of type ID
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_3_4/s3_3_4ii02.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_3_4/s3_3_4ii02.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4ii01_s3_3_4ii01i():
    """
    Multiple attributes of type ID, with restriction on enum
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_3_4/s3_3_4ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_3_4/s3_3_4ii01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4v30_s3_3_4v30i():
    """
    equality of an atomic value with a singleton list in ID/IDREF
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_4/s3_3_4v30.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_4/s3_3_4v30.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4v29_s3_3_4v29i():
    """
    Multiple attributes of type ID with default value
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_4/s3_3_4v29.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_4/s3_3_4v29.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4v28_s3_3_4v28i():
    """
    xs:ID/IDREF with default value on attribute
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_4/s3_3_4v28.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_4/s3_3_4v28.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4v27_s3_3_4v27i():
    """
    xs:ID/IDREF with default value on attribute
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_4/s3_3_4v27.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_4/s3_3_4v27.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4v26_s3_3_4v26i():
    """
    xs:ID with default value on attribute, and xs:IDREF on element
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_4/s3_3_4v26.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_4/s3_3_4v26.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4v25_s3_3_4v25i():
    """
    Multiple attributes of type ID
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_4/s3_3_4v25.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_4/s3_3_4v25.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4v24_s3_3_4v24i():
    """
    Multiple attributes of type ID
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_4/s3_3_4v24.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_4/s3_3_4v24.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4v23_s3_3_4v23i():
    """
    Multiple attributes of type ID
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_4/s3_3_4v23.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_4/s3_3_4v23.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4v22_s3_3_4v22i():
    """
    Multiple attributes of type ID
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_4/s3_3_4v22.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_4/s3_3_4v22.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4v21_s3_3_4v21i():
    """
    lists of ID, simpleContent
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_4/s3_3_4v21.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_4/s3_3_4v21.xml",
        instance_is_valid=True,
        class_name="Wrapper",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4v20_s3_3_4v20i():
    """
    Unions involving ID in elements, attributes
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_4/s3_3_4v20.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_4/s3_3_4v20.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4v19_s3_3_4v19i():
    """
    Unions involving ID in elements, attributes
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_4/s3_3_4v19.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_4/s3_3_4v19.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4v18_s3_3_4v18i():
    """
    Unions involving ID in attributes
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_4/s3_3_4v18.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_4/s3_3_4v18.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4v17_s3_3_4v17i():
    """
    Unions involving ID in elements
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_4/s3_3_4v17.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_4/s3_3_4v17.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4v16_s3_3_4v16i():
    """
    lists of ID, simpleContent
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_4/s3_3_4v16.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_4/s3_3_4v16.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4v15_s3_3_4v15i():
    """
    lists of ID, simpleContent
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_4/s3_3_4v15.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_4/s3_3_4v15.xml",
        instance_is_valid=True,
        class_name="Wrapper",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4v14_s3_3_4v14i():
    """
    lists of ID, naive test case on elements
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_4/s3_3_4v14.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_4/s3_3_4v14.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4v13_s3_3_4v13i():
    """
    lists of ID on attributes
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_4/s3_3_4v13.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_4/s3_3_4v13.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4v12_s3_3_4v12i():
    """
    Multiple attributes of type ID
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_4/s3_3_4v12.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_4/s3_3_4v12.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4v11_s3_3_4v11i():
    """
    Unions involving ID
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_4/s3_3_4v11.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_4/s3_3_4v11.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4v10_s3_3_4v10i():
    """
    lists of ID, naive test case on elements
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_4/s3_3_4v10.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_4/s3_3_4v10.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4v09_s3_3_4v09i():
    """
    xs:ID/IDREF with fixed value on attribute
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_4/s3_3_4v09.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_4/s3_3_4v09.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4v08_s3_3_4v08i():
    """
    xs:ID/IDREF with default value on attribute
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_4/s3_3_4v08.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_4/s3_3_4v08.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4v07_s3_3_4v07i():
    """
    xs:ID/IDREF with fixed value on attribute
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_4/s3_3_4v07.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_4/s3_3_4v07.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4v06_s3_3_4v06i():
    """
    xs:ID/IDREF with default value on attribute
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_4/s3_3_4v06.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_4/s3_3_4v06.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4v05_s3_3_4v05i():
    """
    xs:ENTITY with default value on attribute
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_4/s3_3_4v05.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_4/s3_3_4v05.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4v04_s3_3_4v04i():
    """
    xs:ENTITIES with default value on attribute
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_4/s3_3_4v04.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_4/s3_3_4v04.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4v03_s3_3_4v03i():
    """
    xs:ID/IDREF with fixed value on attribute
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_4/s3_3_4v03.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_4/s3_3_4v03.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4v02_s3_3_4v02i():
    """
    xs:ID/IDREF with xs:anyAttribute
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_4/s3_3_4v02.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_4/s3_3_4v02.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_3_4v01_s3_3_4v01i():
    """
    xs:ID/IDREF with xs:anyAttribute
    """
    assert_bindings(
        schema="ibmData/valid/S3_3_4/s3_3_4v01.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_3_4/s3_3_4v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s2_2_4ii03_s2_2_4ii03i():
    """
    Tests for duplication on components with keys and uniques
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S2_2_4/s2_2_4ii03.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S2_2_4/s2_2_4ii03.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s2_2_4ii02_s2_2_4ii02i():
    """
    Tests for duplication on components with identity constraints Checks
    that ic referrals works when nested
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S2_2_4/s2_2_4ii02.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S2_2_4/s2_2_4ii02.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s2_2_4ii01_s2_2_4ii01i():
    """
    test attribute which is required as declared in key is abscent
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S2_2_4/s2_2_4ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S2_2_4/s2_2_4ii01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s2_2_4v03_s2_2_4v03i():
    """
    Tests unresolvable xpath
    """
    assert_bindings(
        schema="ibmData/valid/S2_2_4/s2_2_4v03.xsd",
        is_valid=True,
        instance="ibmData/valid/S2_2_4/s2_2_4v03.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s2_2_4v02_s2_2_4v02i():
    """
    Valid test for identity constraint referrals
    """
    assert_bindings(
        schema="ibmData/valid/S2_2_4/s2_2_4v02.xsd",
        is_valid=True,
        instance="ibmData/valid/S2_2_4/s2_2_4v02.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s2_2_4v01_s2_2_4v01i():
    """
    Valid test for identity constraint referrals with annotation
    """
    assert_bindings(
        schema="ibmData/valid/S2_2_4/s2_2_4v01.xsd",
        is_valid=True,
        instance="ibmData/valid/S2_2_4/s2_2_4v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d2_4_1_2v01_d2_4_1_2v01i():
    """
    test Units of length for list datatype.
    """
    assert_bindings(
        schema="ibmData/valid/D2_4_1_2/d2_4_1_2v01.xsd",
        is_valid=True,
        instance="ibmData/valid/D2_4_1_2/d2_4_1_2v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_4_1ii05_s3_4_1ii05i():
    """
    Tests derivation by restriction with openContent mode suffix in base
    type
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_4_1/s3_4_1ii05.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_4_1/s3_4_1ii05.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_4_1ii04_s3_4_1ii04i():
    """
    Tests wildcard in opencontent with restrictions (notQName)
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_4_1/s3_4_1ii04.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_4_1/s3_4_1ii04.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_4_1ii03_s3_4_1ii03i():
    """
    Tests defaultOpenContent: when openContent is present in CT,
    defaultOpenContent should not be used
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_4_1/s3_4_1ii03.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_4_1/s3_4_1ii03.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_4_1ii02_s3_4_1ii02i():
    """
    Tests defaultOpenContent: appliesToEmpty="false"
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_4_1/s3_4_1ii02.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_4_1/s3_4_1ii02.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_4_1ii01_s3_4_1ii01i():
    """
    3.4.4.3 Element Sequence Locally valid (Complex Content) Validation
    rule 2. (openContent)             mode = suffix BUT wildcard inserted
    in front of and in between CT group particles
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_4_1/s3_4_1ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_4_1/s3_4_1ii01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_4_1v11_s3_4_1v11i():
    """
    complexType/@mixed
    """
    assert_bindings(
        schema="ibmData/valid/S3_4_1/s3_4_1v11.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_4_1/s3_4_1v11.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_4_1v10_s3_4_1v10i():
    """
    Tests derivation by extension with openContent mode interleave in both
    type and its derived type
    """
    assert_bindings(
        schema="ibmData/valid/S3_4_1/s3_4_1v10.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_4_1/s3_4_1v10.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_4_1v09_s3_4_1v09i():
    """
    Tests derivation by restriction with openContent mode interleave in
    base type
    """
    assert_bindings(
        schema="ibmData/valid/S3_4_1/s3_4_1v09.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_4_1/s3_4_1v09.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_4_1v08_s3_4_1v08i():
    """
    Tests derivation by extension with openContent mode interleave in
    derived type and suffix in its base type
    """
    assert_bindings(
        schema="ibmData/valid/S3_4_1/s3_4_1v08.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_4_1/s3_4_1v08.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
@pytest.mark.xfail
def test_s3_4_1v07_s3_4_1v07i():
    """
    Tests derivation by extension with openContent mode suffix in both
    type and its derived type
    """
    assert_bindings(
        schema="ibmData/valid/S3_4_1/s3_4_1v07.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_4_1/s3_4_1v07.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
@pytest.mark.xfail
def test_s3_4_1v06_s3_4_1v06i():
    """
    Tests openContent in complexType derived by extension
    """
    assert_bindings(
        schema="ibmData/valid/S3_4_1/s3_4_1v06.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_4_1/s3_4_1v06.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
@pytest.mark.xfail
def test_s3_4_1v05_s3_4_1v05i():
    """
    Tests openContent in complexType derived by restriction
    """
    assert_bindings(
        schema="ibmData/valid/S3_4_1/s3_4_1v05.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_4_1/s3_4_1v05.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
@pytest.mark.xfail
def test_s3_4_1v04_s3_4_1v04i():
    """
    Tests defaultOpenContent in suffix mode
    """
    assert_bindings(
        schema="ibmData/valid/S3_4_1/s3_4_1v04.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_4_1/s3_4_1v04.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_4_1v03_s3_4_1v03i():
    """
    Tests openContent for empty content model
    """
    assert_bindings(
        schema="ibmData/valid/S3_4_1/s3_4_1v03.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_4_1/s3_4_1v03.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
@pytest.mark.xfail
def test_s3_4_1v02_s3_4_1v02i():
    """
    Tests defaultOpenContent for CT not empty
    """
    assert_bindings(
        schema="ibmData/valid/S3_4_1/s3_4_1v02.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_4_1/s3_4_1v02.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
@pytest.mark.xfail
def test_s3_4_1v01_s3_4_1v01i():
    """
    Tests defaultOpenContent: appliesToEmpty="true"
    """
    assert_bindings(
        schema="ibmData/valid/S3_4_1/s3_4_1v01.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_4_1/s3_4_1v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d6_gii04_d6_gii04i():
    """
    invalid instance use of hyphens within square brackets in regular
    expressions [bc-]
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D6_G/d6_gii04.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D6_G/d6_gii04.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d6_gii03_d6_gii03i():
    """
    invalid instance use of hyphens within square brackets in regular
    expressions [-abc]
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D6_G/d6_gii03.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D6_G/d6_gii03.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d6_gii02_d6_gii02i():
    """
    invalid instance use of hyphens within square brackets in regular
    expressions [abc-[c]]
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D6_G/d6_gii02.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D6_G/d6_gii02.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d6_gii01_d6_gii01i():
    """
    invalid instance use of hyphens within square brackets in regular
    expressions [a-c]
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D6_G/d6_gii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D6_G/d6_gii01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d6_gv04_d6_gv04i():
    """
    use of hyphens within square brackets in regular expressions [bc-]
    """
    assert_bindings(
        schema="ibmData/valid/D6_G/d6_gv04.xsd",
        is_valid=True,
        instance="ibmData/valid/D6_G/d6_gv04.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d6_gv03_d6_gv03i():
    """
    use of hyphens within square brackets in regular expressions [-abc]
    """
    assert_bindings(
        schema="ibmData/valid/D6_G/d6_gv03.xsd",
        is_valid=True,
        instance="ibmData/valid/D6_G/d6_gv03.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d6_gv02_d6_gv02i():
    """
    use of hyphens within square brackets in regular expressions [abc-[c]]
    """
    assert_bindings(
        schema="ibmData/valid/D6_G/d6_gv02.xsd",
        is_valid=True,
        instance="ibmData/valid/D6_G/d6_gv02.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d6_gv01_d6_gv01i():
    """
    use of hyphens within square brackets in regular expressions [a-c]
    """
    assert_bindings(
        schema="ibmData/valid/D6_G/d6_gv01.xsd",
        is_valid=True,
        instance="ibmData/valid/D6_G/d6_gv01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_4_6ii03_s3_4_6ii03i():
    """
    Tests notQName
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_4_6/s3_4_6ii03.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_4_6/s3_4_6ii03.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_4_6ii01_s3_4_6ii01i():
    """
    Instance document element has higher occurences than schema allows
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_4_6/s3_4_6ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_4_6/s3_4_6ii01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
@pytest.mark.xfail
def test_s3_4_6v08_s3_4_6v08i():
    """
    Restrict xs:all to xs:sequence
    """
    assert_bindings(
        schema="ibmData/valid/S3_4_6/s3_4_6v08.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_4_6/s3_4_6v08.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_4_6v05_s3_4_6v05i():
    """
    Tests maxOccurs > 1 for elements within all group
    """
    assert_bindings(
        schema="ibmData/valid/S3_4_6/s3_4_6v05.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_4_6/s3_4_6v05.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_4_6v04_s3_4_6v04i():
    """
    Tests restriction of all group
    """
    assert_bindings(
        schema="ibmData/valid/S3_4_6/s3_4_6v04.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_4_6/s3_4_6v04.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_4_6v01_s3_4_6v01i():
    """
    Wildcards are now allowed in xs:all
    """
    assert_bindings(
        schema="ibmData/valid/S3_4_6/s3_4_6v01.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_4_6/s3_4_6v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_6ii01_d4_3_6ii01i():
    """
    when the value is collapse, literals consisting solely of whitespace
    characters are reduced to the empty string.
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D4_3_6/d4_3_6ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D4_3_6/d4_3_6ii01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d4_3_6v01_d4_3_6v01i():
    """
    when the value is collapse, literals consisting solely of whitespace
    characters are reduced to the empty string.
    """
    assert_bindings(
        schema="ibmData/valid/D4_3_6/d4_3_6v01.xsd",
        is_valid=True,
        instance="ibmData/valid/D4_3_6/d4_3_6v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
@pytest.mark.xfail
def test_s2_2_2v03_s2_2_2v03i():
    """
    Tests for 1 substitution group head
    """
    assert_bindings(
        schema="ibmData/valid/S2_2_2/s2_2_2v03.xsd",
        is_valid=True,
        instance="ibmData/valid/S2_2_2/s2_2_2v03.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
@pytest.mark.xfail
def test_s2_2_2v02_s2_2_2v02i():
    """
    Tests multiple substitution group heads
    """
    assert_bindings(
        schema="ibmData/valid/S2_2_2/s2_2_2v02.xsd",
        is_valid=True,
        instance="ibmData/valid/S2_2_2/s2_2_2v02.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
@pytest.mark.xfail
def test_s2_2_2v01_s2_2_2v01i():
    """
    Tests abstract substitution group
    """
    assert_bindings(
        schema="ibmData/valid/S2_2_2/s2_2_2v01.xsd",
        is_valid=True,
        instance="ibmData/valid/S2_2_2/s2_2_2v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_target_namespace_005_target_namespace_005_2():
    """
    This example demonstrates 'targetNamespace' attribute on xs:attribute
    schema component.
    """
    assert_bindings(
        schema="ibmData/mixed/targetNamespace/tns5.xsd",
        is_valid=True,
        instance="ibmData/mixed/targetNamespace/tns5.xml",
        instance_is_valid=True,
        class_name="X",
        version="1.1",
    )


@pytest.mark.schema11
def test_target_namespace_004_target_namespace_004_2():
    """
    Composition of XML schemas via xs:import to be able to achive
    hetrogeneous namespaced elements                         in "one" XML
    document.
    """
    assert_bindings(
        schema="ibmData/mixed/targetNamespace/tns4.xsd",
        is_valid=True,
        instance="ibmData/mixed/targetNamespace/tns4.xml",
        instance_is_valid=True,
        class_name="X",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_3_9v01_d3_3_9v01i():
    """
    1a: chameleon include on unqualified names in XPath expressions
    1b: A calendar day with a very early timezone may be completely
    disjoint from a calendar day with a very late timezone.
    1c: A time in a timezone may convert to a UTC time on a different day.
    """
    assert_bindings(
        schema="ibmData/valid/D3_3_9/d3_3_9v01.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_3_9/d3_3_9v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_3_9v01_d3_3_9v01ai():
    """
    1a: chameleon include on unqualified names in XPath expressions
    1b: A calendar day with a very early timezone may be completely
    disjoint from a calendar day with a very late timezone.
    1c: A time in a timezone may convert to a UTC time on a different day.
    """
    assert_bindings(
        schema="ibmData/valid/D3_3_9/d3_3_9v01.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_3_9/d3_3_9v01a.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_3_9v01_d3_3_9v01bi():
    """
    1a: chameleon include on unqualified names in XPath expressions
    1b: A calendar day with a very early timezone may be completely
    disjoint from a calendar day with a very late timezone.
    1c: A time in a timezone may convert to a UTC time on a different day.
    """
    assert_bindings(
        schema="ibmData/valid/D3_3_9/d3_3_9v01.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_3_9/d3_3_9v01b.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_3_9v01_d3_3_9v01ci():
    """
    1a: chameleon include on unqualified names in XPath expressions
    1b: A calendar day with a very early timezone may be completely
    disjoint from a calendar day with a very late timezone.
    1c: A time in a timezone may convert to a UTC time on a different day.
    """
    assert_bindings(
        schema="ibmData/valid/D3_3_9/d3_3_9v01.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_3_9/d3_3_9v01c.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
@pytest.mark.xfail
def test_s3_12ii05_s3_12ii05i():
    """
    test xs:error as conditionally assigned type
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_12/s3_12ii05.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_12/s3_12ii05.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_12ii04_s3_12ii04i():
    """
    Basic type alternatives selecting invalid content.
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_12/s3_12ii04.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_12/s3_12ii04.xml",
        instance_is_valid=False,
        class_name="Invoice",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_12ii03_s3_12ii03i():
    """
    The type alternative is selects an invalid element using constructor
    functions and comparator operators.
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_12/s3_12ii03.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_12/s3_12ii03.xml",
        instance_is_valid=False,
        class_name="Shape",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_12ii02_s3_12ii02i():
    """
    The type alternative is selects an invalid element using comparator
    operators.
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_12/s3_12ii02.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_12/s3_12ii02.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_12ii01_s3_12ii01i():
    """
    The alternative type's value is an invalid float
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_12/s3_12ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_12/s3_12ii01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_12v11_s3_12v01i():
    """
    Attribute declarations can now be marked {inheritable}.
    """
    assert_bindings(
        schema="ibmData/valid/S3_12/s3_12v11.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_12/s3_12v11.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_12v10_s3_12v11i():
    """
    Basic type alternatives.             Selection of the alternative type
    is dertermined by evaluating a Constructor function and a Cast
    Expression on attribute values
    """
    assert_bindings(
        schema="ibmData/valid/S3_12/s3_12v10.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_12/s3_12v10.xml",
        instance_is_valid=True,
        class_name="Shape",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_12v09_s3_12v09i():
    """
    Basic type alternatives.
    """
    assert_bindings(
        schema="ibmData/valid/S3_12/s3_12v09.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_12/s3_12v09.xml",
        instance_is_valid=True,
        class_name="Invoice",
        version="1.1",
    )


@pytest.mark.schema11
@pytest.mark.xfail
def test_s3_12v08_s3_12v08i():
    """
    Basic type alternatives.             Selection of the alternative type
    is dertermined by evaluating an And operation on the presence of
    attributes in an element
    """
    assert_bindings(
        schema="ibmData/valid/S3_12/s3_12v08.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_12/s3_12v08.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_12v07_s3_12v07i():
    """
    Basic type alternatives.             Selection of the alternative type
    is dertermined by evaluating a Constructor function on attribute
    values
    """
    assert_bindings(
        schema="ibmData/valid/S3_12/s3_12v07.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_12/s3_12v07.xml",
        instance_is_valid=True,
        class_name="Shape",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_12v06_s3_12v06i():
    """
    Basic type alternatives.             Selection of the alternative type
    is dertermined by evaluating a path And and Or expressions with a
    comparator operator with an attribute's value
    """
    assert_bindings(
        schema="ibmData/valid/S3_12/s3_12v06.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_12/s3_12v06.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_12v05_s3_12v05i():
    """
    Basic type alternatives.             Selection of the alternative type
    is dertermined by evaluating a path And expression with a comparator
    operator with an attribute's value
    """
    assert_bindings(
        schema="ibmData/valid/S3_12/s3_12v05.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_12/s3_12v05.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_12v04_s3_12v04i():
    """
    Basic type alternatives.             For the first alternative type,
    the attribute whose value is to be selected by the alternative type's
    {test} expression is of type string.             The attribute value
    in the XML document contains a trailing space and will not normalized
    and selected by the alternate type.              For the second
    alternative type, the case of the attribute whose value is to be
    selected by the {test} expression is in a different case in the XML
    document.             In both cases, the alternative type should not
    be selected.
    """
    assert_bindings(
        schema="ibmData/valid/S3_12/s3_12v04.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_12/s3_12v04.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_12v03_s3_12v03i():
    """
    Basic type alternatives.                          The alternative type
    extends the base element's type.                          More that
    one alternative type is present. One of the alternative types is the
    default type.
    """
    assert_bindings(
        schema="ibmData/valid/S3_12/s3_12v03.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_12/s3_12v03.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_12v02_s3_12v02i():
    """
    Basic type alternatives. alternative element with a complexType child
    that is                          derived from the base element  type
    and no type attribute More that one alternative
    type is present. One of the alternative types is the default type.
    """
    assert_bindings(
        schema="ibmData/valid/S3_12/s3_12v02.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_12/s3_12v02.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_12v01_s3_12v01i():
    """
    Basic type alternatives. The alternative type extends the base
    element's type.              More that one alternative type is
    present. One of the alternative types is the default type.
    """
    assert_bindings(
        schema="ibmData/valid/S3_12/s3_12v01.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_12/s3_12v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_type_alternatives_006_type_alternatives_006_2():
    """
    Demonstrates XML Schema 1.1 type-alternatives.
    """
    assert_bindings(
        schema="ibmData/mixed/type-alternatives/test5.xsd",
        is_valid=True,
        instance="ibmData/mixed/type-alternatives/test5_1.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.1",
    )


@pytest.mark.schema11
def test_type_alternatives_006_type_alternatives_006_3():
    """
    Demonstrates XML Schema 1.1 type-alternatives.
    """
    assert_bindings(
        schema="ibmData/mixed/type-alternatives/test5.xsd",
        is_valid=True,
        instance="ibmData/mixed/type-alternatives/test5_2.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.1",
    )


@pytest.mark.schema11
def test_type_alternatives_005_type_alternatives_005_2():
    """
    Demonstrates XML Schema 1.1 type-alternatives. Using inheritable
    attributes in this example.
    """
    assert_bindings(
        schema="ibmData/mixed/type-alternatives/test4.xsd",
        is_valid=True,
        instance="ibmData/mixed/type-alternatives/test4_1.xml",
        instance_is_valid=True,
        class_name="Example",
        version="1.1",
    )


@pytest.mark.schema11
def test_type_alternatives_005_type_alternatives_005_3():
    """
    Demonstrates XML Schema 1.1 type-alternatives. Using inheritable
    attributes in this example.
    """
    assert_bindings(
        schema="ibmData/mixed/type-alternatives/test4.xsd",
        is_valid=True,
        instance="ibmData/mixed/type-alternatives/test4_2.xml",
        instance_is_valid=False,
        class_name="Example",
        version="1.1",
    )


@pytest.mark.schema11
def test_type_alternatives_004_type_alternatives_004_2():
    """
    Demonstrates XML Schema 1.1 type-alternatives. Using inheritable
    attributes and assertions along                         with type-
    alternatives.
    """
    assert_bindings(
        schema="ibmData/mixed/type-alternatives/test3.xsd",
        is_valid=True,
        instance="ibmData/mixed/type-alternatives/test3_1.xml",
        instance_is_valid=True,
        class_name="X",
        version="1.1",
    )


@pytest.mark.schema11
def test_type_alternatives_004_type_alternatives_004_3():
    """
    Demonstrates XML Schema 1.1 type-alternatives. Using inheritable
    attributes and assertions along                         with type-
    alternatives.
    """
    assert_bindings(
        schema="ibmData/mixed/type-alternatives/test3.xsd",
        is_valid=True,
        instance="ibmData/mixed/type-alternatives/test3_2.xml",
        instance_is_valid=False,
        class_name="X",
        version="1.1",
    )


@pytest.mark.schema11
@pytest.mark.xfail
def test_type_alternatives_003_type_alternatives_003_2():
    """
    Demonstrates XML Schema 1.1 type-alternatives. In this example, schema
    type definition's are provided                         as children of
    xs:alternative instructions.
    """
    assert_bindings(
        schema="ibmData/mixed/type-alternatives/test2_1.xsd",
        is_valid=True,
        instance="ibmData/mixed/type-alternatives/test2.xml",
        instance_is_valid=True,
        class_name="Example",
        version="1.1",
    )


@pytest.mark.schema11
@pytest.mark.xfail
def test_type_alternatives_002_type_alternatives_002_2():
    """
    Demonstrates XML Schema 1.1 type-alternatives.
    """
    assert_bindings(
        schema="ibmData/mixed/type-alternatives/test2.xsd",
        is_valid=True,
        instance="ibmData/mixed/type-alternatives/test2.xml",
        instance_is_valid=True,
        class_name="Example",
        version="1.1",
    )


@pytest.mark.schema11
def test_type_alternatives_001_type_alternatives_001_2():
    """
    Demonstrates XML Schema 1.1 type-alternatives.
    """
    assert_bindings(
        schema="ibmData/mixed/type-alternatives/test1.xsd",
        is_valid=True,
        instance="ibmData/mixed/type-alternatives/test1.xml",
        instance_is_valid=True,
        class_name="Shapes",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_16_2ii07_s3_16_2ii07i():
    """
    xsi:type used to name a member of a restricted union type
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_16_2/s3_16_2ii07.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_16_2/s3_16_2ii07.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_16_2ii06_s3_16_2ii06i():
    """
    xsi:type used to name a member of a restricted union type
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_16_2/s3_16_2ii06.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_16_2/s3_16_2ii06.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_16_2ii05_s3_16_2ii05i():
    """
    xsi:type used to name a member of a restricted union type
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_16_2/s3_16_2ii05.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_16_2/s3_16_2ii05.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_16_2ii04_s3_16_2ii04i():
    """
    Types derived by restriction from a union type
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_16_2/s3_16_2ii04.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_16_2/s3_16_2ii04.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_16_2ii03_s3_16_2ii03i():
    """
    tests restriction facet in intervening union
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_16_2/s3_16_2ii03.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_16_2/s3_16_2ii03.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_16_2ii02_s3_16_2ii02i():
    """
    tests restriction facet in intervening union
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_16_2/s3_16_2ii02.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_16_2/s3_16_2ii02.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_16_2ii01_s3_16_2ii01i():
    """
    tests restriction facet in intervening union
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_16_2/s3_16_2ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_16_2/s3_16_2ii01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


def test_s3_16_2v07_s3_16_2v07i():
    """
    xsi:type used to name a member of a restricted union type
    """
    assert_bindings(
        schema="ibmData/valid/S3_16_2/s3_16_2v07.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_16_2/s3_16_2v07.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.schema11
def test_s3_16_2v06_s3_16_2v06i():
    """
    Union of unions
    """
    assert_bindings(
        schema="ibmData/valid/S3_16_2/s3_16_2v06.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_16_2/s3_16_2v06.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_16_2v05_s3_16_2v05i():
    """
    xsi:type used to name a member of a restricted union type
    """
    assert_bindings(
        schema="ibmData/valid/S3_16_2/s3_16_2v05.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_16_2/s3_16_2v05.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_16_2v04_s3_16_2v04i():
    """
    Types derived by restriction from a union type
    """
    assert_bindings(
        schema="ibmData/valid/S3_16_2/s3_16_2v04.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_16_2/s3_16_2v04.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_16_2v03_s3_16_2v03i():
    """
    tests restriction facet in intervening union
    """
    assert_bindings(
        schema="ibmData/valid/S3_16_2/s3_16_2v03.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_16_2/s3_16_2v03.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_16_2v02_s3_16_2v02i():
    """
    Types derived by restriction from a union type
    """
    assert_bindings(
        schema="ibmData/valid/S3_16_2/s3_16_2v02.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_16_2/s3_16_2v02.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_16_2v01_s3_16_2v01i():
    """
    tests restriction facet in intervening union
    """
    assert_bindings(
        schema="ibmData/valid/S3_16_2/s3_16_2v01.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_16_2/s3_16_2v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d2_4_1_2ii01_d2_4_1_2ii01i():
    """
    test Units of length for list datatype
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D2_4_1_2/d2_4_1_2ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D2_4_1_2/d2_4_1_2ii01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_3_17ii01_d3_3_17ii01i():
    """
    test base64Binary datatype
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D3_3_17/d3_3_17ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D3_3_17/d3_3_17ii01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_3_17v01_d3_3_17v01i():
    """
    test Units of length for base64Binary datatype.
    """
    assert_bindings(
        schema="ibmData/valid/D3_3_17/d3_3_17v01.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_3_17/d3_3_17v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_3_16ii02_d3_3_16ii02i():
    """
    test Units of length for hexBinary datatype
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D3_3_16/d3_3_16ii02.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D3_3_16/d3_3_16ii02.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_3_16ii01_d3_3_16ii01i():
    """
    test hexBinary datatype
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D3_3_16/d3_3_16ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D3_3_16/d3_3_16ii01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


def test_d3_3_16v01_d3_3_16v01i():
    """
    test Units of length for hexBinary datatype.
    """
    assert_bindings(
        schema="ibmData/valid/D3_3_16/d3_3_16v01.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_3_16/d3_3_16v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.schema11
def test_d3_4_24ii01_d3_4_24ii01i():
    """
    The possibility of a leading sign is allowed for unsignedByte.
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D3_4_24/d3_4_24ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D3_4_24/d3_4_24ii01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_23ii01_d3_4_23ii01i():
    """
    The possibility of a leading sign is allowed for unsignedShort.
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D3_4_23/d3_4_23ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D3_4_23/d3_4_23ii01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_22ii01_d3_4_22ii01i():
    """
    The possibility of a leading sign is allowed for unsignedInt.
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D3_4_22/d3_4_22ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D3_4_22/d3_4_22ii01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_21ii01_d3_4_21ii01i():
    """
    test unsignedLong invalid instance
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D3_4_21/d3_4_21ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D3_4_21/d3_4_21ii01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_24v01_d3_4_24v01i():
    """
    The possibility of a leading sign is allowed for unsignedByte.
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_24/d3_4_24v01.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_24/d3_4_24v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_23v01_d3_4_23v01i():
    """
    The possibility of a leading sign is allowed for unsignedInt.
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_23/d3_4_23v01.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_23/d3_4_23v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_22v01_d3_4_22v01i():
    """
    The possibility of a leading sign is allowed for unsignedInt.
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_22/d3_4_22v01.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_22/d3_4_22v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_21v01_d3_4_21v01i():
    """
    test unsignedLong
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_21/d3_4_21v01.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_21/d3_4_21v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
@pytest.mark.xfail
def test_vc_009_vc_009_2():

    assert_bindings(
        schema="ibmData/mixed/VC/test6.xsd",
        is_valid=True,
        instance="ibmData/mixed/VC/test6.xml",
        instance_is_valid=True,
        class_name="Example",
        version="1.1",
    )


@pytest.mark.schema11
@pytest.mark.xfail
def test_vc_008_vc_008_2():

    assert_bindings(
        schema="ibmData/mixed/VC/test5_1.xsd",
        is_valid=True,
        instance="ibmData/mixed/VC/test5.xml",
        instance_is_valid=True,
        class_name="Example",
        version="1.1",
    )


@pytest.mark.schema11
def test_vc_007_vc_007_2():

    assert_bindings(
        schema="ibmData/mixed/VC/test4.xsd",
        is_valid=True,
        instance="ibmData/mixed/VC/test4_1.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.1",
    )


@pytest.mark.schema11
@pytest.mark.xfail
def test_vc_007_vc_007_3():

    assert_bindings(
        schema="ibmData/mixed/VC/test4.xsd",
        is_valid=True,
        instance="ibmData/mixed/VC/test4_2.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.1",
    )


@pytest.mark.schema11
def test_vc_005_vc_005_2():

    assert_bindings(
        schema="ibmData/mixed/VC/test3.xsd",
        is_valid=True,
        instance="ibmData/mixed/VC/test3.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.1",
    )


@pytest.mark.schema11
def test_vc_003_vc_003_2():

    assert_bindings(
        schema="ibmData/mixed/VC/test2.xsd",
        is_valid=True,
        instance="ibmData/mixed/VC/test2.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.1",
    )


@pytest.mark.schema11
def test_vc_001_vc_001_2():

    assert_bindings(
        schema="ibmData/mixed/VC/test1.xsd",
        is_valid=True,
        instance="ibmData/mixed/VC/test1_1.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.1",
    )


@pytest.mark.schema11
def test_vc_001_vc_001_3():

    assert_bindings(
        schema="ibmData/mixed/VC/test1.xsd",
        is_valid=True,
        instance="ibmData/mixed/VC/test1_2.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.1",
    )


def test_s3_10_1ii09_s3_10_1ii09i():
    """
    the keyword ##definedSibling can be used to exclude all elements
    explicitly mentioned in a content model (and all elements
    substitutable for those elements)
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_10_1/s3_10_1ii09.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_10_1/s3_10_1ii09.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_s3_10_1ii08_s3_10_1ii08i():
    """
    the keyword ##definedSibling can be used to exclude all elements
    explicitly mentioned in a content model
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_10_1/s3_10_1ii08.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_10_1/s3_10_1ii08.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_s3_10_1ii07_s3_10_1ii07i():
    """
    Tests namespace attribute in wildcard
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_10_1/s3_10_1ii07.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_10_1/s3_10_1ii07.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.schema11
def test_s3_10_1ii06_s3_10_1ii06i():
    """
    invalid element in instance document as it matches the namespace in
    notNamespace list in wildcard
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_10_1/s3_10_1ii06.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_10_1/s3_10_1ii06.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


def test_s3_10_1ii04_s3_10_1ii04i():
    """
    invalid element in instance document as it does not match ns of
    wildcard
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_10_1/s3_10_1ii04.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_10_1/s3_10_1ii04.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_s3_10_1ii03_s3_10_1ii03i():
    """
    invalid element in instance document as it does not match ns of
    wildcard
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_10_1/s3_10_1ii03.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_10_1/s3_10_1ii03.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.schema11
def test_s3_10_1ii02_s3_10_1ii02i():
    """
    invalid element in instance document as it does not match ns of
    wildcard
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_10_1/s3_10_1ii02.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_10_1/s3_10_1ii02.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


def test_s3_10_1ii01_s3_10_1ii01i():
    """
    invalid element in instance document as it does not match ns of
    wildcard
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_10_1/s3_10_1ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_10_1/s3_10_1ii01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.schema11
def test_s3_10_1v07_s3_10_1v07i():
    """
    skip wildcards now excluded from EDC constraint
    """
    assert_bindings(
        schema="ibmData/valid/S3_10_1/s3_10_1v07.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_10_1/s3_10_1v07.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_10_1v06_s3_10_1v06i():
    """
    the keyword ##definedSibling can be used to exclude all elements
    explicitly mentioned in a content model (and all elements
    substitutable for those elements)
    """
    assert_bindings(
        schema="ibmData/valid/S3_10_1/s3_10_1v06.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_10_1/s3_10_1v06.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_10_1v05_s3_10_1v05i():
    """
    the keyword ##definedSibling can be used to exclude all elements
    explicitly mentioned in a content model
    """
    assert_bindings(
        schema="ibmData/valid/S3_10_1/s3_10_1v05.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_10_1/s3_10_1v05.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
@pytest.mark.xfail
def test_s3_10_1v04_s3_10_1v04i():
    """
    Tests weakened wildcard (tests whether error occurs on violation of
    UPA)
    """
    assert_bindings(
        schema="ibmData/valid/S3_10_1/s3_10_1v04.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_10_1/s3_10_1v04.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_10_1v03_s3_10_1v03i():
    """
    Tests namespace attribute in wildcard
    """
    assert_bindings(
        schema="ibmData/valid/S3_10_1/s3_10_1v03.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_10_1/s3_10_1v03.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_10_1v02_s3_10_1v02i():
    """
    Tests notQName and notNamespace list
    """
    assert_bindings(
        schema="ibmData/valid/S3_10_1/s3_10_1v02.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_10_1/s3_10_1v02.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_10_1v01_s3_10_1v01i():
    """
    Tests notQName="##defined"
    """
    assert_bindings(
        schema="ibmData/valid/S3_10_1/s3_10_1v01.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_10_1/s3_10_1v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


def test_d3_4_6ii04_d3_4_6ii04i():
    r"""
    invalid instance for effect of \c in regular expressions
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D3_4_6/d3_4_6ii04.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D3_4_6/d3_4_6ii04.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_d3_4_6ii03_d3_4_6ii03i():
    r"""
    invalid instance for effect of \i in regular expressions
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D3_4_6/d3_4_6ii03.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D3_4_6/d3_4_6ii03.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_d3_4_6ii02_d3_4_6ii02i():
    """
    invalid instance for value space of xs:NCName
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D3_4_6/d3_4_6ii02.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D3_4_6/d3_4_6ii02.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_d3_4_6ii01_d3_4_6ii01i():
    """
    invalid instance for value space of xs:Name
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D3_4_6/d3_4_6ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D3_4_6/d3_4_6ii01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.schema11
def test_d3_4_6v07_d3_4_6v07i():
    """
    Use of newly allowed name characters in names of schema components
    "all"
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_6/d3_4_6v07.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_6/d3_4_6v07.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_6v06_d3_4_6v06i():
    """
    Use of newly allowed name characters in names of schema components
    "choice"
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_6/d3_4_6v06.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_6/d3_4_6v06.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_6v05_d3_4_6v05i():
    """
    Use of newly allowed name characters in names of schema components
    "sequence"
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_6/d3_4_6v05.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_6/d3_4_6v05.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_6v04_d3_4_6v04i():
    r"""
    effect of \i in regular expressions
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_6/d3_4_6v04.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_6/d3_4_6v04.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_6v03_d3_4_6v03i():
    r"""
    effect of \i in regular expressions
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_6/d3_4_6v03.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_6/d3_4_6v03.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_6v02_d3_4_6v02i():
    """
    value space of xs:Name and related types (test NCName)
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_6/d3_4_6v02.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_6/d3_4_6v02.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_6v01_d3_4_6v01i():
    """
    value space of xs:Name and related types (test Name)
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_6/d3_4_6v01.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_6/d3_4_6v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_11_2ii07_s3_11_2ii07i():
    """
    invalid instance key/keyref selection expressions_2
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_11_2/s3_11_2ii07.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_11_2/s3_11_2ii07.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_11_2ii06_s3_11_2ii06i():
    """
    invalid instance key/keyref selection expressions_1
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_11_2/s3_11_2ii06.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_11_2/s3_11_2ii06.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_11_2ii05_s3_11_2ii05i():
    """
    invalid instance key selection expressions_2
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_11_2/s3_11_2ii05.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_11_2/s3_11_2ii05.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_11_2ii04_s3_11_2ii04i():
    """
    invalid instance key selection expressions_1
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_11_2/s3_11_2ii04.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_11_2/s3_11_2ii04.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_11_2ii03_s3_11_2ii03i():
    """
    invalid instance unique selection expressions_3
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_11_2/s3_11_2ii03.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_11_2/s3_11_2ii03.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_11_2ii02_s3_11_2ii02i():
    """
    invalid instance unique selection expressions_2
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_11_2/s3_11_2ii02.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_11_2/s3_11_2ii02.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_11_2ii01_s3_11_2ii01i():
    """
    invalid instance unique selection expressions_1
    """
    assert_bindings(
        schema="ibmData/instance_invalid/S3_11_2/s3_11_2ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/S3_11_2/s3_11_2ii01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_11_2v06_s3_11_2v06i():
    """
    key/keyref selection expressions_2
    """
    assert_bindings(
        schema="ibmData/valid/S3_11_2/s3_11_2v06.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_11_2/s3_11_2v06.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_11_2v05_s3_11_2v05i():
    """
    key/keyref selection expressions_1
    """
    assert_bindings(
        schema="ibmData/valid/S3_11_2/s3_11_2v05.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_11_2/s3_11_2v05.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_11_2v04_s3_11_2v04i():
    """
    key selection expressions_2
    """
    assert_bindings(
        schema="ibmData/valid/S3_11_2/s3_11_2v04.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_11_2/s3_11_2v04.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_11_2v03_s3_11_2v03i():
    """
    key selection expressions_1
    """
    assert_bindings(
        schema="ibmData/valid/S3_11_2/s3_11_2v03.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_11_2/s3_11_2v03.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_11_2v02_s3_11_2v02i():
    """
    unique selection expressions 2
    """
    assert_bindings(
        schema="ibmData/valid/S3_11_2/s3_11_2v02.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_11_2/s3_11_2v02.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_s3_11_2v01_s3_11_2v01i():
    """
    unique selection expressions
    """
    assert_bindings(
        schema="ibmData/valid/S3_11_2/s3_11_2v01.xsd",
        is_valid=True,
        instance="ibmData/valid/S3_11_2/s3_11_2v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_26ii07_d3_4_26ii07i():
    """
    Tests the simpleType yearMonthDuration and its facets with (min|max)
    (Inclusive|Exclusive) constraint checks in derivations of simpleTypes
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D3_4_26/d3_4_26ii07.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D3_4_26/d3_4_26ii07.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_26ii06_d3_4_26ii06i():
    """
    Tests yearMonthDuration used in unions
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D3_4_26/d3_4_26ii06.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D3_4_26/d3_4_26ii06.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_26ii05_d3_4_26ii05i():
    """
    Invalid values of yearMonthDuration and invalid instance of its facets
    used in attributes
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D3_4_26/d3_4_26ii05.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D3_4_26/d3_4_26ii05.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_26ii04_d3_4_26ii04i():
    """
    Invalid yearMonthDuration Min/Max Exclusive
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D3_4_26/d3_4_26ii04.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D3_4_26/d3_4_26ii04.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_26ii03_d3_4_26ii03i():
    """
    Invalid yearMonthDuration Min/Max Inclusive
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D3_4_26/d3_4_26ii03.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D3_4_26/d3_4_26ii03.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_26ii02_d3_4_26ii02i():
    """
    Invalid yearMonthDuration enumeration values
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D3_4_26/d3_4_26ii02.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D3_4_26/d3_4_26ii02.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_26ii01_d3_4_26ii01i():
    """
    Invalid yearMonthDuration values
    """
    assert_bindings(
        schema="ibmData/instance_invalid/D3_4_26/d3_4_26ii01.xsd",
        is_valid=True,
        instance="ibmData/instance_invalid/D3_4_26/d3_4_26ii01.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_26v06_d3_4_26v06i():
    """
    Pattern is a valid facet for yearMonthDuration
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_26/d3_4_26v06.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_26/d3_4_26v06.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_26v05_d3_4_26v05i():
    """
    Additional tests for yearMonth Duration and its facets with (min|max)
    (Inclusive|Exclusive) constraint checks in derivations of simpleTypes
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_26/d3_4_26v05.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_26/d3_4_26v05.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_26v04_d3_4_26v04i():
    """
    Tests the simpleType yearMonthDuration and its facets with (min|max)
    (Inclusive|Exclusive) constraint checks in derivations of simpleTypes
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_26/d3_4_26v04.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_26/d3_4_26v04.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_26v03_d3_4_26v03i():
    """
    Tests yearMonthDuration used in unions
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_26/d3_4_26v03.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_26/d3_4_26v03.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_26v02_d3_4_26v02i():
    """
    Tests the simpleType decimal and its facets and its use in attributes
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_26/d3_4_26v02.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_26/d3_4_26v02.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


@pytest.mark.schema11
def test_d3_4_26v01_d3_4_26v01i():
    """
    Tests the simpleType yearMonthDuration and its facets and its use in
    elements
    """
    assert_bindings(
        schema="ibmData/valid/D3_4_26/d3_4_26v01.xsd",
        is_valid=True,
        instance="ibmData/valid/D3_4_26/d3_4_26v01.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )
