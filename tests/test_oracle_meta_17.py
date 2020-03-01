from tests.utils import assert_bindings


def test_zone405_zone405_v1_xml():
    """
    Test new timezone facet explicitTimezone, value="optional" for
    datatype xs:dateTime Test new timezone facet explicitTimezone,
    value="optional" for datatype xs:dateTime
    """
    assert_bindings(
        schema="oracleData/Zone/zone405.xsd",
        is_valid=True,
        instance="oracleData/Zone/zone405.v1.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.1",
    )


def test_zone405_zone405_v2_xml():
    """
    Test new timezone facet explicitTimezone, value="optional" for
    datatype xs:dateTime Test new timezone facet explicitTimezone,
    value="optional" for datatype xs:dateTime
    """
    assert_bindings(
        schema="oracleData/Zone/zone405.xsd",
        is_valid=True,
        instance="oracleData/Zone/zone405.v2.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.1",
    )


def test_zone405_zone405_v3_xml():
    """
    Test new timezone facet explicitTimezone, value="optional" for
    datatype xs:dateTime Test new timezone facet explicitTimezone,
    value="optional" for datatype xs:dateTime
    """
    assert_bindings(
        schema="oracleData/Zone/zone405.xsd",
        is_valid=True,
        instance="oracleData/Zone/zone405.v3.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.1",
    )


def test_zone404_zone404_v1_xml():
    """
    Test new timezone facet explicitTimezone, value="prohibited" for
    datatype xs:dateTime Test new timezone facet explicitTimezone,
    value="prohibited" for datatype xs:dateTime
    """
    assert_bindings(
        schema="oracleData/Zone/zone404.xsd",
        is_valid=True,
        instance="oracleData/Zone/zone404.v1.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.1",
    )


def test_zone404_zone404_n1_xml():
    """
    Test new timezone facet explicitTimezone, value="prohibited" for
    datatype xs:dateTime Test new timezone facet explicitTimezone,
    value="prohibited" for datatype xs:dateTime
    """
    assert_bindings(
        schema="oracleData/Zone/zone404.xsd",
        is_valid=True,
        instance="oracleData/Zone/zone404.n1.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.1",
    )


def test_zone404_zone404_n2_xml():
    """
    Test new timezone facet explicitTimezone, value="prohibited" for
    datatype xs:dateTime Test new timezone facet explicitTimezone,
    value="prohibited" for datatype xs:dateTime
    """
    assert_bindings(
        schema="oracleData/Zone/zone404.xsd",
        is_valid=True,
        instance="oracleData/Zone/zone404.n2.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.1",
    )


def test_zone403_zone403_v1_xml():
    """
    Test new timezone facet explicitTimezone, value="required" for
    datatype xs:dateTime Test new timezone facet explicitTimezone,
    value="required" for datatype xs:dateTime
    """
    assert_bindings(
        schema="oracleData/Zone/zone403.xsd",
        is_valid=True,
        instance="oracleData/Zone/zone403.v1.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.1",
    )


def test_zone403_zone403_v2_xml():
    """
    Test new timezone facet explicitTimezone, value="required" for
    datatype xs:dateTime Test new timezone facet explicitTimezone,
    value="required" for datatype xs:dateTime
    """
    assert_bindings(
        schema="oracleData/Zone/zone403.xsd",
        is_valid=True,
        instance="oracleData/Zone/zone403.v2.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.1",
    )


def test_zone403_zone403_n1_xml():
    """
    Test new timezone facet explicitTimezone, value="required" for
    datatype xs:dateTime Test new timezone facet explicitTimezone,
    value="required" for datatype xs:dateTime
    """
    assert_bindings(
        schema="oracleData/Zone/zone403.xsd",
        is_valid=True,
        instance="oracleData/Zone/zone403.n1.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.1",
    )


def test_zone402_zone402_n1_xml():
    """
    Test year zero allowed for facet maxInclusive for datatype xs:dateTime
    Test year zero allowed for facet maxInclusive for datatype xs:dateTime
    """
    assert_bindings(
        schema="oracleData/Zone/zone402.xsd",
        is_valid=True,
        instance="oracleData/Zone/zone402.n1.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.1",
    )


def test_zone402_zone402_n2_xml():
    """
    Test year zero allowed for facet maxInclusive for datatype xs:dateTime
    Test year zero allowed for facet maxInclusive for datatype xs:dateTime
    """
    assert_bindings(
        schema="oracleData/Zone/zone402.xsd",
        is_valid=True,
        instance="oracleData/Zone/zone402.n2.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.1",
    )


def test_zone402_zone402_v1_xml():
    """
    Test year zero allowed for facet maxInclusive for datatype xs:dateTime
    Test year zero allowed for facet maxInclusive for datatype xs:dateTime
    """
    assert_bindings(
        schema="oracleData/Zone/zone402.xsd",
        is_valid=True,
        instance="oracleData/Zone/zone402.v1.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.1",
    )


def test_zone401_zone401_v1_xml():
    """
    Equality testing (enumeration) for dateTime values, use YEAR as ZERO
    Use Year as Zero
    """
    assert_bindings(
        schema="oracleData/Zone/zone401.xsd",
        is_valid=True,
        instance="oracleData/Zone/zone401.v1.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.1",
    )


def test_zone401_zone401_v2_xml():
    """
    Equality testing (enumeration) for dateTime values, use YEAR as ZERO
    Use Year as Zero
    """
    assert_bindings(
        schema="oracleData/Zone/zone401.xsd",
        is_valid=True,
        instance="oracleData/Zone/zone401.v2.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.1",
    )


def test_zone401_zone401_v3_xml():
    """
    Equality testing (enumeration) for dateTime values, use YEAR as ZERO
    Use Year as Zero
    """
    assert_bindings(
        schema="oracleData/Zone/zone401.xsd",
        is_valid=True,
        instance="oracleData/Zone/zone401.v3.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.1",
    )


def test_zone401_zone401_n1_xml():
    """
    Equality testing (enumeration) for dateTime values, use YEAR as ZERO
    Use Year as Zero
    """
    assert_bindings(
        schema="oracleData/Zone/zone401.xsd",
        is_valid=True,
        instance="oracleData/Zone/zone401.n1.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.1",
    )


def test_zone401_zone401_n2_xml():
    """
    Equality testing (enumeration) for dateTime values, use YEAR as ZERO
    Use Year as Zero
    """
    assert_bindings(
        schema="oracleData/Zone/zone401.xsd",
        is_valid=True,
        instance="oracleData/Zone/zone401.n2.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.1",
    )
