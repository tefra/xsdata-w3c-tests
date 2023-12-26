from output.models.ibm_data.valid.d3_4_6.d3_4_6v06_xsd.d3_4_6v06 import Root
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Root(
    choice=[
        DerivedElement(
            qname='{a}_-',
            value='_-'
        ),
    ]
)
