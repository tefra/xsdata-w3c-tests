from output.models.ibm_data.valid.d3_4_28.d3_4_28v02_xsd.d3_4_28v02 import DTimeStampEnumeration
from output.models.ibm_data.valid.d3_4_28.d3_4_28v02_xsd.d3_4_28v02 import Root
from xsdata.models.datatype import XmlDateTime


obj = Root(
    attrd_time_stamp_type=XmlDateTime(2000, 1, 1, 12, 0, 0, 123000000, 0),
    attrd_time_stamp_enumeration=DTimeStampEnumeration.VALUE_2002_01_01_T12_00_00_990_08_00,
    attrd_time_stamp_pattern='2003-01-01T01:00:00-08:00',
    attrd_time_stamp_min_max_inclusive=XmlDateTime(2003, 1, 1, 12, 0, 0, 990000000, -480),
    attrd_time_stamp_min_max_exclusive=XmlDateTime(1999, 1, 1, 11, 59, 59, 0, 0)
)
