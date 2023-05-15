from output.models.ms_data.wildcards.wild_i006_xsd.wild_i006 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Foo(
    choice=[
        AnyElement(
            qname="{a}b",
            text="test"
        ),
        AnyElement(
            qname="{b}b",
            text="test"
        ),
        AnyElement(
            qname="{http://xsdtesting}bar",
            text="test"
        ),
        AnyElement(
            qname="local",
            text=""
        ),
        AnyElement(
            qname="{a}b",
            text="test"
        ),
        AnyElement(
            qname="{b}b",
            text="test"
        ),
        AnyElement(
            qname="{http://xsdtesting}bar",
            text="test"
        ),
        AnyElement(
            qname="local",
            text=""
        ),
    ]
)
