from output.models.saxon_data.zone.zone302_xsd.zone302 import Doc
from xsdata.models.datatype import XmlDuration


obj = Doc(
    target=XmlDuration("P2Y4M"),
    equiv=[
        XmlDuration("P28M"),
        XmlDuration("P01Y016M"),
    ]
)
