from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict

__NAMESPACE__ = "http://eden.com/"


@dataclass
class Eden:
    """
    :ivar any_attributes:
    """
    class Meta:
        name = "eden"
        namespace = "http://eden.com/"

    any_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any"
        )
    )
