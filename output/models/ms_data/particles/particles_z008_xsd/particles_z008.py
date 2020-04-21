from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:my-namespace"


@dataclass
class Member2:
    """
    :ivar value:
    """
    class Meta:
        namespace = "urn:my-namespace"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class ContainMember2Type:
    """
    :ivar my_namespace_member2:
    :ivar member2:
    :ivar head2:
    """
    my_namespace_member2: Optional[Member2] = field(
        default=None,
        metadata=dict(
            name="Member2",
            type="Element",
            namespace="urn:my-namespace",
            required=True
        )
    )
    member2: Optional[Member2] = field(
        default=None,
        metadata=dict(
            name="Member2",
            type="Element",
            namespace="urn:my-namespace",
            required=True
        )
    )
    head2: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Head2",
            type="Element",
            namespace="urn:my-namespace",
            required=True
        )
    )


@dataclass
class Root(ContainMember2Type):
    class Meta:
        name = "root"
        namespace = "urn:my-namespace"
