from output.models.saxon_data.id.id005_xsd.id005 import Doc
from output.models.saxon_data.id.id005_xsd.id005 import Node
from xsdata.formats.dataclass.models.generics import DerivedElement


obj = Doc(
    node=[
        Node(
            node_or_id_or_idrefs=[
                Node(
                    node_or_id_or_idrefs=[],
                    id_attribute=[],
                    idrefs_attribute=[
                        "bbb",
                        "ccc",
                        "ggg",
                    ]
                ),
                Node(
                    node_or_id_or_idrefs=[
                        DerivedElement(
                            qname="idrefs",
                            value=[
                                "aaa",
                                "ddd",
                            ],
                            type=None
                        ),
                    ],
                    id_attribute=[
                        "ggg",
                    ],
                    idrefs_attribute=[]
                ),
                [
                    "ccc",
                    "ddd",
                ],
            ],
            id_attribute=[
                "aaa",
                "bbb",
            ],
            idrefs_attribute=[]
        ),
    ]
)
