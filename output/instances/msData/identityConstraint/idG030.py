from output.models.ms_data.identity_constraint.id_g030_xsd.id_g030 import Ctype2
from output.models.ms_data.identity_constraint.id_g030_xsd.id_g030 import Root
from output.models.ms_data.identity_constraint.id_g030_xsd.id_g030 import T


obj = Root(
    t=[
        T(
            c=Ctype2(
                content=[
                    ' 1 ',
                ],
                val2='1'
            )
        ),
        T(
            c=Ctype2(
                content=[
                    ' 2 ',
                ],
                val2='2'
            )
        ),
        T(
            c=Ctype2(
                content=[
                    ' 3 ',
                ],
                val2='3'
            )
        ),
    ]
)
