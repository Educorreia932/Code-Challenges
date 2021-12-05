import std.stdio;
import std.string;
import std.file;
import std.algorithm;
import std.conv;
import std.array;
import std.range;

class Board {
    public:
        int[][] numbers;
        int[int] marked;

        this(int[][] boardArray) {
            numbers = boardArray;

            foreach (row ; numbers)
                foreach (number ; row)
                    marked[number] = false;
        }

        void markNumber(int number) {
            if (number in marked)
                marked[number] = true;
        }

        int checkRows(int drawnNumber) {
            return check(drawnNumber, false);
        }

        int checkColumns(int drawnNumber) {
            return check(drawnNumber, true);
        }

    private:
        int check(int drawnNumber, bool transpose) {
            foreach(row ; transpose ? transposed(numbers.dup).map!(array).array : numbers) {
                bool completeRow = true;

                foreach (number ; row) 
                    if (!marked[number]) 
                        completeRow = false;

                if (completeRow) {

                    return marked.byPair
                        .filter!(p => !p[1])
                        .map!(pair => pair[0])
                        .sum * drawnNumber;
                }
            }

            return 0;
        }
}

int part_one() {
    return -1;
}

void main() {
    auto lines = readText("input.txt").splitLines();
    auto drawnNumbers = lines[0].split(",").map!(to!int);
    auto boardsLines = lines.split("").remove(0);

    Board[] boards = boardsLines.map!(
        boardLines => new Board(boardLines.map!(
            boardLine => boardLine.split.map!(to!int).array).array
        )
    ).array;

    loop: foreach (drawnNumber ; drawnNumbers) {
        foreach (board ; boards) {
            board.markNumber(drawnNumber);

            int columnCheck = board.checkColumns(drawnNumber);
            int rowCheck = board.checkRows(drawnNumber);

            if (columnCheck != 0) {
                writeln(columnCheck);

                break loop;
            }

            if (rowCheck != 0) {
                writeln(rowCheck);

                break loop;
            }
        }
    }
}
