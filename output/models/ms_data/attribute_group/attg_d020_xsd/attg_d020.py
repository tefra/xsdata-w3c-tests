from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict, Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Doc:
    """
    :ivar att1:
    :ivar abc:
    :ivar any_attributes:
    """
    class Meta:
        name = "doc"
        namespace = "http://xsdtesting"

    att1: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://xsdtesting"
        )
    )
    abc: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://xsdtesting"
        )
    )
    any_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any"
        )
    )
