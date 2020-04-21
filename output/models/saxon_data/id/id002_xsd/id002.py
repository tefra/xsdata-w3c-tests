from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict, List, Optional


@dataclass
class Para:
    """
    :ivar value:
    :ivar id_one:
    :ivar any_attributes:
    """
    class Meta:
        name = "para"

    value: Optional[str] = field(
        default=None,
    )
    id_one: Optional[str] = field(
        default=None,
        metadata=dict(
            name="id-one",
            type="Attribute"
        )
    )
    any_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any"
        )
    )


@dataclass
class Doc:
    """
    :ivar para:
    """
    class Meta:
        name = "doc"

    para: List[Para] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
