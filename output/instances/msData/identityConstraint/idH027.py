from output.models.ms_data.identity_constraint.id_h027_xsd.id_h027 import Kid
from output.models.ms_data.identity_constraint.id_h027_xsd.id_h027 import Root
from output.models.ms_data.identity_constraint.id_h027_xsd.id_h027 import Uidtype


obj = Root(
    uid=[
        Uidtype(
            iid='1'
        ),
        Uidtype(
            iid='11'
        ),
        Uidtype(
            iid='111'
        ),
        Uidtype(
            iid='1.0'
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
