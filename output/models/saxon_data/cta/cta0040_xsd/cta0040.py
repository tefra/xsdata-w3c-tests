from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Appendix:
    """
    :ivar dm_fsd_wu:
    :ivar dm_fsd_wu:
    :ivar dm_fsd_wu:
    :ivar d_hlw_zq:
    """
    class Meta:
        name = "appendix"

    dm_fsd_wu: Optional[str] = field(
        default=None,
    )
    dm_fsd_wu: Optional[str] = field(
        default=None,
    )
    dm_fsd_wu: Optional[str] = field(
        default=None,
    )
    d_hlw_zq: Optional[str] = field(
        default=None,
        metadata=dict(
            name="type",
            type="Attribute"
        )
    )


@dataclass
class Chap:
    """
    :ivar dm_fsd_wu:
    :ivar dm_fsd_wu:
    :ivar dm_fsd_wu:
    :ivar d_hlw_zq:
    """
    class Meta:
        name = "chap"

    dm_fsd_wu: Optional[str] = field(
        default=None,
    )
    dm_fsd_wu: Optional[str] = field(
        default=None,
    )
    dm_fsd_wu: Optional[str] = field(
        default=None,
    )
    d_hlw_zq: Optional[str] = field(
        default=None,
        metadata=dict(
            name="type",
            type="Attribute"
        )
    )


@dataclass
class Doc:
    """
    :ivar appendix:
    :ivar chap:
    """
    class Meta:
        name = "doc"

    appendix: List[Appendix] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    chap: List[Chap] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
