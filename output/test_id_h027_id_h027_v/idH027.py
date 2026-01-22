from output.models.ms_data.identity_constraint.id_h027_xsd.id_h027 import Kid
from output.models.ms_data.identity_constraint.id_h027_xsd.id_h027 import Root
from output.models.ms_data.identity_constraint.id_h027_xsd.id_h027 import Uidtype
from output.models.ms_data.identity_constraint.id_h027_xsd.id_h027_imp import Iid


obj = Root(
    uid=[
        Uidtype(
            iid=Iid(
                value='1'
            )
        ),
        Uidtype(
            iid=Iid(
                value='11'
            )
        ),
        Uidtype(
            iid=Iid(
                value='111'
            )
        ),
        Uidtype(
            iid=Iid(
                value='1.0'
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
