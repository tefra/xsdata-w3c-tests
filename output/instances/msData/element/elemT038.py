from output.models.ms_data.element.elem_t038_xsd.elem_t038 import RCa
from output.models.ms_data.element.elem_t038_xsd.elem_t038 import Root
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Root(
    s_a_or_test=None,
    test2=None,
    test3=DerivedElement(
        qname="test3",
        value=RCa(
            x=[
                "",
            ],
            y=None
        ),
        type="R-CA"
    )
)
