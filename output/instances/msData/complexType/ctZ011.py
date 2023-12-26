from output.models.ms_data.complex_type.ct_z011_xsd.ct_z011 import A
from output.models.ms_data.complex_type.ct_z011_xsd.ct_z011 import B
from xsdata.formats.dataclass.models.generics import AnyElement


obj = A(
    any_element=AnyElement(
        text='\n1242\n        ',
        children=[
            B(

            ),
        ],
        attributes={
            '{http://www.w3.org/2001/XMLSchema-instance}type': '{http://www.w3.org/2001/XMLSchema}anyType',
        }
    )
)
