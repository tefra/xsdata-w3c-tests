from output.models.ms_data.complex_type.ct_z007_a_xsd import Customers
from output.models.ms_data.complex_type.ct_z007_a_xsd import MyCustomer


obj = Customers(
    my_customer=[
        MyCustomer(
            first_name='Dare',
            last_name='Obasanjo',
            customer_id=12345,
            phone_number='425-555-1234',
            address='2001',
            city='Redmond',
            zip='98052'
        ),
    ]
)
