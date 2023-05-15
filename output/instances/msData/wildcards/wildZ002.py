from output.models.ms_data.wildcards.wild_z002_xsd.wild_z002 import A
from output.models.ms_data.wildcards.wild_z002_xsd.wild_z002 import B
from output.models.ms_data.wildcards.wild_z002_xsd.wild_z002 import C
from output.models.ms_data.wildcards.wild_z002_xsd.wild_z002 import D
from output.models.ms_data.wildcards.wild_z002_xsd.wild_z002 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    a=[
        A(
            any_element=[
                AnyElement(
                    qname="a",
                    text="",
                    attributes={
                        "att": "123",
                        "att1": "123",
                        "att2": "123",
                    }
                ),
                AnyElement(
                    qname="{foo}foo",
                    text="",
                    children=[
                        AnyElement(
                            qname="{bar}bar",
                            text=""
                        ),
                    ],
                    attributes={
                        "{foo}att": "123",
                    }
                ),
            ]
        ),
    ],
    b=[
        B(
            target_namespace_element=[
                AnyElement(
                    qname="{main}notDeclared",
                    text="",
                    children=[
                        AnyElement(
                            qname="{foo}foo",
                            text=""
                        ),
                    ],
                    attributes={
                        "notexist": "foo",
                    }
                ),
            ]
        ),
    ],
    c=[
        C(
            foo_bar_element=[
                AnyElement(
                    qname="{foo}x",
                    text="",
                    attributes={
                        "{foo}foo": "asd",
                    }
                ),
                AnyElement(
                    qname="{bar}x",
                    text=""
                ),
                AnyElement(
                    qname="{foo}x",
                    text=""
                ),
            ]
        ),
    ],
    d=[
        D(
            target_namespace_foo_element=[
                AnyElement(
                    qname="{foo}x",
                    text=""
                ),
                AnyElement(
                    qname="{foo}x",
                    text=""
                ),
                AnyElement(
                    qname="{main}a",
                    text="",
                    children=[
                        AnyElement(
                            qname="{main}b",
                            text="",
                            children=[
                                AnyElement(
                                    qname="{main}c",
                                    text="",
                                    attributes={
                                        "b": "b",
                                        "c": "b",
                                    }
                                ),
                            ],
                            attributes={
                                "b": "b",
                            }
                        ),
                    ],
                    attributes={
                        "a": "a",
                    }
                ),
            ]
        ),
    ]
)
