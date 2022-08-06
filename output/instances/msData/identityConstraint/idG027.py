from output.models.ms_data.identity_constraint.id_g027_xsd.id_g027 import Root
from output.models.ms_data.identity_constraint.id_g027_xsd.id_g027 import T
from output.models.ms_data.identity_constraint.id_g027_xsd.id_g027a import R


obj = Root(
    t=[
        T(
            r=R(
                val2="a",
                content=[
                    " 1 ",
                ]
            ),
            val="1"
        ),
        T(
            r=R(
                val2="b",
                content=[
                    " 2 ",
                ]
            ),
            val="2"
        ),
        T(
            r=R(
                val2="c",
                content=[
                    " 3 ",
                ]
            ),
            val="3"
        ),
    ]
)
