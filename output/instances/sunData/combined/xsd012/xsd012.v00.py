from output.models.sun_data.combined.xsd012.xsd012_xsd.xsd012 import A
from output.models.sun_data.combined.xsd012.xsd012_xsd.xsd012 import B
from output.models.sun_data.combined.xsd012.xsd012_xsd.xsd012 import C
from output.models.sun_data.combined.xsd012.xsd012_xsd.xsd012 import Root
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Root(
    mixed_or_element_only=[
        Root.Mixed(
            content=[
                "&#10;&#9;&#9;abcdef&#10;&#9;",
            ]
        ),
        Root.Mixed(
            content=[
                DerivedElement(
                    qname="{foo}a",
                    value=A(
                        any_element=AnyElement(
                            qname=None,
                            text=None,
                            tail=" mi ",
                            children=[],
                            attributes={}
                        )
                    ),
                    type=None
                ),
                DerivedElement(
                    qname="{foo}b",
                    value=B(
                        any_element=AnyElement(
                            qname=None,
                            text=None,
                            tail=" xed ",
                            children=[],
                            attributes={}
                        )
                    ),
                    type=None
                ),
                DerivedElement(
                    qname="{foo}c",
                    value=C(
                        any_element=AnyElement(
                            qname=None,
                            text=None,
                            tail=" content&#10;&#9;",
                            children=[],
                            attributes={}
                        )
                    ),
                    type=None
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
