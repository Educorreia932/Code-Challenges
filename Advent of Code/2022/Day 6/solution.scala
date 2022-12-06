import scala.io.Source

object Solution {
	def uniqueCharacters(s: String) = s.groupBy(c => c).keys.toList

	def findMarker(datastream: String, length: Int): Int = {
		for (i <- length until datastream.length) {
			val slice = datastream.slice(i - length, i)

			if (uniqueCharacters(slice).length == slice.length)
				return i
		}

		-1
	}
	
	def partOne(datastream: String): Int = {
		findMarker(datastream, 4)
	}

	def partTwo(datastream: String): Int = {
		findMarker(datastream, 14)
	}

	def readInput(): String = {
		val bufferedSource = Source.fromResource("input.txt")
		val input = bufferedSource.getLines
		val datastream = input.iterator.next()

		bufferedSource.close

		datastream
	}

	def main(args: Array[String]): Unit = {
		val input = readInput()

		println(partOne(input))
		println(partTwo(input))
	}
}
