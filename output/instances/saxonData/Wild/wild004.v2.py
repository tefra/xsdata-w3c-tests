from output.models.saxon_data.wild.wild006_xsd.wild006 import Eden
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Eden(
    any_element=AnyElement(
        qname='{http://eden.com/}adam',
        text='eve'
    )
)
