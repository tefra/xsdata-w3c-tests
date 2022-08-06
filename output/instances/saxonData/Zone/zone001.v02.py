from output.models.saxon_data.zone.zone001_xsd.zone001 import Doc
from xsdata.models.datatype import XmlTime


obj = Doc(
    value=XmlTime(12, 20, 0, 0, 0)
)
