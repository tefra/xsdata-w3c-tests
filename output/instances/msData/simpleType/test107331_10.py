from output.models.ms_data.simple_type.test107331_j_xsd.test107331_j import Item
from output.models.ms_data.simple_type.test107331_j_xsd.test107331_j import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    choice=[
        Item(
            any_element=AnyElement(
                qname=None,
                text="abc",
                tail=None,
                children=[],
                attributes={}
            )
        ),
        Item(
            any_element=AnyElement(
                qname=None,
                text="123",
                tail=None,
                children=[],
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}int",
                }
            )
        ),
        Item(
            any_element=AnyElement(
                qname=None,
                text="4.56",
                tail=None,
                children=[],
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}float",
                }
            )
        ),
        Item(
            any_element=AnyElement(
                qname=None,
                text="this is a string",
                tail=None,
                children=[],
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}string",
                }
            )
        ),
        Item(
            any_element=AnyElement(
                qname=None,
                text="false",
                tail=None,
                children=[],
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}boolean",
                }
            )
        ),
        Item(
            any_element=AnyElement(
                qname=None,
                text="45",
                tail=None,
                children=[],
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}decimal",
                }
            )
        ),
        Item(
            any_element=AnyElement(
                qname=None,
                text="P1347Y",
                tail=None,
                children=[],
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}duration",
                }
            )
        ),
        Item(
            any_element=AnyElement(
                qname=None,
                text="1999-05-31T13:20:00-05:00",
                tail=None,
                children=[],
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}dateTime",
                }
            )
        ),
        Item(
            any_element=AnyElement(
                qname=None,
                text="13:20:00-05:00",
                tail=None,
                children=[],
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}time",
                }
            )
        ),
        Item(
            any_element=AnyElement(
                qname=None,
                text="1999-05-31",
                tail=None,
                children=[],
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}date",
                }
            )
        ),
        Item(
            any_element=AnyElement(
                qname=None,
                text="1999",
                tail=None,
                children=[],
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}gYear",
                }
            )
        ),
        Item(
            any_element=AnyElement(
                qname=None,
                text="--02-13",
                tail=None,
                children=[],
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}gMonthDay",
                }
            )
        ),
        Item(
            any_element=AnyElement(
                qname=None,
                text="abcd",
                tail=None,
                children=[],
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}hexBinary",
                }
            )
        ),
        Item(
            any_element=AnyElement(
                qname=None,
                text="http://tempuri",
                tail=None,
                children=[],
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}anyURI",
                }
            )
        ),
        Item(
            any_element=AnyElement(
                qname=None,
                text="123",
                tail=None,
                children=[],
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}anySimpleType",
                }
            )
        ),
        Item(
            any_element=AnyElement(
                qname=None,
                text="123",
                tail=None,
                children=[],
                attributes={
                    "{http://www.w3.org/2001/XMLSchema-instance}type": "{http://www.w3.org/2001/XMLSchema}anyType",
                }
            )
        ),
    ]
)
