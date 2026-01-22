from output.models.ms_data.datatypes.facets.duration.duration_min_inclusive001_xsd.duration_min_inclusive001 import Test
from xsdata.models.datatype import XmlDuration


obj = Test(
    foo=XmlDuration("P1Y1MT1H")
)
