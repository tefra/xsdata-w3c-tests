from output.models.ms_data.simple_type.test107331_j_xsd.test107331_j import Item
from output.models.ms_data.simple_type.test107331_j_xsd.test107331_j import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    choice=[
        Item(
            any_element=AnyElement(
                text="abc"
            )
        ),
        Item(
            any_element=AnyElement(
                text="123",
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}int",
                }
            )
        ),
        Item(
            any_element=AnyElement(
                text="4.56",
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}float",
                }
            )
        ),
        Item(
            any_element=AnyElement(
                text="this is a string",
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}string",
                }
            )
        ),
        Item(
            any_element=AnyElement(
                text="false",
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}boolean",
                }
            )
        ),
        Item(
            any_element=AnyElement(
                text="45",
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}decimal",
                }
            )
        ),
        Item(
            any_element=AnyElement(
                text="P1347Y",
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}duration",
                }
            )
        ),
        Item(
            any_element=AnyElement(
                text="1999-05-31T13:20:00-05:00",
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}dateTime",
                }
            )
        ),
        Item(
            any_element=AnyElement(
                text="13:20:00-05:00",
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}time",
                }
            )
        ),
        Item(
            any_element=AnyElement(
                text="1999-05-31",
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}date",
                }
            )
        ),
        Item(
            any_element=AnyElement(
                text="1999",
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}gYear",
                }
            )
        ),
        Item(
            any_element=AnyElement(
                text="--02-13",
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}gMonthDay",
                }
            )
        ),
        Item(
            any_element=AnyElement(
                text="abcd",
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}hexBinary",
                }
            )
        ),
        Item(
            any_element=AnyElement(
                text="http://tempuri",
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}anyURI",
                }
            )
        ),
        Item(
            any_element=AnyElement(
                text="123",
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}anySimpleType",
                }
            )
        ),
        Item(
            any_element=AnyElement(
                text="123",
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}anyType",
                }
            )
        ),
    ]
)
