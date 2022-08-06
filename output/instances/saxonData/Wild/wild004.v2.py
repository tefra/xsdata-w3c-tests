from output.models.saxon_data.wild.wild004_xsd.wild004 import Eden
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Eden(
    any_element=AnyElement(
        qname="{http://eden.com/}adam",
        text="eve",
        tail=None,
        children=[],
        attributes={}
    )
)
