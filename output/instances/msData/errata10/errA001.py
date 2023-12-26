from decimal import Decimal
from output.models.ms_data.errata10.err_a001_xsd.err_a001 import Root
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Root(
    choice=[
        -100,
        DerivedElement(
            qname='testUnsignedByte',
            value=100
        ),
        DerivedElement(
            qname='testInteger',
            value=-32000
        ),
        DerivedElement(
            qname='testPositiveInteger',
            value=50000
        ),
        DerivedElement(
            qname='testNegativeInteger',
            value=-50000
        ),
        DerivedElement(
            qname='testNonNegativeInteger',
            value=50000
        ),
        DerivedElement(
            qname='testNonPositiveInteger',
            value=-50000
        ),
        DerivedElement(
            qname='testInt',
            value=-32000
        ),
        DerivedElement(
            qname='testUnsignedInt',
            value=50000
        ),
        DerivedElement(
            qname='testLong',
            value=-123456789012345
        ),
        DerivedElement(
            qname='testUnsignedLong',
            value=12345789012345
        ),
        DerivedElement(
            qname='testShort',
            value=-12345
        ),
        DerivedElement(
            qname='testUnsignedShort',
            value=12345
        ),
        Decimal('123456789.12345'),
    ]
)
