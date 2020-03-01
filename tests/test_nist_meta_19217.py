import pytest

from tests.utils import assert_bindings


def test_atomic_integer_min_inclusive_1_nistxml_sv_iv_atomic_integer_min_inclusive_2_4():
    """
    Type atomic/integer is restricted by facet minInclusive with value
    156487900906511434.
    """
    assert_bindings(
        schema="nistData/atomic/integer/Schema+Instance/NISTSchema-SV-IV-atomic-integer-minInclusive-2.xsd",
        is_valid=True,
        instance="nistData/atomic/integer/Schema+Instance/NISTXML-SV-IV-atomic-integer-minInclusive-2-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicIntegerMinInclusive2",
        version="1.0",
    )


def test_atomic_integer_min_inclusive_1_nistxml_sv_iv_atomic_integer_min_inclusive_2_5():
    """
    Type atomic/integer is restricted by facet minInclusive with value
    156487900906511434.
    """
    assert_bindings(
        schema="nistData/atomic/integer/Schema+Instance/NISTSchema-SV-IV-atomic-integer-minInclusive-2.xsd",
        is_valid=True,
        instance="nistData/atomic/integer/Schema+Instance/NISTXML-SV-IV-atomic-integer-minInclusive-2-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicIntegerMinInclusive2",
        version="1.0",
    )


def test_atomic_integer_min_inclusive_nistxml_sv_iv_atomic_integer_min_inclusive_1_1():
    """
    Type atomic/integer is restricted by facet minInclusive with value
    -999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/integer/Schema+Instance/NISTSchema-SV-IV-atomic-integer-minInclusive-1.xsd",
        is_valid=True,
        instance="nistData/atomic/integer/Schema+Instance/NISTXML-SV-IV-atomic-integer-minInclusive-1-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicIntegerMinInclusive1",
        version="1.0",
    )


def test_atomic_integer_min_inclusive_nistxml_sv_iv_atomic_integer_min_inclusive_1_2():
    """
    Type atomic/integer is restricted by facet minInclusive with value
    -999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/integer/Schema+Instance/NISTSchema-SV-IV-atomic-integer-minInclusive-1.xsd",
        is_valid=True,
        instance="nistData/atomic/integer/Schema+Instance/NISTXML-SV-IV-atomic-integer-minInclusive-1-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicIntegerMinInclusive1",
        version="1.0",
    )


def test_atomic_integer_min_inclusive_nistxml_sv_iv_atomic_integer_min_inclusive_1_3():
    """
    Type atomic/integer is restricted by facet minInclusive with value
    -999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/integer/Schema+Instance/NISTSchema-SV-IV-atomic-integer-minInclusive-1.xsd",
        is_valid=True,
        instance="nistData/atomic/integer/Schema+Instance/NISTXML-SV-IV-atomic-integer-minInclusive-1-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicIntegerMinInclusive1",
        version="1.0",
    )


def test_atomic_integer_min_inclusive_nistxml_sv_iv_atomic_integer_min_inclusive_1_4():
    """
    Type atomic/integer is restricted by facet minInclusive with value
    -999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/integer/Schema+Instance/NISTSchema-SV-IV-atomic-integer-minInclusive-1.xsd",
        is_valid=True,
        instance="nistData/atomic/integer/Schema+Instance/NISTXML-SV-IV-atomic-integer-minInclusive-1-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicIntegerMinInclusive1",
        version="1.0",
    )


def test_atomic_integer_min_inclusive_nistxml_sv_iv_atomic_integer_min_inclusive_1_5():
    """
    Type atomic/integer is restricted by facet minInclusive with value
    -999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/integer/Schema+Instance/NISTSchema-SV-IV-atomic-integer-minInclusive-1.xsd",
        is_valid=True,
        instance="nistData/atomic/integer/Schema+Instance/NISTXML-SV-IV-atomic-integer-minInclusive-1-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicIntegerMinInclusive1",
        version="1.0",
    )


def test_atomic_integer_min_exclusive_4_nistxml_sv_iv_atomic_integer_min_exclusive_5_1():
    """
    Type atomic/integer is restricted by facet minExclusive with value
    999999999999999998.
    """
    assert_bindings(
        schema="nistData/atomic/integer/Schema+Instance/NISTSchema-SV-IV-atomic-integer-minExclusive-5.xsd",
        is_valid=True,
        instance="nistData/atomic/integer/Schema+Instance/NISTXML-SV-IV-atomic-integer-minExclusive-5-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicIntegerMinExclusive5",
        version="1.0",
    )


def test_atomic_integer_min_exclusive_3_nistxml_sv_iv_atomic_integer_min_exclusive_4_1():
    """
    Type atomic/integer is restricted by facet minExclusive with value
    470740450062970382.
    """
    assert_bindings(
        schema="nistData/atomic/integer/Schema+Instance/NISTSchema-SV-IV-atomic-integer-minExclusive-4.xsd",
        is_valid=True,
        instance="nistData/atomic/integer/Schema+Instance/NISTXML-SV-IV-atomic-integer-minExclusive-4-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicIntegerMinExclusive4",
        version="1.0",
    )


def test_atomic_integer_min_exclusive_3_nistxml_sv_iv_atomic_integer_min_exclusive_4_2():
    """
    Type atomic/integer is restricted by facet minExclusive with value
    470740450062970382.
    """
    assert_bindings(
        schema="nistData/atomic/integer/Schema+Instance/NISTSchema-SV-IV-atomic-integer-minExclusive-4.xsd",
        is_valid=True,
        instance="nistData/atomic/integer/Schema+Instance/NISTXML-SV-IV-atomic-integer-minExclusive-4-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicIntegerMinExclusive4",
        version="1.0",
    )


def test_atomic_integer_min_exclusive_3_nistxml_sv_iv_atomic_integer_min_exclusive_4_3():
    """
    Type atomic/integer is restricted by facet minExclusive with value
    470740450062970382.
    """
    assert_bindings(
        schema="nistData/atomic/integer/Schema+Instance/NISTSchema-SV-IV-atomic-integer-minExclusive-4.xsd",
        is_valid=True,
        instance="nistData/atomic/integer/Schema+Instance/NISTXML-SV-IV-atomic-integer-minExclusive-4-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicIntegerMinExclusive4",
        version="1.0",
    )


def test_atomic_integer_min_exclusive_3_nistxml_sv_iv_atomic_integer_min_exclusive_4_4():
    """
    Type atomic/integer is restricted by facet minExclusive with value
    470740450062970382.
    """
    assert_bindings(
        schema="nistData/atomic/integer/Schema+Instance/NISTSchema-SV-IV-atomic-integer-minExclusive-4.xsd",
        is_valid=True,
        instance="nistData/atomic/integer/Schema+Instance/NISTXML-SV-IV-atomic-integer-minExclusive-4-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicIntegerMinExclusive4",
        version="1.0",
    )


def test_atomic_integer_min_exclusive_3_nistxml_sv_iv_atomic_integer_min_exclusive_4_5():
    """
    Type atomic/integer is restricted by facet minExclusive with value
    470740450062970382.
    """
    assert_bindings(
        schema="nistData/atomic/integer/Schema+Instance/NISTSchema-SV-IV-atomic-integer-minExclusive-4.xsd",
        is_valid=True,
        instance="nistData/atomic/integer/Schema+Instance/NISTXML-SV-IV-atomic-integer-minExclusive-4-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicIntegerMinExclusive4",
        version="1.0",
    )


def test_atomic_integer_min_exclusive_2_nistxml_sv_iv_atomic_integer_min_exclusive_3_1():
    """
    Type atomic/integer is restricted by facet minExclusive with value
    389578809107570477.
    """
    assert_bindings(
        schema="nistData/atomic/integer/Schema+Instance/NISTSchema-SV-IV-atomic-integer-minExclusive-3.xsd",
        is_valid=True,
        instance="nistData/atomic/integer/Schema+Instance/NISTXML-SV-IV-atomic-integer-minExclusive-3-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicIntegerMinExclusive3",
        version="1.0",
    )


def test_atomic_integer_min_exclusive_2_nistxml_sv_iv_atomic_integer_min_exclusive_3_2():
    """
    Type atomic/integer is restricted by facet minExclusive with value
    389578809107570477.
    """
    assert_bindings(
        schema="nistData/atomic/integer/Schema+Instance/NISTSchema-SV-IV-atomic-integer-minExclusive-3.xsd",
        is_valid=True,
        instance="nistData/atomic/integer/Schema+Instance/NISTXML-SV-IV-atomic-integer-minExclusive-3-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicIntegerMinExclusive3",
        version="1.0",
    )


def test_atomic_integer_min_exclusive_2_nistxml_sv_iv_atomic_integer_min_exclusive_3_3():
    """
    Type atomic/integer is restricted by facet minExclusive with value
    389578809107570477.
    """
    assert_bindings(
        schema="nistData/atomic/integer/Schema+Instance/NISTSchema-SV-IV-atomic-integer-minExclusive-3.xsd",
        is_valid=True,
        instance="nistData/atomic/integer/Schema+Instance/NISTXML-SV-IV-atomic-integer-minExclusive-3-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicIntegerMinExclusive3",
        version="1.0",
    )


def test_atomic_integer_min_exclusive_2_nistxml_sv_iv_atomic_integer_min_exclusive_3_4():
    """
    Type atomic/integer is restricted by facet minExclusive with value
    389578809107570477.
    """
    assert_bindings(
        schema="nistData/atomic/integer/Schema+Instance/NISTSchema-SV-IV-atomic-integer-minExclusive-3.xsd",
        is_valid=True,
        instance="nistData/atomic/integer/Schema+Instance/NISTXML-SV-IV-atomic-integer-minExclusive-3-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicIntegerMinExclusive3",
        version="1.0",
    )


def test_atomic_integer_min_exclusive_2_nistxml_sv_iv_atomic_integer_min_exclusive_3_5():
    """
    Type atomic/integer is restricted by facet minExclusive with value
    389578809107570477.
    """
    assert_bindings(
        schema="nistData/atomic/integer/Schema+Instance/NISTSchema-SV-IV-atomic-integer-minExclusive-3.xsd",
        is_valid=True,
        instance="nistData/atomic/integer/Schema+Instance/NISTXML-SV-IV-atomic-integer-minExclusive-3-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicIntegerMinExclusive3",
        version="1.0",
    )


def test_atomic_integer_min_exclusive_1_nistxml_sv_iv_atomic_integer_min_exclusive_2_1():
    """
    Type atomic/integer is restricted by facet minExclusive with value
    511594901568435787.
    """
    assert_bindings(
        schema="nistData/atomic/integer/Schema+Instance/NISTSchema-SV-IV-atomic-integer-minExclusive-2.xsd",
        is_valid=True,
        instance="nistData/atomic/integer/Schema+Instance/NISTXML-SV-IV-atomic-integer-minExclusive-2-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicIntegerMinExclusive2",
        version="1.0",
    )


def test_atomic_integer_min_exclusive_1_nistxml_sv_iv_atomic_integer_min_exclusive_2_2():
    """
    Type atomic/integer is restricted by facet minExclusive with value
    511594901568435787.
    """
    assert_bindings(
        schema="nistData/atomic/integer/Schema+Instance/NISTSchema-SV-IV-atomic-integer-minExclusive-2.xsd",
        is_valid=True,
        instance="nistData/atomic/integer/Schema+Instance/NISTXML-SV-IV-atomic-integer-minExclusive-2-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicIntegerMinExclusive2",
        version="1.0",
    )


def test_atomic_integer_min_exclusive_1_nistxml_sv_iv_atomic_integer_min_exclusive_2_3():
    """
    Type atomic/integer is restricted by facet minExclusive with value
    511594901568435787.
    """
    assert_bindings(
        schema="nistData/atomic/integer/Schema+Instance/NISTSchema-SV-IV-atomic-integer-minExclusive-2.xsd",
        is_valid=True,
        instance="nistData/atomic/integer/Schema+Instance/NISTXML-SV-IV-atomic-integer-minExclusive-2-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicIntegerMinExclusive2",
        version="1.0",
    )


def test_atomic_integer_min_exclusive_1_nistxml_sv_iv_atomic_integer_min_exclusive_2_4():
    """
    Type atomic/integer is restricted by facet minExclusive with value
    511594901568435787.
    """
    assert_bindings(
        schema="nistData/atomic/integer/Schema+Instance/NISTSchema-SV-IV-atomic-integer-minExclusive-2.xsd",
        is_valid=True,
        instance="nistData/atomic/integer/Schema+Instance/NISTXML-SV-IV-atomic-integer-minExclusive-2-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicIntegerMinExclusive2",
        version="1.0",
    )


def test_atomic_integer_min_exclusive_1_nistxml_sv_iv_atomic_integer_min_exclusive_2_5():
    """
    Type atomic/integer is restricted by facet minExclusive with value
    511594901568435787.
    """
    assert_bindings(
        schema="nistData/atomic/integer/Schema+Instance/NISTSchema-SV-IV-atomic-integer-minExclusive-2.xsd",
        is_valid=True,
        instance="nistData/atomic/integer/Schema+Instance/NISTXML-SV-IV-atomic-integer-minExclusive-2-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicIntegerMinExclusive2",
        version="1.0",
    )


def test_atomic_integer_min_exclusive_nistxml_sv_iv_atomic_integer_min_exclusive_1_1():
    """
    Type atomic/integer is restricted by facet minExclusive with value
    -999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/integer/Schema+Instance/NISTSchema-SV-IV-atomic-integer-minExclusive-1.xsd",
        is_valid=True,
        instance="nistData/atomic/integer/Schema+Instance/NISTXML-SV-IV-atomic-integer-minExclusive-1-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicIntegerMinExclusive1",
        version="1.0",
    )


def test_atomic_integer_min_exclusive_nistxml_sv_iv_atomic_integer_min_exclusive_1_2():
    """
    Type atomic/integer is restricted by facet minExclusive with value
    -999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/integer/Schema+Instance/NISTSchema-SV-IV-atomic-integer-minExclusive-1.xsd",
        is_valid=True,
        instance="nistData/atomic/integer/Schema+Instance/NISTXML-SV-IV-atomic-integer-minExclusive-1-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicIntegerMinExclusive1",
        version="1.0",
    )


def test_atomic_integer_min_exclusive_nistxml_sv_iv_atomic_integer_min_exclusive_1_3():
    """
    Type atomic/integer is restricted by facet minExclusive with value
    -999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/integer/Schema+Instance/NISTSchema-SV-IV-atomic-integer-minExclusive-1.xsd",
        is_valid=True,
        instance="nistData/atomic/integer/Schema+Instance/NISTXML-SV-IV-atomic-integer-minExclusive-1-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicIntegerMinExclusive1",
        version="1.0",
    )


def test_atomic_integer_min_exclusive_nistxml_sv_iv_atomic_integer_min_exclusive_1_4():
    """
    Type atomic/integer is restricted by facet minExclusive with value
    -999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/integer/Schema+Instance/NISTSchema-SV-IV-atomic-integer-minExclusive-1.xsd",
        is_valid=True,
        instance="nistData/atomic/integer/Schema+Instance/NISTXML-SV-IV-atomic-integer-minExclusive-1-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicIntegerMinExclusive1",
        version="1.0",
    )


def test_atomic_integer_min_exclusive_nistxml_sv_iv_atomic_integer_min_exclusive_1_5():
    """
    Type atomic/integer is restricted by facet minExclusive with value
    -999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/integer/Schema+Instance/NISTSchema-SV-IV-atomic-integer-minExclusive-1.xsd",
        is_valid=True,
        instance="nistData/atomic/integer/Schema+Instance/NISTXML-SV-IV-atomic-integer-minExclusive-1-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicIntegerMinExclusive1",
        version="1.0",
    )


def test_atomic_decimal_white_space_nistxml_sv_iv_atomic_decimal_white_space_1_1():
    """
    Type atomic/decimal is restricted by facet whiteSpace with value
    collapse.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-whiteSpace-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-whiteSpace-1-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalWhiteSpace1",
        version="1.0",
    )


def test_atomic_decimal_white_space_nistxml_sv_iv_atomic_decimal_white_space_1_2():
    """
    Type atomic/decimal is restricted by facet whiteSpace with value
    collapse.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-whiteSpace-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-whiteSpace-1-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalWhiteSpace1",
        version="1.0",
    )


def test_atomic_decimal_white_space_nistxml_sv_iv_atomic_decimal_white_space_1_3():
    """
    Type atomic/decimal is restricted by facet whiteSpace with value
    collapse.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-whiteSpace-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-whiteSpace-1-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalWhiteSpace1",
        version="1.0",
    )


def test_atomic_decimal_white_space_nistxml_sv_iv_atomic_decimal_white_space_1_4():
    """
    Type atomic/decimal is restricted by facet whiteSpace with value
    collapse.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-whiteSpace-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-whiteSpace-1-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalWhiteSpace1",
        version="1.0",
    )


def test_atomic_decimal_white_space_nistxml_sv_iv_atomic_decimal_white_space_1_5():
    """
    Type atomic/decimal is restricted by facet whiteSpace with value
    collapse.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-whiteSpace-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-whiteSpace-1-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalWhiteSpace1",
        version="1.0",
    )


def test_atomic_decimal_enumeration_4_nistxml_sv_iv_atomic_decimal_enumeration_5_1():
    """
    Type atomic/decimal is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-enumeration-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-enumeration-5-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalEnumeration5",
        version="1.0",
    )


def test_atomic_decimal_enumeration_4_nistxml_sv_iv_atomic_decimal_enumeration_5_2():
    """
    Type atomic/decimal is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-enumeration-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-enumeration-5-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalEnumeration5",
        version="1.0",
    )


def test_atomic_decimal_enumeration_4_nistxml_sv_iv_atomic_decimal_enumeration_5_3():
    """
    Type atomic/decimal is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-enumeration-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-enumeration-5-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalEnumeration5",
        version="1.0",
    )


def test_atomic_decimal_enumeration_4_nistxml_sv_iv_atomic_decimal_enumeration_5_4():
    """
    Type atomic/decimal is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-enumeration-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-enumeration-5-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalEnumeration5",
        version="1.0",
    )


def test_atomic_decimal_enumeration_4_nistxml_sv_iv_atomic_decimal_enumeration_5_5():
    """
    Type atomic/decimal is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-enumeration-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-enumeration-5-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalEnumeration5",
        version="1.0",
    )


def test_atomic_decimal_enumeration_3_nistxml_sv_iv_atomic_decimal_enumeration_4_1():
    """
    Type atomic/decimal is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-enumeration-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-enumeration-4-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalEnumeration4",
        version="1.0",
    )


def test_atomic_decimal_enumeration_3_nistxml_sv_iv_atomic_decimal_enumeration_4_2():
    """
    Type atomic/decimal is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-enumeration-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-enumeration-4-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalEnumeration4",
        version="1.0",
    )


def test_atomic_decimal_enumeration_3_nistxml_sv_iv_atomic_decimal_enumeration_4_3():
    """
    Type atomic/decimal is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-enumeration-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-enumeration-4-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalEnumeration4",
        version="1.0",
    )


def test_atomic_decimal_enumeration_3_nistxml_sv_iv_atomic_decimal_enumeration_4_4():
    """
    Type atomic/decimal is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-enumeration-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-enumeration-4-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalEnumeration4",
        version="1.0",
    )


def test_atomic_decimal_enumeration_3_nistxml_sv_iv_atomic_decimal_enumeration_4_5():
    """
    Type atomic/decimal is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-enumeration-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-enumeration-4-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalEnumeration4",
        version="1.0",
    )


def test_atomic_decimal_enumeration_2_nistxml_sv_iv_atomic_decimal_enumeration_3_1():
    """
    Type atomic/decimal is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-enumeration-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-enumeration-3-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalEnumeration3",
        version="1.0",
    )


def test_atomic_decimal_enumeration_2_nistxml_sv_iv_atomic_decimal_enumeration_3_2():
    """
    Type atomic/decimal is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-enumeration-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-enumeration-3-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalEnumeration3",
        version="1.0",
    )


def test_atomic_decimal_enumeration_2_nistxml_sv_iv_atomic_decimal_enumeration_3_3():
    """
    Type atomic/decimal is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-enumeration-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-enumeration-3-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalEnumeration3",
        version="1.0",
    )


def test_atomic_decimal_enumeration_2_nistxml_sv_iv_atomic_decimal_enumeration_3_4():
    """
    Type atomic/decimal is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-enumeration-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-enumeration-3-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalEnumeration3",
        version="1.0",
    )


def test_atomic_decimal_enumeration_2_nistxml_sv_iv_atomic_decimal_enumeration_3_5():
    """
    Type atomic/decimal is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-enumeration-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-enumeration-3-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalEnumeration3",
        version="1.0",
    )


def test_atomic_decimal_enumeration_1_nistxml_sv_iv_atomic_decimal_enumeration_2_1():
    """
    Type atomic/decimal is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-enumeration-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-enumeration-2-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalEnumeration2",
        version="1.0",
    )


def test_atomic_decimal_enumeration_1_nistxml_sv_iv_atomic_decimal_enumeration_2_2():
    """
    Type atomic/decimal is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-enumeration-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-enumeration-2-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalEnumeration2",
        version="1.0",
    )


def test_atomic_decimal_enumeration_1_nistxml_sv_iv_atomic_decimal_enumeration_2_3():
    """
    Type atomic/decimal is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-enumeration-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-enumeration-2-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalEnumeration2",
        version="1.0",
    )


def test_atomic_decimal_enumeration_1_nistxml_sv_iv_atomic_decimal_enumeration_2_4():
    """
    Type atomic/decimal is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-enumeration-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-enumeration-2-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalEnumeration2",
        version="1.0",
    )


def test_atomic_decimal_enumeration_1_nistxml_sv_iv_atomic_decimal_enumeration_2_5():
    """
    Type atomic/decimal is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-enumeration-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-enumeration-2-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalEnumeration2",
        version="1.0",
    )


def test_atomic_decimal_enumeration_nistxml_sv_iv_atomic_decimal_enumeration_1_1():
    """
    Type atomic/decimal is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-enumeration-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-enumeration-1-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalEnumeration1",
        version="1.0",
    )


def test_atomic_decimal_enumeration_nistxml_sv_iv_atomic_decimal_enumeration_1_2():
    """
    Type atomic/decimal is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-enumeration-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-enumeration-1-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalEnumeration1",
        version="1.0",
    )


def test_atomic_decimal_enumeration_nistxml_sv_iv_atomic_decimal_enumeration_1_3():
    """
    Type atomic/decimal is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-enumeration-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-enumeration-1-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalEnumeration1",
        version="1.0",
    )


def test_atomic_decimal_enumeration_nistxml_sv_iv_atomic_decimal_enumeration_1_4():
    """
    Type atomic/decimal is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-enumeration-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-enumeration-1-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalEnumeration1",
        version="1.0",
    )


def test_atomic_decimal_enumeration_nistxml_sv_iv_atomic_decimal_enumeration_1_5():
    """
    Type atomic/decimal is restricted by facet enumeration.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-enumeration-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-enumeration-1-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalEnumeration1",
        version="1.0",
    )


def test_atomic_decimal_pattern_4_nistxml_sv_iv_atomic_decimal_pattern_5_1():
    r"""
    Type atomic/decimal is restricted by facet pattern with value
    \d{5}\.\d{13}.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-pattern-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-pattern-5-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalPattern5",
        version="1.0",
    )


def test_atomic_decimal_pattern_4_nistxml_sv_iv_atomic_decimal_pattern_5_2():
    r"""
    Type atomic/decimal is restricted by facet pattern with value
    \d{5}\.\d{13}.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-pattern-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-pattern-5-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalPattern5",
        version="1.0",
    )


def test_atomic_decimal_pattern_4_nistxml_sv_iv_atomic_decimal_pattern_5_3():
    r"""
    Type atomic/decimal is restricted by facet pattern with value
    \d{5}\.\d{13}.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-pattern-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-pattern-5-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalPattern5",
        version="1.0",
    )


def test_atomic_decimal_pattern_4_nistxml_sv_iv_atomic_decimal_pattern_5_4():
    r"""
    Type atomic/decimal is restricted by facet pattern with value
    \d{5}\.\d{13}.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-pattern-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-pattern-5-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalPattern5",
        version="1.0",
    )


def test_atomic_decimal_pattern_4_nistxml_sv_iv_atomic_decimal_pattern_5_5():
    r"""
    Type atomic/decimal is restricted by facet pattern with value
    \d{5}\.\d{13}.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-pattern-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-pattern-5-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalPattern5",
        version="1.0",
    )


@pytest.mark.xfail
def test_atomic_decimal_pattern_3_nistxml_sv_iv_atomic_decimal_pattern_4_1():
    r"""
    Type atomic/decimal is restricted by facet pattern with value
    \.\d{13}.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-pattern-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-pattern-4-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalPattern4",
        version="1.0",
    )


@pytest.mark.xfail
def test_atomic_decimal_pattern_3_nistxml_sv_iv_atomic_decimal_pattern_4_2():
    r"""
    Type atomic/decimal is restricted by facet pattern with value
    \.\d{13}.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-pattern-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-pattern-4-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalPattern4",
        version="1.0",
    )


@pytest.mark.xfail
def test_atomic_decimal_pattern_3_nistxml_sv_iv_atomic_decimal_pattern_4_3():
    r"""
    Type atomic/decimal is restricted by facet pattern with value
    \.\d{13}.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-pattern-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-pattern-4-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalPattern4",
        version="1.0",
    )


@pytest.mark.xfail
def test_atomic_decimal_pattern_3_nistxml_sv_iv_atomic_decimal_pattern_4_4():
    r"""
    Type atomic/decimal is restricted by facet pattern with value
    \.\d{13}.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-pattern-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-pattern-4-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalPattern4",
        version="1.0",
    )


@pytest.mark.xfail
def test_atomic_decimal_pattern_3_nistxml_sv_iv_atomic_decimal_pattern_4_5():
    r"""
    Type atomic/decimal is restricted by facet pattern with value
    \.\d{13}.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-pattern-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-pattern-4-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalPattern4",
        version="1.0",
    )


def test_atomic_decimal_pattern_2_nistxml_sv_iv_atomic_decimal_pattern_3_1():
    r"""
    Type atomic/decimal is restricted by facet pattern with value
    \-\d{1}\.\d{8}.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-pattern-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-pattern-3-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalPattern3",
        version="1.0",
    )


def test_atomic_decimal_pattern_2_nistxml_sv_iv_atomic_decimal_pattern_3_2():
    r"""
    Type atomic/decimal is restricted by facet pattern with value
    \-\d{1}\.\d{8}.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-pattern-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-pattern-3-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalPattern3",
        version="1.0",
    )


def test_atomic_decimal_pattern_2_nistxml_sv_iv_atomic_decimal_pattern_3_3():
    r"""
    Type atomic/decimal is restricted by facet pattern with value
    \-\d{1}\.\d{8}.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-pattern-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-pattern-3-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalPattern3",
        version="1.0",
    )


def test_atomic_decimal_pattern_2_nistxml_sv_iv_atomic_decimal_pattern_3_4():
    r"""
    Type atomic/decimal is restricted by facet pattern with value
    \-\d{1}\.\d{8}.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-pattern-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-pattern-3-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalPattern3",
        version="1.0",
    )


def test_atomic_decimal_pattern_2_nistxml_sv_iv_atomic_decimal_pattern_3_5():
    r"""
    Type atomic/decimal is restricted by facet pattern with value
    \-\d{1}\.\d{8}.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-pattern-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-pattern-3-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalPattern3",
        version="1.0",
    )


def test_atomic_decimal_pattern_1_nistxml_sv_iv_atomic_decimal_pattern_2_1():
    r"""
    Type atomic/decimal is restricted by facet pattern with value
    \-\d{2}\.\d{3}.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-pattern-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-pattern-2-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalPattern2",
        version="1.0",
    )


def test_atomic_decimal_pattern_1_nistxml_sv_iv_atomic_decimal_pattern_2_2():
    r"""
    Type atomic/decimal is restricted by facet pattern with value
    \-\d{2}\.\d{3}.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-pattern-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-pattern-2-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalPattern2",
        version="1.0",
    )


def test_atomic_decimal_pattern_1_nistxml_sv_iv_atomic_decimal_pattern_2_3():
    r"""
    Type atomic/decimal is restricted by facet pattern with value
    \-\d{2}\.\d{3}.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-pattern-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-pattern-2-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalPattern2",
        version="1.0",
    )


def test_atomic_decimal_pattern_1_nistxml_sv_iv_atomic_decimal_pattern_2_4():
    r"""
    Type atomic/decimal is restricted by facet pattern with value
    \-\d{2}\.\d{3}.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-pattern-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-pattern-2-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalPattern2",
        version="1.0",
    )


def test_atomic_decimal_pattern_1_nistxml_sv_iv_atomic_decimal_pattern_2_5():
    r"""
    Type atomic/decimal is restricted by facet pattern with value
    \-\d{2}\.\d{3}.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-pattern-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-pattern-2-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalPattern2",
        version="1.0",
    )


def test_atomic_decimal_pattern_nistxml_sv_iv_atomic_decimal_pattern_1_1():
    r"""
    Type atomic/decimal is restricted by facet pattern with value \d{1}.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-pattern-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-pattern-1-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalPattern1",
        version="1.0",
    )


def test_atomic_decimal_pattern_nistxml_sv_iv_atomic_decimal_pattern_1_2():
    r"""
    Type atomic/decimal is restricted by facet pattern with value \d{1}.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-pattern-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-pattern-1-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalPattern1",
        version="1.0",
    )


def test_atomic_decimal_pattern_nistxml_sv_iv_atomic_decimal_pattern_1_3():
    r"""
    Type atomic/decimal is restricted by facet pattern with value \d{1}.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-pattern-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-pattern-1-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalPattern1",
        version="1.0",
    )


def test_atomic_decimal_pattern_nistxml_sv_iv_atomic_decimal_pattern_1_4():
    r"""
    Type atomic/decimal is restricted by facet pattern with value \d{1}.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-pattern-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-pattern-1-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalPattern1",
        version="1.0",
    )


def test_atomic_decimal_pattern_nistxml_sv_iv_atomic_decimal_pattern_1_5():
    r"""
    Type atomic/decimal is restricted by facet pattern with value \d{1}.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-pattern-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-pattern-1-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalPattern1",
        version="1.0",
    )


def test_atomic_decimal_total_digits_4_nistxml_sv_iv_atomic_decimal_total_digits_5_1():
    """
    Type atomic/decimal is restricted by facet totalDigits with value 18.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-totalDigits-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-totalDigits-5-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalTotalDigits5",
        version="1.0",
    )


def test_atomic_decimal_total_digits_4_nistxml_sv_iv_atomic_decimal_total_digits_5_2():
    """
    Type atomic/decimal is restricted by facet totalDigits with value 18.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-totalDigits-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-totalDigits-5-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalTotalDigits5",
        version="1.0",
    )


def test_atomic_decimal_total_digits_4_nistxml_sv_iv_atomic_decimal_total_digits_5_3():
    """
    Type atomic/decimal is restricted by facet totalDigits with value 18.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-totalDigits-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-totalDigits-5-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalTotalDigits5",
        version="1.0",
    )


def test_atomic_decimal_total_digits_4_nistxml_sv_iv_atomic_decimal_total_digits_5_4():
    """
    Type atomic/decimal is restricted by facet totalDigits with value 18.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-totalDigits-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-totalDigits-5-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalTotalDigits5",
        version="1.0",
    )


def test_atomic_decimal_total_digits_4_nistxml_sv_iv_atomic_decimal_total_digits_5_5():
    """
    Type atomic/decimal is restricted by facet totalDigits with value 18.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-totalDigits-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-totalDigits-5-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalTotalDigits5",
        version="1.0",
    )


def test_atomic_decimal_total_digits_3_nistxml_sv_iv_atomic_decimal_total_digits_4_1():
    """
    Type atomic/decimal is restricted by facet totalDigits with value 13.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-totalDigits-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-totalDigits-4-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalTotalDigits4",
        version="1.0",
    )


def test_atomic_decimal_total_digits_3_nistxml_sv_iv_atomic_decimal_total_digits_4_2():
    """
    Type atomic/decimal is restricted by facet totalDigits with value 13.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-totalDigits-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-totalDigits-4-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalTotalDigits4",
        version="1.0",
    )


def test_atomic_decimal_total_digits_3_nistxml_sv_iv_atomic_decimal_total_digits_4_3():
    """
    Type atomic/decimal is restricted by facet totalDigits with value 13.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-totalDigits-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-totalDigits-4-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalTotalDigits4",
        version="1.0",
    )


def test_atomic_decimal_total_digits_3_nistxml_sv_iv_atomic_decimal_total_digits_4_4():
    """
    Type atomic/decimal is restricted by facet totalDigits with value 13.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-totalDigits-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-totalDigits-4-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalTotalDigits4",
        version="1.0",
    )


def test_atomic_decimal_total_digits_3_nistxml_sv_iv_atomic_decimal_total_digits_4_5():
    """
    Type atomic/decimal is restricted by facet totalDigits with value 13.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-totalDigits-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-totalDigits-4-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalTotalDigits4",
        version="1.0",
    )


def test_atomic_decimal_total_digits_2_nistxml_sv_iv_atomic_decimal_total_digits_3_1():
    """
    Type atomic/decimal is restricted by facet totalDigits with value 9.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-totalDigits-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-totalDigits-3-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalTotalDigits3",
        version="1.0",
    )


def test_atomic_decimal_total_digits_2_nistxml_sv_iv_atomic_decimal_total_digits_3_2():
    """
    Type atomic/decimal is restricted by facet totalDigits with value 9.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-totalDigits-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-totalDigits-3-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalTotalDigits3",
        version="1.0",
    )


def test_atomic_decimal_total_digits_2_nistxml_sv_iv_atomic_decimal_total_digits_3_3():
    """
    Type atomic/decimal is restricted by facet totalDigits with value 9.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-totalDigits-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-totalDigits-3-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalTotalDigits3",
        version="1.0",
    )


def test_atomic_decimal_total_digits_2_nistxml_sv_iv_atomic_decimal_total_digits_3_4():
    """
    Type atomic/decimal is restricted by facet totalDigits with value 9.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-totalDigits-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-totalDigits-3-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalTotalDigits3",
        version="1.0",
    )


def test_atomic_decimal_total_digits_2_nistxml_sv_iv_atomic_decimal_total_digits_3_5():
    """
    Type atomic/decimal is restricted by facet totalDigits with value 9.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-totalDigits-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-totalDigits-3-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalTotalDigits3",
        version="1.0",
    )


def test_atomic_decimal_total_digits_1_nistxml_sv_iv_atomic_decimal_total_digits_2_1():
    """
    Type atomic/decimal is restricted by facet totalDigits with value 5.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-totalDigits-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-totalDigits-2-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalTotalDigits2",
        version="1.0",
    )


def test_atomic_decimal_total_digits_1_nistxml_sv_iv_atomic_decimal_total_digits_2_2():
    """
    Type atomic/decimal is restricted by facet totalDigits with value 5.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-totalDigits-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-totalDigits-2-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalTotalDigits2",
        version="1.0",
    )


def test_atomic_decimal_total_digits_1_nistxml_sv_iv_atomic_decimal_total_digits_2_3():
    """
    Type atomic/decimal is restricted by facet totalDigits with value 5.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-totalDigits-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-totalDigits-2-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalTotalDigits2",
        version="1.0",
    )


def test_atomic_decimal_total_digits_1_nistxml_sv_iv_atomic_decimal_total_digits_2_4():
    """
    Type atomic/decimal is restricted by facet totalDigits with value 5.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-totalDigits-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-totalDigits-2-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalTotalDigits2",
        version="1.0",
    )


def test_atomic_decimal_total_digits_1_nistxml_sv_iv_atomic_decimal_total_digits_2_5():
    """
    Type atomic/decimal is restricted by facet totalDigits with value 5.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-totalDigits-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-totalDigits-2-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalTotalDigits2",
        version="1.0",
    )


def test_atomic_decimal_total_digits_nistxml_sv_iv_atomic_decimal_total_digits_1_1():
    """
    Type atomic/decimal is restricted by facet totalDigits with value 1.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-totalDigits-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-totalDigits-1-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalTotalDigits1",
        version="1.0",
    )


def test_atomic_decimal_total_digits_nistxml_sv_iv_atomic_decimal_total_digits_1_2():
    """
    Type atomic/decimal is restricted by facet totalDigits with value 1.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-totalDigits-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-totalDigits-1-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalTotalDigits1",
        version="1.0",
    )


def test_atomic_decimal_total_digits_nistxml_sv_iv_atomic_decimal_total_digits_1_3():
    """
    Type atomic/decimal is restricted by facet totalDigits with value 1.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-totalDigits-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-totalDigits-1-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalTotalDigits1",
        version="1.0",
    )


def test_atomic_decimal_total_digits_nistxml_sv_iv_atomic_decimal_total_digits_1_4():
    """
    Type atomic/decimal is restricted by facet totalDigits with value 1.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-totalDigits-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-totalDigits-1-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalTotalDigits1",
        version="1.0",
    )


def test_atomic_decimal_total_digits_nistxml_sv_iv_atomic_decimal_total_digits_1_5():
    """
    Type atomic/decimal is restricted by facet totalDigits with value 1.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-totalDigits-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-totalDigits-1-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalTotalDigits1",
        version="1.0",
    )


def test_atomic_decimal_fraction_digits_4_nistxml_sv_iv_atomic_decimal_fraction_digits_5_1():
    """
    Type atomic/decimal is restricted by facet fractionDigits with value
    18.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-fractionDigits-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-fractionDigits-5-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalFractionDigits5",
        version="1.0",
    )


def test_atomic_decimal_fraction_digits_4_nistxml_sv_iv_atomic_decimal_fraction_digits_5_2():
    """
    Type atomic/decimal is restricted by facet fractionDigits with value
    18.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-fractionDigits-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-fractionDigits-5-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalFractionDigits5",
        version="1.0",
    )


def test_atomic_decimal_fraction_digits_4_nistxml_sv_iv_atomic_decimal_fraction_digits_5_3():
    """
    Type atomic/decimal is restricted by facet fractionDigits with value
    18.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-fractionDigits-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-fractionDigits-5-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalFractionDigits5",
        version="1.0",
    )


def test_atomic_decimal_fraction_digits_4_nistxml_sv_iv_atomic_decimal_fraction_digits_5_4():
    """
    Type atomic/decimal is restricted by facet fractionDigits with value
    18.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-fractionDigits-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-fractionDigits-5-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalFractionDigits5",
        version="1.0",
    )


def test_atomic_decimal_fraction_digits_4_nistxml_sv_iv_atomic_decimal_fraction_digits_5_5():
    """
    Type atomic/decimal is restricted by facet fractionDigits with value
    18.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-fractionDigits-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-fractionDigits-5-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalFractionDigits5",
        version="1.0",
    )


def test_atomic_decimal_fraction_digits_3_nistxml_sv_iv_atomic_decimal_fraction_digits_4_1():
    """
    Type atomic/decimal is restricted by facet fractionDigits with value
    12.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-fractionDigits-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-fractionDigits-4-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalFractionDigits4",
        version="1.0",
    )


def test_atomic_decimal_fraction_digits_3_nistxml_sv_iv_atomic_decimal_fraction_digits_4_2():
    """
    Type atomic/decimal is restricted by facet fractionDigits with value
    12.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-fractionDigits-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-fractionDigits-4-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalFractionDigits4",
        version="1.0",
    )


def test_atomic_decimal_fraction_digits_3_nistxml_sv_iv_atomic_decimal_fraction_digits_4_3():
    """
    Type atomic/decimal is restricted by facet fractionDigits with value
    12.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-fractionDigits-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-fractionDigits-4-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalFractionDigits4",
        version="1.0",
    )


def test_atomic_decimal_fraction_digits_3_nistxml_sv_iv_atomic_decimal_fraction_digits_4_4():
    """
    Type atomic/decimal is restricted by facet fractionDigits with value
    12.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-fractionDigits-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-fractionDigits-4-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalFractionDigits4",
        version="1.0",
    )


def test_atomic_decimal_fraction_digits_3_nistxml_sv_iv_atomic_decimal_fraction_digits_4_5():
    """
    Type atomic/decimal is restricted by facet fractionDigits with value
    12.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-fractionDigits-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-fractionDigits-4-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalFractionDigits4",
        version="1.0",
    )


def test_atomic_decimal_fraction_digits_2_nistxml_sv_iv_atomic_decimal_fraction_digits_3_1():
    """
    Type atomic/decimal is restricted by facet fractionDigits with value
    8.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-fractionDigits-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-fractionDigits-3-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalFractionDigits3",
        version="1.0",
    )


def test_atomic_decimal_fraction_digits_2_nistxml_sv_iv_atomic_decimal_fraction_digits_3_2():
    """
    Type atomic/decimal is restricted by facet fractionDigits with value
    8.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-fractionDigits-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-fractionDigits-3-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalFractionDigits3",
        version="1.0",
    )


def test_atomic_decimal_fraction_digits_2_nistxml_sv_iv_atomic_decimal_fraction_digits_3_3():
    """
    Type atomic/decimal is restricted by facet fractionDigits with value
    8.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-fractionDigits-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-fractionDigits-3-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalFractionDigits3",
        version="1.0",
    )


def test_atomic_decimal_fraction_digits_2_nistxml_sv_iv_atomic_decimal_fraction_digits_3_4():
    """
    Type atomic/decimal is restricted by facet fractionDigits with value
    8.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-fractionDigits-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-fractionDigits-3-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalFractionDigits3",
        version="1.0",
    )


def test_atomic_decimal_fraction_digits_2_nistxml_sv_iv_atomic_decimal_fraction_digits_3_5():
    """
    Type atomic/decimal is restricted by facet fractionDigits with value
    8.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-fractionDigits-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-fractionDigits-3-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalFractionDigits3",
        version="1.0",
    )


def test_atomic_decimal_fraction_digits_1_nistxml_sv_iv_atomic_decimal_fraction_digits_2_1():
    """
    Type atomic/decimal is restricted by facet fractionDigits with value
    4.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-fractionDigits-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-fractionDigits-2-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalFractionDigits2",
        version="1.0",
    )


def test_atomic_decimal_fraction_digits_1_nistxml_sv_iv_atomic_decimal_fraction_digits_2_2():
    """
    Type atomic/decimal is restricted by facet fractionDigits with value
    4.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-fractionDigits-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-fractionDigits-2-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalFractionDigits2",
        version="1.0",
    )


def test_atomic_decimal_fraction_digits_1_nistxml_sv_iv_atomic_decimal_fraction_digits_2_3():
    """
    Type atomic/decimal is restricted by facet fractionDigits with value
    4.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-fractionDigits-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-fractionDigits-2-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalFractionDigits2",
        version="1.0",
    )


def test_atomic_decimal_fraction_digits_1_nistxml_sv_iv_atomic_decimal_fraction_digits_2_4():
    """
    Type atomic/decimal is restricted by facet fractionDigits with value
    4.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-fractionDigits-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-fractionDigits-2-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalFractionDigits2",
        version="1.0",
    )


def test_atomic_decimal_fraction_digits_1_nistxml_sv_iv_atomic_decimal_fraction_digits_2_5():
    """
    Type atomic/decimal is restricted by facet fractionDigits with value
    4.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-fractionDigits-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-fractionDigits-2-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalFractionDigits2",
        version="1.0",
    )


def test_atomic_decimal_fraction_digits_nistxml_sv_iv_atomic_decimal_fraction_digits_1_1():
    """
    Type atomic/decimal is restricted by facet fractionDigits with value
    0.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-fractionDigits-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-fractionDigits-1-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalFractionDigits1",
        version="1.0",
    )


def test_atomic_decimal_fraction_digits_nistxml_sv_iv_atomic_decimal_fraction_digits_1_2():
    """
    Type atomic/decimal is restricted by facet fractionDigits with value
    0.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-fractionDigits-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-fractionDigits-1-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalFractionDigits1",
        version="1.0",
    )


def test_atomic_decimal_fraction_digits_nistxml_sv_iv_atomic_decimal_fraction_digits_1_3():
    """
    Type atomic/decimal is restricted by facet fractionDigits with value
    0.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-fractionDigits-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-fractionDigits-1-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalFractionDigits1",
        version="1.0",
    )


def test_atomic_decimal_fraction_digits_nistxml_sv_iv_atomic_decimal_fraction_digits_1_4():
    """
    Type atomic/decimal is restricted by facet fractionDigits with value
    0.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-fractionDigits-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-fractionDigits-1-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalFractionDigits1",
        version="1.0",
    )


def test_atomic_decimal_fraction_digits_nistxml_sv_iv_atomic_decimal_fraction_digits_1_5():
    """
    Type atomic/decimal is restricted by facet fractionDigits with value
    0.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-fractionDigits-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-fractionDigits-1-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalFractionDigits1",
        version="1.0",
    )


def test_atomic_decimal_max_inclusive_4_nistxml_sv_iv_atomic_decimal_max_inclusive_5_1():
    """
    Type atomic/decimal is restricted by facet maxInclusive with value
    999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxInclusive-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxInclusive-5-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxInclusive5",
        version="1.0",
    )


def test_atomic_decimal_max_inclusive_4_nistxml_sv_iv_atomic_decimal_max_inclusive_5_2():
    """
    Type atomic/decimal is restricted by facet maxInclusive with value
    999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxInclusive-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxInclusive-5-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxInclusive5",
        version="1.0",
    )


def test_atomic_decimal_max_inclusive_4_nistxml_sv_iv_atomic_decimal_max_inclusive_5_3():
    """
    Type atomic/decimal is restricted by facet maxInclusive with value
    999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxInclusive-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxInclusive-5-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxInclusive5",
        version="1.0",
    )


def test_atomic_decimal_max_inclusive_4_nistxml_sv_iv_atomic_decimal_max_inclusive_5_4():
    """
    Type atomic/decimal is restricted by facet maxInclusive with value
    999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxInclusive-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxInclusive-5-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxInclusive5",
        version="1.0",
    )


def test_atomic_decimal_max_inclusive_4_nistxml_sv_iv_atomic_decimal_max_inclusive_5_5():
    """
    Type atomic/decimal is restricted by facet maxInclusive with value
    999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxInclusive-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxInclusive-5-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxInclusive5",
        version="1.0",
    )


def test_atomic_decimal_max_inclusive_3_nistxml_sv_iv_atomic_decimal_max_inclusive_4_1():
    """
    Type atomic/decimal is restricted by facet maxInclusive with value
    -95776055693671313.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxInclusive-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxInclusive-4-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxInclusive4",
        version="1.0",
    )


def test_atomic_decimal_max_inclusive_3_nistxml_sv_iv_atomic_decimal_max_inclusive_4_2():
    """
    Type atomic/decimal is restricted by facet maxInclusive with value
    -95776055693671313.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxInclusive-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxInclusive-4-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxInclusive4",
        version="1.0",
    )


def test_atomic_decimal_max_inclusive_3_nistxml_sv_iv_atomic_decimal_max_inclusive_4_3():
    """
    Type atomic/decimal is restricted by facet maxInclusive with value
    -95776055693671313.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxInclusive-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxInclusive-4-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxInclusive4",
        version="1.0",
    )


def test_atomic_decimal_max_inclusive_3_nistxml_sv_iv_atomic_decimal_max_inclusive_4_4():
    """
    Type atomic/decimal is restricted by facet maxInclusive with value
    -95776055693671313.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxInclusive-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxInclusive-4-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxInclusive4",
        version="1.0",
    )


def test_atomic_decimal_max_inclusive_3_nistxml_sv_iv_atomic_decimal_max_inclusive_4_5():
    """
    Type atomic/decimal is restricted by facet maxInclusive with value
    -95776055693671313.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxInclusive-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxInclusive-4-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxInclusive4",
        version="1.0",
    )


def test_atomic_decimal_max_inclusive_2_nistxml_sv_iv_atomic_decimal_max_inclusive_3_1():
    """
    Type atomic/decimal is restricted by facet maxInclusive with value
    -888403528420030673.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxInclusive-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxInclusive-3-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxInclusive3",
        version="1.0",
    )


def test_atomic_decimal_max_inclusive_2_nistxml_sv_iv_atomic_decimal_max_inclusive_3_2():
    """
    Type atomic/decimal is restricted by facet maxInclusive with value
    -888403528420030673.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxInclusive-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxInclusive-3-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxInclusive3",
        version="1.0",
    )


def test_atomic_decimal_max_inclusive_2_nistxml_sv_iv_atomic_decimal_max_inclusive_3_3():
    """
    Type atomic/decimal is restricted by facet maxInclusive with value
    -888403528420030673.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxInclusive-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxInclusive-3-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxInclusive3",
        version="1.0",
    )


def test_atomic_decimal_max_inclusive_2_nistxml_sv_iv_atomic_decimal_max_inclusive_3_4():
    """
    Type atomic/decimal is restricted by facet maxInclusive with value
    -888403528420030673.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxInclusive-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxInclusive-3-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxInclusive3",
        version="1.0",
    )


def test_atomic_decimal_max_inclusive_2_nistxml_sv_iv_atomic_decimal_max_inclusive_3_5():
    """
    Type atomic/decimal is restricted by facet maxInclusive with value
    -888403528420030673.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxInclusive-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxInclusive-3-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxInclusive3",
        version="1.0",
    )


def test_atomic_decimal_max_inclusive_1_nistxml_sv_iv_atomic_decimal_max_inclusive_2_1():
    """
    Type atomic/decimal is restricted by facet maxInclusive with value
    625897845365533055.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxInclusive-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxInclusive-2-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxInclusive2",
        version="1.0",
    )


def test_atomic_decimal_max_inclusive_1_nistxml_sv_iv_atomic_decimal_max_inclusive_2_2():
    """
    Type atomic/decimal is restricted by facet maxInclusive with value
    625897845365533055.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxInclusive-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxInclusive-2-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxInclusive2",
        version="1.0",
    )


def test_atomic_decimal_max_inclusive_1_nistxml_sv_iv_atomic_decimal_max_inclusive_2_3():
    """
    Type atomic/decimal is restricted by facet maxInclusive with value
    625897845365533055.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxInclusive-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxInclusive-2-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxInclusive2",
        version="1.0",
    )


def test_atomic_decimal_max_inclusive_1_nistxml_sv_iv_atomic_decimal_max_inclusive_2_4():
    """
    Type atomic/decimal is restricted by facet maxInclusive with value
    625897845365533055.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxInclusive-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxInclusive-2-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxInclusive2",
        version="1.0",
    )


def test_atomic_decimal_max_inclusive_1_nistxml_sv_iv_atomic_decimal_max_inclusive_2_5():
    """
    Type atomic/decimal is restricted by facet maxInclusive with value
    625897845365533055.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxInclusive-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxInclusive-2-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxInclusive2",
        version="1.0",
    )


def test_atomic_decimal_max_inclusive_nistxml_sv_iv_atomic_decimal_max_inclusive_1_1():
    """
    Type atomic/decimal is restricted by facet maxInclusive with value
    -999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxInclusive-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxInclusive-1-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxInclusive1",
        version="1.0",
    )


def test_atomic_decimal_max_exclusive_4_nistxml_sv_iv_atomic_decimal_max_exclusive_5_1():
    """
    Type atomic/decimal is restricted by facet maxExclusive with value
    999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxExclusive-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxExclusive-5-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxExclusive5",
        version="1.0",
    )


def test_atomic_decimal_max_exclusive_4_nistxml_sv_iv_atomic_decimal_max_exclusive_5_2():
    """
    Type atomic/decimal is restricted by facet maxExclusive with value
    999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxExclusive-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxExclusive-5-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxExclusive5",
        version="1.0",
    )


def test_atomic_decimal_max_exclusive_4_nistxml_sv_iv_atomic_decimal_max_exclusive_5_3():
    """
    Type atomic/decimal is restricted by facet maxExclusive with value
    999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxExclusive-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxExclusive-5-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxExclusive5",
        version="1.0",
    )


def test_atomic_decimal_max_exclusive_4_nistxml_sv_iv_atomic_decimal_max_exclusive_5_4():
    """
    Type atomic/decimal is restricted by facet maxExclusive with value
    999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxExclusive-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxExclusive-5-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxExclusive5",
        version="1.0",
    )


def test_atomic_decimal_max_exclusive_4_nistxml_sv_iv_atomic_decimal_max_exclusive_5_5():
    """
    Type atomic/decimal is restricted by facet maxExclusive with value
    999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxExclusive-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxExclusive-5-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxExclusive5",
        version="1.0",
    )


def test_atomic_decimal_max_exclusive_3_nistxml_sv_iv_atomic_decimal_max_exclusive_4_1():
    """
    Type atomic/decimal is restricted by facet maxExclusive with value
    -214771926190724381.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxExclusive-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxExclusive-4-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxExclusive4",
        version="1.0",
    )


def test_atomic_decimal_max_exclusive_3_nistxml_sv_iv_atomic_decimal_max_exclusive_4_2():
    """
    Type atomic/decimal is restricted by facet maxExclusive with value
    -214771926190724381.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxExclusive-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxExclusive-4-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxExclusive4",
        version="1.0",
    )


def test_atomic_decimal_max_exclusive_3_nistxml_sv_iv_atomic_decimal_max_exclusive_4_3():
    """
    Type atomic/decimal is restricted by facet maxExclusive with value
    -214771926190724381.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxExclusive-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxExclusive-4-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxExclusive4",
        version="1.0",
    )


def test_atomic_decimal_max_exclusive_3_nistxml_sv_iv_atomic_decimal_max_exclusive_4_4():
    """
    Type atomic/decimal is restricted by facet maxExclusive with value
    -214771926190724381.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxExclusive-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxExclusive-4-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxExclusive4",
        version="1.0",
    )


def test_atomic_decimal_max_exclusive_3_nistxml_sv_iv_atomic_decimal_max_exclusive_4_5():
    """
    Type atomic/decimal is restricted by facet maxExclusive with value
    -214771926190724381.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxExclusive-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxExclusive-4-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxExclusive4",
        version="1.0",
    )


def test_atomic_decimal_max_exclusive_2_nistxml_sv_iv_atomic_decimal_max_exclusive_3_1():
    """
    Type atomic/decimal is restricted by facet maxExclusive with value
    171942968603657986.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxExclusive-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxExclusive-3-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxExclusive3",
        version="1.0",
    )


def test_atomic_decimal_max_exclusive_2_nistxml_sv_iv_atomic_decimal_max_exclusive_3_2():
    """
    Type atomic/decimal is restricted by facet maxExclusive with value
    171942968603657986.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxExclusive-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxExclusive-3-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxExclusive3",
        version="1.0",
    )


def test_atomic_decimal_max_exclusive_2_nistxml_sv_iv_atomic_decimal_max_exclusive_3_3():
    """
    Type atomic/decimal is restricted by facet maxExclusive with value
    171942968603657986.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxExclusive-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxExclusive-3-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxExclusive3",
        version="1.0",
    )


def test_atomic_decimal_max_exclusive_2_nistxml_sv_iv_atomic_decimal_max_exclusive_3_4():
    """
    Type atomic/decimal is restricted by facet maxExclusive with value
    171942968603657986.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxExclusive-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxExclusive-3-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxExclusive3",
        version="1.0",
    )


def test_atomic_decimal_max_exclusive_2_nistxml_sv_iv_atomic_decimal_max_exclusive_3_5():
    """
    Type atomic/decimal is restricted by facet maxExclusive with value
    171942968603657986.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxExclusive-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxExclusive-3-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxExclusive3",
        version="1.0",
    )


def test_atomic_decimal_max_exclusive_1_nistxml_sv_iv_atomic_decimal_max_exclusive_2_1():
    """
    Type atomic/decimal is restricted by facet maxExclusive with value
    78119693427168402.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxExclusive-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxExclusive-2-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxExclusive2",
        version="1.0",
    )


def test_atomic_decimal_max_exclusive_1_nistxml_sv_iv_atomic_decimal_max_exclusive_2_2():
    """
    Type atomic/decimal is restricted by facet maxExclusive with value
    78119693427168402.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxExclusive-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxExclusive-2-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxExclusive2",
        version="1.0",
    )


def test_atomic_decimal_max_exclusive_1_nistxml_sv_iv_atomic_decimal_max_exclusive_2_3():
    """
    Type atomic/decimal is restricted by facet maxExclusive with value
    78119693427168402.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxExclusive-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxExclusive-2-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxExclusive2",
        version="1.0",
    )


def test_atomic_decimal_max_exclusive_1_nistxml_sv_iv_atomic_decimal_max_exclusive_2_4():
    """
    Type atomic/decimal is restricted by facet maxExclusive with value
    78119693427168402.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxExclusive-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxExclusive-2-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxExclusive2",
        version="1.0",
    )


def test_atomic_decimal_max_exclusive_1_nistxml_sv_iv_atomic_decimal_max_exclusive_2_5():
    """
    Type atomic/decimal is restricted by facet maxExclusive with value
    78119693427168402.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxExclusive-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxExclusive-2-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxExclusive2",
        version="1.0",
    )


def test_atomic_decimal_max_exclusive_nistxml_sv_iv_atomic_decimal_max_exclusive_1_1():
    """
    Type atomic/decimal is restricted by facet maxExclusive with value
    -999999999999999998.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-maxExclusive-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-maxExclusive-1-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMaxExclusive1",
        version="1.0",
    )


def test_atomic_decimal_min_inclusive_4_nistxml_sv_iv_atomic_decimal_min_inclusive_5_1():
    """
    Type atomic/decimal is restricted by facet minInclusive with value
    999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minInclusive-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minInclusive-5-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinInclusive5",
        version="1.0",
    )


def test_atomic_decimal_min_inclusive_3_nistxml_sv_iv_atomic_decimal_min_inclusive_4_1():
    """
    Type atomic/decimal is restricted by facet minInclusive with value
    325207740352921658.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minInclusive-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minInclusive-4-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinInclusive4",
        version="1.0",
    )


def test_atomic_decimal_min_inclusive_3_nistxml_sv_iv_atomic_decimal_min_inclusive_4_2():
    """
    Type atomic/decimal is restricted by facet minInclusive with value
    325207740352921658.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minInclusive-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minInclusive-4-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinInclusive4",
        version="1.0",
    )


def test_atomic_decimal_min_inclusive_3_nistxml_sv_iv_atomic_decimal_min_inclusive_4_3():
    """
    Type atomic/decimal is restricted by facet minInclusive with value
    325207740352921658.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minInclusive-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minInclusive-4-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinInclusive4",
        version="1.0",
    )


def test_atomic_decimal_min_inclusive_3_nistxml_sv_iv_atomic_decimal_min_inclusive_4_4():
    """
    Type atomic/decimal is restricted by facet minInclusive with value
    325207740352921658.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minInclusive-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minInclusive-4-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinInclusive4",
        version="1.0",
    )


def test_atomic_decimal_min_inclusive_3_nistxml_sv_iv_atomic_decimal_min_inclusive_4_5():
    """
    Type atomic/decimal is restricted by facet minInclusive with value
    325207740352921658.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minInclusive-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minInclusive-4-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinInclusive4",
        version="1.0",
    )


def test_atomic_decimal_min_inclusive_2_nistxml_sv_iv_atomic_decimal_min_inclusive_3_1():
    """
    Type atomic/decimal is restricted by facet minInclusive with value
    -785368448026986020.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minInclusive-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minInclusive-3-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinInclusive3",
        version="1.0",
    )


def test_atomic_decimal_min_inclusive_2_nistxml_sv_iv_atomic_decimal_min_inclusive_3_2():
    """
    Type atomic/decimal is restricted by facet minInclusive with value
    -785368448026986020.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minInclusive-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minInclusive-3-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinInclusive3",
        version="1.0",
    )


def test_atomic_decimal_min_inclusive_2_nistxml_sv_iv_atomic_decimal_min_inclusive_3_3():
    """
    Type atomic/decimal is restricted by facet minInclusive with value
    -785368448026986020.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minInclusive-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minInclusive-3-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinInclusive3",
        version="1.0",
    )


def test_atomic_decimal_min_inclusive_2_nistxml_sv_iv_atomic_decimal_min_inclusive_3_4():
    """
    Type atomic/decimal is restricted by facet minInclusive with value
    -785368448026986020.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minInclusive-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minInclusive-3-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinInclusive3",
        version="1.0",
    )


def test_atomic_decimal_min_inclusive_2_nistxml_sv_iv_atomic_decimal_min_inclusive_3_5():
    """
    Type atomic/decimal is restricted by facet minInclusive with value
    -785368448026986020.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minInclusive-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minInclusive-3-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinInclusive3",
        version="1.0",
    )


def test_atomic_decimal_min_inclusive_1_nistxml_sv_iv_atomic_decimal_min_inclusive_2_1():
    """
    Type atomic/decimal is restricted by facet minInclusive with value
    229822855408968073.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minInclusive-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minInclusive-2-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinInclusive2",
        version="1.0",
    )


def test_atomic_decimal_min_inclusive_1_nistxml_sv_iv_atomic_decimal_min_inclusive_2_2():
    """
    Type atomic/decimal is restricted by facet minInclusive with value
    229822855408968073.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minInclusive-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minInclusive-2-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinInclusive2",
        version="1.0",
    )


def test_atomic_decimal_min_inclusive_1_nistxml_sv_iv_atomic_decimal_min_inclusive_2_3():
    """
    Type atomic/decimal is restricted by facet minInclusive with value
    229822855408968073.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minInclusive-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minInclusive-2-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinInclusive2",
        version="1.0",
    )


def test_atomic_decimal_min_inclusive_1_nistxml_sv_iv_atomic_decimal_min_inclusive_2_4():
    """
    Type atomic/decimal is restricted by facet minInclusive with value
    229822855408968073.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minInclusive-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minInclusive-2-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinInclusive2",
        version="1.0",
    )


def test_atomic_decimal_min_inclusive_1_nistxml_sv_iv_atomic_decimal_min_inclusive_2_5():
    """
    Type atomic/decimal is restricted by facet minInclusive with value
    229822855408968073.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minInclusive-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minInclusive-2-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinInclusive2",
        version="1.0",
    )


def test_atomic_decimal_min_inclusive_nistxml_sv_iv_atomic_decimal_min_inclusive_1_1():
    """
    Type atomic/decimal is restricted by facet minInclusive with value
    -999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minInclusive-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minInclusive-1-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinInclusive1",
        version="1.0",
    )


def test_atomic_decimal_min_inclusive_nistxml_sv_iv_atomic_decimal_min_inclusive_1_2():
    """
    Type atomic/decimal is restricted by facet minInclusive with value
    -999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minInclusive-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minInclusive-1-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinInclusive1",
        version="1.0",
    )


def test_atomic_decimal_min_inclusive_nistxml_sv_iv_atomic_decimal_min_inclusive_1_3():
    """
    Type atomic/decimal is restricted by facet minInclusive with value
    -999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minInclusive-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minInclusive-1-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinInclusive1",
        version="1.0",
    )


def test_atomic_decimal_min_inclusive_nistxml_sv_iv_atomic_decimal_min_inclusive_1_4():
    """
    Type atomic/decimal is restricted by facet minInclusive with value
    -999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minInclusive-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minInclusive-1-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinInclusive1",
        version="1.0",
    )


def test_atomic_decimal_min_inclusive_nistxml_sv_iv_atomic_decimal_min_inclusive_1_5():
    """
    Type atomic/decimal is restricted by facet minInclusive with value
    -999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minInclusive-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minInclusive-1-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinInclusive1",
        version="1.0",
    )


def test_atomic_decimal_min_exclusive_4_nistxml_sv_iv_atomic_decimal_min_exclusive_5_1():
    """
    Type atomic/decimal is restricted by facet minExclusive with value
    999999999999999998.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minExclusive-5.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minExclusive-5-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinExclusive5",
        version="1.0",
    )


def test_atomic_decimal_min_exclusive_3_nistxml_sv_iv_atomic_decimal_min_exclusive_4_1():
    """
    Type atomic/decimal is restricted by facet minExclusive with value
    -294253147230818967.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minExclusive-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minExclusive-4-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinExclusive4",
        version="1.0",
    )


def test_atomic_decimal_min_exclusive_3_nistxml_sv_iv_atomic_decimal_min_exclusive_4_2():
    """
    Type atomic/decimal is restricted by facet minExclusive with value
    -294253147230818967.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minExclusive-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minExclusive-4-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinExclusive4",
        version="1.0",
    )


def test_atomic_decimal_min_exclusive_3_nistxml_sv_iv_atomic_decimal_min_exclusive_4_3():
    """
    Type atomic/decimal is restricted by facet minExclusive with value
    -294253147230818967.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minExclusive-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minExclusive-4-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinExclusive4",
        version="1.0",
    )


def test_atomic_decimal_min_exclusive_3_nistxml_sv_iv_atomic_decimal_min_exclusive_4_4():
    """
    Type atomic/decimal is restricted by facet minExclusive with value
    -294253147230818967.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minExclusive-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minExclusive-4-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinExclusive4",
        version="1.0",
    )


def test_atomic_decimal_min_exclusive_3_nistxml_sv_iv_atomic_decimal_min_exclusive_4_5():
    """
    Type atomic/decimal is restricted by facet minExclusive with value
    -294253147230818967.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minExclusive-4.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minExclusive-4-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinExclusive4",
        version="1.0",
    )


def test_atomic_decimal_min_exclusive_2_nistxml_sv_iv_atomic_decimal_min_exclusive_3_1():
    """
    Type atomic/decimal is restricted by facet minExclusive with value
    -67428259604688900.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minExclusive-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minExclusive-3-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinExclusive3",
        version="1.0",
    )


def test_atomic_decimal_min_exclusive_2_nistxml_sv_iv_atomic_decimal_min_exclusive_3_2():
    """
    Type atomic/decimal is restricted by facet minExclusive with value
    -67428259604688900.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minExclusive-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minExclusive-3-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinExclusive3",
        version="1.0",
    )


def test_atomic_decimal_min_exclusive_2_nistxml_sv_iv_atomic_decimal_min_exclusive_3_3():
    """
    Type atomic/decimal is restricted by facet minExclusive with value
    -67428259604688900.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minExclusive-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minExclusive-3-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinExclusive3",
        version="1.0",
    )


def test_atomic_decimal_min_exclusive_2_nistxml_sv_iv_atomic_decimal_min_exclusive_3_4():
    """
    Type atomic/decimal is restricted by facet minExclusive with value
    -67428259604688900.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minExclusive-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minExclusive-3-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinExclusive3",
        version="1.0",
    )


def test_atomic_decimal_min_exclusive_2_nistxml_sv_iv_atomic_decimal_min_exclusive_3_5():
    """
    Type atomic/decimal is restricted by facet minExclusive with value
    -67428259604688900.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minExclusive-3.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minExclusive-3-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinExclusive3",
        version="1.0",
    )


def test_atomic_decimal_min_exclusive_1_nistxml_sv_iv_atomic_decimal_min_exclusive_2_1():
    """
    Type atomic/decimal is restricted by facet minExclusive with value
    631308414640570968.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minExclusive-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minExclusive-2-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinExclusive2",
        version="1.0",
    )


def test_atomic_decimal_min_exclusive_1_nistxml_sv_iv_atomic_decimal_min_exclusive_2_2():
    """
    Type atomic/decimal is restricted by facet minExclusive with value
    631308414640570968.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minExclusive-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minExclusive-2-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinExclusive2",
        version="1.0",
    )


def test_atomic_decimal_min_exclusive_1_nistxml_sv_iv_atomic_decimal_min_exclusive_2_3():
    """
    Type atomic/decimal is restricted by facet minExclusive with value
    631308414640570968.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minExclusive-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minExclusive-2-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinExclusive2",
        version="1.0",
    )


def test_atomic_decimal_min_exclusive_1_nistxml_sv_iv_atomic_decimal_min_exclusive_2_4():
    """
    Type atomic/decimal is restricted by facet minExclusive with value
    631308414640570968.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minExclusive-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minExclusive-2-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinExclusive2",
        version="1.0",
    )


def test_atomic_decimal_min_exclusive_1_nistxml_sv_iv_atomic_decimal_min_exclusive_2_5():
    """
    Type atomic/decimal is restricted by facet minExclusive with value
    631308414640570968.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minExclusive-2.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minExclusive-2-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinExclusive2",
        version="1.0",
    )


def test_atomic_decimal_min_exclusive_nistxml_sv_iv_atomic_decimal_min_exclusive_1_1():
    """
    Type atomic/decimal is restricted by facet minExclusive with value
    -999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minExclusive-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minExclusive-1-1.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinExclusive1",
        version="1.0",
    )


def test_atomic_decimal_min_exclusive_nistxml_sv_iv_atomic_decimal_min_exclusive_1_2():
    """
    Type atomic/decimal is restricted by facet minExclusive with value
    -999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minExclusive-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minExclusive-1-2.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinExclusive1",
        version="1.0",
    )


def test_atomic_decimal_min_exclusive_nistxml_sv_iv_atomic_decimal_min_exclusive_1_3():
    """
    Type atomic/decimal is restricted by facet minExclusive with value
    -999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minExclusive-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minExclusive-1-3.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinExclusive1",
        version="1.0",
    )


def test_atomic_decimal_min_exclusive_nistxml_sv_iv_atomic_decimal_min_exclusive_1_4():
    """
    Type atomic/decimal is restricted by facet minExclusive with value
    -999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minExclusive-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minExclusive-1-4.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinExclusive1",
        version="1.0",
    )


def test_atomic_decimal_min_exclusive_nistxml_sv_iv_atomic_decimal_min_exclusive_1_5():
    """
    Type atomic/decimal is restricted by facet minExclusive with value
    -999999999999999999.
    """
    assert_bindings(
        schema="nistData/atomic/decimal/Schema+Instance/NISTSchema-SV-IV-atomic-decimal-minExclusive-1.xsd",
        is_valid=True,
        instance="nistData/atomic/decimal/Schema+Instance/NISTXML-SV-IV-atomic-decimal-minExclusive-1-5.xml",
        instance_is_valid=True,
        class_name="NistschemaSvIvAtomicDecimalMinExclusive1",
        version="1.0",
    )
