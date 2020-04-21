from dataclasses import dataclass, field
from typing import List


@dataclass
class RegistryValueModOpSetType:
    """
    :ivar regvalueop:
    """
    regvalueop: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=1,
            max_occurs=2
        )
    )


@dataclass
class Regvaluemodopset(RegistryValueModOpSetType):
    class Meta:
        name = "regvaluemodopset"
