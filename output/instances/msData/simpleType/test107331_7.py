from output.models.ms_data.simple_type.test107331_h_xsd.test107331_h import Item
from output.models.ms_data.simple_type.test107331_h_xsd.test107331_h import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    a=[],
    item=[
        Item(
            any_element=AnyElement(
                qname=None,
                text="abc",
                tail=None,
                children=[],
                attributes={}
            )
        ),
        Item(
            any_element=AnyElement(
                qname=None,
                text="abc",
                tail=None,
                children=[],
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}anySimpleType",
                }
            )
        ),
    ]
)
