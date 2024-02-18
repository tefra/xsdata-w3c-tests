from output.models.saxon_data.assert_pkg.assert_simple006_xsd.assert_simple006 import Outer
from output.models.saxon_data.assert_pkg.assert_simple006_xsd.assert_simple006 import Value
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime


obj = Outer(
    value=[
        Value(
            value=XmlDate(2008, 6, 11)
        ),
        Value(
            value=XmlDateTime(2008, 6, 12, 12, 0, 0)
        ),
        Value(
            value=XmlDate(2008, 6, 13, 0)
        ),
        Value(
            value=XmlDateTime(2008, 6, 14, 13, 13, 13, 130000000, 60)
        ),
    ]
)
