from output.models.ms_data.additional.isdefault072_xsd.isdefault072 import Array
from xml.etree.ElementTree import QName
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Array(
    item=[
        AnyElement(
            qname="Item",
            text=None,
            tail=None,
            children=[
                AnyElement(
                    qname="{http://tempuri.org/Suites/Serialization}color",
                    text=None,
                    tail=None,
                    children=[
                        AnyElement(
                            qname="{http://tempuri.org/Suites/Serialization}colorId",
                            text="1",
                            tail=None,
                            children=[],
                            attributes={}
                        ),
                    ],
                    attributes={
                        "{http://schemas.microsoft.com/2003/10/Serialization/}Id": "3",
                    }
                ),
            ],
            attributes={
                "{http://schemas.microsoft.com/2003/10/Serialization/}Id": "2",
            }
        ),
    ],
    item_type=QName("{http://tempuri.org/Suites/Serialization}Callbacks.ColorClassHolder"),
    dimensions=[
        1,
    ],
    lower_bounds=[
        0,
    ]
)
