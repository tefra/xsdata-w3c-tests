from output.models.ibm_data.valid.d3_4_28.d3_4_28v04_xsd.d3_4_28v04 import Root
from xsdata.models.datatype import XmlDateTime


obj = Root(
    eld_time_stamp_union_a=[
        'Computer',
        XmlDateTime(1999, 2, 2, 2, 0, 0, 123000000, 0),
    ],
    eld_time_stamp_union_b=[
        XmlDateTime(1999, 2, 2, 2, 0, 0, 123000000, 0),
        7,
    ],
    eld_time_stamp_union_c=[
        '2000-02-02T02:00:00.123Z',
        '1',
        'once',
    ]
)
