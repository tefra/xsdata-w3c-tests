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
                        '{http://www.w3.org/1999/xlink}href': 'http://www.w3.org/TR/xmlschema11-2/#list-datatypes',
                    },
                    content=[
                        'list',
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
                                'test Units of length for list datatype.',
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
                        href='../ibmData/valid/D2_4_1_2/d2_4_1_2v01.xsd'
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
                name='d2_4_1_2v01s'
            ),
            instance_test=[
                InstanceTest(
                    instance_document=InstanceDocument(
                        href='../ibmData/valid/D2_4_1_2/d2_4_1_2v01.xml'
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
                    name='d2_4_1_2v01i'
                ),
            ],
            name='d2_4_1_2v01',
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
                                'Lists cannot be bounded',
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
                        href='../ibmData/schema_invalid/D2_4_1_2/d2_4_1_2si01.xsd'
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
                name='d2_4_1_2si01s'
            ),
            name='d2_4_1_2si01',
            version=[
                KnownToken.VALUE_1_1,
            ]
        ),
    ],
    contributor='IBM',
    name='list',
    other_attributes={
        '{http://www.w3.org/2001/XMLSchema-instance}schemaLocation': 'http://www.w3.org/XML/2004/xml-schema-test-suite/ ../common/xsts.xsd',
    }
)
