from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict

__NAMESPACE__ = "psContents"


@dataclass
class A:
    """
    :ivar any_attributes:
    """
    class Meta:
        name = "a"
        namespace = "psContents"

    any_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any"
        )
    )
