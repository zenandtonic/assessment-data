log_file = open("um-server-01.txt")
#^create a variable called log_file and assign the text file to said variable^

def sales_reports(log_file):
#^create a new function called sales_reports and tell it to expect log_file as a parameter^
    for line in log_file:
#^start a for in loop^
        line = line.rstrip()
#^create a variable called line and use the rstrip method to remove spaces^
        day = line[0:3]
#^create a variable called day and set it to be the first element in "line" with a character length of three^
        if day == "Mon":
#^if day is "Mon", then...^
            print(line)
#^...print "line"^    


sales_reports(log_file)
#^call the function^