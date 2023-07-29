from output.models.common.xsts_xsd.xsts import Annotation
from output.models.common.xsts_xsd.xsts import Current
from output.models.common.xsts_xsd.xsts import Documentation
from output.models.common.xsts_xsd.xsts import DocumentationReference
from output.models.common.xsts_xsd.xsts import Expected
from output.models.common.xsts_xsd.xsts import ExpectedOutcome
from output.models.common.xsts_xsd.xsts import InstanceDocument
from output.models.common.xsts_xsd.xsts import InstanceTest
from output.models.common.xsts_xsd.xsts import SchemaDocument
from output.models.common.xsts_xsd.xsts import SchemaTest
from output.models.common.xsts_xsd.xsts import Status
from output.models.common.xsts_xsd.xsts import TestGroup
from output.models.common.xsts_xsd.xsts import TestSet
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.models.datatype import XmlDate


obj = TestSet(
    test_group=[
        TestGroup(
            annotation=[
                Annotation(
                    appinfo_or_documentation=[
                        Documentation(
                            content=[
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Title",
                                    text="human-targeted  annotation for the schema itself (valid schema)"
                                ),
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Description",
                                    text="Annotations provide for human- and machine-targeted &#10;                             annotations of schema components.&#10;                              In the test the human-targeted annotation &#10;                             is provided for the schema itself."
                                ),
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href="http://www.w3.org/TR/2001/REC-xmlschema-1-20010502/#Schemas"
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href="../sunData/Schema/annotations/annotations00101m/annotations00101m1.xsd"
                    ),
                ],
                expected=[
                    Expected(
                        validity=ExpectedOutcome.VALID
                    ),
                ],
                current=Current(
                    status=Status.ACCEPTED,
                    date=XmlDate(2005, 6, 21)
                ),
                name="annotations00101m1"
            ),
            instance_test=[
                InstanceTest(
                    instance_document=InstanceDocument(
                        href="../sunData/Schema/annotations/annotations00101m/annotations00101m1_p.xml"
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.VALID
                        ),
                    ],
                    current=Current(
                        status=Status.ACCEPTED,
                        date=XmlDate(2005, 6, 21)
                    ),
                    name="Positive"
                ),
            ],
            name="annotations00101m1"
        ),
        TestGroup(
            annotation=[
                Annotation(
                    appinfo_or_documentation=[
                        Documentation(
                            content=[
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Title",
                                    text="human-targeted double annotation for the schema itself (valid schema)"
                                ),
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Description",
                                    text="Annotations provide for human- and machine-targeted &#10;                             annotations of schema components.&#10;                              In the test the human-targeted annotation &#10;                             is provided for the schema itself.&#10;                             The annotation is specified twice."
                                ),
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href="http://www.w3.org/TR/2001/REC-xmlschema-1-20010502/#Schemas"
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href="../sunData/Schema/annotations/annotations00101m/annotations00101m2.xsd"
                    ),
                ],
                expected=[
                    Expected(
                        validity=ExpectedOutcome.VALID
                    ),
                ],
                current=Current(
                    status=Status.ACCEPTED,
                    date=XmlDate(2005, 6, 21)
                ),
                name="annotations00101m2"
            ),
            instance_test=[
                InstanceTest(
                    instance_document=InstanceDocument(
                        href="../sunData/Schema/annotations/annotations00101m/annotations00101m2_p.xml"
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.VALID
                        ),
                    ],
                    current=Current(
                        status=Status.ACCEPTED,
                        date=XmlDate(2005, 6, 21)
                    ),
                    name="Positive"
                ),
            ],
            name="annotations00101m2"
        ),
        TestGroup(
            annotation=[
                Annotation(
                    appinfo_or_documentation=[
                        Documentation(
                            content=[
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Title",
                                    text="human-targeted placed at the end annotation for the schema itself (valid schema)"
                                ),
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Description",
                                    text="Annotations provide for human- and machine-targeted &#10;                             annotations of schema components.&#10;                              In the test the human-targeted annotation &#10;                             is provided for the schema itself.&#10;                             The annotation is placed at the end."
                                ),
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href="http://www.w3.org/TR/2001/REC-xmlschema-1-20010502/#Schemas"
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href="../sunData/Schema/annotations/annotations00101m/annotations00101m3.xsd"
                    ),
                ],
                expected=[
                    Expected(
                        validity=ExpectedOutcome.VALID
                    ),
                ],
                current=Current(
                    status=Status.ACCEPTED,
                    date=XmlDate(2005, 6, 21)
                ),
                name="annotations00101m3"
            ),
            instance_test=[
                InstanceTest(
                    instance_document=InstanceDocument(
                        href="../sunData/Schema/annotations/annotations00101m/annotations00101m3_p.xml"
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.VALID
                        ),
                    ],
                    current=Current(
                        status=Status.ACCEPTED,
                        date=XmlDate(2005, 6, 21)
                    ),
                    name="Positive"
                ),
            ],
            name="annotations00101m3"
        ),
        TestGroup(
            annotation=[
                Annotation(
                    appinfo_or_documentation=[
                        Documentation(
                            content=[
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Title",
                                    text="machine-targeted  annotation for the schema itself (valid schema)"
                                ),
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Description",
                                    text="Annotations provide for human- and machine-targeted &#10;                             annotations of schema components.&#10;                              In the test the machine-targeted annotation &#10;                             is provided for the schema itself."
                                ),
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href="http://www.w3.org/TR/2001/REC-xmlschema-1-20010502/#Schemas"
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href="../sunData/Schema/annotations/annotations00101m/annotations00101m4.xsd"
                    ),
                ],
                expected=[
                    Expected(
                        validity=ExpectedOutcome.VALID
                    ),
                ],
                current=Current(
                    status=Status.ACCEPTED,
                    date=XmlDate(2005, 6, 21)
                ),
                name="annotations00101m4"
            ),
            instance_test=[
                InstanceTest(
                    instance_document=InstanceDocument(
                        href="../sunData/Schema/annotations/annotations00101m/annotations00101m4_p.xml"
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.VALID
                        ),
                    ],
                    current=Current(
                        status=Status.ACCEPTED,
                        date=XmlDate(2005, 6, 21)
                    ),
                    name="Positive"
                ),
            ],
            name="annotations00101m4"
        ),
        TestGroup(
            annotation=[
                Annotation(
                    appinfo_or_documentation=[
                        Documentation(
                            content=[
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Title",
                                    text="machine-targeted double annotation for the schema itself (valid schema)"
                                ),
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Description",
                                    text="Annotations provide for human- and machine-targeted &#10;                             annotations of schema components.&#10;                              In the test the machine-targeted annotation &#10;                             is provided for the schema itself.&#10;                             The annotation is specified twice."
                                ),
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href="http://www.w3.org/TR/2001/REC-xmlschema-1-20010502/#Schemas"
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href="../sunData/Schema/annotations/annotations00101m/annotations00101m5.xsd"
                    ),
                ],
                expected=[
                    Expected(
                        validity=ExpectedOutcome.VALID
                    ),
                ],
                current=Current(
                    status=Status.ACCEPTED,
                    date=XmlDate(2005, 6, 21)
                ),
                name="annotations00101m5"
            ),
            instance_test=[
                InstanceTest(
                    instance_document=InstanceDocument(
                        href="../sunData/Schema/annotations/annotations00101m/annotations00101m5_p.xml"
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.VALID
                        ),
                    ],
                    current=Current(
                        status=Status.ACCEPTED,
                        date=XmlDate(2005, 6, 21)
                    ),
                    name="Positive"
                ),
            ],
            name="annotations00101m5"
        ),
        TestGroup(
            annotation=[
                Annotation(
                    appinfo_or_documentation=[
                        Documentation(
                            content=[
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Title",
                                    text="machine-targeted placed at the end annotation for the schema itself (valid schema)"
                                ),
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Description",
                                    text="Annotations provide for human- and machine-targeted &#10;                             annotations of schema components.&#10;                              In the test the machine-targeted annotation &#10;                             is provided for the schema itself.&#10;                             The annotation is placed at the end."
                                ),
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href="http://www.w3.org/TR/2001/REC-xmlschema-1-20010502/#Schemas"
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href="../sunData/Schema/annotations/annotations00101m/annotations00101m6.xsd"
                    ),
                ],
                expected=[
                    Expected(
                        validity=ExpectedOutcome.VALID
                    ),
                ],
                current=Current(
                    status=Status.ACCEPTED,
                    date=XmlDate(2005, 6, 21)
                ),
                name="annotations00101m6"
            ),
            instance_test=[
                InstanceTest(
                    instance_document=InstanceDocument(
                        href="../sunData/Schema/annotations/annotations00101m/annotations00101m6_p.xml"
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.VALID
                        ),
                    ],
                    current=Current(
                        status=Status.ACCEPTED,
                        date=XmlDate(2005, 6, 21)
                    ),
                    name="Positive"
                ),
            ],
            name="annotations00101m6"
        ),
    ],
    contributor="SUN",
    name="Schema",
    other_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation": "http://www.w3.org/XML/2004/xml-schema-test-suite/ ../common/xsts.xsd",
    }
)
