from output.models.ms_data.datatypes.g_year_xsd.g_year import ComplexTest
from output.models.ms_data.datatypes.g_year_xsd.g_year import Root
from xsdata.models.datatype import XmlPeriod


obj = Root(
    complex_test=ComplexTest(
        comp_foo=XmlPeriod("1999-05:00")
    ),
    simple_test=XmlPeriod("1999-05:00")
)
