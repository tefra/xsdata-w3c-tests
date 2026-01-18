from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "foo"


@dataclass(kw_only=True)
class Empty:
    class Meta:
        name = "empty"


@dataclass(kw_only=True)
class B:
    foo: Empty = field(
        metadata={
            "type": "Element",
            "namespace": "foo",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class De(B):
    pass


@dataclass(kw_only=True)
class Dr(B):
    pass


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    item1_or_item2: list[Root.Item1 | Root.Item2] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "item1",
                    "type": ForwardRef("Root.Item1"),
                },
                {
                    "name": "item2",
                    "type": ForwardRef("Root.Item2"),
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class Item1(B):
        pass

    @dataclass(kw_only=True)
    class Item2(B):
        pass


@dataclass(kw_only=True)
class Dee(De):
    pass


@dataclass(kw_only=True)
class Der(De):
    pass


@dataclass(kw_only=True)
class Dre(Dr):
    pass


@dataclass(kw_only=True)
class Drr(Dr):
    pass
