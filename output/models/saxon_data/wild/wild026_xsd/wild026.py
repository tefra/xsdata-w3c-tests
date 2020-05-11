from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict


@dataclass
class T:
    """
    :ivar any_attributes:
    :ivar adam_com_http_eve_com_attributes:
    """
    any_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any"
        )
    )
    adam_com_http_eve_com_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="http://adam.com/ http://eve.com/"
        )
    )


@dataclass
class Eden(T):
    class Meta:
        name = "eden"
