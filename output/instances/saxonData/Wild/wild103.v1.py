from output.models.saxon_data.wild.wild103_xsd.wild103 import Doc
from output.models.saxon_data.wild.wild103_xsd.wild103 import Note
from output.models.saxon_data.wild.wild103_xsd.wild103 import P
from output.models.saxon_data.wild.wild103_xsd.wild103 import Wrapper
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    note_or_wrapper=[
        Note(
            id='note1',
            p=[
                P(
                    content=[
                        'A paragraph in note.',
                    ]
                ),
            ]
        ),
        Note(
            id='note2',
            p=[
                P(
                    content=[
                        'A paragraph in note.',
                    ]
                ),
            ]
        ),
        Wrapper(
            content=[
                '\n    Any ',
                AnyElement(
                    qname='{http://example.com/sample}stuff',
                    text='',
                    tail=' can go here, even a note:\n     '
                ),
                AnyElement(
                    qname='{http://example.com/sample}not',
                    text='',
                    children=[
                        AnyElement(
                            qname='{http://example.com/sample}id',
                            text='note3'
                        ),
                        AnyElement(
                            qname='{http://example.com/sample}p',
                            text='Some stuff'
                        ),
                    ]
                ),
            ]
        ),
    ]
)
