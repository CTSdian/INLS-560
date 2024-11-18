def sort_lines(input_file, output_file):

    with open(input_file,'r') as f:
        lines = f.readlines()

    sorted_lines = sorted(lines, key= lambda x:x[12].lower())
    # 12 for first name
    # 30 for last name

    with open(output_file,'w') as f:
        f.writelines(sorted_lines)

input_file = 'md_list.md'
output_file = '01_result_first.md'

sort_lines(input_file, output_file)