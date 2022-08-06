from output.models.ms_data.identity_constraint.id_k010_xsd.id_k010 import Kid
from output.models.ms_data.identity_constraint.id_k010_xsd.id_k010 import Root
from output.models.ms_data.identity_constraint.id_k010_xsd.id_k010 import Uid


obj = Root(
    uid=[
        Uid(
            elem="1",
            val=None
        ),
        Uid(
            elem="11",
            val=None
        ),
        Uid(
            elem="111",
            val=None
        ),
        Uid(
            elem="1.0",
            val=None
        ),
    ],
    kid=[
        Kid(
            elem="1",
            val=None
        ),
        Kid(
            elem="11",
            val=None
        ),
        Kid(
            elem="111",
            val=None
        ),
        Kid(
            elem="1.0",
            val=None
        ),
    ]
)
