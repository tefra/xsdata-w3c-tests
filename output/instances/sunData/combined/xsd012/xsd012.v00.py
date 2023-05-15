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
                        tail=" mi "
                    )
                ),
                B(
                    any_element=AnyElement(
                        tail=" xed "
                    )
                ),
                C(
                    any_element=AnyElement(
                        tail=" content&#10;&#9;"
                    )
                ),
            ]
        ),
        Root.ElementOnly(
            a_or_b_or_c=[
                A(

                ),
                B(

                ),
                A(

                ),
            ]
        ),
    ]
)
