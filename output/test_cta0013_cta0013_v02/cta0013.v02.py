from output.models.saxon_data.cta.cta0013_xsd.cta0013 import Chap
from output.models.saxon_data.cta.cta0013_xsd.cta0013 import Doc
from output.models.saxon_data.cta.cta0013_xsd.cta0013 import Part


obj = Doc(
    part=[
        Part(
            chap=[
                Chap(
                    de=''
                ),
            ],
            lang='fr'
        ),
        Part(
            chap=[
                Chap(
                    lang='fr',
                    fr=''
                ),
            ],
            lang='en'
        ),
    ],
    lang='de'
)
