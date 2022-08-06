from output.models.ms_data.datatypes.facets.time.time_min_inclusive001_xsd.time_min_inclusive001 import Test
from xsdata.models.datatype import XmlTime


obj = Test(
    foo=XmlTime(10, 21, 0, 0, -300)
)
