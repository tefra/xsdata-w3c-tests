from dataclasses import dataclass, field
from typing import List, Optional, Any

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Base:
    annotation: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    element_or_any: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "element",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "any",
                    "type": object,
                    "namespace": "",
                },
            ),
        },
    )


@dataclass
class Derived(Base):
    any: Any = field(
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

    elem: Optional[Derived] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
