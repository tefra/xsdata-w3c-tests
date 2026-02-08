from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "urn:my-namespace"


@dataclass(kw_only=True)
class Head2:
    class Meta:
        namespace = "urn:my-namespace"

    value: str = field(default="")


@dataclass(kw_only=True)
class Member2:
    class Meta:
        namespace = "urn:my-namespace"

    value: str = field(default="")


@dataclass(kw_only=True)
class ContainHead2Type:
    member2: None | Member2 = field(
        default=None,
        metadata={
            "name": "Member2",
            "type": "Element",
            "namespace": "urn:my-namespace",
        },
    )


@dataclass(kw_only=True)
class ContainMember2Type(ContainHead2Type):
    member2: Member2 = field(
        metadata={
            "name": "Member2",
            "type": "Element",
            "namespace": "urn:my-namespace",
        }
    )


@dataclass(kw_only=True)
class Root(ContainMember2Type):
    class Meta:
        name = "root"
        namespace = "urn:my-namespace"
