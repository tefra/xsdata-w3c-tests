from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xstest-tns/schema11_D4_3_15"


@dataclass
class Root:
    """
    :ivar e1:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D4_3_15"

    e1: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
