from output.models.saxon_data.override.over010_xsd.over010a import Doc
from xsdata.models.datatype import XmlDate


obj = Doc(
    para=[
        XmlDate(2012, 1, 1),
    ]
)
