from output.models.ibm_data.valid.d4_3_16.d4_3_16v03_xsd.d4_3_16v03 import ElDtimeListOptional
from output.models.ibm_data.valid.d4_3_16.d4_3_16v03_xsd.d4_3_16v03 import ElDtimeListProhibited
from output.models.ibm_data.valid.d4_3_16.d4_3_16v03_xsd.d4_3_16v03 import ElDtimeListRequired
from output.models.ibm_data.valid.d4_3_16.d4_3_16v03_xsd.d4_3_16v03 import Root
from xsdata.models.datatype import XmlDateTime


obj = Root(
    el_dtime_et=XmlDateTime(1999, 10, 20, 10, 0, 0, 0, -300),
    el_dtime_list_required=ElDtimeListRequired(
        value=[
            XmlDateTime(1999, 10, 20, 10, 0, 0, 0, 0),
            XmlDateTime(2000, 10, 20, 10, 0, 0, 0, -300),
            XmlDateTime(2001, 10, 20, 10, 0, 0, 0, 300),
        ]
    ),
    el_dtime_list_prohibited=ElDtimeListProhibited(
        value=[
            XmlDateTime(2002, 10, 20, 10, 0, 0),
            XmlDateTime(2003, 10, 20, 10, 0, 0),
            XmlDateTime(2004, 10, 20, 10, 0, 0),
        ]
    ),
    el_dtime_list_optional=ElDtimeListOptional(
        value=[
            XmlDateTime(2005, 10, 20, 10, 0, 0, 0, 0),
            XmlDateTime(2006, 10, 20, 10, 0, 0, 0, -300),
            XmlDateTime(2007, 10, 20, 10, 0, 0, 0, 300),
            XmlDateTime(2008, 10, 20, 10, 0, 0),
        ]
    )
)
