from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "foo"


@dataclass
class E1:
    """
    :ivar any_element:
    """
    class Meta:
        name = "e1"
        namespace = "foo"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class E2:
    """
    :ivar any_element:
    """
    class Meta:
        name = "e2"
        namespace = "foo"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class ImpElem1:
    """
    :ivar any_element:
    """
    class Meta:
        name = "impElem1"
        namespace = "foo"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
