from output.models.ms_data.datatypes.facets.date_time.date_time_min_inclusive001_xsd.date_time_min_inclusive001 import Test
from xsdata.models.datatype import XmlDateTime


obj = Test(
    foo=XmlDateTime(1981, 3, 12, 10, 30, 0)
)
