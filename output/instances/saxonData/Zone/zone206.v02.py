from output.models.saxon_data.zone.zone206_xsd.zone206 import Doc
from xsdata.models.datatype import XmlTime


obj = Doc(
    target=XmlTime(0, 0, 0, 0, 0),
    equiv=[
        XmlTime(5, 0, 0, 0, 300),
        XmlTime(24, 0, 0, 0, 0),
        XmlTime(24, 0, 0, 0, 0),
    ]
)
