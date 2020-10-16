from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "IdConstrDefs/annotation"


@dataclass
class People:
    """
    :ivar person:
    """
    class Meta:
        name = "people"
        namespace = "IdConstrDefs/annotation"

    person: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class Root:
    """
    :ivar any_element:
    """
    class Meta:
        name = "root"
        namespace = "IdConstrDefs/annotation"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
