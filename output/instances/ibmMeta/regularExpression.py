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
                        "{http://www.w3.org/1999/xlink}href": "http://www.w3.org/TR/xmlschema11-2/#regexs",
                    },
                    content=[
                        "substitutionGroup ",
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
                                "use of hyphens within square brackets in regular expressions [a-c] ",
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
                    href="http://www.w3.org/TR/xmlschema11-2/#regexs",
                    other_attributes={}
                ),
                DocumentationReference(
                    annotation=[],
                    type=TypeType.LOCATOR,
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-Misc-HyphensAndBracketsInRegex",
                    other_attributes={}
                ),
            ],
            schema_test=SchemaTest(
                annotation=[],
                schema_document=[
                    SchemaDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/valid/D6_G/d6_gv01.xsd",
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
                name="d6_gv01s",
                version=[],
                other_attributes={}
            ),
            instance_test=[
                InstanceTest(
                    annotation=[],
                    instance_document=InstanceDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/valid/D6_G/d6_gv01.xml",
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
                    name="d6_gv01i",
                    version=[],
                    other_attributes={}
                ),
            ],
            name="d6_gv01",
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
                                "use of hyphens within square brackets in regular expressions [abc-[c]] ",
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
                    href="http://www.w3.org/TR/xmlschema11-2/#regexs",
                    other_attributes={}
                ),
                DocumentationReference(
                    annotation=[],
                    type=TypeType.LOCATOR,
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-Misc-HyphensAndBracketsInRegex",
                    other_attributes={}
                ),
            ],
            schema_test=SchemaTest(
                annotation=[],
                schema_document=[
                    SchemaDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/valid/D6_G/d6_gv02.xsd",
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
                name="d6_gv02s",
                version=[],
                other_attributes={}
            ),
            instance_test=[
                InstanceTest(
                    annotation=[],
                    instance_document=InstanceDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/valid/D6_G/d6_gv02.xml",
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
                    name="d6_gv02i",
                    version=[],
                    other_attributes={}
                ),
            ],
            name="d6_gv02",
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
                                "use of hyphens within square brackets in regular expressions [-abc] ",
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
                    href="http://www.w3.org/TR/xmlschema11-2/#regexs",
                    other_attributes={}
                ),
                DocumentationReference(
                    annotation=[],
                    type=TypeType.LOCATOR,
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-Misc-HyphensAndBracketsInRegex",
                    other_attributes={}
                ),
            ],
            schema_test=SchemaTest(
                annotation=[],
                schema_document=[
                    SchemaDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/valid/D6_G/d6_gv03.xsd",
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
                name="d6_gv03s",
                version=[],
                other_attributes={}
            ),
            instance_test=[
                InstanceTest(
                    annotation=[],
                    instance_document=InstanceDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/valid/D6_G/d6_gv03.xml",
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
                    name="d6_gv03i",
                    version=[],
                    other_attributes={}
                ),
            ],
            name="d6_gv03",
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
                                "use of hyphens within square brackets in regular expressions [bc-] ",
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
                    href="http://www.w3.org/TR/xmlschema11-2/#regexs",
                    other_attributes={}
                ),
                DocumentationReference(
                    annotation=[],
                    type=TypeType.LOCATOR,
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-Misc-HyphensAndBracketsInRegex",
                    other_attributes={}
                ),
            ],
            schema_test=SchemaTest(
                annotation=[],
                schema_document=[
                    SchemaDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/valid/D6_G/d6_gv04.xsd",
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
                name="d6_gv04s",
                version=[],
                other_attributes={}
            ),
            instance_test=[
                InstanceTest(
                    annotation=[],
                    instance_document=InstanceDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/valid/D6_G/d6_gv04.xml",
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
                    name="d6_gv04i",
                    version=[],
                    other_attributes={}
                ),
            ],
            name="d6_gv04",
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
                                "invalid instance use of hyphens within square brackets in regular expressions [a-c] ",
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
                    href="http://www.w3.org/TR/xmlschema11-2/#regexs",
                    other_attributes={}
                ),
                DocumentationReference(
                    annotation=[],
                    type=TypeType.LOCATOR,
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-Misc-HyphensAndBracketsInRegex",
                    other_attributes={}
                ),
            ],
            schema_test=SchemaTest(
                annotation=[],
                schema_document=[
                    SchemaDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/instance_invalid/D6_G/d6_gii01.xsd",
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
                name="d6_gii01s",
                version=[],
                other_attributes={}
            ),
            instance_test=[
                InstanceTest(
                    annotation=[],
                    instance_document=InstanceDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/instance_invalid/D6_G/d6_gii01.xml",
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
                    name="d6_gii01i",
                    version=[],
                    other_attributes={}
                ),
            ],
            name="d6_gii01",
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
                                "invalid instance use of hyphens within square brackets in regular expressions [abc-[c]] ",
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
                    href="http://www.w3.org/TR/xmlschema11-2/#regexs",
                    other_attributes={}
                ),
                DocumentationReference(
                    annotation=[],
                    type=TypeType.LOCATOR,
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-Misc-HyphensAndBracketsInRegex",
                    other_attributes={}
                ),
            ],
            schema_test=SchemaTest(
                annotation=[],
                schema_document=[
                    SchemaDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/instance_invalid/D6_G/d6_gii02.xsd",
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
                name="d6_gii02s",
                version=[],
                other_attributes={}
            ),
            instance_test=[
                InstanceTest(
                    annotation=[],
                    instance_document=InstanceDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/instance_invalid/D6_G/d6_gii02.xml",
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
                    name="d6_gii02i",
                    version=[],
                    other_attributes={}
                ),
            ],
            name="d6_gii02",
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
                                " invalid instance use of hyphens within square brackets in regular expressions [-abc] ",
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
                    href="http://www.w3.org/TR/xmlschema11-2/#regexs",
                    other_attributes={}
                ),
                DocumentationReference(
                    annotation=[],
                    type=TypeType.LOCATOR,
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-Misc-HyphensAndBracketsInRegex",
                    other_attributes={}
                ),
            ],
            schema_test=SchemaTest(
                annotation=[],
                schema_document=[
                    SchemaDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/instance_invalid/D6_G/d6_gii03.xsd",
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
                name="d6_gii03s",
                version=[],
                other_attributes={}
            ),
            instance_test=[
                InstanceTest(
                    annotation=[],
                    instance_document=InstanceDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/instance_invalid/D6_G/d6_gii03.xml",
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
                    name="d6_gii03i",
                    version=[],
                    other_attributes={}
                ),
            ],
            name="d6_gii03",
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
                                "invalid instance use of hyphens within square brackets in regular expressions [bc-] ",
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
                    href="http://www.w3.org/TR/xmlschema11-2/#regexs",
                    other_attributes={}
                ),
                DocumentationReference(
                    annotation=[],
                    type=TypeType.LOCATOR,
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-Misc-HyphensAndBracketsInRegex",
                    other_attributes={}
                ),
            ],
            schema_test=SchemaTest(
                annotation=[],
                schema_document=[
                    SchemaDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/instance_invalid/D6_G/d6_gii04.xsd",
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
                name="d6_gii04s",
                version=[],
                other_attributes={}
            ),
            instance_test=[
                InstanceTest(
                    annotation=[],
                    instance_document=InstanceDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/instance_invalid/D6_G/d6_gii04.xml",
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
                    name="d6_gii04i",
                    version=[],
                    other_attributes={}
                ),
            ],
            name="d6_gii04",
            version=[
                KnownToken.VALUE_1_1,
            ],
            other_attributes={}
        ),
    ],
    contributor="IBM",
    name="RegularExpression",
    version=[],
    other_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation": "http://www.w3.org/XML/2004/xml-schema-test-suite/ AnnotatedTSSchema.xsd",
    }
)