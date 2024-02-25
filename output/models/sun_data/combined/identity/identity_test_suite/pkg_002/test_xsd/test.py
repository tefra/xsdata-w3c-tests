from dataclasses import dataclass, field
from typing import List, Optional, Type, Union
from xml.etree.ElementTree import QName

__NAMESPACE__ = "foo"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "foo"

    key_or_ref: List[Union["Root.Key", "Root.Ref"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "key",
                    "type": Type["Root.Key"],
                },
                {
                    "name": "ref",
                    "type": Type["Root.Ref"],
                },
            ),
        },
    )

    @dataclass
    class Key:
        value: Optional[QName] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class Ref:
        value: Optional[QName] = field(
            default=None,
            metadata={
                "required": True,
            },
        )
