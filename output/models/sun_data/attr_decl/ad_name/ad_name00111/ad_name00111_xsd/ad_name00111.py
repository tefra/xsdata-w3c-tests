from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "AttrDecl/name"


@dataclass
class Root:
    """
    :ivar a_a:
    :ivar b_b:
    :ivar c_c:
    :ivar d_d:
    :ivar e_e:
    :ivar f_f:
    :ivar g_g:
    """
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    a_a: Optional[int] = field(
        default=None,
        metadata={
            "name": "a--a",
            "type": "Attribute",
        }
    )
    b_b: Optional[int] = field(
        default=None,
        metadata={
            "name": "b..b",
            "type": "Attribute",
        }
    )
    c_c: Optional[int] = field(
        default=None,
        metadata={
            "name": "c__c",
            "type": "Attribute",
        }
    )
    d_d: Optional[int] = field(
        default=None,
        metadata={
            "name": "d··d",
            "type": "Attribute",
        }
    )
    e_e: Optional[int] = field(
        default=None,
        metadata={
            "name": "e··e",
            "type": "Attribute",
        }
    )
    f_f: Optional[int] = field(
        default=None,
        metadata={
            "name": "f۝۝f",
            "type": "Attribute",
        }
    )
    g_g: Optional[int] = field(
        default=None,
        metadata={
            "name": "g۞۞g",
            "type": "Attribute",
        }
    )
