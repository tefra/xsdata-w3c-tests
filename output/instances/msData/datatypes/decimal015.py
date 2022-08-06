from decimal import Decimal
from output.models.ms_data.datatypes.decimal_xsd.decimal import ComplexTest
from output.models.ms_data.datatypes.decimal_xsd.decimal import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo=Decimal("9876543210987654321098765432")
    ),
    simple_test=Decimal("9876543210987654321098765432")
)
