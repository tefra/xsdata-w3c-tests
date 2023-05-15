from output.models.ms_data.identity_constraint.id_h026_xsd.id_h026 import Kid
from output.models.ms_data.identity_constraint.id_h026_xsd.id_h026 import Root
from output.models.ms_data.identity_constraint.id_h026_xsd.id_h026 import Uidtype
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    uid=[
        Uidtype(
            any_element=AnyElement(
                qname="{fooNS.tempuri.org}a",
                text="1"
            )
        ),
        Uidtype(
            any_element=AnyElement(
                qname="{fooNS.tempuri.org}a",
                text="11"
            )
        ),
        Uidtype(
            any_element=AnyElement(
                qname="{fooNS.tempuri.org}a",
                text="111"
            )
        ),
        Uidtype(
            any_element=AnyElement(
                qname="{fooNS.tempuri.org}a",
                text="11.0"
            )
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
