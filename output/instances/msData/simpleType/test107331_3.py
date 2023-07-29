from output.models.ms_data.simple_type.test107331_d_xsd.test107331_d import A
from output.models.ms_data.simple_type.test107331_d_xsd.test107331_d import Root
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Root(
    choice=[
        A(
            value="12"
        ),
        DerivedElement(
            qname="b",
            value=-5.444
        ),
        DerivedElement(
            qname="c",
            value=[
                1.2,
                3.4,
                5.6,
                -7.9,
            ]
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
