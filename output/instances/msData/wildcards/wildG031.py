from output.models.ms_data.wildcards.wild_g031_xsd.wild_g031 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Foo(
    a_b_c_d_e_target_namespace_local_element=[
        AnyElement(
            qname="{http://foobar}bar",
            text="foo bar"
        ),
        AnyElement(
            qname="bar",
            text="foo bar"
        ),
        AnyElement(
            qname="foo",
            text=""
        ),
        AnyElement(
            qname="{A}foo",
            text=""
        ),
        AnyElement(
            qname="{B}foo",
            text=""
        ),
        AnyElement(
            qname="{C}foo",
            text=""
        ),
        AnyElement(
            qname="{D}foo",
            text=""
        ),
        AnyElement(
            qname="{E}foo",
            text=""
        ),
    ]
)
