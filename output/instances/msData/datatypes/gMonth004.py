from output.models.ms_data.datatypes.g_month_xsd.g_month import ComplexTest
from output.models.ms_data.datatypes.g_month_xsd.g_month import Root
from xsdata.models.datatype import XmlPeriod


obj = Root(
    complex_test=ComplexTest(
        comp_foo=XmlPeriod("--05---05:00")
    ),
    simple_test=XmlPeriod("--05---05:00")
)
