from output.models.common.xsts_xsd.xsts import Annotation
from output.models.common.xsts_xsd.xsts import Current
from output.models.common.xsts_xsd.xsts import Documentation
from output.models.common.xsts_xsd.xsts import DocumentationReference
from output.models.common.xsts_xsd.xsts import Expected
from output.models.common.xsts_xsd.xsts import ExpectedOutcome
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
                        '{http://www.w3.org/1999/xlink}href': 'http://www.w3.org/TR/xmlschema11-1/#composition-schemaImport',
                    },
                    content=[
                        'Referring to a namespace requires an xs:import',
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
                                'invalid schema for referring to a namespace requires an xs:import',
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href='http://www.w3.org/TR/xmlschema11-1/#composition-schemaImport'
                ),
                DocumentationReference(
                    href='../common/XSD1_1TestCategories.xml#xsd1_1-SchemaComposition-NSRefRequiresImport'
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href='../ibmData/schema_invalid/S4_2_6/s4_2_6si01.xsd'
                    ),
                    SchemaDocument(
                        href='../ibmData/schema_invalid/S4_2_6/s4_2_6si01b.xsd'
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
                name='s4_2_6si01s'
            ),
            name='s4_2_6si01',
            version=[
                KnownToken.VALUE_1_1,
            ]
        ),
    ],
    contributor='IBM',
    name='XSImportReference',
    other_attributes={
        '{http://www.w3.org/2001/XMLSchema-instance}schemaLocation': 'http://www.w3.org/XML/2004/xml-schema-test-suite/ ../common/xsts.xsd',
    }
)
