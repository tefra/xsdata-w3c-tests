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
                        "{http://www.w3.org/1999/xlink}href": "http://www.w3.org/TR/xmlschema11-1/#Constraint_Summary",
                    },
                    content=[
                        "&#10;        Identity-constraint tests&#10;&#9;      ",
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
                                "Valid test for identity constraint referrals with annotation  ",
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
                    href="http://www.w3.org/TR/xmlschema11-1/#Constraint_Summary",
                    other_attributes={}
                ),
                DocumentationReference(
                    annotation=[],
                    type=TypeType.LOCATOR,
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-NewLocalDecl-NamedIdContraintsOnElemDecl",
                    other_attributes={}
                ),
            ],
            schema_test=SchemaTest(
                annotation=[],
                schema_document=[
                    SchemaDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/valid/S2_2_4/s2_2_4v01.xsd",
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
                name="s2_2_4v01s",
                version=[],
                other_attributes={}
            ),
            instance_test=[
                InstanceTest(
                    annotation=[],
                    instance_document=InstanceDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/valid/S2_2_4/s2_2_4v01.xml",
                        other_attributes={}
                    ),
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
                    name="s2_2_4v01i",
                    version=[],
                    other_attributes={}
                ),
            ],
            name="s2_2_4v01",
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
                                "Valid test for identity constraint referrals  ",
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
                    href="http://www.w3.org/TR/xmlschema11-1/#Constraint_Summary",
                    other_attributes={}
                ),
                DocumentationReference(
                    annotation=[],
                    type=TypeType.LOCATOR,
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-NewLocalDecl-NamedIdContraintsOnElemDecl",
                    other_attributes={}
                ),
            ],
            schema_test=SchemaTest(
                annotation=[],
                schema_document=[
                    SchemaDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/valid/S2_2_4/s2_2_4v02.xsd",
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
                name="s2_2_4v02s",
                version=[],
                other_attributes={}
            ),
            instance_test=[
                InstanceTest(
                    annotation=[],
                    instance_document=InstanceDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/valid/S2_2_4/s2_2_4v02.xml",
                        other_attributes={}
                    ),
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
                    name="s2_2_4v02i",
                    version=[],
                    other_attributes={}
                ),
            ],
            name="s2_2_4v02",
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
                                "Tests unresolvable xpath ",
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
                    href="http://www.w3.org/TR/xmlschema11-1/#Constraint_Summary",
                    other_attributes={}
                ),
                DocumentationReference(
                    annotation=[],
                    type=TypeType.LOCATOR,
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-NewLocalDecl-NamedIdContraintsOnElemDecl",
                    other_attributes={}
                ),
            ],
            schema_test=SchemaTest(
                annotation=[],
                schema_document=[
                    SchemaDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/valid/S2_2_4/s2_2_4v03.xsd",
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
                name="s2_2_4v03s",
                version=[],
                other_attributes={}
            ),
            instance_test=[
                InstanceTest(
                    annotation=[],
                    instance_document=InstanceDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/valid/S2_2_4/s2_2_4v03.xml",
                        other_attributes={}
                    ),
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
                    name="s2_2_4v03i",
                    version=[],
                    other_attributes={}
                ),
            ],
            name="s2_2_4v03",
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
                                "test attribute which is required as declared in key is abscent ",
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
                    href="http://www.w3.org/TR/xmlschema11-1/#Constraint_Summary",
                    other_attributes={}
                ),
                DocumentationReference(
                    annotation=[],
                    type=TypeType.LOCATOR,
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-NewLocalDecl-NamedIdContraintsOnElemDecl",
                    other_attributes={}
                ),
            ],
            schema_test=SchemaTest(
                annotation=[],
                schema_document=[
                    SchemaDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/instance_invalid/S2_2_4/s2_2_4ii01.xsd",
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
                name="s2_2_4ii01s",
                version=[],
                other_attributes={}
            ),
            instance_test=[
                InstanceTest(
                    annotation=[],
                    instance_document=InstanceDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/instance_invalid/S2_2_4/s2_2_4ii01.xml",
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
                    name="s2_2_4ii01i",
                    version=[],
                    other_attributes={}
                ),
            ],
            name="s2_2_4ii01",
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
                                "Tests for duplication on components with identity constraints Checks that ic referrals works when nested",
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
                    href="http://www.w3.org/TR/xmlschema11-1/#Constraint_Summary",
                    other_attributes={}
                ),
                DocumentationReference(
                    annotation=[],
                    type=TypeType.LOCATOR,
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-NewLocalDecl-NamedIdContraintsOnElemDecl",
                    other_attributes={}
                ),
            ],
            schema_test=SchemaTest(
                annotation=[],
                schema_document=[
                    SchemaDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/instance_invalid/S2_2_4/s2_2_4ii02.xsd",
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
                name="s2_2_4ii02s",
                version=[],
                other_attributes={}
            ),
            instance_test=[
                InstanceTest(
                    annotation=[],
                    instance_document=InstanceDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/instance_invalid/S2_2_4/s2_2_4ii02.xml",
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
                    name="s2_2_4ii02i",
                    version=[],
                    other_attributes={}
                ),
            ],
            name="s2_2_4ii02",
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
                                "Tests for duplication on components with keys and uniques",
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
                    href="http://www.w3.org/TR/xmlschema11-1/#Constraint_Summary",
                    other_attributes={}
                ),
                DocumentationReference(
                    annotation=[],
                    type=TypeType.LOCATOR,
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-NewLocalDecl-NamedIdContraintsOnElemDecl",
                    other_attributes={}
                ),
            ],
            schema_test=SchemaTest(
                annotation=[],
                schema_document=[
                    SchemaDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/instance_invalid/S2_2_4/s2_2_4ii03.xsd",
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
                name="s2_2_4ii03s",
                version=[],
                other_attributes={}
            ),
            instance_test=[
                InstanceTest(
                    annotation=[],
                    instance_document=InstanceDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/instance_invalid/S2_2_4/s2_2_4ii03.xml",
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
                    name="s2_2_4ii03i",
                    version=[],
                    other_attributes={}
                ),
            ],
            name="s2_2_4ii03",
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
                                "3.11.3.4 - If ref is present, then only id and [annotation] are allowed to appear together with ref.",
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
                    href="http://www.w3.org/TR/xmlschema11-1/#Constraint_Summary",
                    other_attributes={}
                ),
                DocumentationReference(
                    annotation=[],
                    type=TypeType.LOCATOR,
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-NewLocalDecl-NamedIdContraintsOnElemDecl",
                    other_attributes={}
                ),
            ],
            schema_test=SchemaTest(
                annotation=[],
                schema_document=[
                    SchemaDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/schema_invalid/S2_2_4/s2_2_4si01.xsd",
                        other_attributes={}
                    ),
                ],
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
                name="s2_2_4si01s",
                version=[],
                other_attributes={}
            ),
            instance_test=[],
            name="s2_2_4si01",
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
                                "3.11.3.5 - If ref is present, then the {identity-constraint category} of the identity-constraint definition resolved to by the actual value of the ref [attribute] matches the name of the element information item.",
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
                    href="http://www.w3.org/TR/xmlschema11-1/#Constraint_Summary",
                    other_attributes={}
                ),
                DocumentationReference(
                    annotation=[],
                    type=TypeType.LOCATOR,
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-NewLocalDecl-NamedIdContraintsOnElemDecl",
                    other_attributes={}
                ),
            ],
            schema_test=SchemaTest(
                annotation=[],
                schema_document=[
                    SchemaDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/schema_invalid/S2_2_4/s2_2_4si02.xsd",
                        other_attributes={}
                    ),
                ],
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
                name="s2_2_4si02s",
                version=[],
                other_attributes={}
            ),
            instance_test=[],
            name="s2_2_4si02",
            version=[],
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
                                "identity constraints contains no name and no ref attribute ",
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
                    href="http://www.w3.org/TR/xmlschema11-1/#Constraint_Summary",
                    other_attributes={}
                ),
                DocumentationReference(
                    annotation=[],
                    type=TypeType.LOCATOR,
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-NewLocalDecl-NamedIdContraintsOnElemDecl",
                    other_attributes={}
                ),
            ],
            schema_test=SchemaTest(
                annotation=[],
                schema_document=[
                    SchemaDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/schema_invalid/S2_2_4/s2_2_4si04.xsd",
                        other_attributes={}
                    ),
                ],
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
                name="s2_2_4si04s",
                version=[],
                other_attributes={}
            ),
            instance_test=[],
            name="s2_2_4si04",
            version=[],
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
                                "key refers to nonexisting key ",
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
                    href="http://www.w3.org/TR/xmlschema11-1/#Constraint_Summary",
                    other_attributes={}
                ),
                DocumentationReference(
                    annotation=[],
                    type=TypeType.LOCATOR,
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-NewLocalDecl-NamedIdContraintsOnElemDecl",
                    other_attributes={}
                ),
            ],
            schema_test=SchemaTest(
                annotation=[],
                schema_document=[
                    SchemaDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/schema_invalid/S2_2_4/s2_2_4si05.xsd",
                        other_attributes={}
                    ),
                ],
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
                name="s2_2_4si05s",
                version=[],
                other_attributes={}
            ),
            instance_test=[],
            name="s2_2_4si05",
            version=[],
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
                                "[key] cannot have both ref and name attributes",
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
                    href="http://www.w3.org/TR/xmlschema11-1/#Constraint_Summary",
                    other_attributes={}
                ),
                DocumentationReference(
                    annotation=[],
                    type=TypeType.LOCATOR,
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-NewLocalDecl-NamedIdContraintsOnElemDecl",
                    other_attributes={}
                ),
            ],
            schema_test=SchemaTest(
                annotation=[],
                schema_document=[
                    SchemaDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/schema_invalid/S2_2_4/s2_2_4si06.xsd",
                        other_attributes={}
                    ),
                ],
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
                name="s2_2_4si06s",
                version=[],
                other_attributes={}
            ),
            instance_test=[],
            name="s2_2_4si06",
            version=[],
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
                                "[key] cannot have both ref and name attributes",
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
                    href="http://www.w3.org/TR/xmlschema11-1/#Constraint_Summary",
                    other_attributes={}
                ),
                DocumentationReference(
                    annotation=[],
                    type=TypeType.LOCATOR,
                    href="../common/XSD1_1TestCategories.xml#xsd1_1-NewLocalDecl-NamedIdContraintsOnElemDecl",
                    other_attributes={}
                ),
            ],
            schema_test=SchemaTest(
                annotation=[],
                schema_document=[
                    SchemaDocument(
                        annotation=[],
                        type=TypeType.LOCATOR,
                        href="../ibmData/schema_invalid/S2_2_4/s2_2_4si07.xsd",
                        other_attributes={}
                    ),
                ],
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
                name="s2_2_4si07s",
                version=[],
                other_attributes={}
            ),
            instance_test=[],
            name="s2_2_4si07",
            version=[],
            other_attributes={}
        ),
    ],
    contributor="IBM",
    name="IdentityConstraint",
    version=[],
    other_attributes={
        "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation": "http://www.w3.org/XML/2004/xml-schema-test-suite/ AnnotatedTSSchema.xsd",
    }
)