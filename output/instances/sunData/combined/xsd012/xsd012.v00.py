from output.models.sun_data.combined.xsd012.xsd012_xsd.xsd012 import A
from output.models.sun_data.combined.xsd012.xsd012_xsd.xsd012 import B
from output.models.sun_data.combined.xsd012.xsd012_xsd.xsd012 import C
from output.models.sun_data.combined.xsd012.xsd012_xsd.xsd012 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    mixed_or_element_only=[
        Root.Mixed(
            content=[
                "&#10;&#9;&#9;abcdef&#10;&#9;",
            ]
        ),
        Root.Mixed(
            content=[
                A(
                    any_element=AnyElement(
                        qname=None,
                        text=None,
                        tail=" mi ",
                        children=[],
                        attributes={}
                    )
                ),
                B(
                    any_element=AnyElement(
                        qname=None,
                        text=None,
                        tail=" xed ",
                        children=[],
                        attributes={}
                    )
                ),
                C(
                    any_element=AnyElement(
                        qname=None,
                        text=None,
                        tail=" content&#10;&#9;",
                        children=[],
                        attributes={}
                    )
                ),
            ]
        ),
        Root.ElementOnly(
            a_or_b_or_c=[
                A(
                    any_element=None
                ),
                B(
                    any_element=None
                ),
                A(
                    any_element=None
                ),
            ]
        ),
    ]
)
