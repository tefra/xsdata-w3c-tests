from output.models.ms_data.element.elem_r005_xsd.elem_r005 import PurchaseOrder
from output.models.ms_data.element.elem_r005_xsd.elem_r005 import Usaddress


obj = PurchaseOrder(
    ship_to=Usaddress(
        name="Alice Smith",
        street="123 Maple Street",
        country="US"
    ),
    bill_to=Usaddress(
        name="Robert Smith",
        street="8 Oak Avenue",
        country="US"
    ),
    comment="Hurry, my lawn is going wild!"
)