from output.models.ms_data.datatypes.any_uri_xsd.any_uri import ComplexTest
from output.models.ms_data.datatypes.any_uri_xsd.any_uri import Root
from output.models.ms_data.datatypes.any_uri_xsd.any_uri import SimpleTest


obj = Root(
    complex_test=ComplexTest(
        comp_foo='mailto:davebrow@microsoft.com'
    ),
    simple_test=SimpleTest(
        value='mailto:davebrow@microsoft.com'
    )
)
