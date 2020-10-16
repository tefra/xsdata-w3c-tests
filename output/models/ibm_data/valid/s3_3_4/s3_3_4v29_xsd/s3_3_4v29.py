from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Ids:
    """
    :ivar idref_element1:
    :ivar idref_element2:
    :ivar id1:
    :ivar id2:
    """
    class Meta:
        name = "ids"

    idref_element1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    idref_element2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    id1: str = field(
        default="abc",
        metadata={
            "type": "Attribute",
        }
    )
    id2: str = field(
        default="xyz",
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Root:
    """
    :ivar multiple_ids:
    """
    class Meta:
        name = "root"

    multiple_ids: Optional[Ids] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
