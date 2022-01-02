import { readFileSync } from "fs"

const scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

const matches = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}

const input = readFileSync("input.txt", "utf-8").split("\n");
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

console.log(total_score)
