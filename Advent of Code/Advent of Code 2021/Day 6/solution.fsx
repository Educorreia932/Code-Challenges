open System.IO

let grow fish days =
    let rec loop (fish: int64 array) n =
        match n with
            | n when n = days -> fish |> Seq.sum
            | _ ->
                let day_zero_fish = fish.[0]

                for i in 0 .. 7 do
                    fish.[i] <- fish.[i + 1]

                fish.[6] <- fish.[6] + day_zero_fish
                fish.[8] <- day_zero_fish

                loop fish (n + 1)

    loop fish 0

let part_one fish =
    grow fish 80

let part_two fish =
    grow fish 256

let mutable fish: int64 array = Array.zeroCreate 9
    
(File.ReadLines("input.txt") |> Seq.toArray).[0].Split[|','|] 
    |> Array.map System.Int64.Parse 
    |> Seq.countBy id 
    |> Seq.iter (fun (k, v) -> fish.[int k] <- v)

printfn "Part 1: %d" (part_one (Array.copy fish))
printfn "Part 2: %d" (part_two (Array.copy fish))