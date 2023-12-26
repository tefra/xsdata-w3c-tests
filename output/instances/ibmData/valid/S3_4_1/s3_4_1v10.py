from output.models.ibm_data.valid.s3_4_1.s3_4_1v10_xsd.s3_4_1v10 import D
from output.models.ibm_data.valid.s3_4_1.s3_4_1v10_xsd.s3_4_1v10 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    p=D(
        any_element=AnyElement(
            qname='qwe',
            text='asd'
        ),
        x=1,
        y=2,
        z=0
    )
)
