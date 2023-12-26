from decimal import Decimal
from output.models.ibm_data.valid.s3_4_1.s3_4_1v11_xsd.s3_4_1v11 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    version=Decimal('1.0'),
    content=[
        '\n\t\t123abc12133b\n\t\t',
        AnyElement(
            qname='{a}element',
            text='xk'
        ),
        '\n\t\t23123124noifew\n',
    ]
)
