from dataclasses import dataclass, field
from typing import Dict


@dataclass
class B:
    """
    :ivar any_attributes:
    """
    any_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any"
        )
    )


@dataclass
class R:
    """
    :ivar any_attributes:
    """
    any_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any"
        )
    )


@dataclass
class Eden(R):
    class Meta:
        name = "eden"
