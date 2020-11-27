from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "nsConstraint"


@dataclass
class A:
    class Meta:
        name = "a"
        namespace = "nsConstraint"

    other_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "required": True,
        }
    )


@dataclass
class Date:
    class Meta:
        name = "date"
        namespace = "nsConstraint"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
