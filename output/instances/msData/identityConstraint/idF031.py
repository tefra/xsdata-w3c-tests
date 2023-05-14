from output.models.ms_data.identity_constraint.id_f031_xsd.id_f031 import Root
from output.models.ms_data.identity_constraint.id_f031_xsd.id_f031 import T
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Root(
    t=[
        T(
            r2_or_r=DerivedElement(
                qname="r",
                value=" 1 ",
                type=None
            )
        ),
        T(
            r2_or_r=" 2 "
        ),
        T(
            r2_or_r=DerivedElement(
                qname="r",
                value=" 3 ",
                type=None
            )
        ),
        T(
            r2_or_r=" 4 "
        ),
    ]
)
