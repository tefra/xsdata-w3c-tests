from output.models.ibm_data.valid.s3_4_1.s3_4_1v07_xsd.s3_4_1v07 import D
from output.models.ibm_data.valid.s3_4_1.s3_4_1v07_xsd.s3_4_1v07 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    p=D(
        x=1,
        y=2,
        z=0,
        any_element=AnyElement(
            qname="asd",
            text="asd",
            tail=None,
            children=[],
            attributes={}
        )
    )
)
