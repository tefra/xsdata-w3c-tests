import pytest

from tests.utils import assert_bindings


def test_string005_1855_string005_1855_v():
    """
    TEST :Facet Schemas for string : value=#x20 | #xD | #xA | [a-zA-Z0-9]
    | [-'()+,./:=?;!*#@$_%]
    """
    assert_bindings(
        schema="msData/datatypes/string.xsd",
        is_valid=True,
        instance="msData/datatypes/string005.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_string004_1854_string004_1854_v():
    """
    TEST :Facet Schemas for string : value=sdflhksdgh;let vm'peoaivm'weiv'
    """
    assert_bindings(
        schema="msData/datatypes/string.xsd",
        is_valid=True,
        instance="msData/datatypes/string004.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_string003_1853_string003_1853_v():
    """
    TEST :Facet Schemas for string : value=!$%%*))*(
    """
    assert_bindings(
        schema="msData/datatypes/string.xsd",
        is_valid=True,
        instance="msData/datatypes/string003.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_string002_1852_string002_1852_v():
    """
    TEST :Facet Schemas for string : value=a_?>
    """
    assert_bindings(
        schema="msData/datatypes/string.xsd",
        is_valid=True,
        instance="msData/datatypes/string002.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_string001_1851_string001_1851_v():
    """
    TEST :Facet Schemas for string : value=
    """
    assert_bindings(
        schema="msData/datatypes/string.xsd",
        is_valid=True,
        instance="msData/datatypes/string001.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_positive_integer_total_digits003_1849_positive_integer_total_digits003_1849_v():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=4 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_totalDigits003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_totalDigits003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_positive_integer_total_digits002_1848_positive_integer_total_digits002_1848_v():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=3 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_totalDigits002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_totalDigits002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_positive_integer_total_digits001_1847_positive_integer_total_digits001_1847_i():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=2 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_totalDigits001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_totalDigits001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_positive_integer_min_exclusive005_1846_positive_integer_min_exclusive005_1846_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_minExclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_minExclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_positive_integer_min_exclusive004_1845_positive_integer_min_exclusive004_1845_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_minExclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_minExclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_positive_integer_min_exclusive003_1844_positive_integer_min_exclusive003_1844_v():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_minExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_minExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_positive_integer_min_exclusive002_1843_positive_integer_min_exclusive002_1843_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=5 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_minExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_minExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_positive_integer_min_exclusive001_1842_positive_integer_min_exclusive001_1842_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_minExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_minExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_positive_integer_min_inclusive005_1841_positive_integer_min_inclusive005_1841_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_minInclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_minInclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_positive_integer_min_inclusive004_1840_positive_integer_min_inclusive004_1840_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_minInclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_minInclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_positive_integer_min_inclusive003_1839_positive_integer_min_inclusive003_1839_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_minInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_minInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_positive_integer_min_inclusive002_1838_positive_integer_min_inclusive002_1838_i():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=5 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_minInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_minInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_positive_integer_min_inclusive001_1837_positive_integer_min_inclusive001_1837_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_minInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_minInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_positive_integer_max_exclusive003_1836_positive_integer_max_exclusive003_1836_v():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_maxExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_maxExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_positive_integer_max_inclusive003_1833_positive_integer_max_inclusive003_1833_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_maxInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_maxInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_positive_integer_max_inclusive002_1832_positive_integer_max_inclusive002_1832_i():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_maxInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_maxInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_positive_integer_max_inclusive001_1831_positive_integer_max_inclusive001_1831_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_maxInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_maxInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_positive_integer_enumeration004_1830_positive_integer_enumeration004_1830_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=567 1 234
    and document value=567
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_positive_integer_enumeration003_1829_positive_integer_enumeration003_1829_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=567 1 234
    and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_positive_integer_enumeration002_1828_positive_integer_enumeration002_1828_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=567 and
    document value=567
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_positive_integer_enumeration001_1827_positive_integer_enumeration001_1827_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=567 and
    document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_positive_integer_pattern001_1826_positive_integer_pattern001_1826_v():
    r"""
    TEST :Facet Schemas for string : facet=pattern and value=\p{Nd}{1,3}
    and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/positiveInteger/positiveInteger_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/positiveInteger/positiveInteger_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_byte_total_digits003_1825_unsigned_byte_total_digits003_1825_v():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=4 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_totalDigits003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_totalDigits003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_byte_total_digits002_1824_unsigned_byte_total_digits002_1824_v():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=3 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_totalDigits002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_totalDigits002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_byte_total_digits001_1823_unsigned_byte_total_digits001_1823_i():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=2 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_totalDigits001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_totalDigits001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_byte_min_exclusive005_1822_unsigned_byte_min_exclusive005_1822_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_minExclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_minExclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_byte_min_exclusive004_1821_unsigned_byte_min_exclusive004_1821_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_minExclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_minExclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_byte_min_exclusive003_1820_unsigned_byte_min_exclusive003_1820_v():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_minExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_minExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_byte_min_exclusive002_1819_unsigned_byte_min_exclusive002_1819_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=5 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_minExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_minExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_byte_min_exclusive001_1818_unsigned_byte_min_exclusive001_1818_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_minExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_minExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_byte_min_inclusive005_1817_unsigned_byte_min_inclusive005_1817_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_minInclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_minInclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_byte_min_inclusive004_1816_unsigned_byte_min_inclusive004_1816_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_minInclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_minInclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_byte_min_inclusive003_1815_unsigned_byte_min_inclusive003_1815_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_minInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_minInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_byte_min_inclusive002_1814_unsigned_byte_min_inclusive002_1814_i():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=5 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_minInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_minInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_byte_min_inclusive001_1813_unsigned_byte_min_inclusive001_1813_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_minInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_minInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_byte_max_exclusive003_1812_unsigned_byte_max_exclusive003_1812_v():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_maxExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_maxExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_byte_max_exclusive002_1811_unsigned_byte_max_exclusive002_1811_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_maxExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_maxExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_byte_max_exclusive001_1810_unsigned_byte_max_exclusive001_1810_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_maxExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_maxExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_byte_max_inclusive003_1809_unsigned_byte_max_inclusive003_1809_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_maxInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_maxInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_byte_max_inclusive002_1808_unsigned_byte_max_inclusive002_1808_i():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_maxInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_maxInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_byte_max_inclusive001_1807_unsigned_byte_max_inclusive001_1807_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_maxInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_maxInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_byte_enumeration004_1806_unsigned_byte_enumeration004_1806_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 1 234
    and document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_byte_enumeration003_1805_unsigned_byte_enumeration003_1805_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 1 234
    and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_byte_enumeration002_1804_unsigned_byte_enumeration002_1804_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 and
    document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_byte_enumeration001_1803_unsigned_byte_enumeration001_1803_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 and
    document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_byte_pattern001_1802_unsigned_byte_pattern001_1802_v():
    r"""
    TEST :Facet Schemas for string : facet=pattern and value=\p{Nd}{1,3}
    and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedByte/unsignedByte_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedByte/unsignedByte_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_short_total_digits003_1801_unsigned_short_total_digits003_1801_v():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=4 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_totalDigits003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_totalDigits003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_short_total_digits002_1800_unsigned_short_total_digits002_1800_v():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=3 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_totalDigits002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_totalDigits002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_short_total_digits001_1799_unsigned_short_total_digits001_1799_i():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=2 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_totalDigits001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_totalDigits001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_short_min_exclusive005_1798_unsigned_short_min_exclusive005_1798_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_minExclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_minExclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_short_min_exclusive004_1797_unsigned_short_min_exclusive004_1797_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_minExclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_minExclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_short_min_exclusive003_1796_unsigned_short_min_exclusive003_1796_v():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_minExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_minExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_short_min_exclusive002_1795_unsigned_short_min_exclusive002_1795_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=5 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_minExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_minExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_short_min_exclusive001_1794_unsigned_short_min_exclusive001_1794_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_minExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_minExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_short_min_inclusive005_1793_unsigned_short_min_inclusive005_1793_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_minInclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_minInclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_short_min_inclusive004_1792_unsigned_short_min_inclusive004_1792_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_minInclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_minInclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_short_min_inclusive003_1791_unsigned_short_min_inclusive003_1791_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_minInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_minInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_short_min_inclusive002_1790_unsigned_short_min_inclusive002_1790_i():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=5 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_minInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_minInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_short_min_inclusive001_1789_unsigned_short_min_inclusive001_1789_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_minInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_minInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_short_max_exclusive003_1788_unsigned_short_max_exclusive003_1788_v():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_maxExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_maxExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_short_max_exclusive002_1787_unsigned_short_max_exclusive002_1787_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_maxExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_maxExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_short_max_exclusive001_1786_unsigned_short_max_exclusive001_1786_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_maxExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_maxExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_short_max_inclusive003_1785_unsigned_short_max_inclusive003_1785_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_maxInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_maxInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_short_max_inclusive002_1784_unsigned_short_max_inclusive002_1784_i():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_maxInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_maxInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_short_max_inclusive001_1783_unsigned_short_max_inclusive001_1783_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_maxInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_maxInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_short_enumeration004_1782_unsigned_short_enumeration004_1782_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 1 234
    and document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_short_enumeration003_1781_unsigned_short_enumeration003_1781_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 1 234
    and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_short_enumeration002_1780_unsigned_short_enumeration002_1780_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 and
    document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_short_enumeration001_1779_unsigned_short_enumeration001_1779_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 and
    document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_short_pattern001_1778_unsigned_short_pattern001_1778_v():
    r"""
    TEST :Facet Schemas for string : facet=pattern and value=\p{Nd}{1,3}
    and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedShort/unsignedShort_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedShort/unsignedShort_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_int_total_digits003_1777_unsigned_int_total_digits003_1777_v():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=4 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_totalDigits003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_totalDigits003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_int_total_digits002_1776_unsigned_int_total_digits002_1776_v():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=3 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_totalDigits002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_totalDigits002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_int_total_digits001_1775_unsigned_int_total_digits001_1775_i():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=2 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_totalDigits001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_totalDigits001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_int_min_exclusive005_1774_unsigned_int_min_exclusive005_1774_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_minExclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_minExclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_int_min_exclusive004_1773_unsigned_int_min_exclusive004_1773_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_minExclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_minExclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_int_min_exclusive003_1772_unsigned_int_min_exclusive003_1772_v():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_minExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_minExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_int_min_exclusive002_1771_unsigned_int_min_exclusive002_1771_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=5 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_minExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_minExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_int_min_exclusive001_1770_unsigned_int_min_exclusive001_1770_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_minExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_minExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_int_min_inclusive005_1769_unsigned_int_min_inclusive005_1769_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_minInclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_minInclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_int_min_inclusive004_1768_unsigned_int_min_inclusive004_1768_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_minInclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_minInclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_int_min_inclusive003_1767_unsigned_int_min_inclusive003_1767_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_minInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_minInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_int_min_inclusive002_1766_unsigned_int_min_inclusive002_1766_i():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=5 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_minInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_minInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_int_min_inclusive001_1765_unsigned_int_min_inclusive001_1765_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_minInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_minInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_int_max_exclusive003_1764_unsigned_int_max_exclusive003_1764_v():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_maxExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_maxExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_int_max_exclusive002_1763_unsigned_int_max_exclusive002_1763_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_maxExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_maxExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_int_max_exclusive001_1762_unsigned_int_max_exclusive001_1762_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_maxExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_maxExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_int_max_inclusive003_1761_unsigned_int_max_inclusive003_1761_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_maxInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_maxInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_int_max_inclusive002_1760_unsigned_int_max_inclusive002_1760_i():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_maxInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_maxInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_int_max_inclusive001_1759_unsigned_int_max_inclusive001_1759_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_maxInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_maxInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_int_enumeration004_1758_unsigned_int_enumeration004_1758_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 1 234
    and document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_int_enumeration003_1757_unsigned_int_enumeration003_1757_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 1 234
    and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_int_enumeration002_1756_unsigned_int_enumeration002_1756_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 and
    document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_int_enumeration001_1755_unsigned_int_enumeration001_1755_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 and
    document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_int_pattern001_1754_unsigned_int_pattern001_1754_v():
    r"""
    TEST :Facet Schemas for string : facet=pattern and value=\p{Nd}{1,3}
    and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedInt/unsignedInt_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedInt/unsignedInt_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_long_total_digits003_1753_unsigned_long_total_digits003_1753_v():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=4 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_totalDigits003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_totalDigits003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_long_total_digits002_1752_unsigned_long_total_digits002_1752_v():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=3 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_totalDigits002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_totalDigits002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_long_total_digits001_1751_unsigned_long_total_digits001_1751_i():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=2 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_totalDigits001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_totalDigits001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_long_min_exclusive005_1750_unsigned_long_min_exclusive005_1750_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_minExclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_minExclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_long_min_exclusive004_1749_unsigned_long_min_exclusive004_1749_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_minExclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_minExclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_long_min_exclusive003_1748_unsigned_long_min_exclusive003_1748_v():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_minExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_minExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_long_min_exclusive002_1747_unsigned_long_min_exclusive002_1747_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=5 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_minExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_minExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_long_min_exclusive001_1746_unsigned_long_min_exclusive001_1746_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_minExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_minExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_long_min_inclusive005_1745_unsigned_long_min_inclusive005_1745_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_minInclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_minInclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_long_min_inclusive004_1744_unsigned_long_min_inclusive004_1744_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_minInclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_minInclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_long_min_inclusive003_1743_unsigned_long_min_inclusive003_1743_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_minInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_minInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_long_min_inclusive002_1742_unsigned_long_min_inclusive002_1742_i():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=5 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_minInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_minInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_long_min_inclusive001_1741_unsigned_long_min_inclusive001_1741_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_minInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_minInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_long_max_exclusive003_1740_unsigned_long_max_exclusive003_1740_v():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_maxExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_maxExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_long_max_exclusive002_1739_unsigned_long_max_exclusive002_1739_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_maxExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_maxExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_long_max_exclusive001_1738_unsigned_long_max_exclusive001_1738_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_maxExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_maxExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_long_max_inclusive003_1737_unsigned_long_max_inclusive003_1737_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_maxInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_maxInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_long_max_inclusive002_1736_unsigned_long_max_inclusive002_1736_i():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_maxInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_maxInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_long_max_inclusive001_1735_unsigned_long_max_inclusive001_1735_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_maxInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_maxInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_long_enumeration004_1734_unsigned_long_enumeration004_1734_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 1 234
    and document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_long_enumeration003_1733_unsigned_long_enumeration003_1733_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 1 234
    and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_long_enumeration002_1732_unsigned_long_enumeration002_1732_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 and
    document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_long_enumeration001_1731_unsigned_long_enumeration001_1731_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 and
    document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_unsigned_long_pattern001_1730_unsigned_long_pattern001_1730_v():
    r"""
    TEST :Facet Schemas for string : facet=pattern and value=\p{Nd}{1,3}
    and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/unsignedLong/unsignedLong_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/unsignedLong/unsignedLong_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_non_negative_integer_total_digits003_1729_non_negative_integer_total_digits003_1729_v():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=4 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_totalDigits003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_totalDigits003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_non_negative_integer_total_digits002_1728_non_negative_integer_total_digits002_1728_v():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=3 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_totalDigits002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_totalDigits002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_non_negative_integer_total_digits001_1727_non_negative_integer_total_digits001_1727_i():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=2 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_totalDigits001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_totalDigits001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_non_negative_integer_min_exclusive005_1726_non_negative_integer_min_exclusive005_1726_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minExclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minExclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_non_negative_integer_min_exclusive004_1725_non_negative_integer_min_exclusive004_1725_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minExclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minExclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_non_negative_integer_min_exclusive003_1724_non_negative_integer_min_exclusive003_1724_v():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_non_negative_integer_min_exclusive002_1723_non_negative_integer_min_exclusive002_1723_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=5 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_non_negative_integer_min_exclusive001_1722_non_negative_integer_min_exclusive001_1722_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_non_negative_integer_min_inclusive005_1721_non_negative_integer_min_inclusive005_1721_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minInclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minInclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_non_negative_integer_min_inclusive004_1720_non_negative_integer_min_inclusive004_1720_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minInclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minInclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_non_negative_integer_min_inclusive003_1719_non_negative_integer_min_inclusive003_1719_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_non_negative_integer_min_inclusive002_1718_non_negative_integer_min_inclusive002_1718_i():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=5 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_non_negative_integer_min_inclusive001_1717_non_negative_integer_min_inclusive001_1717_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_minInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_non_negative_integer_max_exclusive003_1716_non_negative_integer_max_exclusive003_1716_v():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_maxExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_maxExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_non_negative_integer_max_exclusive002_1715_non_negative_integer_max_exclusive002_1715_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_maxExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_maxExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_non_negative_integer_max_exclusive001_1714_non_negative_integer_max_exclusive001_1714_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_maxExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_maxExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_non_negative_integer_max_inclusive003_1713_non_negative_integer_max_inclusive003_1713_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_maxInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_maxInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_non_negative_integer_max_inclusive002_1712_non_negative_integer_max_inclusive002_1712_i():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_maxInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_maxInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_non_negative_integer_max_inclusive001_1711_non_negative_integer_max_inclusive001_1711_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_maxInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_maxInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_non_negative_integer_enumeration004_1710_non_negative_integer_enumeration004_1710_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=456 789 0
    and document value=456
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_non_negative_integer_enumeration003_1709_non_negative_integer_enumeration003_1709_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=456 789 0
    and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_non_negative_integer_enumeration002_1708_non_negative_integer_enumeration002_1708_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=456 and
    document value=456
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_non_negative_integer_enumeration001_1707_non_negative_integer_enumeration001_1707_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=456 and
    document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_non_negative_integer_pattern001_1706_non_negative_integer_pattern001_1706_v():
    r"""
    TEST :Facet Schemas for string : facet=pattern and value=\p{Nd}{1,3}
    and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonNegativeInteger/nonNegativeInteger_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_byte_total_digits003_1705_byte_total_digits003_1705_v():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=4 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_totalDigits003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/byte/byte_totalDigits003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_byte_total_digits002_1704_byte_total_digits002_1704_v():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=3 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_totalDigits002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/byte/byte_totalDigits002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_byte_total_digits001_1703_byte_total_digits001_1703_i():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=2 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_totalDigits001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/byte/byte_totalDigits001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_byte_min_exclusive005_1702_byte_min_exclusive005_1702_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_minExclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/byte/byte_minExclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_byte_min_exclusive004_1701_byte_min_exclusive004_1701_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_minExclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/byte/byte_minExclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_byte_min_exclusive003_1700_byte_min_exclusive003_1700_v():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_minExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/byte/byte_minExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_byte_min_exclusive002_1699_byte_min_exclusive002_1699_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=5 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_minExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/byte/byte_minExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_byte_min_exclusive001_1698_byte_min_exclusive001_1698_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_minExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/byte/byte_minExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_byte_min_inclusive005_1697_byte_min_inclusive005_1697_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_minInclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/byte/byte_minInclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_byte_min_inclusive004_1696_byte_min_inclusive004_1696_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_minInclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/byte/byte_minInclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_byte_min_inclusive003_1695_byte_min_inclusive003_1695_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_minInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/byte/byte_minInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_byte_min_inclusive002_1694_byte_min_inclusive002_1694_i():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=5 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_minInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/byte/byte_minInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_byte_min_inclusive001_1693_byte_min_inclusive001_1693_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_minInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/byte/byte_minInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_byte_max_exclusive003_1692_byte_max_exclusive003_1692_v():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_maxExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/byte/byte_maxExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_byte_max_exclusive002_1691_byte_max_exclusive002_1691_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_maxExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/byte/byte_maxExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_byte_max_exclusive001_1690_byte_max_exclusive001_1690_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_maxExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/byte/byte_maxExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_byte_max_inclusive003_1689_byte_max_inclusive003_1689_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_maxInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/byte/byte_maxInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_byte_max_inclusive002_1688_byte_max_inclusive002_1688_i():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_maxInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/byte/byte_maxInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_byte_max_inclusive001_1687_byte_max_inclusive001_1687_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_maxInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/byte/byte_maxInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_byte_enumeration004_1686_byte_enumeration004_1686_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=-1 0 1
    and document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/byte/byte_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_byte_enumeration003_1685_byte_enumeration003_1685_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=-1 0 1
    and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/byte/byte_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_byte_enumeration002_1684_byte_enumeration002_1684_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 and
    document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/byte/byte_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_byte_enumeration001_1683_byte_enumeration001_1683_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 and
    document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/byte/byte_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_byte_pattern001_1682_byte_pattern001_1682_v():
    r"""
    TEST :Facet Schemas for string : facet=pattern and value=\p{Nd}{1,3}
    and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/byte/byte_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/byte/byte_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_short_total_digits003_1681_short_total_digits003_1681_v():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=4 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_totalDigits003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/short/short_totalDigits003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_short_total_digits002_1680_short_total_digits002_1680_v():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=3 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_totalDigits002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/short/short_totalDigits002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_short_total_digits001_1679_short_total_digits001_1679_i():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=2 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_totalDigits001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/short/short_totalDigits001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_short_min_exclusive005_1678_short_min_exclusive005_1678_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_minExclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/short/short_minExclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_short_min_exclusive004_1677_short_min_exclusive004_1677_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_minExclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/short/short_minExclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_short_min_exclusive003_1676_short_min_exclusive003_1676_v():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_minExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/short/short_minExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_short_min_exclusive002_1675_short_min_exclusive002_1675_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=5 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_minExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/short/short_minExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_short_min_exclusive001_1674_short_min_exclusive001_1674_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_minExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/short/short_minExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_short_min_inclusive005_1673_short_min_inclusive005_1673_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_minInclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/short/short_minInclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_short_min_inclusive004_1672_short_min_inclusive004_1672_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_minInclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/short/short_minInclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_short_min_inclusive003_1671_short_min_inclusive003_1671_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_minInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/short/short_minInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_short_min_inclusive002_1670_short_min_inclusive002_1670_i():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=5 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_minInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/short/short_minInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_short_min_inclusive001_1669_short_min_inclusive001_1669_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_minInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/short/short_minInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_short_max_exclusive003_1668_short_max_exclusive003_1668_v():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_maxExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/short/short_maxExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_short_max_exclusive002_1667_short_max_exclusive002_1667_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_maxExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/short/short_maxExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_short_max_exclusive001_1666_short_max_exclusive001_1666_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_maxExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/short/short_maxExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_short_max_inclusive003_1665_short_max_inclusive003_1665_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_maxInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/short/short_maxInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_short_max_inclusive002_1664_short_max_inclusive002_1664_i():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_maxInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/short/short_maxInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_short_max_inclusive001_1663_short_max_inclusive001_1663_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_maxInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/short/short_maxInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_short_enumeration004_1662_short_enumeration004_1662_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=-1 0 1
    and document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/short/short_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_short_enumeration003_1661_short_enumeration003_1661_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=-1 0 1
    and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/short/short_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_short_enumeration002_1660_short_enumeration002_1660_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 and
    document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/short/short_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_short_enumeration001_1659_short_enumeration001_1659_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 and
    document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/short/short_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_short_pattern001_1658_short_pattern001_1658_v():
    r"""
    TEST :Facet Schemas for string : facet=pattern and value=\p{Nd}{1,3}
    and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/short/short_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/short/short_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_test111092_1657_test111092_1657_i():
    """
    TEST :Facet Schemas for string : test derived maxExclusive to be equal
    to the base maxInclusive
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/test111092.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/int/test111092.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_int_total_digits003_1656_int_total_digits003_1656_v():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=4 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_totalDigits003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/int/int_totalDigits003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_int_total_digits002_1655_int_total_digits002_1655_v():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=3 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_totalDigits002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/int/int_totalDigits002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_int_total_digits001_1654_int_total_digits001_1654_i():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=2 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_totalDigits001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/int/int_totalDigits001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_int_min_exclusive005_1653_int_min_exclusive005_1653_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_minExclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/int/int_minExclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_int_min_exclusive004_1652_int_min_exclusive004_1652_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_minExclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/int/int_minExclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_int_min_exclusive003_1651_int_min_exclusive003_1651_v():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_minExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/int/int_minExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_int_min_exclusive002_1650_int_min_exclusive002_1650_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=5 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_minExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/int/int_minExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_int_min_exclusive001_1649_int_min_exclusive001_1649_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_minExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/int/int_minExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_int_min_inclusive005_1648_int_min_inclusive005_1648_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_minInclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/int/int_minInclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_int_min_inclusive004_1647_int_min_inclusive004_1647_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_minInclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/int/int_minInclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_int_min_inclusive003_1646_int_min_inclusive003_1646_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_minInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/int/int_minInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_int_min_inclusive002_1645_int_min_inclusive002_1645_i():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=5 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_minInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/int/int_minInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_int_min_inclusive001_1644_int_min_inclusive001_1644_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_minInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/int/int_minInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_int_max_exclusive003_1643_int_max_exclusive003_1643_v():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_maxExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/int/int_maxExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_int_max_exclusive002_1642_int_max_exclusive002_1642_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_maxExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/int/int_maxExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_int_max_exclusive001_1641_int_max_exclusive001_1641_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_maxExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/int/int_maxExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_int_max_inclusive003_1640_int_max_inclusive003_1640_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_maxInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/int/int_maxInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_int_max_inclusive002_1639_int_max_inclusive002_1639_i():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_maxInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/int/int_maxInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_int_max_inclusive001_1638_int_max_inclusive001_1638_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_maxInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/int/int_maxInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_int_enumeration004_1637_int_enumeration004_1637_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=-1 0 1
    and document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/int/int_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_int_enumeration003_1636_int_enumeration003_1636_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=-1 0 1
    and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/int/int_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_int_enumeration002_1635_int_enumeration002_1635_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 and
    document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/int/int_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_int_enumeration001_1634_int_enumeration001_1634_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 and
    document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/int/int_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_int_pattern001_1633_int_pattern001_1633_v():
    r"""
    TEST :Facet Schemas for string : facet=pattern and value=\p{Nd}{1,3}
    and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/int/int_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/int/int_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_long_total_digits003_1632_long_total_digits003_1632_v():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=4 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_totalDigits003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/long/long_totalDigits003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_long_total_digits002_1631_long_total_digits002_1631_v():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=3 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_totalDigits002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/long/long_totalDigits002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_long_total_digits001_1630_long_total_digits001_1630_i():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=2 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_totalDigits001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/long/long_totalDigits001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_long_min_exclusive005_1629_long_min_exclusive005_1629_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_minExclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/long/long_minExclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_long_min_exclusive004_1628_long_min_exclusive004_1628_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_minExclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/long/long_minExclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_long_min_exclusive003_1627_long_min_exclusive003_1627_v():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_minExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/long/long_minExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_long_min_exclusive002_1626_long_min_exclusive002_1626_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=5 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_minExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/long/long_minExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_long_min_exclusive001_1625_long_min_exclusive001_1625_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_minExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/long/long_minExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_long_min_inclusive005_1624_long_min_inclusive005_1624_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_minInclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/long/long_minInclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_long_min_inclusive004_1623_long_min_inclusive004_1623_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_minInclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/long/long_minInclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_long_min_inclusive003_1622_long_min_inclusive003_1622_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_minInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/long/long_minInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_long_min_inclusive002_1621_long_min_inclusive002_1621_i():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=5 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_minInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/long/long_minInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_long_min_inclusive001_1620_long_min_inclusive001_1620_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_minInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/long/long_minInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_long_max_exclusive003_1619_long_max_exclusive003_1619_v():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_maxExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/long/long_maxExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_long_max_exclusive002_1618_long_max_exclusive002_1618_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_maxExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/long/long_maxExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_long_max_exclusive001_1617_long_max_exclusive001_1617_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_maxExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/long/long_maxExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_long_max_inclusive003_1616_long_max_inclusive003_1616_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_maxInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/long/long_maxInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_long_max_inclusive002_1615_long_max_inclusive002_1615_i():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_maxInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/long/long_maxInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_long_max_inclusive001_1614_long_max_inclusive001_1614_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_maxInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/long/long_maxInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_long_enumeration004_1613_long_enumeration004_1613_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=-1 0 1
    and document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/long/long_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_long_enumeration003_1612_long_enumeration003_1612_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=-1 0 1
    and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/long/long_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_long_enumeration002_1611_long_enumeration002_1611_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 and
    document value=0
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/long/long_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_long_enumeration001_1610_long_enumeration001_1610_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=0 and
    document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/long/long_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_long_pattern001_1609_long_pattern001_1609_v():
    r"""
    TEST :Facet Schemas for string : facet=pattern and value=\p{Nd}{1,3}
    and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/long/long_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/long/long_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_negative_integer_total_digits003_1608_negative_integer_total_digits003_1608_v():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=4 and
    document value=-123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_totalDigits003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_totalDigits003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_negative_integer_total_digits002_1607_negative_integer_total_digits002_1607_v():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=3 and
    document value=-123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_totalDigits002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_totalDigits002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_negative_integer_total_digits001_1606_negative_integer_total_digits001_1606_i():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=2 and
    document value=-123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_totalDigits001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_totalDigits001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_negative_integer_min_exclusive005_1605_negative_integer_min_exclusive005_1605_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=-7 and
    facet=maxExclusive and value=-1) and document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_minExclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_minExclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_negative_integer_min_exclusive004_1604_negative_integer_min_exclusive004_1604_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=-7 and
    facet=maxInclusive and value=-1) and document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_minExclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_minExclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_negative_integer_min_exclusive003_1603_negative_integer_min_exclusive003_1603_v():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=-7 and
    document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_minExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_minExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_negative_integer_min_exclusive002_1602_negative_integer_min_exclusive002_1602_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=-5 and
    document value=-7
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_minExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_minExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_negative_integer_min_exclusive001_1601_negative_integer_min_exclusive001_1601_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=-7 and
    document value=-7
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_minExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_minExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_negative_integer_min_inclusive005_1600_negative_integer_min_inclusive005_1600_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=-7 and
    facet=maxExclusive and value=-1) and document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_minInclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_minInclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_negative_integer_min_inclusive004_1599_negative_integer_min_inclusive004_1599_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=-7 and
    facet=maxInclusive and value=-1) and document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_minInclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_minInclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_negative_integer_min_inclusive003_1598_negative_integer_min_inclusive003_1598_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=-7 and
    document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_minInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_minInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_negative_integer_min_inclusive002_1597_negative_integer_min_inclusive002_1597_i():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=-5 and
    document value=-7
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_minInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_minInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_negative_integer_min_inclusive001_1596_negative_integer_min_inclusive001_1596_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=-7 and
    document value=-7
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_minInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_minInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_negative_integer_max_exclusive003_1595_negative_integer_max_exclusive003_1595_v():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=-1 and
    document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_maxExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_maxExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_negative_integer_max_exclusive002_1594_negative_integer_max_exclusive002_1594_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=-7 and
    document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_maxExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_maxExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_negative_integer_max_exclusive001_1593_negative_integer_max_exclusive001_1593_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=-7 and
    document value=-7
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_maxExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_maxExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_negative_integer_max_inclusive003_1592_negative_integer_max_inclusive003_1592_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=-1 and
    document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_maxInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_maxInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_negative_integer_max_inclusive002_1591_negative_integer_max_inclusive002_1591_i():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=-7 and
    document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_maxInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_maxInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_negative_integer_max_inclusive001_1590_negative_integer_max_inclusive001_1590_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=-7 and
    document value=-7
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_maxInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_maxInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_negative_integer_enumeration004_1589_negative_integer_enumeration004_1589_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=-456 -789
    -1 and document value=-456
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_negative_integer_enumeration003_1588_negative_integer_enumeration003_1588_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=-456 -789
    -1 and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_negative_integer_enumeration002_1587_negative_integer_enumeration002_1587_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=-456 and
    document value=-456
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_negative_integer_enumeration001_1586_negative_integer_enumeration001_1586_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=-456 and
    document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_negative_integer_pattern001_1585_negative_integer_pattern001_1585_v():
    r"""
    TEST :Facet Schemas for string : facet=pattern and value=-\p{Nd}{1,3}
    and document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/negativeInteger/negativeInteger_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/negativeInteger/negativeInteger_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_non_positive_integer_total_digits003_1584_non_positive_integer_total_digits003_1584_v():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=4 and
    document value=-123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_totalDigits003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_totalDigits003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_non_positive_integer_total_digits002_1583_non_positive_integer_total_digits002_1583_v():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=3 and
    document value=-123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_totalDigits002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_totalDigits002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_non_positive_integer_total_digits001_1582_non_positive_integer_total_digits001_1582_i():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=2 and
    document value=-123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_totalDigits001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_totalDigits001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_non_positive_integer_min_exclusive005_1581_non_positive_integer_min_exclusive005_1581_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=-7 and
    facet=maxExclusive and value=-1) and document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minExclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minExclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_non_positive_integer_min_exclusive004_1580_non_positive_integer_min_exclusive004_1580_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=-7 and
    facet=maxInclusive and value=-1) and document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minExclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minExclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_non_positive_integer_min_exclusive003_1579_non_positive_integer_min_exclusive003_1579_v():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=-7 and
    document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_non_positive_integer_min_exclusive002_1578_non_positive_integer_min_exclusive002_1578_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=-5 and
    document value=-7
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_non_positive_integer_min_exclusive001_1577_non_positive_integer_min_exclusive001_1577_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=-7 and
    document value=-7
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_non_positive_integer_min_inclusive005_1576_non_positive_integer_min_inclusive005_1576_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=-7 and
    facet=maxExclusive and value=-1) and document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minInclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minInclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_non_positive_integer_min_inclusive004_1575_non_positive_integer_min_inclusive004_1575_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=-7 and
    facet=maxInclusive and value=-1) and document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minInclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minInclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_non_positive_integer_min_inclusive003_1574_non_positive_integer_min_inclusive003_1574_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=-7 and
    document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_non_positive_integer_min_inclusive002_1573_non_positive_integer_min_inclusive002_1573_i():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=-5 and
    document value=-7
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_non_positive_integer_min_inclusive001_1572_non_positive_integer_min_inclusive001_1572_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=-7 and
    document value=-7
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_minInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_non_positive_integer_max_exclusive003_1571_non_positive_integer_max_exclusive003_1571_v():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=-1 and
    document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_maxExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_maxExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_non_positive_integer_max_exclusive002_1570_non_positive_integer_max_exclusive002_1570_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=-7 and
    document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_maxExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_maxExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_non_positive_integer_max_exclusive001_1569_non_positive_integer_max_exclusive001_1569_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=-7 and
    document value=-7
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_maxExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_maxExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_non_positive_integer_max_inclusive003_1568_non_positive_integer_max_inclusive003_1568_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=-1 and
    document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_maxInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_maxInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_non_positive_integer_max_inclusive002_1567_non_positive_integer_max_inclusive002_1567_i():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=-7 and
    document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_maxInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_maxInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_non_positive_integer_max_inclusive001_1566_non_positive_integer_max_inclusive001_1566_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=-7 and
    document value=-7
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_maxInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_maxInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_non_positive_integer_enumeration004_1565_non_positive_integer_enumeration004_1565_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=-456 -789
    0 and document value=-456
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_non_positive_integer_enumeration003_1564_non_positive_integer_enumeration003_1564_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=-456 -789
    0 and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_non_positive_integer_enumeration002_1563_non_positive_integer_enumeration002_1563_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=-456 and
    document value=-456
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_non_positive_integer_enumeration001_1562_non_positive_integer_enumeration001_1562_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=-456 and
    document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_non_positive_integer_pattern001_1561_non_positive_integer_pattern001_1561_v():
    r"""
    TEST :Facet Schemas for string : facet=pattern and value=-\p{Nd}{1,3}
    and document value=-5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/nonPositiveInteger/nonPositiveInteger_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_integer_total_digits003_1560_integer_total_digits003_1560_v():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=4 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_totalDigits003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/integer/integer_totalDigits003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_integer_total_digits002_1559_integer_total_digits002_1559_v():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=3 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_totalDigits002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/integer/integer_totalDigits002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_integer_total_digits001_1558_integer_total_digits001_1558_i():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=2 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_totalDigits001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/integer/integer_totalDigits001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_integer_min_exclusive005_1557_integer_min_exclusive005_1557_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_minExclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/integer/integer_minExclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_integer_min_exclusive004_1556_integer_min_exclusive004_1556_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_minExclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/integer/integer_minExclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_integer_min_exclusive003_1555_integer_min_exclusive003_1555_v():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_minExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/integer/integer_minExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_integer_min_exclusive002_1554_integer_min_exclusive002_1554_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=5 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_minExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/integer/integer_minExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_integer_min_exclusive001_1553_integer_min_exclusive001_1553_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_minExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/integer/integer_minExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_integer_min_inclusive005_1552_integer_min_inclusive005_1552_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxExclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_minInclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/integer/integer_minInclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_integer_min_inclusive004_1551_integer_min_inclusive004_1551_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1 and
    facet=maxInclusive and value=7) and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_minInclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/integer/integer_minInclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_integer_min_inclusive003_1550_integer_min_inclusive003_1550_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_minInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/integer/integer_minInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_integer_min_inclusive002_1549_integer_min_inclusive002_1549_i():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=5 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_minInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/integer/integer_minInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_integer_min_inclusive001_1548_integer_min_inclusive001_1548_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_minInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/integer/integer_minInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_integer_max_exclusive003_1547_integer_max_exclusive003_1547_v():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_maxExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/integer/integer_maxExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_integer_max_exclusive002_1546_integer_max_exclusive002_1546_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_maxExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/integer/integer_maxExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_integer_max_exclusive001_1545_integer_max_exclusive001_1545_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_maxExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/integer/integer_maxExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_integer_max_inclusive003_1544_integer_max_inclusive003_1544_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=7 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_maxInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/integer/integer_maxInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_integer_max_inclusive002_1543_integer_max_inclusive002_1543_i():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_maxInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/integer/integer_maxInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_integer_max_inclusive001_1542_integer_max_inclusive001_1542_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1 and
    document value=1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_maxInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/integer/integer_maxInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_integer_enumeration004_1541_integer_enumeration004_1541_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=123 456
    789 and document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/integer/integer_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_integer_enumeration003_1540_integer_enumeration003_1540_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=123 456
    789 and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/integer/integer_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_integer_enumeration002_1539_integer_enumeration002_1539_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=123 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/integer/integer_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_integer_enumeration001_1538_integer_enumeration001_1538_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=123 and
    document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/integer/integer_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_integer_pattern001_1537_integer_pattern001_1537_v():
    r"""
    TEST :Facet Schemas for string : facet=pattern and value=\p{Nd}{1,3}
    and document value=5
    """
    assert_bindings(
        schema="msData/datatypes/Facets/integer/integer_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/integer/integer_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_idref_enumeration004_1536_idref_enumeration004_1536_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    foo123 fu1 and document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREF/IDREF_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/IDREF/IDREF_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_idref_enumeration003_1535_idref_enumeration003_1535_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    foo123 fu1 and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREF/IDREF_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/IDREF/IDREF_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_idref_enumeration002_1534_idref_enumeration002_1534_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREF/IDREF_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/IDREF/IDREF_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_idref_enumeration001_1533_idref_enumeration001_1533_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREF/IDREF_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/IDREF/IDREF_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_idref_pattern001_1532_idref_pattern001_1532_v():
    """
    TEST :Facet Schemas for string : facet=pattern and value=[a-z]{3} and
    document value=abc
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREF/IDREF_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/IDREF/IDREF_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_idref_max_length003_1531_idref_max_length003_1531_v():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=6 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREF/IDREF_maxLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/IDREF/IDREF_maxLength003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_idref_max_length002_1530_idref_max_length002_1530_v():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREF/IDREF_maxLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/IDREF/IDREF_maxLength002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_idref_max_length001_1529_idref_max_length001_1529_i():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=4 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREF/IDREF_maxLength001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/IDREF/IDREF_maxLength001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_idref_min_length004_1528_idref_min_length004_1528_v():
    """
    TEST :Facet Schemas for string : (facet=minLength and value=4 and
    facet=maxLength and value=6) and document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREF/IDREF_minLength004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/IDREF/IDREF_minLength004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_idref_min_length003_1527_idref_min_length003_1527_i():
    """
    TEST :Facet Schemas for string : facet=minLength and value=6 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREF/IDREF_minLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/IDREF/IDREF_minLength003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_idref_min_length002_1526_idref_min_length002_1526_v():
    """
    TEST :Facet Schemas for string : facet=minLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREF/IDREF_minLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/IDREF/IDREF_minLength002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_idref_min_length001_1525_idref_min_length001_1525_v():
    """
    TEST :Facet Schemas for string : facet=minLength and value=4 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREF/IDREF_minLength001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/IDREF/IDREF_minLength001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_idref_length003_1524_idref_length003_1524_i():
    """
    TEST :Facet Schemas for string : facet=length and value=6 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREF/IDREF_length003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/IDREF/IDREF_length003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_idref_length002_1523_idref_length002_1523_v():
    """
    TEST :Facet Schemas for string : facet=length and value=5 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREF/IDREF_length002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/IDREF/IDREF_length002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_idref_length001_1522_idref_length001_1522_i():
    """
    TEST :Facet Schemas for string : facet=length and value=4 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREF/IDREF_length001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/IDREF/IDREF_length001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_id_enumeration004_1521_id_enumeration004_1521_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    foo123 fu1 and document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/ID/ID_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/ID/ID_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_id_enumeration003_1520_id_enumeration003_1520_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    foo123 fu1 and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/ID/ID_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/ID/ID_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_id_enumeration002_1519_id_enumeration002_1519_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/ID/ID_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/ID/ID_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_id_enumeration001_1518_id_enumeration001_1518_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/ID/ID_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/ID/ID_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_id_pattern001_1517_id_pattern001_1517_v():
    """
    TEST :Facet Schemas for string : facet=pattern and value=[a-z]{3} and
    document value=abc
    """
    assert_bindings(
        schema="msData/datatypes/Facets/ID/ID_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/ID/ID_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_id_max_length003_1516_id_max_length003_1516_v():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=6 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/ID/ID_maxLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/ID/ID_maxLength003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_id_max_length002_1515_id_max_length002_1515_v():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/ID/ID_maxLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/ID/ID_maxLength002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_id_max_length001_1514_id_max_length001_1514_i():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=4 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/ID/ID_maxLength001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/ID/ID_maxLength001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_id_min_length004_1513_id_min_length004_1513_v():
    """
    TEST :Facet Schemas for string : (facet=minLength and value=4 and
    facet=maxLength and value=6) and document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/ID/ID_minLength004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/ID/ID_minLength004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_id_min_length003_1512_id_min_length003_1512_i():
    """
    TEST :Facet Schemas for string : facet=minLength and value=6 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/ID/ID_minLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/ID/ID_minLength003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_id_min_length002_1511_id_min_length002_1511_v():
    """
    TEST :Facet Schemas for string : facet=minLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/ID/ID_minLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/ID/ID_minLength002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_id_min_length001_1510_id_min_length001_1510_v():
    """
    TEST :Facet Schemas for string : facet=minLength and value=4 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/ID/ID_minLength001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/ID/ID_minLength001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_id_length003_1509_id_length003_1509_i():
    """
    TEST :Facet Schemas for string : facet=length and value=6 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/ID/ID_length003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/ID/ID_length003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_id_length002_1508_id_length002_1508_v():
    """
    TEST :Facet Schemas for string : facet=length and value=5 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/ID/ID_length002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/ID/ID_length002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_id_length001_1507_id_length001_1507_i():
    """
    TEST :Facet Schemas for string : facet=length and value=4 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/ID/ID_length001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/ID/ID_length001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_ncname_enumeration004_1506_ncname_enumeration004_1506_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    foo123 fu1 and document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NCName/NCName_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NCName/NCName_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_ncname_enumeration003_1505_ncname_enumeration003_1505_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    foo123 fu1 and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NCName/NCName_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NCName/NCName_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_ncname_enumeration002_1504_ncname_enumeration002_1504_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NCName/NCName_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NCName/NCName_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_ncname_enumeration001_1503_ncname_enumeration001_1503_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NCName/NCName_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NCName/NCName_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_ncname_pattern001_1502_ncname_pattern001_1502_v():
    """
    TEST :Facet Schemas for string : facet=pattern and value=[a-z]{3} and
    document value=abc
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NCName/NCName_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NCName/NCName_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_ncname_max_length003_1501_ncname_max_length003_1501_v():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=6 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NCName/NCName_maxLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NCName/NCName_maxLength003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_ncname_max_length002_1500_ncname_max_length002_1500_v():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NCName/NCName_maxLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NCName/NCName_maxLength002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_ncname_max_length001_1499_ncname_max_length001_1499_i():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=4 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NCName/NCName_maxLength001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NCName/NCName_maxLength001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_ncname_min_length004_1498_ncname_min_length004_1498_v():
    """
    TEST :Facet Schemas for string : (facet=minLength and value=4 and
    facet=maxLength and value=6) and document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NCName/NCName_minLength004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NCName/NCName_minLength004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_ncname_min_length003_1497_ncname_min_length003_1497_i():
    """
    TEST :Facet Schemas for string : facet=minLength and value=6 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NCName/NCName_minLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NCName/NCName_minLength003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_ncname_min_length002_1496_ncname_min_length002_1496_v():
    """
    TEST :Facet Schemas for string : facet=minLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NCName/NCName_minLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NCName/NCName_minLength002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_ncname_min_length001_1495_ncname_min_length001_1495_v():
    """
    TEST :Facet Schemas for string : facet=minLength and value=4 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NCName/NCName_minLength001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NCName/NCName_minLength001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_ncname_length003_1494_ncname_length003_1494_i():
    """
    TEST :Facet Schemas for string : facet=length and value=6 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NCName/NCName_length003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NCName/NCName_length003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_ncname_length002_1493_ncname_length002_1493_v():
    """
    TEST :Facet Schemas for string : facet=length and value=5 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NCName/NCName_length002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NCName/NCName_length002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_ncname_length001_1492_ncname_length001_1492_i():
    """
    TEST :Facet Schemas for string : facet=length and value=4 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NCName/NCName_length001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NCName/NCName_length001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_name_enumeration004_1491_name_enumeration004_1491_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    foo123 fu1 and document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/Name/Name_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/Name/Name_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_name_enumeration003_1490_name_enumeration003_1490_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    foo123 fu1 and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/Name/Name_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/Name/Name_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_name_enumeration002_1489_name_enumeration002_1489_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/Name/Name_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/Name/Name_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_name_enumeration001_1488_name_enumeration001_1488_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/Name/Name_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/Name/Name_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_name_pattern001_1487_name_pattern001_1487_v():
    """
    TEST :Facet Schemas for string : facet=pattern and value=[a-z]{3} and
    document value=abc
    """
    assert_bindings(
        schema="msData/datatypes/Facets/Name/Name_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/Name/Name_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_name_max_length003_1486_name_max_length003_1486_v():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=6 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/Name/Name_maxLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/Name/Name_maxLength003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_name_max_length002_1485_name_max_length002_1485_v():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/Name/Name_maxLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/Name/Name_maxLength002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_name_max_length001_1484_name_max_length001_1484_i():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=4 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/Name/Name_maxLength001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/Name/Name_maxLength001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_name_min_length004_1483_name_min_length004_1483_v():
    """
    TEST :Facet Schemas for string : (facet=minLength and value=4 and
    facet=maxLength and value=6) and document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/Name/Name_minLength004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/Name/Name_minLength004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_name_min_length003_1482_name_min_length003_1482_i():
    """
    TEST :Facet Schemas for string : facet=minLength and value=6 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/Name/Name_minLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/Name/Name_minLength003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_name_min_length002_1481_name_min_length002_1481_v():
    """
    TEST :Facet Schemas for string : facet=minLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/Name/Name_minLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/Name/Name_minLength002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_name_min_length001_1480_name_min_length001_1480_v():
    """
    TEST :Facet Schemas for string : facet=minLength and value=4 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/Name/Name_minLength001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/Name/Name_minLength001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_name_length003_1479_name_length003_1479_i():
    """
    TEST :Facet Schemas for string : facet=length and value=6 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/Name/Name_length003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/Name/Name_length003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_name_length002_1478_name_length002_1478_v():
    """
    TEST :Facet Schemas for string : facet=length and value=5 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/Name/Name_length002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/Name/Name_length002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_name_length001_1477_name_length001_1477_i():
    """
    TEST :Facet Schemas for string : facet=length and value=4 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/Name/Name_length001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/Name/Name_length001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_nmtokens_pattern002_1476_nmtokens_pattern002_1476_i():
    """
    TEST :Facet Schemas for string : XSD: NMTOKENS, IDREFS, and ENTITIES
    now allow the pattern facet
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKENS/NMTOKENS_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NMTOKENS/NMTOKENS_pattern002.xml",
        instance_is_valid=False,
        class_name="Foo",
        version="1.0",
    )


def test_nmtokens_pattern001_1475_nmtokens_pattern001_1475_v():
    """
    TEST :Facet Schemas for string : XSD: NMTOKENS, IDREFS, and ENTITIES
    now allow the pattern facet
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKENS/NMTOKENS_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NMTOKENS/NMTOKENS_pattern001.xml",
        instance_is_valid=True,
        class_name="Foo",
        version="1.0",
    )


def test_nmtokens_enumeration004_1474_nmtokens_enumeration004_1474_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    foo123 fu1 and document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKENS/NMTOKENS_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NMTOKENS/NMTOKENS_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_nmtokens_enumeration003_1473_nmtokens_enumeration003_1473_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    foo123 fu1 and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKENS/NMTOKENS_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NMTOKENS/NMTOKENS_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_nmtokens_enumeration002_1472_nmtokens_enumeration002_1472_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKENS/NMTOKENS_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NMTOKENS/NMTOKENS_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_nmtokens_enumeration001_1471_nmtokens_enumeration001_1471_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKENS/NMTOKENS_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NMTOKENS/NMTOKENS_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_nmtokens_max_length003_1470_nmtokens_max_length003_1470_v():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=6 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKENS/NMTOKENS_maxLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NMTOKENS/NMTOKENS_maxLength003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_nmtokens_max_length002_1469_nmtokens_max_length002_1469_v():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKENS/NMTOKENS_maxLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NMTOKENS/NMTOKENS_maxLength002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_nmtokens_min_length003_1466_nmtokens_min_length003_1466_i():
    """
    TEST :Facet Schemas for string : facet=minLength and value=6 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKENS/NMTOKENS_minLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NMTOKENS/NMTOKENS_minLength003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_nmtokens_min_length002_1465_nmtokens_min_length002_1465_v():
    """
    TEST :Facet Schemas for string : facet=minLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKENS/NMTOKENS_minLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NMTOKENS/NMTOKENS_minLength002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_nmtokens_length003_1463_nmtokens_length003_1463_i():
    """
    TEST :Facet Schemas for string : facet=length and value=6 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKENS/NMTOKENS_length003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NMTOKENS/NMTOKENS_length003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_nmtokens_length002_1462_nmtokens_length002_1462_v():
    """
    TEST :Facet Schemas for string : facet=length and value=5 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKENS/NMTOKENS_length002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NMTOKENS/NMTOKENS_length002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_nmtokens_length001_1461_nmtokens_length001_1461_i():
    """
    TEST :Facet Schemas for string : facet=length and value=4 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKENS/NMTOKENS_length001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NMTOKENS/NMTOKENS_length001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_nmtoken_enumeration004_1460_nmtoken_enumeration004_1460_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    foo123 fu1 and document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKEN/NMTOKEN_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NMTOKEN/NMTOKEN_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_nmtoken_enumeration003_1459_nmtoken_enumeration003_1459_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    foo123 fu1 and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKEN/NMTOKEN_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NMTOKEN/NMTOKEN_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_nmtoken_enumeration002_1458_nmtoken_enumeration002_1458_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKEN/NMTOKEN_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NMTOKEN/NMTOKEN_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_nmtoken_enumeration001_1457_nmtoken_enumeration001_1457_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKEN/NMTOKEN_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NMTOKEN/NMTOKEN_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_nmtoken_pattern001_1456_nmtoken_pattern001_1456_v():
    """
    TEST :Facet Schemas for string : facet=pattern and value=[a-z]{3} and
    document value=abc
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKEN/NMTOKEN_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NMTOKEN/NMTOKEN_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_nmtoken_max_length003_1455_nmtoken_max_length003_1455_v():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=6 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKEN/NMTOKEN_maxLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NMTOKEN/NMTOKEN_maxLength003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_nmtoken_max_length002_1454_nmtoken_max_length002_1454_v():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKEN/NMTOKEN_maxLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NMTOKEN/NMTOKEN_maxLength002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_nmtoken_max_length001_1453_nmtoken_max_length001_1453_i():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=4 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKEN/NMTOKEN_maxLength001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NMTOKEN/NMTOKEN_maxLength001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_nmtoken_min_length004_1452_nmtoken_min_length004_1452_v():
    """
    TEST :Facet Schemas for string : (facet=minLength and value=4 and
    facet=maxLength and value=6) and document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKEN/NMTOKEN_minLength004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NMTOKEN/NMTOKEN_minLength004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_nmtoken_min_length003_1451_nmtoken_min_length003_1451_i():
    """
    TEST :Facet Schemas for string : facet=minLength and value=6 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKEN/NMTOKEN_minLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NMTOKEN/NMTOKEN_minLength003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_nmtoken_min_length002_1450_nmtoken_min_length002_1450_v():
    """
    TEST :Facet Schemas for string : facet=minLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKEN/NMTOKEN_minLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NMTOKEN/NMTOKEN_minLength002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_nmtoken_min_length001_1449_nmtoken_min_length001_1449_v():
    """
    TEST :Facet Schemas for string : facet=minLength and value=4 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKEN/NMTOKEN_minLength001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NMTOKEN/NMTOKEN_minLength001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_nmtoken_length003_1448_nmtoken_length003_1448_i():
    """
    TEST :Facet Schemas for string : facet=length and value=6 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKEN/NMTOKEN_length003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NMTOKEN/NMTOKEN_length003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_nmtoken_length002_1447_nmtoken_length002_1447_v():
    """
    TEST :Facet Schemas for string : facet=length and value=5 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKEN/NMTOKEN_length002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NMTOKEN/NMTOKEN_length002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_nmtoken_length001_1446_nmtoken_length001_1446_i():
    """
    TEST :Facet Schemas for string : facet=length and value=4 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NMTOKEN/NMTOKEN_length001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NMTOKEN/NMTOKEN_length001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_idrefs_enumeration004_1445_idrefs_enumeration004_1445_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    foo123 fu1 and document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREFS/IDREFS_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/IDREFS/IDREFS_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_idrefs_enumeration003_1444_idrefs_enumeration003_1444_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    foo123 fu1 and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREFS/IDREFS_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/IDREFS/IDREFS_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_idrefs_enumeration002_1443_idrefs_enumeration002_1443_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREFS/IDREFS_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/IDREFS/IDREFS_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_idrefs_enumeration001_1442_idrefs_enumeration001_1442_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREFS/IDREFS_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/IDREFS/IDREFS_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_idrefs_max_length003_1441_idrefs_max_length003_1441_v():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=2 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREFS/IDREFS_maxLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/IDREFS/IDREFS_maxLength003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_idrefs_max_length002_1440_idrefs_max_length002_1440_v():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=1 and
    document value=more
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREFS/IDREFS_maxLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/IDREFS/IDREFS_maxLength002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_idrefs_max_length001_1439_idrefs_max_length001_1439_i():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=2 and
    document value="foofo more"
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREFS/IDREFS_maxLength001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/IDREFS/IDREFS_maxLength001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_idrefs_min_length004_1438_idrefs_min_length004_1438_v():
    """
    TEST :Facet Schemas for string : (facet=minLength and value=4 and
    facet=maxLength and value=6) and document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREFS/IDREFS_minLength004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/IDREFS/IDREFS_minLength004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_idrefs_min_length003_1437_idrefs_min_length003_1437_i():
    """
    TEST :Facet Schemas for string : facet=minLength and value=3 and
    document value="foofo more"
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREFS/IDREFS_minLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/IDREFS/IDREFS_minLength003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_idrefs_min_length002_1436_idrefs_min_length002_1436_v():
    """
    TEST :Facet Schemas for string : facet=minLength and value=2 and
    document value="more foofo"
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREFS/IDREFS_minLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/IDREFS/IDREFS_minLength002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_idrefs_min_length001_1435_idrefs_min_length001_1435_v():
    """
    TEST :Facet Schemas for string : facet=minLength and value=1 and
    document value="foofo more"
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREFS/IDREFS_minLength001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/IDREFS/IDREFS_minLength001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_idrefs_length003_1434_idrefs_length003_1434_i():
    """
    TEST :Facet Schemas for string : facet=length and value=1 and document
    value="foofo more"
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREFS/IDREFS_length003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/IDREFS/IDREFS_length003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_idrefs_length002_1433_idrefs_length002_1433_v():
    """
    TEST :Facet Schemas for string : facet=length and value=2 and document
    value="foofo more"
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREFS/IDREFS_length002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/IDREFS/IDREFS_length002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_idrefs_length001_1432_idrefs_length001_1432_i():
    """
    TEST :Facet Schemas for string : facet=length and value=4 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/IDREFS/IDREFS_length001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/IDREFS/IDREFS_length001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_language_enumeration004_1431_language_enumeration004_1431_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=en fr de
    and document value=en
    """
    assert_bindings(
        schema="msData/datatypes/Facets/language/language_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/language/language_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_language_enumeration003_1430_language_enumeration003_1430_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=en fr de
    and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/language/language_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/language/language_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_language_enumeration002_1429_language_enumeration002_1429_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=en and
    document value=en
    """
    assert_bindings(
        schema="msData/datatypes/Facets/language/language_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/language/language_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_language_enumeration001_1428_language_enumeration001_1428_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=en and
    document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/language/language_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/language/language_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_language_pattern001_1427_language_pattern001_1427_v():
    """
    TEST :Facet Schemas for string : facet=pattern and value=en-[a-z]{2}
    and document value=en-xx
    """
    assert_bindings(
        schema="msData/datatypes/Facets/language/language_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/language/language_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_language_max_length003_1426_language_max_length003_1426_v():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=6 and
    document value=en-xx
    """
    assert_bindings(
        schema="msData/datatypes/Facets/language/language_maxLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/language/language_maxLength003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_language_max_length002_1425_language_max_length002_1425_v():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=5 and
    document value=en-xx
    """
    assert_bindings(
        schema="msData/datatypes/Facets/language/language_maxLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/language/language_maxLength002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_language_max_length001_1424_language_max_length001_1424_i():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=4 and
    document value=en-xx
    """
    assert_bindings(
        schema="msData/datatypes/Facets/language/language_maxLength001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/language/language_maxLength001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_language_min_length004_1423_language_min_length004_1423_v():
    """
    TEST :Facet Schemas for string : (facet=minLength and value=4 and
    facet=maxLength and value=6) and document value=en-xx
    """
    assert_bindings(
        schema="msData/datatypes/Facets/language/language_minLength004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/language/language_minLength004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_language_min_length003_1422_language_min_length003_1422_i():
    """
    TEST :Facet Schemas for string : facet=minLength and value=6 and
    document value=en-xx
    """
    assert_bindings(
        schema="msData/datatypes/Facets/language/language_minLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/language/language_minLength003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_language_min_length002_1421_language_min_length002_1421_v():
    """
    TEST :Facet Schemas for string : facet=minLength and value=5 and
    document value=en-xx
    """
    assert_bindings(
        schema="msData/datatypes/Facets/language/language_minLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/language/language_minLength002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_language_min_length001_1420_language_min_length001_1420_v():
    """
    TEST :Facet Schemas for string : facet=minLength and value=4 and
    document value=en-xx
    """
    assert_bindings(
        schema="msData/datatypes/Facets/language/language_minLength001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/language/language_minLength001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_language_length003_1419_language_length003_1419_i():
    """
    TEST :Facet Schemas for string : facet=length and value=6 and document
    value=en-xx
    """
    assert_bindings(
        schema="msData/datatypes/Facets/language/language_length003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/language/language_length003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_language_length002_1418_language_length002_1418_v():
    """
    TEST :Facet Schemas for string : facet=length and value=5 and document
    value=en-xx
    """
    assert_bindings(
        schema="msData/datatypes/Facets/language/language_length002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/language/language_length002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_language_length001_1417_language_length001_1417_i():
    """
    TEST :Facet Schemas for string : facet=length and value=4 and document
    value=en-xx
    """
    assert_bindings(
        schema="msData/datatypes/Facets/language/language_length001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/language/language_length001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_token_enumeration004_1416_token_enumeration004_1416_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    foo123 fu1 and document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/token/token_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/token/token_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_token_enumeration003_1415_token_enumeration003_1415_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    foo123 fu1 and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/token/token_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/token/token_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_token_enumeration002_1414_token_enumeration002_1414_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/token/token_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/token/token_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_token_enumeration001_1413_token_enumeration001_1413_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/token/token_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/token/token_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_token_pattern001_1412_token_pattern001_1412_v():
    """
    TEST :Facet Schemas for string : facet=pattern and value=[a-z]{3} and
    document value=abc
    """
    assert_bindings(
        schema="msData/datatypes/Facets/token/token_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/token/token_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_token_max_length003_1411_token_max_length003_1411_v():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=6 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/token/token_maxLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/token/token_maxLength003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_token_max_length002_1410_token_max_length002_1410_v():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/token/token_maxLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/token/token_maxLength002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_token_max_length001_1409_token_max_length001_1409_i():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=4 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/token/token_maxLength001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/token/token_maxLength001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_token_min_length004_1408_token_min_length004_1408_v():
    """
    TEST :Facet Schemas for string : (facet=minLength and value=4 and
    facet=maxLength and value=6) and document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/token/token_minLength004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/token/token_minLength004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_token_min_length003_1407_token_min_length003_1407_i():
    """
    TEST :Facet Schemas for string : facet=minLength and value=6 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/token/token_minLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/token/token_minLength003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_token_min_length002_1406_token_min_length002_1406_v():
    """
    TEST :Facet Schemas for string : facet=minLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/token/token_minLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/token/token_minLength002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_token_min_length001_1405_token_min_length001_1405_v():
    """
    TEST :Facet Schemas for string : facet=minLength and value=4 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/token/token_minLength001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/token/token_minLength001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_token_length003_1404_token_length003_1404_i():
    """
    TEST :Facet Schemas for string : facet=length and value=6 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/token/token_length003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/token/token_length003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_token_length002_1403_token_length002_1403_v():
    """
    TEST :Facet Schemas for string : facet=length and value=5 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/token/token_length002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/token/token_length002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_token_length001_1402_token_length001_1402_i():
    """
    TEST :Facet Schemas for string : facet=length and value=4 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/token/token_length001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/token/token_length001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_normalized_string_enumeration004_1401_normalized_string_enumeration004_1401_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    foo123 fu1 and document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/normalizedString/normalizedString_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/normalizedString/normalizedString_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_normalized_string_enumeration003_1400_normalized_string_enumeration003_1400_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    foo123 fu1 and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/normalizedString/normalizedString_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/normalizedString/normalizedString_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_normalized_string_enumeration002_1399_normalized_string_enumeration002_1399_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/normalizedString/normalizedString_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/normalizedString/normalizedString_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_normalized_string_enumeration001_1398_normalized_string_enumeration001_1398_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/normalizedString/normalizedString_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/normalizedString/normalizedString_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_normalized_string_pattern001_1397_normalized_string_pattern001_1397_v():
    """
    TEST :Facet Schemas for string : facet=pattern and value=[a-z]{3} and
    document value=abc
    """
    assert_bindings(
        schema="msData/datatypes/Facets/normalizedString/normalizedString_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/normalizedString/normalizedString_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_normalized_string_max_length003_1396_normalized_string_max_length003_1396_v():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=6 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/normalizedString/normalizedString_maxLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/normalizedString/normalizedString_maxLength003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_normalized_string_max_length002_1395_normalized_string_max_length002_1395_v():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/normalizedString/normalizedString_maxLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/normalizedString/normalizedString_maxLength002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_normalized_string_max_length001_1394_normalized_string_max_length001_1394_i():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=4 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/normalizedString/normalizedString_maxLength001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/normalizedString/normalizedString_maxLength001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_normalized_string_min_length004_1393_normalized_string_min_length004_1393_v():
    """
    TEST :Facet Schemas for string : (facet=minLength and value=4 and
    facet=maxLength and value=6) and document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/normalizedString/normalizedString_minLength004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/normalizedString/normalizedString_minLength004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_normalized_string_min_length003_1392_normalized_string_min_length003_1392_i():
    """
    TEST :Facet Schemas for string : facet=minLength and value=6 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/normalizedString/normalizedString_minLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/normalizedString/normalizedString_minLength003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_normalized_string_min_length002_1391_normalized_string_min_length002_1391_v():
    """
    TEST :Facet Schemas for string : facet=minLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/normalizedString/normalizedString_minLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/normalizedString/normalizedString_minLength002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_normalized_string_min_length001_1390_normalized_string_min_length001_1390_v():
    """
    TEST :Facet Schemas for string : facet=minLength and value=4 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/normalizedString/normalizedString_minLength001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/normalizedString/normalizedString_minLength001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_normalized_string_length003_1389_normalized_string_length003_1389_i():
    """
    TEST :Facet Schemas for string : facet=length and value=6 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/normalizedString/normalizedString_length003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/normalizedString/normalizedString_length003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_normalized_string_length002_1388_normalized_string_length002_1388_v():
    """
    TEST :Facet Schemas for string : facet=length and value=5 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/normalizedString/normalizedString_length002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/normalizedString/normalizedString_length002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_normalized_string_length001_1387_normalized_string_length001_1387_i():
    """
    TEST :Facet Schemas for string : facet=length and value=4 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/normalizedString/normalizedString_length001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/normalizedString/normalizedString_length001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_notation_enumeration004_1386_notation_enumeration004_1386_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    foo123 fu1 and document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NOTATION/NOTATION_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NOTATION/NOTATION_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_notation_enumeration003_1385_notation_enumeration003_1385_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    foo123 fu1 and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NOTATION/NOTATION_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NOTATION/NOTATION_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_notation_enumeration002_1384_notation_enumeration002_1384_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NOTATION/NOTATION_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NOTATION/NOTATION_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_notation_enumeration001_1383_notation_enumeration001_1383_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NOTATION/NOTATION_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NOTATION/NOTATION_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_notation_pattern001_1382_notation_pattern001_1382_v():
    """
    TEST :Facet Schemas for string : facet=pattern and value=[a-z]{3} and
    document value=abc
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NOTATION/NOTATION_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NOTATION/NOTATION_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_notation_max_length003_1381_notation_max_length003_1381_v():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=6 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NOTATION/NOTATION_maxLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NOTATION/NOTATION_maxLength003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_notation_max_length002_1380_notation_max_length002_1380_v():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NOTATION/NOTATION_maxLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NOTATION/NOTATION_maxLength002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_notation_max_length001_1379_notation_max_length001_1379_i():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=4 and
    document value=foofo TSTF ruled that 1.0 says all QNames satisfy all
    length-related tess
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NOTATION/NOTATION_maxLength001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NOTATION/NOTATION_maxLength001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_notation_min_length004_1378_notation_min_length004_1378_v():
    """
    TEST :Facet Schemas for string : (facet=minLength and value=4 and
    facet=maxLength and value=6) and document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NOTATION/NOTATION_minLength004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NOTATION/NOTATION_minLength004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_notation_min_length003_1377_notation_min_length003_1377_i():
    """
    TEST :Facet Schemas for string : facet=minLength and value=6 and
    document value=foofo TSTF ruled that 1.0 says all QNames satisfy all
    length-related tess
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NOTATION/NOTATION_minLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NOTATION/NOTATION_minLength003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_notation_min_length002_1376_notation_min_length002_1376_v():
    """
    TEST :Facet Schemas for string : facet=minLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NOTATION/NOTATION_minLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NOTATION/NOTATION_minLength002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_notation_min_length001_1375_notation_min_length001_1375_v():
    """
    TEST :Facet Schemas for string : facet=minLength and value=4 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NOTATION/NOTATION_minLength001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NOTATION/NOTATION_minLength001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_notation_length003_1374_notation_length003_1374_i():
    """
    TEST :Facet Schemas for string : facet=length and value=6 and document
    value=foofo TSTF ruled that 1.0 says all QNames satisfy all length-
    related tess
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NOTATION/NOTATION_length003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NOTATION/NOTATION_length003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_notation_length002_1373_notation_length002_1373_v():
    """
    TEST :Facet Schemas for string : facet=length and value=5 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NOTATION/NOTATION_length002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NOTATION/NOTATION_length002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_notation_length001_1372_notation_length001_1372_i():
    """
    TEST :Facet Schemas for string : facet=length and value=4 and document
    value=foofo TSTF ruled that 1.0 says all QNames satisfy all length-
    related tess
    """
    assert_bindings(
        schema="msData/datatypes/Facets/NOTATION/NOTATION_length001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/NOTATION/NOTATION_length001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


@pytest.mark.xfail
def test_qname_enumeration004_1371_qname_enumeration004_1371_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo:fo
    foo:foo123 foo:fu1 and document value=foo:fo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/QName/QName_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/QName/QName_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_qname_enumeration003_1370_qname_enumeration003_1370_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo:fo
    foo:foo123 foo:fu1 and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/QName/QName_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/QName/QName_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


@pytest.mark.xfail
def test_qname_enumeration002_1369_qname_enumeration002_1369_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo:fo
    and document value=foo:fo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/QName/QName_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/QName/QName_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_qname_enumeration001_1368_qname_enumeration001_1368_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo:fo
    and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/QName/QName_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/QName/QName_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_qname_pattern001_1367_qname_pattern001_1367_v():
    """
    TEST :Facet Schemas for string : facet=pattern and value=[a-z]{3} and
    document value=abc
    """
    assert_bindings(
        schema="msData/datatypes/Facets/QName/QName_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/QName/QName_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_qname_max_length003_1366_qname_max_length003_1366_v():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=6 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/QName/QName_maxLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/QName/QName_maxLength003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_qname_max_length002_1365_qname_max_length002_1365_v():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/QName/QName_maxLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/QName/QName_maxLength002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_qname_max_length001_1364_qname_max_length001_1364_i():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=4 and
    document value=foofo TSTF ruled that 1.0 says all QNames satisfy all
    length-related tess
    """
    assert_bindings(
        schema="msData/datatypes/Facets/QName/QName_maxLength001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/QName/QName_maxLength001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_qname_min_length004_1363_qname_min_length004_1363_v():
    """
    TEST :Facet Schemas for string : (facet=minLength and value=4 and
    facet=maxLength and value=6) and document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/QName/QName_minLength004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/QName/QName_minLength004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_qname_min_length003_1362_qname_min_length003_1362_i():
    """
    TEST :Facet Schemas for string : facet=minLength and value=6 and
    document value=foofo TSTF ruled that 1.0 says all QNames satisfy all
    length-related tess
    """
    assert_bindings(
        schema="msData/datatypes/Facets/QName/QName_minLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/QName/QName_minLength003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_qname_min_length002_1361_qname_min_length002_1361_v():
    """
    TEST :Facet Schemas for string : facet=minLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/QName/QName_minLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/QName/QName_minLength002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_qname_min_length001_1360_qname_min_length001_1360_v():
    """
    TEST :Facet Schemas for string : facet=minLength and value=4 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/QName/QName_minLength001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/QName/QName_minLength001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_qname_length003_1359_qname_length003_1359_i():
    """
    TEST :Facet Schemas for string : facet=length and value=6 and document
    value=foofo TSTF ruled that 1.0 says all QNames satisfy all length-
    related tess
    """
    assert_bindings(
        schema="msData/datatypes/Facets/QName/QName_length003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/QName/QName_length003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_qname_length002_1358_qname_length002_1358_v():
    """
    TEST :Facet Schemas for string : facet=length and value=5 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/QName/QName_length002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/QName/QName_length002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_qname_length001_1357_qname_length001_1357_i():
    """
    TEST :Facet Schemas for string : facet=length and value=4 and document
    value=foofo TSTF ruled that 1.0 says all QNames satisfy all length-
    related tess
    """
    assert_bindings(
        schema="msData/datatypes/Facets/QName/QName_length001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/QName/QName_length001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


@pytest.mark.schema11
@pytest.mark.xfail
def test_any_uri_b006_1356_any_uri_b006_1356_i():
    r"""
    TEST :Facet Schemas for string : test with //, \\, \, /, and many
    combinations of \ and / TSTF ruled that strictly speaking, per 1.0,
    the schema contains one or more invalid anyURIs In XSD 1.1, any
    sequence of characters is allowed in xs:anyURI, so the schema becomes
    valid;             but the instance is invalid because the value \a is
    not present in the enumeration facet - MHK
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_b006.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/anyURI/anyURI_b006.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.1",
    )


def test_any_uri_b005_1355_any_uri_b005_1355_i():
    """
    TEST :Facet Schemas for string : 2 spaces should not match one %20,
    enumeration of anyURI: http://a/x%20y, and instance has http://a/x y
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_b005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/anyURI/anyURI_b005.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.schema11
def test_any_uri_b004_1354_any_uri_b004_1354_v():
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
        is_valid=True,
        instance="msData/datatypes/Facets/anyURI/anyURI_b004.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.1",
    )


def test_any_uri_b002_1353_any_uri_b002_1353_v():
    """
    TEST :Facet Schemas for string : enum of anyURI: with dbcs char, and
    instance has valid dbcs char
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_b002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/anyURI/anyURI_b002.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_any_uri_b001_1352_any_uri_b001_1352_i():
    """
    TEST :Facet Schemas for string : enum of anyURI: c, and instance has
    anyURI:c
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_b001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/anyURI/anyURI_b001.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_any_uri_a004_1339_any_uri_a004_1339_i():
    """
    TEST :Facet Schemas for string : test that uri with ftp:// gofer://
    mailto: news: telnet: are accepted in anyURI Schema doc changed to
    guaranteed-to-fail URIs, but that does not make the schema (or
    instance) invalid -- see http://www.w3.org/TR/xmlschema-1/#src-include
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_a004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/anyURI/anyURI_a004.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_any_uri_a002_1337_any_uri_a002_1337_v():
    """
    TEST :Facet Schemas for string : test that dbcs charanters are allowed
    as anyURI in, any, anyAttribute, notation, appinfo, documentation,
    schema, include, redefine, import
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_a002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/anyURI/anyURI_a002.xml",
        instance_is_valid=True,
        class_name="",
        version="1.0",
    )


@pytest.mark.schema11
def test_any_uri_a001_1336_any_uri_a001_1336_v():
    """
    TEST :Facet Schemas for string : test that the numbers are allowed as
    anyURI in, any, anyAttribute, notation, appinfo, documentation,
    schema, include, redefine, import TSTF ruled that strictly speaking,
    per 1.0, the schema contains         one or more invalid anyURIs
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_a001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/anyURI/anyURI_a001.xml",
        instance_is_valid=True,
        class_name="Bar",
        version="1.1",
    )


def test_any_uri_enumeration004_1335_any_uri_enumeration004_1335_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    http://www.microsoft.com mailto:davebrow@microsoft.com and document
    value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/anyURI/anyURI_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_any_uri_enumeration003_1334_any_uri_enumeration003_1334_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo
    http://www.microsoft.com mailto:davebrow@microsoft.com and document
    value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/anyURI/anyURI_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_any_uri_enumeration002_1333_any_uri_enumeration002_1333_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/anyURI/anyURI_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_any_uri_enumeration001_1332_any_uri_enumeration001_1332_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/anyURI/anyURI_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_any_uri_max_length003_1331_any_uri_max_length003_1331_v():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=6 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_maxLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/anyURI/anyURI_maxLength003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_any_uri_max_length002_1330_any_uri_max_length002_1330_v():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_maxLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/anyURI/anyURI_maxLength002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_any_uri_max_length001_1329_any_uri_max_length001_1329_i():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=4 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_maxLength001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/anyURI/anyURI_maxLength001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_any_uri_min_length004_1328_any_uri_min_length004_1328_v():
    """
    TEST :Facet Schemas for string : (facet=minLength and value=4 and
    facet=maxLength and value=6) and document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_minLength004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/anyURI/anyURI_minLength004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_any_uri_min_length003_1327_any_uri_min_length003_1327_i():
    """
    TEST :Facet Schemas for string : facet=minLength and value=6 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_minLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/anyURI/anyURI_minLength003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_any_uri_min_length002_1326_any_uri_min_length002_1326_v():
    """
    TEST :Facet Schemas for string : facet=minLength and value=5 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_minLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/anyURI/anyURI_minLength002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_any_uri_min_length001_1325_any_uri_min_length001_1325_v():
    """
    TEST :Facet Schemas for string : facet=minLength and value=4 and
    document value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_minLength001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/anyURI/anyURI_minLength001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_any_uri_length003_1324_any_uri_length003_1324_i():
    """
    TEST :Facet Schemas for string : facet=length and value=6 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_length003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/anyURI/anyURI_length003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_any_uri_length002_1323_any_uri_length002_1323_v():
    """
    TEST :Facet Schemas for string : facet=length and value=5 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_length002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/anyURI/anyURI_length002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_any_uri_length001_1322_any_uri_length001_1322_i():
    """
    TEST :Facet Schemas for string : facet=length and value=4 and document
    value=foofo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/anyURI/anyURI_length001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/anyURI/anyURI_length001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_base64_binary_enumeration002_1320_base64_binary_enumeration002_1320_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=MS0yLTM=
    and document value=MS0yLTM=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/base64Binary/base64Binary_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/base64Binary/base64Binary_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_base64_binary_enumeration001_1319_base64_binary_enumeration001_1319_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=MS0yLTM=
    and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/base64Binary/base64Binary_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/base64Binary/base64Binary_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_base64_binary_max_length003_1318_base64_binary_max_length003_1318_i():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=6 and
    document value=abcde
    """
    assert_bindings(
        schema="msData/datatypes/Facets/base64Binary/base64Binary_maxLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/base64Binary/base64Binary_maxLength003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_base64_binary_max_length002_1317_base64_binary_max_length002_1317_i():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=5 and
    document value=abcde
    """
    assert_bindings(
        schema="msData/datatypes/Facets/base64Binary/base64Binary_maxLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/base64Binary/base64Binary_maxLength002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_base64_binary_max_length001_1316_base64_binary_max_length001_1316_i():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=4 and
    document value=abcde
    """
    assert_bindings(
        schema="msData/datatypes/Facets/base64Binary/base64Binary_maxLength001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/base64Binary/base64Binary_maxLength001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_base64_binary_min_length004_1315_base64_binary_min_length004_1315_v():
    """
    TEST :Facet Schemas for string : (facet=minLength and value=4 and
    facet=maxLength and value=6) and document value=MS0yLTM=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/base64Binary/base64Binary_minLength004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/base64Binary/base64Binary_minLength004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_base64_binary_min_length003_1314_base64_binary_min_length003_1314_i():
    """
    TEST :Facet Schemas for string : facet=minLength and value=6 and
    document value=abcde
    """
    assert_bindings(
        schema="msData/datatypes/Facets/base64Binary/base64Binary_minLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/base64Binary/base64Binary_minLength003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_base64_binary_min_length002_1313_base64_binary_min_length002_1313_v():
    """
    TEST :Facet Schemas for string : facet=minLength and value=5 and
    document value=MS0yLTM=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/base64Binary/base64Binary_minLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/base64Binary/base64Binary_minLength002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_base64_binary_min_length001_1312_base64_binary_min_length001_1312_v():
    """
    TEST :Facet Schemas for string : facet=minLength and value=4 and
    document value=MS0yLTM=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/base64Binary/base64Binary_minLength001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/base64Binary/base64Binary_minLength001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_base64_binary_length003_1311_base64_binary_length003_1311_i():
    """
    TEST :Facet Schemas for string : facet=length and value=6 and document
    value=abcde
    """
    assert_bindings(
        schema="msData/datatypes/Facets/base64Binary/base64Binary_length003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/base64Binary/base64Binary_length003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_base64_binary_length002_1310_base64_binary_length002_1310_v():
    """
    TEST :Facet Schemas for string : facet=length and value=5 and document
    value=MS0yLTM=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/base64Binary/base64Binary_length002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/base64Binary/base64Binary_length002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_base64_binary_length001_1309_base64_binary_length001_1309_i():
    """
    TEST :Facet Schemas for string : facet=length and value=4 and document
    value=abcde
    """
    assert_bindings(
        schema="msData/datatypes/Facets/base64Binary/base64Binary_length001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/base64Binary/base64Binary_length001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_hex_binary_enumeration004_1308_hex_binary_enumeration004_1308_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=adf789
    abcedf 0123456789 and document value=adf789
    """
    assert_bindings(
        schema="msData/datatypes/Facets/hexBinary/hexBinary_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/hexBinary/hexBinary_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_hex_binary_enumeration003_1307_hex_binary_enumeration003_1307_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=adf789
    abcedf 0123456789 and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/hexBinary/hexBinary_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/hexBinary/hexBinary_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_hex_binary_enumeration002_1306_hex_binary_enumeration002_1306_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=adf789
    and document value=adf789
    """
    assert_bindings(
        schema="msData/datatypes/Facets/hexBinary/hexBinary_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/hexBinary/hexBinary_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_hex_binary_enumeration001_1305_hex_binary_enumeration001_1305_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=adf789
    and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/hexBinary/hexBinary_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/hexBinary/hexBinary_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_hex_binary_max_length003_1304_hex_binary_max_length003_1304_v():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=6 and
    document value=abcde
    """
    assert_bindings(
        schema="msData/datatypes/Facets/hexBinary/hexBinary_maxLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/hexBinary/hexBinary_maxLength003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_hex_binary_max_length002_1303_hex_binary_max_length002_1303_v():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=5 and
    document value=abcde
    """
    assert_bindings(
        schema="msData/datatypes/Facets/hexBinary/hexBinary_maxLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/hexBinary/hexBinary_maxLength002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_hex_binary_max_length001_1302_hex_binary_max_length001_1302_v():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=4 and
    document value=abcde
    """
    assert_bindings(
        schema="msData/datatypes/Facets/hexBinary/hexBinary_maxLength001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/hexBinary/hexBinary_maxLength001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_hex_binary_min_length004_1301_hex_binary_min_length004_1301_v():
    """
    TEST :Facet Schemas for string : (facet=minLength and value=4 and
    facet=maxLength and value=6) and document value=abcdef1234 (let's try
    5 Octets [ab cd ef 12 34]
    """
    assert_bindings(
        schema="msData/datatypes/Facets/hexBinary/hexBinary_minLength004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/hexBinary/hexBinary_minLength004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_hex_binary_min_length003_1300_hex_binary_min_length003_1300_i():
    """
    TEST :Facet Schemas for string : facet=minLength and value=6 and
    document value=abcde
    """
    assert_bindings(
        schema="msData/datatypes/Facets/hexBinary/hexBinary_minLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/hexBinary/hexBinary_minLength003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_hex_binary_min_length002_1299_hex_binary_min_length002_1299_v():
    """
    TEST :Facet Schemas for string : facet=minLength and value=5 and
    document value=abcdef123456. Let's try 6 Octets [ab cd ef 12 34 56]
    """
    assert_bindings(
        schema="msData/datatypes/Facets/hexBinary/hexBinary_minLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/hexBinary/hexBinary_minLength002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_hex_binary_min_length001_1298_hex_binary_min_length001_1298_v():
    """
    TEST :Facet Schemas for string : facet=minLength and value=4 and
    document value=abcdefab 4 Octets are [ab cd ef ab]
    """
    assert_bindings(
        schema="msData/datatypes/Facets/hexBinary/hexBinary_minLength001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/hexBinary/hexBinary_minLength001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_hex_binary_length003_1297_hex_binary_length003_1297_i():
    """
    TEST :Facet Schemas for string : facet=length and value=6 and document
    value=abcde
    """
    assert_bindings(
        schema="msData/datatypes/Facets/hexBinary/hexBinary_length003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/hexBinary/hexBinary_length003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_hex_binary_length002_1296_hex_binary_length002_1296_v():
    """
    TEST :Facet Schemas for string : facet=length and value=5 and document
    value=abcdefabcd where 5 Octets are [ab cd ef ab cd]
    """
    assert_bindings(
        schema="msData/datatypes/Facets/hexBinary/hexBinary_length002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/hexBinary/hexBinary_length002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_hex_binary_length001_1295_hex_binary_length001_1295_i():
    """
    TEST :Facet Schemas for string : facet=length and value=4 and document
    value=abcde
    """
    assert_bindings(
        schema="msData/datatypes/Facets/hexBinary/hexBinary_length001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/hexBinary/hexBinary_length001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_month_pattern001_1274_g_month_pattern001_1274_v():
    """
    TEST :Facet Schemas for string : facet=pattern and value=- -[0-9]{2}-
    - and document value=- -03- -
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gMonth/gMonth_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gMonth/gMonth_pattern001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_day_min_exclusive005_1273_g_day_min_exclusive005_1273_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=- - -01
    and facet=maxExclusive and value=- - -30) and document value=- - -15
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gDay/gDay_minExclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gDay/gDay_minExclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_day_min_exclusive004_1272_g_day_min_exclusive004_1272_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=- - -01
    and facet=maxInclusive and value=- - -30) and document value=- - -15
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gDay/gDay_minExclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gDay/gDay_minExclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_day_min_exclusive003_1271_g_day_min_exclusive003_1271_v():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=- - -01
    and document value=- - -15
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gDay/gDay_minExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gDay/gDay_minExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_day_min_exclusive002_1270_g_day_min_exclusive002_1270_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=- - -15
    and document value=- - -01
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gDay/gDay_minExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gDay/gDay_minExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_day_min_exclusive001_1269_g_day_min_exclusive001_1269_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=- - -01
    and document value=- - -01
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gDay/gDay_minExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gDay/gDay_minExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_day_min_inclusive005_1268_g_day_min_inclusive005_1268_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=- - -01
    and facet=maxExclusive and value=- - -30) and document value=- - -15
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gDay/gDay_minInclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gDay/gDay_minInclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_day_min_inclusive004_1267_g_day_min_inclusive004_1267_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=- - -01
    and facet=maxInclusive and value=- - -30) and document value=- - -15
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gDay/gDay_minInclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gDay/gDay_minInclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_day_min_inclusive003_1266_g_day_min_inclusive003_1266_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=- - -01
    and document value=- - -15
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gDay/gDay_minInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gDay/gDay_minInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_day_min_inclusive002_1265_g_day_min_inclusive002_1265_i():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=- - -15
    and document value=- - -01
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gDay/gDay_minInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gDay/gDay_minInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_day_min_inclusive001_1264_g_day_min_inclusive001_1264_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=- - -01
    and document value=- - -01
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gDay/gDay_minInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gDay/gDay_minInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_day_max_exclusive003_1263_g_day_max_exclusive003_1263_v():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=- - -30
    and document value=- - -15
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gDay/gDay_maxExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gDay/gDay_maxExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_day_max_exclusive002_1262_g_day_max_exclusive002_1262_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=- - -01
    and document value=- - -15
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gDay/gDay_maxExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gDay/gDay_maxExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_day_max_exclusive001_1261_g_day_max_exclusive001_1261_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=- - -01
    and document value=- - -01
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gDay/gDay_maxExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gDay/gDay_maxExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_day_max_inclusive003_1260_g_day_max_inclusive003_1260_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=- - -30
    and document value=- - -15
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gDay/gDay_maxInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gDay/gDay_maxInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_day_max_inclusive002_1259_g_day_max_inclusive002_1259_i():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=- - -01
    and document value=- - -15
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gDay/gDay_maxInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gDay/gDay_maxInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_day_max_inclusive001_1258_g_day_max_inclusive001_1258_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=- - -01
    and document value=- - -01
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gDay/gDay_maxInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gDay/gDay_maxInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_day_enumeration004_1257_g_day_enumeration004_1257_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=- - -15 -
    - -01 - - -30 and document value=- - -15
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gDay/gDay_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gDay/gDay_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_day_enumeration003_1256_g_day_enumeration003_1256_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=- - -15 -
    - -01 - - -30 and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gDay/gDay_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gDay/gDay_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_day_enumeration002_1255_g_day_enumeration002_1255_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=- - -15
    and document value=- - -15
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gDay/gDay_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gDay/gDay_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_day_enumeration001_1254_g_day_enumeration001_1254_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=- - -15
    and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gDay/gDay_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gDay/gDay_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_day_pattern001_1253_g_day_pattern001_1253_v():
    """
    TEST :Facet Schemas for string : facet=pattern and value=- - -[0-9]{2}
    and document value=- - -15
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gDay/gDay_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gDay/gDay_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_month_day_min_exclusive005_1252_g_month_day_min_exclusive005_1252_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=-
    -01-01 and facet=maxExclusive and value=- -10-01) and document value=-
    -03-15
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gMonthDay/gMonthDay_minExclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gMonthDay/gMonthDay_minExclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_month_day_min_exclusive004_1251_g_month_day_min_exclusive004_1251_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=-
    -01-01 and facet=maxInclusive and value=- -10-01) and document value=-
    -03-15
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gMonthDay/gMonthDay_minExclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gMonthDay/gMonthDay_minExclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_month_day_min_exclusive003_1250_g_month_day_min_exclusive003_1250_v():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=- -01-01
    and document value=- -03-15
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gMonthDay/gMonthDay_minExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gMonthDay/gMonthDay_minExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_month_day_min_exclusive002_1249_g_month_day_min_exclusive002_1249_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=- -03-15
    and document value=- -01-01
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gMonthDay/gMonthDay_minExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gMonthDay/gMonthDay_minExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_month_day_min_exclusive001_1248_g_month_day_min_exclusive001_1248_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=- -01-01
    and document value=- -01-01
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gMonthDay/gMonthDay_minExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gMonthDay/gMonthDay_minExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_month_day_min_inclusive005_1247_g_month_day_min_inclusive005_1247_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=-
    -01-01 and facet=maxExclusive and value=- -10-01) and document value=-
    -03-15
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gMonthDay/gMonthDay_minInclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gMonthDay/gMonthDay_minInclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_month_day_min_inclusive004_1246_g_month_day_min_inclusive004_1246_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=-
    -01-01 and facet=maxInclusive and value=- -10-01) and document value=-
    -03-15
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gMonthDay/gMonthDay_minInclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gMonthDay/gMonthDay_minInclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_month_day_min_inclusive003_1245_g_month_day_min_inclusive003_1245_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=- -01-01
    and document value=- -03-15
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gMonthDay/gMonthDay_minInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gMonthDay/gMonthDay_minInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_month_day_min_inclusive002_1244_g_month_day_min_inclusive002_1244_i():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=- -03-15
    and document value=- -01-01
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gMonthDay/gMonthDay_minInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gMonthDay/gMonthDay_minInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_month_day_min_inclusive001_1243_g_month_day_min_inclusive001_1243_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=- -01-01
    and document value=- -01-01
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gMonthDay/gMonthDay_minInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gMonthDay/gMonthDay_minInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_month_day_max_exclusive003_1242_g_month_day_max_exclusive003_1242_v():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=- -10-01
    and document value=- -03-15
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gMonthDay/gMonthDay_maxExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gMonthDay/gMonthDay_maxExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_month_day_max_exclusive002_1241_g_month_day_max_exclusive002_1241_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=- -01-01
    and document value=- -03-15
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gMonthDay/gMonthDay_maxExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gMonthDay/gMonthDay_maxExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_month_day_max_exclusive001_1240_g_month_day_max_exclusive001_1240_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=- -01-01
    and document value=- -01-01
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gMonthDay/gMonthDay_maxExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gMonthDay/gMonthDay_maxExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_month_day_max_inclusive003_1239_g_month_day_max_inclusive003_1239_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=- -10-01
    and document value=- -03-15
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gMonthDay/gMonthDay_maxInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gMonthDay/gMonthDay_maxInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_month_day_max_inclusive002_1238_g_month_day_max_inclusive002_1238_i():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=- -01-01
    and document value=- -03-15
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gMonthDay/gMonthDay_maxInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gMonthDay/gMonthDay_maxInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_month_day_max_inclusive001_1237_g_month_day_max_inclusive001_1237_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=- -01-01
    and document value=- -01-01
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gMonthDay/gMonthDay_maxInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gMonthDay/gMonthDay_maxInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_month_day_enumeration004_1236_g_month_day_enumeration004_1236_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=- -03-15
    - -01-01 - -10-01 and document value=- -03-15
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gMonthDay/gMonthDay_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gMonthDay/gMonthDay_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_month_day_enumeration003_1235_g_month_day_enumeration003_1235_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=- -03-15
    - -01-01 - -10-01 and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gMonthDay/gMonthDay_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gMonthDay/gMonthDay_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_month_day_enumeration002_1234_g_month_day_enumeration002_1234_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=- -03-15
    and document value=- -03-15
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gMonthDay/gMonthDay_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gMonthDay/gMonthDay_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_month_day_enumeration001_1233_g_month_day_enumeration001_1233_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=- -03-15
    and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gMonthDay/gMonthDay_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gMonthDay/gMonthDay_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_month_day_pattern001_1232_g_month_day_pattern001_1232_v():
    """
    TEST :Facet Schemas for string : facet=pattern and value=-
    -[0-9]{2}-[0-9]{2} and document value=- -03-15
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gMonthDay/gMonthDay_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gMonthDay/gMonthDay_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_year_min_exclusive005_1231_g_year_min_exclusive005_1231_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1998
    and facet=maxExclusive and value=2002) and document value=2000
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYear/gYear_minExclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYear/gYear_minExclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_year_min_exclusive004_1230_g_year_min_exclusive004_1230_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1998
    and facet=maxInclusive and value=2002) and document value=2000
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYear/gYear_minExclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYear/gYear_minExclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_year_min_exclusive003_1229_g_year_min_exclusive003_1229_v():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1998 and
    document value=2000
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYear/gYear_minExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYear/gYear_minExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_year_min_exclusive002_1228_g_year_min_exclusive002_1228_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=2000 and
    document value=1998
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYear/gYear_minExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYear/gYear_minExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_year_min_exclusive001_1227_g_year_min_exclusive001_1227_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1998 and
    document value=1998
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYear/gYear_minExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYear/gYear_minExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_year_min_inclusive005_1226_g_year_min_inclusive005_1226_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1998
    and facet=maxExclusive and value=2002) and document value=2000
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYear/gYear_minInclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYear/gYear_minInclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_year_min_inclusive004_1225_g_year_min_inclusive004_1225_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1998
    and facet=maxInclusive and value=2002) and document value=2000
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYear/gYear_minInclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYear/gYear_minInclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_year_min_inclusive003_1224_g_year_min_inclusive003_1224_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1998 and
    document value=2000
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYear/gYear_minInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYear/gYear_minInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_year_min_inclusive002_1223_g_year_min_inclusive002_1223_i():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=2000 and
    document value=1998
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYear/gYear_minInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYear/gYear_minInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_year_min_inclusive001_1222_g_year_min_inclusive001_1222_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1998 and
    document value=1998
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYear/gYear_minInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYear/gYear_minInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_year_max_exclusive003_1221_g_year_max_exclusive003_1221_v():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=2002 and
    document value=2000
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYear/gYear_maxExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYear/gYear_maxExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_year_max_exclusive002_1220_g_year_max_exclusive002_1220_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=1998 and
    document value=2000
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYear/gYear_maxExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYear/gYear_maxExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_year_max_exclusive001_1219_g_year_max_exclusive001_1219_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=1998 and
    document value=1998
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYear/gYear_maxExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYear/gYear_maxExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_year_max_inclusive003_1218_g_year_max_inclusive003_1218_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=2002 and
    document value=2000
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYear/gYear_maxInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYear/gYear_maxInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_year_max_inclusive002_1217_g_year_max_inclusive002_1217_i():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1998 and
    document value=2000
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYear/gYear_maxInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYear/gYear_maxInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_year_max_inclusive001_1216_g_year_max_inclusive001_1216_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1998 and
    document value=1998
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYear/gYear_maxInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYear/gYear_maxInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_year_enumeration004_1215_g_year_enumeration004_1215_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=2000 1999
    2038 and document value=2000
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYear/gYear_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYear/gYear_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_year_enumeration003_1214_g_year_enumeration003_1214_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=2000 1999
    2038 and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYear/gYear_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYear/gYear_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_year_enumeration002_1213_g_year_enumeration002_1213_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=2000 and
    document value=2000
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYear/gYear_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYear/gYear_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_year_enumeration001_1212_g_year_enumeration001_1212_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=2000 and
    document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYear/gYear_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYear/gYear_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_year_pattern001_1211_g_year_pattern001_1211_v():
    """
    TEST :Facet Schemas for string : facet=pattern and value=[0-9]{4} and
    document value=2000
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYear/gYear_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYear/gYear_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_year_month_min_exclusive005_1210_g_year_month_min_exclusive005_1210_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=2000-12
    and facet=maxExclusive and value=2001-12) and document value=2001-03
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYearMonth/gYearMonth_minExclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYearMonth/gYearMonth_minExclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_year_month_min_exclusive004_1209_g_year_month_min_exclusive004_1209_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=2000-12
    and facet=maxInclusive and value=2001-12) and document value=2001-03
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYearMonth/gYearMonth_minExclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYearMonth/gYearMonth_minExclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_year_month_min_exclusive003_1208_g_year_month_min_exclusive003_1208_v():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=2000-12
    and document value=2001-03
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYearMonth/gYearMonth_minExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYearMonth/gYearMonth_minExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_year_month_min_exclusive002_1207_g_year_month_min_exclusive002_1207_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=2001-03
    and document value=2000-12
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYearMonth/gYearMonth_minExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYearMonth/gYearMonth_minExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_year_month_min_exclusive001_1206_g_year_month_min_exclusive001_1206_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=2000-12
    and document value=2000-12
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYearMonth/gYearMonth_minExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYearMonth/gYearMonth_minExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_year_month_min_inclusive005_1205_g_year_month_min_inclusive005_1205_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=2000-12
    and facet=maxExclusive and value=2001-12) and document value=2001-03
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYearMonth/gYearMonth_minInclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYearMonth/gYearMonth_minInclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_year_month_min_inclusive004_1204_g_year_month_min_inclusive004_1204_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=2000-12
    and facet=maxInclusive and value=2001-12) and document value=2001-03
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYearMonth/gYearMonth_minInclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYearMonth/gYearMonth_minInclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_year_month_min_inclusive003_1203_g_year_month_min_inclusive003_1203_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=2000-12
    and document value=2001-03
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYearMonth/gYearMonth_minInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYearMonth/gYearMonth_minInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_year_month_min_inclusive002_1202_g_year_month_min_inclusive002_1202_i():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=2001-03
    and document value=2000-12
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYearMonth/gYearMonth_minInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYearMonth/gYearMonth_minInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_year_month_min_inclusive001_1201_g_year_month_min_inclusive001_1201_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=2000-12
    and document value=2000-12
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYearMonth/gYearMonth_minInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYearMonth/gYearMonth_minInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_year_month_max_exclusive003_1200_g_year_month_max_exclusive003_1200_v():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=2001-12
    and document value=2001-03
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYearMonth/gYearMonth_maxExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYearMonth/gYearMonth_maxExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_year_month_max_exclusive002_1199_g_year_month_max_exclusive002_1199_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=2000-12
    and document value=2001-03
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYearMonth/gYearMonth_maxExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYearMonth/gYearMonth_maxExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_year_month_max_exclusive001_1198_g_year_month_max_exclusive001_1198_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=2000-12
    and document value=2000-12
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYearMonth/gYearMonth_maxExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYearMonth/gYearMonth_maxExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_year_month_max_inclusive003_1197_g_year_month_max_inclusive003_1197_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=2001-12
    and document value=2001-03
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYearMonth/gYearMonth_maxInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYearMonth/gYearMonth_maxInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_year_month_max_inclusive002_1196_g_year_month_max_inclusive002_1196_i():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=2000-12
    and document value=2001-03
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYearMonth/gYearMonth_maxInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYearMonth/gYearMonth_maxInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_year_month_max_inclusive001_1195_g_year_month_max_inclusive001_1195_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=2000-12
    and document value=2000-12
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYearMonth/gYearMonth_maxInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYearMonth/gYearMonth_maxInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_year_month_enumeration004_1194_g_year_month_enumeration004_1194_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=2001-03
    2000-10 2001-12 and document value=2001-03
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYearMonth/gYearMonth_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYearMonth/gYearMonth_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_year_month_enumeration003_1193_g_year_month_enumeration003_1193_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=2001-03
    2000-10 2001-12 and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYearMonth/gYearMonth_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYearMonth/gYearMonth_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_year_month_enumeration002_1192_g_year_month_enumeration002_1192_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=2001-03
    and document value=2001-03
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYearMonth/gYearMonth_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYearMonth/gYearMonth_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_g_year_month_enumeration001_1191_g_year_month_enumeration001_1191_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=2001-03
    and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYearMonth/gYearMonth_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYearMonth/gYearMonth_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_g_year_month_pattern001_1190_g_year_month_pattern001_1190_v():
    """
    TEST :Facet Schemas for string : facet=pattern and
    value=[0-9]{4}-[0-9]{2} and document value=2001-03
    """
    assert_bindings(
        schema="msData/datatypes/Facets/gYearMonth/gYearMonth_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/gYearMonth/gYearMonth_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_date_min_exclusive005_1189_date_min_exclusive005_1189_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and
    value=1999-01-31 and facet=maxExclusive and value=2000-05-31) and
    document value=1999-05-31
    """
    assert_bindings(
        schema="msData/datatypes/Facets/date/date_minExclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/date/date_minExclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_date_min_exclusive004_1188_date_min_exclusive004_1188_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and
    value=1999-01-31 and facet=maxInclusive and value=2000-05-31) and
    document value=1999-05-31
    """
    assert_bindings(
        schema="msData/datatypes/Facets/date/date_minExclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/date/date_minExclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_date_min_exclusive003_1187_date_min_exclusive003_1187_v():
    """
    TEST :Facet Schemas for string : facet=minExclusive and
    value=1999-01-31 and document value=1999-05-31
    """
    assert_bindings(
        schema="msData/datatypes/Facets/date/date_minExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/date/date_minExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_date_min_exclusive002_1186_date_min_exclusive002_1186_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and
    value=1999-05-31 and document value=1999-01-31
    """
    assert_bindings(
        schema="msData/datatypes/Facets/date/date_minExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/date/date_minExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_date_min_exclusive001_1185_date_min_exclusive001_1185_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and
    value=1999-01-31 and document value=1999-01-31
    """
    assert_bindings(
        schema="msData/datatypes/Facets/date/date_minExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/date/date_minExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_date_min_inclusive005_1184_date_min_inclusive005_1184_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and
    value=1999-01-31 and facet=maxExclusive and value=2000-05-31) and
    document value=1999-05-31
    """
    assert_bindings(
        schema="msData/datatypes/Facets/date/date_minInclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/date/date_minInclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_date_min_inclusive004_1183_date_min_inclusive004_1183_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and
    value=1999-01-31 and facet=maxInclusive and value=2000-05-31) and
    document value=1999-05-31
    """
    assert_bindings(
        schema="msData/datatypes/Facets/date/date_minInclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/date/date_minInclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_date_min_inclusive003_1182_date_min_inclusive003_1182_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and
    value=1999-01-31 and document value=1999-05-31
    """
    assert_bindings(
        schema="msData/datatypes/Facets/date/date_minInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/date/date_minInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_date_min_inclusive002_1181_date_min_inclusive002_1181_i():
    """
    TEST :Facet Schemas for string : facet=minInclusive and
    value=1999-05-31 and document value=1999-01-31
    """
    assert_bindings(
        schema="msData/datatypes/Facets/date/date_minInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/date/date_minInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_date_min_inclusive001_1180_date_min_inclusive001_1180_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and
    value=1999-01-31 and document value=1999-01-31
    """
    assert_bindings(
        schema="msData/datatypes/Facets/date/date_minInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/date/date_minInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_date_max_exclusive003_1179_date_max_exclusive003_1179_v():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and
    value=2000-05-31 and document value=1999-05-31
    """
    assert_bindings(
        schema="msData/datatypes/Facets/date/date_maxExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/date/date_maxExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_date_max_exclusive002_1178_date_max_exclusive002_1178_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and
    value=1999-01-31 and document value=1999-05-31
    """
    assert_bindings(
        schema="msData/datatypes/Facets/date/date_maxExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/date/date_maxExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_date_max_exclusive001_1177_date_max_exclusive001_1177_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and
    value=1999-01-31 and document value=1999-01-31
    """
    assert_bindings(
        schema="msData/datatypes/Facets/date/date_maxExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/date/date_maxExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_date_max_inclusive003_1176_date_max_inclusive003_1176_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and
    value=2000-05-31 and document value=1999-05-31
    """
    assert_bindings(
        schema="msData/datatypes/Facets/date/date_maxInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/date/date_maxInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_date_max_inclusive002_1175_date_max_inclusive002_1175_i():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and
    value=1999-01-31 and document value=1999-05-31
    """
    assert_bindings(
        schema="msData/datatypes/Facets/date/date_maxInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/date/date_maxInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_date_max_inclusive001_1174_date_max_inclusive001_1174_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and
    value=1999-01-31 and document value=1999-01-31
    """
    assert_bindings(
        schema="msData/datatypes/Facets/date/date_maxInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/date/date_maxInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_date_enumeration004_1173_date_enumeration004_1173_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and
    value=1999-05-31 1999-07-31 2000-03-10 and document value=1999-05-31
    """
    assert_bindings(
        schema="msData/datatypes/Facets/date/date_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/date/date_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_date_enumeration003_1172_date_enumeration003_1172_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and
    value=1999-05-31 1999-07-31 2000-03-10 and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/date/date_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/date/date_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_date_enumeration002_1171_date_enumeration002_1171_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and
    value=1999-05-31 and document value=1999-05-31
    """
    assert_bindings(
        schema="msData/datatypes/Facets/date/date_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/date/date_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_date_enumeration001_1170_date_enumeration001_1170_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and
    value=1999-05-31 and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/date/date_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/date/date_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_date_pattern001_1169_date_pattern001_1169_v():
    """
    TEST :Facet Schemas for string : facet=pattern and
    value=[0-9]{4}-[0-9]{2}-[0-9]{2} and document value=1999-05-31
    """
    assert_bindings(
        schema="msData/datatypes/Facets/date/date_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/date/date_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_time_min_exclusive005_1168_time_min_exclusive005_1168_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and
    value=10:21:00-05:00 and facet=maxExclusive and value=13:20:00-04:00)
    and document value=13:20:00-03:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/time/time_minExclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/time/time_minExclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_time_min_exclusive004_1167_time_min_exclusive004_1167_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and
    value=10:21:00-05:00 and facet=maxInclusive and value=13:20:00-04:00)
    and document value=13:20:00-03:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/time/time_minExclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/time/time_minExclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_time_min_exclusive003_1166_time_min_exclusive003_1166_v():
    """
    TEST :Facet Schemas for string : facet=minExclusive and
    value=10:21:00-05:00 and document value=13:20:00-05:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/time/time_minExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/time/time_minExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_time_min_exclusive002_1165_time_min_exclusive002_1165_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and
    value=13:20:00-05:00 and document value=10:21:00-05:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/time/time_minExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/time/time_minExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_time_min_exclusive001_1164_time_min_exclusive001_1164_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and
    value=10:21:00-05:00 and document value=10:21:00-05:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/time/time_minExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/time/time_minExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_time_min_inclusive006_1163_time_min_inclusive006_1163_i():
    """
    TEST :Facet Schemas for string : facet=minInclusive and
    value=10:21:00-05:00 and facet=maxInclusive and value=13:20:00-04:00)
    and document value=13:20:00-03:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/time/time_minInclusive006.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/time/time_minInclusive006.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_time_min_inclusive005_1162_time_min_inclusive005_1162_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and
    value=10:21:00-05:00 and facet=maxExclusive and value=13:20:00-04:00)
    and document value=13:20:00-03:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/time/time_minInclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/time/time_minInclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_time_min_inclusive004_1161_time_min_inclusive004_1161_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and
    value=10:21:00-05:00 and facet=maxInclusive and value=13:20:00-04:00)
    and document value=13:20:00-03:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/time/time_minInclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/time/time_minInclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_time_min_inclusive003_1160_time_min_inclusive003_1160_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and
    value=10:21:00-05:00 and document value=13:20:00-05:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/time/time_minInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/time/time_minInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_time_min_inclusive002_1159_time_min_inclusive002_1159_i():
    """
    TEST :Facet Schemas for string : facet=minInclusive and
    value=13:20:00-05:00 and document value=10:21:00-05:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/time/time_minInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/time/time_minInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_time_min_inclusive001_1158_time_min_inclusive001_1158_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and
    value=10:21:00-05:00 and document value=10:21:00-05:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/time/time_minInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/time/time_minInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_time_max_exclusive003_1157_time_max_exclusive003_1157_v():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and
    value=13:20:00-04:00 and document value=13:20:00-03:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/time/time_maxExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/time/time_maxExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_time_max_exclusive002_1156_time_max_exclusive002_1156_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and
    value=10:21:00-05:00 and document value=13:20:00-05:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/time/time_maxExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/time/time_maxExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_time_max_exclusive001_1155_time_max_exclusive001_1155_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and
    value=10:21:00-05:00 and document value=10:21:00-05:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/time/time_maxExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/time/time_maxExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_time_max_inclusive003_1154_time_max_inclusive003_1154_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and
    value=13:20:00-04:00 and document value=13:20:00-03:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/time/time_maxInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/time/time_maxInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_time_max_inclusive002_1153_time_max_inclusive002_1153_i():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and
    value=10:21:00-05:00 and document value=13:20:00-05:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/time/time_maxInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/time/time_maxInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_time_max_inclusive001_1152_time_max_inclusive001_1152_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and
    value=10:21:00-05:00 and document value=10:21:00-05:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/time/time_maxInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/time/time_maxInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_time_enumeration004_1151_time_enumeration004_1151_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and
    value=13:20:00-05:00 13:20:00 01:50:40 and document
    value=13:20:00-05:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/time/time_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/time/time_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_time_enumeration003_1150_time_enumeration003_1150_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and
    value=13:20:00-05:00 13:20:00 01:50:40 and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/time/time_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/time/time_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_time_enumeration002_1149_time_enumeration002_1149_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and
    value=13:20:00-05:00 and document value=13:20:00-05:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/time/time_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/time/time_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_time_enumeration001_1148_time_enumeration001_1148_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and
    value=13:20:00-05:00 and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/time/time_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/time/time_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_time_pattern001_1147_time_pattern001_1147_v():
    """
    TEST :Facet Schemas for string : facet=pattern and
    value=[0-9]{1,2}:[0-9]{2}:[0-9]{2}-[0-9]{2}:[0-9]{2} and document
    value=13:20:00-05:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/time/time_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/time/time_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_date_time_min_exclusive005_1146_date_time_min_exclusive005_1146_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and
    value=1981-03-12T10:30:00 and facet=maxExclusive and
    value=1999-05-12T10:31:00) and document value=1985-04-12T10:30:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/dateTime/dateTime_minExclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/dateTime/dateTime_minExclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_date_time_min_exclusive004_1145_date_time_min_exclusive004_1145_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and
    value=1981-03-12T10:30:00 and facet=maxInclusive and
    value=1999-05-12T10:31:00) and document value=1985-04-12T10:30:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/dateTime/dateTime_minExclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/dateTime/dateTime_minExclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_date_time_min_exclusive003_1144_date_time_min_exclusive003_1144_v():
    """
    TEST :Facet Schemas for string : facet=minExclusive and
    value=1981-03-12T10:30:00 and document value=1985-04-12T10:30:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/dateTime/dateTime_minExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/dateTime/dateTime_minExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_date_time_min_exclusive002_1143_date_time_min_exclusive002_1143_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and
    value=1985-04-12T10:30:00 and document value=1981-03-12T10:30:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/dateTime/dateTime_minExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/dateTime/dateTime_minExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_date_time_min_exclusive001_1142_date_time_min_exclusive001_1142_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and
    value=1981-03-12T10:30:00 and document value=1981-03-12T10:30:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/dateTime/dateTime_minExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/dateTime/dateTime_minExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_date_time_min_inclusive005_1141_date_time_min_inclusive005_1141_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and
    value=1981-03-12T10:30:00 and facet=maxExclusive and
    value=1999-05-12T10:31:00) and document value=1985-04-12T10:30:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/dateTime/dateTime_minInclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/dateTime/dateTime_minInclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_date_time_min_inclusive004_1140_date_time_min_inclusive004_1140_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and
    value=1981-03-12T10:30:00 and facet=maxInclusive and
    value=1999-05-12T10:31:00) and document value=1985-04-12T10:30:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/dateTime/dateTime_minInclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/dateTime/dateTime_minInclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_date_time_min_inclusive003_1139_date_time_min_inclusive003_1139_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and
    value=1981-03-12T10:30:00 and document value=1985-04-12T10:30:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/dateTime/dateTime_minInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/dateTime/dateTime_minInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_date_time_min_inclusive002_1138_date_time_min_inclusive002_1138_i():
    """
    TEST :Facet Schemas for string : facet=minInclusive and
    value=1985-04-12T10:30:00 and document value=1981-03-12T10:30:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/dateTime/dateTime_minInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/dateTime/dateTime_minInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_date_time_min_inclusive001_1137_date_time_min_inclusive001_1137_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and
    value=1981-03-12T10:30:00 and document value=1981-03-12T10:30:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/dateTime/dateTime_minInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/dateTime/dateTime_minInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_date_time_max_exclusive003_1136_date_time_max_exclusive003_1136_v():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and
    value=1999-05-12T10:31:00 and document value=1985-04-12T10:30:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/dateTime/dateTime_maxExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/dateTime/dateTime_maxExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_date_time_max_exclusive002_1135_date_time_max_exclusive002_1135_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and
    value=1981-03-12T10:30:00 and document value=1985-04-12T10:30:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/dateTime/dateTime_maxExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/dateTime/dateTime_maxExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_date_time_max_exclusive001_1134_date_time_max_exclusive001_1134_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and
    value=1981-03-12T10:30:00 and document value=1981-03-12T10:30:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/dateTime/dateTime_maxExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/dateTime/dateTime_maxExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_date_time_max_inclusive003_1133_date_time_max_inclusive003_1133_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and
    value=1999-05-12T10:31:00 and document value=1985-04-12T10:30:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/dateTime/dateTime_maxInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/dateTime/dateTime_maxInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_date_time_max_inclusive002_1132_date_time_max_inclusive002_1132_i():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and
    value=1981-03-12T10:30:00 and document value=1985-04-12T10:30:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/dateTime/dateTime_maxInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/dateTime/dateTime_maxInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_date_time_max_inclusive001_1131_date_time_max_inclusive001_1131_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and
    value=1981-03-12T10:30:00 and document value=1981-03-12T10:30:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/dateTime/dateTime_maxInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/dateTime/dateTime_maxInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_date_time_enumeration005b_1130_date_time_enumeration005b_1130_v():
    """
    TEST :Facet Schemas for string : XSD: XsdDateTime comparison of
    identical representations of the time zones(b)
    """
    assert_bindings(
        schema="msData/datatypes/Facets/dateTime/dateTime_enumeration005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/dateTime/dateTime_enumeration005b.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_date_time_enumeration005a_1129_date_time_enumeration005a_1129_v():
    """
    TEST :Facet Schemas for string : XSD: XsdDateTime comparison of
    identical representations of the time zones(a)
    """
    assert_bindings(
        schema="msData/datatypes/Facets/dateTime/dateTime_enumeration005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/dateTime/dateTime_enumeration005a.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_date_time_enumeration004_1128_date_time_enumeration004_1128_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and
    value=1985-04-12T10:30:00 1985-04-12T12:00:00 1999-07-31T01:00:00 and
    document value=1985-04-12T10:30:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/dateTime/dateTime_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/dateTime/dateTime_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_date_time_enumeration003_1127_date_time_enumeration003_1127_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and
    value=1985-04-12T10:30:00 1985-04-12T12:00:00 1999-07-31T01:00:00 and
    document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/dateTime/dateTime_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/dateTime/dateTime_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_date_time_enumeration002_1126_date_time_enumeration002_1126_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and
    value=1985-04-12T10:30:00 and document value=1985-04-12T10:30:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/dateTime/dateTime_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/dateTime/dateTime_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_date_time_enumeration001_1125_date_time_enumeration001_1125_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and
    value=1985-04-12T10:30:00 and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/dateTime/dateTime_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/dateTime/dateTime_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_date_time_pattern001_1124_date_time_pattern001_1124_v():
    """
    TEST :Facet Schemas for string : facet=pattern and
    value=[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{1,2}:[0-9]{2}:[0-9]{2} and
    document value=1985-04-12T10:30:00
    """
    assert_bindings(
        schema="msData/datatypes/Facets/dateTime/dateTime_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/dateTime/dateTime_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_duration_min_exclusive005_1123_duration_min_exclusive005_1123_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and
    value=P1Y1MT1H and facet=maxExclusive and value=P2Y3MT2H) and document
    value=P1Y2MT2H
    """
    assert_bindings(
        schema="msData/datatypes/Facets/duration/duration_minExclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/duration/duration_minExclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_duration_min_exclusive004_1122_duration_min_exclusive004_1122_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and
    value=P1Y1MT1H and facet=maxInclusive and value=P2Y3MT2H) and document
    value=P1Y2MT2H
    """
    assert_bindings(
        schema="msData/datatypes/Facets/duration/duration_minExclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/duration/duration_minExclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_duration_min_exclusive003_1121_duration_min_exclusive003_1121_v():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=P1Y1MT1H
    and document value=P1Y2MT2H
    """
    assert_bindings(
        schema="msData/datatypes/Facets/duration/duration_minExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/duration/duration_minExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_duration_min_exclusive002_1120_duration_min_exclusive002_1120_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=P1Y2MT2H
    and document value=P1Y1MT1H
    """
    assert_bindings(
        schema="msData/datatypes/Facets/duration/duration_minExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/duration/duration_minExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_duration_min_exclusive001_1119_duration_min_exclusive001_1119_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=P1Y1MT1H
    and document value=P1Y1MT1H
    """
    assert_bindings(
        schema="msData/datatypes/Facets/duration/duration_minExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/duration/duration_minExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_duration_min_inclusive005_1118_duration_min_inclusive005_1118_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and
    value=P1Y1MT1H and facet=maxExclusive and value=P2Y3MT2H) and document
    value=P1Y2MT2H
    """
    assert_bindings(
        schema="msData/datatypes/Facets/duration/duration_minInclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/duration/duration_minInclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_duration_min_inclusive004_1117_duration_min_inclusive004_1117_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and
    value=P1Y1MT1H and facet=maxInclusive and value=P2Y3MT2H) and document
    value=P1Y2MT2H
    """
    assert_bindings(
        schema="msData/datatypes/Facets/duration/duration_minInclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/duration/duration_minInclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_duration_min_inclusive003_1116_duration_min_inclusive003_1116_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=P1Y1MT1H
    and document value=P1Y2MT2H
    """
    assert_bindings(
        schema="msData/datatypes/Facets/duration/duration_minInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/duration/duration_minInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_duration_min_inclusive002_1115_duration_min_inclusive002_1115_i():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=P1Y2MT2H
    and document value=P1Y1MT1H
    """
    assert_bindings(
        schema="msData/datatypes/Facets/duration/duration_minInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/duration/duration_minInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_duration_min_inclusive001_1114_duration_min_inclusive001_1114_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=P1Y1MT1H
    and document value=P1Y1MT1H
    """
    assert_bindings(
        schema="msData/datatypes/Facets/duration/duration_minInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/duration/duration_minInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_duration_max_exclusive003_1113_duration_max_exclusive003_1113_v():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=P2Y3MT2H
    and document value=P1Y2MT2H
    """
    assert_bindings(
        schema="msData/datatypes/Facets/duration/duration_maxExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/duration/duration_maxExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_duration_max_exclusive002_1112_duration_max_exclusive002_1112_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=P1Y1MT1H
    and document value=P1Y2MT2H
    """
    assert_bindings(
        schema="msData/datatypes/Facets/duration/duration_maxExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/duration/duration_maxExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_duration_max_exclusive001_1111_duration_max_exclusive001_1111_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=P1Y1MT1H
    and document value=P1Y1MT1H
    """
    assert_bindings(
        schema="msData/datatypes/Facets/duration/duration_maxExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/duration/duration_maxExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_duration_max_inclusive003_1110_duration_max_inclusive003_1110_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=P2Y3MT2H
    and document value=P1Y2MT2H
    """
    assert_bindings(
        schema="msData/datatypes/Facets/duration/duration_maxInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/duration/duration_maxInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_duration_max_inclusive002_1109_duration_max_inclusive002_1109_i():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=P1Y1MT1H
    and document value=P1Y2MT2H
    """
    assert_bindings(
        schema="msData/datatypes/Facets/duration/duration_maxInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/duration/duration_maxInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_duration_max_inclusive001_1108_duration_max_inclusive001_1108_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=P1Y1MT1H
    and document value=P1Y1MT1H
    """
    assert_bindings(
        schema="msData/datatypes/Facets/duration/duration_maxInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/duration/duration_maxInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_duration_enumeration004_1107_duration_enumeration004_1107_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=P1347Y
    P1347M P1Y2MT2H and document value=P1347Y
    """
    assert_bindings(
        schema="msData/datatypes/Facets/duration/duration_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/duration/duration_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_duration_enumeration003_1106_duration_enumeration003_1106_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=P1347Y
    P1347M P1Y2MT2H and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/duration/duration_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/duration/duration_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_duration_enumeration002_1105_duration_enumeration002_1105_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=P1347Y
    and document value=P1347Y
    """
    assert_bindings(
        schema="msData/datatypes/Facets/duration/duration_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/duration/duration_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_duration_enumeration001_1104_duration_enumeration001_1104_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=P1347Y
    and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/duration/duration_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/duration/duration_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_duration_pattern001_1103_duration_pattern001_1103_v():
    r"""
    TEST :Facet Schemas for string : facet=pattern and
    value=P\p{Nd}{1,4}Y\p{Nd}{1,2}MT\p{Nd}{1,2}H and document
    value=P1Y2MT2H
    """
    assert_bindings(
        schema="msData/datatypes/Facets/duration/duration_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/duration/duration_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_double_min_exclusive005_1102_double_min_exclusive005_1102_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1.1 and
    facet=maxExclusive and value=7.7) and document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/double/double_minExclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/double/double_minExclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_double_min_exclusive004_1101_double_min_exclusive004_1101_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1.1 and
    facet=maxInclusive and value=7.7) and document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/double/double_minExclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/double/double_minExclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_double_min_exclusive003_1100_double_min_exclusive003_1100_v():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1.1 and
    document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/double/double_minExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/double/double_minExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_double_min_exclusive002_1099_double_min_exclusive002_1099_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=5.55 and
    document value=1.1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/double/double_minExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/double/double_minExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_double_min_exclusive001_1098_double_min_exclusive001_1098_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1.1 and
    document value=1.1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/double/double_minExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/double/double_minExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_double_min_inclusive005_1097_double_min_inclusive005_1097_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1.1 and
    facet=maxExclusive and value=7.7) and document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/double/double_minInclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/double/double_minInclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_double_min_inclusive004_1096_double_min_inclusive004_1096_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1.1 and
    facet=maxInclusive and value=7.7) and document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/double/double_minInclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/double/double_minInclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_double_min_inclusive003_1095_double_min_inclusive003_1095_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1.1 and
    document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/double/double_minInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/double/double_minInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_double_min_inclusive002_1094_double_min_inclusive002_1094_i():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=5.55 and
    document value=1.1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/double/double_minInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/double/double_minInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_double_min_inclusive001_1093_double_min_inclusive001_1093_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1.1 and
    document value=1.1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/double/double_minInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/double/double_minInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_double_max_exclusive003_1092_double_max_exclusive003_1092_v():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=7.7 and
    document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/double/double_maxExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/double/double_maxExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_double_max_exclusive002_1091_double_max_exclusive002_1091_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=1.1 and
    document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/double/double_maxExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/double/double_maxExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_double_max_exclusive001_1090_double_max_exclusive001_1090_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=1.1 and
    document value=1.1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/double/double_maxExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/double/double_maxExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_double_max_inclusive003_1089_double_max_inclusive003_1089_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=7.7 and
    document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/double/double_maxInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/double/double_maxInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_double_max_inclusive002_1088_double_max_inclusive002_1088_i():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1.1 and
    document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/double/double_maxInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/double/double_maxInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_double_max_inclusive001_1087_double_max_inclusive001_1087_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1.1 and
    document value=1.1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/double/double_maxInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/double/double_maxInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_double_enumeration004_1086_double_enumeration004_1086_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=1.1 3.14
    2.718 and document value=1.1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/double/double_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/double/double_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_double_enumeration003_1085_double_enumeration003_1085_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=1.1 3.14
    2.718 and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/double/double_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/double/double_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_double_enumeration002_1084_double_enumeration002_1084_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=1.1 and
    document value=1.1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/double/double_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/double/double_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_double_enumeration001_1083_double_enumeration001_1083_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=1.1 and
    document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/double/double_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/double/double_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_double_pattern001_1082_double_pattern001_1082_v():
    """
    TEST :Facet Schemas for string : facet=pattern and
    value=[0-9]{0,2}.[0-9]{0,2} and document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/double/double_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/double/double_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_float_min_exclusive005_1081_float_min_exclusive005_1081_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1.1 and
    facet=maxExclusive and value=7.7) and document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/float/float_minExclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/float/float_minExclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_float_min_exclusive004_1080_float_min_exclusive004_1080_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1.1 and
    facet=maxInclusive and value=7.7) and document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/float/float_minExclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/float/float_minExclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_float_min_exclusive003_1079_float_min_exclusive003_1079_v():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1.1 and
    document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/float/float_minExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/float/float_minExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_float_min_exclusive002_1078_float_min_exclusive002_1078_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=5.55 and
    document value=1.1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/float/float_minExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/float/float_minExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_float_min_exclusive001_1077_float_min_exclusive001_1077_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1.1 and
    document value=1.1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/float/float_minExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/float/float_minExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_float_min_inclusive005_1076_float_min_inclusive005_1076_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1.1 and
    facet=maxExclusive and value=7.7) and document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/float/float_minInclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/float/float_minInclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_float_min_inclusive004_1075_float_min_inclusive004_1075_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1.1 and
    facet=maxInclusive and value=7.7) and document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/float/float_minInclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/float/float_minInclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_float_min_inclusive003_1074_float_min_inclusive003_1074_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1.1 and
    document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/float/float_minInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/float/float_minInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_float_min_inclusive002_1073_float_min_inclusive002_1073_i():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=5.55 and
    document value=1.1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/float/float_minInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/float/float_minInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_float_min_inclusive001_1072_float_min_inclusive001_1072_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1.1 and
    document value=1.1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/float/float_minInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/float/float_minInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_float_max_exclusive003_1071_float_max_exclusive003_1071_v():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=7.7 and
    document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/float/float_maxExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/float/float_maxExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_float_max_exclusive002_1070_float_max_exclusive002_1070_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=1.1 and
    document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/float/float_maxExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/float/float_maxExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_float_max_exclusive001_1069_float_max_exclusive001_1069_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=1.1 and
    document value=1.1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/float/float_maxExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/float/float_maxExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_float_max_inclusive003_1068_float_max_inclusive003_1068_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=7.7 and
    document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/float/float_maxInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/float/float_maxInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_float_max_inclusive002_1067_float_max_inclusive002_1067_i():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1.1 and
    document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/float/float_maxInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/float/float_maxInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_float_max_inclusive001_1066_float_max_inclusive001_1066_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1.1 and
    document value=1.1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/float/float_maxInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/float/float_maxInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_float_enumeration004_1065_float_enumeration004_1065_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=1.1 3.14
    2.718 and document value=1.1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/float/float_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/float/float_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_float_enumeration003_1064_float_enumeration003_1064_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=1.1 3.14
    2.718 and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/float/float_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/float/float_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_float_enumeration002_1063_float_enumeration002_1063_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=1.1 and
    document value=1.1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/float/float_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/float/float_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_float_enumeration001_1062_float_enumeration001_1062_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=1.1 and
    document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/float/float_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/float/float_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_float_pattern001_1061_float_pattern001_1061_v():
    """
    TEST :Facet Schemas for string : facet=pattern and
    value=[0-9]{0,2}.[0-9]{0,2} and document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/float/float_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/float/float_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_decimal_total_digits004_1060_decimal_total_digits004_1060_v():
    """
    TEST :Facet Schemas for string : XSD: totalDigits calculartion for
    xs:decimal
    """
    assert_bindings(
        schema="msData/datatypes/Facets/decimal/decimal_totalDigits004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/decimal/decimal_totalDigits004.xml",
        instance_is_valid=True,
        class_name="T1",
        version="1.0",
    )


def test_decimal_total_digits003_1059_decimal_total_digits003_1059_v():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=4 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/decimal/decimal_totalDigits003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/decimal/decimal_totalDigits003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_decimal_total_digits002_1058_decimal_total_digits002_1058_v():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=3 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/decimal/decimal_totalDigits002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/decimal/decimal_totalDigits002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_decimal_total_digits001_1057_decimal_total_digits001_1057_i():
    """
    TEST :Facet Schemas for string : facet=totalDigits and value=2 and
    document value=123
    """
    assert_bindings(
        schema="msData/datatypes/Facets/decimal/decimal_totalDigits001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/decimal/decimal_totalDigits001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_decimal_min_exclusive005_1056_decimal_min_exclusive005_1056_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1.1 and
    facet=maxExclusive and value=7.7) and document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/decimal/decimal_minExclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/decimal/decimal_minExclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_decimal_min_exclusive004_1055_decimal_min_exclusive004_1055_v():
    """
    TEST :Facet Schemas for string : (facet=minExclusive and value=1.1 and
    facet=maxInclusive and value=7.7) and document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/decimal/decimal_minExclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/decimal/decimal_minExclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_decimal_min_exclusive003_1054_decimal_min_exclusive003_1054_v():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1.1 and
    document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/decimal/decimal_minExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/decimal/decimal_minExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_decimal_min_exclusive002_1053_decimal_min_exclusive002_1053_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=5.55 and
    document value=1.1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/decimal/decimal_minExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/decimal/decimal_minExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_decimal_min_exclusive001_1052_decimal_min_exclusive001_1052_i():
    """
    TEST :Facet Schemas for string : facet=minExclusive and value=1.1 and
    document value=1.1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/decimal/decimal_minExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/decimal/decimal_minExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_decimal_min_inclusive005_1051_decimal_min_inclusive005_1051_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1.1 and
    facet=maxExclusive and value=7.7) and document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/decimal/decimal_minInclusive005.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/decimal/decimal_minInclusive005.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_decimal_min_inclusive004_1050_decimal_min_inclusive004_1050_v():
    """
    TEST :Facet Schemas for string : (facet=minInclusive and value=1.1 and
    facet=maxInclusive and value=7.7) and document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/decimal/decimal_minInclusive004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/decimal/decimal_minInclusive004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_decimal_min_inclusive003_1049_decimal_min_inclusive003_1049_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1.1 and
    document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/decimal/decimal_minInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/decimal/decimal_minInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_decimal_min_inclusive002_1048_decimal_min_inclusive002_1048_i():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=5.55 and
    document value=1.1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/decimal/decimal_minInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/decimal/decimal_minInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_decimal_min_inclusive001_1047_decimal_min_inclusive001_1047_v():
    """
    TEST :Facet Schemas for string : facet=minInclusive and value=1.1 and
    document value=1.1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/decimal/decimal_minInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/decimal/decimal_minInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_decimal_max_exclusive003_1046_decimal_max_exclusive003_1046_v():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=7.7 and
    document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/decimal/decimal_maxExclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/decimal/decimal_maxExclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_decimal_max_exclusive002_1045_decimal_max_exclusive002_1045_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=1.1 and
    document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/decimal/decimal_maxExclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/decimal/decimal_maxExclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_decimal_max_exclusive001_1044_decimal_max_exclusive001_1044_i():
    """
    TEST :Facet Schemas for string : facet=maxExclusive and value=1.1 and
    document value=1.1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/decimal/decimal_maxExclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/decimal/decimal_maxExclusive001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_decimal_max_inclusive003_1043_decimal_max_inclusive003_1043_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=7.7 and
    document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/decimal/decimal_maxInclusive003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/decimal/decimal_maxInclusive003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_decimal_max_inclusive002_1042_decimal_max_inclusive002_1042_i():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1.1 and
    document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/decimal/decimal_maxInclusive002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/decimal/decimal_maxInclusive002.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_decimal_max_inclusive001_1041_decimal_max_inclusive001_1041_v():
    """
    TEST :Facet Schemas for string : facet=maxInclusive and value=1.1 and
    document value=1.1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/decimal/decimal_maxInclusive001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/decimal/decimal_maxInclusive001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_decimal_enumeration004_1040_decimal_enumeration004_1040_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=1.1 3.14
    2.718 and document value=1.1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/decimal/decimal_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/decimal/decimal_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_decimal_enumeration003_1039_decimal_enumeration003_1039_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=1.1 3.14
    2.718 and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/decimal/decimal_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/decimal/decimal_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_decimal_enumeration002_1038_decimal_enumeration002_1038_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=1.1 and
    document value=1.1
    """
    assert_bindings(
        schema="msData/datatypes/Facets/decimal/decimal_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/decimal/decimal_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_decimal_enumeration001_1037_decimal_enumeration001_1037_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=1.1 and
    document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/decimal/decimal_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/decimal/decimal_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_decimal_pattern001_1036_decimal_pattern001_1036_v():
    """
    TEST :Facet Schemas for string : facet=pattern and
    value=[0-9]{0,2}.[0-9]{0,2} and document value=5.55
    """
    assert_bindings(
        schema="msData/datatypes/Facets/decimal/decimal_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/decimal/decimal_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_string_enumeration004_1035_string_enumeration004_1035_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo 123
    foo123 and document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/string/string_enumeration004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/string/string_enumeration004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_string_enumeration003_1034_string_enumeration003_1034_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo 123
    foo123 and document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/string/string_enumeration003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/string/string_enumeration003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_string_enumeration002_1033_string_enumeration002_1033_v():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=foo
    """
    assert_bindings(
        schema="msData/datatypes/Facets/string/string_enumeration002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/string/string_enumeration002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_string_enumeration001_1032_string_enumeration001_1032_i():
    """
    TEST :Facet Schemas for string : facet=enumeration and value=foo and
    document value=
    """
    assert_bindings(
        schema="msData/datatypes/Facets/string/string_enumeration001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/string/string_enumeration001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_string_pattern002_1031_string_pattern002_1031_i():
    """
    TEST :Facet Schemas for string : facet=pattern and value=[a-z]{3} and
    document value=abc
    """
    assert_bindings(
        schema="msData/datatypes/Facets/string/string_pattern002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/string/string_pattern002.xml",
        instance_is_valid=False,
        class_name="Xml",
        version="1.0",
    )


def test_string_pattern001_1030_string_pattern001_1030_v():
    """
    TEST :Facet Schemas for string : facet=pattern and value=[a-z]{3} and
    document value=abc
    """
    assert_bindings(
        schema="msData/datatypes/Facets/string/string_pattern001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/string/string_pattern001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_string_max_length003_1029_string_max_length003_1029_v():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=6 and
    document value=abcde
    """
    assert_bindings(
        schema="msData/datatypes/Facets/string/string_maxLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/string/string_maxLength003.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_string_max_length002_1028_string_max_length002_1028_v():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=5 and
    document value=abcde
    """
    assert_bindings(
        schema="msData/datatypes/Facets/string/string_maxLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/string/string_maxLength002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_string_max_length001_1027_string_max_length001_1027_i():
    """
    TEST :Facet Schemas for string : facet=maxLength and value=4 and
    document value=abcde
    """
    assert_bindings(
        schema="msData/datatypes/Facets/string/string_maxLength001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/string/string_maxLength001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_string_min_length004_1026_string_min_length004_1026_v():
    """
    TEST :Facet Schemas for string : (facet=minLength and value=4 and
    facet=maxLength and value=6) and document value=abcde
    """
    assert_bindings(
        schema="msData/datatypes/Facets/string/string_minLength004.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/string/string_minLength004.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_string_min_length003_1025_string_min_length003_1025_i():
    """
    TEST :Facet Schemas for string : facet=minLength and value=6 and
    document value=abcde
    """
    assert_bindings(
        schema="msData/datatypes/Facets/string/string_minLength003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/string/string_minLength003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_string_min_length002_1024_string_min_length002_1024_v():
    """
    TEST :Facet Schemas for string : facet=minLength and value=5 and
    document value=abcde
    """
    assert_bindings(
        schema="msData/datatypes/Facets/string/string_minLength002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/string/string_minLength002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_string_min_length001_1023_string_min_length001_1023_v():
    """
    TEST :Facet Schemas for string : facet=minLength and value=4 and
    document value=abcde
    """
    assert_bindings(
        schema="msData/datatypes/Facets/string/string_minLength001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/string/string_minLength001.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_string_length003_1022_string_length003_1022_i():
    """
    TEST :Facet Schemas for string : facet=length and value=6 and document
    value=abcde
    """
    assert_bindings(
        schema="msData/datatypes/Facets/string/string_length003.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/string/string_length003.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_string_length002_1021_string_length002_1021_v():
    """
    TEST :Facet Schemas for string : facet=length and value=5 and document
    value=abcde
    """
    assert_bindings(
        schema="msData/datatypes/Facets/string/string_length002.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/string/string_length002.xml",
        instance_is_valid=True,
        class_name="Test",
        version="1.0",
    )


def test_string_length001_1020_string_length001_1020_i():
    """
    TEST :Facet Schemas for string : facet=length and value=4 and document
    value=abcde
    """
    assert_bindings(
        schema="msData/datatypes/Facets/string/string_length001.xsd",
        is_valid=True,
        instance="msData/datatypes/Facets/string/string_length001.xml",
        instance_is_valid=False,
        class_name="Test",
        version="1.0",
    )


def test_elem_z033b_elem_z033b_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : XSD: test laxly validate an element with no element
    declaration having xsi:nill(2)
    """
    assert_bindings(
        schema="",
        is_valid=False,
        instance="msData/element/elemZ033b.xml",
        instance_is_valid=True,
        class_name="Foo",
        version="1.0",
    )


def test_elem_z029_elem_z029_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : XSD: an element can have a default value constraints and
    xsi:nil=true
    """
    assert_bindings(
        schema="msData/element/elemZ029.xsd",
        is_valid=True,
        instance="msData/element/elemZ029.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


@pytest.mark.xfail
def test_qfe1700g2_qfe1700g2_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : G2:XmlValidation for xsi:nil="false" even though
    processContents="skip"
    """
    assert_bindings(
        schema="msData/element/QFE1700g.xsd",
        is_valid=True,
        instance="msData/element/QFE1700g2.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_qfe1700g1_qfe1700g1_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : G1:XmlValidation for xsi:nil="false" even though
    processContents="skip"
    """
    assert_bindings(
        schema="msData/element/QFE1700g.xsd",
        is_valid=True,
        instance="msData/element/QFE1700g1.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_qfe1700f3_qfe1700f3_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : F3:XmlValidation for xsi:nil="false" even though
    processContents="skip"
    """
    assert_bindings(
        schema="msData/element/QFE1700f.xsd",
        is_valid=True,
        instance="msData/element/QFE1700f3.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_qfe1700f2_qfe1700f2_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : F2:XmlValidation for xsi:nil="false" even though
    processContents="skip"
    """
    assert_bindings(
        schema="msData/element/QFE1700f.xsd",
        is_valid=True,
        instance="msData/element/QFE1700f2.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_qfe1700f1_qfe1700f1_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : F1:XmlValidation for xsi:nil="false" even though
    processContents="skip"
    """
    assert_bindings(
        schema="msData/element/QFE1700f.xsd",
        is_valid=True,
        instance="msData/element/QFE1700f1.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_qfe1700e3_qfe1700e3_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : E3:XmlValidation for xsi:nil="false" even though
    processContents="skip"
    """
    assert_bindings(
        schema="msData/element/QFE1700e.xsd",
        is_valid=True,
        instance="msData/element/QFE1700e3.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_qfe1700e2_qfe1700e2_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : E2:XmlValidation for xsi:nil="false" even though
    processContents="skip"
    """
    assert_bindings(
        schema="msData/element/QFE1700e.xsd",
        is_valid=True,
        instance="msData/element/QFE1700e2.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_qfe1700e1_qfe1700e1_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : E1:XmlValidation for xsi:nil="false" even though
    processContents="skip"
    """
    assert_bindings(
        schema="msData/element/QFE1700e.xsd",
        is_valid=True,
        instance="msData/element/QFE1700e1.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_qfe1700d1_qfe1700d1_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : D1:XmlValidation for xsi:nil="false" even though
    processContents="skip"
    """
    assert_bindings(
        schema="msData/element/QFE1700d.xsd",
        is_valid=True,
        instance="msData/element/QFE1700d1.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_qfe1700c2_qfe1700c2_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : C2:XmlValidation for xsi:nil="false" even though
    processContents="skip"
    """
    assert_bindings(
        schema="msData/element/QFE1700c.xsd",
        is_valid=True,
        instance="msData/element/QFE1700c2.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_qfe1700c1_qfe1700c1_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : C1:XmlValidation for xsi:nil="false" even though
    processContents="skip"
    """
    assert_bindings(
        schema="msData/element/QFE1700c.xsd",
        is_valid=True,
        instance="msData/element/QFE1700c1.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_qfe1700b2_qfe1700b2_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : B2:XmlValidation for xsi:nil="false" even though
    processContents="skip"
    """
    assert_bindings(
        schema="msData/element/QFE1700b.xsd",
        is_valid=True,
        instance="msData/element/QFE1700b2.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_qfe1700b1_qfe1700b1_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : B1:XmlValidation for xsi:nil="false" even though
    processContents="skip"
    """
    assert_bindings(
        schema="msData/element/QFE1700b.xsd",
        is_valid=True,
        instance="msData/element/QFE1700b1.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_qfe1700a3_qfe1700a3_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : A3:XmlValidation for xsi:nil="false" even though
    processContents="skip"
    """
    assert_bindings(
        schema="msData/element/QFE1700a.xsd",
        is_valid=True,
        instance="msData/element/QFE1700a3.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_qfe1700a2_qfe1700a2_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : A2:XmlValidation for xsi:nil="false" even though
    processContents="skip"
    """
    assert_bindings(
        schema="msData/element/QFE1700a.xsd",
        is_valid=True,
        instance="msData/element/QFE1700a2.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_qfe1700a1_qfe1700a1_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : A1:XmlValidation for xsi:nil="false" even though
    processContents="skip"
    """
    assert_bindings(
        schema="msData/element/QFE1700a.xsd",
        is_valid=True,
        instance="msData/element/QFE1700a1.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_z023_elem_z023_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : XSD: member of substitutionGroup and local particle with
    the same qualified name
    """
    assert_bindings(
        schema="msData/element/elemZ023.xsd",
        is_valid=True,
        instance="msData/element/elemZ023.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_z022b_elem_z022b_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : XSD: Wildcard prohibited element through a
    substitutionGroup(2)
    """
    assert_bindings(
        schema="msData/element/test115478_b.xsd",
        is_valid=True,
        instance="msData/element/test115478_b.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_z022a_elem_z022a_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : XSD: Wildcard prohibited element through a
    substitutionGroup
    """
    assert_bindings(
        schema="msData/element/test115478.xsd",
        is_valid=True,
        instance="msData/element/test115478.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_z021g_elem_z021g_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : XSD: member of substitutionGroup and local particle with
    the same qualified name (7)
    """
    assert_bindings(
        schema="msData/element/test115044_4.xsd",
        is_valid=True,
        instance="msData/element/test115044_c.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_z021f_elem_z021f_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : XSD: member of substitutionGroup and local particle with
    the same qualified name (6)
    """
    assert_bindings(
        schema="msData/element/test115044_3.xsd",
        is_valid=True,
        instance="msData/element/test115044_b.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_z021e_elem_z021e_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : XSD: member of substitutionGroup and local particle with
    the same qualified name (5)
    """
    assert_bindings(
        schema="msData/element/test115044_3.xsd",
        is_valid=True,
        instance="msData/element/test115044_a.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_elem_z021d_elem_z021d_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : XSD: member of substitutionGroup and local particle with
    the same qualified name (4)
    """
    assert_bindings(
        schema="msData/element/test115044_2.xsd",
        is_valid=True,
        instance="msData/element/test115044_b.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_z021c_elem_z021c_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : XSD: member of substitutionGroup and local particle with
    the same qualified name (3)
    """
    assert_bindings(
        schema="msData/element/test115044_2.xsd",
        is_valid=True,
        instance="msData/element/test115044_a.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_z021b_elem_z021b_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : XSD: member of substitutionGroup and local particle with
    the same qualified name (2)
    """
    assert_bindings(
        schema="msData/element/test115044_1.xsd",
        is_valid=True,
        instance="msData/element/test115044_b.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_z021a_elem_z021a_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : XSD: member of substitutionGroup and local particle with
    the same qualified name (1)
    """
    assert_bindings(
        schema="msData/element/test115044_1.xsd",
        is_valid=True,
        instance="msData/element/test115044_a.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_elem_z020_elem_z020_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : xsd: when substitutionGroup exists, we shold not change
    content model as if it is a choice
    """
    assert_bindings(
        schema="msData/element/elemZ020.xsd",
        is_valid=True,
        instance="msData/element/elemZ020.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_z019_elem_z019_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : XSD: Namespace URIs should not be canonicalized if they
    are GUIDs, XDR uses this GUID for datatype declarations
    """
    assert_bindings(
        schema="msData/element/elemZ019.xsd",
        is_valid=True,
        instance="msData/element/elemZ019.xml",
        instance_is_valid=True,
        class_name="Series",
        version="1.0",
    )


def test_elem_z018_elem_z018_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Schema with deep nested nodes (>14 nested levels)
    """
    assert_bindings(
        schema="msData/element/elemZ018.xsd",
        is_valid=True,
        instance="msData/element/elemZ018.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_z017_elem_z017_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : empty element with xsi:type of xs:string
    """
    assert_bindings(
        schema="",
        is_valid=False,
        instance="msData/element/elemZ017.xml",
        instance_is_valid=True,
        class_name="AccessPermission",
        version="1.0",
    )


@pytest.mark.xfail
def test_elem_z016_elem_z016_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : xsd: element with childNodes typed=ID, dupe ID should be
    invalid. Becomes valid in XSD 1.1 (two child elements of type xs:ID
    are permitted if the ID is the same)
    """
    assert_bindings(
        schema="msData/element/elemZ016.xsd",
        is_valid=True,
        instance="msData/element/elemZ016.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_z015_elem_z015_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : 86614 xsd: uniqueness idendity constraint when using
    xsi:type to change the type of an element.
    """
    assert_bindings(
        schema="msData/element/elemZ015.xsd",
        is_valid=True,
        instance="msData/element/elemZ015.xml",
        instance_is_valid=False,
        class_name="XTask",
        version="1.0",
    )


def test_elem_z014_elem_z014_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : xsi:type references and namespace alias for parent
    element
    """
    assert_bindings(
        schema="msData/element/elemZ014.xsd",
        is_valid=True,
        instance="msData/element/elemZ014.xml",
        instance_is_valid=True,
        class_name="RootElem",
        version="1.0",
    )


def test_elem_z010_elem_z010_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Components in A may be indirectly using components from
    C. Lets assume that a type declared in B derives from one in C (which
    is possible because B imports C). Document A can declare elements
    using that type because it includes B. Such use obviously involves
    information from the base type in C as will as the explicit reference
    in B.
    """
    assert_bindings(
        schema="msData/element/elemZ010.xsd",
        is_valid=True,
        instance="msData/element/elemZ010.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_z009_elem_z009_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Components in A may be indirectly using components from
    C. Lets assume that a type declared in B derives from one in C (which
    is possible because B imports C). Document A can declare elements
    using that type because it includes B. Such use obviously involves
    information from the base type in C as will as the explicit reference
    in B.
    """
    assert_bindings(
        schema="msData/element/elemZ009.xsd",
        is_valid=True,
        instance="msData/element/elemZ009.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_elem_z003_elem_z003_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : 72898 - subsitutionGroup with deep chains
    """
    assert_bindings(
        schema="msData/element/elemZ003.xsd",
        is_valid=True,
        instance="msData/element/elemZ003.xml",
        instance_is_valid=True,
        class_name="Container",
        version="1.0",
    )


def test_elem_z002_elem_z002_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : 67493 - xsd: xsi:type should allowed predefined types as
    valid value.
    """
    assert_bindings(
        schema="msData/element/elemZ002.xsd",
        is_valid=True,
        instance="msData/element/elemZ002.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_z001_elem_z001_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : 81682 - Element with xsi:nil value set to true and
    xsi:type value
    """
    assert_bindings(
        schema="msData/element/elemZ001.xsd",
        is_valid=True,
        instance="msData/element/elemZ001.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_u025_elem_u025_i():
    r"""
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : regular expression: restriction on string "chapter \d"
    """
    assert_bindings(
        schema="msData/element/elemU025.xsd",
        is_valid=True,
        instance="msData/element/elemU025.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_u024_elem_u024_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : regular expression: restriction on string "(ab){2}x"
    """
    assert_bindings(
        schema="msData/element/elemU024.xsd",
        is_valid=True,
        instance="msData/element/elemU024.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_u023_elem_u023_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : regular expression: restriction on string "ab{2,}x"
    """
    assert_bindings(
        schema="msData/element/elemU023.xsd",
        is_valid=True,
        instance="msData/element/elemU023.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_u022_elem_u022_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : regular expression: restriction on string "ab{2,4}x"
    """
    assert_bindings(
        schema="msData/element/elemU022.xsd",
        is_valid=True,
        instance="msData/element/elemU022.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_u021_elem_u021_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : regular expression: restriction on string "ab{2}x"
    """
    assert_bindings(
        schema="msData/element/elemU021.xsd",
        is_valid=True,
        instance="msData/element/elemU021.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_u020_elem_u020_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : regular expression: restriction on string ".*abc.*"
    """
    assert_bindings(
        schema="msData/element/elemU020.xsd",
        is_valid=True,
        instance="msData/element/elemU020.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_u019_elem_u019_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : regular expression: restriction on string ".x"
    """
    assert_bindings(
        schema="msData/element/elemU019.xsd",
        is_valid=True,
        instance="msData/element/elemU019.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_u018_elem_u018_v():
    r"""
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : regular expression: restriction on string "\Dx"
    """
    assert_bindings(
        schema="msData/element/elemU018.xsd",
        is_valid=True,
        instance="msData/element/elemU018.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_u017_elem_u017_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : regular expression: restriction on string "[^0-9]x"
    """
    assert_bindings(
        schema="msData/element/elemU017.xsd",
        is_valid=True,
        instance="msData/element/elemU017.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_u015_elem_u015_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : regular expression: restriction on string "[ae-]x"
    """
    assert_bindings(
        schema="msData/element/elemU015.xsd",
        is_valid=True,
        instance="msData/element/elemU015.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_u014_elem_u014_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : regular expression: restriction on string "[-ae]x"
    """
    assert_bindings(
        schema="msData/element/elemU014.xsd",
        is_valid=True,
        instance="msData/element/elemU014.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_u013_elem_u013_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : regular expression: restriction on string "[a-e]x"
    """
    assert_bindings(
        schema="msData/element/elemU013.xsd",
        is_valid=True,
        instance="msData/element/elemU013.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_u012_elem_u012_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : regular expression: restriction on string "[abcde]x"
    """
    assert_bindings(
        schema="msData/element/elemU012.xsd",
        is_valid=True,
        instance="msData/element/elemU012.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_u011_elem_u011_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : regular expression: restriction on string "(a|b)+x"
    """
    assert_bindings(
        schema="msData/element/elemU011.xsd",
        is_valid=True,
        instance="msData/element/elemU011.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_u010_elem_u010_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : regular expression: restriction on string "a+x"
    """
    assert_bindings(
        schema="msData/element/elemU010.xsd",
        is_valid=True,
        instance="msData/element/elemU010.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_u009_elem_u009_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : regular expression: restriction on string "a?x"
    """
    assert_bindings(
        schema="msData/element/elemU009.xsd",
        is_valid=True,
        instance="msData/element/elemU009.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_u008_elem_u008_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : regular expression: restriction on string "a*x"
    """
    assert_bindings(
        schema="msData/element/elemU008.xsd",
        is_valid=True,
        instance="msData/element/elemU008.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_u007_elem_u007_v():
    r"""
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : regular expression: restriction on string "\P{IsGreek}"
    """
    assert_bindings(
        schema="msData/element/elemU007.xsd",
        is_valid=True,
        instance="msData/element/elemU007.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_u006_elem_u006_v():
    r"""
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : regular expression: restriction on string "\p{IsGreek}"
    """
    assert_bindings(
        schema="msData/element/elemU006.xsd",
        is_valid=True,
        instance="msData/element/elemU006.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_u005_elem_u005_v():
    r"""
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : regular expression: restriction on string "\p{Lu}"
    """
    assert_bindings(
        schema="msData/element/elemU005.xsd",
        is_valid=True,
        instance="msData/element/elemU005.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_u004_elem_u004_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : regular expression: restriction on string
    "Espan&#xF1;ola"
    """
    assert_bindings(
        schema="msData/element/elemU004.xsd",
        is_valid=True,
        instance="msData/element/elemU004.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_u003_elem_u003_v():
    r"""
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : regular expression: restriction on string "\s\w"
    """
    assert_bindings(
        schema="msData/element/elemU003.xsd",
        is_valid=True,
        instance="msData/element/elemU003.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_u002_elem_u002_v():
    r"""
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : regular expression: restriction on string "\s\d"
    """
    assert_bindings(
        schema="msData/element/elemU002.xsd",
        is_valid=True,
        instance="msData/element/elemU002.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_u001_elem_u001_v():
    r"""
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : regular expression: restriction on string "\d"
    """
    assert_bindings(
        schema="msData/element/elemU001.xsd",
        is_valid=True,
        instance="msData/element/elemU001.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_t074_elem_t074_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=Union-AB, block=restriction, and instant
    XMLhas xsi:type=A type derived from a type in the Union
    """
    assert_bindings(
        schema="msData/element/elemT074.xsd",
        is_valid=True,
        instance="msData/element/elemT074.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t073_elem_t073_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=Union-AB, block=extension, and instant
    XMLhas xsi:type=A type derived from a type in the Union
    """
    assert_bindings(
        schema="msData/element/elemT073.xsd",
        is_valid=True,
        instance="msData/element/elemT073.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_t072_elem_t072_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=Union-AB, block=absent, and instant XMLhas
    xsi:type=A type derived from a type in the Union
    """
    assert_bindings(
        schema="msData/element/elemT072.xsd",
        is_valid=True,
        instance="msData/element/elemT072.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_t071_elem_t071_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=Union-A, block=absent, and instant XMLhas
    xsi:type=A type derived from a type in the Union
    """
    assert_bindings(
        schema="msData/element/elemT071.xsd",
        is_valid=True,
        instance="msData/element/elemT071.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_t070_elem_t070_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=A, block="substitution", and instant XMLhas
    xsi:type=a substitution group with ur-type
    """
    assert_bindings(
        schema="msData/element/elemT070.xsd",
        is_valid=True,
        instance="msData/element/elemT070.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t069_elem_t069_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=A, block="substitution", and instant XMLhas
    xsi:type=a substitution group with type=restriction of A
    """
    assert_bindings(
        schema="msData/element/elemT069.xsd",
        is_valid=True,
        instance="msData/element/elemT069.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t068_elem_t068_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=A, block="substitution", and instant XMLhas
    xsi:type=a substitution group with type=extension of A
    """
    assert_bindings(
        schema="msData/element/elemT068.xsd",
        is_valid=True,
        instance="msData/element/elemT068.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_elem_t067_elem_t067_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=A, block="extension", and instant XMLhas
    xsi:type=a substitution group with ur-type
    """
    assert_bindings(
        schema="msData/element/elemT067.xsd",
        is_valid=True,
        instance="msData/element/elemT067.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_elem_t066_elem_t066_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=A, block="extension", and instant XMLhas
    xsi:type=a substitution group with type=restriction of A
    """
    assert_bindings(
        schema="msData/element/elemT066.xsd",
        is_valid=True,
        instance="msData/element/elemT066.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_t065_elem_t065_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=A, block="extension", and instant XMLhas
    xsi:type=a substitution group with type=extension of A (this is valid
    because block is not substitution)
    """
    assert_bindings(
        schema="msData/element/elemT065.xsd",
        is_valid=True,
        instance="msData/element/elemT065.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_elem_t064_elem_t064_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=A, block="restriction", and instant XMLhas
    xsi:type=a substitution group with ur-type
    """
    assert_bindings(
        schema="msData/element/elemT064.xsd",
        is_valid=True,
        instance="msData/element/elemT064.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_t063_elem_t063_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=A, block="restriction", and instant XMLhas
    xsi:type=a substitution group with type=restriction of A (this is
    valid because block is not substitution)
    """
    assert_bindings(
        schema="msData/element/elemT063.xsd",
        is_valid=True,
        instance="msData/element/elemT063.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_elem_t062_elem_t062_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=A, block="restriction", and instant XMLhas
    xsi:type=a substitution group with type=extension of A
    """
    assert_bindings(
        schema="msData/element/elemT062.xsd",
        is_valid=True,
        instance="msData/element/elemT062.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_t061_elem_t061_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=A, block="#all", and instant XMLhas
    xsi:type=a substitution group with ur-type
    """
    assert_bindings(
        schema="msData/element/elemT061.xsd",
        is_valid=True,
        instance="msData/element/elemT061.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t060_elem_t060_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=A, block="#all", and instant XMLhas
    xsi:type=a substitution group with type=restriction of A
    """
    assert_bindings(
        schema="msData/element/elemT060.xsd",
        is_valid=True,
        instance="msData/element/elemT060.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t059_elem_t059_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=A, block="#all", and instant XMLhas
    xsi:type=a substitution group with type=extension of A
    """
    assert_bindings(
        schema="msData/element/elemT059.xsd",
        is_valid=True,
        instance="msData/element/elemT059.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_elem_t058_elem_t058_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : several elements with different blocks and valid instance
    """
    assert_bindings(
        schema="msData/element/elemT058.xsd",
        is_valid=True,
        instance="msData/element/elemT058.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_t057_elem_t057_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=ur-Type, block="#all", and instant XMLhas
    xsi:type=List of the Union of simpleType A and B TSTF observed that
    although the original bug report is mistaken, the instance is none-
    the-less invalid, because the controlling element declaration blocks
    derivation (from its implicit type AnyType) by restriction.
    """
    assert_bindings(
        schema="msData/element/elemT057.xsd",
        is_valid=True,
        instance="msData/element/elemT057.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t056_elem_t056_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=ur-Type, block="#all", and instant XMLhas
    xsi:type=List of simpleType A TSTF observed that although the original
    bug report is mistaken, the instance is none-the-less invalid, because
    the controlling element declaration blocks derivation (from its
    implicit type AnyType) by restriction.
    """
    assert_bindings(
        schema="msData/element/elemT056.xsd",
        is_valid=True,
        instance="msData/element/elemT056.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t055_elem_t055_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=ur-Type, block="#all", and instant XMLhas
    xsi:type=union of simpleType A and B TSTF observed that although the
    original bug report is mistaken, the instance is none-the-less
    invalid, because the controlling element declaration blocks derivation
    (from its implicit type AnyType) by restriction.
    """
    assert_bindings(
        schema="msData/element/elemT055.xsd",
        is_valid=True,
        instance="msData/element/elemT055.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t054_elem_t054_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=ur-Type, block="#all", and instant XMLhas
    xsi:type=union of simpleType A TSTF observed that although the
    original bug report is mistaken, the instance is none-the-less
    invalid, because the controlling element declaration blocks derivation
    (from its implicit type AnyType) by restriction.
    """
    assert_bindings(
        schema="msData/element/elemT054.xsd",
        is_valid=True,
        instance="msData/element/elemT054.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t053_elem_t053_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=complexType A, block="#all", and instant
    XMLhas xsi:type=extension of A
    """
    assert_bindings(
        schema="msData/element/elemT053.xsd",
        is_valid=True,
        instance="msData/element/elemT053.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t052_elem_t052_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=complexType A, block="#all", and instant
    XMLhas xsi:type=restriction of A
    """
    assert_bindings(
        schema="msData/element/elemT052.xsd",
        is_valid=True,
        instance="msData/element/elemT052.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t051_elem_t051_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=simpleType A, block="#all", and instant
    XMLhas xsi:type=list of the Union A and B
    """
    assert_bindings(
        schema="msData/element/elemT051.xsd",
        is_valid=True,
        instance="msData/element/elemT051.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t050_elem_t050_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=simpleType A, block="#all", and instant
    XMLhas xsi:type=list of A
    """
    assert_bindings(
        schema="msData/element/elemT050.xsd",
        is_valid=True,
        instance="msData/element/elemT050.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t049_elem_t049_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=simpleType A, block="#all", and instant
    XMLhas xsi:type=Union of A and B
    """
    assert_bindings(
        schema="msData/element/elemT049.xsd",
        is_valid=True,
        instance="msData/element/elemT049.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t048_elem_t048_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=simpleType A, block="#all", and instant
    XMLhas xsi:type=Union of A
    """
    assert_bindings(
        schema="msData/element/elemT048.xsd",
        is_valid=True,
        instance="msData/element/elemT048.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t047_elem_t047_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=simpleType A, block="#all", and instant
    XMLhas xsi:type=base of A
    """
    assert_bindings(
        schema="msData/element/elemT047.xsd",
        is_valid=True,
        instance="msData/element/elemT047.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t046_elem_t046_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=simpleType A, block="#all", and instant
    XMLhas xsi:type=restriction of A
    """
    assert_bindings(
        schema="msData/element/elemT046.xsd",
        is_valid=True,
        instance="msData/element/elemT046.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t045_elem_t045_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=simpleType A, block="#all", and instant
    XMLhas xsi:type=B (a different type)
    """
    assert_bindings(
        schema="msData/element/elemT045.xsd",
        is_valid=True,
        instance="msData/element/elemT045.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t044_elem_t044_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=simpleType A, block="#all", and instant
    XMLhas xsi:type=A
    """
    assert_bindings(
        schema="msData/element/elemT044.xsd",
        is_valid=True,
        instance="msData/element/elemT044.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_t043_elem_t043_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=ur-Type, block="extension", and instant
    XMLhas xsi:type=List of the Union of simpleType A and B
    """
    assert_bindings(
        schema="msData/element/elemT043.xsd",
        is_valid=True,
        instance="msData/element/elemT043.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_t042_elem_t042_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=ur-Type, block="extension", and instant
    XMLhas xsi:type=List of simpleType A
    """
    assert_bindings(
        schema="msData/element/elemT042.xsd",
        is_valid=True,
        instance="msData/element/elemT042.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_t041_elem_t041_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=ur-Type, block="extension", and instant
    XMLhas xsi:type=union of simpleType A and B
    """
    assert_bindings(
        schema="msData/element/elemT041.xsd",
        is_valid=True,
        instance="msData/element/elemT041.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_t040_elem_t040_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=ur-Type, block="extension", and instant
    XMLhas xsi:type=union of simpleType A
    """
    assert_bindings(
        schema="msData/element/elemT040.xsd",
        is_valid=True,
        instance="msData/element/elemT040.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_t039_elem_t039_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=complexType A, block="extension", and
    instant XMLhas xsi:type=extension of A
    """
    assert_bindings(
        schema="msData/element/elemT039.xsd",
        is_valid=True,
        instance="msData/element/elemT039.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t038_elem_t038_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=complexType A, block="extension", and
    instant XMLhas xsi:type=restriction of A
    """
    assert_bindings(
        schema="msData/element/elemT038.xsd",
        is_valid=True,
        instance="msData/element/elemT038.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_t037_elem_t037_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=simpleType A, block="extension", and instant
    XMLhas xsi:type=list of the Union A and B
    """
    assert_bindings(
        schema="msData/element/elemT037.xsd",
        is_valid=True,
        instance="msData/element/elemT037.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t036_elem_t036_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=simpleType A, block="extension", and instant
    XMLhas xsi:type=list of A
    """
    assert_bindings(
        schema="msData/element/elemT036.xsd",
        is_valid=True,
        instance="msData/element/elemT036.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t035_elem_t035_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=simpleType A, block="extension", and instant
    XMLhas xsi:type=Union of A and B
    """
    assert_bindings(
        schema="msData/element/elemT035.xsd",
        is_valid=True,
        instance="msData/element/elemT035.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t034_elem_t034_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=simpleType A, block="extension", and instant
    XMLhas xsi:type=Union of A
    """
    assert_bindings(
        schema="msData/element/elemT034.xsd",
        is_valid=True,
        instance="msData/element/elemT034.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t033_elem_t033_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=simpleType A, block="extension", and instant
    XMLhas xsi:type=base of A
    """
    assert_bindings(
        schema="msData/element/elemT033.xsd",
        is_valid=True,
        instance="msData/element/elemT033.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t032_elem_t032_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=simpleType A, block="extension", and instant
    XMLhas xsi:type=restriction of A
    """
    assert_bindings(
        schema="msData/element/elemT032.xsd",
        is_valid=True,
        instance="msData/element/elemT032.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_t031_elem_t031_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=simpleType A, block="extension", and instant
    XMLhas xsi:type=B (a different type)
    """
    assert_bindings(
        schema="msData/element/elemT031.xsd",
        is_valid=True,
        instance="msData/element/elemT031.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t030_elem_t030_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=simpleType A, block="extension", and instant
    XMLhas xsi:type=A
    """
    assert_bindings(
        schema="msData/element/elemT030.xsd",
        is_valid=True,
        instance="msData/element/elemT030.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_t029_elem_t029_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=ur-Type, block="restriction", and instant
    XMLhas xsi:type=List of the Union of simpleType A and B TSTF observed
    that although the original bug report is mistaken, the instance is
    none-the-less invalid, because the controlling element declaration
    blocks derivation (from its implicit type AnyType) by restriction.
    """
    assert_bindings(
        schema="msData/element/elemT029.xsd",
        is_valid=True,
        instance="msData/element/elemT029.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t028_elem_t028_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=ur-Type, block="restriction", and instant
    XMLhas xsi:type=List of simpleType A TSTF observed that although the
    original bug report is mistaken, the instance is none-the-less
    invalid, because the controlling element declaration blocks derivation
    (from its implicit type AnyType) by restriction.
    """
    assert_bindings(
        schema="msData/element/elemT028.xsd",
        is_valid=True,
        instance="msData/element/elemT028.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t027_elem_t027_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=ur-Type, block="restriction", and instant
    XMLhas xsi:type=union of simpleType A and B TSTF observed that
    although the original bug report is mistaken, the instance is none-
    the-less invalid, because the controlling element declaration blocks
    derivation (from its implicit type AnyType) by restriction.
    """
    assert_bindings(
        schema="msData/element/elemT027.xsd",
        is_valid=True,
        instance="msData/element/elemT027.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t026_elem_t026_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=ur-Type, block="restriction", and instant
    XMLhas xsi:type=union of simpleType A TSTF observed that although the
    original bug report is mistaken, the instance is none-the-less
    invalid, because the controlling element declaration blocks derivation
    (from its implicit type AnyType) by restriction.
    """
    assert_bindings(
        schema="msData/element/elemT026.xsd",
        is_valid=True,
        instance="msData/element/elemT026.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_elem_t025_elem_t025_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=complexType A, block="restriction", and
    instant XMLhas xsi:type=extension of A
    """
    assert_bindings(
        schema="msData/element/elemT025.xsd",
        is_valid=True,
        instance="msData/element/elemT025.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_t024_elem_t024_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=complexType A, block="restriction", and
    instant XMLhas xsi:type=restriction of A
    """
    assert_bindings(
        schema="msData/element/elemT024.xsd",
        is_valid=True,
        instance="msData/element/elemT024.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t023_elem_t023_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=simpleType A, block="restriction", and
    instant XMLhas xsi:type=list of the Union A and B
    """
    assert_bindings(
        schema="msData/element/elemT023.xsd",
        is_valid=True,
        instance="msData/element/elemT023.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t022_elem_t022_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=simpleType A, block="restriction", and
    instant XMLhas xsi:type=list of A
    """
    assert_bindings(
        schema="msData/element/elemT022.xsd",
        is_valid=True,
        instance="msData/element/elemT022.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t021_elem_t021_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=simpleType A, block="restriction", and
    instant XMLhas xsi:type=Union of A and B
    """
    assert_bindings(
        schema="msData/element/elemT021.xsd",
        is_valid=True,
        instance="msData/element/elemT021.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t020_elem_t020_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=simpleType A, block="restriction", and
    instant XMLhas xsi:type=Union of A
    """
    assert_bindings(
        schema="msData/element/elemT020.xsd",
        is_valid=True,
        instance="msData/element/elemT020.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t019_elem_t019_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=simpleType A, block="restriction", and
    instant XMLhas xsi:type=base of A
    """
    assert_bindings(
        schema="msData/element/elemT019.xsd",
        is_valid=True,
        instance="msData/element/elemT019.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t018_elem_t018_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=simpleType A, block="restriction", and
    instant XMLhas xsi:type=restriction of A
    """
    assert_bindings(
        schema="msData/element/elemT018.xsd",
        is_valid=True,
        instance="msData/element/elemT018.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t017_elem_t017_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=simpleType A, block="restriction", and
    instant XMLhas xsi:type=B (a different type)
    """
    assert_bindings(
        schema="msData/element/elemT017.xsd",
        is_valid=True,
        instance="msData/element/elemT017.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t016_elem_t016_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element type=simpleType A, block="restriction", and
    instant XMLhas xsi:type=A
    """
    assert_bindings(
        schema="msData/element/elemT016.xsd",
        is_valid=True,
        instance="msData/element/elemT016.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_t015_elem_t015_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : schema with block="#all" and, element with block="", a
    list used in instant XML
    """
    assert_bindings(
        schema="msData/element/elemT015.xsd",
        is_valid=True,
        instance="msData/element/elemT015.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_t014_elem_t014_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : schema with block="#all" and, element with block="", a
    union used in instant XML
    """
    assert_bindings(
        schema="msData/element/elemT014.xsd",
        is_valid=True,
        instance="msData/element/elemT014.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_t013_elem_t013_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : schame with blockDefault="#all" and a union used in
    instant XML
    """
    assert_bindings(
        schema="msData/element/elemT013.xsd",
        is_valid=True,
        instance="msData/element/elemT013.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t012_elem_t012_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element with block="#all" and a union used in instant XML
    """
    assert_bindings(
        schema="msData/element/elemT012.xsd",
        is_valid=True,
        instance="msData/element/elemT012.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t011_elem_t011_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : schema with blockDefault="#all" and a list used in
    instant XML
    """
    assert_bindings(
        schema="msData/element/elemT011.xsd",
        is_valid=True,
        instance="msData/element/elemT011.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_elem_t008_elem_t008_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with Element with block="" and a subsitution of
    a derivation by extension
    """
    assert_bindings(
        schema="msData/element/elemT008.xsd",
        is_valid=True,
        instance="msData/element/elemT008.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_t007_elem_t007_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with Element with block="" and a subsitution of
    a derivation by restriction
    """
    assert_bindings(
        schema="msData/element/elemT007.xsd",
        is_valid=True,
        instance="msData/element/elemT007.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_t006_elem_t006_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with Element with block="#all" and a subsitution
    of a derivation by extension
    """
    assert_bindings(
        schema="msData/element/elemT006.xsd",
        is_valid=True,
        instance="msData/element/elemT006.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t005_elem_t005_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with Element with block="#all" and a subsitution
    of a derivation by restriction
    """
    assert_bindings(
        schema="msData/element/elemT005.xsd",
        is_valid=True,
        instance="msData/element/elemT005.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t004_elem_t004_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with Element with block=extension and a
    subsitution of a derivation by extension
    """
    assert_bindings(
        schema="msData/element/elemT004.xsd",
        is_valid=True,
        instance="msData/element/elemT004.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_t003_elem_t003_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with Element with block=extension and a
    subsitution of a derivation by restriction
    """
    assert_bindings(
        schema="msData/element/elemT003.xsd",
        is_valid=True,
        instance="msData/element/elemT003.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_elem_t002_elem_t002_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with Element with block=restriction and a
    subsitution of a derivation by extension
    """
    assert_bindings(
        schema="msData/element/elemT002.xsd",
        is_valid=True,
        instance="msData/element/elemT002.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_t001_elem_t001_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with Element with block=restriction and a
    subsitution of a derivation by restriction
    """
    assert_bindings(
        schema="msData/element/elemT001.xsd",
        is_valid=True,
        instance="msData/element/elemT001.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_elem_s008_elem_s008_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element with final='' and an element affliation by
    extension
    """
    assert_bindings(
        schema="msData/element/elemS008.xsd",
        is_valid=True,
        instance="msData/element/elemS008.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_elem_s007_elem_s007_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element with final='' and an element affliation by
    restriction
    """
    assert_bindings(
        schema="msData/element/elemS007.xsd",
        is_valid=True,
        instance="msData/element/elemS007.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_elem_s003_elem_s003_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element with final=extension and an element affliation by
    restriction
    """
    assert_bindings(
        schema="msData/element/elemS003.xsd",
        is_valid=True,
        instance="msData/element/elemS003.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


@pytest.mark.xfail
def test_elem_s002_elem_s002_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Element with final=restriction and an element affliation
    by extension
    """
    assert_bindings(
        schema="msData/element/elemS002.xsd",
        is_valid=True,
        instance="msData/element/elemS002.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_r005_elem_r005_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Valid Document for Element with schema's
    elementFormDefault=qualified and default qualified elements
    """
    assert_bindings(
        schema="msData/element/elemR005.xsd",
        is_valid=True,
        instance="msData/element/elemR005.xml",
        instance_is_valid=True,
        class_name="PurchaseOrder",
        version="1.0",
    )


def test_elem_r004_elem_r004_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Valid Document for Element with schema's
    elementFormDefault=qualified and explicitly qualified elements
    """
    assert_bindings(
        schema="msData/element/elemR004.xsd",
        is_valid=True,
        instance="msData/element/elemR004.xml",
        instance_is_valid=True,
        class_name="PurchaseOrder",
        version="1.0",
    )


def test_elem_r002_elem_r002_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Valid Document for Element with form=qualified and
    default qualified elements
    """
    assert_bindings(
        schema="msData/element/elemR002.xsd",
        is_valid=True,
        instance="msData/element/elemR002.xml",
        instance_is_valid=True,
        class_name="PurchaseOrder",
        version="1.0",
    )


def test_elem_r001_elem_r001_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Valid Document for Element with form=qualified and
    explicitly qualified elements
    """
    assert_bindings(
        schema="msData/element/elemR001.xsd",
        is_valid=True,
        instance="msData/element/elemR001.xml",
        instance_is_valid=True,
        class_name="PurchaseOrder",
        version="1.0",
    )


def test_elem_q022_elem_q022_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with default=Hello andDocument contains nothing
    """
    assert_bindings(
        schema="msData/element/elemQ022.xsd",
        is_valid=True,
        instance="msData/element/elemQ022.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_q021_elem_q021_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with default=Hello andDocument contains Hello
    World!
    """
    assert_bindings(
        schema="msData/element/elemQ021.xsd",
        is_valid=True,
        instance="msData/element/elemQ021.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_q020_elem_q020_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with default=Hello andDocument contains Hello
    """
    assert_bindings(
        schema="msData/element/elemQ020.xsd",
        is_valid=True,
        instance="msData/element/elemQ020.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_q019_elem_q019_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with fixed=Hello andDocument contains nothing
    """
    assert_bindings(
        schema="msData/element/elemQ019.xsd",
        is_valid=True,
        instance="msData/element/elemQ019.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_q018_elem_q018_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with fixed=Hello andDocument contains Hello
    World!
    """
    assert_bindings(
        schema="msData/element/elemQ018.xsd",
        is_valid=True,
        instance="msData/element/elemQ018.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_q017_elem_q017_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with fixed=Hello andDocument contains Hello
    """
    assert_bindings(
        schema="msData/element/elemQ017.xsd",
        is_valid=True,
        instance="msData/element/elemQ017.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_q015_elem_q015_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with minOccurs = 1 and maxOccurs = unbounded and
    3 occurrences
    """
    assert_bindings(
        schema="msData/element/elemQ015.xsd",
        is_valid=True,
        instance="msData/element/elemQ015.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_q014_elem_q014_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with minOccurs = 1 and maxOccurs = 2 and 3
    occurrences
    """
    assert_bindings(
        schema="msData/element/elemQ014.xsd",
        is_valid=True,
        instance="msData/element/elemQ014.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_q013_elem_q013_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with minOccurs = 1 and maxOccurs = 2 and 2
    occurrences
    """
    assert_bindings(
        schema="msData/element/elemQ013.xsd",
        is_valid=True,
        instance="msData/element/elemQ013.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_q012_elem_q012_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with minOccurs = 1 and 2 occurrences
    """
    assert_bindings(
        schema="msData/element/elemQ012.xsd",
        is_valid=True,
        instance="msData/element/elemQ012.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_q011_elem_q011_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with minOccurs = 1 and 1 occurrence
    """
    assert_bindings(
        schema="msData/element/elemQ011.xsd",
        is_valid=True,
        instance="msData/element/elemQ011.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_q010_elem_q010_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with minOccurs = 1 and no occurences
    """
    assert_bindings(
        schema="msData/element/elemQ010.xsd",
        is_valid=True,
        instance="msData/element/elemQ010.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_q009_elem_q009_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with default maxOccurs and 2 occurrences
    """
    assert_bindings(
        schema="msData/element/elemQ009.xsd",
        is_valid=True,
        instance="msData/element/elemQ009.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_q008_elem_q008_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with default maxOccurs and 1 occurrence
    """
    assert_bindings(
        schema="msData/element/elemQ008.xsd",
        is_valid=True,
        instance="msData/element/elemQ008.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_q007_elem_q007_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with default minOccurs and no occurences
    """
    assert_bindings(
        schema="msData/element/elemQ007.xsd",
        is_valid=True,
        instance="msData/element/elemQ007.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_o012_elem_o012_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with element with nillable = false
    """
    assert_bindings(
        schema="msData/element/elemO012.xsd",
        is_valid=True,
        instance="msData/element/elemO012.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_o011_elem_o011_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with element with nillable = false andDocument's
    null = false in xml
    """
    assert_bindings(
        schema="msData/element/elemO011.xsd",
        is_valid=True,
        instance="msData/element/elemO011.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_o010_elem_o010_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with element with nillable = false andDocument's
    null = true in xml
    """
    assert_bindings(
        schema="msData/element/elemO010.xsd",
        is_valid=True,
        instance="msData/element/elemO010.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_o009_elem_o009_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with element with nillable = true
    """
    assert_bindings(
        schema="msData/element/elemO009.xsd",
        is_valid=True,
        instance="msData/element/elemO009.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_o008_elem_o008_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with element with nillable = true andDocument's
    null = false in xml
    """
    assert_bindings(
        schema="msData/element/elemO008.xsd",
        is_valid=True,
        instance="msData/element/elemO008.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_o007_elem_o007_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with element with nillable = true and Document's
    null = true but element has content
    """
    assert_bindings(
        schema="msData/element/elemO007.xsd",
        is_valid=True,
        instance="msData/element/elemO007.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_elem_o006_elem_o006_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with element with nillable = true in xsd
    andDocument's nil = true in xml
    """
    assert_bindings(
        schema="msData/element/elemO006.xsd",
        is_valid=True,
        instance="msData/element/elemO006.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_o005_elem_o005_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with element with anonymous complexType, no type
    on element
    """
    assert_bindings(
        schema="msData/element/elemO005.xsd",
        is_valid=True,
        instance="msData/element/elemO005.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_o004_elem_o004_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with element with complexType
    """
    assert_bindings(
        schema="msData/element/elemO004.xsd",
        is_valid=True,
        instance="msData/element/elemO004.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_o003_elem_o003_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with element with anonymous simpleType, no type
    on element
    """
    assert_bindings(
        schema="msData/element/elemO003.xsd",
        is_valid=True,
        instance="msData/element/elemO003.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_o002_elem_o002_v():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with element with simpleType
    """
    assert_bindings(
        schema="msData/element/elemO002.xsd",
        is_valid=True,
        instance="msData/element/elemO002.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_elem_o001_elem_o001_i():
    """
    TEST :3.3.2 XML Representation of Element Declaration Schema
    Components : Document with element's ref to an element with
    abstract=true
    """
    assert_bindings(
        schema="msData/element/elemO001.xsd",
        is_valid=True,
        instance="msData/element/elemO001.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_err_f001_err_f001_i():
    """
    TEST :Primer Errata : Errata E2-35: length facet is now allowed with
    either minLength or maxLength if they are specified in different
    derivation steps
    """
    assert_bindings(
        schema="msData/errata10/errF001.xsd",
        is_valid=True,
        instance="msData/errata10/errF001.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_err_e008_err_e008_v():
    """
    TEST :Primer Errata : E2-17 Error: Do not allow carriage return in
    token values
    """
    assert_bindings(
        schema="msData/errata10/errE008.xsd",
        is_valid=True,
        instance="msData/errata10/errE008.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_err_e006_err_e006_v():
    """
    TEST :Primer Errata : E2-22 Clarification: test date, gYearMonth,
    gMonthDay, gDay, gMonth and gYear permit an optional, trailing time
    zone specification.
    """
    assert_bindings(
        schema="msData/errata10/errE006.xsd",
        is_valid=True,
        instance="msData/errata10/errE006.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_err_e004_err_e004_i():
    """
    TEST :Primer Errata : E2-24 Error: test that absent 'T' is enforced
    when no time elements are present
    """
    assert_bindings(
        schema="msData/errata10/errE004.xsd",
        is_valid=True,
        instance="msData/errata10/errE004.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_err_e003_err_e003_v():
    """
    TEST :Primer Errata : E2-25 Error: test support for the new language
    pattern ([a-zA-Z]{1,8})-([a-zA-Z0-9]{1,8})*
    """
    assert_bindings(
        schema="msData/errata10/errE003.xsd",
        is_valid=True,
        instance="msData/errata10/errE003.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_err_e002_err_e002_v():
    """
    TEST :Primer Errata : E2-27 Error: test that nonNegativeIntegers
    support a '-' on zero
    """
    assert_bindings(
        schema="msData/errata10/errE002.xsd",
        is_valid=True,
        instance="msData/errata10/errE002.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_err_e001_err_e001_v():
    """
    TEST :Primer Errata : E2-27 Error: test that nonPositiveIntegers
    support a '+' on zero
    """
    assert_bindings(
        schema="msData/errata10/errE001.xsd",
        is_valid=True,
        instance="msData/errata10/errE001.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_err_c007_err_c007_v():
    """
    TEST :Primer Errata : E1-22 Error: R-117 Process contents for ur-type
    need to be lax
    """
    assert_bindings(
        schema="msData/errata10/errC007.xsd",
        is_valid=True,
        instance="msData/errata10/errC007.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_err_c001_err_c001_v():
    """
    TEST :Primer Errata : E1-40 Clarification: test that anySimpleType
    whitespace normalization is set to preserve
    """
    assert_bindings(
        schema="msData/errata10/errC001.xsd",
        is_valid=True,
        instance="msData/errata10/errC001.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_err_a003_err_a003_v():
    """
    TEST :Primer Errata : E0-15 Error, E2-12 Error: test lexical
    representation of gMonth
    """
    assert_bindings(
        schema="msData/errata10/errA003.xsd",
        is_valid=True,
        instance="msData/errata10/errA003.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_err_a002_err_a002_i():
    """
    TEST :Primer Errata : E0-10 Error, E1-11 Error: test that ##other
    namespace is any namespace other than the target namespace
    """
    assert_bindings(
        schema="msData/errata10/errA002.xsd",
        is_valid=True,
        instance="msData/errata10/errA002.xml",
        instance_is_valid=False,
        class_name="Root",
        version="1.0",
    )


def test_err_a001_err_a001_v():
    """
    TEST :Primer Errata : E0-23 Clarification: test that facet
    fractionDigits can be added to all numeric datatypes as long as value
    is 0 (except for decimal which takes any value)
    """
    assert_bindings(
        schema="msData/errata10/errA001.xsd",
        is_valid=True,
        instance="msData/errata10/errA001.xml",
        instance_is_valid=True,
        class_name="Root",
        version="1.0",
    )


def test_group_o009v_group_o009v_i():
    """
    TEST :Syntax Checking (id, ref) : Test content: (xml instant is
    invalid) annotation follow by sequence
    """
    assert_bindings(
        schema="msData/group/groupO009.xsd",
        is_valid=True,
        instance="msData/group/groupO009.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_o008v_group_o008v_v():
    """
    TEST :Syntax Checking (id, ref) : Test content: annotation follow by
    sequence
    """
    assert_bindings(
        schema="msData/group/groupO008.xsd",
        is_valid=True,
        instance="msData/group/groupO008.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_o007v_group_o007v_i():
    """
    TEST :Syntax Checking (id, ref) : Test content: (xml instant is
    invalid) annotation follow by choice
    """
    assert_bindings(
        schema="msData/group/groupO007.xsd",
        is_valid=True,
        instance="msData/group/groupO007.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_o006v_group_o006v_v():
    """
    TEST :Syntax Checking (id, ref) : Test content: annotation follow by
    choice
    """
    assert_bindings(
        schema="msData/group/groupO006.xsd",
        is_valid=True,
        instance="msData/group/groupO006.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_o005v_group_o005v_i():
    """
    TEST :Syntax Checking (id, ref) : Test content: (xml instant is
    invalid) annotation follow by all
    """
    assert_bindings(
        schema="msData/group/groupO005.xsd",
        is_valid=True,
        instance="msData/group/groupO005.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_o004v_group_o004v_v():
    """
    TEST :Syntax Checking (id, ref) : Test content: annotation follow by
    all
    """
    assert_bindings(
        schema="msData/group/groupO004.xsd",
        is_valid=True,
        instance="msData/group/groupO004.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_n021v_group_n021v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is complexType: elements in
    instant XML=3, maxOccurs=unbounded
    """
    assert_bindings(
        schema="msData/group/groupN021.xsd",
        is_valid=True,
        instance="msData/group/groupN021.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_n019v_group_n019v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is complexType: elements in
    instant XML=3, minOccurs=1, maxOccurs=2
    """
    assert_bindings(
        schema="msData/group/groupN019.xsd",
        is_valid=True,
        instance="msData/group/groupN019.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_n018v_group_n018v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is complexType: elements in
    instant XML=2, minOccurs=1, maxOccurs=2
    """
    assert_bindings(
        schema="msData/group/groupN018.xsd",
        is_valid=True,
        instance="msData/group/groupN018.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_n017v_group_n017v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is complexType: elements in
    instant XML=1, minOccurs=1, maxOccurs=2
    """
    assert_bindings(
        schema="msData/group/groupN017.xsd",
        is_valid=True,
        instance="msData/group/groupN017.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_n016v_group_n016v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is complexType: elements in
    instant XML=0, minOccurs=1, maxOccurs=2
    """
    assert_bindings(
        schema="msData/group/groupN016.xsd",
        is_valid=True,
        instance="msData/group/groupN016.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_n015v_group_n015v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is complexType: elements in
    instant XML=2, minOccurs=1, maxOccurs=1
    """
    assert_bindings(
        schema="msData/group/groupN015.xsd",
        is_valid=True,
        instance="msData/group/groupN015.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_n014v_group_n014v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is complexType: elements in
    instant XML=1, minOccurs=1, maxOccurs=1
    """
    assert_bindings(
        schema="msData/group/groupN014.xsd",
        is_valid=True,
        instance="msData/group/groupN014.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_n013v_group_n013v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is complexType: elements in
    instant XML=0, minOccurs=1, maxOccurs=1
    """
    assert_bindings(
        schema="msData/group/groupN013.xsd",
        is_valid=True,
        instance="msData/group/groupN013.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_n012v_group_n012v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is complexType: elements in
    instant XML=2, minOccurs=1, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupN012.xsd",
        is_valid=True,
        instance="msData/group/groupN012.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_n011v_group_n011v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is complexType: elements in
    instant XML=1, minOccurs=1, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupN011.xsd",
        is_valid=True,
        instance="msData/group/groupN011.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_n010v_group_n010v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is complexType: elements in
    instant XML=0, minOccurs=1, maxOccurs=absent
    """
    assert_bindings(
        schema="msData/group/groupN010.xsd",
        is_valid=True,
        instance="msData/group/groupN010.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_n009v_group_n009v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is complexType: elements in
    instant XML=0, minOccurs=0, maxOccurs=999999999
    """
    assert_bindings(
        schema="msData/group/groupN009.xsd",
        is_valid=True,
        instance="msData/group/groupN009.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_n008v_group_n008v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is complexType: elements in
    instant XML=1, minOccurs=0, maxOccurs=0
    """
    assert_bindings(
        schema="msData/group/groupN008.xsd",
        is_valid=True,
        instance="msData/group/groupN008.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )


def test_group_n007v_group_n007v_v():
    """
    TEST :Syntax Checking (id, ref) : parent is complexType: elements in
    instant XML=0, minOccurs=0, maxOccurs=0
    """
    assert_bindings(
        schema="msData/group/groupN007.xsd",
        is_valid=True,
        instance="msData/group/groupN007.xml",
        instance_is_valid=True,
        class_name="Doc",
        version="1.0",
    )


def test_group_n006v_group_n006v_i():
    """
    TEST :Syntax Checking (id, ref) : parent is complexType: elements in
    instant XML=2, minOccurs=0, maxOccurs=1
    """
    assert_bindings(
        schema="msData/group/groupN006.xsd",
        is_valid=True,
        instance="msData/group/groupN006.xml",
        instance_is_valid=False,
        class_name="Doc",
        version="1.0",
    )
