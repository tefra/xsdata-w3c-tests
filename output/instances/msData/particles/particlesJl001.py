from output.models.ms_data.particles.particles_jl001_xsd.particles_jl001 import Doc
from output.models.ms_data.particles.particles_jl001_xsd.particles_jl001 import R
from output.models.ms_data.particles.particles_jl001_xsd.particles_jl001_imp import ImpElem1
from xsdata.formats.dataclass.models.generics import AnyElement


obj = Doc(
    elem=R(
        imp_elem1=ImpElem1(
            any_element=AnyElement(
                text='testing'
            )
        )
    )
)
