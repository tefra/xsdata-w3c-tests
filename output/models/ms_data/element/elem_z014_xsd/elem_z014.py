from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn-klondike-test"


@dataclass
class CtypeFoo:
    """
    :ivar a:
    """
    class Meta:
        name = "ctype_foo"

    a: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class RootElem:
    """
    :ivar any_element:
    """
    class Meta:
        name = "root_elem"
        namespace = "urn-klondike-test"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
