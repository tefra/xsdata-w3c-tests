from output.models.ms_data.identity_constraint.id_f012_xsd.id_f012 import Root
from output.models.ms_data.identity_constraint.id_f012_xsd.id_f012 import Uid
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    uid=[
        Uid(
            any_element=AnyElement(
                text='1',
                attributes={
                    '{http://www.w3.org/2001/XMLSchema-instance}type': '{http://www.w3.org/2001/XMLSchema}boolean',
                }
            )
        ),
        Uid(
            any_element=AnyElement(
                text='1',
                attributes={
                    '{http://www.w3.org/2001/XMLSchema-instance}type': '{http://www.w3.org/2001/XMLSchema}decimal',
                }
            )
        ),
    ]
)
