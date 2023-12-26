from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "foo"


@dataclass
class Scope:
    class Meta:
        name = "scope"
        namespace = "foo"

    key_or_ref: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "key",
                    "type": str,
                },
                {
                    "name": "ref",
                    "type": str,
                },
            ),
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    scope: List[Scope] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
