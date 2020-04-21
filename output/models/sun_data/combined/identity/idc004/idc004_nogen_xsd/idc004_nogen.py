from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.vehicle.org"


@dataclass
class Person:
    """
    :ivar car:
    """
    class Meta:
        name = "person"
        namespace = "http://www.vehicle.org"

    car: List["Person.Car"] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )

    @dataclass
    class Car:
        """
        :ivar reg_state:
        :ivar reg_plate:
        """
        reg_state: Optional[str] = field(
            default=None,
            metadata=dict(
                name="regState",
                type="Attribute"
            )
        )
        reg_plate: Optional[int] = field(
            default=None,
            metadata=dict(
                name="regPlate",
                type="Attribute"
            )
        )


@dataclass
class Vehicle:
    """
    :ivar plate_number:
    :ivar state:
    """
    class Meta:
        name = "vehicle"
        namespace = "http://www.vehicle.org"

    plate_number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="plateNumber",
            type="Attribute"
        )
    )
    state: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class State:
    """
    :ivar code:
    :ivar vehicle:
    :ivar person:
    """
    class Meta:
        name = "state"
        namespace = "http://www.vehicle.org"

    code: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    vehicle: List[Vehicle] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    person: List[Person] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Root:
    """
    :ivar state:
    """
    class Meta:
        name = "root"
        namespace = "http://www.vehicle.org"

    state: List[State] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
