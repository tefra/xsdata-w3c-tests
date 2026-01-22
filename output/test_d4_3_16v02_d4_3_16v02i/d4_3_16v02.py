from output.models.ibm_data.valid.d4_3_16.d4_3_16v02_xsd.d4_3_16v02 import Root
from xsdata.models.datatype import XmlDateTime


obj = Root(
    attr_dtime_type=XmlDateTime(1999, 10, 23, 11, 59, 59, 0, -360),
    attr_dtime_type_et=XmlDateTime(2000, 10, 23, 11, 59, 59, 0, 0),
    attr_dtetprohibited=XmlDateTime(2001, 10, 23, 11, 59, 59),
    attr_dtetrequired=XmlDateTime(2002, 10, 23, 11, 59, 59, 0, 0),
    attr_dtetoptional=XmlDateTime(2008, 10, 23, 11, 59, 59, 0, 300)
)
