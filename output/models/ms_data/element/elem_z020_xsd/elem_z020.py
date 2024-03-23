from dataclasses import dataclass, field
from typing import List, Optional, Union

__NAMESPACE__ = "foo"


@dataclass
class E1:
    class Meta:
        name = "e1"
        namespace = "foo"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Foo:
    class Meta:
        name = "foo"
        namespace = "foo"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class B:
    foo_or_e1: List[Union[Foo, E1, int]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "foo",
                    "type": Foo,
                    "namespace": "foo",
                    "max_occurs": 1000,
                },
                {
                    "name": "e1",
                    "type": E1,
                    "namespace": "foo",
                    "max_occurs": 1000,
                },
                {
                    "name": "foo",
                    "type": int,
                    "namespace": "",
                    "max_occurs": 1000,
                },
            ),
            "max_occurs": 1000,
        },
    )


@dataclass
class Root(B):
    class Meta:
        name = "root"
        namespace = "foo"
