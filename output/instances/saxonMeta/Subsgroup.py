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
                                    text="Tests to show an element declaration can be in multiple substitution groups"
                                ),
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Description",
                                    text="Tests to show an element declaration can be in multiple substitution groups"
                                ),
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href="http://www.w3.org/TR/xmlschema11-1/#sec-cos-equiv-class"
                ),
                DocumentationReference(
                    href="../XSD1_1TestCategories.xml#xsd1_1-SubstitutionGroups-ElemInMoreThanOne"
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href="../saxonData/Subsgroup/subsgroup001.xsd"
                    ),
                ],
                expected=[
                    Expected(
                        validity=ExpectedOutcome.VALID
                    ),
                ],
                current=Current(
                    status=Status.ACCEPTED,
                    date=XmlDate(2008, 7, 31)
                ),
                name="subsgroup001.xsd"
            ),
            instance_test=[
                InstanceTest(
                    annotation=[
                        Annotation(
                            appinfo_or_documentation=[
                                Documentation(
                                    content=[
                                        "&#10;&#9;&#9;                Valid, element subsitutes for both abstract elements.&#10;&#9;&#9;            ",
                                    ]
                                ),
                            ]
                        ),
                    ],
                    instance_document=InstanceDocument(
                        href="../saxonData/Subsgroup/subsgroup001.v1.xml"
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.VALID
                        ),
                    ],
                    current=Current(
                        status=Status.ACCEPTED,
                        date=XmlDate(2008, 7, 31)
                    ),
                    name="subsgroup001.v1.xml"
                ),
                InstanceTest(
                    annotation=[
                        Annotation(
                            appinfo_or_documentation=[
                                Documentation(
                                    content=[
                                        "&#10;&#9;&#9;                Invalid, abstract element present in instance.&#10;&#9;&#9;            ",
                                    ]
                                ),
                            ]
                        ),
                    ],
                    instance_document=InstanceDocument(
                        href="../saxonData/Subsgroup/subsgroup001.n1.xml"
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.INVALID
                        ),
                    ],
                    current=Current(
                        status=Status.ACCEPTED,
                        date=XmlDate(2008, 7, 31)
                    ),
                    name="subsgroup001.n1.xml"
                ),
            ],
            name="subsgroup001",
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
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Title",
                                    text="Tests to show an element declaration can be in multiple substitution groups"
                                ),
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Description",
                                    text="Element substitutable for another in more than one way, both valid"
                                ),
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href="http://www.w3.org/TR/xmlschema11-1/#sec-cos-equiv-class"
                ),
                DocumentationReference(
                    href="../XSD1_1TestCategories.xml#xsd1_1-SubstitutionGroups-ElemInMoreThanOne"
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href="../saxonData/Subsgroup/subsgroup002.xsd"
                    ),
                ],
                expected=[
                    Expected(
                        validity=ExpectedOutcome.VALID
                    ),
                ],
                current=Current(
                    status=Status.ACCEPTED,
                    date=XmlDate(2010, 6, 10)
                ),
                name="subsgroup002.xsd"
            ),
            instance_test=[
                InstanceTest(
                    annotation=[
                        Annotation(
                            appinfo_or_documentation=[
                                Documentation(
                                    content=[
                                        "&#10;&#9;&#9;                Valid, element subsitutes for both abstract elements.&#10;&#9;&#9;            ",
                                    ]
                                ),
                            ]
                        ),
                    ],
                    instance_document=InstanceDocument(
                        href="../saxonData/Subsgroup/subsgroup001.v1.xml"
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.VALID
                        ),
                    ],
                    current=Current(
                        status=Status.ACCEPTED,
                        date=XmlDate(2010, 6, 10)
                    ),
                    name="subsgroup002.v1.xml"
                ),
                InstanceTest(
                    annotation=[
                        Annotation(
                            appinfo_or_documentation=[
                                Documentation(
                                    content=[
                                        "&#10;&#9;&#9;                Invalid, abstract element present in instance.&#10;&#9;&#9;            ",
                                    ]
                                ),
                            ]
                        ),
                    ],
                    instance_document=InstanceDocument(
                        href="../saxonData/Subsgroup/subsgroup001.n1.xml"
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.INVALID
                        ),
                    ],
                    current=Current(
                        status=Status.ACCEPTED,
                        date=XmlDate(2010, 6, 10)
                    ),
                    name="subsgroup002.n1.xml"
                ),
            ],
            name="subsgroup002",
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
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Title",
                                    text="Tests to show an a substitution group with declarations in different namespaces"
                                ),
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Description",
                                    text="Substitution group has an abstract owner in one namespace, two concrete&#10;                members in different namespaces. Should work with XSD 1.0 or 1.1. Posted as a problem&#10;                on StackOverflow ref 9495098 on 29 Feb 2012."
                                ),
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href="http://www.w3.org/TR/xmlschema11-1/#sec-cos-equiv-class"
                ),
                DocumentationReference(
                    href="../XSD1_1TestCategories.xml#xsd1_1-SubstitutionGroups-ElemInMoreThanOne"
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href="../saxonData/Subsgroup/subsgroup003a.xsd"
                    ),
                    SchemaDocument(
                        href="../saxonData/Subsgroup/subsgroup003b.xsd"
                    ),
                    SchemaDocument(
                        href="../saxonData/Subsgroup/subsgroup003c.xsd"
                    ),
                ],
                expected=[
                    Expected(
                        validity=ExpectedOutcome.VALID
                    ),
                ],
                current=Current(
                    status=Status.ACCEPTED,
                    date=XmlDate(2012, 2, 29)
                ),
                name="subsgroup003a.xsd"
            ),
            instance_test=[
                InstanceTest(
                    annotation=[
                        Annotation(
                            appinfo_or_documentation=[
                                Documentation(
                                    content=[
                                        "&#10;&#9;&#9;                Valid, both elements in the content are in the substitution group.&#10;&#9;&#9;            ",
                                    ]
                                ),
                            ]
                        ),
                    ],
                    instance_document=InstanceDocument(
                        href="../saxonData/Subsgroup/subsgroup003.xml"
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.VALID
                        ),
                    ],
                    current=Current(
                        status=Status.ACCEPTED,
                        date=XmlDate(2012, 2, 29)
                    ),
                    name="subsgroup003.v1.xml"
                ),
            ],
            name="subsgroup003"
        ),
        TestGroup(
            annotation=[
                Annotation(
                    appinfo_or_documentation=[
                        Documentation(
                            content=[
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Title",
                                    text="Substitution group causes failure of Element Declarations Consistent"
                                ),
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Description",
                                    text="Element in substitution group, fails &quot;element declarations consistent&quot; because of a conflict&#10;     between a locally declared element and the substitution group of a globally declared element.&#10;     This is actually a 1.0 test, but it's a condition that appears to be untested in the 1.0&#10;     test suite"
                                ),
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href="http://www.w3.org/TR/xmlschema11-1/#sec-cos-equiv-class"
                ),
                DocumentationReference(
                    href="../XSD1_1TestCategories.xml#xsd1_1-SubstitutionGroups"
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href="../saxonData/Subsgroup/subsgroup901.bad.xsd"
                    ),
                ],
                expected=[
                    Expected(
                        validity=ExpectedOutcome.INVALID
                    ),
                ],
                current=Current(
                    status=Status.ACCEPTED,
                    date=XmlDate(2008, 7, 31)
                ),
                name="subsgroup901.xsd"
            ),
            name="subsgroup901"
        ),
        TestGroup(
            annotation=[
                Annotation(
                    appinfo_or_documentation=[
                        Documentation(
                            content=[
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Title",
                                    text="Element in more than one substitution group causes UPA violation in xs:sequence group"
                                ),
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Description",
                                    text="The UPA violation occurs because the para element could be ascribed to either particle&#10;                in the content model of the 'back' element"
                                ),
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href="http://www.w3.org/TR/xmlschema11-1/#sec-cos-equiv-class"
                ),
                DocumentationReference(
                    href="../XSD1_1TestCategories.xml#xsd1_1-SubstitutionGroups-ElemInMoreThanOne"
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href="../saxonData/Subsgroup/subsgroup902.bad.xsd"
                    ),
                ],
                expected=[
                    Expected(
                        validity=ExpectedOutcome.INVALID
                    ),
                ],
                current=Current(
                    status=Status.ACCEPTED,
                    date=XmlDate(2010, 6, 10)
                ),
                name="subsgroup902.xsd"
            ),
            name="subsgroup902",
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
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Title",
                                    text="Element in more than one substitution group causes UPA violation in xs:all group"
                                ),
                                AnyElement(
                                    qname="{http://www.w3.org/XML/2004/xml-schema-test-suite/}Description",
                                    text="The UPA violation occurs because the para element could be ascribed to either particle&#10;                in the content model of the 'back' element"
                                ),
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href="http://www.w3.org/TR/xmlschema11-1/#sec-cos-equiv-class"
                ),
                DocumentationReference(
                    href="../XSD1_1TestCategories.xml#xsd1_1-SubstitutionGroups-ElemInMoreThanOne"
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href="../saxonData/Subsgroup/subsgroup903.bad.xsd"
                    ),
                ],
                expected=[
                    Expected(
                        validity=ExpectedOutcome.INVALID
                    ),
                ],
                current=Current(
                    status=Status.ACCEPTED,
                    date=XmlDate(2010, 6, 10)
                ),
                name="subsgroup903.xsd"
            ),
            name="subsgroup903",
            version=[
                KnownToken.VALUE_1_1,
            ]
        ),
    ],
    contributor="Saxonica",
    name="Subsgroup",
    version=[
        KnownToken.VALUE_1_1,
    ],
    other_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation": "http://www.w3.org/XML/2004/xml-schema-test-suite/ ../common/xsts.xsd",
    }
)
