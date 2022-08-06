from output.models.saxon_data.assert_pkg.assert010_xsd.assert010 import Temp
from xsdata.models.datatype import XmlDate


obj = Temp(
    value=XmlDate(2008, 7, 1),
    start_date=XmlDate(2008, 6, 1)
)
