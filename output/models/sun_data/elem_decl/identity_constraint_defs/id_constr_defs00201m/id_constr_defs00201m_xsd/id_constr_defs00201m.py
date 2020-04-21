from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "ElemDecl/identityConstraintDefs"


@dataclass
class Root:
    """
    :ivar account:
    :ivar name:
    :ivar manager:
    """
    class Meta:
        name = "root"
        namespace = "ElemDecl/identityConstraintDefs"

    account: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Account",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    name: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Name",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
    manager: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Manager",
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=9223372036854775807,
            sequential=True
        )
    )
