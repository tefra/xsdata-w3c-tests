from output.models.saxon_data.override.over030_xsd.over030a import Doc
from output.models.saxon_data.override.over030_xsd.over030a import Emphasis
from output.models.saxon_data.override.over030_xsd.over030a import P
from output.models.saxon_data.override.over030_xsd.over030a import Title
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Doc(
    title=Title(
        role=None,
        id=None,
        base=None,
        content=[
            "Document Title",
        ]
    ),
    xsdextra=None,
    p_or_blockquote=[
        P(
            role=None,
            id=None,
            base=None,
            content=[
                "This is some ",
                DerivedElement(
                    qname="{http://example.org/ns/document}emphasis",
                    value=Emphasis(
                        role=None,
                        id=None,
                        base=None,
                        content=[
                            "text",
                            ".",
                        ]
                    ),
                    type=None
                ),
            ]
        ),
    ],
    role=None,
    id=None,
    base=None
)
