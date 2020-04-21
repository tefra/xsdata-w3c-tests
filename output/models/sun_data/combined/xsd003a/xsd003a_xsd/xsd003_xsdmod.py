from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "foo"


@dataclass
class ComplexType:
    """
    :ivar root:
    :ivar g_att:
    """
    class Meta:
        name = "complexType"

    root: List["Root"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="foo",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    g_att: Optional[str] = field(
        default=None,
        metadata=dict(
            name="gAtt",
            type="Attribute",
            namespace="foo"
        )
    )


@dataclass
class Root(ComplexType):
    class Meta:
        name = "root"
        namespace = "foo"
