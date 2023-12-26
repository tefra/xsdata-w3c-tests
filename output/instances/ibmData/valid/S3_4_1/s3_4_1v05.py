from output.models.ibm_data.valid.s3_4_1.s3_4_1v05_xsd.s3_4_1v05 import D
from output.models.ibm_data.valid.s3_4_1.s3_4_1v05_xsd.s3_4_1v05 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    p=D(
        x=1,
        y=2,
        any_element=AnyElement(
            qname='z',
            text='sdf9873'
        )
    )
)
