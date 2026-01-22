from output.models.saxon_data.assert_pkg.assert_simple001_xsd.assert_simple001 import Date
from output.models.saxon_data.assert_pkg.assert_simple001_xsd.assert_simple001 import Outer
from xsdata.models.datatype import XmlDate


obj = Outer(
    date=[
        Date(
            value=XmlDate(2001, 1, 1)
        ),
        Date(
            value=XmlDate(1999, 11, 16, 60)
        ),
        Date(
            value=XmlDate(1066, 3, 3)
        ),
    ]
)
