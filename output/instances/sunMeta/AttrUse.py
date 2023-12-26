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
                                    qname='{http://www.w3.org/XML/2004/xml-schema-test-suite/}Title',
                                    text='Attribute declaration is resolved for attribute use. (valid schema)'
                                ),
                                AnyElement(
                                    qname='{http://www.w3.org/XML/2004/xml-schema-test-suite/}Description',
                                    text='Attribute use should has proper ref value to be resolved to its declaration.'
                                ),
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href='http://www.w3.org/TR/2001/REC-xmlschema-1-20010502/#cAttributeUse'
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href='../sunData/AttrUse/AU_attrDecl/AU_attrDecl00101m/AU_attrDecl00101m1_p.xsd'
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
                name='AU_attrDecl00101m1_p'
            ),
            instance_test=[
                InstanceTest(
                    instance_document=InstanceDocument(
                        href='../sunData/AttrUse/AU_attrDecl/AU_attrDecl00101m/AU_attrDecl00101m1.xml'
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
                    name='Positive'
                ),
            ],
            name='au_attrdecl00101m1_p'
        ),
        TestGroup(
            annotation=[
                Annotation(
                    appinfo_or_documentation=[
                        Documentation(
                            content=[
                                AnyElement(
                                    qname='{http://www.w3.org/XML/2004/xml-schema-test-suite/}Title',
                                    text='Attribute declaration is resolved for attribute use. (invalid schema)'
                                ),
                                AnyElement(
                                    qname='{http://www.w3.org/XML/2004/xml-schema-test-suite/}Description',
                                    text='Attribute use should has proper ref value to be resolved to its declaration.'
                                ),
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href='http://www.w3.org/TR/2001/REC-xmlschema-1-20010502/#cAttributeUse'
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href='../sunData/AttrUse/AU_attrDecl/AU_attrDecl00101m/AU_attrDecl00101m1_n.xsd'
                    ),
                ],
                expected=[
                    Expected(
                        validity=ExpectedOutcome.INVALID
                    ),
                ],
                current=Current(
                    status=Status.ACCEPTED,
                    date=XmlDate(2005, 6, 21)
                ),
                name='AU_attrDecl00101m1_n'
            ),
            name='au_attrdecl00101m1_n'
        ),
        TestGroup(
            annotation=[
                Annotation(
                    appinfo_or_documentation=[
                        Documentation(
                            content=[
                                AnyElement(
                                    qname='{http://www.w3.org/XML/2004/xml-schema-test-suite/}Title',
                                    text='Attribute use is declared required.  (valid schema)'
                                ),
                                AnyElement(
                                    qname='{http://www.w3.org/XML/2004/xml-schema-test-suite/}Description',
                                    text='Element whose attribute use is declared required should has the attribute specified.'
                                ),
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href='http://www.w3.org/TR/2001/REC-xmlschema-1-20010502/#cAttributeUse'
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href='../sunData/AttrUse/AU_required/AU_required00101m/AU_required00101m1.xsd'
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
                name='AU_required00101m1'
            ),
            instance_test=[
                InstanceTest(
                    instance_document=InstanceDocument(
                        href='../sunData/AttrUse/AU_required/AU_required00101m/AU_required00101m1_p.xml'
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
                    name='Positive'
                ),
                InstanceTest(
                    instance_document=InstanceDocument(
                        href='../sunData/AttrUse/AU_required/AU_required00101m/AU_required00101m1_n.xml'
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.INVALID
                        ),
                    ],
                    current=Current(
                        status=Status.ACCEPTED,
                        date=XmlDate(2005, 6, 21)
                    ),
                    name='Negative'
                ),
            ],
            name='au_required00101m1'
        ),
        TestGroup(
            annotation=[
                Annotation(
                    appinfo_or_documentation=[
                        Documentation(
                            content=[
                                AnyElement(
                                    qname='{http://www.w3.org/XML/2004/xml-schema-test-suite/}Title',
                                    text='Attribute with fixed value is declared within element by reference  (valid schema)'
                                ),
                                AnyElement(
                                    qname='{http://www.w3.org/XML/2004/xml-schema-test-suite/}Description',
                                    text='Attribute declared with fixed value may not have another value in an instance document.'
                                ),
                            ]
                        ),
                    ]
                ),
            ],
            documentation_reference=[
                DocumentationReference(
                    href='http://www.w3.org/TR/2001/REC-xmlschema-1-20010502/#cAttributeUse'
                ),
            ],
            schema_test=SchemaTest(
                schema_document=[
                    SchemaDocument(
                        href='../sunData/AttrUse/AU_valConstr/AU_valConstr00101m/AU_valConstr00101m1.xsd'
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
                name='AU_valConstr00101m1'
            ),
            instance_test=[
                InstanceTest(
                    instance_document=InstanceDocument(
                        href='../sunData/AttrUse/AU_valConstr/AU_valConstr00101m/AU_valConstr00101m1_p.xml'
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
                    name='Positive'
                ),
                InstanceTest(
                    instance_document=InstanceDocument(
                        href='../sunData/AttrUse/AU_valConstr/AU_valConstr00101m/AU_valConstr00101m1_n.xml'
                    ),
                    expected=[
                        Expected(
                            validity=ExpectedOutcome.INVALID
                        ),
                    ],
                    current=Current(
                        status=Status.ACCEPTED,
                        date=XmlDate(2005, 6, 21)
                    ),
                    name='Negative'
                ),
            ],
            name='au_valconstr00101m1'
        ),
    ],
    contributor='SUN',
    name='AttrUse',
    other_attributes={
        '{http://www.w3.org/2001/XMLSchema-instance}schemaLocation': 'http://www.w3.org/XML/2004/xml-schema-test-suite/ ../common/xsts.xsd',
    }
)
