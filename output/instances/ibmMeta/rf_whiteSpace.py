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
                    other_attributes={
                        "{http://www.w3.org/1999/xlink}href": "http://www.w3.org/TR/xmlschema11-2/#rf-whiteSpace",
                    },
                    content=[
                        "collapse test for string.",
                    ]
                ),
            ]
        ),
    ],
    test_group=[
        TestGroup(
            annotation=[
                Annotation(
                    appinfo_or_documentation=[
                        Documentation(
                            content=[
                                "when the value is collapse, literals consisting solely of whitespace characters are reduced to the empty string.",
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href="http://www.w3.org/TR/xmlschema11-2/#rf-whiteSpace"
                ),
                DocumentationReference(
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-Misc-CollapseEmptyString"
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href="../ibmData/valid/D4_3_6/d4_3_6v01.xsd"
                    ),
                ],
                expected=[
                    Expected(
                        validity=ExpectedOutcome.VALID
                    ),
                ],
                current=Current(
                    status=Status.ACCEPTED,
                    date=XmlDate(2010, 12, 1)
                ),
                name="d4_3_6v01s"
            ),
            instance_test=[
                InstanceTest(
                    instance_document=InstanceDocument(
                        href="../ibmData/valid/D4_3_6/d4_3_6v01.xml"
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.VALID
                        ),
                    ],
                    current=Current(
                        status=Status.ACCEPTED,
                        date=XmlDate(2010, 12, 1)
                    ),
                    name="d4_3_6v01i"
                ),
            ],
            name="d4_3_6v01",
            version=[
                KnownToken.VALUE_1_1,
            ]
        ),
        TestGroup(
            annotation=[
                Annotation(
                    appinfo_or_documentation=[
                        Documentation(
                            content=[
                                "when the value is collapse, literals consisting solely of whitespace characters are reduced to the empty string.",
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href="http://www.w3.org/TR/xmlschema11-2/#rf-whiteSpace"
                ),
                DocumentationReference(
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-Misc-CollapseEmptyString"
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href="../ibmData/instance_invalid/D4_3_6/d4_3_6ii01.xsd"
                    ),
                ],
                expected=[
                    Expected(
                        validity=ExpectedOutcome.VALID
                    ),
                ],
                current=Current(
                    status=Status.ACCEPTED,
                    date=XmlDate(2010, 12, 1)
                ),
                name="d4_3_6ii01s"
            ),
            instance_test=[
                InstanceTest(
                    instance_document=InstanceDocument(
                        href="../ibmData/instance_invalid/D4_3_6/d4_3_6ii01.xml"
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.INVALID
                        ),
                    ],
                    current=Current(
                        status=Status.ACCEPTED,
                        date=XmlDate(2010, 12, 1)
                    ),
                    name="d4_3_6ii01i"
                ),
            ],
            name="d4_3_6ii01",
            version=[
                KnownToken.VALUE_1_1,
            ]
        ),
    ],
    contributor="IBM",
    name="rf-whiteSpace",
    other_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation": "http://www.w3.org/XML/2004/xml-schema-test-suite/ ../common/xsts.xsd",
    }
)
