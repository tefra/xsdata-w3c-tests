from tests.utils import assert_bindings


def test_all314_all314_v01_xml(mode, save_output, output_format):
    """
    All model group derived by extension from another all model group,
    both minOccurs="0" Allowed in 1.1. Test case from Priscilla Walmsley
    """
    assert_bindings(
        schema="saxonData/All/all314.xsd",
        instance="saxonData/All/all314.v01.xml",
        class_name="Product",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_all314_all314_v02_xml(mode, save_output, output_format):
    """
    All model group derived by extension from another all model group,
    both minOccurs="0" Allowed in 1.1. Test case from Priscilla Walmsley
    """
    assert_bindings(
        schema="saxonData/All/all314.xsd",
        instance="saxonData/All/all314.v02.xml",
        class_name="Product",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_all314_all314_v05_xml(mode, save_output, output_format):
    """
    All model group derived by extension from another all model group,
    both minOccurs="0" Allowed in 1.1. Test case from Priscilla Walmsley
    """
    assert_bindings(
        schema="saxonData/All/all314.xsd",
        instance="saxonData/All/all314.v05.xml",
        class_name="Product",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_all306_all306_v01_xml(mode, save_output, output_format):
    """
    All model group derived by extension from another all model group;
    mixed="true" in extension. Allowed in 1.1
    """
    assert_bindings(
        schema="saxonData/All/all306.xsd",
        instance="saxonData/All/all306.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_all304_all304_v01_xml(mode, save_output, output_format):
    """
    All model group derived by extension from another all model group
    Allowed in 1.1
    """
    assert_bindings(
        schema="saxonData/All/all304.xsd",
        instance="saxonData/All/all304.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_all301_all301_v01_xml(mode, save_output, output_format):
    """
    All model group derived by extension from another all model group
    Allowed in 1.1
    """
    assert_bindings(
        schema="saxonData/All/all301.xsd",
        instance="saxonData/All/all301.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_all007_all007_v01_xml(mode, save_output, output_format):
    """
    All model group with a nested xs:group reference All model group with
    with a nested xs:group reference (otherwise same as all001)
    """
    assert_bindings(
        schema="saxonData/All/all007.xsd",
        instance="saxonData/All/all001.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_all006_all006_v01_xml(mode, save_output, output_format):
    """
    All model group, test on children Test that each child of an all group
    is validated against the right type
    """
    assert_bindings(
        schema="saxonData/All/all006.xsd",
        instance="saxonData/All/all006.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_all005_all005_v01_xml(mode, save_output, output_format):
    """
    All model group with two xs:any wildcards Test cases matching and non-
    matching wildcards
    """
    assert_bindings(
        schema="saxonData/All/all005.xsd",
        instance="saxonData/All/all005.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_all004_all004_v01_xml(mode, save_output, output_format):
    """
    All model group with nillable="true" Test cases involving
    xsi:nil="true" or "false"
    """
    assert_bindings(
        schema="saxonData/All/all004.xsd",
        instance="saxonData/All/all004.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_all004_all004_v02_xml(mode, save_output, output_format):
    """
    All model group with nillable="true" Test cases involving
    xsi:nil="true" or "false"
    """
    assert_bindings(
        schema="saxonData/All/all004.xsd",
        instance="saxonData/All/all004.v02.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_all003_all003_v01_xml(mode, save_output, output_format):
    """
    All model group with mixed content with extended minOccurs and
    maxOccurs values All model group with mixed content with extended
    minOccurs and maxOccurs values
    """
    assert_bindings(
        schema="saxonData/All/all003.xsd",
        instance="saxonData/All/all003.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_all003_all003_v02_xml(mode, save_output, output_format):
    """
    All model group with mixed content with extended minOccurs and
    maxOccurs values All model group with mixed content with extended
    minOccurs and maxOccurs values
    """
    assert_bindings(
        schema="saxonData/All/all003.xsd",
        instance="saxonData/All/all003.v02.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_all003_all003_v03_xml(mode, save_output, output_format):
    """
    All model group with mixed content with extended minOccurs and
    maxOccurs values All model group with mixed content with extended
    minOccurs and maxOccurs values
    """
    assert_bindings(
        schema="saxonData/All/all003.xsd",
        instance="saxonData/All/all003.v03.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_all002_all002_v01_xml(mode, save_output, output_format):
    """
    All model group with substitution groups All model group with extended
    minOccurs and maxOccurs values
    """
    assert_bindings(
        schema="saxonData/All/all002.xsd",
        instance="saxonData/All/all002.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_all001_all001_v01_xml(mode, save_output, output_format):
    """
    All model group with extended minOccurs and maxOccurs values All model
    group with extended minOccurs and maxOccurs values
    """
    assert_bindings(
        schema="saxonData/All/all001.xsd",
        instance="saxonData/All/all001.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert_simple006_assert_simple006_v1_xml(mode, save_output, output_format):
    """
    Assertion on a simple type with variety union Assertion on a simple
    type: $value contains the typed value
    """
    assert_bindings(
        schema="saxonData/Assert/assert-simple006.xsd",
        instance="saxonData/Assert/assert-simple006.v1.xml",
        class_name="Outer",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert_simple005_assert_simple005_v1_xml(mode, save_output, output_format):
    """
    Assertion on a simple type with variety list Assertion on a simple
    type: $value contains the typed value
    """
    assert_bindings(
        schema="saxonData/Assert/assert-simple005.xsd",
        instance="saxonData/Assert/assert-simple005.v1.xml",
        class_name="Outer",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert_simple004_assert_simple004_v1_xml(mode, save_output, output_format):
    """
    Assertion on a simple type using xpathDefaultNamespace on xs:schema
    element Assertion on a simple type: value must be castable to
    xs:double
    """
    assert_bindings(
        schema="saxonData/Assert/assert-simple004.xsd",
        instance="saxonData/Assert/assert-simple003.v1.xml",
        class_name="Outer",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert_simple003_assert_simple003_v1_xml(mode, save_output, output_format):
    """
    Assertion on a simple type using xpathDefaultNamespace Assertion on a
    simple type: value must be castable to xs:double
    """
    assert_bindings(
        schema="saxonData/Assert/assert-simple003.xsd",
        instance="saxonData/Assert/assert-simple003.v1.xml",
        class_name="Outer",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert_simple001_assert_simple001_v1_xml(mode, save_output, output_format):
    """
    Assertion on a simple type Assertion on a simple type: date must be in
    the past
    """
    assert_bindings(
        schema="saxonData/Assert/assert-simple001.xsd",
        instance="saxonData/Assert/assert-simple001.v1.xml",
        class_name="Outer",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert024_assert024_v1_xml(mode, save_output, output_format):
    """
    Namespace-aware assertions The subtree being validated must include
    copies of in-scope namespaces
    """
    assert_bindings(
        schema="saxonData/Assert/assert024.xsd",
        instance="saxonData/Assert/assert024.v1.xml",
        class_name="Test",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert023_assert023_v1_xml(mode, save_output, output_format):
    """
    Check that comments are by default not visible in assertions Schema
    asserts that comments are not allowed. Result depends on configuration
    setting (see resolution of spec bug 13935
    """
    assert_bindings(
        schema="saxonData/Assert/assert023.xsd",
        instance="saxonData/Assert/assert023.v1.xml",
        class_name="Temp",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert023_assert023_v2_xml(mode, save_output, output_format):
    """
    Check that comments are by default not visible in assertions Schema
    asserts that comments are not allowed. Result depends on configuration
    setting (see resolution of spec bug 13935
    """
    assert_bindings(
        schema="saxonData/Assert/assert023.xsd",
        instance="saxonData/Assert/assert023.n1.xml",
        class_name="Temp",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert022_assert022_v1_xml(mode, save_output, output_format):
    """
    Assertion testing type of data Elements below the assertion root are
    properly typed
    """
    assert_bindings(
        schema="saxonData/Assert/assert022.xsd",
        instance="saxonData/Assert/assert022.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert021_assert021_v1_xml(mode, save_output, output_format):
    """
    Assertion combined with chameleon include Effect of
    xpathDefaultNamespace="##targetNamespace"
    """
    assert_bindings(
        schema="saxonData/Assert/assert021.xsd",
        instance="saxonData/Assert/assert021.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert020_assert020_v1_xml(mode, save_output, output_format):
    """
    Assertion combined with chameleon include Effect of
    xpathDefaultNamespace="##targetNamespace"
    """
    assert_bindings(
        schema="saxonData/Assert/assert020.xsd",
        instance="saxonData/Assert/assert020.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert019_assert019_v1_xml(mode, save_output, output_format):
    """
    Assertion testing type of data Elements below the assertion root are
    properly typed
    """
    assert_bindings(
        schema="saxonData/Assert/assert019.xsd",
        instance="saxonData/Assert/assert016.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert018_assert018_v1_xml(mode, save_output, output_format):
    """
    Assertion testing type of data Elements below the assertion root are
    properly typed
    """
    assert_bindings(
        schema="saxonData/Assert/assert018.xsd",
        instance="saxonData/Assert/assert016.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert017_assert017_v1_xml(mode, save_output, output_format):
    """
    Assertion testing type of data Atomizing the element succeeds, and the
    result is untypedAtomic
    """
    assert_bindings(
        schema="saxonData/Assert/assert017.xsd",
        instance="saxonData/Assert/assert016.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert016_assert016_v1_xml(mode, save_output, output_format):
    """
    Assertion testing type of data Atomizing the element succeeds (it has
    type xs:anyType, not a type with element-only content)
    """
    assert_bindings(
        schema="saxonData/Assert/assert016.xsd",
        instance="saxonData/Assert/assert016.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert015_assert015_v1_xml(mode, save_output, output_format):
    """
    Assertion testing type of data $value is typed (complex type with
    simple content)
    """
    assert_bindings(
        schema="saxonData/Assert/assert015.xsd",
        instance="saxonData/Assert/assert013.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert014_assert014_v1_xml(mode, save_output, output_format):
    """
    Assertion testing type of data Element root of subtree is anyType
    """
    assert_bindings(
        schema="saxonData/Assert/assert014.xsd",
        instance="saxonData/Assert/assert013.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert013_assert013_v1_xml(mode, save_output, output_format):
    """
    Assertion testing type of data Attribute within subtree is typed
    """
    assert_bindings(
        schema="saxonData/Assert/assert013.xsd",
        instance="saxonData/Assert/assert013.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert010_assert010_v1_xml(mode, save_output, output_format):
    """
    Assertion on a complex type with simple content Co-occurrence
    constraint between the text content and an attribute.
    """
    assert_bindings(
        schema="saxonData/Assert/assert010.xsd",
        instance="saxonData/Assert/assert010.v1.xml",
        class_name="Temp",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert009_assert009_v1_xml(mode, save_output, output_format):
    """
    Assert that a node-set is empty - error diagnostics handled specially
    by Saxon Simple assertion on an attribute value
    """
    assert_bindings(
        schema="saxonData/Assert/assert009.xsd",
        instance="saxonData/Assert/assert009.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert008a_assert008a_v1_xml(mode, save_output, output_format):
    """
    Use xpathDefaultNamespace on xs:schema element Variant of assert007
    written with xpathDefaultNamespace. Same instance documents.
    """
    assert_bindings(
        schema="saxonData/Assert/assert008a.xsd",
        instance="saxonData/Assert/assert007.v1.xml",
        class_name="Game",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert008_assert008_v1_xml(mode, save_output, output_format):
    """
    Use xpathDefaultNamespace on xs:assert Variant of assert007 written
    with xpathDefaultNamespace. Same instance documents.
    """
    assert_bindings(
        schema="saxonData/Assert/assert008.xsd",
        instance="saxonData/Assert/assert007.v1.xml",
        class_name="Game",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert007_assert007_v1_xml(mode, save_output, output_format):
    """
    Inheritance of constraints in a type derived by extension Tests
    inheritance of constraints; also imposes a constraint on a text node
    in a type with complex content; also uses namespaces
    """
    assert_bindings(
        schema="saxonData/Assert/assert007.xsd",
        instance="saxonData/Assert/assert007.v1.xml",
        class_name="Game",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert006_assert006_v1_xml(mode, save_output, output_format):
    """
    Inheritance of constraints in a type derived by restriction Tests
    inheritance of constraints; also imposes a constraint on a text node
    in a type with simple content.
    """
    assert_bindings(
        schema="saxonData/Assert/assert006.xsd",
        instance="saxonData/Assert/assert006.v1.xml",
        class_name="Outer",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert005_assert005_v1_xml(mode, save_output, output_format):
    """
    Multiple constraints on an inner level, no constraint at outer level
    Tests the ability to construct multiple subtrees for validation,
    including use of preceding axis designed to stress the Saxon
    implementation.
    """
    assert_bindings(
        schema="saxonData/Assert/assert005.xsd",
        instance="saxonData/Assert/assert005.v1.xml",
        class_name="Outer",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert005_assert005_v2_xml(mode, save_output, output_format):
    """
    Multiple constraints on an inner level, no constraint at outer level
    Tests the ability to construct multiple subtrees for validation,
    including use of preceding axis designed to stress the Saxon
    implementation.
    """
    assert_bindings(
        schema="saxonData/Assert/assert005.xsd",
        instance="saxonData/Assert/assert005.v2.xml",
        class_name="Outer",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert004_assert004_v1_xml(mode, save_output, output_format):
    """
    Constraints at more than one level Imposes constraints at two levels
    of the same tree; also tests that constraints at the inner level are
    rooted at the node being validated.
    """
    assert_bindings(
        schema="saxonData/Assert/assert004.xsd",
        instance="saxonData/Assert/assert004.v1.xml",
        class_name="Outer",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert004_assert004_v2_xml(mode, save_output, output_format):
    """
    Constraints at more than one level Imposes constraints at two levels
    of the same tree; also tests that constraints at the inner level are
    rooted at the node being validated.
    """
    assert_bindings(
        schema="saxonData/Assert/assert004.xsd",
        instance="saxonData/Assert/assert004.v2.xml",
        class_name="Outer",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert003_assert003_v1_xml(mode, save_output, output_format):
    """
    Cross validation between elements and attributes Asserts that
    existence of an attribute and a descendant element are mutually
    exclusive
    """
    assert_bindings(
        schema="saxonData/Assert/assert003.xsd",
        instance="saxonData/Assert/assert003.v1.xml",
        class_name="Temp",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert003_assert003_v2_xml(mode, save_output, output_format):
    """
    Cross validation between elements and attributes Asserts that
    existence of an attribute and a descendant element are mutually
    exclusive
    """
    assert_bindings(
        schema="saxonData/Assert/assert003.xsd",
        instance="saxonData/Assert/assert003.v2.xml",
        class_name="Temp",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert002_assert002_v1_xml(mode, save_output, output_format):
    """
    Cross validation between two attributes Cross validation between two
    attributes
    """
    assert_bindings(
        schema="saxonData/Assert/assert002.xsd",
        instance="saxonData/Assert/assert002.v1.xml",
        class_name="Temp",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_assert001_assert001_v1_xml(mode, save_output, output_format):
    """
    Simple assertion on an attribute value Simple assertion on an
    attribute value
    """
    assert_bindings(
        schema="saxonData/Assert/assert001.xsd",
        instance="saxonData/Assert/assert001.v1.xml",
        class_name="Temp",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_unique003_unique003_v1_xml(mode, save_output, output_format):
    """
    For the purposes of uniqueness constraints, NaN is effectively equal
    to NaN For the purposes of uniqueness constraints, NaN is effectively
    equal to NaN. (Uniqueness is violated if the values are "identical or
    equal"). See bug 9196.
    """
    assert_bindings(
        schema="saxonData/Complex/unique003.xsd",
        instance="saxonData/Complex/unique003.v1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_unique003_unique003_v2_xml(mode, save_output, output_format):
    """
    For the purposes of uniqueness constraints, NaN is effectively equal
    to NaN For the purposes of uniqueness constraints, NaN is effectively
    equal to NaN. (Uniqueness is violated if the values are "identical or
    equal"). See bug 9196.
    """
    assert_bindings(
        schema="saxonData/Complex/unique003.xsd",
        instance="saxonData/Complex/unique003.v2.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_unique001_unique001_v1_xml(mode, save_output, output_format):
    """
    Test uniqueness constraint on a field having a complex type with
    simple content See comment in the schema document, and bug 10236. In
    the XSD 1.0 spec, see clause 3 of "Identity Constraint Satisfied" in
    3.11.4 Identity-constraint Definition Validation Rules.
    """
    assert_bindings(
        schema="saxonData/Complex/unique001.xsd",
        instance="saxonData/Complex/unique001.v1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_complex014_complex014_v1_xml(mode, save_output, output_format):
    """
    xsi:nil on complex type with element-only content, xs:all compositor
    (not specific to 1.1) All combinations of xsi:nil with value present
    or absent
    """
    assert_bindings(
        schema="saxonData/Complex/complex014.xsd",
        instance="saxonData/Complex/complex013.v1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_complex014_complex014_v2_xml(mode, save_output, output_format):
    """
    xsi:nil on complex type with element-only content, xs:all compositor
    (not specific to 1.1) All combinations of xsi:nil with value present
    or absent
    """
    assert_bindings(
        schema="saxonData/Complex/complex014.xsd",
        instance="saxonData/Complex/complex013.v2.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_complex013_complex013_v1_xml(mode, save_output, output_format):
    """
    xsi:nil on complex type with element-only content (not specific to
    1.1) All combinations of xsi:nil with value present or absent
    """
    assert_bindings(
        schema="saxonData/Complex/complex013.xsd",
        instance="saxonData/Complex/complex013.v1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_complex013_complex013_v2_xml(mode, save_output, output_format):
    """
    xsi:nil on complex type with element-only content (not specific to
    1.1) All combinations of xsi:nil with value present or absent
    """
    assert_bindings(
        schema="saxonData/Complex/complex013.xsd",
        instance="saxonData/Complex/complex013.v2.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_complex012_complex012_v1_xml(mode, save_output, output_format):
    """
    xsi:nil on complex type with mixede content (not specific to 1.1) All
    combinations of xsi:nil with value present or absent
    """
    assert_bindings(
        schema="saxonData/Complex/complex012.xsd",
        instance="saxonData/Complex/complex012.v1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_complex012_complex012_v2_xml(mode, save_output, output_format):
    """
    xsi:nil on complex type with mixede content (not specific to 1.1) All
    combinations of xsi:nil with value present or absent
    """
    assert_bindings(
        schema="saxonData/Complex/complex012.xsd",
        instance="saxonData/Complex/complex012.v2.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_complex012_complex012_v3_xml(mode, save_output, output_format):
    """
    xsi:nil on complex type with mixede content (not specific to 1.1) All
    combinations of xsi:nil with value present or absent
    """
    assert_bindings(
        schema="saxonData/Complex/complex012.xsd",
        instance="saxonData/Complex/complex012.v3.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_complex012_complex012_v4_xml(mode, save_output, output_format):
    """
    xsi:nil on complex type with mixede content (not specific to 1.1) All
    combinations of xsi:nil with value present or absent
    """
    assert_bindings(
        schema="saxonData/Complex/complex012.xsd",
        instance="saxonData/Complex/complex012.v4.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_complex012_complex012_v5_xml(mode, save_output, output_format):
    """
    xsi:nil on complex type with mixede content (not specific to 1.1) All
    combinations of xsi:nil with value present or absent
    """
    assert_bindings(
        schema="saxonData/Complex/complex012.xsd",
        instance="saxonData/Complex/complex012.v5.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_complex012_complex012_v6_xml(mode, save_output, output_format):
    """
    xsi:nil on complex type with mixede content (not specific to 1.1) All
    combinations of xsi:nil with value present or absent
    """
    assert_bindings(
        schema="saxonData/Complex/complex012.xsd",
        instance="saxonData/Complex/complex012.v6.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_complex011_complex011_v1_xml(mode, save_output, output_format):
    """
    xsi:nil on complex type with simple content (not specific to 1.1) All
    combinations of xsi:nil with value present or absent
    """
    assert_bindings(
        schema="saxonData/Complex/complex011.xsd",
        instance="saxonData/Complex/complex011.v1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_complex011_complex011_v2_xml(mode, save_output, output_format):
    """
    xsi:nil on complex type with simple content (not specific to 1.1) All
    combinations of xsi:nil with value present or absent
    """
    assert_bindings(
        schema="saxonData/Complex/complex011.xsd",
        instance="saxonData/Complex/complex011.v2.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_complex010_complex010_v1_xml(mode, save_output, output_format):
    """
    xsi:noNamespaceSchemaLocation use="required Specifying use="required"
    for xsi:noNamespaceSchemaLocation is allowed and effective
    """
    assert_bindings(
        schema="saxonData/Complex/complex010.xsd",
        instance="saxonData/Complex/complex010.v1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_complex009_complex009_v1_xml(mode, save_output, output_format):
    """
    xsi:type use="required Specifying use="required" for xsi:type is
    allowed and effective
    """
    assert_bindings(
        schema="saxonData/Complex/complex009.xsd",
        instance="saxonData/Complex/complex009.v1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_complex009_complex009_v2_xml(mode, save_output, output_format):
    """
    xsi:type use="required Specifying use="required" for xsi:type is
    allowed and effective
    """
    assert_bindings(
        schema="saxonData/Complex/complex009.xsd",
        instance="saxonData/Complex/complex009.v2.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_complex007_complex007_v1_xml(mode, save_output, output_format):
    """
    xsi:nil fixed Fixed value for xsi:nil is allowed but ignored, except
    if present in the instance it must match and be obeyed
    """
    assert_bindings(
        schema="saxonData/Complex/complex007.xsd",
        instance="saxonData/Complex/complex006.v1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_complex007_complex007_v2_xml(mode, save_output, output_format):
    """
    xsi:nil fixed Fixed value for xsi:nil is allowed but ignored, except
    if present in the instance it must match and be obeyed
    """
    assert_bindings(
        schema="saxonData/Complex/complex007.xsd",
        instance="saxonData/Complex/complex006.v2.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_complex006_complex006_v1_xml(mode, save_output, output_format):
    """
    xsi:nil default Default value for xsi:nil is allowed but ignored
    """
    assert_bindings(
        schema="saxonData/Complex/complex006.xsd",
        instance="saxonData/Complex/complex006.v1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_complex006_complex006_v2_xml(mode, save_output, output_format):
    """
    xsi:nil default Default value for xsi:nil is allowed but ignored
    """
    assert_bindings(
        schema="saxonData/Complex/complex006.xsd",
        instance="saxonData/Complex/complex006.v2.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_complex005_complex005_v2_xml(mode, save_output, output_format):
    """
    xsi:type fixed Fixed value for xsi:type is allowed but ignored, except
    that the instance must match
    """
    assert_bindings(
        schema="saxonData/Complex/complex005.xsd",
        instance="saxonData/Complex/complex005.v2.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_complex004_complex004_v1_xml(mode, save_output, output_format):
    """
    xsi:type default Default value for xsi:type is allowed but ignored
    """
    assert_bindings(
        schema="saxonData/Complex/complex004.xsd",
        instance="saxonData/Complex/complex004.v1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_complex004_complex004_v2_xml(mode, save_output, output_format):
    """
    xsi:type default Default value for xsi:type is allowed but ignored
    """
    assert_bindings(
        schema="saxonData/Complex/complex004.xsd",
        instance="saxonData/Complex/complex004.n2.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_complex003_complex003_v1_xml(mode, save_output, output_format):
    """
    xsi:type default Default value for xsi:type is allowed but ignored
    """
    assert_bindings(
        schema="saxonData/Complex/complex003.xsd",
        instance="saxonData/Complex/complex003.v1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0044_cta0044_v01(mode, save_output, output_format):
    """
    Type alternatives - restricting attributes Attribute allowed in one
    alternative but not allowed in another
    """
    assert_bindings(
        schema="saxonData/CTA/cta0044.xsd",
        instance="saxonData/CTA/cta0044.v01.xml",
        class_name="Top",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0042_cta0042_v01(mode, save_output, output_format):
    """
    Element Declarations Consistent Two particles in a content model have
    the same name; permitted because they have the same type table
    """
    assert_bindings(
        schema="saxonData/CTA/cta0042.xsd",
        instance="saxonData/CTA/cta0042.v01.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0041_cta0041_v01(mode, save_output, output_format):
    """
    Type alternative - substitutability Invalid substitution in a
    substitution group - detected only at validation time, by particular
    instances
    """
    assert_bindings(
        schema="saxonData/CTA/cta0041.xsd",
        instance="saxonData/CTA/cta0041.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0040_cta0040_v01(mode, save_output, output_format):
    """
    Type alternative - substitutability Valid substitution in a
    substitution group
    """
    assert_bindings(
        schema="saxonData/CTA/cta0040.xsd",
        instance="saxonData/CTA/cta0040.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0028_cta0028_v01(mode, save_output, output_format):
    """
    Type alternative using a simple type Static context of XPath
    expression
    """
    assert_bindings(
        schema="saxonData/CTA/cta0028.xsd",
        instance="saxonData/CTA/cta0023.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0027_cta0027_v01(mode, save_output, output_format):
    """
    Type alternative using a simple type Static context of XPath
    expression
    """
    assert_bindings(
        schema="saxonData/CTA/cta0027.xsd",
        instance="saxonData/CTA/cta0023.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0026_cta0026_v01(mode, save_output, output_format):
    """
    Type alternative using a simple type Static context of XPath
    expression
    """
    assert_bindings(
        schema="saxonData/CTA/cta0026.xsd",
        instance="saxonData/CTA/cta0023.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0025_cta0025_v01(mode, save_output, output_format):
    """
    Type alternative using a simple type Static context of XPath
    expression
    """
    assert_bindings(
        schema="saxonData/CTA/cta0025.xsd",
        instance="saxonData/CTA/cta0023.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0024_cta0024_v01(mode, save_output, output_format):
    """
    Type alternative using a simple type Static context of XPath
    expression
    """
    assert_bindings(
        schema="saxonData/CTA/cta0024.xsd",
        instance="saxonData/CTA/cta0023.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0023_cta0023_v01(mode, save_output, output_format):
    """
    Type alternative using a simple type Static context of XPath
    expression
    """
    assert_bindings(
        schema="saxonData/CTA/cta0023.xsd",
        instance="saxonData/CTA/cta0023.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0022_cta0022_v01(mode, save_output, output_format):
    """
    Type alternative using a simple type Dynamic context of XPath
    expression
    """
    assert_bindings(
        schema="saxonData/CTA/cta0022.xsd",
        instance="saxonData/CTA/cta0017.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0021_cta0021_v01(mode, save_output, output_format):
    """
    Type alternative using a simple type XPath expression sees base URI of
    element node
    """
    assert_bindings(
        schema="saxonData/CTA/cta0021.xsd",
        instance="saxonData/CTA/cta0021.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0020_cta0020_v01(mode, save_output, output_format):
    """
    Type alternative using a simple type XPath expression sees name of
    element node
    """
    assert_bindings(
        schema="saxonData/CTA/cta0020.xsd",
        instance="saxonData/CTA/cta0017.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0019_cta0019_v01(mode, save_output, output_format):
    """
    Type alternative using a simple type XPath expression sees untyped
    data
    """
    assert_bindings(
        schema="saxonData/CTA/cta0019.xsd",
        instance="saxonData/CTA/cta0017.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0018_cta0018_v01(mode, save_output, output_format):
    """
    Type alternative using a simple type XPath expression sees untyped
    data
    """
    assert_bindings(
        schema="saxonData/CTA/cta0018.xsd",
        instance="saxonData/CTA/cta0017.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0017_cta0017_v01(mode, save_output, output_format):
    """
    Type alternative using a simple type XPath expression can only access
    attributes
    """
    assert_bindings(
        schema="saxonData/CTA/cta0017.xsd",
        instance="saxonData/CTA/cta0017.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0016_cta0016_v01(mode, save_output, output_format):
    """
    Type alternative using a simple type Error in XPath evaluation treated
    as false
    """
    assert_bindings(
        schema="saxonData/CTA/cta0016.xsd",
        instance="saxonData/CTA/cta0014.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0016_cta0016_v02(mode, save_output, output_format):
    """
    Type alternative using a simple type Error in XPath evaluation treated
    as false
    """
    assert_bindings(
        schema="saxonData/CTA/cta0016.xsd",
        instance="saxonData/CTA/cta0014.v02.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0015_cta0015_v01(mode, save_output, output_format):
    """
    Type alternative using a simple type Implicit default alternative as
    last alternative
    """
    assert_bindings(
        schema="saxonData/CTA/cta0015.xsd",
        instance="saxonData/CTA/cta0014.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0015_cta0015_v02(mode, save_output, output_format):
    """
    Type alternative using a simple type Implicit default alternative as
    last alternative
    """
    assert_bindings(
        schema="saxonData/CTA/cta0015.xsd",
        instance="saxonData/CTA/cta0014.v02.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0014_cta0014_v01(mode, save_output, output_format):
    """
    Type alternative using a simple type Explicit default alternative as
    last alternative
    """
    assert_bindings(
        schema="saxonData/CTA/cta0014.xsd",
        instance="saxonData/CTA/cta0014.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0014_cta0014_v02(mode, save_output, output_format):
    """
    Type alternative using a simple type Explicit default alternative as
    last alternative
    """
    assert_bindings(
        schema="saxonData/CTA/cta0014.xsd",
        instance="saxonData/CTA/cta0014.v02.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0013_cta0013_v01(mode, save_output, output_format):
    """
    Type alternative using an inherited attribute A non-inheritable
    attribute does not mask an inheritable attribute on an ancestor
    """
    assert_bindings(
        schema="saxonData/CTA/cta0013.xsd",
        instance="saxonData/CTA/cta0013.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0013_cta0013_v02(mode, save_output, output_format):
    """
    Type alternative using an inherited attribute A non-inheritable
    attribute does not mask an inheritable attribute on an ancestor
    """
    assert_bindings(
        schema="saxonData/CTA/cta0013.xsd",
        instance="saxonData/CTA/cta0013.v02.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0012_cta0012_v01(mode, save_output, output_format):
    """
    Type alternative using an inherited attribute Inheritability differs
    between attribute declaration and use: attribute use wins
    """
    assert_bindings(
        schema="saxonData/CTA/cta0012.xsd",
        instance="saxonData/CTA/cta0012.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0011_cta0011_v01(mode, save_output, output_format):
    """
    Type alternative using an inherited attribute Inheritability differs
    between attribute declaration and use: attribute use wins
    """
    assert_bindings(
        schema="saxonData/CTA/cta0011.xsd",
        instance="saxonData/CTA/cta0009.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0011_cta0011_v02(mode, save_output, output_format):
    """
    Type alternative using an inherited attribute Inheritability differs
    between attribute declaration and use: attribute use wins
    """
    assert_bindings(
        schema="saxonData/CTA/cta0011.xsd",
        instance="saxonData/CTA/cta0009.v02.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0010_cta0010_v01(mode, save_output, output_format):
    """
    Type alternative using an inherited attribute Type alternative is an
    anonymous type defined as child of xs:alternative
    """
    assert_bindings(
        schema="saxonData/CTA/cta0010.xsd",
        instance="saxonData/CTA/cta0010.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0010_cta0010_v02(mode, save_output, output_format):
    """
    Type alternative using an inherited attribute Type alternative is an
    anonymous type defined as child of xs:alternative
    """
    assert_bindings(
        schema="saxonData/CTA/cta0010.xsd",
        instance="saxonData/CTA/cta0010.v02.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0009_cta0009_v01(mode, save_output, output_format):
    """
    Type alternative using an inherited attribute Type alternative is an
    anonymous type defined as child of xs:alternative
    """
    assert_bindings(
        schema="saxonData/CTA/cta0009.xsd",
        instance="saxonData/CTA/cta0009.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0009_cta0009_v02(mode, save_output, output_format):
    """
    Type alternative using an inherited attribute Type alternative is an
    anonymous type defined as child of xs:alternative
    """
    assert_bindings(
        schema="saxonData/CTA/cta0009.xsd",
        instance="saxonData/CTA/cta0009.v02.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0008_cta0008_v01(mode, save_output, output_format):
    """
    Inline type alternative Type alternative is an anonymous type defined
    as child of xs:alternative
    """
    assert_bindings(
        schema="saxonData/CTA/cta0008.xsd",
        instance="saxonData/CTA/cta0008.v01.xml",
        class_name="Example",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0006_cta0006_v01(mode, save_output, output_format):
    """
    Conditional simple type: selecting a branch of a union Simple type of
    message depends on enumerated kind attribute, value is a QName
    identifying the branch of a union (xsi:type simulation)
    """
    assert_bindings(
        schema="saxonData/CTA/cta0006.xsd",
        instance="saxonData/CTA/cta0006.v01.xml",
        class_name="Messages",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0005_cta0005_v01(mode, save_output, output_format):
    """
    Conditional complex type with namespaces Variant of cta0003 (same
    instance documents) using xpathDefaultNamespace at the schema level
    """
    assert_bindings(
        schema="saxonData/CTA/cta0005.xsd",
        instance="saxonData/CTA/cta0003.v01.xml",
        class_name="Messages",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0004_cta0004_v01(mode, save_output, output_format):
    """
    Conditional complex type with namespaces Variant of cta0003 (same
    instance documents) using xpathDefaultNamespace
    """
    assert_bindings(
        schema="saxonData/CTA/cta0004.xsd",
        instance="saxonData/CTA/cta0003.v01.xml",
        class_name="Messages",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0003_cta0003_v01(mode, save_output, output_format):
    """
    Conditional complex type with namespaces Trivial reference to the name
    of the element
    """
    assert_bindings(
        schema="saxonData/CTA/cta0003.xsd",
        instance="saxonData/CTA/cta0003.v01.xml",
        class_name="Messages",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0002_cta0002_v01(mode, save_output, output_format):
    """
    Conditional complex type with namespaces Complex type of message
    depends on enumerated min attribute
    """
    assert_bindings(
        schema="saxonData/CTA/cta0002.xsd",
        instance="saxonData/CTA/cta0002.v01.xml",
        class_name="Messages",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0001_cta0001_v01(mode, save_output, output_format):
    """
    Conditional simple type: example based on spec Simple type of message
    depends on enumerated kind attribute
    """
    assert_bindings(
        schema="saxonData/CTA/cta0001.xsd",
        instance="saxonData/CTA/cta0001.v01.xml",
        class_name="Message",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0001_cta0001_v02(mode, save_output, output_format):
    """
    Conditional simple type: example based on spec Simple type of message
    depends on enumerated kind attribute
    """
    assert_bindings(
        schema="saxonData/CTA/cta0001.xsd",
        instance="saxonData/CTA/cta0001.v02.xml",
        class_name="Message",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_cta0001_cta0001_v03(mode, save_output, output_format):
    """
    Conditional simple type: example based on spec Simple type of message
    depends on enumerated kind attribute
    """
    assert_bindings(
        schema="saxonData/CTA/cta0001.xsd",
        instance="saxonData/CTA/cta0001.v03.xml",
        class_name="Messages",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id054_id054_v01_xml(mode, save_output, output_format):
    """
    Keyref constraint using xpathDefaultNamespace Use
    XPathDefaultNamespace=##local on the local element and the xs:schema
    element
    """
    assert_bindings(
        schema="saxonData/Id/id054.xsd",
        instance="saxonData/Id/id054.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id053_id053_v01_xml(mode, save_output, output_format):
    """
    Key constraint using xpathDefaultNamespace Use
    XPathDefaultNamespace=##targetNamespace on the local element
    """
    assert_bindings(
        schema="saxonData/Id/id053.xsd",
        instance="saxonData/Id/id050.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id052_id052_v01_xml(mode, save_output, output_format):
    """
    Key constraint using xpathDefaultNamespace Use XPathDefaultNamespace
    on the xs:schema element
    """
    assert_bindings(
        schema="saxonData/Id/id052.xsd",
        instance="saxonData/Id/id050.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id051_id051_v01_xml(mode, save_output, output_format):
    """
    Key constraint using xpathDefaultNamespace Use XPathDefaultNamespace
    on the xs:schema element
    """
    assert_bindings(
        schema="saxonData/Id/id051.xsd",
        instance="saxonData/Id/id050.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id050_id050_v01_xml(mode, save_output, output_format):
    """
    Unique constraint using xpathDefaultNamespace Use
    XPathDefaultNamespace on the selector and field elements
    """
    assert_bindings(
        schema="saxonData/Id/id050.xsd",
        instance="saxonData/Id/id050.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id044_id044_v01_xml(mode, save_output, output_format):
    """
    Keyref constraint using ref attribute Keyref constraint refers to
    another keyref constraint using ref attribute
    """
    assert_bindings(
        schema="saxonData/Id/id044.xsd",
        instance="saxonData/Id/id044.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id043_id043_v01_xml(mode, save_output, output_format):
    """
    Key constraint using ref attribute Key constraint refers to another
    key constraint using ref attribute
    """
    assert_bindings(
        schema="saxonData/Id/id043.xsd",
        instance="saxonData/Id/id043.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id040_id040_v01_xml(mode, save_output, output_format):
    """
    Unique constraint using ref attribute Unique constraint refers to
    another unique constraint using ref attribute
    """
    assert_bindings(
        schema="saxonData/Id/id040.xsd",
        instance="saxonData/Id/id040.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id022_id022_v01_xml(mode, save_output, output_format):
    """
    Atomic value equal to singleton list Value of a key is atomic; value
    of keyref is a list; they can be equal
    """
    assert_bindings(
        schema="saxonData/Id/id022.xsd",
        instance="saxonData/Id/id022.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id021_id021_v01_xml(mode, save_output, output_format):
    """
    Element of type xs:ENTITIES with default value Element of type
    xs:ENTITIES with default value
    """
    assert_bindings(
        schema="saxonData/Id/id021.xsd",
        instance="saxonData/Id/id021.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id021_id021_v02_xml(mode, save_output, output_format):
    """
    Element of type xs:ENTITIES with default value Element of type
    xs:ENTITIES with default value
    """
    assert_bindings(
        schema="saxonData/Id/id021.xsd",
        instance="saxonData/Id/id021.v02.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id020_id020_v01_xml(mode, save_output, output_format):
    """
    Element of type xs:ENTITY with default value Element of type xs:ENTITY
    with default value
    """
    assert_bindings(
        schema="saxonData/Id/id020.xsd",
        instance="saxonData/Id/id020.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id020_id020_v02_xml(mode, save_output, output_format):
    """
    Element of type xs:ENTITY with default value Element of type xs:ENTITY
    with default value
    """
    assert_bindings(
        schema="saxonData/Id/id020.xsd",
        instance="saxonData/Id/id020.v02.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id020_id020_v03_xml(mode, save_output, output_format):
    """
    Element of type xs:ENTITY with default value Element of type xs:ENTITY
    with default value
    """
    assert_bindings(
        schema="saxonData/Id/id020.xsd",
        instance="saxonData/Id/id020.v03.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id019_id019_v01_xml(mode, save_output, output_format):
    """
    Union of ENTITY and integer attribute with default value Union of
    ENTITY and integer attribute with default value
    """
    assert_bindings(
        schema="saxonData/Id/id019.xsd",
        instance="saxonData/Id/id019.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id019_id019_v02_xml(mode, save_output, output_format):
    """
    Union of ENTITY and integer attribute with default value Union of
    ENTITY and integer attribute with default value
    """
    assert_bindings(
        schema="saxonData/Id/id019.xsd",
        instance="saxonData/Id/id019.v02.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id018_id018_v01_xml(mode, save_output, output_format):
    """
    ENTITIES attribute with default value ENTITIES attribute with default
    value
    """
    assert_bindings(
        schema="saxonData/Id/id018.xsd",
        instance="saxonData/Id/id018.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id018_id018_v02_xml(mode, save_output, output_format):
    """
    ENTITIES attribute with default value ENTITIES attribute with default
    value
    """
    assert_bindings(
        schema="saxonData/Id/id018.xsd",
        instance="saxonData/Id/id018.v02.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id018_id018_v03_xml(mode, save_output, output_format):
    """
    ENTITIES attribute with default value ENTITIES attribute with default
    value
    """
    assert_bindings(
        schema="saxonData/Id/id018.xsd",
        instance="saxonData/Id/id018.v03.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id017_id017_v01_xml(mode, save_output, output_format):
    """
    ENTITY attribute with default value ENTITY attribute with default
    value
    """
    assert_bindings(
        schema="saxonData/Id/id017.xsd",
        instance="saxonData/Id/id017.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id017_id017_v02_xml(mode, save_output, output_format):
    """
    ENTITY attribute with default value ENTITY attribute with default
    value
    """
    assert_bindings(
        schema="saxonData/Id/id017.xsd",
        instance="saxonData/Id/id017.v02.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id016_id016_v01_xml(mode, save_output, output_format):
    """
    IDREF attribute with default value IDREF attribute with default value
    """
    assert_bindings(
        schema="saxonData/Id/id016.xsd",
        instance="saxonData/Id/id016.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id016_id016_v02_xml(mode, save_output, output_format):
    """
    IDREF attribute with default value IDREF attribute with default value
    """
    assert_bindings(
        schema="saxonData/Id/id016.xsd",
        instance="saxonData/Id/id016.v02.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id015_id015_v01_xml(mode, save_output, output_format):
    """
    ID element with fixed value ID element with fixed value
    """
    assert_bindings(
        schema="saxonData/Id/id015.xsd",
        instance="saxonData/Id/id015.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id014_id014_v01_xml(mode, save_output, output_format):
    """
    ID element with default value ID element with default value
    """
    assert_bindings(
        schema="saxonData/Id/id014.xsd",
        instance="saxonData/Id/id014.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id013_id013_v01_xml(mode, save_output, output_format):
    """
    ID attribute with fixed value ID attribute with fixed value
    """
    assert_bindings(
        schema="saxonData/Id/id013.xsd",
        instance="saxonData/Id/id011.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id012_id012_v01_xml(mode, save_output, output_format):
    """
    ID attribute with default value ID attribute with default value
    """
    assert_bindings(
        schema="saxonData/Id/id012.xsd",
        instance="saxonData/Id/id010.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id011_id011_v01_xml(mode, save_output, output_format):
    """
    ID attribute with fixed value ID attribute with fixed value
    """
    assert_bindings(
        schema="saxonData/Id/id011.xsd",
        instance="saxonData/Id/id011.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id010_id010_v01_xml(mode, save_output, output_format):
    """
    ID attribute with default value ID attribute with default value
    """
    assert_bindings(
        schema="saxonData/Id/id010.xsd",
        instance="saxonData/Id/id010.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id009_id009_v01_xml(mode, save_output, output_format):
    """
    Nillable ID/IDREF elements Nillable ID/IDREF elements
    """
    assert_bindings(
        schema="saxonData/Id/id009.xsd",
        instance="saxonData/Id/id009.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id008_id008_v01_xml(mode, save_output, output_format):
    """
    A complex type with simple ID/IDREF content A complex type with simple
    ID/IDREF content at one time imposed no uniqueness or referential
    constraints, but this has been clarified.
    """
    assert_bindings(
        schema="saxonData/Id/id008.xsd",
        instance="saxonData/Id/id008.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id007_id007_v01_xml(mode, save_output, output_format):
    """
    A highly devious test in which we define a list type whose items may
    be either IDs or IDREFs A highly devious test in which we define a
    list type whose items may be either IDs or IDREFs
    """
    assert_bindings(
        schema="saxonData/Id/id007.xsd",
        instance="saxonData/Id/id007.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id006_id006_v01_xml(mode, save_output, output_format):
    """
    Element with list-of-maybe-IDREF attributes and list-of-maybe-IDREF
    children Element with list-of-maybe-IDREF attributes and list-of-
    maybe-IDREF children
    """
    assert_bindings(
        schema="saxonData/Id/id006.xsd",
        instance="saxonData/Id/id006.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id005_id005_v01_xml(mode, save_output, output_format):
    """
    Element with list-of-IDREF attributes and list-of-IDREF children
    Element with list-of-IDREF attributes and list-of-IDREF children
    """
    assert_bindings(
        schema="saxonData/Id/id005.xsd",
        instance="saxonData/Id/id005.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id004_id004_v01_xml(mode, save_output, output_format):
    """
    Element with list-of-ID attributes and list-of-ID children Element
    with list-of-ID attributes and list-of-ID children
    """
    assert_bindings(
        schema="saxonData/Id/id004.xsd",
        instance="saxonData/Id/id004.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id003_id003_v01_xml(mode, save_output, output_format):
    """
    Element with more than one ID attribute, one being a wildcard, plus ID
    children Element with more than one ID attribute, one being a
    wildcard, plus ID children
    """
    assert_bindings(
        schema="saxonData/Id/id003.xsd",
        instance="saxonData/Id/id003.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id002_id002_v01_xml(mode, save_output, output_format):
    """
    Element with more than one ID attribute, one being a wildcard Element
    with more than one ID attribute, one being a wildcard
    """
    assert_bindings(
        schema="saxonData/Id/id002.xsd",
        instance="saxonData/Id/id001.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_id001_id001_v01_xml(mode, save_output, output_format):
    """
    Element with more than one ID attribute Element with more than one ID
    attribute
    """
    assert_bindings(
        schema="saxonData/Id/id001.xsd",
        instance="saxonData/Id/id001.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_missing006_missing006_v1_xml(mode, save_output, output_format):
    """
    List type with missing item type Error only if the list type is needed
    for validation
    """
    assert_bindings(
        schema="saxonData/Missing/missing006.xsd",
        instance="saxonData/Missing/missing001.v1.xml",
        class_name="Good",
        version="1.0",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_missing003_missing003_v1_xml(mode, save_output, output_format):
    """
    Element declaration with missing substitution group head Error only if
    the element declaration is needed for validation
    """
    assert_bindings(
        schema="saxonData/Missing/missing003.xsd",
        instance="saxonData/Missing/missing001.v1.xml",
        class_name="Good",
        version="1.0",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_missing002_missing001_v1_xml(mode, save_output, output_format):
    """
    Element declaration with missing substitution group head Error only if
    the element declaration is needed for validation
    """
    assert_bindings(
        schema="saxonData/Missing/missing002.xsd",
        instance="saxonData/Missing/missing001.v1.xml",
        class_name="Good",
        version="1.0",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_missing002_missing001_n1_xml(mode, save_output, output_format):
    """
    Element declaration with missing substitution group head Error only if
    the element declaration is needed for validation
    """
    assert_bindings(
        schema="saxonData/Missing/missing002.xsd",
        instance="saxonData/Missing/missing001.n1.xml",
        class_name="Bad",
        version="1.0",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_missing001_missing001_v1_xml(mode, save_output, output_format):
    """
    Element declaration with missing type Error only if the element
    declaration is needed for validation
    """
    assert_bindings(
        schema="saxonData/Missing/missing001.xsd",
        instance="saxonData/Missing/missing001.v1.xml",
        class_name="Good",
        version="1.0",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open205_open205_v1_xml(mode, save_output, output_format):
    """
    Valid content model defaultAttributes in an imported namespace
    """
    assert_bindings(
        schema="saxonData/Open/open205.xsd",
        instance="saxonData/Open/open205.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open202_open202_v1_xml(mode, save_output, output_format):
    """
    Valid content model Basic test of defaultAttributes with
    defaultAttributesApply=false
    """
    assert_bindings(
        schema="saxonData/Open/open202.xsd",
        instance="saxonData/Open/open202.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open201_open201_v1_xml(mode, save_output, output_format):
    """
    Valid content model Basic test of defaultAttributes
    """
    assert_bindings(
        schema="saxonData/Open/open201.xsd",
        instance="saxonData/Open/open201.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open201_open201_v2_xml(mode, save_output, output_format):
    """
    Valid content model Basic test of defaultAttributes
    """
    assert_bindings(
        schema="saxonData/Open/open201.xsd",
        instance="saxonData/Open/open201.v2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open047_open047_v1_xml(mode, save_output, output_format):
    """
    A valid extension complex type extension: derived type's open content
    allows the union of the wildcards specified for the base type and for
    the extension.
    """
    assert_bindings(
        schema="saxonData/Open/open047.xsd",
        instance="saxonData/Open/open047.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open047_open047_v2_xml(mode, save_output, output_format):
    """
    A valid extension complex type extension: derived type's open content
    allows the union of the wildcards specified for the base type and for
    the extension.
    """
    assert_bindings(
        schema="saxonData/Open/open047.xsd",
        instance="saxonData/Open/open047.v2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open047_open047_v3_xml(mode, save_output, output_format):
    """
    A valid extension complex type extension: derived type's open content
    allows the union of the wildcards specified for the base type and for
    the extension.
    """
    assert_bindings(
        schema="saxonData/Open/open047.xsd",
        instance="saxonData/Open/open047.v3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open045_open045_v1_xml(mode, save_output, output_format):
    """
    defaultAttributes does not apply to types defined within xs:override
    defaultAttributes does not apply to types defined within xs:override.
    Test rewritten 2011-10-10 to reflect the fact that for a complexType
    defined within xs:override, the defaultAttributes that apply are those
    defined within the overridden schema document, not the overriding
    schema document.
    """
    assert_bindings(
        schema="saxonData/Open/open045.xsd",
        instance="saxonData/Open/open045.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open044_open044_v1_xml(mode, save_output, output_format):
    """
    defaultAttributes applies to types defined within xs:redefine
    defaultAttributes applies to types defined within xs:redefine
    """
    assert_bindings(
        schema="saxonData/Open/open044.xsd",
        instance="saxonData/Open/open044.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open043_open043_v1_xml(mode, save_output, output_format):
    """
    For types defined within xs:override, the relevant defaultOpenContent
    is the one in the overridden schema document For types defined within
    xs:override, the relevant defaultOpenContent is the one in the
    overridden schema document. Test revised 2011-10-10 in response to bug
    13458.
    """
    assert_bindings(
        schema="saxonData/Open/open043.xsd",
        instance="saxonData/Open/open043.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open042_open042_v1_xml(mode, save_output, output_format):
    """
    defaultOpenContent applies to types defined within xs:redefine
    defaultOpenContent applies to types defined within xs:redefine
    """
    assert_bindings(
        schema="saxonData/Open/open042.xsd",
        instance="saxonData/Open/open042.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open041_open041_v1_xml(mode, save_output, output_format):
    """
    defaultOpenContent is scoped to a schema document defaultOpenContent
    does not apply to types included from a different schema document
    """
    assert_bindings(
        schema="saxonData/Open/open041.xsd",
        instance="saxonData/Open/open041.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open040_open040_v1_xml(mode, save_output, output_format):
    """
    defaultOpenContent is scoped to a schema document defaultOpenContent
    does not apply to types included from a different schema document
    """
    assert_bindings(
        schema="saxonData/Open/open040.xsd",
        instance="saxonData/Open/open040.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open035_open035_v1_xml(mode, save_output, output_format):
    """
    Test defaultAttributesApply on an anonymous complex type Attribute is
    allowed on both named and unnamed types
    """
    assert_bindings(
        schema="saxonData/Open/open035.xsd",
        instance="saxonData/Open/open035.v1.xml",
        class_name="BookStore",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open031_open031_v1_xml(mode, save_output, output_format):
    """
    A valid extension complex type extension: derived type takes
    openContent from the base type ignoring the defaultOpenContent when
    the type is empty and default open content does not apply to empty
    """
    assert_bindings(
        schema="saxonData/Open/open031.xsd",
        instance="saxonData/Open/open027.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open031_open031_v2_xml(mode, save_output, output_format):
    """
    A valid extension complex type extension: derived type takes
    openContent from the base type ignoring the defaultOpenContent when
    the type is empty and default open content does not apply to empty
    """
    assert_bindings(
        schema="saxonData/Open/open031.xsd",
        instance="saxonData/Open/open027.v2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open031_open031_v3_xml(mode, save_output, output_format):
    """
    A valid extension complex type extension: derived type takes
    openContent from the base type ignoring the defaultOpenContent when
    the type is empty and default open content does not apply to empty
    """
    assert_bindings(
        schema="saxonData/Open/open031.xsd",
        instance="saxonData/Open/open027.v3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open031_open031_v4_xml(mode, save_output, output_format):
    """
    A valid extension complex type extension: derived type takes
    openContent from the base type ignoring the defaultOpenContent when
    the type is empty and default open content does not apply to empty
    """
    assert_bindings(
        schema="saxonData/Open/open031.xsd",
        instance="saxonData/Open/open027.n1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open028_open028_v1_xml(mode, save_output, output_format):
    """
    A valid extension Derived type has suffix open content, base type does
    not
    """
    assert_bindings(
        schema="saxonData/Open/open028.xsd",
        instance="saxonData/Open/open027.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open028_open028_v2_xml(mode, save_output, output_format):
    """
    A valid extension Derived type has suffix open content, base type does
    not
    """
    assert_bindings(
        schema="saxonData/Open/open028.xsd",
        instance="saxonData/Open/open027.v2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open028_open028_v3_xml(mode, save_output, output_format):
    """
    A valid extension Derived type has suffix open content, base type does
    not
    """
    assert_bindings(
        schema="saxonData/Open/open028.xsd",
        instance="saxonData/Open/open027.v3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open027_open027_v1_xml(mode, save_output, output_format):
    """
    A valid extension Base type has suffix open content, extended type
    does not
    """
    assert_bindings(
        schema="saxonData/Open/open027.xsd",
        instance="saxonData/Open/open027.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open027_open027_v2_xml(mode, save_output, output_format):
    """
    A valid extension Base type has suffix open content, extended type
    does not
    """
    assert_bindings(
        schema="saxonData/Open/open027.xsd",
        instance="saxonData/Open/open027.v2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open027_open027_v3_xml(mode, save_output, output_format):
    """
    A valid extension Base type has suffix open content, extended type
    does not
    """
    assert_bindings(
        schema="saxonData/Open/open027.xsd",
        instance="saxonData/Open/open027.v3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open025_open025_v1_xml(mode, save_output, output_format):
    """
    Open content and regular content match the same instances Show that
    regular particles take precedence
    """
    assert_bindings(
        schema="saxonData/Open/open025.xsd",
        instance="saxonData/Open/open025.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open024_open024_v1_xml(mode, save_output, output_format):
    """
    A valid restriction Open content in base type has weaker
    processContents than open content in derived type
    """
    assert_bindings(
        schema="saxonData/Open/open024.xsd",
        instance="saxonData/Open/open023.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open023_open023_v1_xml(mode, save_output, output_format):
    """
    A valid restriction Open content in base type allows more namespaces
    than open content in derived type
    """
    assert_bindings(
        schema="saxonData/Open/open023.xsd",
        instance="saxonData/Open/open023.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open022_open022_v1_xml(mode, save_output, output_format):
    """
    A valid restriction (though Saxon can't yet handle it) Base type has
    an explicit wildcard, restricted type has interleaved open content,
    all instances of the restricted type are valid against the base type.
    """
    assert_bindings(
        schema="saxonData/Open/open022.xsd",
        instance="saxonData/Open/open022.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open021_open021_v1_xml(mode, save_output, output_format):
    """
    A valid restriction Base type has suffixed open content, restricted
    type has interleaved open content, but it's OK because the restricted
    type is otherwise empty (well, "mixed empty").
    """
    assert_bindings(
        schema="saxonData/Open/open021.xsd",
        instance="saxonData/Open/open021.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open020_open020_v1_xml(mode, save_output, output_format):
    """
    A valid restriction Base type has suffixed open content, restricted
    type has interleaved open content, but it's OK because the restricted
    type is otherwise empty.
    """
    assert_bindings(
        schema="saxonData/Open/open020.xsd",
        instance="saxonData/Open/open020.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open016_open016_v1_xml(mode, save_output, output_format):
    """
    Open content: no effect on complex types with simple content Default
    open content ignored on a CT-with-SC
    """
    assert_bindings(
        schema="saxonData/Open/open016.xsd",
        instance="saxonData/Open/open016.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open015_open015_v1_xml(mode, save_output, output_format):
    """
    A valid restriction Base type has open content, restricted type has
    identical open content
    """
    assert_bindings(
        schema="saxonData/Open/open015.xsd",
        instance="saxonData/Open/open015.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open014_open014_v1_xml(mode, save_output, output_format):
    """
    A valid restriction Base type has open content, restricted type does
    not
    """
    assert_bindings(
        schema="saxonData/Open/open014.xsd",
        instance="saxonData/Open/open014.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open013_open013_v1_xml(mode, save_output, output_format):
    """
    Schema defines default open content not applying to an empty content
    model - but it does apply to a mixed content model with an empty
    particle Defined by defaultOpenContent with appliesToEmpty=false.
    """
    assert_bindings(
        schema="saxonData/Open/open013.xsd",
        instance="saxonData/Open/open013.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open012_open012_v1_xml(mode, save_output, output_format):
    """
    Schema defines default open content but not applying to an empty
    content model Defined by defaultOpenContent with appliesToEmpty=false.
    """
    assert_bindings(
        schema="saxonData/Open/open012.xsd",
        instance="saxonData/Open/open012.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open011_open011_v1_xml(mode, save_output, output_format):
    """
    Open content in an (otherwise) empty content model Defined by
    defaultOpenContent with appliesToEmpty=true. Uses same instances as
    open010.
    """
    assert_bindings(
        schema="saxonData/Open/open011.xsd",
        instance="saxonData/Open/open010.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open011_open011_v2_xml(mode, save_output, output_format):
    """
    Open content in an (otherwise) empty content model Defined by
    defaultOpenContent with appliesToEmpty=true. Uses same instances as
    open010.
    """
    assert_bindings(
        schema="saxonData/Open/open011.xsd",
        instance="saxonData/Open/open010.v2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open010_open010_v1_xml(mode, save_output, output_format):
    """
    Open content in an (otherwise) empty content model Allows any element
    in specified namespace
    """
    assert_bindings(
        schema="saxonData/Open/open010.xsd",
        instance="saxonData/Open/open010.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open010_open010_v2_xml(mode, save_output, output_format):
    """
    Open content in an (otherwise) empty content model Allows any element
    in specified namespace
    """
    assert_bindings(
        schema="saxonData/Open/open010.xsd",
        instance="saxonData/Open/open010.v2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open009_open009_v1_xml(mode, save_output, output_format):
    """
    Suffix open content in an xs:all group Allows any element in specified
    namespace at end of xs:all content
    """
    assert_bindings(
        schema="saxonData/Open/open009.xsd",
        instance="saxonData/Open/open009.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open009_open009_v2_xml(mode, save_output, output_format):
    """
    Suffix open content in an xs:all group Allows any element in specified
    namespace at end of xs:all content
    """
    assert_bindings(
        schema="saxonData/Open/open009.xsd",
        instance="saxonData/Open/open009.v2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open008_open008_v1_xml(mode, save_output, output_format):
    """
    Interleaved open content in an xs:all group Allows any element in
    specified namespace anywhere in xs:all content
    """
    assert_bindings(
        schema="saxonData/Open/open008.xsd",
        instance="saxonData/Open/open008.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open008_open008_v2_xml(mode, save_output, output_format):
    """
    Interleaved open content in an xs:all group Allows any element in
    specified namespace anywhere in xs:all content
    """
    assert_bindings(
        schema="saxonData/Open/open008.xsd",
        instance="saxonData/Open/open008.v2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open008_open008_v3_xml(mode, save_output, output_format):
    """
    Interleaved open content in an xs:all group Allows any element in
    specified namespace anywhere in xs:all content
    """
    assert_bindings(
        schema="saxonData/Open/open008.xsd",
        instance="saxonData/Open/open008.v3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open007_open007_v1_xml(mode, save_output, output_format):
    """
    Interleaved open content within a counting content model Designed to
    test that counting still works correctly.
    """
    assert_bindings(
        schema="saxonData/Open/open007.xsd",
        instance="saxonData/Open/open007.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open007_open007_v2_xml(mode, save_output, output_format):
    """
    Interleaved open content within a counting content model Designed to
    test that counting still works correctly.
    """
    assert_bindings(
        schema="saxonData/Open/open007.xsd",
        instance="saxonData/Open/open007.v2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open006_open006_v1_xml(mode, save_output, output_format):
    """
    Basic interleaved open content using defaultOpenContent definition
    Allows any element in specified namespace anywhere in content. Same as
    open005 except for the schema.
    """
    assert_bindings(
        schema="saxonData/Open/open006.xsd",
        instance="saxonData/Open/open005.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open006_open006_v2_xml(mode, save_output, output_format):
    """
    Basic interleaved open content using defaultOpenContent definition
    Allows any element in specified namespace anywhere in content. Same as
    open005 except for the schema.
    """
    assert_bindings(
        schema="saxonData/Open/open006.xsd",
        instance="saxonData/Open/open005.v2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open006_open006_v3_xml(mode, save_output, output_format):
    """
    Basic interleaved open content using defaultOpenContent definition
    Allows any element in specified namespace anywhere in content. Same as
    open005 except for the schema.
    """
    assert_bindings(
        schema="saxonData/Open/open006.xsd",
        instance="saxonData/Open/open005.v3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open006_open006_v4_xml(mode, save_output, output_format):
    """
    Basic interleaved open content using defaultOpenContent definition
    Allows any element in specified namespace anywhere in content. Same as
    open005 except for the schema.
    """
    assert_bindings(
        schema="saxonData/Open/open006.xsd",
        instance="saxonData/Open/open005.v4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open005_open005_v1_xml(mode, save_output, output_format):
    """
    Basic interleaved open content Allows any element in specified
    namespace anywhere in content
    """
    assert_bindings(
        schema="saxonData/Open/open005.xsd",
        instance="saxonData/Open/open005.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open005_open005_v2_xml(mode, save_output, output_format):
    """
    Basic interleaved open content Allows any element in specified
    namespace anywhere in content
    """
    assert_bindings(
        schema="saxonData/Open/open005.xsd",
        instance="saxonData/Open/open005.v2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open005_open005_v3_xml(mode, save_output, output_format):
    """
    Basic interleaved open content Allows any element in specified
    namespace anywhere in content
    """
    assert_bindings(
        schema="saxonData/Open/open005.xsd",
        instance="saxonData/Open/open005.v3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open005_open005_v4_xml(mode, save_output, output_format):
    """
    Basic interleaved open content Allows any element in specified
    namespace anywhere in content
    """
    assert_bindings(
        schema="saxonData/Open/open005.xsd",
        instance="saxonData/Open/open005.v4.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open004_open004_v1_xml(mode, save_output, output_format):
    """
    mode="none" takes precedence over default open content Open content
    not allowed.
    """
    assert_bindings(
        schema="saxonData/Open/open004.xsd",
        instance="saxonData/Open/open004.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open003_open003_v1_xml(mode, save_output, output_format):
    """
    Explicit open content takes precedence over default open content
    Different namespaces for the local open content and default open
    content wildcards.
    """
    assert_bindings(
        schema="saxonData/Open/open003.xsd",
        instance="saxonData/Open/open003.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open002_open002_v1_xml(mode, save_output, output_format):
    """
    Suffixed open content defined by defaultOpenContent element Same as
    open001 except for the schema.
    """
    assert_bindings(
        schema="saxonData/Open/open002.xsd",
        instance="saxonData/Open/open001.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open002_open002_v2_xml(mode, save_output, output_format):
    """
    Suffixed open content defined by defaultOpenContent element Same as
    open001 except for the schema.
    """
    assert_bindings(
        schema="saxonData/Open/open002.xsd",
        instance="saxonData/Open/open001.v2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open002_open002_v3_xml(mode, save_output, output_format):
    """
    Suffixed open content defined by defaultOpenContent element Same as
    open001 except for the schema.
    """
    assert_bindings(
        schema="saxonData/Open/open002.xsd",
        instance="saxonData/Open/open001.v3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open001_open001_v1_xml(mode, save_output, output_format):
    """
    Basic suffixed open content Allows any element in specified namespace
    at end of content
    """
    assert_bindings(
        schema="saxonData/Open/open001.xsd",
        instance="saxonData/Open/open001.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open001_open001_v2_xml(mode, save_output, output_format):
    """
    Basic suffixed open content Allows any element in specified namespace
    at end of content
    """
    assert_bindings(
        schema="saxonData/Open/open001.xsd",
        instance="saxonData/Open/open001.v2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_open001_open001_v3_xml(mode, save_output, output_format):
    """
    Basic suffixed open content Allows any element in specified namespace
    at end of content
    """
    assert_bindings(
        schema="saxonData/Open/open001.xsd",
        instance="saxonData/Open/open001.v3.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_over030_over030_v01_xml(mode, save_output, output_format):
    """
    Override a schema document with top-level annotation See W3C bug
    20784. Test case supplied by Norm Walsh.
    """
    assert_bindings(
        schema="saxonData/Override/over030.xsd",
        instance="saxonData/Override/over030.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_over029_over029_v01_xml(mode, save_output, output_format):
    """
    Interaction of xs:override and xs:import. Test case from Priscilla
    Walmsley The xs:override contains a reference to a type in an imported
    schema document, which is not imported into the overridden schema
    document. See Saxon bug 1505 and W3C bug 17574
    """
    assert_bindings(
        schema="saxonData/Override/over029.xsd",
        instance="saxonData/Override/over029.v01.xml",
        class_name="Order",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_over028_over028_v01_xml(mode, save_output, output_format):
    """
    Simple override test. Test case from Priscilla Walmsley Override a
    simpleType
    """
    assert_bindings(
        schema="saxonData/Override/over028a.xsd",
        instance="saxonData/Override/over028.v01.xml",
        class_name="NewSize",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_over023_over023_v01_xml(mode, save_output, output_format):
    """
    A permissible circular xs:override A permissible circular xs:override
    (doesn't work in Saxon 9.3)
    """
    assert_bindings(
        schema="saxonData/Override/over023.xsd",
        instance="saxonData/Override/over001.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_over020_over020_v01_xml(mode, save_output, output_format):
    """
    Indirect chameleon Override declaration Indirect chameleon Override
    declaration (uses over019)
    """
    assert_bindings(
        schema="saxonData/Override/over020.xsd",
        instance="saxonData/Override/over019.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_over019_over019_v01_xml(mode, save_output, output_format):
    """
    Chameleon Override declaration Chameleon Override declaration
    """
    assert_bindings(
        schema="saxonData/Override/over019.xsd",
        instance="saxonData/Override/over019.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_over018_over018_v01_xml(mode, save_output, output_format):
    """
    Override declaration in a target namespace Override declaration in a
    target namespace
    """
    assert_bindings(
        schema="saxonData/Override/over018.xsd",
        instance="saxonData/Override/over018.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_over015_over015_v01_xml(mode, save_output, output_format):
    """
    Override a notation Override a notation
    """
    assert_bindings(
        schema="saxonData/Override/over015.xsd",
        instance="saxonData/Override/over015.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="namespaces",
    )


def test_over015_over015_v02_xml(mode, save_output, output_format):
    """
    Override a notation Override a notation
    """
    assert_bindings(
        schema="saxonData/Override/over015.xsd",
        instance="saxonData/Override/over015.v02.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="namespaces",
    )


def test_over012_over012_v01_xml(mode, save_output, output_format):
    """
    Override a complex type Override a complex type
    """
    assert_bindings(
        schema="saxonData/Override/over012.xsd",
        instance="saxonData/Override/over012.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_over010_over010_v01_xml(mode, save_output, output_format):
    """
    Override a simple type Override a simple type
    """
    assert_bindings(
        schema="saxonData/Override/over010.xsd",
        instance="saxonData/Override/over010.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_over009_over009_v01_xml(mode, save_output, output_format):
    """
    Double override Double override. Depends on schema documents in
    over003
    """
    assert_bindings(
        schema="saxonData/Override/over009.xsd",
        instance="saxonData/Override/over009.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_over008_over008_v01_xml(mode, save_output, output_format):
    """
    xs:override of an attribute group declaration xs:override of an
    attribute group declaration
    """
    assert_bindings(
        schema="saxonData/Override/over008.xsd",
        instance="saxonData/Override/over008.v01.xml",
        class_name="Section",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_over007_over007_v01_xml(mode, save_output, output_format):
    """
    xs:override of a model group declaration xs:override of model group
    declaration
    """
    assert_bindings(
        schema="saxonData/Override/over007.xsd",
        instance="saxonData/Override/over007.v01.xml",
        class_name="Section",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_over006_over006_v01_xml(mode, save_output, output_format):
    """
    xs:override of a self-referential element declaration xs:override of
    self-referential element declaration
    """
    assert_bindings(
        schema="saxonData/Override/over006.xsd",
        instance="saxonData/Override/over006.v01.xml",
        class_name="Section",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_over005_over005_v01_xml(mode, save_output, output_format):
    """
    xs:override of an attribute declaration xs:override of an attribute
    declaration
    """
    assert_bindings(
        schema="saxonData/Override/over005.xsd",
        instance="saxonData/Override/over005.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_over004_over004_v01_xml(mode, save_output, output_format):
    """
    xs:override including a declaration outside the xs:override. Depends
    on over003 xs:override including a declaration outside the xs:override
    """
    assert_bindings(
        schema="saxonData/Override/over004.xsd",
        instance="saxonData/Override/over003.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_over003_over003_v01_xml(mode, save_output, output_format):
    """
    xs:override including a declaration which overrides nothing in the
    overridden schema xs:override including a declaration which overrides
    nothing in the overridden schema
    """
    assert_bindings(
        schema="saxonData/Override/over003.xsd",
        instance="saxonData/Override/over003.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_over002_over002_v01_xml(mode, save_output, output_format):
    """
    xs:override overriding an element declaration which is referenced in
    the overridden schema doc xs:override overriding an element
    declaration which is referenced in the overridden schema doc
    """
    assert_bindings(
        schema="saxonData/Override/over002.xsd",
        instance="saxonData/Override/over002.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_over001_over001_v01_xml(mode, save_output, output_format):
    """
    xs:override overriding an element declaration xs:override overriding
    an element declaration
    """
    assert_bindings(
        schema="saxonData/Override/over001.xsd",
        instance="saxonData/Override/over001.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_simple086_simple086_v01_xml(mode, save_output, output_format):
    """
    Duration seconds component requires a digit before and after the
    decimal point The BNF for the lexical space in XSD 1.1 (part 2, §
    3.3.6.2) suggests that the seconds component can start or end with a
    decimal separator, but this disagrees with the regular expressions in
    the same section. The BNF is believed to be in error.
    """
    assert_bindings(
        schema="saxonData/Simple/simple086.xsd",
        instance="saxonData/Simple/simple086.v01.xml",
        class_name="Elem",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_simple085_simple085_v01_xml(mode, save_output, output_format):
    """
    Union derived by restriction with a pattern facet Pattern facet
    applies after doing whitespace processing defined in the member type
    against which validation succeeded
    """
    assert_bindings(
        schema="saxonData/Simple/simple085.xsd",
        instance="saxonData/Simple/simple085.v01.xml",
        class_name="Elem",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_simple050_simple050_v01_xml(mode, save_output, output_format):
    """
    Use of xs:anyAtomicType Tests use of xs:anyAtomicType as the type of
    an element declaration
    """
    assert_bindings(
        schema="saxonData/Simple/simple050.xsd",
        instance="saxonData/Simple/simple050.v01.xml",
        class_name="E",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_simple050_simple050_v02_xml(mode, save_output, output_format):
    """
    Use of xs:anyAtomicType Tests use of xs:anyAtomicType as the type of
    an element declaration
    """
    assert_bindings(
        schema="saxonData/Simple/simple050.xsd",
        instance="saxonData/Simple/simple050.v02.xml",
        class_name="E",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_simple046_simple046_v01_xml(mode, save_output, output_format):
    """
    Hyphens in regular expressions Tests use of hyphens in regular
    expressions
    """
    assert_bindings(
        schema="saxonData/Simple/simple046.xsd",
        instance="saxonData/Simple/simple046.v01.xml",
        class_name="E",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_simple045_simple045_v01_xml(mode, save_output, output_format):
    """
    Hyphens in regular expressions Tests use of hyphens in regular
    expressions
    """
    assert_bindings(
        schema="saxonData/Simple/simple045.xsd",
        instance="saxonData/Simple/simple045.v01.xml",
        class_name="E",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_simple044_simple044_v01_xml(mode, save_output, output_format):
    """
    Hyphens in regular expressions Tests use of hyphens in regular
    expressions
    """
    assert_bindings(
        schema="saxonData/Simple/simple044.xsd",
        instance="saxonData/Simple/simple044.v01.xml",
        class_name="E",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_simple040_simple040_v01_xml(mode, save_output, output_format):
    """
    Hyphens in regular expressions Tests use of hyphens in regular
    expressions
    """
    assert_bindings(
        schema="saxonData/Simple/simple040.xsd",
        instance="saxonData/Simple/simple040.v01.xml",
        class_name="E",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_simple022_simple022_v01_xml(mode, save_output, output_format):
    """
    Enumeration value OK if "equal or identical", so NaN is accepted. See
    bug 9196 Enumeration value OK if "equal or identical", so NaN is
    accepted. See bug 9196
    """
    assert_bindings(
        schema="saxonData/Simple/simple022.xsd",
        instance="saxonData/Simple/simple022.v01.xml",
        class_name="Price",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_simple022_simple022_v02_xml(mode, save_output, output_format):
    """
    Enumeration value OK if "equal or identical", so NaN is accepted. See
    bug 9196 Enumeration value OK if "equal or identical", so NaN is
    accepted. See bug 9196
    """
    assert_bindings(
        schema="saxonData/Simple/simple022.xsd",
        instance="saxonData/Simple/simple022.v02.xml",
        class_name="Price",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_simple022_simple022_v03_xml(mode, save_output, output_format):
    """
    Enumeration value OK if "equal or identical", so NaN is accepted. See
    bug 9196 Enumeration value OK if "equal or identical", so NaN is
    accepted. See bug 9196
    """
    assert_bindings(
        schema="saxonData/Simple/simple022.xsd",
        instance="saxonData/Simple/simple022.v03.xml",
        class_name="Price",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_simple016_simple016_v01_xml(mode, save_output, output_format):
    """
    xsi:type OK to select a member of a union only if there are no
    restriction facets xsi:type OK to select a member of a union only if
    there are no restriction facets
    """
    assert_bindings(
        schema="saxonData/Simple/simple016.xsd",
        instance="saxonData/Simple/simple016.v01.xml",
        class_name="Book",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_simple013_simple013_v01_xml(mode, save_output, output_format):
    """
    Type D is substitutable for union(X,DT) when DT is union (D,T) Tests
    substitutability of transitive membership of the union
    """
    assert_bindings(
        schema="saxonData/Simple/simple013.xsd",
        instance="saxonData/Simple/simple013.v01.xml",
        class_name="Book",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_simple012_simple012_v01_xml(mode, save_output, output_format):
    """
    Type X is substitutable for union(X,Y) when X is itself a union type
    Union is substitutable by one of the member types when that member
    type is a union
    """
    assert_bindings(
        schema="saxonData/Simple/simple012.xsd",
        instance="saxonData/Simple/simple012.v01.xml",
        class_name="Book",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_simple012_simple012_v02_xml(mode, save_output, output_format):
    """
    Type X is substitutable for union(X,Y) when X is itself a union type
    Union is substitutable by one of the member types when that member
    type is a union
    """
    assert_bindings(
        schema="saxonData/Simple/simple012.xsd",
        instance="saxonData/Simple/simple012.v02.xml",
        class_name="Book",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_simple010_simple010_v01_xml(mode, save_output, output_format):
    """
    Type X is substitutable for union(X,Y) Union is substitutable by one
    of the member types
    """
    assert_bindings(
        schema="saxonData/Simple/simple010.xsd",
        instance="saxonData/Simple/simple010.v01.xml",
        class_name="Book",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_simple003_simple003_v01_xml(mode, save_output, output_format):
    """
    Test that simpleType/@final = extension is allowed Depends on
    resolution of spec bug 2074
    """
    assert_bindings(
        schema="saxonData/Simple/simple003.xsd",
        instance="saxonData/Simple/simple003.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_simple002_simple002_v01_xml(mode, save_output, output_format):
    """
    +INF allowed in xs:float lexical space +INF allowed in xs:float
    lexical space in XSD 1.1
    """
    assert_bindings(
        schema="saxonData/Simple/simple002.xsd",
        instance="saxonData/Simple/simple001.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_simple001_simple001_v01_xml(mode, save_output, output_format):
    """
    +INF allowed in xs:double lexical space +INF allowed in xs:double
    lexical space in XSD 1.1
    """
    assert_bindings(
        schema="saxonData/Simple/simple001.xsd",
        instance="saxonData/Simple/simple001.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_subsgroup003_subsgroup003_v1_xml(mode, save_output, output_format):
    """
    Tests to show an a substitution group with declarations in different
    namespaces Substitution group has an abstract owner in one namespace,
    two concrete members in different namespaces. Should work with XSD 1.0
    or 1.1. Posted as a problem on StackOverflow ref 9495098 on 29 Feb
    2012.
    """
    assert_bindings(
        schema="saxonData/Subsgroup/subsgroup003a.xsd",
        instance="saxonData/Subsgroup/subsgroup003.xml",
        class_name="Command",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_subsgroup002_subsgroup002_v1_xml(mode, save_output, output_format):
    """
    Tests to show an element declaration can be in multiple substitution
    groups Element substitutable for another in more than one way, both
    valid
    """
    assert_bindings(
        schema="saxonData/Subsgroup/subsgroup002.xsd",
        instance="saxonData/Subsgroup/subsgroup001.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_subsgroup001_subsgroup001_v1_xml(mode, save_output, output_format):
    """
    Tests to show an element declaration can be in multiple substitution
    groups Tests to show an element declaration can be in multiple
    substitution groups
    """
    assert_bindings(
        schema="saxonData/Subsgroup/subsgroup001.xsd",
        instance="saxonData/Subsgroup/subsgroup001.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_target003_target003_v1_xml(mode, save_output, output_format):
    """
    Simple use of targetNamespace on a local attribute declaration Simple
    use of targetNamespace on a local attribute declaration
    DocumentationReference(annotation=[], type_value=<TypeType.LOCATOR:
    'locator'>,
    href='../common/XSD1_1TestCategories.xml#xsd1_1-NewLocalDecl-
    TargNSOnAttrDecl', other_attributes={})
    """
    assert_bindings(
        schema="saxonData/TargetNS/target003.xsd",
        instance="saxonData/TargetNS/target003.v1.xml",
        class_name="Parent",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_target001_target001_v1_xml(mode, save_output, output_format):
    """
    Simple use of targetNamespace on a local element declaration Simple
    use of targetNamespace on a local element declaration
    """
    assert_bindings(
        schema="saxonData/TargetNS/target001.xsd",
        instance="saxonData/TargetNS/target001.v1.xml",
        class_name="Parent",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_vc024_11_vc024_v1_xml(mode, save_output, output_format):
    """
    Simple assertion on an attribute value, ignored under XSD 1.0 Simple
    assertion on an attribute value, ignored under XSD 1.0
    """
    assert_bindings(
        schema="saxonData/VC/vc024.xsd",
        instance="saxonData/VC/vc001.v1.xml",
        class_name="Temp",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_vc024_11_vc024_n1_xml(mode, save_output, output_format):
    """
    Simple assertion on an attribute value, ignored under XSD 1.0 Simple
    assertion on an attribute value, ignored under XSD 1.0
    """
    assert_bindings(
        schema="saxonData/VC/vc024.xsd",
        instance="saxonData/VC/vc001.n1.xml",
        class_name="Temp",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_vc023_vc023_v1_xml(mode, save_output, output_format):
    """
    vc:facetUnavailable with a mix of known and unknown facet
    vc:facetUnavailable with a mix of known and unknown facets
    """
    assert_bindings(
        schema="saxonData/VC/vc023.xsd",
        instance="saxonData/VC/vc010.v1.xml",
        class_name="Temp",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_vc020_vc020_v1_xml(mode, save_output, output_format):
    """
    vc:facetAvailable with a known facet vc:facetAvailable with a known
    facet
    """
    assert_bindings(
        schema="saxonData/VC/vc020.xsd",
        instance="saxonData/VC/vc010.v1.xml",
        class_name="Temp",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_vc014_vc014_v1_xml(mode, save_output, output_format):
    """
    Conditional use of xs:error controlled by vc:typeAvailable Conditional
    use of xs:error controlled by vc:typeAvailable
    """
    assert_bindings(
        schema="saxonData/VC/vc014.xsd",
        instance="saxonData/VC/vc014.v1.xml",
        class_name="Temp",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_vc013_vc013_v1_xml(mode, save_output, output_format):
    """
    vc:typeUnavailable with a mix of known and unknown types
    vc:typeUnavailable with a mix of known and unknown types
    """
    assert_bindings(
        schema="saxonData/VC/vc013.xsd",
        instance="saxonData/VC/vc010.v1.xml",
        class_name="Temp",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_vc010_vc010_v1_xml(mode, save_output, output_format):
    """
    vc:typeAvailable with a known type vc:typeAvailable with a known type
    """
    assert_bindings(
        schema="saxonData/VC/vc010.xsd",
        instance="saxonData/VC/vc010.v1.xml",
        class_name="Temp",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_vc009_vc009_v1_xml(mode, save_output, output_format):
    """
    Misspelt vc: attribute has no effect Misspelt vc: attribute has no
    effect
    """
    assert_bindings(
        schema="saxonData/VC/vc009.xsd",
        instance="saxonData/VC/vc001.v1.xml",
        class_name="Temp",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_vc008_vc008_v1_xml(mode, save_output, output_format):
    """
    Empty vc:xx[un]available attributes have no effect Empty
    vc:xx[un]available attributes have no effect
    """
    assert_bindings(
        schema="saxonData/VC/vc008.xsd",
        instance="saxonData/VC/vc001.v1.xml",
        class_name="Temp",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_vc007_vc007_v1_xml(mode, save_output, output_format):
    """
    Include a schema document made empty by version control attributes
    Include a schema document made empty by version control attributes
    """
    assert_bindings(
        schema="saxonData/VC/vc007.xsd",
        instance="saxonData/VC/vc002.v1.xml",
        class_name="Temp",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_vc005_vc005_v1_xml(mode, save_output, output_format):
    """
    Use of version conditionals to ignore an (otherwise invalid)
    xs:include Use of version conditionals to ignore an (otherwise
    invalid) xs:include
    """
    assert_bindings(
        schema="saxonData/VC/vc005.xsd",
        instance="saxonData/VC/vc003.v1.xml",
        class_name="Temp",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_vc004_vc004_v1_xml(mode, save_output, output_format):
    """
    Use of version conditionals in an included schema document Use of
    version conditionals in an included schema document
    """
    assert_bindings(
        schema="saxonData/VC/vc004.xsd",
        instance="saxonData/VC/vc003.v1.xml",
        class_name="Temp",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_vc003_vc003_v1_xml(mode, save_output, output_format):
    """
    Test a hypothetical 5.0 feature ignored under XSD 1.1 Test a
    hypothetical 5.0 feature ignored under XSD 1.1
    """
    assert_bindings(
        schema="saxonData/VC/vc003.xsd",
        instance="saxonData/VC/vc003.v1.xml",
        class_name="Temp",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_vc002_vc002_v1_xml(mode, save_output, output_format):
    """
    Equivalent schemas with different formulations under XSD 1.0 and XSD
    1.1 Equivalent schemas with different formulations under XSD 1.0 and
    XSD 1.1
    """
    assert_bindings(
        schema="saxonData/VC/vc002.xsd",
        instance="saxonData/VC/vc002.v1.xml",
        class_name="Temp",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_vc001_vc001_v1_xml(mode, save_output, output_format):
    """
    Simple assertion on an attribute value, ignored under XSD 1.0 Simple
    assertion on an attribute value, ignored under XSD 1.0
    """
    assert_bindings(
        schema="saxonData/VC/vc001.xsd",
        instance="saxonData/VC/vc001.v1.xml",
        class_name="Temp",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_vc001_vc001_n1_xml(mode, save_output, output_format):
    """
    Simple assertion on an attribute value, ignored under XSD 1.0 Simple
    assertion on an attribute value, ignored under XSD 1.0
    """
    assert_bindings(
        schema="saxonData/VC/vc001.xsd",
        instance="saxonData/VC/vc001.n1.xml",
        class_name="Temp",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild083_wild083_v1_xml(mode, save_output, output_format):
    """
    Element Wildcard union with notQName="##defined" Tests the spec note:
    Note: When one of the wildcards has defined in {disallowed names} and
    the other does not, then defined is not included in the union. This
    may allow QNames that are not allowed by either wildcard. This is to
    ensure that all unions are expressible. If defined is intended to be
    included, then it is necessary to have it in both wildcards.
    """
    assert_bindings(
        schema="saxonData/Wild/wild083.xsd",
        instance="saxonData/Wild/wild083.v1.xml",
        class_name="E",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild082_wild082_v1_xml(mode, save_output, output_format):
    """
    Consistency of governing type declarations between locally-declared
    elements in a content model No violation of Element Declarations
    Consistent because the type tables are "the same"
    """
    assert_bindings(
        schema="saxonData/Wild/wild082.xsd",
        instance="saxonData/Wild/wild082.v1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild080_wild080_v1_xml(mode, save_output, output_format):
    """
    Consistency of governing type declarations between locally-declared
    elements and lax wildcards in a content model No violation of Element
    Declarations Consistent with a skip wildcard
    """
    assert_bindings(
        schema="saxonData/Wild/wild080.xsd",
        instance="saxonData/Wild/wild080.v1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild077_wild077_v1_xml(mode, save_output, output_format):
    """
    Consistency of governing type declarations between locally-declared
    elements and wildcards in a content model Violation of Element Locally
    Valid (Complex Type) Rule 5, not a problem with a skip wildcard
    """
    assert_bindings(
        schema="saxonData/Wild/wild077.xsd",
        instance="saxonData/Wild/wild075.v1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild077_wild077_n1_xml(mode, save_output, output_format):
    """
    Consistency of governing type declarations between locally-declared
    elements and wildcards in a content model Violation of Element Locally
    Valid (Complex Type) Rule 5, not a problem with a skip wildcard
    """
    assert_bindings(
        schema="saxonData/Wild/wild077.xsd",
        instance="saxonData/Wild/wild075.n1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild076_wild076_v1_xml(mode, save_output, output_format):
    """
    Consistency of governing type declarations between locally-declared
    elements and wildcards in a content model Violation of Element Locally
    Valid (Complex Type) Rule 5
    """
    assert_bindings(
        schema="saxonData/Wild/wild076.xsd",
        instance="saxonData/Wild/wild075.v1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild075_wild075_v1_xml(mode, save_output, output_format):
    """
    Consistency of governing type declarations between locally-declared
    elements and wildcards in a content model Violation of Element Locally
    Valid (Complex Type) Rule 5
    """
    assert_bindings(
        schema="saxonData/Wild/wild075.xsd",
        instance="saxonData/Wild/wild075.v1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild074_wild074_v1_xml(mode, save_output, output_format):
    """
    Test of openContent wildcards and substitution groups in xs:sequence
    content model Open Content with ##definedSibling
    """
    assert_bindings(
        schema="saxonData/Wild/wild074.xsd",
        instance="saxonData/Wild/wild074.v1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild073_wild073_v1_xml(mode, save_output, output_format):
    """
    Test of wildcards and substitution groups in xs:all content model
    Variant of wild072 without the ##definedSibling, for comparison
    """
    assert_bindings(
        schema="saxonData/Wild/wild073.xsd",
        instance="saxonData/Wild/wild072.v1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild073_wild073_v2_xml(mode, save_output, output_format):
    """
    Test of wildcards and substitution groups in xs:all content model
    Variant of wild072 without the ##definedSibling, for comparison
    """
    assert_bindings(
        schema="saxonData/Wild/wild073.xsd",
        instance="saxonData/Wild/wild072.n1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild073_wild073_v3_xml(mode, save_output, output_format):
    """
    Test of wildcards and substitution groups in xs:all content model
    Variant of wild072 without the ##definedSibling, for comparison
    """
    assert_bindings(
        schema="saxonData/Wild/wild073.xsd",
        instance="saxonData/Wild/wild072.n2.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild072_wild072_v1_xml(mode, save_output, output_format):
    """
    Test of notQName=##definedSibling with substitution groups in xs:all
    content model notQName=##definedSibling in an xs:all content model
    """
    assert_bindings(
        schema="saxonData/Wild/wild072.xsd",
        instance="saxonData/Wild/wild072.v1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild071_wild071_v1_xml(mode, save_output, output_format):
    """
    Basic test of notQName=##definedSibling with substitution groups
    notQName=##definedSibling in a sequence content model
    """
    assert_bindings(
        schema="saxonData/Wild/wild071.xsd",
        instance="saxonData/Wild/wild071.v1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild070_wild070_v1_xml(mode, save_output, output_format):
    """
    Basic test of notQName=##definedSibling notQName=##definedSibling in a
    sequence content model
    """
    assert_bindings(
        schema="saxonData/Wild/wild070.xsd",
        instance="saxonData/Wild/wild070.v1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild066_wild066_v1_xml(mode, save_output, output_format):
    """
    Element fails "dynamic EDC" test - lax wildcard Substitutability
    involving a union
    """
    assert_bindings(
        schema="saxonData/Wild/wild066.xsd",
        instance="saxonData/Wild/wild066.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild065_wild065_v1_xml(mode, save_output, output_format):
    """
    Element fails "dynamic EDC" test - lax wildcard Schema is valid,
    instance is not
    """
    assert_bindings(
        schema="saxonData/Wild/wild065.xsd",
        instance="saxonData/Wild/wild065.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild064_wild064_v1_xml(mode, save_output, output_format):
    """
    Element fails "dynamic EDC" test - lax wildcard Schema is valid,
    instance is not
    """
    assert_bindings(
        schema="saxonData/Wild/wild064.xsd",
        instance="saxonData/Wild/wild064.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild064_wild064_v2_xml(mode, save_output, output_format):
    """
    Element fails "dynamic EDC" test - lax wildcard Schema is valid,
    instance is not
    """
    assert_bindings(
        schema="saxonData/Wild/wild064.xsd",
        instance="saxonData/Wild/wild064.v2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild063_wild063_v1_xml(mode, save_output, output_format):
    """
    Element fails "dynamic EDC" test - lax wildcard Schema is valid,
    instance is not
    """
    assert_bindings(
        schema="saxonData/Wild/wild063.xsd",
        instance="saxonData/Wild/wild063.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild063_wild063_v2_xml(mode, save_output, output_format):
    """
    Element fails "dynamic EDC" test - lax wildcard Schema is valid,
    instance is not
    """
    assert_bindings(
        schema="saxonData/Wild/wild063.xsd",
        instance="saxonData/Wild/wild063.v2.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild062_wild062_v1_xml(mode, save_output, output_format):
    """
    Element fails "dynamic EDC" test - lax wildcard Schema is valid,
    instance is not
    """
    assert_bindings(
        schema="saxonData/Wild/wild062.xsd",
        instance="saxonData/Wild/wild062.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild060_wild060_v1_xml(mode, save_output, output_format):
    """
    Attribute Wildcard union with notQName=##defined Both wildcards
    specify notQName="##defined" so union is expressible
    """
    assert_bindings(
        schema="saxonData/Wild/wild060.xsd",
        instance="saxonData/Wild/wild058.v1.xml",
        class_name="Zing",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild060_wild060_v2_xml(mode, save_output, output_format):
    """
    Attribute Wildcard union with notQName=##defined Both wildcards
    specify notQName="##defined" so union is expressible
    """
    assert_bindings(
        schema="saxonData/Wild/wild060.xsd",
        instance="saxonData/Wild/wild058.n1.xml",
        class_name="Zing",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild059_wild059_v1_xml(mode, save_output, output_format):
    """
    Attribute Wildcard intersection with notQName=##defined One wildcard
    specifies notQName="##defined"
    """
    assert_bindings(
        schema="saxonData/Wild/wild059.xsd",
        instance="saxonData/Wild/wild058.v1.xml",
        class_name="Zing",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild058_wild058_v1_xml(mode, save_output, output_format):
    """
    Attribute Wildcard intersection with notQName=##defined Both wildcards
    specify notQName="##defined"
    """
    assert_bindings(
        schema="saxonData/Wild/wild058.xsd",
        instance="saxonData/Wild/wild058.v1.xml",
        class_name="Zing",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild056_wild056_v1_xml(mode, save_output, output_format):
    """
    Attribute Wildcard with notQName=##defined Valid restriction of
    wildcard
    """
    assert_bindings(
        schema="saxonData/Wild/wild056.xsd",
        instance="saxonData/Wild/wild055.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild055_wild055_v1_xml(mode, save_output, output_format):
    """
    Attribute Wildcard with notQName=##defined Valid restriction of
    wildcard
    """
    assert_bindings(
        schema="saxonData/Wild/wild055.xsd",
        instance="saxonData/Wild/wild055.v1.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild054_wild054_v1_xml(mode, save_output, output_format):
    """
    Attribute Wildcard with notQName=##defined Basic test of ##defined
    """
    assert_bindings(
        schema="saxonData/Wild/wild054.xsd",
        instance="saxonData/Wild/wild054.v1.xml",
        class_name="Zing",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild054_wild054_v2_xml(mode, save_output, output_format):
    """
    Attribute Wildcard with notQName=##defined Basic test of ##defined
    """
    assert_bindings(
        schema="saxonData/Wild/wild054.xsd",
        instance="saxonData/Wild/wild054.v2.xml",
        class_name="Zing",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild053_wild053_v1_xml(mode, save_output, output_format):
    """
    Element Wildcard with notQName=##defined Basic test of ##defined with
    multiple namespaces
    """
    assert_bindings(
        schema="saxonData/Wild/wild053.xsd",
        instance="saxonData/Wild/wild053.v1.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild053_wild053_v2_xml(mode, save_output, output_format):
    """
    Element Wildcard with notQName=##defined Basic test of ##defined with
    multiple namespaces
    """
    assert_bindings(
        schema="saxonData/Wild/wild053.xsd",
        instance="saxonData/Wild/wild053.v2.xml",
        class_name="Root",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild052_wild052_v1_xml(mode, save_output, output_format):
    """
    Element Wildcard with notQName=##defined Basic test of ##defined
    """
    assert_bindings(
        schema="saxonData/Wild/wild052.xsd",
        instance="saxonData/Wild/wild052.v1.xml",
        class_name="Zing",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild052_wild052_v2_xml(mode, save_output, output_format):
    """
    Element Wildcard with notQName=##defined Basic test of ##defined
    """
    assert_bindings(
        schema="saxonData/Wild/wild052.xsd",
        instance="saxonData/Wild/wild052.v2.xml",
        class_name="Zing",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild047_wild047_v1_xml(mode, save_output, output_format):
    """
    Element Wildcard union with notQName and notNamespace disallows the
    intersection of the disallowed QNames
    """
    assert_bindings(
        schema="saxonData/Wild/wild047.xsd",
        instance="saxonData/Wild/wild047.v1.xml",
        class_name="Computer",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild046_wild046_v1_xml(mode, save_output, output_format):
    """
    Wildcard union with notQName and notNamespace disallows the
    intersection of the disallowed QNames
    """
    assert_bindings(
        schema="saxonData/Wild/wild046.xsd",
        instance="saxonData/Wild/wild045.v1.xml",
        class_name="Computer",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild046_wild046_v2_xml(mode, save_output, output_format):
    """
    Wildcard union with notQName and notNamespace disallows the
    intersection of the disallowed QNames
    """
    assert_bindings(
        schema="saxonData/Wild/wild046.xsd",
        instance="saxonData/Wild/wild045.v2.xml",
        class_name="Computer",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild045_wild045_v1_xml(mode, save_output, output_format):
    """
    Wildcard union with notQName disallows the intersection of the
    disallowed QNames
    """
    assert_bindings(
        schema="saxonData/Wild/wild045.xsd",
        instance="saxonData/Wild/wild045.v1.xml",
        class_name="Computer",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild045_wild045_v2_xml(mode, save_output, output_format):
    """
    Wildcard union with notQName disallows the intersection of the
    disallowed QNames
    """
    assert_bindings(
        schema="saxonData/Wild/wild045.xsd",
        instance="saxonData/Wild/wild045.v2.xml",
        class_name="Computer",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild044_wild044_v1_xml(mode, save_output, output_format):
    """
    Wildcard intersection with notQName disallows the union of the
    disallowed QNames
    """
    assert_bindings(
        schema="saxonData/Wild/wild044.xsd",
        instance="saxonData/Wild/wild044.v1.xml",
        class_name="Computer",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild043_wild043_v1_xml(mode, save_output, output_format):
    """
    Wildcard intersection with notQName disallows the union of the
    disallowed QNames
    """
    assert_bindings(
        schema="saxonData/Wild/wild043.xsd",
        instance="saxonData/Wild/wild043.v1.xml",
        class_name="Computer",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild042_wild042_v1_xml(mode, save_output, output_format):
    """
    xsi attribute wildcards are allowed There's no rule to stop non-
    standard attributes in the xsi namespace being introduced by wildcard
    """
    assert_bindings(
        schema="saxonData/Wild/wild042.xsd",
        instance="saxonData/Wild/wild042.v1.xml",
        class_name="Computer",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild040_wild040_v1_xml(mode, save_output, output_format):
    """
    Banning xsi attributes has no effect xsi:type is validated without
    reference to attribute uses or wildcards
    """
    assert_bindings(
        schema="saxonData/Wild/wild040.xsd",
        instance="saxonData/Wild/wild040.v1.xml",
        class_name="Computer",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild030_wild030_v1_xml(mode, save_output, output_format):
    """
    Example from the spec: restricting away a child element that overlaps
    a wildcard No speaker element allowed on the subtype
    """
    assert_bindings(
        schema="saxonData/Wild/wild030.xsd",
        instance="saxonData/Wild/wild030.v1.xml",
        class_name="Computer",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild030_wild030_v2_xml(mode, save_output, output_format):
    """
    Example from the spec: restricting away a child element that overlaps
    a wildcard No speaker element allowed on the subtype
    """
    assert_bindings(
        schema="saxonData/Wild/wild030.xsd",
        instance="saxonData/Wild/wild030.v2.xml",
        class_name="Computer",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild029_wild029_v1_xml(mode, save_output, output_format):
    """
    Test of xs:any with notQName attribute in an xs:sequence model group
    Allows any child element except for a
    """
    assert_bindings(
        schema="saxonData/Wild/wild029.xsd",
        instance="saxonData/Wild/wild029.v1.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild028_wild028_v1_xml(mode, save_output, output_format):
    """
    Basic test of xs:any with notQName attribute Allows any child element
    except for xml:space or xml:id
    """
    assert_bindings(
        schema="saxonData/Wild/wild028.xsd",
        instance="saxonData/Wild/wild028.v1.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild027_wild027_v1_xml(mode, save_output, output_format):
    """
    Basic test of xs:anyAttribute with notQName attribute Allows any
    attribute except for xml:space or xml:id
    """
    assert_bindings(
        schema="saxonData/Wild/wild027.xsd",
        instance="saxonData/Wild/wild027.v1.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild026_wild026_v1_xml(mode, save_output, output_format):
    """
    Wildcard intersection Type allows anything allowed by all the
    attribute wildcards
    """
    assert_bindings(
        schema="saxonData/Wild/wild026.xsd",
        instance="saxonData/Wild/wild025.v1.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild025_wild025_v1_xml(mode, save_output, output_format):
    """
    Wildcard intersection Type allows anything allowed by all the
    attribute wildcards
    """
    assert_bindings(
        schema="saxonData/Wild/wild025.xsd",
        instance="saxonData/Wild/wild025.v1.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild024_wild024_v1_xml(mode, save_output, output_format):
    """
    Wildcard intersection Type allows anything allowed by all the
    attribute wildcards
    """
    assert_bindings(
        schema="saxonData/Wild/wild024.xsd",
        instance="saxonData/Wild/wild023.v1.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild024_wild024_v2_xml(mode, save_output, output_format):
    """
    Wildcard intersection Type allows anything allowed by all the
    attribute wildcards
    """
    assert_bindings(
        schema="saxonData/Wild/wild024.xsd",
        instance="saxonData/Wild/wild024.v2.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild023_wild023_v1_xml(mode, save_output, output_format):
    """
    Wildcard intersection Type allows anything allowed by all the
    attribute wildcards
    """
    assert_bindings(
        schema="saxonData/Wild/wild023.xsd",
        instance="saxonData/Wild/wild023.v1.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild019_wild019_v1_xml(mode, save_output, output_format):
    """
    Valid restriction of wildcards Restricted type disallows more
    namespaces than the base type disallows
    """
    assert_bindings(
        schema="saxonData/Wild/wild019.xsd",
        instance="saxonData/Wild/wild017.v1.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild018_wild018_v1_xml(mode, save_output, output_format):
    """
    Valid restriction of wildcards Restricted type disallows more
    namespaces than the base type disallows
    """
    assert_bindings(
        schema="saxonData/Wild/wild018.xsd",
        instance="saxonData/Wild/wild017.v1.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild017_wild017_v1_xml(mode, save_output, output_format):
    """
    Valid restriction of wildcards Restricted type disallows more
    namespaces than the base type disallows
    """
    assert_bindings(
        schema="saxonData/Wild/wild017.xsd",
        instance="saxonData/Wild/wild017.v1.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild016_wild016_v1_xml(mode, save_output, output_format):
    """
    Union of two wildcards using namespace and notNamespace respectively
    The union allows adam, eve, and abel but not cain. Inversion of
    wild015.xsd.
    """
    assert_bindings(
        schema="saxonData/Wild/wild016.xsd",
        instance="saxonData/Wild/wild015.v1.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild015_wild015_v1_xml(mode, save_output, output_format):
    """
    Union of two wildcards using namespace and notNamespace respectively
    The union allows adam, eve, and abel but not cain
    """
    assert_bindings(
        schema="saxonData/Wild/wild015.xsd",
        instance="saxonData/Wild/wild015.v1.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild014_wild014_v1_xml(mode, save_output, output_format):
    """
    Union of two wildcards using notNamespace The union allows abel but
    not cain
    """
    assert_bindings(
        schema="saxonData/Wild/wild014.xsd",
        instance="saxonData/Wild/wild014.v1.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild013_wild013_v1_xml(mode, save_output, output_format):
    """
    Union of two wildcards using notNamespace The union allows anything
    """
    assert_bindings(
        schema="saxonData/Wild/wild013.xsd",
        instance="saxonData/Wild/wild013.v1.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild012_wild012_v1_xml(mode, save_output, output_format):
    """
    Test of xs:any with notNamespace = ##targetNamespace in a namespaced
    schema Allows any child so long as it's in a namespace other than
    target
    """
    assert_bindings(
        schema="saxonData/Wild/wild012.xsd",
        instance="saxonData/Wild/wild010.v1.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild012_wild012_v2_xml(mode, save_output, output_format):
    """
    Test of xs:any with notNamespace = ##targetNamespace in a namespaced
    schema Allows any child so long as it's in a namespace other than
    target
    """
    assert_bindings(
        schema="saxonData/Wild/wild012.xsd",
        instance="saxonData/Wild/wild010.v2.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild011_wild011_v1_xml(mode, save_output, output_format):
    """
    Test of xs:anyAttribute with notNamespace = ##targetNamespace in a
    chameleon schema Allows any attribute so long as it's in a namespace
    other than target
    """
    assert_bindings(
        schema="saxonData/Wild/wild011.xsd",
        instance="saxonData/Wild/wild009.v1.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild011_wild011_v2_xml(mode, save_output, output_format):
    """
    Test of xs:anyAttribute with notNamespace = ##targetNamespace in a
    chameleon schema Allows any attribute so long as it's in a namespace
    other than target
    """
    assert_bindings(
        schema="saxonData/Wild/wild011.xsd",
        instance="saxonData/Wild/wild009.v2.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild010_wild010_v1_xml(mode, save_output, output_format):
    """
    Test of xs:any with notNamespace = ##targetNamespace in a namespaced
    schema Allows any child so long as it's in a namespace other than
    target
    """
    assert_bindings(
        schema="saxonData/Wild/wild010.xsd",
        instance="saxonData/Wild/wild010.v1.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild010_wild010_v2_xml(mode, save_output, output_format):
    """
    Test of xs:any with notNamespace = ##targetNamespace in a namespaced
    schema Allows any child so long as it's in a namespace other than
    target
    """
    assert_bindings(
        schema="saxonData/Wild/wild010.xsd",
        instance="saxonData/Wild/wild010.v2.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild009_wild009_v1_xml(mode, save_output, output_format):
    """
    Test of xs:anyAttribute with notNamespace = ##targetNamespace in a
    namespaced schema Allows any attribute so long as it's in a namespace
    other than target
    """
    assert_bindings(
        schema="saxonData/Wild/wild009.xsd",
        instance="saxonData/Wild/wild009.v1.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild009_wild009_v2_xml(mode, save_output, output_format):
    """
    Test of xs:anyAttribute with notNamespace = ##targetNamespace in a
    namespaced schema Allows any attribute so long as it's in a namespace
    other than target
    """
    assert_bindings(
        schema="saxonData/Wild/wild009.xsd",
        instance="saxonData/Wild/wild009.v2.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild006_wild006_v1_xml(mode, save_output, output_format):
    """
    Basic test of xs:any with notNamespace = ##targetNamespace in a no-
    namespace schema Allows any child so long as it's in a namespace
    """
    assert_bindings(
        schema="saxonData/Wild/wild006.xsd",
        instance="saxonData/Wild/wild004.v1.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild006_wild006_v2_xml(mode, save_output, output_format):
    """
    Basic test of xs:any with notNamespace = ##targetNamespace in a no-
    namespace schema Allows any child so long as it's in a namespace
    """
    assert_bindings(
        schema="saxonData/Wild/wild006.xsd",
        instance="saxonData/Wild/wild004.v2.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild005_wild005_v1_xml(mode, save_output, output_format):
    """
    Basic test of xs:anyAttribute with notNamespace = ##targetNamespace in
    a no-namespace schema Allows any attribute so long as it's in a
    namespace
    """
    assert_bindings(
        schema="saxonData/Wild/wild005.xsd",
        instance="saxonData/Wild/wild003.v1.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild005_wild005_v2_xml(mode, save_output, output_format):
    """
    Basic test of xs:anyAttribute with notNamespace = ##targetNamespace in
    a no-namespace schema Allows any attribute so long as it's in a
    namespace
    """
    assert_bindings(
        schema="saxonData/Wild/wild005.xsd",
        instance="saxonData/Wild/wild003.v2.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild004_wild004_v1_xml(mode, save_output, output_format):
    """
    Basic test of xs:any with notNamespace = ##local Allows any child so
    long as it's in a namespace
    """
    assert_bindings(
        schema="saxonData/Wild/wild004.xsd",
        instance="saxonData/Wild/wild004.v1.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild004_wild004_v2_xml(mode, save_output, output_format):
    """
    Basic test of xs:any with notNamespace = ##local Allows any child so
    long as it's in a namespace
    """
    assert_bindings(
        schema="saxonData/Wild/wild004.xsd",
        instance="saxonData/Wild/wild004.v2.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild003_wild003_v1_xml(mode, save_output, output_format):
    """
    Basic test of xs:anyAttribute with notNamespace = ##local Allows any
    attribute so long as it's in a namespace
    """
    assert_bindings(
        schema="saxonData/Wild/wild003.xsd",
        instance="saxonData/Wild/wild003.v1.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild003_wild003_v2_xml(mode, save_output, output_format):
    """
    Basic test of xs:anyAttribute with notNamespace = ##local Allows any
    attribute so long as it's in a namespace
    """
    assert_bindings(
        schema="saxonData/Wild/wild003.xsd",
        instance="saxonData/Wild/wild003.v2.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild002_wild002_v1_xml(mode, save_output, output_format):
    """
    Basic test of xs:anyAttribute with notNamespace attribute Allows any
    attribute except for two designated namespaces
    """
    assert_bindings(
        schema="saxonData/Wild/wild002.xsd",
        instance="saxonData/Wild/wild002.v1.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild002_wild002_v2_xml(mode, save_output, output_format):
    """
    Basic test of xs:anyAttribute with notNamespace attribute Allows any
    attribute except for two designated namespaces
    """
    assert_bindings(
        schema="saxonData/Wild/wild002.xsd",
        instance="saxonData/Wild/wild002.v2.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild001_wild001_v1_xml(mode, save_output, output_format):
    """
    Basic test of xs:anyAttribute with notNamespace attribute Allows any
    attribute except for two designated namespaces
    """
    assert_bindings(
        schema="saxonData/Wild/wild001.xsd",
        instance="saxonData/Wild/wild001.v1.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_wild001_wild001_v2_xml(mode, save_output, output_format):
    """
    Basic test of xs:anyAttribute with notNamespace attribute Allows any
    attribute except for two designated namespaces
    """
    assert_bindings(
        schema="saxonData/Wild/wild001.xsd",
        instance="saxonData/Wild/wild001.v2.xml",
        class_name="Eden",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_xv100notc_xv100notc_notc_xml(mode, save_output, output_format):
    r"""
    Test which characters match \C in a regex Name characters in XML 1.1
    are the same as 1.05e
    """
    assert_bindings(
        schema="saxonData/XmlVersions/xv100.notc.xsd",
        instance="saxonData/XmlVersions/xv100.notc.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_xv100noti_xv100noti_noti_xml(mode, save_output, output_format):
    r"""
    Test which characters match \I in a regex Name characters in XML 1.1
    are the same as 1.05e
    """
    assert_bindings(
        schema="saxonData/XmlVersions/xv100.noti.xsd",
        instance="saxonData/XmlVersions/xv100.noti.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_xv100noti_xv100noti_notc_xml(mode, save_output, output_format):
    r"""
    Test which characters match \I in a regex Name characters in XML 1.1
    are the same as 1.05e
    """
    assert_bindings(
        schema="saxonData/XmlVersions/xv100.noti.xsd",
        instance="saxonData/XmlVersions/xv100.notc.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_xv100c_xv100c_i_xml(mode, save_output, output_format):
    r"""
    Test which characters match \c in a regex Name characters in XML 1.1
    are the same as 1.05e
    """
    assert_bindings(
        schema="saxonData/XmlVersions/xv100.c.xsd",
        instance="saxonData/XmlVersions/xv100.i.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_xv100c_xv100c_c_xml(mode, save_output, output_format):
    r"""
    Test which characters match \c in a regex Name characters in XML 1.1
    are the same as 1.05e
    """
    assert_bindings(
        schema="saxonData/XmlVersions/xv100.c.xsd",
        instance="saxonData/XmlVersions/xv100.c.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_xv100i_xv100i_i_xml(mode, save_output, output_format):
    r"""
    Test which characters match \i in a regex Name characters in XML 1.1
    are the same as 1.05e
    """
    assert_bindings(
        schema="saxonData/XmlVersions/xv100.i.xsd",
        instance="saxonData/XmlVersions/xv100.i.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_xv009_xv009_v01_xml(mode, save_output, output_format):
    """
    Test interpretation of NMTOKENS under XML 1.1 Name characters in XML
    1.1 were different from 1.0
    """
    assert_bindings(
        schema="saxonData/XmlVersions/xv009.xsd",
        instance="saxonData/XmlVersions/xv009.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_xv009_xv009_v02_xml(mode, save_output, output_format):
    """
    Test interpretation of NMTOKENS under XML 1.1 Name characters in XML
    1.1 were different from 1.0
    """
    assert_bindings(
        schema="saxonData/XmlVersions/xv009.xsd",
        instance="saxonData/XmlVersions/xv009.v02.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_xv008_xv008_v01_xml(mode, save_output, output_format):
    r"""
    Test which characters match \C in a regex Name characters in XML 1.1
    were different from 1.0
    """
    assert_bindings(
        schema="saxonData/XmlVersions/xv008.xsd",
        instance="saxonData/XmlVersions/xv008.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_xv007_xv007_v01_xml(mode, save_output, output_format):
    r"""
    Test which characters match \c in a regex Name characters in XML 1.1
    were different from 1.0
    """
    assert_bindings(
        schema="saxonData/XmlVersions/xv007.xsd",
        instance="saxonData/XmlVersions/xv007.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_xv006_xv006_v01_xml(mode, save_output, output_format):
    r"""
    Test which characters match \I in a regex Initial name characters in
    XML 1.1 were different from 1.0
    """
    assert_bindings(
        schema="saxonData/XmlVersions/xv006.xsd",
        instance="saxonData/XmlVersions/xv006.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_xv005_xv005_v01_xml(mode, save_output, output_format):
    r"""
    Test which characters match \i in a regex Initial name characters in
    XML 1.1 were different from 1.0
    """
    assert_bindings(
        schema="saxonData/XmlVersions/xv005.xsd",
        instance="saxonData/XmlVersions/xv005.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_xv004_xv004_v01_xml(mode, save_output, output_format):
    """
    Use newly-allowed name characters in schema component names Non-BMP
    chars is allowed in names in XML 1.1 but not earlier
    """
    assert_bindings(
        schema="saxonData/XmlVersions/xv004.xsd",
        instance="saxonData/XmlVersions/xv004.v01.xml",
        class_name="DKstra",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_xv003_xv003_v01_xml(mode, save_output, output_format):
    """
    Use newly-allowed C0 characters in character content and in attribute
    values C0 characters allowed in content in XML 1.1 but not earlier
    """
    assert_bindings(
        schema="saxonData/XmlVersions/xv003.xsd",
        instance="saxonData/XmlVersions/xv003.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_xv002_xv002_v01_xml(mode, save_output, output_format):
    """
    Use newly-allowed name characters in NCName value Dutch ligature ij is
    allowed in names in XML 1.1 and XML 1.0 5th ed but not earlier
    """
    assert_bindings(
        schema="saxonData/XmlVersions/xv002.xsd",
        instance="saxonData/XmlVersions/xv002.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_xv001_xv001_v01_xml(mode, save_output, output_format):
    """
    Use newly-allowed name characters in element and attribute name Dutch
    ligature ij is allowed in names in XML 1.1 and XML 1.0 5th ed but not
    earlier
    """
    assert_bindings(
        schema="saxonData/XmlVersions/xv001.xsd",
        instance="saxonData/XmlVersions/xv001.v01.xml",
        class_name="DKstra",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_zone304_zone304_v01_xml(mode, save_output, output_format):
    """
    Test xs:yearMonthDuration min/max rules For example, P1Y is equal to
    P12M
    """
    assert_bindings(
        schema="saxonData/Zone/zone304.xsd",
        instance="saxonData/Zone/zone304.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_zone304_zone304_v02_xml(mode, save_output, output_format):
    """
    Test xs:yearMonthDuration min/max rules For example, P1Y is equal to
    P12M
    """
    assert_bindings(
        schema="saxonData/Zone/zone304.xsd",
        instance="saxonData/Zone/zone304.v02.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_zone304_zone304_v03_xml(mode, save_output, output_format):
    """
    Test xs:yearMonthDuration min/max rules For example, P1Y is equal to
    P12M
    """
    assert_bindings(
        schema="saxonData/Zone/zone304.xsd",
        instance="saxonData/Zone/zone304.v03.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_zone303_zone303_v01_xml(mode, save_output, output_format):
    """
    Test xs:dayTimeDuration min/max rules For example, P1Y is equal to
    P12M
    """
    assert_bindings(
        schema="saxonData/Zone/zone303.xsd",
        instance="saxonData/Zone/zone303.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_zone303_zone303_v02_xml(mode, save_output, output_format):
    """
    Test xs:dayTimeDuration min/max rules For example, P1Y is equal to
    P12M
    """
    assert_bindings(
        schema="saxonData/Zone/zone303.xsd",
        instance="saxonData/Zone/zone303.v02.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_zone303_zone303_v03_xml(mode, save_output, output_format):
    """
    Test xs:dayTimeDuration min/max rules For example, P1Y is equal to
    P12M
    """
    assert_bindings(
        schema="saxonData/Zone/zone303.xsd",
        instance="saxonData/Zone/zone303.v03.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_zone302_zone302_v01_xml(mode, save_output, output_format):
    """
    Test xs:yearMonthDuration including equality rules For example, P1Y is
    equal to P12M
    """
    assert_bindings(
        schema="saxonData/Zone/zone302.xsd",
        instance="saxonData/Zone/zone302.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_zone301_zone301_v01_xml(mode, save_output, output_format):
    """
    Test xs:dayTimeDuration including equality rules For example, P1D is
    equal to P24H
    """
    assert_bindings(
        schema="saxonData/Zone/zone301.xsd",
        instance="saxonData/Zone/zone301.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_zone206_zone206_v01_xml(mode, save_output, output_format):
    """
    Test equality of xs:time values appearing in integrity constraints For
    example, 00:00:00 is equal to 24:00:00
    """
    assert_bindings(
        schema="saxonData/Zone/zone206.xsd",
        instance="saxonData/Zone/zone206.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_zone206_zone206_v02_xml(mode, save_output, output_format):
    """
    Test equality of xs:time values appearing in integrity constraints For
    example, 00:00:00 is equal to 24:00:00
    """
    assert_bindings(
        schema="saxonData/Zone/zone206.xsd",
        instance="saxonData/Zone/zone206.v02.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_zone205_zone205_v01_xml(mode, save_output, output_format):
    """
    Test equality of xs:dateTime values appearing in an enumeration For
    example, 00:00:00 is equal to 24:00:00 on the previous day
    """
    assert_bindings(
        schema="saxonData/Zone/zone205.xsd",
        instance="saxonData/Zone/zone205.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_zone205_zone205_v02_xml(mode, save_output, output_format):
    """
    Test equality of xs:dateTime values appearing in an enumeration For
    example, 00:00:00 is equal to 24:00:00 on the previous day
    """
    assert_bindings(
        schema="saxonData/Zone/zone205.xsd",
        instance="saxonData/Zone/zone205.v02.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_zone205_zone205_v03_xml(mode, save_output, output_format):
    """
    Test equality of xs:dateTime values appearing in an enumeration For
    example, 00:00:00 is equal to 24:00:00 on the previous day
    """
    assert_bindings(
        schema="saxonData/Zone/zone205.xsd",
        instance="saxonData/Zone/zone205.v03.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_zone203_zone203_v01_xml(mode, save_output, output_format):
    """
    Test leap years in proleptic Gregorian calendar 0, -4, ... are a leap
    years; but not -100
    """
    assert_bindings(
        schema="saxonData/Zone/zone203.xsd",
        instance="saxonData/Zone/zone203.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_zone203_zone203_v02_xml(mode, save_output, output_format):
    """
    Test leap years in proleptic Gregorian calendar 0, -4, ... are a leap
    years; but not -100
    """
    assert_bindings(
        schema="saxonData/Zone/zone203.xsd",
        instance="saxonData/Zone/zone203.v02.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_zone203_zone203_v03_xml(mode, save_output, output_format):
    """
    Test leap years in proleptic Gregorian calendar 0, -4, ... are a leap
    years; but not -100
    """
    assert_bindings(
        schema="saxonData/Zone/zone203.xsd",
        instance="saxonData/Zone/zone203.v03.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_zone202_zone202_v01_xml(mode, save_output, output_format):
    """
    Test year zero allowed in type xs:gYearMonth use year zero in
    enumeration facet
    """
    assert_bindings(
        schema="saxonData/Zone/zone202.xsd",
        instance="saxonData/Zone/zone202.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_zone202_zone202_v02_xml(mode, save_output, output_format):
    """
    Test year zero allowed in type xs:gYearMonth use year zero in
    enumeration facet
    """
    assert_bindings(
        schema="saxonData/Zone/zone202.xsd",
        instance="saxonData/Zone/zone202.v02.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_zone202_zone202_v03_xml(mode, save_output, output_format):
    """
    Test year zero allowed in type xs:gYearMonth use year zero in
    enumeration facet
    """
    assert_bindings(
        schema="saxonData/Zone/zone202.xsd",
        instance="saxonData/Zone/zone202.v03.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_zone201_zone201_v01_xml(mode, save_output, output_format):
    """
    Test year zero allowed in type xs:dateTimeStamp use year zero in
    minInclusive facet
    """
    assert_bindings(
        schema="saxonData/Zone/zone201.xsd",
        instance="saxonData/Zone/zone201.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_zone201_zone201_v02_xml(mode, save_output, output_format):
    """
    Test year zero allowed in type xs:dateTimeStamp use year zero in
    minInclusive facet
    """
    assert_bindings(
        schema="saxonData/Zone/zone201.xsd",
        instance="saxonData/Zone/zone201.v02.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_zone102_zone102_v01_xml(mode, save_output, output_format):
    """
    Test built-in type xs:dateTimeStamp restriction from xs:dateTimeStamp
    """
    assert_bindings(
        schema="saxonData/Zone/zone102.xsd",
        instance="saxonData/Zone/zone101.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_zone102_zone102_v02_xml(mode, save_output, output_format):
    """
    Test built-in type xs:dateTimeStamp restriction from xs:dateTimeStamp
    """
    assert_bindings(
        schema="saxonData/Zone/zone102.xsd",
        instance="saxonData/Zone/zone101.v02.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_zone101_zone101_v01_xml(mode, save_output, output_format):
    """
    Test built-in type xs:dateTimeStamp A dateTime value with a required
    timezone
    """
    assert_bindings(
        schema="saxonData/Zone/zone101.xsd",
        instance="saxonData/Zone/zone101.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_zone101_zone101_v02_xml(mode, save_output, output_format):
    """
    Test built-in type xs:dateTimeStamp A dateTime value with a required
    timezone
    """
    assert_bindings(
        schema="saxonData/Zone/zone101.xsd",
        instance="saxonData/Zone/zone101.v02.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_zone003_zone003_v01_xml(mode, save_output, output_format):
    """
    Test timezone facet with value="optional" Allows an xs:time value
    provided it has a timezone
    """
    assert_bindings(
        schema="saxonData/Zone/zone003.xsd",
        instance="saxonData/Zone/zone001.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_zone003_zone003_v02_xml(mode, save_output, output_format):
    """
    Test timezone facet with value="optional" Allows an xs:time value
    provided it has a timezone
    """
    assert_bindings(
        schema="saxonData/Zone/zone003.xsd",
        instance="saxonData/Zone/zone001.v02.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_zone003_zone003_v03_xml(mode, save_output, output_format):
    """
    Test timezone facet with value="optional" Allows an xs:time value
    provided it has a timezone
    """
    assert_bindings(
        schema="saxonData/Zone/zone003.xsd",
        instance="saxonData/Zone/zone001.n01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_zone002_zone002_v01_xml(mode, save_output, output_format):
    """
    Test timezone facet with value="prohibited" Allows an xs:time value
    provided it has a timezone
    """
    assert_bindings(
        schema="saxonData/Zone/zone002.xsd",
        instance="saxonData/Zone/zone001.n01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_zone001_zone001_v01_xml(mode, save_output, output_format):
    """
    Test timezone facet with value="required" Allows an xs:time value
    provided it has a timezone
    """
    assert_bindings(
        schema="saxonData/Zone/zone001.xsd",
        instance="saxonData/Zone/zone001.v01.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )


def test_zone001_zone001_v02_xml(mode, save_output, output_format):
    """
    Test timezone facet with value="required" Allows an xs:time value
    provided it has a timezone
    """
    assert_bindings(
        schema="saxonData/Zone/zone001.xsd",
        instance="saxonData/Zone/zone001.v02.xml",
        class_name="Doc",
        version="1.1",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="filenames",
    )
