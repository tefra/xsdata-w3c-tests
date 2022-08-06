from output.models.saxon_data.assert_pkg.assert_simple006_xsd.assert_simple006 import Outer
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime


obj = Outer(
    value=[
        XmlDate(2008, 6, 11),
        XmlDateTime(2008, 6, 12, 12, 0, 0),
        XmlDate(2008, 6, 13, 0),
        XmlDateTime(2008, 6, 14, 13, 13, 13, 130000000, 60),
    ]
)
