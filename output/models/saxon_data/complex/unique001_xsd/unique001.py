from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Root:
    """
    :ivar sub:
    """
    class Meta:
        name = "root"

    sub: List["Root.Sub"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass
    class Sub:
        """
        :ivar idelt:
        """
        idelt: Optional["Root.Sub.Idelt"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "",
                "required": True,
            }
        )

        @dataclass
        class Idelt:
            """
            :ivar value:
            :ivar attr:
            """
            value: Optional[int] = field(
                default=None,
            )
            attr: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                }
            )
