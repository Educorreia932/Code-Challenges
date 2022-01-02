import { readFileSync } from "fs"

const matches = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}

function part_one(input) {
    const scores = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }

    let total_score = 0

    for (const line of input) {
        const tokens = []
        let illegal = false;

        for (var token of line) {
            tokens.push(token);

            const found_match = matches[token] == tokens[tokens.length - 2];
            const closing_token = Object.keys(matches).includes(token);

            if (tokens.length > 1) {
                if (closing_token && !found_match) {
                    illegal = true;

                    break;
                }

                else if (found_match && tokens.length > 1) {
                    tokens.pop();
                    tokens.pop();
                }
            }
        }

        if (illegal)
            total_score += scores[token];
    }

    return total_score
}

function part_two(input) {
    const scores = {
        "(": 1,
        "[": 2,
        "{": 3,
        "<": 4
    }

    let line_scores = []

    for (const line of input) {
        const tokens = []
        let illegal = false;
        let score = 0;

        for (const token of line) {
            tokens.push(token);

            const found_match = matches[token] == tokens[tokens.length - 2];
            const closing_token = Object.keys(matches).includes(token);

            if (tokens.length > 1) {
                if (closing_token && !found_match) {
                    illegal = true;

                    break;
                }

                else if (found_match && tokens.length > 1) {
                    tokens.pop();
                    tokens.pop();
                }
            }
        }

        if (!illegal) {
            for (const token of tokens.slice().reverse())
                score = score * 5 + scores[token];

            line_scores.push(score)
        }
    }

    line_scores.sort(function (a, b) {
        return a - b;
    });

    return line_scores[Math.floor(line_scores.length / 2)]
}

const input = readFileSync("input.txt", "utf-8").split("\n");

console.log(`Part 1: ${part_one(input)}`)
console.log(`Part 2: ${part_two(input)}`)
