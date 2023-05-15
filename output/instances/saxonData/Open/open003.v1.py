from output.models.saxon_data.open.open003_xsd.open003 import Doc
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    a="",
    b="",
    local_com_element=AnyElement(
        qname="{http://local.com/}extra",
        text="42"
    )
)
