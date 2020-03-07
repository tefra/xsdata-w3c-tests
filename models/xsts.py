from decimal import Decimal
from enum import Enum
from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict, List, Optional
from models.xlink import (
    TypeType,
)


class XdmFiltering(Enum):
    """<ns0:div>

        <ns0:p>Clause 1.2 of validation rule<ns0:a>Assertion satisifed</ns0:a>(in Structures sec. 3.13.4.1) says</ns0:p>
        <ns0:blockquote>
          <ns0:p>By default, comments and processing instructions are
                excluded from the partial post-schema-validation infoset,
                but at user option processors may retain comments and
                processing instructions instead of excluding them.</ns0:p>
        </ns0:blockquote>
        <ns0:p>The value "<ns0:tt>comments-and-PIs-excluded</ns0:tt>" denotes the default
                situation:  comments and processing instructions are suppressed
                before creating the XDM instance and thus cannot be examined
                by assertions.</ns0:p>
        <ns0:p>The value "<ns0:tt>comments-and-PIs-included</ns0:tt>" denotes the opposite:
                comments and processing instructions are included in the XDM
                instance and thus can be examined by assertions.  (Since this is
                required to be "at user option", any processor that supports this
                token must also be available in a configuration that supports the
                other token.)</ns0:p>
        <ns0:p>(The user option was added in November 2012 to address bug<ns0:a>13935
                xsd 1.1 assertions testing comment nodes</ns0:a>.
                These token values were added 20 January 2012 to allow both
                configurations to be tested.)</ns0:p>
      </ns0:div>
    :cvar COMMENTS_AND_PIS_EXCLUDED:
    :cvar COMMENTS_AND_PIS_INCLUDED:
    """
    COMMENTS_AND_PIS_EXCLUDED = "comments-and-PIs-excluded"
    COMMENTS_AND_PIS_INCLUDED = "comments-and-PIs-included"


@dataclass
class Appinfo:
    """
    :ivar any_element:
    :ivar source:
    :ivar attributes:
    """
    class Meta:
        name = "appinfo"
        mixed = True
        namespace = "http://www.w3.org/XML/2004/xml-schema-test-suite/"

    any_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Any",
            namespace="##any",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    source: Optional[str] = field(
        default=None,
        metadata=dict(
            name="source",
            type="Attribute"
        )
    )
    attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            name="attributes",
            type="AnyAttribute"
        )
    )


@dataclass
class Documentation:
    """
    :ivar any_element:
    :ivar source:
    :ivar lang:
    :ivar attributes:
    """
    class Meta:
        name = "documentation"
        mixed = True
        namespace = "http://www.w3.org/XML/2004/xml-schema-test-suite/"

    any_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Any",
            namespace="##any",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    source: Optional[str] = field(
        default=None,
        metadata=dict(
            name="source",
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            name="lang",
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            name="attributes",
            type="AnyAttribute"
        )
    )


class ExpectedOutcome(Enum):
    """<ns0:div>

        <ns0:p>Enumerates the possible values for the prescribed outcome
                of a test.  Values include both (a) the possible values of
                type<ns0:a>ts:test-outcome</ns0:a>and
                the following additional values:</ns0:p>
        <ns0:dl>
          <ns0:dt>
            <ns0:tt>implementation-defined</ns0:tt>
          </ns0:dt>
          <ns0:dd>(For instance tests) The value of the<ns0:tt>[validity]</ns0:tt>property on the validation root
                  depends upon some property or behavior which is
                  explicitly described in the relevant version of the spec
                  as "implementation-defined", or for which the spec explicitly
                  imposes a requirement that implementations specify their
                  behavior.  (It follows that this
                  value should never occur for 1.0 tests.)</ns0:dd>
          <ns0:dd>(For schema tests) The conformance of the schema
                  depends upon some property or behavior explicitly
                  described in the spec as "implementation-defined",
                  or for which the spec explicitly
                  imposes a requirement that implementations specify their
                  behavior.</ns0:dd>
        </ns0:dl>
        <ns0:p>Note: in most cases of implementation-defined behaviors,
                as a matter of test suite design it is better to analyse
                the set of possible implementation behaviors, define
                version tokens for the possible behaviors, and specify
                more informative results based on those tokens.  The value<ns0:tt>implementation-defined</ns0:tt>is provided for situations
                where this is not feasible for whatever reason.</ns0:p>
        <ns0:dl>
          <ns0:dt>
            <ns0:tt>implementation-dependent</ns0:tt>
          </ns0:dt>
          <ns0:dd>(For instance tests) The value of the<ns0:tt>[validity]</ns0:tt>property on the validation root
                  depends upon some property or behavior which is
                  explicitly described in the relevant version of the spec
                  as "implementation-dependent", or otherwise explicitly
                  described as varying among implementations but not
                  "implementation-defined".  (For XSD 1.0, this will often
                  take the form of a normative "<ns0:span>may</ns0:span>" in the text.)</ns0:dd>
          <ns0:dd>(For schema tests) The conformance of the schema
                  depends upon some property or behavior explicitly
                  described in the spec as "implementation-dependent" or
                  as varying among implementations, but not described as
                  "implementation-defined".</ns0:dd>
          <ns0:dt>
            <ns0:tt>indeterminate</ns0:tt>
          </ns0:dt>
          <ns0:dd>The intended result is indeterminate for one of the
                  following reasons, or for other reasons:<ns0:ul><ns0:li>The result is under-determined (the spec is vague
                      or underspecified), but not described explicitly as
                      varying among conforming implementations.</ns0:li><ns0:li>The spec imposed contradictory requirements on the
                      result. (I.e. the result is<ns0:em>over-determined.)</ns0:em></ns0:li><ns0:li/></ns0:ul></ns0:dd>
        </ns0:dl>
        <ns0:p>N.B. the values<ns0:tt>implementation-dependent</ns0:tt>and<ns0:tt>implementation-defined</ns0:tt>should be used only when
                the spec is explicit about the implementation-dependence
                of the result and it is thus clear that the
                implementation-dependence is a design choice consciously
                made by the working group. They must not be used in cases
                where the spec simply appeals to some concept which it
                turns out not to define: such cases are to be marked<ns0:tt>indeterminate</ns0:tt>.</ns0:p>
        <ns0:p>Note:  in most cases, as a matter of language design
                it is better for the language specification to prescribe
                clearly a particular result for a test, or to identify the
                result explicitly as implementation-defined or
                implementation-dependent.  The value<ns0:tt>indeterminate</ns0:tt>is provided for situations where
                this has not been done for whatever reason.</ns0:p>
        <ns0:p>The value<ns0:tt>invalid-latent</ns0:tt>described
                in earlier drafts of this schema document is no longer
                needed; the version keywords for complex-type restriction
                behaviors can be used to describe the relevant cases
                more precisely.</ns0:p>
      </ns0:div>
    :cvar IMPLEMENTATION_DEFINED:
    :cvar IMPLEMENTATION_DEPENDENT:
    :cvar INDETERMINATE:
    :cvar INVALID:
    :cvar INVALID_LATENT:
    :cvar NOT_KNOWN:
    :cvar RUNTIME_SCHEMA_ERROR:
    :cvar VALID:
    """
    IMPLEMENTATION_DEFINED = "implementation-defined"
    IMPLEMENTATION_DEPENDENT = "implementation-dependent"
    INDETERMINATE = "indeterminate"
    INVALID = "invalid"
    INVALID_LATENT = "invalid-latent"
    NOT_KNOWN = "notKnown"
    RUNTIME_SCHEMA_ERROR = "runtime-schema-error"
    VALID = "valid"


class KnownToken(Enum):
    """<ns0:div>

        <ns0:p>Tokens to denote well-known (i.e. documented)
                versions, features, or implementation-defined behaviors,
                of XSD.</ns0:p>
        <ns0:p>The<ns0:tt>known-token</ns0:tt>type is a union of several other
                types, each with an enumeration of values.  Each sub-type
                defines keywords for a set of mutually exclusive versions,
                features, or behaviors, such that in any given schema
                validation episode, at most one keyword in any subtype
                will apply.  For examples, see the various subtypes
                defined immediately below.</ns0:p>
      </ns0:div>
    :cvar VALUE_1_0:
    :cvar VALUE_1_0_1E:
    :cvar VALUE_1_0_2E:
    :cvar VALUE_1_1:
    :cvar CTR_ALL_COMPILE:
    :cvar CTR_ALL_IDEP:
    :cvar CTR_ALL_RUNTIME:
    :cvar UNICODE_4_0_0:
    :cvar UNICODE_6_0_0:
    :cvar XML_1_0:
    :cvar XML_1_0_1E_4E:
    :cvar XML_1_0_5E:
    :cvar XML_1_1:
    :cvar COMMENTS_AND_PIS_EXCLUDED:
    :cvar COMMENTS_AND_PIS_INCLUDED:
    :cvar FULL_XPATH_IN_CTA:
    :cvar RESTRICTED_XPATH_IN_CTA:
    """
    VALUE_1_0 = "1.0"
    VALUE_1_0_1E = "1.0-1e"
    VALUE_1_0_2E = "1.0-2e"
    VALUE_1_1 = "1.1"
    CTR_ALL_COMPILE = "CTR-all-compile"
    CTR_ALL_IDEP = "CTR-all-idep"
    CTR_ALL_RUNTIME = "CTR-all-runtime"
    UNICODE_4_0_0 = "Unicode_4.0.0"
    UNICODE_6_0_0 = "Unicode_6.0.0"
    XML_1_0 = "XML-1.0"
    XML_1_0_1E_4E = "XML-1.0-1e-4e"
    XML_1_0_5E = "XML-1.0-5e"
    XML_1_1 = "XML-1.1"
    COMMENTS_AND_PIS_EXCLUDED = "comments-and-PIs-excluded"
    COMMENTS_AND_PIS_INCLUDED = "comments-and-PIs-included"
    FULL_XPATH_IN_CTA = "full-xpath-in-CTA"
    RESTRICTED_XPATH_IN_CTA = "restricted-xpath-in-CTA"


class KnownXsdVersion(Enum):
    """<ns0:div>

        <ns0:p>Tokens to denote specific known versions of XSD.</ns0:p>
        <ns0:p>Each token denotes the version of the XSD language
                identified by the<ns0:tt>ts:standard-version-id</ns0:tt>attribute on the<ns0:tt>xsd:enumeration</ns0:tt>element.
                That is, "<ns0:tt>1.0</ns0:tt>" denotes XSD 1.0 (without reference
                to a particular edition), and "<ns0:tt>1.1</ns0:tt>" denotes XSD 1.1
                (without referece to a particular edition).</ns0:p>
      </ns0:div>
    :cvar VALUE_1_0:
    :cvar VALUE_1_1:
    """
    VALUE_1_0 = "1.0"
    VALUE_1_1 = "1.1"


class RuntimeSchemaError(Enum):
    """<ns0:div>

        <ns0:p>Tokens to denote different implementation-defined
                behavior in the presence of faulty restriction in
                a complex-type definition.</ns0:p>
        <ns0:p>A full explanation of this token and its meaning
                is needed, but not yet available. For the moment let it
                suffice to say that if an<ns0:tt>all</ns0:tt>-group
                in a restriction allows content not allowed by
                the base type, the processor is not required
                to detect the problem by inspection of the schema
                in isolation.  Three behaviors are allowed; the choice
                among them is implementation-defined.  The values
                denoting the three behaviors are these.</ns0:p>
        <ns0:dl>
          <ns0:dt>
            <ns0:tt>CTR-all-compile</ns0:tt>
          </ns0:dt>
          <ns0:dd>Compile-time detection:  the processor always
                  detects the problem by examining the schema in
                  isolation; it warrants that no non-conforming
                  schema will ever be used in validation.</ns0:dd>
          <ns0:dt>
            <ns0:tt>CTR-all-runtime</ns0:tt>
          </ns0:dt>
          <ns0:dd>Run-time detection:  the processor never
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
                  base type.)</ns0:dd>
          <ns0:dt>
            <ns0:tt>CTR-all-idep</ns0:tt>
          </ns0:dt>
          <ns0:dd>Implementation-dependent detection:  the processor
                  sometimes detects the problem by examining the schema in
                  isolation, sometimes when examining an instance.
                  No guarantees.</ns0:dd>
        </ns0:dl>
        <ns0:p>Note, 20 January 2012.  Is this distinction still required,
              or has it been overtaken by the change made to resolve<ns0:a>bug 12185 Conditional Type Assignment and substitutability</ns0:a>(or other late changes)?</ns0:p>
      </ns0:div>
    :cvar CTR_ALL_COMPILE:
    :cvar CTR_ALL_IDEP:
    :cvar CTR_ALL_RUNTIME:
    """
    CTR_ALL_COMPILE = "CTR-all-compile"
    CTR_ALL_IDEP = "CTR-all-idep"
    CTR_ALL_RUNTIME = "CTR-all-runtime"


class Status(Enum):
    """
    :cvar ACCEPTED:
    :cvar DISPUTED_SPEC:
    :cvar DISPUTED_TEST:
    :cvar QUERIED:
    :cvar STABLE:
    """
    ACCEPTED = "accepted"
    DISPUTED_SPEC = "disputed-spec"
    DISPUTED_TEST = "disputed-test"
    QUERIED = "queried"
    STABLE = "stable"


class TestOutcome(Enum):
    """<ns0:div>

        <ns0:p>Enumerates the possible outcomes of running a test.
                Usually, these are values of the<ns0:tt>[validity]</ns0:tt>property on the validation root.</ns0:p>
        <ns0:p>The most common values are:</ns0:p>
        <ns0:dl>
          <ns0:dt>
            <ns0:tt>valid</ns0:tt>
          </ns0:dt>
          <ns0:dd>(For instance tests) The value of the<ns0:tt>[validity]</ns0:tt>property on the validation root is<ns0:tt>valid</ns0:tt>.</ns0:dd>
          <ns0:dd>(For schema tests) The schema is a conforming schema.</ns0:dd>
          <ns0:dt>
            <ns0:tt>invalid</ns0:tt>
          </ns0:dt>
          <ns0:dd>(For instance tests) The value of the<ns0:tt>[validity]</ns0:tt>property on the validation root is<ns0:tt>invalid</ns0:tt>.</ns0:dd>
          <ns0:dd>(For schema tests) The schema is<ns0:em>not</ns0:em>a
                  conforming schema.</ns0:dd>
          <ns0:dt>
            <ns0:tt>notKnown</ns0:tt>
          </ns0:dt>
          <ns0:dd>(For instance tests) The value of the<ns0:tt>[validity]</ns0:tt>property on the validation root is<ns0:tt>notKnown</ns0:tt>.</ns0:dd>
          <ns0:dd>(For schema tests, this value is meaningless.)</ns0:dd>
        </ns0:dl>
        <ns0:p>Note:  processors built as<ns0:a>instance validators</ns0:a>are not required by XSD to
                distinguish between invalid documents and documents with
                unknown validity; it is thus not an absolute requirement
                (although it is desirable for clarity)
                that a test result distinguish<ns0:tt>invalid</ns0:tt>from<ns0:tt>notKnown</ns0:tt>outcomes.</ns0:p>
        <ns0:p>One further value is needed only in fairly specialized
                circumstances (but is essential there):</ns0:p>
        <ns0:dl>
          <ns0:dt>
            <ns0:tt>runtime-schema-error</ns0:tt>
          </ns0:dt>
          <ns0:dd>
            <ns0:p>(For instance tests) The instance has a schema with
                    a latent error (see description below in the documentation
                    for type<ns0:a>ts:expected-outcome</ns0:a>);
                    the processor did not detect the latent error on the
                    corresponding schema test, but the instance document
                    has exposed the error (by including content
                    which is valid against the apparent content model of the
                    governing type, but not valid against the base type)
                    and the processor has detected the schema error in the
                    course of instance validation.</ns0:p>
            <ns0:p>Note: processors are encouraged, though not required, to
                    distinguish this outcome from<ns0:tt>invalid</ns0:tt>, since
                    on an instance test<ns0:tt>invalid</ns0:tt>normally means that
                    the processor has found an invalid instance, not a
                    non-conforming schema.</ns0:p>
          </ns0:dd>
          <ns0:dd>
            <ns0:p>(For schema tests) The value<ns0:tt>runtime-schema-error</ns0:tt>is meaningless for schema tests and should not be used for
                    them.  (It would be a contradiction in terms.)</ns0:p>
          </ns0:dd>
        </ns0:dl>
      </ns0:div>
    :cvar INVALID:
    :cvar NOT_KNOWN:
    :cvar RUNTIME_SCHEMA_ERROR:
    :cvar VALID:
    """
    INVALID = "invalid"
    NOT_KNOWN = "notKnown"
    RUNTIME_SCHEMA_ERROR = "runtime-schema-error"
    VALID = "valid"


class UnicodeVersions(Enum):
    """<ns0:div>

        <ns0:p>Tokens to denote specific known versions of Unicode.</ns0:p>
        <ns0:p>Each token denotes the version of the Unicode specification. The list
                is not complete; in the only cases where results are known to vary
                between Unicode versions, results are published for version 4.0.0
                and 6.0.0. Implementors wishing to provide reference results for
                other versions of Unicode are welcome to submit such results.</ns0:p>
      </ns0:div>
    :cvar UNICODE_4_0_0:
    :cvar UNICODE_6_0_0:
    """
    UNICODE_4_0_0 = "Unicode_4.0.0"
    UNICODE_6_0_0 = "Unicode_6.0.0"


class XmlSubstrate(Enum):
    """<ns0:div>

        <ns0:p>Tokens to denote different versions of XML-dependent
                datatypes.  Conforming XSD 1.1 processors may support
                XML 1.0-based datatypes, XML 1.1-based datatypes,
                or both.  There is dispute in the working group over
                whether conforming XSD 1.0 processors are allowed to
                suport XML 1.1-based datatypes or not.</ns0:p>
        <ns0:p>The value "<ns0:tt>XML-1.0</ns0:tt>" denotes processor support
                for, or test applicability to, XSD datatypes based on XML
                1.0, without specifying a particular edition.  (This value
                is retained for backward compatibility of this schema, but
                it should be avoided unless there is no difference, for a
                given test or test result, between editions 1-4 and
                edition 5 of XML 1.0. Where there is a difference, the
                values "<ns0:tt>XML-1.0-1e-4e</ns0:tt>" and "<ns0:tt>XML-1.0-5e</ns0:tt>"
                should be used in preference.
                (XSD 1.1 describes XML 1.0 Fifth Edition as the base
                version in its normative reference, so in theory the
                distinction between "<ns0:tt>XML-1.0-1e-4e</ns0:tt>" and
                "<ns0:tt>XML-1.0-5e</ns0:tt>" is only relevant to XSD 1.0
                processors.  In practice, it may also be relevant for some
                XSD 1.1 processors.</ns0:p>
        <ns0:p>The value "<ns0:tt>XML-1.0-1e-4e</ns0:tt>" denotes processor support
                for, or test applicability to, XSD datatypes based on XML
                1.0 First Edition through Fourth Edition.</ns0:p>
        <ns0:p>The value "<ns0:tt>XML-1.0-5e</ns0:tt>" denotes processor support
                for, or test applicability to, XSD datatypes based on XML
                1.0 Fifth Edition.</ns0:p>
        <ns0:p>The value "<ns0:tt>XML-1.1</ns0:tt>" denotes processor support
                for, or test applicability to, XSD datatypes based on XML
                1.1 (for which at the moment there is only one edition).</ns0:p>
        <ns0:p>In most cases, of course, "<ns0:tt>XML-1.0-5e</ns0:tt>" and
                "<ns0:tt>XML-1.1</ns0:tt>" will describe the same behaviors.</ns0:p>
      </ns0:div>
    :cvar XML_1_0:
    :cvar XML_1_0_1E_4E:
    :cvar XML_1_0_5E:
    :cvar XML_1_1:
    """
    XML_1_0 = "XML-1.0"
    XML_1_0_1E_4E = "XML-1.0-1e-4e"
    XML_1_0_5E = "XML-1.0-5e"
    XML_1_1 = "XML-1.1"


class XpathInCta(Enum):
    """<ns0:div>

        <ns0:p>Tokens to distinguish tests which use only the "required
                subset" of XPath in conditional type assignment
                from tests which use full XPath (or: any XPath outside
                the subset) in conditional type assignment.
                See "3.12.6 Constraints on Type Alternative Schema Components"
                of the Structures spec, which reads in part</ns0:p>
        <ns0:blockquote>
          <ns0:p>A conforming processor must accept and process any XPath
                expression conforming to the "required subset" of [XPath 2.0]
                defined by the following grammar.</ns0:p>
          <ns0:p>Note: Any XPath expression containing no static errors as
                  defined in [XPath 2.0] may appear in a conforming schema.
                  Conforming processors may but are not required to support
                  XPath expressions not belonging to the required subset of
                XPath.</ns0:p>
        </ns0:blockquote>
        <ns0:p>The value "<ns0:tt>restricted-xpath-in-CTA</ns0:tt>" denotes processor support
                for, or test applicability to, the minimal subset of XPath
                required of all conforming 1.1 processors.  All 1.1 processors
                should support this feature and run tests marked with it.</ns0:p>
        <ns0:p>The value "<ns0:tt>full-xpath-in-CTA</ns0:tt>" denotes processor support
                for, or test applicability to, full XPath in conditional type
                assignment expressions.</ns0:p>
        <ns0:p>(These token values were added 29 July 2011 to address bug<ns0:a>13455
                XPath subset causes problem</ns0:a>.)</ns0:p>
      </ns0:div>
    :cvar FULL_XPATH_IN_CTA:
    :cvar RESTRICTED_XPATH_IN_CTA:
    """
    FULL_XPATH_IN_CTA = "full-xpath-in-CTA"
    RESTRICTED_XPATH_IN_CTA = "restricted-xpath-in-CTA"


class Xsd10Editions(Enum):
    """<ns0:div>

        <ns0:p>Tokens to denote specific editions of XSD 1.0.</ns0:p>
        <ns0:p>Each token denotes the version of the XSD language
                identified by the<ns0:tt>ts:standard-version-id</ns0:tt>attribute on the<ns0:tt>xsd:enumeration</ns0:tt>element.
                That is,
                "<ns0:tt>1.0-1e</ns0:tt>" and "<ns0:tt>1.0-2e</ns0:tt>" represent
                1.0 First Edition and 1.0 Second Edition,
                respectively.</ns0:p>
        <ns0:p>Outside the context of XSD 1.0, these edition
                identifiers have no meaning or applicability.</ns0:p>
      </ns0:div>
    :cvar VALUE_1_0_1E:
    :cvar VALUE_1_0_2E:
    """
    VALUE_1_0_1E = "1.0-1e"
    VALUE_1_0_2E = "1.0-2e"


@dataclass
class Annotation:
    """<ns0:div>

        <ns0:p>This is an exact copy of the<ns0:tt>annotation</ns0:tt>element defined in the Schema
                Recommendation. It is duplicated here in order to replicate the
                functionality of the<ns0:tt>xsd:annotation</ns0:tt>element and because the Schema for
                Schemas cannot be imported.</ns0:p>
      </ns0:div>
    :ivar appinfo:
    :ivar documentation:
    :ivar attributes:
    """
    class Meta:
        name = "annotation"
        namespace = "http://www.w3.org/XML/2004/xml-schema-test-suite/"

    appinfo: List[Appinfo] = field(
        default_factory=list,
        metadata=dict(
            name="appinfo",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    documentation: List[Documentation] = field(
        default_factory=list,
        metadata=dict(
            name="documentation",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            name="attributes",
            type="AnyAttribute"
        )
    )


@dataclass
class Expected:
    """<ns0:div>

        <ns0:p>The validation outcome prescribed by the spec
                for a test in the XSTS.</ns0:p>
        <ns0:p>This element has one optional attribute:</ns0:p>
        <ns0:ul>
          <ns0:li>
            <ns0:p><ns0:tt>version</ns0:tt>- a list of version tokens.
                    The result specified is applicable to processor
                    configurations supporting<ns0:em>all</ns0:em>of the
                    indicated versions or features of XSD.
                    See the definition of the<ns0:a><ns0:tt>version-info</ns0:tt></ns0:a>type.</ns0:p>
            <ns0:p>It is an error for more than one<ns0:tt>expected</ns0:tt>element to be applicable to any given processor
                    configuration; this is most easily avoided by
                    making sure that any two sibling<ns0:tt>expected</ns0:tt>elements have<ns0:tt>version</ns0:tt>attributes containing
                    mutually exclusive tokens.</ns0:p>
          </ns0:li>
        </ns0:ul>
        <ns0:p>Note: The meaning of the<ns0:tt>version</ns0:tt></ns0:p>
        <ns0:p>On tests and elements for groups of
                tests (<ns0:tt>testGroup</ns0:tt>etc.), a<ns0:tt>version</ns0:tt>attribute of the form<ns0:code>version="<ns0:i>x</ns0:i><ns0:i>y</ns0:i><ns0:i>z</ns0:i>"</ns0:code>means "If<ns0:strong>any</ns0:strong>of<ns0:tt>x</ns0:tt>,<ns0:tt>y</ns0:tt>, or<ns0:tt>z</ns0:tt>are supported, tests
                in this group are applicable."</ns0:p>
        <ns0:p>On the<ns0:tt>expected</ns0:tt>element, the
                meaning changes in a crucial way: the tokens are connected
                with an implicit<ns0:tt>and</ns0:tt>, not an<ns0:tt>or</ns0:tt>. So<ns0:code>version="<ns0:i>x</ns0:i><ns0:i>y</ns0:i><ns0:i>z</ns0:i>"</ns0:code>means
                "If<ns0:strong>all</ns0:strong>of<ns0:tt>x</ns0:tt>,<ns0:tt>y</ns0:tt>, or<ns0:tt>z</ns0:tt>are supported, the prescribed outcome is as
                described.  So on a test group,<ns0:code>version="1.0
                  1.1"</ns0:code>means tests for both versions are included.
                On an<ns0:tt>expected</ns0:tt>element,<ns0:code>version="1.0
                  1.1"</ns0:code>would mean the expected result holds only if a
                given processor is using both version 1.0 and version 1.1
                in the same validation episode.  Since the two tokens are
                defined as mutually exclusive, this would be a
                contradiction.</ns0:p>
        <ns0:p>As a matter of test suite design, it
                is a good idea to keep<ns0:tt>version</ns0:tt>attributes
                on<ns0:tt>expected</ns0:tt>elements to a single token if
                possible, to minimize opportunities for confusion.</ns0:p>
        <ns0:p>And one required attribute:</ns0:p>
        <ns0:ul>
          <ns0:li>
            <ns0:p><ns0:tt>validity</ns0:tt>- indicates the expected outcome
                    of the test, using a value of type<ns0:a>ts:expected-outcome</ns0:a>.</ns0:p>
            <ns0:p>For an instance test, this typically indicates the expected
                    value of the<ns0:code>[validity]</ns0:code>property on the
                    root element of the instance document, or indicates
                    that the value may vary among processors.</ns0:p>
            <ns0:p>For a schema test, this indicates whether the
                    schema created from the schema documents in the test
                    is expected to be a conforming schema (<ns0:code>valid</ns0:code>)
                    or a non-conforming schema (<ns0:code>invalid</ns0:code>).
                    The value<ns0:code>notKnown</ns0:code>has no meaning
                    for a schema test.</ns0:p>
          </ns0:li>
        </ns0:ul>
      </ns0:div>
    :ivar validity:
    :ivar version:
    :ivar attributes:
    """
    class Meta:
        name = "expected"
        namespace = "http://www.w3.org/XML/2004/xml-schema-test-suite/"

    validity: Optional[ExpectedOutcome] = field(
        default=None,
        metadata=dict(
            name="validity",
            type="Attribute",
            required=True
        )
    )
    version: Optional[str] = field(
        default=None,
        metadata=dict(
            name="version",
            type="Attribute"
        )
    )
    attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            name="attributes",
            type="AnyAttribute"
        )
    )


@dataclass
class Ref:
    """
    :ivar annotation:
    :ivar type:
    :ivar href:
    :ivar attributes:
    """
    class Meta:
        name = "ref"

    annotation: List[Annotation] = field(
        default_factory=list,
        metadata=dict(
            name="annotation",
            type="Element",
            namespace="http://www.w3.org/XML/2004/xml-schema-test-suite/",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    type: TypeType = field(
        default="locator",
        metadata=dict(
            name="type",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )
    href: Optional[str] = field(
        default=None,
        metadata=dict(
            name="href",
            type="Attribute",
            namespace="http://www.w3.org/1999/xlink"
        )
    )
    attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            name="attributes",
            type="AnyAttribute"
        )
    )


@dataclass
class StatusEntry:
    """
    :ivar annotation:
    :ivar status:
    :ivar date:
    :ivar bugzilla:
    :ivar attributes:
    """
    class Meta:
        name = "statusEntry"

    annotation: List[Annotation] = field(
        default_factory=list,
        metadata=dict(
            name="annotation",
            type="Element",
            namespace="http://www.w3.org/XML/2004/xml-schema-test-suite/",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    status: Optional[Status] = field(
        default=None,
        metadata=dict(
            name="status",
            type="Attribute",
            required=True
        )
    )
    date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="date",
            type="Attribute",
            required=True
        )
    )
    bugzilla: Optional[str] = field(
        default=None,
        metadata=dict(
            name="bugzilla",
            type="Attribute",
            pattern=r"http://www\.w3\.org/Bugs/Public/show_bug\.cgi\?id=[0-9]*"
        )
    )
    attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            name="attributes",
            type="AnyAttribute"
        )
    )


@dataclass
class TestResult:
    """<ns0:div>

        <ns0:p>The result of an individual instance test or a schema test.</ns0:p>
        <ns0:p>This element has four required attributes:</ns0:p>
        <ns0:ul>
          <ns0:li><ns0:tt>validity</ns0:tt>- the validition outcome of the test.
                  A value of type<ns0:a>ts:expected-outcome</ns0:a>,
                  i.e.
                  one of "<ns0:tt>valid</ns0:tt>", "<ns0:tt>invalid</ns0:tt>",
                  "<ns0:tt>notKnown</ns0:tt>", or "<ns0:tt>runtime-schema-error</ns0:tt>".</ns0:li>
          <ns0:li><ns0:tt>set</ns0:tt>- the value of the "<ns0:tt>name</ns0:tt>"
                  attribute of the test set to which the test belongs.</ns0:li>
          <ns0:li><ns0:tt>group</ns0:tt>- the value of the "<ns0:tt>name</ns0:tt>"
                  attribute of the test group to which the test belongs.</ns0:li>
          <ns0:li><ns0:tt>test</ns0:tt>- the value of the "<ns0:tt>name</ns0:tt>"
                  attribute of the schema test or instance test, the
                  validation outcome of which this result reports.</ns0:li>
        </ns0:ul>
        <ns0:p>NOTE: The "<ns0:tt>set</ns0:tt>", "<ns0:tt>group</ns0:tt>" and
                "<ns0:tt>test</ns0:tt>" attributes are used to uniquely identify
                the test within the XSTS for which this result reports the
                validation outcome.  Each matches the "<ns0:tt>name</ns0:tt>"
                attribute of the respective element in the test suite.</ns0:p>
        <ns0:p>This element has one optional attribute:</ns0:p>
        <ns0:ul>
          <ns0:li><ns0:tt>normalizedLoad</ns0:tt>- a relative load value, intended as an indicator
                  of the resource requirements of an individual
                  test. Values may be based on processing time,
                  memory usage or a combination of the two.
                  Values should be in the vicinity of 1.0.</ns0:li>
        </ns0:ul>
        <ns0:p>The element has one optional element:</ns0:p>
        <ns0:ul>
          <ns0:li><ns0:tt>annotation</ns0:tt>- zero or more instances of more detailed
                  (<ns0:tt>ts:documentation</ns0:tt>) or structured (<ns0:tt>ts:appinfo</ns0:tt>)
                  information or commentary regarding the individual
                  test result. Reporters are encouraged to use<ns0:tt>annotation/appinfo</ns0:tt>to report more detailed outcome
                  information, such as error and warning messages.</ns0:li>
        </ns0:ul>
      </ns0:div>
    :ivar annotation:
    :ivar validity:
    :ivar set:
    :ivar group:
    :ivar test:
    :ivar normalized_load:
    :ivar attributes:
    """
    class Meta:
        name = "testResult"
        namespace = "http://www.w3.org/XML/2004/xml-schema-test-suite/"

    annotation: List[Annotation] = field(
        default_factory=list,
        metadata=dict(
            name="annotation",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    validity: Optional[TestOutcome] = field(
        default=None,
        metadata=dict(
            name="validity",
            type="Attribute",
            required=True
        )
    )
    set: Optional[str] = field(
        default=None,
        metadata=dict(
            name="set",
            type="Attribute",
            required=True
        )
    )
    group: Optional[str] = field(
        default=None,
        metadata=dict(
            name="group",
            type="Attribute",
            required=True
        )
    )
    test: Optional[str] = field(
        default=None,
        metadata=dict(
            name="test",
            type="Attribute",
            required=True
        )
    )
    normalized_load: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            name="normalizedLoad",
            type="Attribute"
        )
    )
    attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            name="attributes",
            type="AnyAttribute"
        )
    )


@dataclass
class Current(StatusEntry):
    """<ns0:div>

      <ns0:p>The current status of a test in the XSTS.</ns0:p>
      <ns0:p>This element has two attributes, both of which are
              required:</ns0:p>
      <ns0:ul>
        <ns0:li><ns0:tt>status</ns0:tt>- the status of the test. One of
                "<ns0:tt>accepted</ns0:tt>", "<ns0:tt>stable</ns0:tt>",
                "<ns0:tt>disputed-test</ns0:tt>" or "<ns0:tt>disputed-spec</ns0:tt>"
                (see the XSTS website for an explanation of these values).</ns0:li>
        <ns0:li><ns0:tt>date</ns0:tt>- the date on which the test or the
                metadata (including the value in the<ns0:tt>status</ns0:tt>attribute, but also anything else
                of importance) was last changed.</ns0:li>
      </ns0:ul>
    </ns0:div>
    """
    class Meta:
        name = "current"
        namespace = "http://www.w3.org/XML/2004/xml-schema-test-suite/"



@dataclass
class DocumentationReference(Ref):
    """<ns0:div>

    <ns0:p>A link to documentation relevant to a test, such as a link to
    the           Recommendation, an erratum, an archived email discussion,
    etc.</ns0:p> </ns0:div>
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
    """<ns0:div>

      <ns0:p>A former status of a test in the XSTS.</ns0:p>
      <ns0:p>This element has two attributes, both of which are
              required:</ns0:p>
      <ns0:ul>
        <ns0:li><ns0:tt>status</ns0:tt>- the former status of the test. One of
                "<ns0:tt>accepted</ns0:tt>", "<ns0:tt>stable</ns0:tt>",
                "<ns0:tt>disputed-test</ns0:tt>" or "<ns0:tt>disputed-spec</ns0:tt>"
                (see the XSTS website for an explanation of these values).</ns0:li>
        <ns0:li><ns0:tt>date</ns0:tt>- the date on which the test or the
                metadata (including the value in the<ns0:tt>status</ns0:tt>attribute, but also anything else
                of importance) was last changed.</ns0:li>
      </ns0:ul>
    </ns0:div>
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
    """<ns0:div>

        <ns0:p>This is the root element of a document containing a test
                result report. The report takes the form of a set of test
                results returned by a processor/validator when run against
                the XSTS.</ns0:p>
        <ns0:p>It has three required attributes:</ns0:p>
        <ns0:ul>
          <ns0:li><ns0:tt>suite</ns0:tt>- the name of the test suite to which
                  these results correspond.  This should be the value of
                  the<ns0:tt>name</ns0:tt>attribute of the<ns0:tt>testSuite</ns0:tt>element at the root of the test suite document
                  describing the tests to which these results correspond.</ns0:li>
          <ns0:li><ns0:tt>processor</ns0:tt>- some identifying information for
                  the processor/ validator which produced the reported
                  results. The value of this attribute is left to the
                  discretion of the reporter.</ns0:li>
          <ns0:li><ns0:tt>submitDate</ns0:tt>- the date on which these results
                  were submitted to the XSTS Task Force.</ns0:li>
        </ns0:ul>
        <ns0:p>The element also has one optional attribute:</ns0:p>
        <ns0:ul>
          <ns0:li><ns0:tt>publicationPermission</ns0:tt>- the degree to which the
                  result reporter authorizes the W3C to disseminate the
                  reported results. One of "<ns0:tt>W3C members</ns0:tt>" or
                  "<ns0:tt>public</ns0:tt>" (see the XSTS website for an explanation
                  of these values). If this attribute is absent, no
                  permission to publish is granted.</ns0:li>
        </ns0:ul>
        <ns0:p>This element has two optional elements:</ns0:p>
        <ns0:ul>
          <ns0:li><ns0:tt>annotation</ns0:tt>- zero or more instances of more
                  detailed (<ns0:tt>ts:documentation</ns0:tt>) or structured
                  (<ns0:tt>ts:appinfo</ns0:tt>) information or commentary
                  regarding the enclosed test results.</ns0:li>
          <ns0:li><ns0:tt>testResult</ns0:tt>- any number of reports of the
                  results of individual tests. Any results may be omitted,
                  particularly those for tests of features for which the
                  processor claims no support.</ns0:li>
        </ns0:ul>
      </ns0:div>
    :ivar annotation:
    :ivar test_result:
    :ivar suite:
    :ivar processor:
    :ivar submit_date:
    :ivar publication_permission:
    :ivar attributes:
    """
    class Meta:
        name = "testSuiteResults"
        namespace = "http://www.w3.org/XML/2004/xml-schema-test-suite/"

    annotation: List[Annotation] = field(
        default_factory=list,
        metadata=dict(
            name="annotation",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    test_result: List[TestResult] = field(
        default_factory=list,
        metadata=dict(
            name="testResult",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    suite: Optional[str] = field(
        default=None,
        metadata=dict(
            name="suite",
            type="Attribute",
            required=True
        )
    )
    processor: Optional[str] = field(
        default=None,
        metadata=dict(
            name="processor",
            type="Attribute",
            required=True
        )
    )
    submit_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="submitDate",
            type="Attribute",
            required=True
        )
    )
    publication_permission: Optional["TestSuiteResults.PublicationPermission"] = field(
        default=None,
        metadata=dict(
            name="publicationPermission",
            type="Attribute"
        )
    )
    attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            name="attributes",
            type="AnyAttribute"
        )
    )

    class PublicationPermission(Enum):
        """
        :cvar W3_C_MEMBERS:
        :cvar PUBLIC:
        """
        W3_C_MEMBERS = "W3C members"
        PUBLIC = "public"


@dataclass
class InstanceTest:
    """<ns0:div>

        <ns0:p>This element groups together information about an instance
                document which should be validated against the schema
                referenced in the enclosing<ns0:tt>testGroup</ns0:tt>.</ns0:p>
        <ns0:p>Note: per section 5.2 "Assessing Schema-Validity" of the
                Recommendation "XML Schema Part 1: Structures", validation
                may be started in a variety of ways.  For the purposes of
                the XSTS, only the third method shall be used:</ns0:p>
        <ns0:blockquote>
          <ns0:p>The processor starts from Schema-Validity Assessment
                  (Element) (3.3.4) with no stipulated declaration or
                  definition.</ns0:p>
        </ns0:blockquote>
        <ns0:p>The validation root is the outermost element in the
                instance document.</ns0:p>
        <ns0:p>The<ns0:tt>instanceTest</ns0:tt>element has one required
                attribute:</ns0:p>
        <ns0:ul>
          <ns0:li><ns0:tt>name</ns0:tt>- the name of the instance document, which
                  must differ from the name of any other<ns0:tt>schemaTest</ns0:tt>or<ns0:tt>instanceTest</ns0:tt>element
                  within the enclosing<ns0:tt>testGroup</ns0:tt></ns0:li>
        </ns0:ul>
        <ns0:p>and one attribute which is optional, for signaling
                that the test is applicable only to a particular set of
                versions of XSD:</ns0:p>
        <ns0:ul>
          <ns0:li>
            <ns0:p><ns0:tt>version</ns0:tt>- Tests which only apply to certain
                    versions of XML Schema list those versions in the<ns0:tt>version</ns0:tt>attribute.</ns0:p>
            <ns0:p>Processors supporting<ns0:em>any</ns0:em>version or feature
                    indicated by a keyword in the attribute should run the
                    test.  (Or, more declaratively: the test is meaningful
                    to any processor which supports any of the features or
                    versions listed.)  If no value is specified, all
                    processors which haven't already skipped the enclosing
                    test group, test set, or test suite should run the
                    test.</ns0:p>
            <ns0:p>The value is a list of version tokens.  See the
                    definition of the<ns0:a><ns0:tt>version-info</ns0:tt></ns0:a>type.</ns0:p>
            <ns0:p>Note: running instance tests with a
                    processor for an inapplicable version may produce an
                    failure owing to non-conformant constructs in the
                    schema document; if the processor does not detect the
                    problem or continues anyway, the results are certain
                    to be meaningless.</ns0:p>
          </ns0:li>
        </ns0:ul>
        <ns0:p>One child element is required:</ns0:p>
        <ns0:ul>
          <ns0:li><ns0:tt>instanceDocument</ns0:tt>- a link to a file containing
                  the instance document.</ns0:li>
        </ns0:ul>
        <ns0:p>Four child elements may optionally be present:</ns0:p>
        <ns0:ul>
          <ns0:li><ns0:tt>annotation</ns0:tt>- zero or more instances of general
                  documentation</ns0:li>
          <ns0:li><ns0:tt>expected</ns0:tt>- the prescribed validation outcome for
                  the instance document.  Optional, and repeatable.
                  Each<ns0:tt>expected</ns0:tt>element indicates the result
                  on this test for a particular set of versions of the
                  language.</ns0:li>
          <ns0:li><ns0:tt>current</ns0:tt>- the current status of this test in
                  the XSTS (an indication of the test's accuracy in testing
                  the feature it is intended to test).</ns0:li>
          <ns0:li><ns0:tt>prior</ns0:tt>- the history of any changes in the
                  status of this test.</ns0:li>
        </ns0:ul>
        <ns0:p>The elements "<ns0:tt>expected</ns0:tt>" and "<ns0:tt>current</ns0:tt>" may
                be absent when tests are contributed, but will always be
                present for tests included in the XSTS.</ns0:p>
        <ns0:p>The<ns0:tt>current</ns0:tt>and<ns0:tt>prior</ns0:tt>elements should
                be used to keep a change history of the test; see
                discussion under the<ns0:a><ns0:tt>schemaTest</ns0:tt></ns0:a>element.</ns0:p>
      </ns0:div>
    :ivar annotation:
    :ivar instance_document:
    :ivar expected:
    :ivar current:
    :ivar prior:
    :ivar name:
    :ivar version:
    :ivar attributes:
    """
    class Meta:
        name = "instanceTest"
        namespace = "http://www.w3.org/XML/2004/xml-schema-test-suite/"

    annotation: List[Annotation] = field(
        default_factory=list,
        metadata=dict(
            name="annotation",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    instance_document: Optional[InstanceDocument] = field(
        default=None,
        metadata=dict(
            name="instanceDocument",
            type="Element",
            required=True
        )
    )
    expected: List[Expected] = field(
        default_factory=list,
        metadata=dict(
            name="expected",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    current: Optional[Current] = field(
        default=None,
        metadata=dict(
            name="current",
            type="Element"
        )
    )
    prior: List[Prior] = field(
        default_factory=list,
        metadata=dict(
            name="prior",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="name",
            type="Attribute",
            required=True
        )
    )
    version: Optional[str] = field(
        default=None,
        metadata=dict(
            name="version",
            type="Attribute"
        )
    )
    attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            name="attributes",
            type="AnyAttribute"
        )
    )


@dataclass
class SchemaTest:
    """<ns0:div>

        <ns0:p>This element groups together information about the schema
                for a particular test group.</ns0:p>
        <ns0:p>It has one attribute which is required:</ns0:p>
        <ns0:ul>
          <ns0:li><ns0:tt>name</ns0:tt>- the name of the schema test, which must be
                  unique within the enclosing<ns0:tt>testGroup</ns0:tt>(i.e. it must
                  differ from the name(s) of any associated<ns0:tt>instanceTest</ns0:tt>elements).</ns0:li>
        </ns0:ul>
        <ns0:p>and one attribute which is optional, for identifying a subset
                of versions and/or editions for which the test is valid:</ns0:p>
        <ns0:ul>
          <ns0:li>
            <ns0:p><ns0:tt>version</ns0:tt>- Tests which only apply to certain
                    versions of XML Schema list those versions in the<ns0:tt>version</ns0:tt>attribute.  Processors supporting<ns0:em>any</ns0:em>version or feature indicated by a keyword
                    in the attribute should run the test.  (Or, phrased
                    more declaratively: the test is meaningful to any
                    processor which supports any of the features or
                    versions listed.)</ns0:p>
            <ns0:p>If no value is specified, all processors which
                    haven't already skipped the enclosing test group,
                    test set, or test suite should run the test.</ns0:p>
            <ns0:p>The value is a list of version tokens.  See the
                    definition of the<ns0:a><ns0:tt>version-info</ns0:tt></ns0:a>type.</ns0:p>
            <ns0:p>Note that the omission of a version token on a schema
                    test is in some sense strictly advisory: any schema
                    test is meaningful for any processor in any
                    configuration.  For processor configurations not
                    supporting any of the features or versions named, the
                    expected result is that the schema is not a conforming
                    schema.  This will<ns0:em>not</ns0:em>be indicated with an
                    explicit<ns0:tt>expected</ns0:tt>element.</ns0:p>
          </ns0:li>
        </ns0:ul>
        <ns0:p>One child element is required:</ns0:p>
        <ns0:ul>
          <ns0:li><ns0:tt>schemaDocument</ns0:tt>- at least one link to a file
                  containing a schema document. The schema for the test is
                  constructed from the set (or from other schemas via
                  import).</ns0:li>
        </ns0:ul>
        <ns0:p>Four child elements may optionally be present:</ns0:p>
        <ns0:ul>
          <ns0:li><ns0:tt>annotation</ns0:tt>- zero or more instances of general
                  documentation</ns0:li>
          <ns0:li><ns0:tt>expected</ns0:tt>- indicates the conformance or
                  non-conformance of the schema described by the schema
                  document(s)
                  (<ns0:tt>valid</ns0:tt>= conformant,<ns0:tt>invalid</ns0:tt>=
                  non-conformant).</ns0:li>
          <ns0:li><ns0:tt>current</ns0:tt>- the current status of this test in
                  the XSTS (an indication of the test's accuracy in testing
                  the feature it is intended to test).</ns0:li>
          <ns0:li><ns0:tt>prior</ns0:tt>- the history of any changes in the
                  status of this test.</ns0:li>
        </ns0:ul>
        <ns0:p>The elements "<ns0:tt>expected</ns0:tt>" and "<ns0:tt>current</ns0:tt>"
                may be absent when tests are contributed, but will always
                be present for tests included in the XSTS.</ns0:p>
        <ns0:p>The<ns0:tt>current</ns0:tt>and<ns0:tt>prior</ns0:tt>elements were originally
                designed for tracking changes of status in tests; they can and
                should be used to keep a general change history of the test.
                Whenever anything changes that may be of importance for users
                of the test suite, it is appropriate to clone the existing<ns0:tt>current</ns0:tt>element into a pair of similar elements, then
                rename the second one<ns0:tt>prior</ns0:tt>.  In the new<ns0:tt>current</ns0:tt>element, the change made should be described in the<ns0:tt>annotation</ns0:tt>children, and the date of the change
                should be recorded.</ns0:p>
        <ns0:p>Examples:  The status of the test changes.  The expected
                result is questions and reaffirmed.  The expected result is
                changed, or multiple expected results are given for different
                processor configurations.</ns0:p>
        <ns0:p>For status changes involving bug reports, the relevant status
                entries should have a Bugzilla cross-reference.</ns0:p>
      </ns0:div>
    :ivar annotation:
    :ivar schema_document:
    :ivar expected:
    :ivar current:
    :ivar prior:
    :ivar name:
    :ivar version:
    :ivar attributes:
    """
    class Meta:
        name = "schemaTest"
        namespace = "http://www.w3.org/XML/2004/xml-schema-test-suite/"

    annotation: List[Annotation] = field(
        default_factory=list,
        metadata=dict(
            name="annotation",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    schema_document: List[SchemaDocument] = field(
        default_factory=list,
        metadata=dict(
            name="schemaDocument",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    expected: List[Expected] = field(
        default_factory=list,
        metadata=dict(
            name="expected",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    current: Optional[Current] = field(
        default=None,
        metadata=dict(
            name="current",
            type="Element"
        )
    )
    prior: List[Prior] = field(
        default_factory=list,
        metadata=dict(
            name="prior",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="name",
            type="Attribute",
            required=True
        )
    )
    version: Optional[str] = field(
        default=None,
        metadata=dict(
            name="version",
            type="Attribute"
        )
    )
    attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            name="attributes",
            type="AnyAttribute"
        )
    )


@dataclass
class TestSuite:
    """<ns0:div>

        <ns0:p>The root element of a document describing a set of tests for one
                or more versions of W3C XML Schema.</ns0:p>
        <ns0:p>The element has three attributes, each of which is required:</ns0:p>
        <ns0:ul>
          <ns0:li>
            <ns0:p><ns0:tt>name</ns0:tt>- the name of this test suite.</ns0:p>
          </ns0:li>
          <ns0:li>
            <ns0:p><ns0:tt>releaseDate</ns0:tt>- the date on which this test
                  suite was released. This value serves to identify the
                  version of the test suite.</ns0:p>
          </ns0:li>
          <ns0:li>
            <ns0:p><ns0:tt>schemaVersion</ns0:tt>- the versions of XSD for which
                  the tests are designed.  This has documentary function
                  only, and is intended for human readers.  The
                  machine-processable version information is handled by
                  the<ns0:tt>version</ns0:tt>attribute.</ns0:p>
          </ns0:li>
          <ns0:li>
            <ns0:p><ns0:tt>version</ns0:tt>- a list of version tokens indicating
                    versions and features for which at least some tests in the
                    test suite are applicable.</ns0:p>
            <ns0:p>Any processor or processor configuration which
                    supports<ns0:em>any</ns0:em>of the tokens given should run
                    the tests.  Processors which support none of the named
                    features can skip the entire test suite without loss.
                    If no<ns0:tt>version</ns0:tt>value is given, or if the value
                    is the empty string, all processors should run the
                    tests.</ns0:p>
            <ns0:p>For example<ns0:code>version="1.1"</ns0:code>on a test suite
                    element indicates that XSD 1.1 processors will find
                    relevant tests, and XSD 1.0 processors will not,
                    while<ns0:code>version="1.0 1.1"</ns0:code>, or no<ns0:code>version</ns0:code>attribute at all, indicates
                    that the test suite contains tests relevant to both.</ns0:p>
            <ns0:p>Logically, the<ns0:tt>version</ns0:tt>attribute on
                    the<ns0:tt>testSuite</ns0:tt>element, if given explicitly,
                    should include all the tokens used on any<ns0:tt>testSet</ns0:tt>,<ns0:tt>testGroup</ns0:tt>,<ns0:tt>schemaTest</ns0:tt>, or<ns0:tt>instanceTest</ns0:tt>in the
                    test suite, and no others.  This is not necessarily
                    enforced, however, by the schema for this
                    vocabulary.</ns0:p>
          </ns0:li>
        </ns0:ul>
        <ns0:p>Two child elements may optionally be present:</ns0:p>
        <ns0:ul>
          <ns0:li><ns0:tt>annotation</ns0:tt>- zero or more instances of
                  general documentation.</ns0:li>
          <ns0:li><ns0:tt>testSetRef</ns0:tt>- a set of references to the sets
                  of tests which make up this test suite. No two test sets
                  referenced may have the same name.</ns0:li>
        </ns0:ul>
      </ns0:div>
    :ivar annotation:
    :ivar test_set_ref:
    :ivar name:
    :ivar release_date:
    :ivar schema_version:
    :ivar version:
    :ivar attributes:
    """
    class Meta:
        name = "testSuite"
        namespace = "http://www.w3.org/XML/2004/xml-schema-test-suite/"

    annotation: List[Annotation] = field(
        default_factory=list,
        metadata=dict(
            name="annotation",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    test_set_ref: List[TestSetRef] = field(
        default_factory=list,
        metadata=dict(
            name="testSetRef",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="name",
            type="Attribute",
            required=True
        )
    )
    release_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="releaseDate",
            type="Attribute",
            required=True
        )
    )
    schema_version: Optional[str] = field(
        default=None,
        metadata=dict(
            name="schemaVersion",
            type="Attribute",
            required=True
        )
    )
    version: Optional[str] = field(
        default=None,
        metadata=dict(
            name="version",
            type="Attribute"
        )
    )
    attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            name="attributes",
            type="AnyAttribute"
        )
    )


@dataclass
class TestGroup:
    """<ns0:div>

        <ns0:p>This element groups a collection of closely related
                tests. All instance tests in the group are to be
                validated against the same schema; if a<ns0:tt>schemaTest</ns0:tt>is present, it is the schema produced for that test
                which should be used for the instance tests; if no<ns0:tt>schemaTest</ns0:tt>is present, the instance tests
                should be validated against a schema consisting only
                of the built-in components.</ns0:p>
        <ns0:p>The<ns0:tt>testGroup</ns0:tt>element has one attribute which is
                required:</ns0:p>
        <ns0:ul>
          <ns0:li><ns0:tt>name</ns0:tt>- an identifier for the<ns0:tt>testGroup</ns0:tt>which differs from the name of any other<ns0:tt>testGroup</ns0:tt>in the enclosing<ns0:tt>testSet</ns0:tt>.</ns0:li>
        </ns0:ul>
        <ns0:p>And one attribute which is optional:</ns0:p>
        <ns0:ul>
          <ns0:li>
            <ns0:p><ns0:tt>version</ns0:tt>- a list of version tokens, indicating
                    that the tests in the group are applicable to implementations
                    supporting<ns0:em>any</ns0:em>of the versions or features
                    or behaviors indicated.  Any processor or processor
                    configuration which supports<ns0:em>any</ns0:em>of the features
                    indicated should run the tests.  Processors which support<ns0:em>none</ns0:em>of them can skip the entire test set.
                    See the definition of the<ns0:a><ns0:tt>version-info</ns0:tt></ns0:a>type.</ns0:p>
            <ns0:p>Logically, all keywords appearing here should also appear
                    in the<ns0:tt>version</ns0:tt>attribute of the enclosing<ns0:tt>testSet</ns0:tt>, if it has one.</ns0:p>
          </ns0:li>
        </ns0:ul>
        <ns0:p>Four child elements may optionally be present:</ns0:p>
        <ns0:ul>
          <ns0:li>
            <ns0:p><ns0:tt>annotation</ns0:tt>- zero or more instances of
                    general documentation.</ns0:p>
          </ns0:li>
          <ns0:li>
            <ns0:p><ns0:tt>documentationReference</ns0:tt>- any number of
                    references to external documentation upon which the
                    test is based, e.g. links to relevant sections of the
                    Recommendation, to the Errata, etc.</ns0:p>
          </ns0:li>
          <ns0:li>
            <ns0:p><ns0:tt>schemaTest</ns0:tt>- at most on<ns0:tt>schemaTest</ns0:tt>element, containing any number of<ns0:tt>schemaDocument</ns0:tt>elements, each of which holds
                    information on a single schema document.</ns0:p>
            <ns0:p>When more than one schema document is present, a single
                    schema is constructed from the set (or from other
                    schemas via import).</ns0:p>
            <ns0:p>Note: XSD's rules for schema composition
                    mean that the order in which schema documents are
                    encountered may be significant.  When more than one
                    schema document is listed in the<ns0:tt>schemaTest</ns0:tt>element, the test should be run as if the schema
                    documents given were loaded one by one, in order.  For
                    most processors that will correspond to the result of
                    processing an otherwise empty schema document for an
                    otherwise unused namespace, containing one<ns0:tt>xsd:import</ns0:tt>element for each schema document
                    listed in the<ns0:tt>schemaTest</ns0:tt>, with the location
                    indicated, in a processing mode that involves
                    following the schema-location hints in import
                    statements.</ns0:p>
            <ns0:p>Note: the working group has made no
                    decision on whether the schema should be constructed
                    solely from the schema documents listed in the<ns0:tt>schemaTest</ns0:tt>element, or from those schema
                    documents plus the transitive closure of their
                    references to other schema documents.  Similarly, the
                    working group has not decided whether<ns0:tt>schemaLocation</ns0:tt>hints in the instance tests
                    should be honored or not.  It is therefore advisable
                    to draft test cases without dependencies on<ns0:tt>schemaLocation</ns0:tt>hints and the like.</ns0:p>
            <ns0:p>Note: work is pending on these issues of
                    schema composition.  When it's complete, this part o
                    the test suite schema may be expected to change.</ns0:p>
            <ns0:p>Schema documents may be omitted, for the purpose of
                    testing a processor's validation of an instance
                    containing only the built-in datatypes defined in the
                    Recommendation.</ns0:p>
          </ns0:li>
          <ns0:li>
            <ns0:p><ns0:tt>instanceTest</ns0:tt>- any number of elements, each
                    of which holds information on a single instance
                    document to be validated against the included
                    schema.</ns0:p>
          </ns0:li>
        </ns0:ul>
      </ns0:div>
    :ivar annotation:
    :ivar documentation_reference:
    :ivar schema_test:
    :ivar instance_test:
    :ivar name:
    :ivar version:
    :ivar attributes:
    """
    class Meta:
        name = "testGroup"
        namespace = "http://www.w3.org/XML/2004/xml-schema-test-suite/"

    annotation: List[Annotation] = field(
        default_factory=list,
        metadata=dict(
            name="annotation",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    documentation_reference: List[DocumentationReference] = field(
        default_factory=list,
        metadata=dict(
            name="documentationReference",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    schema_test: Optional[SchemaTest] = field(
        default=None,
        metadata=dict(
            name="schemaTest",
            type="Element"
        )
    )
    instance_test: List[InstanceTest] = field(
        default_factory=list,
        metadata=dict(
            name="instanceTest",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="name",
            type="Attribute",
            required=True
        )
    )
    version: Optional[str] = field(
        default=None,
        metadata=dict(
            name="version",
            type="Attribute"
        )
    )
    attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            name="attributes",
            type="AnyAttribute"
        )
    )


@dataclass
class TestSet:
    """<ns0:div>

        <ns0:p>The root element of a document describing a set of tests,
                normally from a single contributor.  A contributor may
                supply any number of<ns0:tt>testSet</ns0:tt>files.</ns0:p>
        <ns0:p>Note: In order to make it possible to browse the test
                suite in a browser, it is helpful if large test
                collections are broken up into several<ns0:tt>testSet</ns0:tt>documents of no more than a megabyte or so each.  If
                contributions have larger<ns0:tt>testSet</ns0:tt>documents, they
                may be broken up into smaller ones.</ns0:p>
        <ns0:p>The element has two attributes:</ns0:p>
        <ns0:ul>
          <ns0:li>
            <ns0:p><ns0:tt>contributor (required)</ns0:tt>- the name of the contributor of
                    this<ns0:tt>testSet</ns0:tt>.  May contain any string of characters;
                    intended for human readers.</ns0:p>
          </ns0:li>
          <ns0:li>
            <ns0:p><ns0:tt>name (required)</ns0:tt>- the name of this<ns0:tt>testSet</ns0:tt>,
                  which must be a name unique among the names of<ns0:tt>testSet</ns0:tt>elements within the enclosing<ns0:tt>testSuite</ns0:tt>.</ns0:p>
          </ns0:li>
          <ns0:li>
            <ns0:p><ns0:tt>version (optional)</ns0:tt>- a list of version tokens indicating
                    versions and features for which at least some tests in the
                    test set are applicable.</ns0:p>
            <ns0:p>Any processor or processor configuration which
                    supports<ns0:em>any</ns0:em>of the tokens given should run
                    the tests.  Processors which support none of the named
                    features can skip the entire test set without loss.
                    If no<ns0:tt>version</ns0:tt>value is given, or if the value
                    is the empty string, all processors should run the
                    tests.</ns0:p>
            <ns0:p>Logically, the tokens given in the<ns0:tt>version</ns0:tt>attribute should all also be included in the<ns0:tt>version</ns0:tt>attribute [if any] of any<ns0:tt>testSuite</ns0:tt>including this test set.  And
                    similarly the<ns0:tt>version</ns0:tt>attribute on a<ns0:tt>testSet</ns0:tt>element should include all the tokens
                    used on any<ns0:tt>testGroup</ns0:tt>,<ns0:tt>schemaTest</ns0:tt>,
                    or<ns0:tt>instanceTest</ns0:tt>in the test set, and no
                    others.  Otherwise processors may skip test sets they
                    ought to run.  This logical rule is not necessarily
                    enforced, however, by the schema for this
                    vocabulary.</ns0:p>
          </ns0:li>
        </ns0:ul>
        <ns0:p>Two child elements may optionally be present:</ns0:p>
        <ns0:ul>
          <ns0:li><ns0:tt>annotation</ns0:tt>- zero or more instances of general
                  documentation.</ns0:li>
          <ns0:li><ns0:tt>testGroup</ns0:tt>- a set of<ns0:tt>testGroup</ns0:tt>elements, each of which defines a group of closely
                  related tests.

                  No two<ns0:tt>testGroup</ns0:tt>elements in the same<ns0:tt>testSet</ns0:tt>may have the same name.</ns0:li>
        </ns0:ul>
      </ns0:div>
    :ivar annotation:
    :ivar test_group:
    :ivar contributor:
    :ivar name:
    :ivar version:
    :ivar attributes:
    """
    class Meta:
        name = "testSet"
        namespace = "http://www.w3.org/XML/2004/xml-schema-test-suite/"

    annotation: List[Annotation] = field(
        default_factory=list,
        metadata=dict(
            name="annotation",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    test_group: List[TestGroup] = field(
        default_factory=list,
        metadata=dict(
            name="testGroup",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    contributor: Optional[str] = field(
        default=None,
        metadata=dict(
            name="contributor",
            type="Attribute",
            required=True
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="name",
            type="Attribute",
            required=True
        )
    )
    version: Optional[str] = field(
        default=None,
        metadata=dict(
            name="version",
            type="Attribute"
        )
    )
    attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            name="attributes",
            type="AnyAttribute"
        )
    )
