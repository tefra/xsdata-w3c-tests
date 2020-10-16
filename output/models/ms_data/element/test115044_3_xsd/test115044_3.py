from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "foo"


@dataclass
class E:
    """
    :ivar any_element:
    """
    class Meta:
        name = "e"
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
class Root:
    """
    :ivar e:
    """
    class Meta:
        name = "root"
        namespace = "foo"

    e: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
