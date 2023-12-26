from decimal import Decimal
from output.models.ms_data.datatypes.decimal_xsd.decimal import ComplexTest
from output.models.ms_data.datatypes.decimal_xsd.decimal import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo=Decimal('12345678901234567890123456789')
    ),
    simple_test=Decimal('12345678901234567890123456789')
)
