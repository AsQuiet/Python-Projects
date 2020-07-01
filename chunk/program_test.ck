> root::print: "Testing out every feature of the chunk language..."

// Testing out arrays
LIST arr 1,2,3,4,5,6,7,8,9,10
> root::print:arr

// adding a var
> root::list_append: "arr", 11

// removing vars
> root::list_remove_first: "arr"
> root::list_remove_last: "arr"
> root::list_remove_index: "arr", 5

// getting data
C>> len root::list_get_length:"arr"
C>> element root::list_get_element: "arr", 0
C>> index root::list_get_index: "arr", 2


> root::print:"list is %v, length is %v, element at 0th index is %v, index of 2 is %v", arr, len, element, index

CHUNK chunk::

    LIST arr 1,2,3

    D print::string, string2
        > root::print:string
        > root::print:string2
    END D

END CHUNK

C> arr_ chunk::arr
> root::print:arr_
> root::print:"done with testing out the lists.. moving on to functions and chunks.."

D print::string
    > root::print:string
END D

CALL print:"lol"
> chunk::print:"lol1", "lol1"

// testing out operations

COP a 15 - 5 
COP b a * 2
COP c a + b
COP c c * 3 
// result should be 90
CALL print:c


D do_something::
    RETURN 5
END D

CCALL f do_something:
CALL print:f


// testing out input
C>> user_input root::input:"type in name : "
CALL print:user_input

// screwing up some memory
R "chunk::arr" 5
C> lol chunk::arr

> root::print:lol