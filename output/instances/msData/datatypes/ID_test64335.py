from decimal import Decimal
from output.models.ms_data.datatypes.id_test64335_xsd.id_test64335 import Apparel
from output.models.ms_data.datatypes.id_test64335_xsd.id_test64335 import Book
from output.models.ms_data.datatypes.id_test64335_xsd.id_test64335 import Cd
from output.models.ms_data.datatypes.id_test64335_xsd.id_test64335 import Dvd
from output.models.ms_data.datatypes.id_test64335_xsd.id_test64335 import Products
from xsdata.models.datatype import XmlDate


obj = Products(
    choice=[
        Apparel(
            price=Decimal('32.11'),
            description='Nice pink crew-neck t-shirt.',
            id='cl101',
            size='M',
            style='T'
        ),
        Cd(
            price=Decimal('44.95'),
            description='An in-depth look at creating applications with\n      XML.',
            id='cd101',
            title="XML Developer's Guide",
            category='Computer',
            artist='Gambardella, Matthew',
            release_date=XmlDate(2000, 10, 1)
        ),
        Book(
            price=Decimal('44.95'),
            description='An in-depth look at creating applications with\n      XML.',
            id='bk101',
            title="XML Developer's Guide",
            category='Computer',
            author='Gambardella, Matthew',
            publish_date=XmlDate(2000, 10, 1)
        ),
        Dvd(
            price=Decimal('23.95'),
            description='Two fellow travellers hook up and engage in mad-cap tomfoolery while stowaways on a British Merchant ship filled with anxious limeys.',
            id='dvd102',
            title='Adventures of John Dong and Don Gill',
            category='Foreign',
            director='Hancock, Trevor',
            release_date=XmlDate(2000, 10, 1)
        ),
    ]
)
