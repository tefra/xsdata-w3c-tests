from dataclasses import dataclass, field
from enum import Enum


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
