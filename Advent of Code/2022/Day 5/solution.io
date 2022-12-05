List transposed := method(
    originalList := call target 
    transposedList := originalList at(0) map(i, v, list)

    originalList foreach(
        i, 
        row, 
        row foreach(
            j,
            value,
            transposedList at(j) append(value)
        )
    )

    transposedList
)

partOne := method(
    input,
    stacks := input at(0)
    instructions := input at(1)

    instructions foreach(
        i,
        instruction,
        quantity := instruction at(0)
        origin := instruction at(1) - 1
        target := instruction at(2) - 1

        quantity repeat(
            box := stacks at(origin) pop
            stacks at(target) append(box)
        )
    )

    stacks map(last) join
)

partTwo := method(
    input,
    stacks := input at(0)
    instructions := input at(1)

    instructions foreach(
        i,
        instruction,
        quantity := instruction at(0)
        origin := instruction at(1) - 1
        target := instruction at(2) - 1

        moving_stack := list()

        quantity repeat(
            box := stacks at(origin) pop
            moving_stack prepend(box)
        )

        moving_stack foreach(
            i, v,
            stacks at(target) append(v)
        )
    )

    stacks map(last) join
)

readInput := method(
    file := File with("./input.txt")
    file openForReading
    lines := file readLines 
    file close

    i := lines indexOf("")

    stacks := lines slice(0, i - 1)
    instructions := lines slice(i + 1)

    stacks mapInPlace(
        value,
        value asList select(i, v, i % 4 - 1 == 0) 
    ) 

    stacks = stacks transposed map(
        i,
        row,
        row remove(" ") reverse
    )

    instructions mapInPlace(
        value,
        value split select(i, v, v != "move" and v != "from" and v != "to") map(asNumber)
    )

    list(stacks, instructions)
)   

input := readInput  

partOne(input) println

input := readInput  

partTwo(input) println
