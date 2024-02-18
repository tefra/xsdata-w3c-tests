from output.models.ms_data.datatypes.boolean018_xsd.boolean018 import ComplexTest
from output.models.ms_data.datatypes.boolean018_xsd.boolean018 import ComplexfooTypeCompFoo
from output.models.ms_data.datatypes.boolean018_xsd.boolean018 import Root
from output.models.ms_data.datatypes.boolean018_xsd.boolean018 import SimpleTest
from output.models.ms_data.datatypes.boolean018_xsd.boolean018 import SimplefooType


obj = Root(
    complex_test=ComplexTest(
        comp_foo=ComplexfooTypeCompFoo.VALUE_0
    ),
    simple_test=SimpleTest(
        value=SimplefooType.TRUE
    )
)
