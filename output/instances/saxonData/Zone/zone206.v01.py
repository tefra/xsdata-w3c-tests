from output.models.saxon_data.zone.zone206_xsd.zone206 import Doc
from xsdata.models.datatype import XmlTime


obj = Doc(
    target=XmlTime(2, 0, 0, 0, -300),
    equiv=[
        XmlTime(7, 0, 0, 0, 0),
        XmlTime(7, 0, 0, 0, 0),
    ]
)
