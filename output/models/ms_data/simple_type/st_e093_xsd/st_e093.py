from dataclasses import dataclass, field
from lxml.etree import QName
from typing import List, Union


@dataclass
class Root:
    """
    :ivar value:
    """
    class Meta:
        name = "root"

    value: List[Union[float, str, int, QName]] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
