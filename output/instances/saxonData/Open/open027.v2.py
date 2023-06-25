<<<<<<< HEAD
from output.models.saxon_data.open.open028_xsd.open028 import Doc
=======
from output.models.saxon_data.open.open027_xsd.open027 import Doc
>>>>>>> 12d2caa18 (update xsdata)
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    a=[
        "",
    ],
    b="",
    c="",
    d="",
    open_com_element=AnyElement(
        qname="{http://open.com/}extra",
        text="42"
    )
)
