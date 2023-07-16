from output.models.saxon_data.zone.zone003_xsd.zone003 import Doc
from xsdata.models.datatype import XmlTime


obj = Doc(
    value=XmlTime(12, 20, 0, 0, -300)
)
