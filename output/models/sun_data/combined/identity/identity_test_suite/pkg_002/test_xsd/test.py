from dataclasses import dataclass, field
from lxml.etree import QName
from typing import List

__NAMESPACE__ = "foo"


@dataclass
class Root:
    """
    :ivar key:
    :ivar ref:
    """
    class Meta:
        name = "root"
        namespace = "foo"

    key: List[QName] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    ref: List[QName] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
