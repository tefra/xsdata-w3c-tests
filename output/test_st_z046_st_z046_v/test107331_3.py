from output.models.ms_data.simple_type.test107331_d_xsd.test107331_d import A
from output.models.ms_data.simple_type.test107331_d_xsd.test107331_d import B
from output.models.ms_data.simple_type.test107331_d_xsd.test107331_d import C
from output.models.ms_data.simple_type.test107331_d_xsd.test107331_d import D
from output.models.ms_data.simple_type.test107331_d_xsd.test107331_d import Root


obj = Root(
    choice=[
        A(
            value='12'
        ),
        B(
            value=-5.444
        ),
        C(
            value=[
                1.2,
                3.4,
                5.6,
                -7.9,
            ]
        ),
        D(
            value=[
                True,
            ]
        ),
        D(
            value=[
                2,
                3,
                4,
                5,
            ]
        ),
        D(
            value=[
                -1.5,
                6.8,
            ]
        ),
        D(
            value=[
                9,
            ]
        ),
    ]
)
