from output.models.ms_data.particles.particles_ib001_xsd.particles_ib001 import Base
from output.models.ms_data.particles.particles_ib001_xsd.particles_ib001 import Doc


obj = Doc(
    foo_or_foo1=[
        Base.Foo(
            value=True
        ),
        Base.Foo(
            value=True
        ),
    ]
)
