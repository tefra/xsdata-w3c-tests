from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlPeriod

__NAMESPACE__ = "http://www.tempuri.org"


@dataclass
class TestDate:
    class Meta:
        name = "testDate"
        namespace = "http://www.tempuri.org"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class TestGday:
    class Meta:
        name = "testGDay"
        namespace = "http://www.tempuri.org"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class TestGmonth:
    class Meta:
        name = "testGMonth"
        namespace = "http://www.tempuri.org"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class TestGmonthDay:
    class Meta:
        name = "testGMonthDay"
        namespace = "http://www.tempuri.org"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class TestGyear:
    class Meta:
        name = "testGYear"
        namespace = "http://www.tempuri.org"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class TestGyearMonth:
    class Meta:
        name = "testGYearMonth"
        namespace = "http://www.tempuri.org"

    value: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://www.tempuri.org"

    test_date: list[TestDate] = field(
        default_factory=list,
        metadata={
            "name": "testDate",
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
    test_gyear_month: list[TestGyearMonth] = field(
        default_factory=list,
        metadata={
            "name": "testGYearMonth",
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
    test_gmonth_day: list[TestGmonthDay] = field(
        default_factory=list,
        metadata={
            "name": "testGMonthDay",
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
    test_gday: list[TestGday] = field(
        default_factory=list,
        metadata={
            "name": "testGDay",
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
    test_gmonth: list[TestGmonth] = field(
        default_factory=list,
        metadata={
            "name": "testGMonth",
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
    test_gyear: list[TestGyear] = field(
        default_factory=list,
        metadata={
            "name": "testGYear",
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
