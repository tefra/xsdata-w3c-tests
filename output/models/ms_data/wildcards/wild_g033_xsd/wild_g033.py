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
        metadata=dict(
            required=True
        )
    )


@dataclass
class Foo:
    """
    :ivar local_foobar_element:
    """
    class Meta:
        name = "foo"
        namespace = "http://foobar"

    local_foobar_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##local http://foobar",
            required=True
        )
    )
