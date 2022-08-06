from output.models.ms_data.datatypes.date_xsd.date import ComplexTest
from output.models.ms_data.datatypes.date_xsd.date import Root
from xsdata.models.datatype import XmlDate


obj = Root(
    complex_test=ComplexTest(
        comp_foo=XmlDate(1999, 5, 31)
    ),
    simple_test=XmlDate(1999, 5, 31)
)
