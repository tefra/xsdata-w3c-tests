from output.models.saxon_data.wild.wild104_xsd.wild104 import Doc
from output.models.saxon_data.wild.wild104_xsd.wild104 import Note
from output.models.saxon_data.wild.wild104_xsd.wild104 import P
from output.models.saxon_data.wild.wild104_xsd.wild104 import Wrapper
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
                    ]
                ),
            ]
        ),
    ]
)
