from output.models.ms_data.identity_constraint.id_h028_xsd.id_h028 import Kid
from output.models.ms_data.identity_constraint.id_h028_xsd.id_h028 import Root
from output.models.ms_data.identity_constraint.id_h028_xsd.id_h028 import Uidtype


obj = Root(
    uid=[
        Uidtype(
            hid=None,
            iid="1"
        ),
        Uidtype(
            hid=None,
            iid="11"
        ),
        Uidtype(
            hid=None,
            iid="111"
        ),
        Uidtype(
            hid=None,
            iid="1.0"
        ),
    ],
    kid=[
        Kid(
            val="1"
        ),
        Kid(
            val="11"
        ),
        Kid(
            val="111"
        ),
        Kid(
            val="1.0"
        ),
    ]
)