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
from output.models.common.xsts_xsd.xsts import Prior
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
                        "{http://www.w3.org/1999/xlink}href": "http://www.w3.org/TR/xmlschema11-1/#sec-cos-element-consistent",
                    },
                    content=[
                        "&#10;        tighter rule for EDC as regards the type of an element that matches a wildcard&#10;        ",
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
                                "tighter rule for EDC as regards the type of an element that matches a wildcard ",
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
                    href="http://www.w3.org/TR/xmlschema11-1/#sec-cos-element-consistent",
                    other_attributes={}
                ),
                DocumentationReference(
                    annotation=[],
                    type=TypeType.LOCATOR,
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-Wildcards-TighterMatchingRuleForEDC",
                    other_attributes={}
                ),
            ],
            schema_test=SchemaTest(
                annotation=[],
                schema_document=[
                    SchemaDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/valid/S3_8_6/s3_8_6v01.xsd",
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
                name="s3_8_6v01s",
                version=[],
                other_attributes={}
            ),
            instance_test=[
                InstanceTest(
                    annotation=[],
                    instance_document=InstanceDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/valid/S3_8_6/s3_8_6v01.xml",
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
                        annotation=[
                            Annotation(
                                appinfo_or_documentation=[
                                    Documentation(
                                        source=None,
                                        lang=None,
                                        other_attributes={},
                                        content=[
                                            '&#10;                        Changed the status to "invalid" in response to bug #12130&#10;                    ',
                                        ]
                                    ),
                                ],
                                other_attributes={}
                            ),
                        ],
                        status=Status.ACCEPTED,
                        date=XmlDate(2011, 7, 29),
                        bugzilla=None,
                        other_attributes={}
                    ),
                    prior=[
                        Prior(
                            annotation=[],
                            status=Status.ACCEPTED,
                            date=XmlDate(2010, 12, 1),
                            bugzilla=None,
                            other_attributes={}
                        ),
                    ],
                    name="s3_8_6v01i",
                    version=[],
                    other_attributes={}
                ),
            ],
            name="s3_8_6v01",
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
                                "tighter rule for EDC as regards the type of an element that matches a wildcard ",
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
                    href="http://www.w3.org/TR/xmlschema11-1/#sec-cos-element-consistent",
                    other_attributes={}
                ),
                DocumentationReference(
                    annotation=[],
                    type=TypeType.LOCATOR,
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-Wildcards-TighterMatchingRuleForEDC",
                    other_attributes={}
                ),
            ],
            schema_test=SchemaTest(
                annotation=[],
                schema_document=[
                    SchemaDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/instance_invalid/S3_8_6/s3_8_6ii01.xsd",
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
                name="s3_8_6ii01s",
                version=[],
                other_attributes={}
            ),
            instance_test=[
                InstanceTest(
                    annotation=[],
                    instance_document=InstanceDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/instance_invalid/S3_8_6/s3_8_6ii01.xml",
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
                    name="s3_8_6ii01i",
                    version=[],
                    other_attributes={}
                ),
            ],
            name="s3_8_6ii01",
            version=[
                KnownToken.VALUE_1_1,
            ],
            other_attributes={}
        ),
    ],
    contributor="IBM",
    name="EDCWildcard",
    version=[],
    other_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation": "http://www.w3.org/XML/2004/xml-schema-test-suite/ AnnotatedTSSchema.xsd",
    }
)