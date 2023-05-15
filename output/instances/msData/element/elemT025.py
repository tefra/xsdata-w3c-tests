from output.models.ms_data.element.elem_t025_xsd.elem_t025 import ECa
from output.models.ms_data.element.elem_t025_xsd.elem_t025 import Root
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Root(
    test2=DerivedElement(
        qname="test2",
        value=ECa(
            x=[
                "",
            ],
            y="",
            z=""
        ),
        type="E-CA"
    )
)
