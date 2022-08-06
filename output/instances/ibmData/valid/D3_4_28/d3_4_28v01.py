from output.models.ibm_data.valid.d3_4_28.d3_4_28v01_xsd.d3_4_28v01 import DTimeStampEnumeration
from output.models.ibm_data.valid.d3_4_28.d3_4_28v01_xsd.d3_4_28v01 import Root
from xsdata.models.datatype import XmlDateTime


obj = Root(
    eld_time_stamp_type=[
        XmlDateTime(1998, 1, 1, 12, 0, 0, 0, 0),
        XmlDateTime(2004, 1, 1, 12, 0, 0, 0, 0),
        XmlDateTime(2005, 1, 1, 12, 0, 0, 123000000, -540),
        XmlDateTime(2006, 1, 1, 12, 0, 0, 123000000, 540),
    ],
    eld_time_stamp_enumeration=[
        DTimeStampEnumeration.VALUE_2000_01_01_T12_00_00_Z,
        DTimeStampEnumeration.VALUE_2001_01_01_T12_00_00_123_09_00,
    ],
    eld_time_stamp_pattern=[
        "2009-01-01T12:00:00.123-09:00",
    ],
    eld_time_stamp_min_max_inclusive=[
        XmlDateTime(2001, 1, 1, 12, 0, 0, 123000000, 540),
        XmlDateTime(2002, 1, 1, 12, 0, 0, 123000000, 540),
    ],
    eld_time_stamp_min_max_exclusive=[
        XmlDateTime(1998, 1, 1, 12, 0, 0, 124000000, 540),
        XmlDateTime(1999, 1, 1, 12, 0, 0, 122000000, 540),
    ]
)
