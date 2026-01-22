from decimal import Decimal
from output.models.ms_data.errata10.err_a001_xsd.err_a001 import Root


obj = Root(
    choice=[
        Root.TestByte(
            value=-100
        ),
        Root.TestUnsignedByte(
            value=100
        ),
        Root.TestInteger(
            value=-32000
        ),
        Root.TestPositiveInteger(
            value=50000
        ),
        Root.TestNegativeInteger(
            value=-50000
        ),
        Root.TestNonNegativeInteger(
            value=50000
        ),
        Root.TestNonPositiveInteger(
            value=-50000
        ),
        Root.TestInt(
            value=-32000
        ),
        Root.TestUnsignedInt(
            value=50000
        ),
        Root.TestLong(
            value=-123456789012345
        ),
        Root.TestUnsignedLong(
            value=12345789012345
        ),
        Root.TestShort(
            value=-12345
        ),
        Root.TestUnsignedShort(
            value=12345
        ),
        Decimal('123456789.12345'),
    ]
)
