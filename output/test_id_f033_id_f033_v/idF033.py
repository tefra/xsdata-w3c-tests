from output.models.ms_data.identity_constraint.id_f033_xsd.id_f033 import Root
from output.models.ms_data.identity_constraint.id_f033_xsd.id_f033 import T
from output.models.ms_data.identity_constraint.id_f033_xsd.id_f033a import R


obj = Root(
    t=[
        T(
            r=R(
                val2='a',
                content=[
                    ' 1 ',
                ]
            ),
            val='1'
        ),
        T(
            r=R(
                val2='b',
                content=[
                    ' 2 ',
                ]
            ),
            val='2'
        ),
        T(
            r=R(
                val2='c',
                content=[
                    ' 3 ',
                ]
            ),
            val='3'
        ),
    ]
)
