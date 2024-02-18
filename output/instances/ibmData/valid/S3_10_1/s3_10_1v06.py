from output.models.ibm_data.valid.s3_10_1.s3_10_1v06_xsd.s3_10_1v06 import B
from output.models.ibm_data.valid.s3_10_1.s3_10_1v06_xsd.s3_10_1v06 import C
from output.models.ibm_data.valid.s3_10_1.s3_10_1v06_xsd.s3_10_1v06 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    d_or_b=B(
        value=1
    ),
    any_element=[
        AnyElement(
            qname='{a}x',
            text='1'
        ),
    ],
    c=C(
        value=1
    )
)
