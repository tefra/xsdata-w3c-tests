from output.models.ms_data.datatypes.facets.date_time.date_time_min_exclusive005_xsd.date_time_min_exclusive005 import Test
from xsdata.models.datatype import XmlDateTime


obj = Test(
    foo=XmlDateTime(1985, 4, 12, 10, 30, 0)
)
