from dataclasses import dataclass, field
from typing import Dict, Optional

__NAMESPACE__ = "Wildcard/annotation"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "Wildcard/annotation"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class TheType:
    """
    :ivar any_attributes: This is a wildcard schema component
        (anyAttribute).
    """
    class Meta:
        name = "theType"

    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        }
    )
