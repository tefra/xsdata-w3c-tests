from output.models.saxon_data.assert_pkg.assert022_xsd.assert022 import Doc
from output.models.saxon_data.assert_pkg.assert022_xsd.assert022 import Temp
from xsdata.models.datatype import XmlDate


obj = Doc(
    temp=[
        Temp(
            d=XmlDate(2008, 7, 1)
        ),
        Temp(
            d=XmlDate(2010, 11, 17, 0)
        ),
    ]
)
