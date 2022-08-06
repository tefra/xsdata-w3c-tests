from output.models.ibm_data.valid.d4_3_16.d4_3_16v04_xsd.d4_3_16v04 import Root
from xsdata.models.datatype import XmlDateTime


obj = Root(
    eld_time_union_a=[
        XmlDateTime(1999, 10, 12, 12, 0, 0, 0, 0),
        XmlDateTime(2000, 10, 12, 12, 0, 0, 0, -300),
        XmlDateTime(2001, 10, 12, 12, 0, 0, 0, 300),
        "2002-10-12T12:00:00-5:00",
    ],
    eld_time_union_b=[
        XmlDateTime(2003, 10, 12, 12, 0, 0),
        2004,
    ],
    eld_time_union_c=[
        XmlDateTime(2005, 10, 12, 12, 0, 0, 0, 0),
        "2006-10-12T12:00:00+5:00",
        XmlDateTime(2007, 10, 12, 12, 0, 0, 0, 300),
        XmlDateTime(2008, 10, 12, 12, 0, 0, 0, -300),
        XmlDateTime(2009, 10, 12, 12, 0, 0),
        12345,
    ]
)
