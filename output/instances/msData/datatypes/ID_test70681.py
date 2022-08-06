from output.models.ms_data.datatypes.datatypes_xsd.datatypes import Data
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Data(
    any_element=AnyElement(
        qname="item",
        text="",
        tail=None,
        children=[],
        attributes={
            "SOMITEM_DATATYPE_ID": " id ",
        }
    )
)
