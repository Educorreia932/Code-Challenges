open System.IO

let inline getRow (array: int array array) i = array.[i]  
let inline getColumn (array: int array array) j = array |> Seq.map (fun line -> line.[j]) |> Seq.toArray
let inline charToInt c = int c - int '0'

let isTreeVisible (trees: int array array) i j = 
    let maximum_height = trees.[i].[j]
    let row = getRow trees i
    let column = getColumn trees j
    let isOnEdge = i = 0 || i = trees.Length - 1 || j = 0 || j = trees.[0].Length - 1
    let isNotHidden = List.contains true ([
            row[.. j - 1];
            row[j + 1 ..];
            column[.. i - 1];
            column[i + 1 ..]
        ] |> List.map (Array.forall (fun value -> value < maximum_height)))

    isOnEdge || isNotHidden

let viewingDistance view maximum_height = 
    match view 
        |> Seq.map (fun value -> value < maximum_height) 
        |> Seq.tryFindIndex ((=) false) with
            | Some index -> (index + 1)
            | None -> (view |> Seq.toList |> List.length)

let scenicScore (trees: int array array) i j = 
    let maximum_height = trees.[i].[j]
    let row = getRow trees i
    let column = getColumn trees j

    [
        row[.. j - 1] |> Seq.rev;
        row[j + 1 ..];
        column[.. i - 1] |> Seq.rev;
        column[i + 1 ..]
    ] |> List.map (fun view -> (viewingDistance view maximum_height)) |> Seq.fold (*) 1

let partOne (trees: int array array) = 
    let height = trees.Length
    let width = trees.[0].Length 

    seq {
        for i in 0 .. height - 1 do
            for j in 0 .. width - 1 ->
                isTreeVisible trees i j
    } |> Seq.sumBy (function | true -> 1 | false -> 0)

let partTwo (trees: int array array) = 
    let height = trees.Length
    let width = trees.[0].Length 

    seq {
        for i in 0 .. height - 1 do
            for j in 0 .. width - 1 ->
                scenicScore trees i j
    } |> Seq.max

let readInput = 
    File.ReadLines("input.txt")
        |> Seq.map (fun line -> line |> Seq.map charToInt |> Seq.toArray)
        |> Seq.toArray

let trees = readInput

// printfn "%d" (partOne trees)
printfn "%d" (partTwo trees)
