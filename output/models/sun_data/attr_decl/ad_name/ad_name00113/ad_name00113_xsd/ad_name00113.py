from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "AttrDecl/name"


@dataclass
class Root:
    """
    :ivar aa111a2_aa:
    :ivar aa22_b3c:
    :ivar aa3_4:
    """
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    aa111a2_aa: Optional[int] = field(
        default=None,
        metadata=dict(
            name="aa111a2Aa",
            type="Attribute"
        )
    )
    aa22_b3c: Optional[int] = field(
        default=None,
        metadata=dict(
            name="aa22B3c",
            type="Attribute"
        )
    )
    aa3_4: Optional[int] = field(
        default=None,
        metadata=dict(
            name="aa3-4_",
            type="Attribute"
        )
    )
