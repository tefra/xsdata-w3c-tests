from output.models.saxon_data.simple.simple016_xsd.simple016 import Book
from output.models.saxon_data.simple.simple016_xsd.simple016 import Doc
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlTime


obj = Book(
    doc=[
        Doc(
            chap=[
                XmlDate(2010, 10, 12, 0),
            ]
        ),
        Doc(
            chap=[
                XmlDateTime(2010, 10, 12, 13, 13, 13, 0, 0),
            ]
        ),
        Doc(
            chap=[
                XmlTime(18, 18, 18, 0, 0),
            ]
        ),
    ]
)
