# 📊 The Number Cruncher

Type a list of numbers and this Python script works out their **mean**, **median** and **mode**.

## Example

```
Enter numbers separated by space: 4 8 2 8 5
Mean: 5.4
Median: 5
Mode: 8
```

## How it works

- **Mean:** the sum divided by the count
- **Median:** sort the list and take the middle value
- **Mode:** the value that appears most often, `max(numbers, key=numbers.count)`

## Run it

```bash
python the-number-cruncher.py
```

## Known limitations

- For an even count of numbers, it returns the upper of the two middle values instead of their average.
- Only whole numbers are accepted.

Python's built-in `statistics` module (`mean`, `median`, `mode`) handles both cases and is a good next step.
