# to sort by column

def sort_lines(input_file, output_file, primary_index, secondary_index, delimiter):

    with open(input_file,'r') as f:
        lines = f.readlines()

    header = lines[:2]
    body = lines[2:]

    sorted_lines = sorted(body, key= lambda x: (
            x.split(delimiter)[primary_index].lower(),
            x.split(delimiter)[secondary_index].lower()
        )
    )

    with open(output_file,'w') as f:
        f.writelines(sorted_lines)

input_file = 'md_list.md'
output_file = '03_result_column.md'

sort_lines(input_file, output_file,2,1,'|')

#primary_index is the first sort parameter
#secondary_index is the second sort parameter
#delimiter is for split, here for example the seperator is '|'
#it dosen't matter how many blanks are in between a '|' and another '|'