from output.models.ms_data.datatypes.time_xsd.time import ComplexTest
from output.models.ms_data.datatypes.time_xsd.time import Root
from xsdata.models.datatype import XmlTime


obj = Root(
    complex_test=ComplexTest(
        comp_foo=XmlTime(13, 20, 0, 0, -359)
    ),
    simple_test=XmlTime(13, 20, 0, 0, -359)
)