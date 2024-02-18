from decimal import Decimal
from output.models.ms_data.datatypes.decimal_xsd.decimal import ComplexTest
from output.models.ms_data.datatypes.decimal_xsd.decimal import Root
from output.models.ms_data.datatypes.decimal_xsd.decimal import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo=Decimal('-0.0')
    ),
    simple_test=SimpleTest(
        value=Decimal('-0.0')
    )
)
