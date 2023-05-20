from output.models.ms_data.additional.test78126_xsd.test78126 import A
from output.models.ms_data.additional.test78126_xsd.test78126 import AnyType
from output.models.ms_data.additional.test78126_xsd.test78126 import Root
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Root(
    any_or_a=[
        A(
            value="a1",
            att1=123,
            att2=True
        ),
        AnyType(
            any_element=[
                AnyElement(
                    qname="foo",
                    text="",
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
                    children=[
                        AnyElement(
                            qname="foo",
                            text="",
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
                    ]
                ),
                AnyElement(
                    qname="foo",
                    text="",
                    children=[
                        AnyElement(
                            qname="bar",
                            text="",
                            children=[
                                AnyElement(
                                    qname="foo",
                                    text="",
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
                            ]
                        ),
                    ]
                ),
                AnyElement(
                    qname="foo",
                    text="",
                    children=[
                        AnyElement(
                            qname="bar",
                            text="",
                            children=[
                                AnyElement(
                                    qname="foo",
                                    text="",
                                    children=[
                                        AnyElement(
                                            qname="bar",
                                            text="",
                                            children=[
                                                AnyElement(
                                                    qname="foo",
                                                    text="",
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
                                            ]
                                        ),
                                    ]
                                ),
                            ]
                        ),
                    ]
                ),
                AnyElement(
                    qname="foo",
                    text="",
                    children=[
                        AnyElement(
                            qname="bar",
                            text="",
                            children=[
                                AnyElement(
                                    qname="foo",
                                    text="",
                                    children=[
                                        AnyElement(
                                            qname="bar",
                                            text="",
                                            children=[
                                                AnyElement(
                                                    qname="foo",
                                                    text="",
                                                    children=[
                                                        AnyElement(
                                                            qname="bar",
                                                            text="",
                                                            children=[
                                                                AnyElement(
                                                                    qname="foo",
                                                                    text="",
                                                                    children=[
                                                                        AnyElement(
                                                                            qname="bar",
                                                                            text="",
                                                                            children=[
                                                                                AnyElement(
                                                                                    qname="foo",
                                                                                    text="",
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
                                                                            ]
                                                                        ),
                                                                    ]
                                                                ),
                                                            ]
                                                        ),
                                                    ]
                                                ),
                                            ]
                                        ),
                                    ]
                                ),
                            ]
                        ),
                    ]
                ),
                AnyElement(
                    qname="a",
                    text="a1",
                    attributes={
                        "att1": "123",
                        "att2": "true",
                    }
                ),
                AnyElement(
                    qname="a",
                    text="1"
                ),
                AnyElement(
                    qname="a",
                    text="blue",
                    attributes={
                        "att1": "123",
                        "att2": "false",
                    }
                ),
                AnyElement(
                    qname="b",
                    text="",
                    attributes={
                        "att1": "123",
                        "att2": "false",
                    }
                ),
            ]
        ),
    ]
)
