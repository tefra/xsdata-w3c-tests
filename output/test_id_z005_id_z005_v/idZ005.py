from output.models.ms_data.identity_constraint.id_z005_xsd.id_z005 import AType
from output.models.ms_data.identity_constraint.id_z005_xsd.id_z005 import BType
from output.models.ms_data.identity_constraint.id_z005_xsd.id_z005 import BsType
from output.models.ms_data.identity_constraint.id_z005_xsd.id_z005 import Root


obj = Root(
    a=[
        AType(
            bs=BsType(
                b=BType(
                    att_b='a'
                )
            ),
            c=[
                '',
            ],
            att_a='a'
        ),
    ]
)
