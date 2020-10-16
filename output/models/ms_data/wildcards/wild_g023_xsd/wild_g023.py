from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://foobar"


@dataclass
class Bar:
    """
    :ivar value:
    """
    class Meta:
        name = "bar"
        namespace = "http://foobar"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Foo:
    """
    :ivar foobar_element:
    """
    class Meta:
        name = "foo"
        namespace = "http://foobar"

    foobar_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "required": True,
        }
    )
