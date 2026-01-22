from output.models.saxon_data.wild.wild102_xsd.wild102 import Doc
from output.models.saxon_data.wild.wild102_xsd.wild102 import Note
from output.models.saxon_data.wild.wild102_xsd.wild102 import P
from output.models.saxon_data.wild.wild102_xsd.wild102 import Wrapper
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    note_or_wrapper=[
        Note(
            p=[
                P(
                    content=[
                        'A paragraph in note.',
                    ]
                ),
            ],
            id='note1'
        ),
        Note(
            p=[
                P(
                    content=[
                        'A paragraph in note.',
                    ]
                ),
            ],
            id='note2'
        ),
        Wrapper(
            content=[
                '\n    Any ',
                AnyElement(
                    qname='{http://example.com/sample}stuff',
                    text='',
                    tail=' can go here, even a note:\n     '
                ),
                Note(
                    p=[
                        P(
                            content=[
                                'Some stuff',
                            ]
                        ),
                    ],
                    id='note3'
                ),
            ]
        ),
    ]
)
