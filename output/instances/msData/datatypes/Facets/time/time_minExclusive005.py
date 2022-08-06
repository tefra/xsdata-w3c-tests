from output.models.ms_data.datatypes.facets.time.time_min_exclusive005_xsd.time_min_exclusive005 import Test
from xsdata.models.datatype import XmlTime


obj = Test(
    foo=XmlTime(13, 20, 0, 0, -180)
)
