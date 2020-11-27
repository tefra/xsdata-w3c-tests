from dataclasses import dataclass, field
from typing import Optional, Union
from xml.etree.ElementTree import QName


@dataclass
class Root:
    class Meta:
        name = "root"

    value: Optional[Union[str, QName, int]] = field(
        default=None,
    )
