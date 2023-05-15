from output.models.saxon_data.wild.wild062_xsd.wild062 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.models.datatype import XmlDate


obj = Doc(
    e=XmlDate(2008, 11, 3),
    f="",
    local_element=AnyElement(
        qname="g",
        text="12:20:02"
    )
)
