from dataclasses import dataclass, field
from typing import List, Union
from xml.etree.ElementTree import QName


@dataclass
class Root:
    class Meta:
        name = "root"

    value: List[Union[float, str, int, QName]] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
