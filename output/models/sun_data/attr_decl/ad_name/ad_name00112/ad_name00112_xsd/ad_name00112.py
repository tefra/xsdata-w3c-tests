from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "AttrDecl/name"


@dataclass
class Root:
    """
    :ivar a_1_2_3_4_5_6:
    :ivar a123456:
    """
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    a_1_2_3_4_5_6: Optional[int] = field(
        default=None,
        metadata=dict(
            name="a-1.2_3·4·5۝6۞",
            type="Attribute"
        )
    )
    a123456: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
