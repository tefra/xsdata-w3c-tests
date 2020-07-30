from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Optional

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
        metadata=dict(
            required=True,
            max_length=5
        )
    )
