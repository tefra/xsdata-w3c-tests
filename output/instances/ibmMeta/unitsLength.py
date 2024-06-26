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
                        '{http://www.w3.org/1999/xlink}href': 'http://www.w3.org/TR/xmlschema11-2/#dt-list',
                    },
                    content=[
                        ' test Units of length for list datatype\n\t      ',
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
                                ' test Units of length for hexBinary datatype.  ',
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href='http://www.w3.org/TR/xmlschema11-2/#hexBinary'
                ),
                DocumentationReference(
                    href='../common/XSD1_1TestCategories.xml#xsd1_1-Misc-ListBounds'
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href='../ibmData/valid/D3_3_16/d3_3_16v01.xsd'
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
                name='d3_3_16v01s'
            ),
            instance_test=[
                InstanceTest(
                    instance_document=InstanceDocument(
                        href='../ibmData/valid/D3_3_16/d3_3_16v01.xml'
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
                    name='d3_3_16v01i'
                ),
            ],
            name='d3_3_16v01'
        ),
        TestGroup(
            annotation=[
                Annotation(
                    appinfo_or_documentation=[
                        Documentation(
                            content=[
                                ' test hexBinary datatype   ',
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href='http://www.w3.org/TR/xmlschema11-2/#hexBinary'
                ),
                DocumentationReference(
                    href='../common/XSD1_1TestCategories.xml#xsd1_1-Misc-ListBounds'
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href='../ibmData/instance_invalid/D3_3_16/d3_3_16ii01.xsd'
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
                name='d3_3_16ii01s'
            ),
            instance_test=[
                InstanceTest(
                    instance_document=InstanceDocument(
                        href='../ibmData/instance_invalid/D3_3_16/d3_3_16ii01.xml'
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
                    name='d3_3_16ii01i'
                ),
            ],
            name='d3_3_16ii01',
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
                                ' test Units of length for hexBinary datatype   ',
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href='http://www.w3.org/TR/xmlschema11-2/#hexBinary'
                ),
                DocumentationReference(
                    href='../common/XSD1_1TestCategories.xml#xsd1_1-Misc-ListBounds'
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href='../ibmData/instance_invalid/D3_3_16/d3_3_16ii02.xsd'
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
                name='d3_3_16ii02s'
            ),
            instance_test=[
                InstanceTest(
                    instance_document=InstanceDocument(
                        href='../ibmData/instance_invalid/D3_3_16/d3_3_16ii02.xml'
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
                    name='d3_3_16ii02i'
                ),
            ],
            name='d3_3_16ii02',
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
                                ' test Units of length for base64Binary datatype.  ',
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href='http://www.w3.org/TR/xmlschema11-2/#base64Binary'
                ),
                DocumentationReference(
                    href='../common/XSD1_1TestCategories.xml#xsd1_1-Misc-ListBounds'
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href='../ibmData/valid/D3_3_17/d3_3_17v01.xsd'
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
                name='d3_3_17v01s'
            ),
            instance_test=[
                InstanceTest(
                    instance_document=InstanceDocument(
                        href='../ibmData/valid/D3_3_17/d3_3_17v01.xml'
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
                    name='d3_3_17v01i'
                ),
            ],
            name='d3_3_17v01',
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
                                ' test base64Binary datatype ',
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href='http://www.w3.org/TR/xmlschema11-2/#base64Binary'
                ),
                DocumentationReference(
                    href='../common/XSD1_1TestCategories.xml#xsd1_1-Misc-ListBounds'
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href='../ibmData/instance_invalid/D3_3_17/d3_3_17ii01.xsd'
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
                name='d3_3_17ii01s'
            ),
            instance_test=[
                InstanceTest(
                    instance_document=InstanceDocument(
                        href='../ibmData/instance_invalid/D3_3_17/d3_3_17ii01.xml'
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
                    name='d3_3_17ii01i'
                ),
            ],
            name='d3_3_17ii01',
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
                                ' test Units of length for list datatype    ',
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href='http://www.w3.org/TR/xmlschema11-2/#list-datatypes'
                ),
                DocumentationReference(
                    href='../common/XSD1_1TestCategories.xml#xsd1_1-Misc-ListBounds'
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href='../ibmData/instance_invalid/D2_4_1_2/d2_4_1_2ii01.xsd'
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
                name='d2_4_1_2ii01s'
            ),
            instance_test=[
                InstanceTest(
                    instance_document=InstanceDocument(
                        href='../ibmData/instance_invalid/D2_4_1_2/d2_4_1_2ii01.xml'
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
                    name='d2_4_1_2ii01i'
                ),
            ],
            name='d2_4_1_2ii01',
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
                                ' Unions with no member types (and thus with empty value space and lexical space) are now explicitly allowed.    ',
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href='http://www.w3.org/TR/xmlschema11-2/#dt-union'
                ),
                DocumentationReference(
                    href='../common/XSD1_1TestCategories.xml#xsd1_1-UnionTypes'
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href='../ibmData/schema_invalid/D2_4_1_3/d2_4_1_3si01.xsd'
                    ),
                ],
                expected=[
                    Expected(
                        validity=ExpectedOutcome.INVALID
                    ),
                ],
                current=Current(
                    status=Status.ACCEPTED,
                    date=XmlDate(2010, 12, 1)
                ),
                name='d2_4_1_3si01s'
            ),
            name='d2_4_1_3si01'
        ),
        TestGroup(
            annotation=[
                Annotation(
                    appinfo_or_documentation=[
                        Documentation(
                            content=[
                                ' use of the namespace http://www.w3.org/2001/XMLSchema-datatypes has been deprecated.  ',
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href='http://www.w3.org/TR/xmlschema11-2/#changes'
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href='../ibmData/schema_invalid/D3_1/d3_1si01.xsd'
                    ),
                ],
                expected=[
                    Expected(
                        validity=ExpectedOutcome.INVALID
                    ),
                ],
                current=Current(
                    status=Status.ACCEPTED,
                    date=XmlDate(2010, 12, 1)
                ),
                name='d3_1si01s'
            ),
            name='d3_1si01',
            version=[
                KnownToken.VALUE_1_1,
            ]
        ),
    ],
    contributor='IBM',
    name='UnitsLength',
    other_attributes={
        '{http://www.w3.org/2001/XMLSchema-instance}schemaLocation': 'http://www.w3.org/XML/2004/xml-schema-test-suite/ ../common/xsts.xsd',
    }
)
