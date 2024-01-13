# python Files
## open
file = open(filename, mode)
contents = file.read()
print(contents)
file.close() # for resource or use with open(filename,mode) as file

## write
file.write("new file.txt) #mode a=append, r=read, w=write


# Day 25 - Pandas
pandas doc: https://pandas.pydata.org/docs/#pandas-documentation

pandas API reference: https://pandas.pydata.org/docs/reference/index.html
### 002 Reading CSV Data in Python
CSV --> pandas(pip install pandas, pandas.read_csv(any.csv))
### DataFrames & Series Working with Rows & Columns
type(data) --> DataFrames(single sheet) or series(single column like List)
Example;
data_dict = {"name":["daniel","abebe"],
        "score":[90,98]
}

data = pandas.DataFrames(data_dict)




