from dataclasses import dataclass, field
from typing import Dict

__NAMESPACE__ = "http://eden.com/"


@dataclass
class Eden:
    class Meta:
        name = "eden"
        namespace = "http://eden.com/"

    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        }
    )
