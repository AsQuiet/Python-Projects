D func::

    > root::print:5


END D

CALL func:

/*
CHUNK chunk_::

    C chunk_var "quinten"

    D func:: x
    RETURN 55
    END D

END CHUNK

C> chunk_var chunk_::chunk_var
C>> chunk_func_result chunk_::func: 5, 12
*/