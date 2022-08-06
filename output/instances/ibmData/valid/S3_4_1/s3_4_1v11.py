from decimal import Decimal
from output.models.ibm_data.valid.s3_4_1.s3_4_1v11_xsd.s3_4_1v11 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    version=Decimal("1.0"),
    content=[
        "&#10;&#9;&#9;123abc12133b&#10;&#9;&#9;",
        AnyElement(
            qname="{a}element",
            text="xk",
            tail=None,
            children=[],
            attributes={}
        ),
    ]
)
