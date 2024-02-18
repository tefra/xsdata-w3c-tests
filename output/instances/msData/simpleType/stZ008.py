from output.models.ms_data.simple_type.st_z008_xsd.st_z008 import Root
from output.models.ms_data.simple_type.st_z008_xsd.st_z008 import T1
from output.models.ms_data.simple_type.st_z008_xsd.st_z008 import T2


obj = Root(
    e1=[
        T1(
            value='123'
        ),
    ],
    e2=[
        T2(
            att='123'
        ),
    ]
)
