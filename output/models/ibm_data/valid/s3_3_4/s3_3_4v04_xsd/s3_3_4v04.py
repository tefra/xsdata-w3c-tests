from enum import Enum
from dataclasses import dataclass, field


class Entities(Enum):
    """
    :cvar ASD_QWE:
    """
    ASD_QWE = "asd qwe"


@dataclass
class Root:
    """
    :ivar e1:
    """
    class Meta:
        name = "root"

    e1: Entities = field(
        default=Entities.ASD_QWE,
        metadata=dict(
            type="Attribute"
        )
    )
