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
                                '&#10;&#9;&#9;    Composition of XML schemas via xs:import to be able to achive hetrogeneous namespaced elements&#10;&#9;&#9;&#9;in "one" XML document.&#10;            ',
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href="http://www.w3.org/TR/xmlschema11-1/"
                ),
                DocumentationReference(
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-SchemaComposition-NSRefRequiresImport"
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href="../ibmData/mixed/targetNamespace/tns4.xsd"
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
                name="targetNamespace_004_1"
            ),
            instance_test=[
                InstanceTest(
                    instance_document=InstanceDocument(
                        href="../ibmData/mixed/targetNamespace/tns4.xml"
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
                    name="targetNamespace_004_2"
                ),
            ],
            name="targetNamespace_004",
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
                                "&#10;&#9;&#9;    This example demonstrates 'targetNamespace' attribute on xs:attribute schema component.&#10;&#9;&#9;    ",
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href="http://www.w3.org/TR/xmlschema11-1/"
                ),
                DocumentationReference(
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-NewLocalDecl-TargNSOnAttrDecl"
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href="../ibmData/mixed/targetNamespace/tns5.xsd"
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
                name="targetNamespace_005_1"
            ),
            instance_test=[
                InstanceTest(
                    instance_document=InstanceDocument(
                        href="../ibmData/mixed/targetNamespace/tns5.xml"
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
                    name="targetNamespace_005_2"
                ),
            ],
            name="targetNamespace_005",
            version=[
                KnownToken.VALUE_1_1,
            ]
        ),
    ],
    contributor="IBM",
    name="TargetNS",
    version=[
        KnownToken.VALUE_1_1,
    ],
    other_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation": "http://www.w3.org/XML/2004/xml-schema-test-suite/ ../common/xsts.xsd",
    }
)
