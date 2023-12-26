from output.models.ms_data.identity_constraint.id_g018_xsd.id_g018 import Root
from output.models.ms_data.identity_constraint.id_g018_xsd.id_g018 import T
from output.models.ms_data.identity_constraint.id_g018_xsd.id_g018a import R


obj = Root(
    t=[
        T(
            r=R(
                val='1',
                content=[
                    ' 1 ',
                ]
            ),
            val='1'
        ),
        T(
            r=R(
                val='2',
                content=[
                    ' 2 ',
                ]
            ),
            val='2'
        ),
        T(
            r=R(
                val='3',
                content=[
                    ' 3 ',
                ]
            ),
            val='3'
        ),
    ]
)
