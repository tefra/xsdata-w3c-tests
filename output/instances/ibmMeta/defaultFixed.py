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
                        "{http://www.w3.org/1999/xlink}href": "http://www.w3.org/TR/xmlschema11-1/#xsi_nil",
                    },
                    content=[
                        "Default/fixed values for xsi:type and xsi:nil",
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
                                "xsi:type must resolve to a type definition",
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
                    href="http://www.w3.org/TR/xmlschema11-1/#xsi_nil",
                    other_attributes={}
                ),
                DocumentationReference(
                    annotation=[],
                    type=TypeType.LOCATOR,
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-Misc-XSITypeMustResolve",
                    other_attributes={}
                ),
            ],
            schema_test=SchemaTest(
                annotation=[],
                schema_document=[
                    SchemaDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/valid/S2_7_1/s2_7_1v01.xsd",
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
                name="s2_7_1v01s",
                version=[],
                other_attributes={}
            ),
            instance_test=[
                InstanceTest(
                    annotation=[],
                    instance_document=InstanceDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/valid/S2_7_1/s2_7_1v01.xml",
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
                    name="s2_7_1v01i",
                    version=[],
                    other_attributes={}
                ),
            ],
            name="s2_7_1v01",
            version=[
                KnownToken.VALUE_1_1,
            ],
            other_attributes={}
        ),
        TestGroup(
            annotation=[
                Annotation(
                    appinfo_or_documentation=[
                        Documentation(
                            source=None,
                            lang=None,
                            other_attributes={},
                            content=[
                                "xsi:type must resolve to a type definition ",
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
                    href="http://www.w3.org/TR/xmlschema11-1/#xsi_type",
                    other_attributes={}
                ),
                DocumentationReference(
                    annotation=[],
                    type=TypeType.LOCATOR,
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-Misc-XSITypeMustResolve",
                    other_attributes={}
                ),
            ],
            schema_test=SchemaTest(
                annotation=[],
                schema_document=[
                    SchemaDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/instance_invalid/S2_7_1/s2_7_1ii01.xsd",
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
                name="s2_7_1ii01s",
                version=[],
                other_attributes={}
            ),
            instance_test=[
                InstanceTest(
                    annotation=[],
                    instance_document=InstanceDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/instance_invalid/S2_7_1/s2_7_1ii01.xml",
                        other_attributes={}
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.INVALID,
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
                    name="s2_7_1ii01i",
                    version=[],
                    other_attributes={}
                ),
            ],
            name="s2_7_1ii01",
            version=[
                KnownToken.VALUE_1_1,
            ],
            other_attributes={}
        ),
        TestGroup(
            annotation=[
                Annotation(
                    appinfo_or_documentation=[
                        Documentation(
                            source=None,
                            lang=None,
                            other_attributes={},
                            content=[
                                'When an xsi:type attribute appears on an element, and has a QName as its value,&#10; but the QName does not resolve to a known type definition, processors are now &#10; required to "fall back" to lax validation, using the declared {type definition}  &#10; of the governing element declaration as the governing type definition. ',
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
                    href="http://www.w3.org/TR/xmlschema11-1/#xsi_type",
                    other_attributes={}
                ),
                DocumentationReference(
                    annotation=[],
                    type=TypeType.LOCATOR,
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-Misc-XSITypeMustResolve",
                    other_attributes={}
                ),
            ],
            schema_test=SchemaTest(
                annotation=[],
                schema_document=[
                    SchemaDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/instance_invalid/S2_7_1/s2_7_1ii02.xsd",
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
                name="s2_7_1ii02s",
                version=[],
                other_attributes={}
            ),
            instance_test=[
                InstanceTest(
                    annotation=[],
                    instance_document=InstanceDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/instance_invalid/S2_7_1/s2_7_1ii02.xml",
                        other_attributes={}
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.INVALID,
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
                    name="s2_7_1ii02i",
                    version=[],
                    other_attributes={}
                ),
            ],
            name="s2_7_1ii02",
            version=[
                KnownToken.VALUE_1_1,
            ],
            other_attributes={}
        ),
        TestGroup(
            annotation=[
                Annotation(
                    appinfo_or_documentation=[
                        Documentation(
                            source=None,
                            lang=None,
                            other_attributes={},
                            content=[
                                "Structures introduces a mechanism for signaling that an element &#10;&#9;&#9;must be accepted as 'valid'  when it has no content despite a content type which &#10;&#9;&#9;does not require or even necessarily allow empty content. An element can be 'valid'  &#10;&#9;&#9;without content if it has the attribute xsi:nil  with the value true. An element &#10;&#9;&#9;so labeled must  be empty, but can carry attributes if permitted by the corresponding &#10;&#9;&#9;complex type. ",
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
                    href="http://www.w3.org/TR/xmlschema11-1/#xsi_nil",
                    other_attributes={}
                ),
                DocumentationReference(
                    annotation=[],
                    type=TypeType.LOCATOR,
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-Misc-XSIDefault",
                    other_attributes={}
                ),
            ],
            schema_test=SchemaTest(
                annotation=[],
                schema_document=[
                    SchemaDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/valid/S2_7_2/s2_7_2v01.xsd",
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
                name="s2_7_2v01s",
                version=[],
                other_attributes={}
            ),
            instance_test=[
                InstanceTest(
                    annotation=[],
                    instance_document=InstanceDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/valid/S2_7_2/s2_7_2v01.xml",
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
                    name="s2_7_2v01i",
                    version=[],
                    other_attributes={}
                ),
            ],
            name="s2_7_2v01",
            version=[],
            other_attributes={}
        ),
        TestGroup(
            annotation=[
                Annotation(
                    appinfo_or_documentation=[
                        Documentation(
                            source=None,
                            lang=None,
                            other_attributes={},
                            content=[
                                "default values for xsi:nil",
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
                    href="http://www.w3.org/TR/xmlschema11-1/#xsi_nil",
                    other_attributes={}
                ),
                DocumentationReference(
                    annotation=[],
                    type=TypeType.LOCATOR,
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-Misc-XSIDefault",
                    other_attributes={}
                ),
            ],
            schema_test=SchemaTest(
                annotation=[],
                schema_document=[
                    SchemaDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/instance_invalid/S2_7_2/s2_7_2ii01.xsd",
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
                name="s2_7_2ii01s",
                version=[],
                other_attributes={}
            ),
            instance_test=[
                InstanceTest(
                    annotation=[],
                    instance_document=InstanceDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/instance_invalid/S2_7_2/s2_7_2ii01.xml",
                        other_attributes={}
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.INVALID,
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
                    name="s2_7_2ii01i",
                    version=[],
                    other_attributes={}
                ),
            ],
            name="s2_7_2ii01",
            version=[
                KnownToken.VALUE_1_1,
            ],
            other_attributes={}
        ),
    ],
    contributor="IBM",
    name="DefaultFixed",
    version=[],
    other_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation": "http://www.w3.org/XML/2004/xml-schema-test-suite/ AnnotatedTSSchema.xsd",
    }
)