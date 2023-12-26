from output.models.saxon_data.all.all006_xsd.all006 import C2
from output.models.saxon_data.all.all006_xsd.all006 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlTime


obj = Doc(
    a=XmlDate(1980, 1, 1),
    b=XmlTime(12, 0, 0, 0),
    target_namespace_element=AnyElement(
        children=[
            C2(
                value=XmlTime(12, 0, 0, 0)
            ),
            AnyElement(
                qname='{http://other.ns/}d',
                text='banana'
            ),
        ]
    )
)
