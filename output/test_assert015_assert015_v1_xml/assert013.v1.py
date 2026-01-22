from output.models.saxon_data.assert_pkg.assert015_xsd.assert015 import Doc
from output.models.saxon_data.assert_pkg.assert015_xsd.assert015 import Temp
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime


obj = Doc(
    temp=[
        Temp(
            value=XmlDate(2008, 7, 1),
            event=XmlDateTime(2008, 7, 1, 12, 0, 0)
        ),
        Temp(
            value=XmlDate(2008, 7, 8),
            event=XmlDateTime(2008, 7, 8, 12, 0, 0)
        ),
        Temp(
            value=XmlDate(2030, 4, 1),
            event=XmlDateTime(2030, 4, 1, 12, 0, 0)
        ),
        Temp(
            value=XmlDate(2102, 1, 5),
            event=XmlDateTime(2102, 1, 5, 12, 0, 0)
        ),
    ]
)
