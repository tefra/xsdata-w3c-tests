from output.models.saxon_data.override.over002_xsd.over002a import Doc
from xsdata.models.datatype import XmlDateTime


obj = Doc(
    para=[
        XmlDateTime(2001, 1, 1, 12, 0, 0),
    ]
)
