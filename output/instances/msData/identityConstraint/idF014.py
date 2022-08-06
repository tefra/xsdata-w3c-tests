from output.models.ms_data.identity_constraint.id_f014_xsd.id_f014 import Root
from output.models.ms_data.identity_constraint.id_f014_xsd.id_f014 import Uid
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
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}float",
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
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}unsignedByte",
                }
            )
        ),
    ]
)
