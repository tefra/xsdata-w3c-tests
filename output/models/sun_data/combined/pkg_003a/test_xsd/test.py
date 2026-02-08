from __future__ import annotations

from dataclasses import dataclass, field

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

    item: list[B] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )


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
