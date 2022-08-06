from output.models.saxon_data.assert_pkg.assert_simple001_xsd.assert_simple001 import Outer
from xsdata.models.datatype import XmlDate


obj = Outer(
    date=[
        XmlDate(2001, 1, 1),
        XmlDate(1999, 11, 16, 60),
        XmlDate(1066, 3, 3),
    ]
)
