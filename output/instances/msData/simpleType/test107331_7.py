from output.models.ms_data.simple_type.test107331_h_xsd.test107331_h import Item
from output.models.ms_data.simple_type.test107331_h_xsd.test107331_h import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    a_or_item=[
        Item(
            any_element=AnyElement(
                text='abc'
            )
        ),
        Item(
            any_element=AnyElement(
                text='abc',
                attributes={
                    '{http://www.w3.org/2001/XMLSchema-instance}type': '{http://www.w3.org/2001/XMLSchema}anySimpleType',
                }
            )
        ),
    ]
)
