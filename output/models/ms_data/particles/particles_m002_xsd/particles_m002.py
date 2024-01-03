from dataclasses import dataclass, field
from typing import List, Optional, Any

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "c1",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "c2",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "d1",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "d2",
                    "type": object,
                    "namespace": "",
                },
            ),
            "max_occurs": 9,
        },
    )


@dataclass
class R(B):
    c2_or_d1_or_d2: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: Optional[R] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
