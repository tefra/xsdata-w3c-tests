from dataclasses import dataclass, field
from typing import List, Optional
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
    :ivar foo1:
    :ivar foo:
    :ivar bar:
    """
    class Meta:
        name = "bar"
        namespace = "foo"

    foo1: List[Foo1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "foo1",
        }
    )
    foo: List[Foo] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    bar: List["Bar"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
