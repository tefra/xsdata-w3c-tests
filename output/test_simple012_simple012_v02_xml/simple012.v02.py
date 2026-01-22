from output.models.saxon_data.simple.simple012_xsd.simple012 import Book
from output.models.saxon_data.simple.simple012_xsd.simple012 import Doc
from output.models.saxon_data.simple.simple012_xsd.simple012 import Subdoc
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlTime


obj = Book(
    subdoc_or_doc=[
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
        Subdoc(
            chap=[
                XmlDate(2010, 10, 12),
            ]
        ),
        Subdoc(
            chap=[
                XmlDateTime(2010, 11, 5, 12, 12, 12),
            ]
        ),
    ]
)
