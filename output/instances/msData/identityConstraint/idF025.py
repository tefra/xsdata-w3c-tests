from output.models.ms_data.identity_constraint.id_f025_xsd.id_f025 import Root
from output.models.ms_data.identity_constraint.id_f025_xsd.id_f025 import T
from output.models.ms_data.identity_constraint.id_f025_xsd.id_f025 import Tabletype


obj = Root(
    t=[
        T(
            r=' 1 ',
            c=Tabletype.C(
                val='1',
                content=[
                    ' 1 ',
                ]
            )
        ),
        T(
            r=' 2 ',
            c=Tabletype.C(
                val='2',
                content=[
                    ' 2 ',
                ]
            )
        ),
        T(
            r=' 3 ',
            c=Tabletype.C(
                val='3',
                content=[
                    ' 3 ',
                ]
            )
        ),
    ]
)
