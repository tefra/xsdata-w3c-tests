from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.tempuri.org"


@dataclass
class TestDate:
    """
    :ivar value:
    """
    class Meta:
        name = "testDate"
        namespace = "http://www.tempuri.org"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TestGday:
    """
    :ivar value:
    """
    class Meta:
        name = "testGDay"
        namespace = "http://www.tempuri.org"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TestGmonth:
    """
    :ivar value:
    """
    class Meta:
        name = "testGMonth"
        namespace = "http://www.tempuri.org"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TestGmonthDay:
    """
    :ivar value:
    """
    class Meta:
        name = "testGMonthDay"
        namespace = "http://www.tempuri.org"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TestGyear:
    """
    :ivar value:
    """
    class Meta:
        name = "testGYear"
        namespace = "http://www.tempuri.org"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class TestGyearMonth:
    """
    :ivar value:
    """
    class Meta:
        name = "testGYearMonth"
        namespace = "http://www.tempuri.org"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Root:
    """
    :ivar test_date:
    :ivar test_gyear_month:
    :ivar test_gmonth_day:
    :ivar test_gday:
    :ivar test_gmonth:
    :ivar test_gyear:
    """
    class Meta:
        name = "root"
        namespace = "http://www.tempuri.org"

    test_date: List[TestDate] = field(
        default_factory=list,
        metadata=dict(
            name="testDate",
            type="Element",
            min_occurs=2,
            max_occurs=2
        )
    )
    test_gyear_month: List[TestGyearMonth] = field(
        default_factory=list,
        metadata=dict(
            name="testGYearMonth",
            type="Element",
            min_occurs=2,
            max_occurs=2
        )
    )
    test_gmonth_day: List[TestGmonthDay] = field(
        default_factory=list,
        metadata=dict(
            name="testGMonthDay",
            type="Element",
            min_occurs=2,
            max_occurs=2
        )
    )
    test_gday: List[TestGday] = field(
        default_factory=list,
        metadata=dict(
            name="testGDay",
            type="Element",
            min_occurs=2,
            max_occurs=2
        )
    )
    test_gmonth: List[TestGmonth] = field(
        default_factory=list,
        metadata=dict(
            name="testGMonth",
            type="Element",
            min_occurs=2,
            max_occurs=2
        )
    )
    test_gyear: List[TestGyear] = field(
        default_factory=list,
        metadata=dict(
            name="testGYear",
            type="Element",
            min_occurs=2,
            max_occurs=2
        )
    )
