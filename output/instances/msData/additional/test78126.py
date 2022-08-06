from output.models.ms_data.additional.test78126_xsd.test78126 import A
from output.models.ms_data.additional.test78126_xsd.test78126 import Any
from output.models.ms_data.additional.test78126_xsd.test78126 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    any_or_a=[
        A(
            value="a1",
            att1=123,
            att2=True
        ),
        Any(
            any_element=[
                AnyElement(
                    qname="foo",
                    text="",
                    tail=None,
                    children=[],
                    attributes={
                        "bar": "bla",
                        "a1": "b",
                        "a2": "b",
                        "a3": "b",
                        "a4": "b",
                        "a5": "b",
                        "a6": "b",
                        "a7": "b",
                        "a8": "b",
                    }
                ),
                AnyElement(
                    qname="bar",
                    text="",
                    tail=None,
                    children=[
                        AnyElement(
                            qname="foo",
                            text="",
                            tail=None,
                            children=[],
                            attributes={
                                "bar": "bla",
                                "a1": "b",
                                "a2": "b",
                                "a3": "b",
                                "a4": "b",
                                "a5": "b",
                                "a6": "b",
                                "a7": "b",
                                "a8": "b",
                            }
                        ),
                    ],
                    attributes={}
                ),
                AnyElement(
                    qname="foo",
                    text="",
                    tail=None,
                    children=[
                        AnyElement(
                            qname="bar",
                            text="",
                            tail=None,
                            children=[
                                AnyElement(
                                    qname="foo",
                                    text="",
                                    tail=None,
                                    children=[],
                                    attributes={
                                        "bar": "bla",
                                        "a1": "b",
                                        "a2": "b",
                                        "a3": "b",
                                        "a4": "b",
                                        "a5": "b",
                                        "a6": "b",
                                        "a7": "b",
                                        "a8": "b",
                                    }
                                ),
                            ],
                            attributes={}
                        ),
                    ],
                    attributes={}
                ),
                AnyElement(
                    qname="foo",
                    text="",
                    tail=None,
                    children=[
                        AnyElement(
                            qname="bar",
                            text="",
                            tail=None,
                            children=[
                                AnyElement(
                                    qname="foo",
                                    text="",
                                    tail=None,
                                    children=[
                                        AnyElement(
                                            qname="bar",
                                            text="",
                                            tail=None,
                                            children=[
                                                AnyElement(
                                                    qname="foo",
                                                    text="",
                                                    tail=None,
                                                    children=[],
                                                    attributes={
                                                        "bar": "bla",
                                                        "a1": "b",
                                                        "a2": "b",
                                                        "a3": "b",
                                                        "a4": "b",
                                                        "a5": "b",
                                                        "a6": "b",
                                                        "a7": "b",
                                                        "a8": "b",
                                                    }
                                                ),
                                            ],
                                            attributes={}
                                        ),
                                    ],
                                    attributes={}
                                ),
                            ],
                            attributes={}
                        ),
                    ],
                    attributes={}
                ),
                AnyElement(
                    qname="foo",
                    text="",
                    tail=None,
                    children=[
                        AnyElement(
                            qname="bar",
                            text="",
                            tail=None,
                            children=[
                                AnyElement(
                                    qname="foo",
                                    text="",
                                    tail=None,
                                    children=[
                                        AnyElement(
                                            qname="bar",
                                            text="",
                                            tail=None,
                                            children=[
                                                AnyElement(
                                                    qname="foo",
                                                    text="",
                                                    tail=None,
                                                    children=[
                                                        AnyElement(
                                                            qname="bar",
                                                            text="",
                                                            tail=None,
                                                            children=[
                                                                AnyElement(
                                                                    qname="foo",
                                                                    text="",
                                                                    tail=None,
                                                                    children=[
                                                                        AnyElement(
                                                                            qname="bar",
                                                                            text="",
                                                                            tail=None,
                                                                            children=[
                                                                                AnyElement(
                                                                                    qname="foo",
                                                                                    text="",
                                                                                    tail=None,
                                                                                    children=[],
                                                                                    attributes={
                                                                                        "bar": "bla",
                                                                                        "a1": "b",
                                                                                        "a2": "b",
                                                                                        "a3": "b",
                                                                                        "a4": "b",
                                                                                        "a5": "b",
                                                                                        "a6": "b",
                                                                                        "a7": "b",
                                                                                        "a8": "b",
                                                                                    }
                                                                                ),
                                                                            ],
                                                                            attributes={}
                                                                        ),
                                                                    ],
                                                                    attributes={}
                                                                ),
                                                            ],
                                                            attributes={}
                                                        ),
                                                    ],
                                                    attributes={}
                                                ),
                                            ],
                                            attributes={}
                                        ),
                                    ],
                                    attributes={}
                                ),
                            ],
                            attributes={}
                        ),
                    ],
                    attributes={}
                ),
                AnyElement(
                    qname="a",
                    text="a1",
                    tail=None,
                    children=[],
                    attributes={
                        "att1": "123",
                        "att2": "true",
                    }
                ),
                AnyElement(
                    qname="a",
                    text="1",
                    tail=None,
                    children=[],
                    attributes={}
                ),
                AnyElement(
                    qname="a",
                    text="blue",
                    tail=None,
                    children=[],
                    attributes={
                        "att1": "123",
                        "att2": "false",
                    }
                ),
                AnyElement(
                    qname="b",
                    text="",
                    tail=None,
                    children=[],
                    attributes={
                        "att1": "123",
                        "att2": "false",
                    }
                ),
            ]
        ),
    ]
)
