from output.models.saxon_data.zone.zone101_xsd.zone101 import Doc
from xsdata.models.datatype import XmlDateTime


obj = Doc(
    value=XmlDateTime(2008, 12, 20, 12, 20, 0, 0, -300)
)
