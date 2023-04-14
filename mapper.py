# This script contains functions for getting the daily quote


def get_quotes_map():
    # For each section do the following:
    # Read first line as date
    # Read the following lines as content, stop at "*"
    # quotes[date] = content

    quotes = {}

    with open("ProdSource.txt", "r") as infile:

        count = 0

        while True:

            # Date
            date = infile.readline().strip()
            if "ENDOFFILE" in date:
                break
            else:
                date = date[:-2]

            # Content
            content = ""
            next_line = infile.readline()
            while ("*" not in next_line):
                content += next_line
                next_line = infile.readline()

            # Map
            quotes[date] = content

            count += 1
            if count > 370:
                break

        # print(quotes)
        # for key in quotes:
        #     print(key)
    return quotes


from datetime import date
def get_today_quote(quotes_map):
    today = date.today()
    month = today.month
    print(month)
    day = today.day
    print(day)

    # Convert date to string 
    # Example: 4 2 to April 2

    date_string = today.strftime("%B") + f" {today.day}"

    # print(f"date string {date_string}")

    # print(f"Today's quote for {date_string}:")

    return f"Today's quote for {date_string}:\n\n" + quotes_map[date_string]

if __name__ == "__main__":
    quotes_map = get_quotes_map()
    # print("main")
    print(get_today_quote(quotes_map))