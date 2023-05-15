from output.models.ibm_data.valid.s3_12.s3_12v09_xsd.s3_12v09 import AddressType
from output.models.ibm_data.valid.s3_12.s3_12v09_xsd.s3_12v09 import AddressTypeType
from output.models.ibm_data.valid.s3_12.s3_12v09_xsd.s3_12v09 import CountryType
from output.models.ibm_data.valid.s3_12.s3_12v09_xsd.s3_12v09 import Invoice
from output.models.ibm_data.valid.s3_12.s3_12v09_xsd.s3_12v09 import ItemType
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Invoice(
    item=[
        ItemType(
            address=[
                AddressType(
                    type=AddressTypeType.SHIPPING,
                    country=CountryType.US,
                    content=[
                        AnyElement(
                            qname="state",
                            text="Texas"
                        ),
                        AnyElement(
                            qname="currency",
                            text="USD"
                        ),
                        AnyElement(
                            qname="zip",
                            text="75244"
                        ),
                    ]
                ),
                AddressType(
                    type=AddressTypeType.BILLING,
                    country=CountryType.CAN,
                    content=[
                        AnyElement(
                            qname="province",
                            text="ON"
                        ),
                        AnyElement(
                            qname="currency",
                            text="CDN"
                        ),
                        AnyElement(
                            qname="postal",
                            text="M1V4K9"
                        ),
                    ]
                ),
            ]
        ),
        ItemType(
            address=[
                AddressType(
                    type=AddressTypeType.SHIPPING,
                    country=CountryType.CAN,
                    content=[
                        AnyElement(
                            qname="province",
                            text="ON"
                        ),
                        AnyElement(
                            qname="currency",
                            text="CDN"
                        ),
                        AnyElement(
                            qname="postal",
                            text="L3S3H6"
                        ),
                    ]
                ),
                AddressType(
                    type=AddressTypeType.BILLING,
                    country=CountryType.CAN,
                    content=[
                        AnyElement(
                            qname="province",
                            text="ON"
                        ),
                        AnyElement(
                            qname="currency",
                            text="CDN"
                        ),
                        AnyElement(
                            qname="postal",
                            text="M3F2W5"
                        ),
                    ]
                ),
            ]
        ),
    ]
)
