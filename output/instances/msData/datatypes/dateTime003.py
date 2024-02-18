from output.models.ms_data.datatypes.date_time_xsd.date_time import ComplexTest
from output.models.ms_data.datatypes.date_time_xsd.date_time import Root
from output.models.ms_data.datatypes.date_time_xsd.date_time import SimpleTest
from xsdata.models.datatype import XmlDateTime


obj = Root(
    complex_test=ComplexTest(
        comp_foo=XmlDateTime(1985, 4, 12, 10, 30, 0)
    ),
    simple_test=SimpleTest(
        value=XmlDateTime(1985, 4, 12, 10, 30, 0)
    )
)
