from output.models.ms_data.wildcards.wild_g010_xsd.wild_g010 import Foo
from output.models.ms_data.wildcards.wild_g010_xsd.wild_g010b_imp import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Foo(
    local_w3_org_1999_xhtml_element=[
        AnyElement(
            qname='bar',
            text='test'
        ),
        Foo(
            any_element=AnyElement(
                text='test'
            )
        ),
        AnyElement(
            qname='bar',
            text='test'
        ),
        Foo(
            any_element=AnyElement(
                text='test'
            )
        ),
        AnyElement(
            qname='bar',
            text='test'
        ),
        Foo(
            any_element=AnyElement(
                text='test'
            )
        ),
        AnyElement(
            qname='bar',
            text='test'
        ),
        Foo(
            any_element=AnyElement(
                text='test'
            )
        ),
        AnyElement(
            qname='bar',
            text='test'
        ),
        Foo(
            any_element=AnyElement(
                text='test'
            )
        ),
    ]
)
