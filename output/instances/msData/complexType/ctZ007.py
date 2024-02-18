from output.models.ms_data.complex_type.ct_z007_a_xsd import Address
from output.models.ms_data.complex_type.ct_z007_a_xsd import City
from output.models.ms_data.complex_type.ct_z007_a_xsd import Customers
from output.models.ms_data.complex_type.ct_z007_a_xsd import FirstName
from output.models.ms_data.complex_type.ct_z007_a_xsd import LastName
from output.models.ms_data.complex_type.ct_z007_a_xsd import MyCustomer
from output.models.ms_data.complex_type.ct_z007_a_xsd import PhoneNumber
from output.models.ms_data.complex_type.ct_z007_a_xsd import State
from output.models.ms_data.complex_type.ct_z007_a_xsd import Zip


obj = Customers(
    my_customer=[
        MyCustomer(
            first_name=FirstName(
                value='Dare'
            ),
            last_name=LastName(
                value='Obasanjo'
            ),
            customer_id=12345,
            phone_number=PhoneNumber(
                value='425-555-1234'
            ),
            address=Address(
                value='2001'
            ),
            city=City(
                value='Redmond'
            ),
            state=State(

            ),
            zip=Zip(
                value='98052'
            )
        ),
    ]
)
