from output.models.common.xsts_xsd.xlink import TypeType
from output.models.common.xsts_xsd.xsts import Annotation
from output.models.common.xsts_xsd.xsts import Current
from output.models.common.xsts_xsd.xsts import Documentation
from output.models.common.xsts_xsd.xsts import DocumentationReference
from output.models.common.xsts_xsd.xsts import Expected
from output.models.common.xsts_xsd.xsts import ExpectedOutcome
from output.models.common.xsts_xsd.xsts import InstanceDocument
from output.models.common.xsts_xsd.xsts import InstanceTest
from output.models.common.xsts_xsd.xsts import KnownToken
from output.models.common.xsts_xsd.xsts import SchemaDocument
from output.models.common.xsts_xsd.xsts import SchemaTest
from output.models.common.xsts_xsd.xsts import Status
from output.models.common.xsts_xsd.xsts import TestGroup
from output.models.common.xsts_xsd.xsts import TestSet
from xsdata.models.datatype import XmlDate


obj = TestSet(
    annotation=[
        Annotation(
            appinfo_or_documentation=[
                Documentation(
                    source=None,
                    lang=None,
                    other_attributes={
                        "{http://www.w3.org/1999/xlink}href": "http://www.w3.org/TR/xmlschema11-2/#time",
                    },
                    content=[
                        "time ",
                    ]
                ),
            ],
            other_attributes={}
        ),
    ],
    test_group=[
        TestGroup(
            annotation=[
                Annotation(
                    appinfo_or_documentation=[
                        Documentation(
                            source=None,
                            lang=None,
                            other_attributes={},
                            content=[
                                "&#10;&#9;&#9;&#9;&#9;1a: chameleon include on unqualified names in XPath expressions&#10;&#9;&#9;        1b: A calendar day with a very early timezone may be completely disjoint from a calendar day with a very late timezone.&#10;&#9;&#9;        1c: A time in a timezone may convert to a UTC time on a different day. &#10;&#9;&#9;        ",
                            ]
                        ),
                    ],
                    other_attributes={}
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    annotation=[],
                    type=TypeType.LOCATOR,
                    href="http://www.w3.org/TR/xmlschema11-2/#time",
                    other_attributes={}
                ),
                DocumentationReference(
                    annotation=[],
                    type=TypeType.LOCATOR,
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-DateTimeTypes-ExplicitTZFacet",
                    other_attributes={}
                ),
            ],
            schema_test=SchemaTest(
                annotation=[],
                schema_document=[
                    SchemaDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/valid/D3_3_9/d3_3_9v01.xsd",
                        other_attributes={}
                    ),
                ],
                expected=[
                    Expected(
                        validity=ExpectedOutcome.VALID,
                        version=[],
                        other_attributes={}
                    ),
                ],
                current=Current(
                    annotation=[],
                    status=Status.ACCEPTED,
                    date=XmlDate(2010, 12, 1),
                    bugzilla=None,
                    other_attributes={}
                ),
                prior=[],
                name="d3_3_9v01s",
                version=[],
                other_attributes={}
            ),
            instance_test=[
                InstanceTest(
                    annotation=[],
                    instance_document=InstanceDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/valid/D3_3_9/d3_3_9v01.xml",
                        other_attributes={}
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.VALID,
                            version=[],
                            other_attributes={}
                        ),
                    ],
                    current=Current(
                        annotation=[],
                        status=Status.ACCEPTED,
                        date=XmlDate(2010, 12, 1),
                        bugzilla=None,
                        other_attributes={}
                    ),
                    prior=[],
                    name="d3_3_9v01i",
                    version=[],
                    other_attributes={}
                ),
                InstanceTest(
                    annotation=[],
                    instance_document=InstanceDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/valid/D3_3_9/d3_3_9v01a.xml",
                        other_attributes={}
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.VALID,
                            version=[],
                            other_attributes={}
                        ),
                    ],
                    current=Current(
                        annotation=[],
                        status=Status.ACCEPTED,
                        date=XmlDate(2010, 12, 1),
                        bugzilla=None,
                        other_attributes={}
                    ),
                    prior=[],
                    name="d3_3_9v01ai",
                    version=[],
                    other_attributes={}
                ),
                InstanceTest(
                    annotation=[],
                    instance_document=InstanceDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/valid/D3_3_9/d3_3_9v01b.xml",
                        other_attributes={}
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.VALID,
                            version=[],
                            other_attributes={}
                        ),
                    ],
                    current=Current(
                        annotation=[],
                        status=Status.ACCEPTED,
                        date=XmlDate(2010, 12, 1),
                        bugzilla=None,
                        other_attributes={}
                    ),
                    prior=[],
                    name="d3_3_9v01bi",
                    version=[],
                    other_attributes={}
                ),
                InstanceTest(
                    annotation=[],
                    instance_document=InstanceDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/valid/D3_3_9/d3_3_9v01c.xml",
                        other_attributes={}
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.VALID,
                            version=[],
                            other_attributes={}
                        ),
                    ],
                    current=Current(
                        annotation=[],
                        status=Status.ACCEPTED,
                        date=XmlDate(2010, 12, 1),
                        bugzilla=None,
                        other_attributes={}
                    ),
                    prior=[],
                    name="d3_3_9v01ci",
                    version=[],
                    other_attributes={}
                ),
            ],
            name="d3_3_9v01",
            version=[
                KnownToken.VALUE_1_1,
            ],
            other_attributes={}
        ),
    ],
    contributor="IBM",
    name="time",
    version=[],
    other_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation": "http://www.w3.org/XML/2004/xml-schema-test-suite/ AnnotatedTSSchema.xsd",
    }
)
