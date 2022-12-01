def read_file():
    with open(f"{__file__.strip('.py')} - Input.txt", "r") as f:
        lines = f.read().split("\n")
        earliest_timestamp = int(lines[0])
        timestamps = lines[1].split(",")

        return earliest_timestamp, timestamps

def part_1(earliest_timestamp, timestamps):
    timestamps = [int(timestamp) for timestamp in timestamps if timestamp != "x"]

    current_timestamp = earliest_timestamp

    while True:
        for timestamp in timestamps:
            if current_timestamp % timestamp == 0: 
                time = current_timestamp - earliest_timestamp

                return time * timestamp

        current_timestamp += 1

def part_2(timestamps):
    timestamps = [int(timestamp) if timestamp != "x" else timestamp for timestamp in timestamps]

    time, step = 1, 1

    for i, timestamp in enumerate(timestamps):
        if timestamp != "x":
            while (time + i) % timestamp != 0:
                time += step

            step *= timestamp

    return time

earliest_timestamp, timestamps = read_file()

print(f"Part 1: {part_1(earliest_timestamp, timestamps)}")
print(f"Part 2: {part_2(timestamps)}")
