from output.models.saxon_data.wild.wild073_xsd.wild073 import A1
from output.models.saxon_data.wild.wild073_xsd.wild073 import Root
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Root(
    a_or_a="",
    b=None,
    c=None,
    any_element=[
        DerivedElement(
            qname="A",
            value=A1(
                any_element=None
            ),
            type=None
        ),
    ]
)
