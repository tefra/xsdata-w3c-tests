from output.models.ms_data.particles.particles_z012_xsd.particles_z012 import E1
from output.models.ms_data.particles.particles_z012_xsd.particles_z012 import E2
from output.models.ms_data.particles.particles_z012_xsd.particles_z012 import E3
from output.models.ms_data.particles.particles_z012_xsd.particles_z012 import MyType10Value
from output.models.ms_data.particles.particles_z012_xsd.particles_z012 import Root


obj = Root(
    e2_or_e1_or_e3=[
        E1(
            value=1
        ),
        E1(
            value=True
        ),
        E1(
            value=False
        ),
        E1(
            value=MyType10Value.X
        ),
        E1(
            value=MyType10Value.Y
        ),
        E2(
            value=1
        ),
        E3(
            att1=123
        ),
    ]
)
