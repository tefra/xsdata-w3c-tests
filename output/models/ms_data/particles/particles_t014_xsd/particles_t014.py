from dataclasses import dataclass, field
from typing import List, Optional, Union

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Foo:
    class Meta:
        name = "foo"

    foo: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    att: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Bar(Foo):
    class Meta:
        name = "bar"

    att1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class B:
    c1_or_c2_or_c3: List[Union[object, Bar]] = field(
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
                    "type": Bar,
                    "namespace": "",
                },
            ),
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
    c1_or_c2: List[object] = field(
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
            ),
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
