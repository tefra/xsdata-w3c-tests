from output.models.ms_data.additional.test78000a_xsd.test78000a import Doc
from output.models.ms_data.additional.test78000a_xsd.test78000a import LaxContainer
from output.models.ms_data.additional.test78000a_xsd.test78000a import RootContainer
from output.models.ms_data.additional.test78000a_xsd.test78000a import SkipContainer
from output.models.ms_data.additional.test78000a_xsd.test78000a import StrictContainer
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    root_container=[
        RootContainer(
            strict_container=StrictContainer(
                other_element=AnyElement(
                    qname="{b}test",
                    text="",
                    tail=None,
                    children=[],
                    attributes={
                        "b1": "a",
                    }
                )
            ),
            lax_container=LaxContainer(
                other_element=AnyElement(
                    qname="{b}test",
                    text="",
                    tail=None,
                    children=[],
                    attributes={
                        "b1": "a",
                    }
                )
            ),
            skip_container=SkipContainer(
                other_element=AnyElement(
                    qname="{other}anyOtherGarbage",
                    text="",
                    tail=None,
                    children=[],
                    attributes={}
                )
            )
        ),
        RootContainer(
            strict_container=StrictContainer(
                other_element=AnyElement(
                    qname="{b}test",
                    text="",
                    tail=None,
                    children=[],
                    attributes={
                        "b1": "a",
                    }
                )
            ),
            lax_container=LaxContainer(
                other_element=AnyElement(
                    qname="{other}anyOtherGarbage",
                    text="",
                    tail=None,
                    children=[],
                    attributes={}
                )
            ),
            skip_container=SkipContainer(
                other_element=AnyElement(
                    qname="{other}anyOtherGarbage",
                    text="",
                    tail=None,
                    children=[],
                    attributes={}
                )
            )
        ),
        RootContainer(
            strict_container=StrictContainer(
                other_element=AnyElement(
                    qname="{b}test",
                    text="",
                    tail=None,
                    children=[],
                    attributes={
                        "b1": "a",
                    }
                )
            ),
            lax_container=LaxContainer(
                other_element=AnyElement(
                    qname="{b}test",
                    text="",
                    tail=None,
                    children=[],
                    attributes={
                        "b1": "a",
                    }
                )
            ),
            skip_container=SkipContainer(
                other_element=AnyElement(
                    qname="{b}test",
                    text="",
                    tail=None,
                    children=[],
                    attributes={}
                )
            )
        ),
    ]
)
