from output.models.ms_data.additional.test75092_xsd.test75092 import Foo
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Foo(
    a="",
    any_element=[
        DerivedElement(
            qname="b",
            value="abc",
            type=None
        ),
        DerivedElement(
            qname="c",
            value=123,
            type=None
        ),
    ]
)
