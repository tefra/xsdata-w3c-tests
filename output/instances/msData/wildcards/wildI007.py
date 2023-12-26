from output.models.ms_data.wildcards.wild_i007_xsd.wild_i007 import Bar
from output.models.ms_data.wildcards.wild_i007_xsd.wild_i007 import Foo
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Foo(
    other_element_or_target_namespace_element=[
        AnyElement(
            qname='{a}b',
            text='test'
        ),
        AnyElement(
            qname='{b}b',
            text='test'
        ),
        Bar(
            any_element=AnyElement(
                text='test'
            )
        ),
        AnyElement(
            qname='{other}local',
            text=''
        ),
        AnyElement(
            qname='{a}b',
            text='test'
        ),
        AnyElement(
            qname='{b}b',
            text='test'
        ),
        Bar(
            any_element=AnyElement(
                text='test'
            )
        ),
        AnyElement(
            qname='{other}local',
            text=''
        ),
    ]
)
