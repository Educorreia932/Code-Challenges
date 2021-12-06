defmodule Main do
	def line_points(line, diagonal) do
		x0 = Enum.at(Enum.at(line, 0), 0)
		x1 = Enum.at(Enum.at(line, 1), 0)
		y0 = Enum.at(Enum.at(line, 0), 1)
		y1 = Enum.at(Enum.at(line, 1), 1)

		cond do
			x0 == x1 ->
				for y <- y0..y1, do: [x0, y]
			y0 == y1 ->
				for x <- x0..x1, do: [x, y0]
			y0 < y1 and diagonal ->
				for {x, i} <- Enum.with_index(x0..x1), do: [x, y0 + i]
			y0 > y1 and diagonal ->
				for {x, i} <- Enum.with_index(x0..x1), do: [x, y0 - i]
			true ->
				[]
		end
	end

	def count_overlaps(lines, diagonal) do 
		points = lines |> Enum.map(fn line -> Main.line_points(line, diagonal) end)

		vents = List.foldl(points, [], fn x, acc -> Enum.concat(x, acc) end) |> 
			Enum.reduce(%{}, fn x, acc -> Map.update(acc, x, 1, &(&1 + 1)) end)

		Enum.count(for {key, value} <- vents, value > 1, into: %{}, do: {key, value})
	end

	def part_one(lines) do
		count_overlaps(lines, false)
	end 

	def part_two(lines) do
		count_overlaps(lines, true)
	end 
end

{:ok, contents} = File.read("input.txt")

lines = contents \
	|> String.split("\n") \
	|> Enum.map(fn x -> String.split(x, " -> ") |> Enum.map(fn y -> String.split(y, ",") |> Enum.map(&String.to_integer/1) end) end)

IO.puts("Part 1: #{Main.part_one(lines)}")
IO.puts("Part 2: #{Main.part_two(lines)}")
