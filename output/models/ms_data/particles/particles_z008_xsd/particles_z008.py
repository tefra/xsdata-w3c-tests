from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:my-namespace"


@dataclass
class ContainHead2Type:
    member2_or_head2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Member2",
                    "type": str,
                    "namespace": "urn:my-namespace",
                },
                {
                    "name": "Head2",
                    "type": str,
                    "namespace": "urn:my-namespace",
                },
            ),
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
class ContainMember2Type(ContainHead2Type):
    member2: Optional[str] = field(
        default=None,
        metadata={
            "name": "Member2",
            "type": "Element",
            "namespace": "urn:my-namespace",
            "required": True,
        }
    )


@dataclass
class Root(ContainMember2Type):
    class Meta:
        name = "root"
        namespace = "urn:my-namespace"
