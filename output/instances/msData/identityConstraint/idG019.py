from output.models.ms_data.identity_constraint.id_g019_xsd.id_g019 import Root
from output.models.ms_data.identity_constraint.id_g019_xsd.id_g019 import T


obj = Root(
    t=[
        T(
            r=" 1 ",
            c=Tabletype.C(
                val="1",
                content=[
                    " 1 ",
                ]
            )
        ),
        T(
            r=" 2 ",
            c=Tabletype.C(
                val="2",
                content=[
                    " 2 ",
                ]
            )
        ),
        T(
            r=" 3 ",
            c=Tabletype.C(
                val="3",
                content=[
                    " 3 ",
                ]
            )
        ),
    ]
)
