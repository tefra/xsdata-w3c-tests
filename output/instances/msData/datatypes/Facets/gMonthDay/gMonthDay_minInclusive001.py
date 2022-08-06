from output.models.ms_data.datatypes.facets.g_month_day.g_month_day_min_inclusive001_xsd.g_month_day_min_inclusive001 import Test
from xsdata.models.datatype import XmlPeriod


obj = Test(
    foo=XmlPeriod("--01-01")
)
