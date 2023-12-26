from dataclasses import dataclass, field
from typing import List, Optional, Union

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Mixed:
    class Meta:
        name = "mixed"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class B:
    c1_or_c2: Optional[Union[Mixed, object]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "c1",
                    "type": Mixed,
                    "namespace": "",
                },
                {
                    "name": "c2",
                    "type": object,
                    "namespace": "",
                },
            ),
        },
    )
    d1_or_d2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
        },
    )


@dataclass
class NotMixed(Mixed):
    class Meta:
        name = "not_mixed"

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
