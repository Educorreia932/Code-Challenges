using System.Collections.Generic;
using System.Linq;

namespace Day3 {
	internal static class Day3 {
		private static IEnumerable<string> ReadInput() {
			return System.IO.File.ReadAllLines(@"input.txt");
		}

		private static int Priority(char c) {
			return c % 32 + (char.IsUpper(c) ? 26 : 0);
		}

		private static int PartOne(IEnumerable<string> Lines) {
			return (
				from Line in Lines
				let First = Line.Substring(0, Line.Length / 2)
				let Second = Line.Substring(Line.Length / 2, Line.Length / 2)
				select First.Intersect(Second).Select(Priority).Sum()
			).Sum();
		}

		private static int PartTwo(IEnumerable<string> Lines) {
			return Lines.Select((s, i) => new {s, i})
				.GroupBy(x => x.i / 3)
				.Select(g => g.Select(x => x.s).ToList())
				.Select(l => l[0].Intersect(l[1]).Intersect(l[2]).ToArray()[0])
				.Select(Priority)
				.Sum();
		}

		private static void Main() {
			var Input = ReadInput().ToList();

			System.Console.WriteLine(PartOne(Input));
			System.Console.WriteLine(PartTwo(Input));
		}
	}
}