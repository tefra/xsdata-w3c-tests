from output.models.saxon_data.simple.simple013_xsd.simple013 import Book
from output.models.saxon_data.simple.simple013_xsd.simple013 import Doc
from output.models.saxon_data.simple.simple013_xsd.simple013 import Subdoc
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlTime


obj = Book(
    subdoc=[
        Subdoc(
            chap=[
                XmlDate(2010, 10, 12),
            ]
        ),
    ],
    doc=[
        Doc(
            chap=[
                XmlDate(2010, 10, 12),
            ]
        ),
        Doc(
            chap=[
                XmlDateTime(2010, 10, 12, 13, 13, 13),
            ]
        ),
        Doc(
            chap=[
                XmlTime(18, 18, 18, 0),
            ]
        ),
    ]
)
