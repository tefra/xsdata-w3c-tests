from output.models.saxon_data.wild.wild082_xsd.wild082 import Root
from output.models.saxon_data.wild.wild082_xsd.wild082 import Zz
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    a=Zz(
        value="42",
        type_value=1
    ),
    local_element=AnyElement(
        qname="a",
        text="93.7",
        attributes={
            "type": "2",
        }
    )
)
