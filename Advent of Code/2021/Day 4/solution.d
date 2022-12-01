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

int bingo(bool letSquidWin, int[] drawnNumbers, Board[] boards) {
    ulong[] winners;
    int lastWinnerScore;

    loop: foreach (drawnNumber ; drawnNumbers) {
        foreach (i, board ; boards.enumerate()) {
            board.markNumber(drawnNumber);

            int columnScore = board.checkColumns(drawnNumber);
            int rowScore = board.checkRows(drawnNumber);

            if (columnScore != 0) {
                if (!winners.canFind(i)) {
                    winners ~= i;
                    lastWinnerScore = columnScore;
                }

                if (!letSquidWin)
                    return columnScore;
            }

            if (rowScore != 0) {
                if (!winners.canFind(i)) {
                    winners ~= i;
                    lastWinnerScore = rowScore;
                }

                if (!letSquidWin)
                    return rowScore;
            }
        }
    }

    return lastWinnerScore;
}

int part_one(int[] drawnNumbers, Board[] boards) {
    return bingo(false, drawnNumbers, boards);
}

int part_two(int[] drawnNumbers, Board[] boards) {
    return bingo(true, drawnNumbers, boards);
}

void main() {
    auto lines = readText("input.txt").splitLines();
    int[] drawnNumbers = lines[0].split(",").map!(to!int).array;
    auto boardsLines = lines.split("").remove(0);

    Board[] boards = boardsLines.map!(
        boardLines => new Board(boardLines.map!(
            boardLine => boardLine.split.map!(to!int).array).array
        )
    ).array;

    writeln("Part 1: ", part_one(drawnNumbers, boards));
    writeln("Part 2: ", part_two(drawnNumbers, boards));
}
