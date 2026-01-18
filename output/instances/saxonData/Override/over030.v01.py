from output.models.saxon_data.override.over030_xsd.over030a import Doc
from output.models.saxon_data.override.over030_xsd.over030a import Emphasis
from output.models.saxon_data.override.over030_xsd.over030a import P
from output.models.saxon_data.override.over030_xsd.over030a import Title


obj = Doc(
    title=Title(
        content=[
            'Document Title',
        ]
    ),
    p_or_blockquote=[
        P(
            content=[
                'This is some ',
                Emphasis(
                    content=[
                        'text',
                    ]
                ),
                '.',
            ]
        ),
    ]
)
