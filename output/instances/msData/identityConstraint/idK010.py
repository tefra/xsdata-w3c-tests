from output.models.ms_data.identity_constraint.id_k010_xsd.id_k010 import Kid
from output.models.ms_data.identity_constraint.id_k010_xsd.id_k010 import Root
from output.models.ms_data.identity_constraint.id_k010_xsd.id_k010 import Uid


obj = Root(
    uid=[
        Uid(
            elem='1'
        ),
        Uid(
            elem='11'
        ),
        Uid(
            elem='111'
        ),
        Uid(
            elem='1.0'
        ),
    ],
    kid=[
        Kid(
            elem='1'
        ),
        Kid(
            elem='11'
        ),
        Kid(
            elem='111'
        ),
        Kid(
            elem='1.0'
        ),
    ]
)
