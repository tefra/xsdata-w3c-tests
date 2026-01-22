from output.models.saxon_data.simple.simple010_xsd.simple010 import Book
from output.models.saxon_data.simple.simple010_xsd.simple010 import Doc
from output.models.saxon_data.simple.simple010_xsd.simple010 import Subdoc
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
                XmlDate(2010, 11, 5),
            ]
        ),
    ]
)
