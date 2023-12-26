from dataclasses import dataclass, field
from typing import List, Optional, Union

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Foo:
    class Meta:
        name = "foo"

    f1_or_f2: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "f1",
                    "type": object,
                    "namespace": "http://xsdtesting",
                },
                {
                    "name": "f2",
                    "type": object,
                    "namespace": "http://xsdtesting",
                },
            ),
            "max_occurs": 5,
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
class Bar(Foo):
    class Meta:
        name = "bar"


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
