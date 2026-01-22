from output.models.ibm_data.valid.s3_4_1.s3_4_1v06_xsd.s3_4_1v06 import D
from output.models.ibm_data.valid.s3_4_1.s3_4_1v06_xsd.s3_4_1v06 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    p=D(
        x=1,
        y=2,
        z=1,
        any_element=AnyElement(
            qname='as',
            text='km'
        )
    )
)
