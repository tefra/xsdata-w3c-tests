from output.models.ms_data.datatypes.string_xsd.string import ComplexTest
from output.models.ms_data.datatypes.string_xsd.string import Root


obj = Root(
    complex_test=ComplexTest(
        comp_foo="#x20 | #xD | #xA | [a-zA-Z0-9] | [-'()+,./:=?;!*#@$_%]"
    ),
    simple_test="#x20 | #xD | #xA | [a-zA-Z0-9] | [-'()+,./:=?;!*#@$_%]"
)