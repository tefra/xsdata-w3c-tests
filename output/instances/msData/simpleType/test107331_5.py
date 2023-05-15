from output.models.ms_data.simple_type.test107331_h_xsd.test107331_h import Item
from output.models.ms_data.simple_type.test107331_h_xsd.test107331_h import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    a_or_item=[
        Item(
            any_element=AnyElement(
                text=" kjhad 254 987 lnfa "
            )
        ),
        AnyElement(
            qname="a",
            text="123456"
        ),
        AnyElement(
            qname="a",
            text="abcdefgh"
        ),
    ]
)
