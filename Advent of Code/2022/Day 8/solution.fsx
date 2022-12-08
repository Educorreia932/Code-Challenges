open System.IO

let inline getRow (array: int array array) i = array.[i]  

let inline getColumn (array: int array array) j = array |> Seq.map (fun line -> line.[j]) |> Seq.toArray

let isTreeVisible (heights: int array array) i j = 
    let maximum_height = heights.[i].[j]
    let row = getRow heights i
    let column = getColumn heights j
    let isOnEdge = i = 0 || i = heights.Length - 1 || j = 0 || j = heights.[0].Length - 1
    let isNotHidden = List.contains true ([
            row[.. j - 1];
            row[j + 1 ..];
            column[.. i - 1];
            column[i + 1 ..]
        ] |> List.map (Array.forall (fun value -> value < maximum_height)))

    isOnEdge || isNotHidden

let inline charToInt c = int c - int '0'

let partOne (heights: int array array) = 
    let height = heights.Length
    let width = heights.[0].Length 

    seq {
        for i in 0 .. height - 1 do
            for j in 0 .. width - 1 ->
                isTreeVisible heights i j
    } |> Seq.sumBy (function | true -> 1 | false -> 0)

let readInput = 
    File.ReadLines("input.txt")
        |> Seq.map (fun line -> line |> Seq.map charToInt |> Seq.toArray)
        |> Seq.toArray

let heights = readInput

printf "%d" (partOne heights)
