from output.models.ms_data.datatypes.date_time_xsd.date_time import ComplexTest
from output.models.ms_data.datatypes.date_time_xsd.date_time import Root
from output.models.ms_data.datatypes.date_time_xsd.date_time import SimpleTest
from xsdata.models.datatype import XmlDateTime


obj = Root(
    complex_test=ComplexTest(
        comp_foo=XmlDateTime(1999, 5, 31, 13, 20, 0, 0, 345)
    ),
    simple_test=SimpleTest(
        value=XmlDateTime(1999, 5, 31, 13, 20, 0, 0, 345)
    )
)
