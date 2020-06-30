
D loop::i, max

    CON continue i < max
    IF continue
        > root::print:"looping again"
        COP i2 i + 1
        CALL loop:i2, max
    END IF
END D

CALL loop:0,5