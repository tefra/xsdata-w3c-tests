from dataclasses import dataclass, field
from typing import List
from xml.etree.ElementTree import QName

__NAMESPACE__ = "foo"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    key_or_ref: List[QName] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "key",
                    "type": QName,
                },
                {
                    "name": "ref",
                    "type": QName,
                },
            ),
        },
    )
