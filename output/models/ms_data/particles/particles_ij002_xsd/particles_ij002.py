from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Foo:
    class Meta:
        name = "foo"

    f1_or_f2: list[Union["Foo.F1", "Foo.F2"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "f1",
                    "type": ForwardRef("Foo.F1"),
                    "namespace": "http://xsdtesting",
                    "max_occurs": 100,
                },
                {
                    "name": "f2",
                    "type": ForwardRef("Foo.F2"),
                    "namespace": "http://xsdtesting",
                },
            ),
            "max_occurs": 100,
        },
    )

    @dataclass
    class F1:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "http://xsdtesting",
                "required": True,
            },
        )

    @dataclass
    class F2:
        content: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "http://xsdtesting",
                "required": True,
            },
        )


@dataclass
class B:
    c1_or_c2: Optional[Union[Foo, object]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "c1",
                    "type": Foo,
                    "namespace": "http://xsdtesting",
                },
                {
                    "name": "c2",
                    "type": object,
                    "namespace": "http://xsdtesting",
                },
            ),
        },
    )


@dataclass
class R(B):
    pass


@dataclass
class Elem(R):
    class Meta:
        name = "elem"
        namespace = "http://xsdtesting"


@dataclass
class Doc:
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    elem: Optional[Elem] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
