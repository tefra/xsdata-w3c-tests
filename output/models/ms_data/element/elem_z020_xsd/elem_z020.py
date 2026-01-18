from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "foo"


@dataclass(kw_only=True)
class E1:
    class Meta:
        name = "e1"
        namespace = "foo"

    value: bool = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"
        namespace = "foo"

    value: bool = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class B:
    foo_or_e1: list[Foo | E1 | int] = field(
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


@dataclass(kw_only=True)
class Root(B):
    class Meta:
        name = "root"
        namespace = "foo"
