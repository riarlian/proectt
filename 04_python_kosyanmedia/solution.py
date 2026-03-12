import csv


def read_data(filename):
    rows = []

    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            rows.append(
                {
                    "name": row["name"],
                    "age": int(row["age"]),
                    "salary": int(row["salary"]),
                }
            )

    return rows


def calculate_stats(data):
    total_age = sum(item["age"] for item in data)
    total_salary = sum(item["salary"] for item in data)

    count = len(data)

    avg_age = total_age / count
    avg_salary = total_salary / count

    return avg_age, avg_salary, count


def main():
    filename = "data.csv"

    data = read_data(filename)

    avg_age, avg_salary, count = calculate_stats(data)

    print("Employees:", count)
    print("Average age:", round(avg_age, 2))
    print("Average salary:", round(avg_salary, 2))


if __name__ == "__main__":
    main()