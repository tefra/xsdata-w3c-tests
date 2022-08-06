from output.models.ms_data.wildcards.wild_i004_xsd.wild_i004 import Elt1
from output.models.ms_data.wildcards.wild_i004_xsd.wild_i004 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    elt1=[
        Elt1(
            any_element=[
                AnyElement(
                    qname="elt2",
                    text="name",
                    tail=None,
                    children=[],
                    attributes={}
                ),
            ]
        ),
    ]
)
