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
class EB(B):
    class Meta:
        name = "eB"
        namespace = "foo"


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


@dataclass(kw_only=True)
class EDe(De):
    class Meta:
        name = "eDe"
        namespace = "foo"


@dataclass(kw_only=True)
class EDr(Dr):
    class Meta:
        name = "eDr"
        namespace = "foo"


@dataclass(kw_only=True)
class EDee(Dee):
    class Meta:
        name = "eDee"
        namespace = "foo"


@dataclass(kw_only=True)
class EDer(Der):
    class Meta:
        name = "eDer"
        namespace = "foo"


@dataclass(kw_only=True)
class EDre(Dre):
    class Meta:
        name = "eDre"
        namespace = "foo"


@dataclass(kw_only=True)
class EDrr(Drr):
    class Meta:
        name = "eDrr"
        namespace = "foo"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    choice: list[EDee | EDer | EDe | EDre | EDrr | EDr | EB] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "eDee",
                    "type": EDee,
                },
                {
                    "name": "eDer",
                    "type": EDer,
                },
                {
                    "name": "eDe",
                    "type": EDe,
                },
                {
                    "name": "eDre",
                    "type": EDre,
                },
                {
                    "name": "eDrr",
                    "type": EDrr,
                },
                {
                    "name": "eDr",
                    "type": EDr,
                },
                {
                    "name": "eB",
                    "type": EB,
                },
            ),
        },
    )
