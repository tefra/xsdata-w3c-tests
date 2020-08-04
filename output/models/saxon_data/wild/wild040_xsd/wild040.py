from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Computer:
    """
    :ivar any_attributes:
    """
    class Meta:
        name = "computer"

    any_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any",
            required=True
        )
    )
