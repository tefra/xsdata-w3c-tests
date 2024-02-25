from dataclasses import dataclass, field
from typing import List, Optional, Type, Union

__NAMESPACE__ = "foo"


@dataclass
class Scope:
    class Meta:
        name = "scope"
        namespace = "foo"

    key_or_ref: List[Union["Scope.Key", "Scope.Ref"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "key",
                    "type": Type["Scope.Key"],
                },
                {
                    "name": "ref",
                    "type": Type["Scope.Ref"],
                },
            ),
        },
    )

    @dataclass
    class Key:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class Ref:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
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
