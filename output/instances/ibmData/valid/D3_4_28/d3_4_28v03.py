from output.models.ibm_data.valid.d3_4_28.d3_4_28v03_xsd.d3_4_28v03 import Root
from xsdata.models.datatype import XmlDateTime


obj = Root(
    eld_time_stamp_pattern="2000-01-01T12:00:00.123-09:00",
    eld_time_stamp_list_a=[
        [
            XmlDateTime(2001, 1, 1, 12, 0, 0, 123000000, -540),
            XmlDateTime(2002, 1, 1, 12, 0, 0, 0, 0),
        ],
    ],
    eld_time_stamp_list_b=[
        "2001-01-01T12:00:00.123-09:00",
        "2004-01-01T12:00:00.123Z",
        "2002-01-01T12:00:00.123+09:00",
    ],
    eld_time_stamp_list_c=[
        "2002-01-01T12:00:00.123-09:00",
        "2005-01-01T12:00:00.123-09:00",
        "2006-01-01T12:00:00.123-09:00",
    ]
)
