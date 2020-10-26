from dataclasses import dataclass, field
from typing import List, Optional, Type
from output.models.ms_data.additional.test66745_a_xsd.test66745_a import Foo1

__NAMESPACE__ = "foo"


@dataclass
class Foo:
    """
    :ivar any_element:
    """
    class Meta:
        name = "foo"
        namespace = "foo"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class Bar:
    """
    :ivar foo1_or_foo_or_bar:
    """
    class Meta:
        name = "bar"
        namespace = "foo"

    foo1_or_foo_or_bar: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "foo1",
                    "type": Foo1,
                    "namespace": "foo1",
                },
                {
                    "name": "foo",
                    "type": Foo,
                },
                {
                    "name": "bar",
                    "type": Type["Bar"],
                },
            ),
        }
    )
