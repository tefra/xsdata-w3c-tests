from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Root:
    """
    :ivar token:
    :ivar language:
    :ivar name:
    :ivar ncname:
    :ivar id:
    :ivar idref:
    :ivar idrefs:
    :ivar nmtoken:
    :ivar nmtokens:
    """
    class Meta:
        name = "root"

    token: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    language: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    ncname: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    idref: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    idrefs: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    nmtoken: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    nmtokens: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            required=True,
            tokens=True
        )
    )
