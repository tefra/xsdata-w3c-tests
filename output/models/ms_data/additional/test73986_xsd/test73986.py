from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Root:
    """
    :ivar value:
    """
    class Meta:
        name = "root"
        namespace = "http://xsdtesting"

    value: Optional[QName] = field(
        default=None,
        metadata={
            "required": True,
            "max_length": 5,
        }
    )
