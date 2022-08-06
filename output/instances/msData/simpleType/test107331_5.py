from output.models.ms_data.simple_type.test107331_h_xsd.test107331_h import Item
from output.models.ms_data.simple_type.test107331_h_xsd.test107331_h import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    a=[
        "123456",
        "abcdefgh",
    ],
    item=[
        Item(
            any_element=AnyElement(
                qname=None,
                text=" kjhad 254 987 lnfa ",
                tail=None,
                children=[],
                attributes={}
            )
        ),
    ]
)
