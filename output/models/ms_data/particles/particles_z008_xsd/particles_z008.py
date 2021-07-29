from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:my-namespace"


@dataclass
class ContainHead2Type:
    member2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Member2",
            "type": "Element",
            "namespace": "urn:my-namespace",
        }
    )
    head2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Head2",
            "type": "Element",
            "namespace": "urn:my-namespace",
        }
    )


@dataclass
class ContainMember2Type:
    member2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Member2",
            "type": "Element",
            "namespace": "urn:my-namespace",
            "required": True,
        }
    )
    head2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Head2",
            "type": "Element",
            "namespace": "urn:my-namespace",
        }
    )


@dataclass
class Head2:
    class Meta:
        namespace = "urn:my-namespace"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Member2:
    class Meta:
        namespace = "urn:my-namespace"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


@dataclass
class Root(ContainMember2Type):
    class Meta:
        name = "root"
        namespace = "urn:my-namespace"
