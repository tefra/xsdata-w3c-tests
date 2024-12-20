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
    test_group=[
        TestGroup(
            annotation=[
                Annotation(
                    appinfo_or_documentation=[
                        Documentation(
                            content=[
                                '\n\t\t    Demonstrates XML Schema 1.1 type-alternatives.\n\t\t ',
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href='http://www.w3.org/TR/xmlschema11-1/'
                ),
                DocumentationReference(
                    href='../common/XSD1_1TestCategories.xml#xsd1_1-CTA'
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href='../ibmData/mixed/type-alternatives/test1.xsd'
                    ),
                ],
                expected=[
                    Expected(
                        validity=ExpectedOutcome.VALID
                    ),
                ],
                current=Current(
                    status=Status.ACCEPTED,
                    date=XmlDate(2010, 10, 12)
                ),
                name='typeAlternatives_001_1'
            ),
            instance_test=[
                InstanceTest(
                    instance_document=InstanceDocument(
                        href='../ibmData/mixed/type-alternatives/test1.xml'
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.VALID
                        ),
                    ],
                    current=Current(
                        status=Status.ACCEPTED,
                        date=XmlDate(2010, 10, 12)
                    ),
                    name='typeAlternatives_001_2'
                ),
            ],
            name='typeAlternatives_001',
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
                                '\n\t\t    Demonstrates XML Schema 1.1 type-alternatives.\n\t\t ',
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href='http://www.w3.org/TR/xmlschema11-1/'
                ),
                DocumentationReference(
                    href='../common/XSD1_1TestCategories.xml#xsd1_1-CTA'
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href='../ibmData/mixed/type-alternatives/test2.xsd'
                    ),
                ],
                expected=[
                    Expected(
                        validity=ExpectedOutcome.VALID
                    ),
                ],
                current=Current(
                    status=Status.ACCEPTED,
                    date=XmlDate(2010, 10, 12)
                ),
                name='typeAlternatives_002_1'
            ),
            instance_test=[
                InstanceTest(
                    instance_document=InstanceDocument(
                        href='../ibmData/mixed/type-alternatives/test2.xml'
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.VALID
                        ),
                    ],
                    current=Current(
                        status=Status.ACCEPTED,
                        date=XmlDate(2010, 10, 12)
                    ),
                    name='typeAlternatives_002_2'
                ),
            ],
            name='typeAlternatives_002',
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
                                "\n\t\t    Demonstrates XML Schema 1.1 type-alternatives. In this example, schema type definition's are provided\n\t\t\tas children of xs:alternative instructions.\n\t\t ",
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href='http://www.w3.org/TR/xmlschema11-1/'
                ),
                DocumentationReference(
                    href='../common/XSD1_1TestCategories.xml#xsd1_1-CTA'
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href='../ibmData/mixed/type-alternatives/test2_1.xsd'
                    ),
                ],
                expected=[
                    Expected(
                        validity=ExpectedOutcome.VALID
                    ),
                ],
                current=Current(
                    status=Status.ACCEPTED,
                    date=XmlDate(2010, 10, 12)
                ),
                name='typeAlternatives_003_1'
            ),
            instance_test=[
                InstanceTest(
                    instance_document=InstanceDocument(
                        href='../ibmData/mixed/type-alternatives/test2.xml'
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.VALID
                        ),
                    ],
                    current=Current(
                        status=Status.ACCEPTED,
                        date=XmlDate(2010, 10, 12)
                    ),
                    name='typeAlternatives_003_2'
                ),
            ],
            name='typeAlternatives_003',
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
                                '\n\t\t    Demonstrates XML Schema 1.1 type-alternatives. Using inheritable attributes and assertions along\n\t\t\twith type-alternatives.\n\t\t ',
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href='http://www.w3.org/TR/xmlschema11-1/'
                ),
                DocumentationReference(
                    href='../common/XSD1_1TestCategories.xml#xsd1_1-CTA'
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href='../ibmData/mixed/type-alternatives/test3.xsd'
                    ),
                ],
                expected=[
                    Expected(
                        validity=ExpectedOutcome.VALID
                    ),
                ],
                current=Current(
                    status=Status.ACCEPTED,
                    date=XmlDate(2010, 10, 12)
                ),
                name='typeAlternatives_004_1'
            ),
            instance_test=[
                InstanceTest(
                    instance_document=InstanceDocument(
                        href='../ibmData/mixed/type-alternatives/test3_1.xml'
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.VALID
                        ),
                    ],
                    current=Current(
                        status=Status.ACCEPTED,
                        date=XmlDate(2010, 10, 12)
                    ),
                    name='typeAlternatives_004_2'
                ),
                InstanceTest(
                    instance_document=InstanceDocument(
                        href='../ibmData/mixed/type-alternatives/test3_2.xml'
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.INVALID
                        ),
                    ],
                    current=Current(
                        status=Status.ACCEPTED,
                        date=XmlDate(2010, 10, 12)
                    ),
                    name='typeAlternatives_004_3'
                ),
            ],
            name='typeAlternatives_004',
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
                                '\n\t\t    Demonstrates XML Schema 1.1 type-alternatives. Using inheritable attributes in this example.\n\t\t ',
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href='http://www.w3.org/TR/xmlschema11-1/'
                ),
                DocumentationReference(
                    href='../common/XSD1_1TestCategories.xml#xsd1_1-CTA'
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href='../ibmData/mixed/type-alternatives/test4.xsd'
                    ),
                ],
                expected=[
                    Expected(
                        validity=ExpectedOutcome.VALID
                    ),
                ],
                current=Current(
                    status=Status.ACCEPTED,
                    date=XmlDate(2010, 10, 12)
                ),
                name='typeAlternatives_005_1'
            ),
            instance_test=[
                InstanceTest(
                    instance_document=InstanceDocument(
                        href='../ibmData/mixed/type-alternatives/test4_1.xml'
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.VALID
                        ),
                    ],
                    current=Current(
                        status=Status.ACCEPTED,
                        date=XmlDate(2010, 10, 12)
                    ),
                    name='typeAlternatives_005_2'
                ),
                InstanceTest(
                    instance_document=InstanceDocument(
                        href='../ibmData/mixed/type-alternatives/test4_2.xml'
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.INVALID
                        ),
                    ],
                    current=Current(
                        status=Status.ACCEPTED,
                        date=XmlDate(2010, 10, 12)
                    ),
                    name='typeAlternatives_005_3'
                ),
            ],
            name='typeAlternatives_005',
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
                                '\n\t\t    Demonstrates XML Schema 1.1 type-alternatives.\n\t\t ',
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href='http://www.w3.org/TR/xmlschema11-1/'
                ),
                DocumentationReference(
                    href='../common/XSD1_1TestCategories.xml#xsd1_1-CTA'
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href='../ibmData/mixed/type-alternatives/test5.xsd'
                    ),
                ],
                expected=[
                    Expected(
                        validity=ExpectedOutcome.VALID
                    ),
                ],
                current=Current(
                    status=Status.ACCEPTED,
                    date=XmlDate(2010, 10, 12)
                ),
                name='typeAlternatives_006_1'
            ),
            instance_test=[
                InstanceTest(
                    instance_document=InstanceDocument(
                        href='../ibmData/mixed/type-alternatives/test5_1.xml'
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.VALID
                        ),
                    ],
                    current=Current(
                        status=Status.ACCEPTED,
                        date=XmlDate(2010, 10, 12)
                    ),
                    name='typeAlternatives_006_2'
                ),
                InstanceTest(
                    instance_document=InstanceDocument(
                        href='../ibmData/mixed/type-alternatives/test5_2.xml'
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.VALID
                        ),
                    ],
                    current=Current(
                        status=Status.ACCEPTED,
                        date=XmlDate(2010, 10, 12)
                    ),
                    name='typeAlternatives_006_3'
                ),
            ],
            name='typeAlternatives_006',
            version=[
                KnownToken.VALUE_1_1,
            ]
        ),
    ],
    contributor='IBM',
    name='CTA',
    version=[
        KnownToken.VALUE_1_1,
    ],
    other_attributes={
        '{http://www.w3.org/2001/XMLSchema-instance}schemaLocation': 'http://www.w3.org/XML/2004/xml-schema-test-suite/ ../common/xsts.xsd',
    }
)
