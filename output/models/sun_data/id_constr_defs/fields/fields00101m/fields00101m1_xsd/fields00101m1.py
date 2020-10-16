from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "IdConstrDefs/fields"


@dataclass
class People:
    """
    :ivar person:
    """
    class Meta:
        name = "people"
        namespace = "IdConstrDefs/fields"

    person: List["People.Person"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Person:
        """
        :ivar value:
        :ivar parent:
        :ivar birthday:
        """
        value: Optional[str] = field(
            default=None,
        )
        parent: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
        birthday: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
