from output.models.ms_data.datatypes.date_xsd.date import ComplexTest
from output.models.ms_data.datatypes.date_xsd.date import Root
from output.models.ms_data.datatypes.date_xsd.date import SimpleTest
from xsdata.models.datatype import XmlDate


obj = Root(
    complex_test=ComplexTest(
        comp_foo=XmlDate(2000, 2, 29)
    ),
    simple_test=SimpleTest(
        value=XmlDate(2000, 2, 29)
    )
)
