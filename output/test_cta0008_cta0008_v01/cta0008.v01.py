from output.models.saxon_data.cta.cta0008_xsd.cta0008 import Example
from output.models.saxon_data.cta.cta0008_xsd.cta0008 import PublicationType
from xsdata.models.datatype import XmlPeriod


obj = Example(
    publication=[
        Example.KindBook(
            title='Illusions The Adventures of a Reluctant Messiah',
            author=[
                'Richard Bach',
            ],
            date=XmlPeriod("1977"),
            kind='book',
            isbn='0-440-34319-4',
            publisher='Dell Publishing Co.'
        ),
        PublicationType(
            title='Natural Health',
            date=XmlPeriod("1999"),
            kind='magazine'
        ),
        PublicationType(
            title='Time to Say Goodbye',
            author=[
                'Sarah Brightman',
            ],
            date=XmlPeriod("1997"),
            kind='CD'
        ),
    ]
)
