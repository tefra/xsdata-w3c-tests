from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class B:
    c1_or_c2_or_c3: List[object] = field(
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
                    "name": "c3",
                    "type": object,
                    "namespace": "",
                },
            ),
            "max_occurs": 4,
        },
    )
    foo: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class R(B):
    pass


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
