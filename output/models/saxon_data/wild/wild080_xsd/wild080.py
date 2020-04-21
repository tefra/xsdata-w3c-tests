from dataclasses import dataclass, field
from typing import Optional


@dataclass
class A:
    class Meta:
        name = "a"



@dataclass
class Zing:
    """
    :ivar a:
    :ivar local_element:
    """
    class Meta:
        name = "zing"

    a: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    local_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##local",
            required=True
        )
    )


@dataclass
class Root(Zing):
    class Meta:
        name = "root"
