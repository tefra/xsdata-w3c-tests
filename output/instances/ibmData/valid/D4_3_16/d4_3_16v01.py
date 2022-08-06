from output.models.ibm_data.valid.d4_3_16.d4_3_16v01_xsd.d4_3_16v01 import Root
from xsdata.models.datatype import XmlDateTime


obj = Root(
    el_dtime_type=[
        XmlDateTime(1999, 11, 23, 12, 0, 0, 123000000, 0),
    ],
    el_dtime_etprohibited=[
        XmlDateTime(2000, 11, 23, 12, 0, 0),
    ],
    el_dtime_etrequired=[
        XmlDateTime(2001, 11, 23, 12, 0, 0, 0, 0),
        XmlDateTime(2002, 11, 23, 12, 0, 0, 0, -300),
        XmlDateTime(2003, 11, 23, 12, 0, 0, 0, 300),
    ],
    el_dtime_etoptional=[
        XmlDateTime(2004, 11, 23, 12, 0, 0, 0, 0),
        XmlDateTime(2005, 11, 23, 12, 0, 0, 0, -300),
        XmlDateTime(2006, 11, 23, 12, 0, 0, 0, 300),
        XmlDateTime(2007, 11, 23, 12, 0, 0),
    ]
)
