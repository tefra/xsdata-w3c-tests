from output.models.ms_data.additional.add_b122_xsd.add_b122 import E6
from output.models.ms_data.additional.add_b122_xsd.add_b122 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    e6=[
        E6(
            any_element=[
                AnyElement(
                    qname="e3",
                    text="",
                    children=[
                        AnyElement(
                            qname="e31",
                            text=""
                        ),
                    ],
                    attributes={
                        "att": "123",
                    }
                ),
            ]
        ),
    ]
)
