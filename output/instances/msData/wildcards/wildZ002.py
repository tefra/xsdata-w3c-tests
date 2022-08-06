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
                    tail=None,
                    children=[],
                    attributes={
                        "att": "123",
                        "att1": "123",
                        "att2": "123",
                    }
                ),
                AnyElement(
                    qname="{foo}foo",
                    text="",
                    tail=None,
                    children=[
                        AnyElement(
                            qname="{bar}bar",
                            text="",
                            tail=None,
                            children=[],
                            attributes={}
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
                    tail=None,
                    children=[
                        AnyElement(
                            qname="{foo}foo",
                            text="",
                            tail=None,
                            children=[],
                            attributes={}
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
                    tail=None,
                    children=[],
                    attributes={
                        "{foo}foo": "asd",
                    }
                ),
                AnyElement(
                    qname="{bar}x",
                    text="",
                    tail=None,
                    children=[],
                    attributes={}
                ),
                AnyElement(
                    qname="{foo}x",
                    text="",
                    tail=None,
                    children=[],
                    attributes={}
                ),
            ]
        ),
    ],
    d=[
        D(
            target_namespace_foo_element=[
                AnyElement(
                    qname="{foo}x",
                    text="",
                    tail=None,
                    children=[],
                    attributes={}
                ),
                AnyElement(
                    qname="{foo}x",
                    text="",
                    tail=None,
                    children=[],
                    attributes={}
                ),
                AnyElement(
                    qname="{main}a",
                    text="",
                    tail=None,
                    children=[
                        AnyElement(
                            qname="{main}b",
                            text="",
                            tail=None,
                            children=[
                                AnyElement(
                                    qname="{main}c",
                                    text="",
                                    tail=None,
                                    children=[],
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
