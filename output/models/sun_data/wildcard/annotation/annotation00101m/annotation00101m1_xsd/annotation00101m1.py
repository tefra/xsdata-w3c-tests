from dataclasses import dataclass, field
from typing import Dict, Optional

__NAMESPACE__ = "Wildcard/annotation"


@dataclass
class Root:
    """
    :ivar any_element:
    """
    class Meta:
        name = "root"
        namespace = "Wildcard/annotation"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class TheType:
    """
    :ivar any_attributes: This is a wildcard schema component (anyAttribute).
    """
    class Meta:
        name = "theType"

    any_attributes: Dict = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any"
        )
    )
