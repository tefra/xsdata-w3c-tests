from output.models.ms_data.additional.test78898_xsd.test78898 import E6
from output.models.ms_data.additional.test78898_xsd.test78898 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    e1=None,
    e2=None,
    e3=[],
    e4=[],
    e5=[],
    e6=[
        E6(
            any_element=[
                AnyElement(
                    qname="e3",
                    text="",
                    tail=None,
                    children=[],
                    attributes={}
                ),
            ],
            att=None
        ),
    ],
    e7=[],
    e8=[]
)
