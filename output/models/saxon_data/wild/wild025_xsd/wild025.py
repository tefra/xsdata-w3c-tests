from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict


@dataclass
class T:
    """
    :ivar eve_com_attributes:
    :ivar any_attributes:
    """
    eve_com_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="http://adam.com/ http://eve.com/"
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
class Eden(T):
    class Meta:
        name = "eden"
