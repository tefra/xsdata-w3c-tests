from output.models.ms_data.identity_constraint.id_h023_xsd.id_h023 import Kid
from output.models.ms_data.identity_constraint.id_h023_xsd.id_h023 import Root
from output.models.ms_data.identity_constraint.id_h023_xsd.id_h023 import Uidtype


obj = Root(
    uid=[
        Uidtype(
            iid=Uidtype.Iid(
                val='1'
            )
        ),
        Uidtype(
            iid=Uidtype.Iid(
                val='11'
            )
        ),
        Uidtype(
            iid=Uidtype.Iid(
                val='111'
            )
        ),
        Uidtype(
            iid=Uidtype.Iid(
                val='1.0'
            )
        ),
    ],
    kid=[
        Kid(
            val='1'
        ),
        Kid(
            val='11'
        ),
        Kid(
            val='111'
        ),
        Kid(
            val='1.0'
        ),
    ]
)
