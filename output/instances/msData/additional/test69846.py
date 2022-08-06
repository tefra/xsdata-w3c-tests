from output.models.ms_data.additional.test69846_xsd.test69846 import Root
from output.models.ms_data.additional.test69846_xsd.test69846 import Uid
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    uid=[
        Uid(
            any_element=AnyElement(
                qname=None,
                text="1",
                tail=None,
                children=[],
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}boolean",
                }
            )
        ),
        Uid(
            any_element=AnyElement(
                qname=None,
                text="1",
                tail=None,
                children=[],
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}decimal",
                }
            )
        ),
    ]
)
