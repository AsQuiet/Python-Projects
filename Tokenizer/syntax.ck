<assignment> := <data-type> <identifier> = <expression>

<data-type> := s (string) | b (bool) | n (number)

<identifier> := *

<function-call> := <identifier> : 

C CHUNK chunk

C chunk_var 34
D chunk_function x y
    R ADD: x ADD: x SUB: x 5
END

C chunk_result chunk::chunk_function: 5 5

END
