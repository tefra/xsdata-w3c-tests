from output.models.ms_data.wildcards.wild_g018_xsd.wild_g018 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Foo(
    other_element=AnyElement(
        qname='{http://bar}bar',
        text='foo bar'
    )
)
