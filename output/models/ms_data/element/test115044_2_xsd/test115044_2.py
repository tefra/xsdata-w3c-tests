from dataclasses import dataclass, field
from typing import Optional, Union

__NAMESPACE__ = "foo"


@dataclass
class E:
    class Meta:
        name = "e"
        namespace = "foo"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class E1:
    class Meta:
        name = "e1"
        namespace = "foo"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    e1_or_e: Optional[Union[int, E]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "e1",
                    "type": int,
                },
                {
                    "name": "e",
                    "type": E,
                },
            ),
        }
    )
