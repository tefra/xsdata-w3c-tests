from output.models.ms_data.wildcards.wild_g031_xsd.wild_g031 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Foo(
    a_b_c_d_e_target_namespace_local_element=[
        AnyElement(
            qname="{http://foobar}bar",
            text="foo bar",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="bar",
            text="foo bar",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="foo",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="{A}foo",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="{B}foo",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="{C}foo",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="{D}foo",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
        AnyElement(
            qname="{E}foo",
            text="",
            tail=None,
            children=[],
            attributes={}
        ),
    ]
)
