from output.models.ms_data.additional.test76423_xsd.test76423 import ClassType
from output.models.ms_data.additional.test76423_xsd.test76423 import EventType
from output.models.ms_data.additional.test76423_xsd.test76423 import EventsType
from output.models.ms_data.additional.test76423_xsd.test76423 import Jsml
from output.models.ms_data.additional.test76423_xsd.test76423 import PropertyType
from output.models.ms_data.additional.test76423_xsd.test76423 import ScopeType


obj = Jsml(
    class_value=[
        ClassType(
            events=EventsType(
                event=[
                    EventType(
                        desc='\n\t\t\t\t\tFired when the singleton instance is created.\n\t\t\t\t',
                        name='InstanceCreated',
                        scope=ScopeType.CLASS
                    ),
                ]
            ),
            property=[
                PropertyType(
                    desc='\n\t\t\t\tSingleton instance, initialized on first access.\n\t\t\t',
                    name='instance',
                    scope=ScopeType.CLASS,
                    type_value='Singleton'
                ),
            ],
            name='Singleton'
        ),
    ]
)
