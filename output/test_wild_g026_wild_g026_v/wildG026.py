from output.models.ms_data.wildcards.wild_g026_xsd.wild_g026 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Foo(
    other_element=AnyElement(
        qname='{http://bar}bar',
        text='foo bar'
    )
)
