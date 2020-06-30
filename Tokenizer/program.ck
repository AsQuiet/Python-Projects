D toRadians:: degrees

    COP pi_180 3.1415 / 180
    COP rad degrees * pi_180
    RETURN rad 

END D

CCALL c toRadians: 360
> root::print:c
