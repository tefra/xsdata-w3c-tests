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
                                    text="Simple use of targetNamespace on a local element declaration"
                                ),
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Description",
                                    text="Simple use of targetNamespace on a local element declaration"
                                ),
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href="http://www.w3.org/TR/2006/WD-xmlschema11-1-20060831/"
                ),
                DocumentationReference(
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-NewLocalDecl-TargNSOnElemDecl"
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href="../saxonData/TargetNS/target001.xsd"
                    ),
                ],
                expected=[
                    Expected(
                        validity=ExpectedOutcome.VALID
                    ),
                ],
                current=Current(
                    status=Status.ACCEPTED,
                    date=XmlDate(2008, 2, 18)
                ),
                name="target001.xsd"
            ),
            instance_test=[
                InstanceTest(
                    annotation=[
                        Annotation(
                            appinfo_or_documentation=[
                                Documentation(
                                    content=[
                                        "&#10;&#9;&#9;                Valid, satisfies the schema.&#10;&#9;&#9;            ",
                                    ]
                                ),
                            ]
                        ),
                    ],
                    instance_document=InstanceDocument(
                        href="../saxonData/TargetNS/target001.v1.xml"
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.VALID
                        ),
                    ],
                    current=Current(
                        status=Status.ACCEPTED,
                        date=XmlDate(2008, 2, 18)
                    ),
                    name="target001.v1.xml"
                ),
                InstanceTest(
                    annotation=[
                        Annotation(
                            appinfo_or_documentation=[
                                Documentation(
                                    content=[
                                        "&#10;&#9;&#9;                Invalid, child element is in wrong namespace.&#10;&#9;&#9;            ",
                                    ]
                                ),
                            ]
                        ),
                    ],
                    instance_document=InstanceDocument(
                        href="../saxonData/TargetNS/target001.n1.xml"
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.INVALID
                        ),
                    ],
                    current=Current(
                        status=Status.ACCEPTED,
                        date=XmlDate(2008, 2, 18)
                    ),
                    name="target001.n1.xml"
                ),
            ],
            name="target001"
        ),
        TestGroup(
            annotation=[
                Annotation(
                    appinfo_or_documentation=[
                        Documentation(
                            content=[
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Title",
                                    text="Invalid use of targetNamespace on a local element declaration"
                                ),
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Description",
                                    text="Invalid because not part of an xs:restriction"
                                ),
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href="http://www.w3.org/TR/2006/WD-xmlschema11-1-20060831/"
                ),
                DocumentationReference(
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-NewLocalDecl-TargNSOnElemDecl"
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href="../saxonData/TargetNS/target002.n.xsd"
                    ),
                ],
                expected=[
                    Expected(
                        validity=ExpectedOutcome.INVALID
                    ),
                ],
                current=Current(
                    status=Status.ACCEPTED,
                    date=XmlDate(2008, 2, 18)
                ),
                name="target002.xsd"
            ),
            name="target002"
        ),
        TestGroup(
            annotation=[
                Annotation(
                    appinfo_or_documentation=[
                        Documentation(
                            content=[
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Title",
                                    text="Simple use of targetNamespace on a local attribute declaration"
                                ),
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Description",
                                    text="Simple use of targetNamespace on a local attribute declaration"
                                ),
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}documentationReference",
                                    text="",
                                    attributes={
                                        "{http://www.w3.org/1999/xlink}href": "../common/XSD1_1TestCategories.xml#xsd1_1-NewLocalDecl-TargNSOnAttrDecl",
                                    }
                                ),
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href="http://www.w3.org/TR/2006/WD-xmlschema11-1-20060831/"
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href="../saxonData/TargetNS/target003.xsd"
                    ),
                ],
                expected=[
                    Expected(
                        validity=ExpectedOutcome.VALID
                    ),
                ],
                current=Current(
                    status=Status.ACCEPTED,
                    date=XmlDate(2008, 2, 18)
                ),
                name="target003.xsd"
            ),
            instance_test=[
                InstanceTest(
                    annotation=[
                        Annotation(
                            appinfo_or_documentation=[
                                Documentation(
                                    content=[
                                        "&#10;&#9;&#9;                Valid, satisfies the schema.&#10;&#9;&#9;            ",
                                    ]
                                ),
                            ]
                        ),
                    ],
                    instance_document=InstanceDocument(
                        href="../saxonData/TargetNS/target003.v1.xml"
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.VALID
                        ),
                    ],
                    current=Current(
                        status=Status.ACCEPTED,
                        date=XmlDate(2008, 2, 18)
                    ),
                    name="target003.v1.xml"
                ),
                InstanceTest(
                    annotation=[
                        Annotation(
                            appinfo_or_documentation=[
                                Documentation(
                                    content=[
                                        "&#10;&#9;&#9;                Invalid, attribute is in wrong namespace.&#10;&#9;&#9;            ",
                                    ]
                                ),
                            ]
                        ),
                    ],
                    instance_document=InstanceDocument(
                        href="../saxonData/TargetNS/target003.n1.xml"
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.INVALID
                        ),
                    ],
                    current=Current(
                        status=Status.ACCEPTED,
                        date=XmlDate(2008, 2, 18)
                    ),
                    name="target003.n1.xml"
                ),
                InstanceTest(
                    annotation=[
                        Annotation(
                            appinfo_or_documentation=[
                                Documentation(
                                    content=[
                                        "&#10;&#9;&#9;                Invalid, attribute is in wrong namespace.&#10;&#9;&#9;            ",
                                    ]
                                ),
                            ]
                        ),
                    ],
                    instance_document=InstanceDocument(
                        href="../saxonData/TargetNS/target003.n2.xml"
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.INVALID
                        ),
                    ],
                    current=Current(
                        status=Status.ACCEPTED,
                        date=XmlDate(2008, 2, 18)
                    ),
                    name="target003.n2.xml"
                ),
            ],
            name="target003"
        ),
        TestGroup(
            annotation=[
                Annotation(
                    appinfo_or_documentation=[
                        Documentation(
                            content=[
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Title",
                                    text="Invalid use of targetNamespace on a local attribute declaration"
                                ),
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Description",
                                    text="Invalid because not part of an xs:restriction"
                                ),
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href="http://www.w3.org/TR/2006/WD-xmlschema11-1-20060831/"
                ),
                DocumentationReference(
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-NewLocalDecl-TargNSOnAttrDecl"
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href="../saxonData/TargetNS/target004.n.xsd"
                    ),
                ],
                expected=[
                    Expected(
                        validity=ExpectedOutcome.INVALID
                    ),
                ],
                current=Current(
                    status=Status.ACCEPTED,
                    date=XmlDate(2008, 2, 18)
                ),
                name="target004.xsd"
            ),
            name="target004"
        ),
        TestGroup(
            annotation=[
                Annotation(
                    appinfo_or_documentation=[
                        Documentation(
                            content=[
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Title",
                                    text="Invalid xs:import - targetNamespace does not match"
                                ),
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Description",
                                    text="Should report an error"
                                ),
                            ]
                        ),
                    ]
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href="../saxonData/TargetNS/target007.xsd"
                    ),
                ],
                expected=[
                    Expected(
                        validity=ExpectedOutcome.INVALID
                    ),
                ],
                current=Current(
                    status=Status.ACCEPTED,
                    date=XmlDate(2018, 10, 1)
                ),
                name="target007.xsd"
            ),
            name="target007",
            version=[
                KnownToken.VALUE_1_1,
            ]
        ),
    ],
    contributor="Saxonica",
    name="TargetNS",
    version=[
        KnownToken.VALUE_1_1,
    ],
    other_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation": "http://www.w3.org/XML/2004/xml-schema-test-suite/ AnnotatedTSSchema.xsd",
    }
)
