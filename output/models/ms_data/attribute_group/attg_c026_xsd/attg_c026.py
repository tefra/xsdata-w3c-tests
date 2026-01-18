from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"

    currency: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class TestElem(Foo):
    class Meta:
        name = "testElem"

    model: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    age: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    att_fix: int = field(
        init=False,
        default=37,
        metadata={
            "name": "attFix",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class DocElem:
    class Meta:
        name = "docElem"

    test: TestElem = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Doc(DocElem):
    class Meta:
        name = "doc"
