from output.models.saxon_data.zone.zone301_xsd.zone301 import Doc
from xsdata.models.datatype import XmlDuration


obj = Doc(
    target=XmlDuration("P1DT5H"),
    equiv=[
        XmlDuration("PT29H0M0.000S"),
        XmlDuration("P01DT300M"),
    ]
)
