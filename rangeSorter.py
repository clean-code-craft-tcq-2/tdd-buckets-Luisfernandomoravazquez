class range_class():
    def __init__(self, minValue, maxValue):
        self.minValue = minValue
        self.maxValue = maxValue
        self.counter = 0
    
    def is_in_range_num(self, value):
        if( value >= self.minValue and value <= self.maxValue):
            return 1
        else:
            return 0

    def analyze_list(self, list):
        # self.counter = 0
        for element in list:
            self.counter += self.is_in_range_num(element)

    def get_comma_separated_line(self):
        return "{}-{},{}".format(self.minValue,self.maxValue,self.counter)

# def string_to_csv_file(string):
#     text_file = open("output.csv", "w")
#     n = text_file.write(string)
#     text_file.close()


def sort_in_ranges(toSort_lst):
    ranges = [range_class(3,5),range_class(10,12)]
    csvText = ""
    for range in ranges:
        range.analyze_list(toSort_lst)
        csvText += range.get_comma_separated_line()+"\n"
    return csvText
    # string_to_csv_file(csvText)
