from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Optional, Union


@dataclass
class Root:
    """
    :ivar value:
    """
    class Meta:
        name = "root"

    value: Optional[Union[str, QName, int]] = field(
        default=None,
    )
