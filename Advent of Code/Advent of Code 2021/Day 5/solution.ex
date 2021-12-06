defmodule Main do
	def line_points(line) do
		x0 = Enum.at(Enum.at(line, 0), 0)
		x1 = Enum.at(Enum.at(line, 1), 0)
		y0 = Enum.at(Enum.at(line, 0), 1)
		y1 = Enum.at(Enum.at(line, 1), 1)

		cond do
			x0 == x1 ->
				for n <- y0..y1, do: [x0, n]
			y0 == y1 ->
				for n <- x0..x1, do: [n, y0]
			true ->
				[]
		end
	end
end

{:ok, contents} = File.read("input.txt")

lines = contents \
	|> String.split("\n") \
	|> Enum.map(fn x -> String.split(x, " -> ") |> Enum.map(fn y -> String.split(y, ",") |> Enum.map(&String.to_integer/1) end) end)

points = lines |> Enum.map(fn line -> Main.line_points(line) end)

vents = List.foldl(points, [], fn x, acc -> Enum.concat(x, acc) end) |> 
	Enum.reduce(%{}, fn x, acc -> Map.update(acc, x, 1, &(&1 + 1)) end)

IO.inspect(Enum.count(for {key, value} <- vents, value > 1, into: %{}, do: {key, value}))