from output.models.saxon_data.wild.wild066_xsd.wild066 import Doc
from output.models.saxon_data.wild.wild066_xsd.wild066 import E
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlTime


obj = Doc(
    e=XmlTime(12, 12, 0, 0),
    f=42,
    local_element=E(
        value=XmlDate(2008, 11, 2)
    )
)
