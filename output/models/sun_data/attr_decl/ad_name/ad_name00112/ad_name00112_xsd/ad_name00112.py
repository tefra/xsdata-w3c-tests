from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "AttrDecl/name"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    a_1_2_3_4_5_6: Optional[int] = field(
        default=None,
        metadata={
            "name": "a-1.2_3·4·5۝6۞",
            "type": "Attribute",
        },
    )
    a123456_attribute: Optional[int] = field(
        default=None,
        metadata={
            "name": "a123456",
            "type": "Attribute",
        },
    )
