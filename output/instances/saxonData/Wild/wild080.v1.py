from output.models.saxon_data.wild.wild080_xsd.wild080 import Root
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.models.datatype import XmlDate


obj = Root(
    a=XmlDate(2010, 10, 16),
    local_element=AnyElement(
        qname='a',
        text='42'
    )
)
