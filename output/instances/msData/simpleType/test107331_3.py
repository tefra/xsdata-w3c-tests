from output.models.ms_data.simple_type.test107331_d_xsd.test107331_d import Root
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Root(
    choice=[
        AnyElement(
            qname="a",
            text="12",
            tail=None,
            children=[],
            attributes={}
        ),
        DerivedElement(
            qname="b",
            value=-5.444,
            type=None
        ),
        DerivedElement(
            qname="c",
            value=[
                1.2,
                3.4,
                5.6,
                -7.9,
            ],
            type=None
        ),
        [
            True,
        ],
        [
            2,
            3,
            4,
            5,
        ],
        [
            -1.5,
            6.8,
        ],
        [
            9,
        ],
    ]
)
