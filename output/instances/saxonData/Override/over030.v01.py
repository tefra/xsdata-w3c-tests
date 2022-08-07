from output.models.saxon_data.override.over030_xsd.over030a import Doc
from output.models.saxon_data.override.over030_xsd.over030a import Emphasis
from output.models.saxon_data.override.over030_xsd.over030a import P
from output.models.saxon_data.override.over030_xsd.over030a import Title


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
                Emphasis(
                    role=None,
                    id=None,
                    base=None,
                    content=[
                        "text",
                        ".",
                    ]
                ),
            ]
        ),
    ],
    role=None,
    id=None,
    base=None
)
