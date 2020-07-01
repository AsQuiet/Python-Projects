// (extremely simple) Calculator CLI written in chunk 30/06

CHUNK calc::

    D get_input::

        C>> NUM1 root::input:"type in number one : "
        C>> OPER root::input:"type in the operator : "
        C>> NUM2 root::input:"type in the second number : "

        CON temp_ NUM1 ! "exit"
        IF temp_
            > calc::calculate:NUM1, NUM2, OPER
        END IF
    
    END D

    D calculate::a, b, operator

        C>> a_ root::float:a
        C>> b_ root::float:b

        CON temp_ operator = "+"
        IF temp_
            COP result a_ + b_
            > root::print:"result is : %v", result 
        END IF   

        CON temp_ operator = "-"
        IF temp_
            COP result a_ - b_
            > root::print:"result is : %v", result 
        END IF   

        CON temp_ operator = "/"
        IF temp_
            COP result a_ / b_
            > root::print:"result is : %v", result 
        END IF   

        CON temp_ operator = "*"
        IF temp_
            COP result a_ * b_
            > root::print:"result is : %v", result 
        END IF    

        > calc::get_input:

    END D

END CHUNK

> calc::get_input:

/* Printing out an array

LIST arr 1,2,3,4,5,6,7,8,9,0

D loop::arr_, i

    C>> arr_len root::list_get_length:"arr_"
    CON temp_ i < arr_len

    IF temp_
        C>> el root::list_get_element:"arr_", i
        C>> el root::int:el
        > root::print:el
        COP i2 i + 1
        CALL loop:arr_, i2
    END IF

END D

CALL loop:arr, 0

*/