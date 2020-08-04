from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Eden:
    """
    :ivar any_attributes:
    """
    class Meta:
        name = "eden"

    any_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any"
        )
    )
