from output.models.ms_data.identity_constraint.id_h031_xsd.id_h031 import Kid
from output.models.ms_data.identity_constraint.id_h031_xsd.id_h031 import Root
from output.models.ms_data.identity_constraint.id_h031_xsd.id_h031 import Uidtype
from output.models.ms_data.identity_constraint.id_h031_xsd.id_h031_imp import Iid


obj = Root(
    uid=[
        Uidtype(
            iid=Iid(
                value='1',
                val='1'
            )
        ),
        Uidtype(
            iid=Iid(
                value='11',
                val='11'
            )
        ),
        Uidtype(
            iid=Iid(
                value='111',
                val='111'
            )
        ),
        Uidtype(
            iid=Iid(
                value='1.0',
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
