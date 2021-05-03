from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Dict, List, Optional, Union
from xsdata.models.datatype import XmlDate
from models.xlink import TypeType
from models.xml import LangValue

__NAMESPACE__ = "http://www.w3.org/XML/2004/xml-schema-test-suite/"


class XdmFiltering(Enum):
    """<div>

    <p>
    Clause 1.2 of validation rule
    <a href="http://www.w3.org/TR/xmlschema11-1/#sec-cvc-assertion">Assertion satisifed</a> (in Structures sec. 3.13.4.1) says
    </p>
    <blockquote>
    <p>By default, comments and processing instructions are
    excluded from the partial post-schema-validation infoset,
    but at user option processors may retain comments and
    processing instructions instead of excluding them.</p>
    </blockquote>
    <p>
    The value "<tt>comments-and-PIs-excluded</tt>" denotes the default
    situation:  comments and processing instructions are suppressed
    before creating the XDM instance and thus cannot be examined
    by assertions.
    </p>
    <p>
    The value "<tt>comments-and-PIs-included</tt>" denotes the opposite:
    comments and processing instructions are included in the XDM
    instance and thus can be examined by assertions.  (Since this is
    required to be "at user option", any processor that supports this
    token must also be available in a configuration that supports the
    other token.)
    </p>
    <p>
    (The user option was added in November 2012 to address bug
    <a href="http://www.w3.org/Bugs/Public/show_bug.cgi?id=13935">13935
    xsd 1.1 assertions testing comment nodes</a>.
    These token values were added 20 January 2012 to allow both
    configurations to be tested.)
    </p>
    </div>
    """
    COMMENTS_AND_PIS_EXCLUDED = "comments-and-PIs-excluded"
    COMMENTS_AND_PIS_INCLUDED = "comments-and-PIs-included"


@dataclass
class Appinfo:
    class Meta:
        name = "appinfo"
        namespace = "http://www.w3.org/XML/2004/xml-schema-test-suite/"

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


class ExpectedOutcome(Enum):
    """<div>

    <p>
    Enumerates the possible values for the prescribed outcome
    of a test.  Values include both (a) the possible values of
    type <a href="#type_test-outcome">ts:test-outcome</a> and
    the following additional values:
    </p>
    <dl>
    <dt>
    <tt>implementation-defined</tt>
    </dt>
    <dd>(For instance tests) The value of the
    <tt>[validity]</tt> property on the validation root
    depends upon some property or behavior which is
    explicitly described in the relevant version of the spec
    as "implementation-defined", or for which the spec explicitly
    imposes a requirement that implementations specify their
    behavior.  (It follows that this
    value should never occur for 1.0 tests.)</dd>
    <dd>(For schema tests) The conformance of the schema
    depends upon some property or behavior explicitly
    described in the spec as "implementation-defined",
    or for which the spec explicitly
    imposes a requirement that implementations specify their
    behavior.</dd>
    </dl>
    <p>Note: in most cases of implementation-defined behaviors,
    as a matter of test suite design it is better to analyse
    the set of possible implementation behaviors, define
    version tokens for the possible behaviors, and specify
    more informative results based on those tokens.  The value
    <tt>implementation-defined</tt> is provided for situations
    where this is not feasible for whatever reason.
    </p>
    <dl>
    <dt>
    <tt>implementation-dependent</tt>
    </dt>
    <dd>(For instance tests) The value of the
    <tt>[validity]</tt> property on the validation root
    depends upon some property or behavior which is
    explicitly described in the relevant version of the spec
    as "implementation-dependent", or otherwise explicitly
    described as varying among implementations but not
    "implementation-defined".  (For XSD 1.0, this will often
    take the form of a normative "<span class="rfc">may</span>" in the text.)
    </dd>
    <dd>(For schema tests) The conformance of the schema
    depends upon some property or behavior explicitly
    described in the spec as "implementation-dependent" or
    as varying among implementations, but not described as
    "implementation-defined".</dd>
    <dt>
    <tt>indeterminate</tt>
    </dt>
    <dd>The intended result is indeterminate for one of the
    following reasons, or for other reasons:<ul><li>The result is under-determined (the spec is vague
    or underspecified), but not described explicitly as
    varying among conforming implementations.
    </li><li>The spec imposed contradictory requirements on the
    result. (I.e. the result is
    <em>over-determined.)</em></li><li>
    There is an unresolved dispute within the working
    group as to what the spec requires the result to be.
    (This includes cases where the working group cannot
    agree on whether the spec explicitly labels the
    result as implementation-dependent or
    implementation-defined or not, as well as cases
    where the group cannot agree on how to apply the
    spec to the case in hand.)
    </li></ul></dd>
    </dl>
    <p>N.B. the values <tt>implementation-dependent</tt> and
    <tt>implementation-defined</tt> should be used only when
    the spec is explicit about the implementation-dependence
    of the result and it is thus clear that the
    implementation-dependence is a design choice consciously
    made by the working group. They must not be used in cases
    where the spec simply appeals to some concept which it
    turns out not to define: such cases are to be marked
    <tt>indeterminate</tt>.
    </p>
    <p>Note:  in most cases, as a matter of language design
    it is better for the language specification to prescribe
    clearly a particular result for a test, or to identify the
    result explicitly as implementation-defined or
    implementation-dependent.  The value
    <tt>indeterminate</tt> is provided for situations where
    this has not been done for whatever reason.
    </p>
    <p class="note">The value <tt>invalid-latent</tt> described
    in earlier drafts of this schema document is no longer
    needed; the version keywords for complex-type restriction
    behaviors can be used to describe the relevant cases
    more precisely.
    </p>
    </div>
    """
    VALID = "valid"
    INVALID = "invalid"
    NOT_KNOWN = "notKnown"
    RUNTIME_SCHEMA_ERROR = "runtime-schema-error"
    IMPLEMENTATION_DEFINED = "implementation-defined"
    IMPLEMENTATION_DEPENDENT = "implementation-dependent"
    INDETERMINATE = "indeterminate"
    INVALID_LATENT = "invalid-latent"


class KnownToken(Enum):
    """<div>

    <p>Tokens to denote well-known (i.e. documented) versions, features,
    or implementation-defined behaviors, of XSD.</p> <p>The <tt>known-
    token</tt> type is a union of several other types, each with an
    enumeration of values.  Each sub-type defines keywords for a set of
    mutually exclusive versions, features, or behaviors, such that in
    any given schema validation episode, at most one keyword in any
    subtype will apply.  For examples, see the various subtypes defined
    immediately below. </p> </div>
    """
    VALUE_1_0 = "1.0"
    VALUE_1_1 = "1.1"
    VALUE_1_0_1E = "1.0-1e"
    VALUE_1_0_2E = "1.0-2e"
    XML_1_0 = "XML-1.0"
    XML_1_0_1E_4E = "XML-1.0-1e-4e"
    XML_1_0_5E = "XML-1.0-5e"
    XML_1_1 = "XML-1.1"
    UNICODE_4_0_0 = "Unicode_4.0.0"
    UNICODE_6_0_0 = "Unicode_6.0.0"
    CTR_ALL_COMPILE = "CTR-all-compile"
    CTR_ALL_RUNTIME = "CTR-all-runtime"
    CTR_ALL_IDEP = "CTR-all-idep"
    RESTRICTED_XPATH_IN_CTA = "restricted-xpath-in-CTA"
    FULL_XPATH_IN_CTA = "full-xpath-in-CTA"
    COMMENTS_AND_PIS_EXCLUDED = "comments-and-PIs-excluded"
    COMMENTS_AND_PIS_INCLUDED = "comments-and-PIs-included"


class KnownXsdVersion(Enum):
    """<div>

    <p> Tokens to denote specific known versions of XSD. </p> <p> Each
    token denotes the version of the XSD language identified by the
    <tt>ts:standard-version-id</tt> attribute on the
    <tt>xsd:enumeration</tt> element. That is, "<tt>1.0</tt>" denotes
    XSD 1.0 (without reference to a particular edition), and
    "<tt>1.1</tt>" denotes XSD 1.1 (without referece to a particular
    edition). </p> </div>
    """
    VALUE_1_0 = "1.0"
    VALUE_1_1 = "1.1"


class RuntimeSchemaError(Enum):
    """<div>

    <p>
    Tokens to denote different implementation-defined
    behavior in the presence of faulty restriction in
    a complex-type definition.
    </p>
    <p>
    A full explanation of this token and its meaning
    is needed, but not yet available. For the moment let it
    suffice to say that if an <tt>all</tt>-group
    in a restriction allows content not allowed by
    the base type, the processor is not required
    to detect the problem by inspection of the schema
    in isolation.  Three behaviors are allowed; the choice
    among them is implementation-defined.  The values
    denoting the three behaviors are these.
    </p>
    <dl>
    <dt>
    <tt>CTR-all-compile</tt>
    </dt>
    <dd>Compile-time detection:  the processor always
    detects the problem by examining the schema in
    isolation; it warrants that no non-conforming
    schema will ever be used in validation.
    </dd>
    <dt>
    <tt>CTR-all-runtime</tt>
    </dt>
    <dd>Run-time detection:  the processor never
    detects the problem by examining the schema in
    isolation; it detects it always and only when
    an instance of the type is valid against the
    restriction but not against the base type.
    If no instance of the type forces the recognition
    of the fault, then a non-conforming schema will
    have been used in validation. The results, however,
    will always be the same as for a schema in
    which the error had been corrected.
    (Processors that don't always check the declaration
    in isolation will need to validate each instance
    both against its governing type and against the
    base type.)
    </dd>
    <dt>
    <tt>CTR-all-idep</tt>
    </dt>
    <dd>Implementation-dependent detection:  the processor
    sometimes detects the problem by examining the schema in
    isolation, sometimes when examining an instance.
    No guarantees.
    </dd>
    </dl>
    <p>Note, 20 January 2012.  Is this distinction still required,
    or has it been overtaken by the change made to resolve
    <a href="https://www.w3.org/Bugs/Public/show_bug.cgi?id=12185">bug 12185 Conditional Type Assignment and substitutability</a>
    (or other late changes)?</p>
    </div>
    """
    CTR_ALL_COMPILE = "CTR-all-compile"
    CTR_ALL_RUNTIME = "CTR-all-runtime"
    CTR_ALL_IDEP = "CTR-all-idep"


class Status(Enum):
    ACCEPTED = "accepted"
    STABLE = "stable"
    QUERIED = "queried"
    DISPUTED_TEST = "disputed-test"
    DISPUTED_SPEC = "disputed-spec"


class TestOutcome(Enum):
    """<div>

    <p>
    Enumerates the possible outcomes of running a test.
    Usually, these are values of the <tt>[validity]</tt>
    property on the validation root.
    </p>
    <p>The most common values are:</p>
    <dl>
    <dt>
    <tt>valid</tt>
    </dt>
    <dd>(For instance tests) The value of the <tt>[validity]</tt>
    property on the validation root is <tt>valid</tt>.</dd>
    <dd>(For schema tests) The schema is a conforming schema.</dd>
    <dt>
    <tt>invalid</tt>
    </dt>
    <dd>(For instance tests) The value of the <tt>[validity]</tt>
    property on the validation root is <tt>invalid</tt>.</dd>
    <dd>(For schema tests) The schema is <em>not</em> a
    conforming schema.</dd>
    <dt>
    <tt>notKnown</tt>
    </dt>
    <dd>(For instance tests) The value of the <tt>[validity]</tt>
    property on the validation root is <tt>notKnown</tt>.</dd>
    <dd>(For schema tests, this value is meaningless.)</dd>
    </dl>
    <p>Note:  processors built as <a href="http://www.w3.org/TR/xmlschema11-1/#key-validator">instance validators</a> are not required by XSD to
    distinguish between invalid documents and documents with
    unknown validity; it is thus not an absolute requirement
    (although it is desirable for clarity)
    that a test result distinguish <tt>invalid</tt>
    from <tt>notKnown</tt> outcomes.
    </p>
    <p>One further value is needed only in fairly specialized
    circumstances (but is essential there):</p>
    <dl>
    <dt>
    <tt>runtime-schema-error</tt>
    </dt>
    <dd>
    <p>(For instance tests) The instance has a schema with
    a latent error (see description below in the documentation
    for type <a href="#type_expected-outcome">ts:expected-outcome</a>);
    the processor did not detect the latent error on the
    corresponding schema test, but the instance document
    has exposed the error (by including content
    which is valid against the apparent content model of the
    governing type, but not valid against the base type)
    and the processor has detected the schema error in the
    course of instance validation.
    </p>
    <p>Note: processors are encouraged, though not required, to
    distinguish this outcome from <tt>invalid</tt>, since
    on an instance test <tt>invalid</tt> normally means that
    the processor has found an invalid instance, not a
    non-conforming schema.
    </p>
    </dd>
    <dd>
    <p>(For schema tests) The value <tt>runtime-schema-error</tt>
    is meaningless for schema tests and should not be used for
    them.  (It would be a contradiction in terms.)</p>
    </dd>
    </dl>
    </div>
    """
    VALID = "valid"
    INVALID = "invalid"
    NOT_KNOWN = "notKnown"
    RUNTIME_SCHEMA_ERROR = "runtime-schema-error"


class TestSuiteResultsPublicationPermission(Enum):
    W3_C_MEMBERS = "W3C members"
    PUBLIC = "public"


class UnicodeVersions(Enum):
    """<div>

    <p> Tokens to denote specific known versions of Unicode. </p> <p>
    Each token denotes the version of the Unicode specification. The
    list is not complete; in the only cases where results are known to
    vary between Unicode versions, results are published for version
    4.0.0 and 6.0.0. Implementors wishing to provide reference results
    for other versions of Unicode are welcome to submit such results.
    </p> </div>
    """
    UNICODE_4_0_0 = "Unicode_4.0.0"
    UNICODE_6_0_0 = "Unicode_6.0.0"


class XmlSubstrate(Enum):
    """<div>

    <p>
    Tokens to denote different versions of XML-dependent
    datatypes.  Conforming XSD 1.1 processors may support
    XML 1.0-based datatypes, XML 1.1-based datatypes,
    or both.  There is dispute in the working group over
    whether conforming XSD 1.0 processors are allowed to
    suport XML 1.1-based datatypes or not.
    </p>
    <p>
    The value "<tt>XML-1.0</tt>" denotes processor support
    for, or test applicability to, XSD datatypes based on XML
    1.0, without specifying a particular edition.  (This value
    is retained for backward compatibility of this schema, but
    it should be avoided unless there is no difference, for a
    given test or test result, between editions 1-4 and
    edition 5 of XML 1.0. Where there is a difference, the
    values "<tt>XML-1.0-1e-4e</tt>" and "<tt>XML-1.0-5e</tt>"
    should be used in preference.
    (XSD 1.1 describes XML 1.0 Fifth Edition as the base
    version in its normative reference, so in theory the
    distinction between "<tt>XML-1.0-1e-4e</tt>" and
    "<tt>XML-1.0-5e</tt>" is only relevant to XSD 1.0
    processors.  In practice, it may also be relevant for some
    XSD 1.1 processors.
    </p>
    <p>
    The value "<tt>XML-1.0-1e-4e</tt>" denotes processor support
    for, or test applicability to, XSD datatypes based on XML
    1.0 First Edition through Fourth Edition.
    </p>
    <p>
    The value "<tt>XML-1.0-5e</tt>" denotes processor support
    for, or test applicability to, XSD datatypes based on XML
    1.0 Fifth Edition.
    </p>
    <p>
    The value "<tt>XML-1.1</tt>" denotes processor support
    for, or test applicability to, XSD datatypes based on XML
    1.1 (for which at the moment there is only one edition).
    </p>
    <p>
    In most cases, of course, "<tt>XML-1.0-5e</tt>" and
    "<tt>XML-1.1</tt>" will describe the same behaviors.
    </p>
    </div>
    """
    XML_1_0 = "XML-1.0"
    XML_1_0_1E_4E = "XML-1.0-1e-4e"
    XML_1_0_5E = "XML-1.0-5e"
    XML_1_1 = "XML-1.1"


class XpathInCta(Enum):
    """<div>

    <p>
    Tokens to distinguish tests which use only the "required
    subset" of XPath in conditional type assignment
    from tests which use full XPath (or: any XPath outside
    the subset) in conditional type assignment.
    See "3.12.6 Constraints on Type Alternative Schema Components"
    of the Structures spec, which reads in part
    </p>
    <blockquote>
    <p>A conforming processor must accept and process any XPath
    expression conforming to the "required subset" of [XPath 2.0]
    defined by the following grammar.</p>
    <p style="margin-left: 2em;">
    Note: Any XPath expression containing no static errors as
    defined in [XPath 2.0] may appear in a conforming schema.
    Conforming processors may but are not required to support
    XPath expressions not belonging to the required subset of
    XPath.</p>
    </blockquote>
    <p>
    The value "<tt>restricted-xpath-in-CTA</tt>" denotes processor support
    for, or test applicability to, the minimal subset of XPath
    required of all conforming 1.1 processors.  All 1.1 processors
    should support this feature and run tests marked with it.
    </p>
    <p>
    The value "<tt>full-xpath-in-CTA</tt>" denotes processor support
    for, or test applicability to, full XPath in conditional type
    assignment expressions.
    </p>
    <p>
    (These token values were added 29 July 2011 to address bug
    <a href="http://www.w3.org/Bugs/Public/show_bug.cgi?id=13455">13455
    XPath subset causes problem</a>.)
    </p>
    </div>
    """
    RESTRICTED_XPATH_IN_CTA = "restricted-xpath-in-CTA"
    FULL_XPATH_IN_CTA = "full-xpath-in-CTA"


class Xsd10Editions(Enum):
    """<div>

    <p>
    Tokens to denote specific editions of XSD 1.0.
    </p>
    <p>
    Each token denotes the version of the XSD language
    identified by the <tt>ts:standard-version-id</tt>
    attribute on the <tt>xsd:enumeration</tt> element.
    That is,
    "<tt>1.0-1e</tt>" and "<tt>1.0-2e</tt>" represent
    1.0 First Edition and 1.0 Second Edition,
    respectively.
    </p>
    <p>Outside the context of XSD 1.0, these edition
    identifiers have no meaning or applicability.
    </p>
    </div>
    """
    VALUE_1_0_1E = "1.0-1e"
    VALUE_1_0_2E = "1.0-2e"


@dataclass
class Documentation:
    class Meta:
        name = "documentation"
        namespace = "http://www.w3.org/XML/2004/xml-schema-test-suite/"

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class Expected:
    """<div>

    <p>The validation outcome prescribed by the spec
    for a test in the XSTS.</p>
    <p>This element has one optional attribute:</p>
    <ul>
    <li>
    <p><tt>version</tt> - a list of version tokens.
    The result specified is applicable to processor
    configurations supporting <em>all</em> of the
    indicated versions or features of XSD.
    See the definition of the
    <a href="#type_version-info"><tt>version-info</tt></a>
    type.
    </p>
    <p>It is an error for more than one <tt>expected</tt>
    element to be applicable to any given processor
    configuration; this is most easily avoided by
    making sure that any two sibling <tt>expected</tt>
    elements have <tt>version</tt> attributes containing
    mutually exclusive tokens.
    </p>
    </li>
    </ul>
    <p class="note">Note: The meaning of the <tt>version</tt></p>
    <p>
    On tests and elements for groups of
    tests (<tt>testGroup</tt> etc.), a <tt>version</tt>
    attribute of the form <code>version="<i>x</i><i>y</i><i>z</i>"</code> means "If <strong>any</strong> of
    <tt>x</tt>, <tt>y</tt>, or <tt>z</tt> are supported, tests
    in this group are applicable."
    </p>
    <p>On the <tt>expected</tt> element, the
    meaning changes in a crucial way: the tokens are connected
    with an implicit <tt>and</tt>, not an <tt>or</tt>. So
    <code>version="<i>x</i><i>y</i><i>z</i>"</code> means
    "If <strong>all</strong> of <tt>x</tt>, <tt>y</tt>, or
    <tt>z</tt> are supported, the prescribed outcome is as
    described.  So on a test group, <code>version="1.0
    1.1"</code> means tests for both versions are included.
    On an <tt>expected</tt> element, <code>version="1.0
    1.1"</code> would mean the expected result holds only if a
    given processor is using both version 1.0 and version 1.1
    in the same validation episode.  Since the two tokens are
    defined as mutually exclusive, this would be a
    contradiction.
    </p>
    <p class="note">As a matter of test suite design, it
    is a good idea to keep <tt>version</tt> attributes
    on <tt>expected</tt> elements to a single token if
    possible, to minimize opportunities for confusion.
    </p>
    <p>And one required attribute:</p>
    <ul>
    <li>
    <p><tt>validity</tt> - indicates the expected outcome
    of the test, using a value of type
    <a href="#type_expected-outcome">ts:expected-outcome</a>.</p>
    <p>
    For an instance test, this typically indicates the expected
    value of the <code>[validity]</code> property on the
    root element of the instance document, or indicates
    that the value may vary among processors.
    </p>
    <p>
    For a schema test, this indicates whether the
    schema created from the schema documents in the test
    is expected to be a conforming schema (<code>valid</code>)
    or a non-conforming schema (<code>invalid</code>).
    The value <code>notKnown</code> has no meaning
    for a schema test.
    </p>
    </li>
    </ul>
    </div>
    """
    class Meta:
        name = "expected"
        namespace = "http://www.w3.org/XML/2004/xml-schema-test-suite/"

    validity: Optional[ExpectedOutcome] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version: List[Union[KnownToken, Decimal, str]] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class Annotation:
    """<div>

    <p> This is an exact copy of the <tt>annotation</tt> element defined
    in the Schema Recommendation. It is duplicated here in order to
    replicate the functionality of the <tt>xsd:annotation</tt> element
    and because the Schema for Schemas cannot be imported. </p> </div>
    """
    class Meta:
        name = "annotation"
        namespace = "http://www.w3.org/XML/2004/xml-schema-test-suite/"

    appinfo: List[Appinfo] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    documentation: List[Documentation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class Ref:
    class Meta:
        name = "ref"

    annotation: List[Annotation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/XML/2004/xml-schema-test-suite/",
        }
    )
    type: TypeType = field(
        default=TypeType.LOCATOR,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class StatusEntry:
    class Meta:
        name = "statusEntry"

    annotation: List[Annotation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/XML/2004/xml-schema-test-suite/",
        }
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    bugzilla: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"http://www\.w3\.org/Bugs/Public/show_bug\.cgi\?id=[0-9]*",
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class TestResult:
    """<div>

    <p>
    The result of an individual instance test or a schema test.
    </p>
    <p>
    This element has four required attributes:
    </p>
    <ul>
    <li><tt>validity</tt> - the validition outcome of the test.
    A value of type <a href="#type_expected-outcome">ts:expected-outcome</a>,
    i.e.
    one of "<tt>valid</tt>", "<tt>invalid</tt>",
    "<tt>notKnown</tt>", or "<tt>runtime-schema-error</tt>".
    </li>
    <li><tt>set</tt> - the value of the "<tt>name</tt>"
    attribute of the test set to which the test belongs.
    </li>
    <li><tt>group</tt> - the value of the "<tt>name</tt>"
    attribute of the test group to which the test belongs.
    </li>
    <li><tt>test</tt> - the value of the "<tt>name</tt>"
    attribute of the schema test or instance test, the
    validation outcome of which this result reports.
    </li>
    </ul>
    <p>

    NOTE: The "<tt>set</tt>", "<tt>group</tt>" and
    "<tt>test</tt>" attributes are used to uniquely identify
    the test within the XSTS for which this result reports the
    validation outcome.  Each matches the "<tt>name</tt>"
    attribute of the respective element in the test suite.
    </p>
    <p>
    This element has one optional attribute:
    </p>
    <ul>
    <li><tt>normalizedLoad</tt> - a relative load value, intended as an indicator
    of the resource requirements of an individual
    test. Values may be based on processing time,
    memory usage or a combination of the two.
    Values should be in the vicinity of 1.0.
    </li>
    </ul>
    <p>The element has one optional element:</p>
    <ul>
    <li><tt>annotation</tt> - zero or more instances of more detailed
    (<tt>ts:documentation</tt>) or structured (<tt>ts:appinfo</tt>)
    information or commentary regarding the individual
    test result. Reporters are encouraged to use
    <tt>annotation/appinfo</tt> to report more detailed outcome
    information, such as error and warning messages.
    </li>
    </ul>
    </div>
    """
    class Meta:
        name = "testResult"
        namespace = "http://www.w3.org/XML/2004/xml-schema-test-suite/"

    annotation: List[Annotation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    validity: Optional[TestOutcome] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    set: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    group: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    test: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    normalized_load: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "normalizedLoad",
            "type": "Attribute",
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class Current(StatusEntry):
    """<div>

    <p>The current status of a test in the XSTS.</p>
    <p>This element has two attributes, both of which are
    required:</p>
    <ul>
    <li><tt>status</tt> - the status of the test. One of
    "<tt>accepted</tt>", "<tt>stable</tt>",
    "<tt>disputed-test</tt>" or "<tt>disputed-spec</tt>"
    (see the XSTS website for an explanation of these values).
    </li>
    <li><tt>date</tt> - the date on which the test or the
    metadata (including the value in the
    <tt>status</tt> attribute, but also anything else
    of importance) was last changed.
    </li>
    </ul>
    </div>
    """
    class Meta:
        name = "current"
        namespace = "http://www.w3.org/XML/2004/xml-schema-test-suite/"


@dataclass
class DocumentationReference(Ref):
    """<div>

    <p> A link to documentation relevant to a test, such as a link to
    the Recommendation, an erratum, an archived email discussion, etc.
    </p> </div>
    """
    class Meta:
        name = "documentationReference"
        namespace = "http://www.w3.org/XML/2004/xml-schema-test-suite/"


@dataclass
class InstanceDocument(Ref):
    class Meta:
        name = "instanceDocument"
        namespace = "http://www.w3.org/XML/2004/xml-schema-test-suite/"


@dataclass
class Prior(StatusEntry):
    """<div>

    <p>A former status of a test in the XSTS.</p>
    <p>This element has two attributes, both of which are
    required:</p>
    <ul>
    <li><tt>status</tt> - the former status of the test. One of
    "<tt>accepted</tt>", "<tt>stable</tt>",
    "<tt>disputed-test</tt>" or "<tt>disputed-spec</tt>"
    (see the XSTS website for an explanation of these values).
    </li>
    <li><tt>date</tt> - the date on which the test or the
    metadata (including the value in the
    <tt>status</tt> attribute, but also anything else
    of importance) was last changed.
    </li>
    </ul>
    </div>
    """
    class Meta:
        name = "prior"
        namespace = "http://www.w3.org/XML/2004/xml-schema-test-suite/"


@dataclass
class SchemaDocument(Ref):
    class Meta:
        name = "schemaDocument"
        namespace = "http://www.w3.org/XML/2004/xml-schema-test-suite/"


@dataclass
class TestSetRef(Ref):
    class Meta:
        name = "testSetRef"
        namespace = "http://www.w3.org/XML/2004/xml-schema-test-suite/"


@dataclass
class TestSuiteResults:
    """<div>

    <p>
    This is the root element of a document containing a test
    result report. The report takes the form of a set of test
    results returned by a processor/validator when run against
    the XSTS.
    </p>
    <p>
    It has three required attributes:
    </p>
    <ul>
    <li><tt>suite</tt> - the name of the test suite to which
    these results correspond.  This should be the value of
    the <tt>name</tt> attribute of the <tt>testSuite</tt>
    element at the root of the test suite document
    describing the tests to which these results correspond.
    </li>
    <li><tt>processor</tt> - some identifying information for
    the processor/ validator which produced the reported
    results. The value of this attribute is left to the
    discretion of the reporter.
    </li>
    <li><tt>submitDate</tt> - the date on which these results
    were submitted to the XSTS Task Force.
    </li>
    </ul>
    <p>The element also has one optional attribute:</p>
    <ul>
    <li><tt>publicationPermission</tt> - the degree to which the
    result reporter authorizes the W3C to disseminate the
    reported results. One of "<tt>W3C members</tt>" or
    "<tt>public</tt>" (see the XSTS website for an explanation
    of these values). If this attribute is absent, no
    permission to publish is granted.
    </li>
    </ul>
    <p>This element has two optional elements:</p>
    <ul>
    <li><tt>annotation</tt> - zero or more instances of more
    detailed (<tt>ts:documentation</tt>) or structured
    (<tt>ts:appinfo</tt>) information or commentary
    regarding the enclosed test results.
    </li>
    <li><tt>testResult</tt> - any number of reports of the
    results of individual tests. Any results may be omitted,
    particularly those for tests of features for which the
    processor claims no support.
    </li>
    </ul>
    </div>
    """
    class Meta:
        name = "testSuiteResults"
        namespace = "http://www.w3.org/XML/2004/xml-schema-test-suite/"

    annotation: List[Annotation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    test_result: List[TestResult] = field(
        default_factory=list,
        metadata={
            "name": "testResult",
            "type": "Element",
        }
    )
    suite: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    processor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    submit_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "submitDate",
            "type": "Attribute",
            "required": True,
        }
    )
    publication_permission: Optional[TestSuiteResultsPublicationPermission] = field(
        default=None,
        metadata={
            "name": "publicationPermission",
            "type": "Attribute",
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class InstanceTest:
    """<div>

    <p>
    This element groups together information about an instance
    document which should be validated against the schema
    referenced in the enclosing <tt>testGroup</tt>.
    </p>
    <p>
    Note: per section 5.2 "Assessing Schema-Validity" of the
    Recommendation "XML Schema Part 1: Structures", validation
    may be started in a variety of ways.  For the purposes of
    the XSTS, only the third method shall be used:
    </p>
    <blockquote>
    <p>
    The processor starts from Schema-Validity Assessment
    (Element) (3.3.4) with no stipulated declaration or
    definition.
    </p>
    </blockquote>
    <p>The validation root is the outermost element in the
    instance document.</p>
    <p>
    The <tt>instanceTest</tt> element has one required
    attribute:
    </p>
    <ul>
    <li><tt>name</tt> - the name of the instance document, which
    must differ from the name of any other
    <tt>schemaTest</tt> or <tt>instanceTest</tt> element
    within the enclosing <tt>testGroup</tt></li>
    </ul>
    <p>
    and one attribute which is optional, for signaling
    that the test is applicable only to a particular set of
    versions of XSD:
    </p>
    <ul>
    <li>
    <p><tt>version</tt> - Tests which only apply to certain
    versions of XML Schema list those versions in the
    <tt>version</tt> attribute.
    </p>
    <p>Processors supporting <em>any</em> version or feature
    indicated by a keyword in the attribute should run the
    test.  (Or, more declaratively: the test is meaningful
    to any processor which supports any of the features or
    versions listed.)  If no value is specified, all
    processors which haven't already skipped the enclosing
    test group, test set, or test suite should run the
    test.
    </p>
    <p>
    The value is a list of version tokens.  See the
    definition of the <a href="#type_version-info"><tt>version-info</tt></a>
    type.</p>
    <p class="note">Note: running instance tests with a
    processor for an inapplicable version may produce an
    failure owing to non-conformant constructs in the
    schema document; if the processor does not detect the
    problem or continues anyway, the results are certain
    to be meaningless.
    </p>
    </li>
    </ul>
    <p>
    One child element is required:
    </p>
    <ul>
    <li><tt>instanceDocument</tt> - a link to a file containing
    the instance document.
    </li>
    </ul>
    <p>
    Four child elements may optionally be present:
    </p>
    <ul>
    <li><tt>annotation</tt> - zero or more instances of general
    documentation</li>
    <li><tt>expected</tt> - the prescribed validation outcome for
    the instance document.  Optional, and repeatable.
    Each <tt>expected</tt> element indicates the result
    on this test for a particular set of versions of the
    language.
    </li>
    <li><tt>current</tt> - the current status of this test in
    the XSTS (an indication of the test's accuracy in testing
    the feature it is intended to test).
    </li>
    <li><tt>prior</tt> - the history of any changes in the
    status of this test.
    </li>
    </ul>
    <p>
    The elements "<tt>expected</tt>" and "<tt>current</tt>" may
    be absent when tests are contributed, but will always be
    present for tests included in the XSTS.
    </p>
    <p>The <tt>current</tt> and <tt>prior</tt> elements should
    be used to keep a change history of the test; see
    discussion under the <a href="#elem_schemaTest"><tt>schemaTest</tt></a> element.
    </p>
    </div>
    """
    class Meta:
        name = "instanceTest"
        namespace = "http://www.w3.org/XML/2004/xml-schema-test-suite/"

    annotation: List[Annotation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    instance_document: Optional[InstanceDocument] = field(
        default=None,
        metadata={
            "name": "instanceDocument",
            "type": "Element",
            "required": True,
        }
    )
    expected: List[Expected] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    current: Optional[Current] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    prior: List[Prior] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version: List[Union[KnownToken, Decimal, str]] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class SchemaTest:
    """<div>

    <p>
    This element groups together information about the schema
    for a particular test group.
    </p>
    <p>
    It has one attribute which is required:
    </p>
    <ul>
    <li><tt>name</tt> - the name of the schema test, which must be
    unique within the enclosing <tt>testGroup</tt> (i.e. it must
    differ from the name(s) of any associated <tt>instanceTest</tt>
    elements).
    </li>
    </ul>
    <p>
    and one attribute which is optional, for identifying a subset
    of versions and/or editions for which the test is valid:
    </p>
    <ul>
    <li>
    <p><tt>version</tt> - Tests which only apply to certain
    versions of XML Schema list those versions in the
    <tt>version</tt> attribute.  Processors supporting
    <em>any</em> version or feature indicated by a keyword
    in the attribute should run the test.  (Or, phrased
    more declaratively: the test is meaningful to any
    processor which supports any of the features or
    versions listed.)
    </p>
    <p>If no value is specified, all processors which
    haven't already skipped the enclosing test group,
    test set, or test suite should run the test.
    </p>
    <p>
    The value is a list of version tokens.  See the
    definition of the <a href="#type_version-info"><tt>version-info</tt></a>
    type.</p>
    <p>Note that the omission of a version token on a schema
    test is in some sense strictly advisory: any schema
    test is meaningful for any processor in any
    configuration.  For processor configurations not
    supporting any of the features or versions named, the
    expected result is that the schema is not a conforming
    schema.  This will <em>not</em> be indicated with an
    explicit <tt>expected</tt> element.
    </p>
    </li>
    </ul>
    <p>
    One child element is required:
    </p>
    <ul>
    <li><tt>schemaDocument</tt> - at least one link to a file
    containing a schema document. The schema for the test is
    constructed from the set (or from other schemas via
    import).
    </li>
    </ul>
    <p>Four child elements may optionally be present:</p>
    <ul>
    <li><tt>annotation</tt> - zero or more instances of general
    documentation</li>
    <li><tt>expected</tt> - indicates the conformance or
    non-conformance of the schema described by the schema
    document(s)
    (<tt>valid</tt> = conformant, <tt>invalid</tt> =
    non-conformant).
    </li>
    <li><tt>current</tt> - the current status of this test in
    the XSTS (an indication of the test's accuracy in testing
    the feature it is intended to test).
    </li>
    <li><tt>prior</tt> - the history of any changes in the
    status of this test.
    </li>
    </ul>
    <p>
    The elements "<tt>expected</tt>" and "<tt>current</tt>"
    may be absent when tests are contributed, but will always
    be present for tests included in the XSTS.
    </p>
    <p>
    The <tt>current</tt> and <tt>prior</tt> elements were originally
    designed for tracking changes of status in tests; they can and
    should be used to keep a general change history of the test.
    Whenever anything changes that may be of importance for users
    of the test suite, it is appropriate to clone the existing
    <tt>current</tt> element into a pair of similar elements, then
    rename the second one <tt>prior</tt>.  In the new <tt>current</tt>
    element, the change made should be described in the
    <tt>annotation</tt> children, and the date of the change
    should be recorded.
    </p>
    <p>
    Examples:  The status of the test changes.  The expected
    result is questions and reaffirmed.  The expected result is
    changed, or multiple expected results are given for different
    processor configurations.
    </p>
    <p>
    For status changes involving bug reports, the relevant status
    entries should have a Bugzilla cross-reference.
    </p>
    </div>
    """
    class Meta:
        name = "schemaTest"
        namespace = "http://www.w3.org/XML/2004/xml-schema-test-suite/"

    annotation: List[Annotation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    schema_document: List[SchemaDocument] = field(
        default_factory=list,
        metadata={
            "name": "schemaDocument",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    expected: List[Expected] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    current: Optional[Current] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    prior: List[Prior] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version: List[Union[KnownToken, Decimal, str]] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class TestSuite:
    """<div>

    <p>
    The root element of a document describing a set of tests for one
    or more versions of W3C XML Schema.
    </p>
    <p>
    The element has three attributes, each of which is required:
    </p>
    <ul>
    <li>
    <p><tt>name</tt> - the name of this test suite.
    </p>
    </li>
    <li>
    <p><tt>releaseDate</tt> - the date on which this test
    suite was released. This value serves to identify the
    version of the test suite.
    </p>
    </li>
    <li>
    <p><tt>schemaVersion</tt> - the versions of XSD for which
    the tests are designed.  This has documentary function
    only, and is intended for human readers.  The
    machine-processable version information is handled by
    the <tt>version</tt> attribute.
    </p>
    </li>
    <li>
    <p><tt>version</tt> - a list of version tokens indicating
    versions and features for which at least some tests in the
    test suite are applicable.
    </p>
    <p>Any processor or processor configuration which
    supports <em>any</em> of the tokens given should run
    the tests.  Processors which support none of the named
    features can skip the entire test suite without loss.
    If no <tt>version</tt> value is given, or if the value
    is the empty string, all processors should run the
    tests.</p>
    <p>For example <code>version="1.1"</code> on a test suite
    element indicates that XSD 1.1 processors will find
    relevant tests, and XSD 1.0 processors will not,
    while <code>version="1.0 1.1"</code>, or no
    <code>version</code> attribute at all, indicates
    that the test suite contains tests relevant to both.
    </p>
    <p>Logically, the <tt>version</tt> attribute on
    the <tt>testSuite</tt> element, if given explicitly,
    should include all the tokens used on any
    <tt>testSet</tt>, <tt>testGroup</tt>,
    <tt>schemaTest</tt>, or <tt>instanceTest</tt> in the
    test suite, and no others.  This is not necessarily
    enforced, however, by the schema for this
    vocabulary.</p>
    </li>
    </ul>
    <p>
    Two child elements may optionally be present:
    </p>
    <ul>
    <li><tt>annotation</tt> - zero or more instances of
    general documentation.</li>
    <li><tt>testSetRef</tt> - a set of references to the sets
    of tests which make up this test suite. No two test sets
    referenced may have the same name.</li>
    </ul>
    </div>
    """
    class Meta:
        name = "testSuite"
        namespace = "http://www.w3.org/XML/2004/xml-schema-test-suite/"

    annotation: List[Annotation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    test_set_ref: List[TestSetRef] = field(
        default_factory=list,
        metadata={
            "name": "testSetRef",
            "type": "Element",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    release_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "releaseDate",
            "type": "Attribute",
            "required": True,
        }
    )
    schema_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
            "required": True,
        }
    )
    version: List[Union[KnownToken, Decimal, str]] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class TestGroup:
    """<div>

    <p>
    This element groups a collection of closely related
    tests. All instance tests in the group are to be
    validated against the same schema; if a <tt>schemaTest</tt>
    is present, it is the schema produced for that test
    which should be used for the instance tests; if no
    <tt>schemaTest</tt> is present, the instance tests
    should be validated against a schema consisting only
    of the built-in components.
    </p>
    <p>
    The <tt>testGroup</tt> element has one attribute which is
    required:
    </p>
    <ul>
    <li><tt>name</tt> - an identifier for the <tt>testGroup</tt>
    which differs from the name of any other
    <tt>testGroup</tt> in the enclosing <tt>testSet</tt>.
    </li>
    </ul>
    <p>
    And one attribute which is optional:
    </p>
    <ul>
    <li>
    <p><tt>version</tt> - a list of version tokens, indicating
    that the tests in the group are applicable to implementations
    supporting <em>any</em> of the versions or features
    or behaviors indicated.  Any processor or processor
    configuration which supports <em>any</em> of the features
    indicated should run the tests.  Processors which support
    <em>none</em> of them can skip the entire test set.
    See the definition of the
    <a href="#type_version-info"><tt>version-info</tt></a>
    type.
    </p>
    <p>
    Logically, all keywords appearing here should also appear
    in the <tt>version</tt> attribute of the enclosing
    <tt>testSet</tt>, if it has one.
    </p>
    </li>
    </ul>
    <p>
    Four child elements may optionally be present:
    </p>
    <ul>
    <li>
    <p><tt>annotation</tt> - zero or more instances of
    general documentation.</p>
    </li>
    <li>
    <p><tt>documentationReference</tt> - any number of
    references to external documentation upon which the
    test is based, e.g. links to relevant sections of the
    Recommendation, to the Errata, etc.</p>
    </li>
    <li>
    <p><tt>schemaTest</tt> - at most on <tt>schemaTest</tt>
    element, containing any number of
    <tt>schemaDocument</tt> elements, each of which holds
    information on a single schema document.
    </p>
    <p>
    When more than one schema document is present, a single
    schema is constructed from the set (or from other
    schemas via import).
    </p>
    <p class="note">Note: XSD's rules for schema composition
    mean that the order in which schema documents are
    encountered may be significant.  When more than one
    schema document is listed in the <tt>schemaTest</tt>
    element, the test should be run as if the schema
    documents given were loaded one by one, in order.  For
    most processors that will correspond to the result of
    processing an otherwise empty schema document for an
    otherwise unused namespace, containing one
    <tt>xsd:import</tt> element for each schema document
    listed in the <tt>schemaTest</tt>, with the location
    indicated, in a processing mode that involves
    following the schema-location hints in import
    statements.
    </p>
    <p class="note">Note: the working group has made no
    decision on whether the schema should be constructed
    solely from the schema documents listed in the
    <tt>schemaTest</tt> element, or from those schema
    documents plus the transitive closure of their
    references to other schema documents.  Similarly, the
    working group has not decided whether
    <tt>schemaLocation</tt> hints in the instance tests
    should be honored or not.  It is therefore advisable
    to draft test cases without dependencies on
    <tt>schemaLocation</tt> hints and the like.
    </p>
    <p class="note">Note: work is pending on these issues of
    schema composition.  When it's complete, this part o
    the test suite schema may be expected to change.
    </p>
    <p>
    Schema documents may be omitted, for the purpose of
    testing a processor's validation of an instance
    containing only the built-in datatypes defined in the
    Recommendation.
    </p>
    </li>
    <li>
    <p><tt>instanceTest</tt> - any number of elements, each
    of which holds information on a single instance
    document to be validated against the included
    schema.</p>
    </li>
    </ul>
    </div>
    """
    class Meta:
        name = "testGroup"
        namespace = "http://www.w3.org/XML/2004/xml-schema-test-suite/"

    annotation: List[Annotation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    documentation_reference: List[DocumentationReference] = field(
        default_factory=list,
        metadata={
            "name": "documentationReference",
            "type": "Element",
        }
    )
    schema_test: Optional[SchemaTest] = field(
        default=None,
        metadata={
            "name": "schemaTest",
            "type": "Element",
        }
    )
    instance_test: List[InstanceTest] = field(
        default_factory=list,
        metadata={
            "name": "instanceTest",
            "type": "Element",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version: List[Union[KnownToken, Decimal, str]] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )


@dataclass
class TestSet:
    """<div>

    <p>
    The root element of a document describing a set of tests,
    normally from a single contributor.  A contributor may
    supply any number of <tt>testSet</tt> files.
    </p>
    <p class="note">
    Note: In order to make it possible to browse the test
    suite in a browser, it is helpful if large test
    collections are broken up into several <tt>testSet</tt>
    documents of no more than a megabyte or so each.  If
    contributions have larger <tt>testSet</tt> documents, they
    may be broken up into smaller ones.
    </p>
    <p>
    The element has two attributes:
    </p>
    <ul>
    <li>
    <p><tt>contributor (required)</tt> - the name of the contributor of
    this <tt>testSet</tt>.  May contain any string of characters;
    intended for human readers.</p>
    </li>
    <li>
    <p><tt>name (required)</tt> - the name of this <tt>testSet</tt>,
    which must be a name unique among the names of
    <tt>testSet</tt> elements within the enclosing
    <tt>testSuite</tt>.</p>
    </li>
    <li>
    <p><tt>version (optional)</tt> - a list of version tokens indicating
    versions and features for which at least some tests in the
    test set are applicable.</p>
    <p>Any processor or processor configuration which
    supports <em>any</em> of the tokens given should run
    the tests.  Processors which support none of the named
    features can skip the entire test set without loss.
    If no <tt>version</tt> value is given, or if the value
    is the empty string, all processors should run the
    tests.</p>
    <p>Logically, the tokens given in the <tt>version</tt>
    attribute should all also be included in the
    <tt>version</tt> attribute [if any] of any
    <tt>testSuite</tt> including this test set.  And
    similarly the <tt>version</tt> attribute on a
    <tt>testSet</tt> element should include all the tokens
    used on any <tt>testGroup</tt>, <tt>schemaTest</tt>,
    or <tt>instanceTest</tt> in the test set, and no
    others.  Otherwise processors may skip test sets they
    ought to run.  This logical rule is not necessarily
    enforced, however, by the schema for this
    vocabulary.</p>
    </li>
    </ul>
    <p>
    Two child elements may optionally be present:
    </p>
    <ul>
    <li><tt>annotation</tt> - zero or more instances of general
    documentation.
    </li>
    <li><tt>testGroup</tt> - a set of <tt>testGroup</tt>
    elements, each of which defines a group of closely
    related tests.

    No two <tt>testGroup</tt> elements in the same
    <tt>testSet</tt> may have the same name.
    </li>
    </ul>
    </div>
    """
    class Meta:
        name = "testSet"
        namespace = "http://www.w3.org/XML/2004/xml-schema-test-suite/"

    annotation: List[Annotation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    test_group: List[TestGroup] = field(
        default_factory=list,
        metadata={
            "name": "testGroup",
            "type": "Element",
        }
    )
    contributor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version: List[Union[KnownToken, Decimal, str]] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )
