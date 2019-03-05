'''
 * Program or Lab 8: Extra Credit PPM Viewer
 *
 * Programmer: João Veloso
 *
 * Due Date: December 7, 2016
 *
 * COMP141, Fall 2016
 *
 * Pledge: I have neither given nor received unauthorized aid
 *         on this program. 
 *
 * Description: Processing functions, user input functions and main function
 *
 * Input: User inputs image file
 *        User inputs 'y' or 'n' to decide on modifications for image.
 *
 * Output: Outputs a PPM file with given modifications.
 *
'''
import Veloso_Joao_mod8 as mod

#standard process header given in class
def process_header(in_file, out_file):
    magic_line = in_file.readline()
    magic_string = magic_line.strip()
    if magic_string != 'P3':
        print('File is not a P3 PPM file, cannot process, exiting')
        sys.exit(1)
    out_file.write(magic_line)
    width_height_line = in_file.readline()
    width_height = width_height_line.split()
    width = int(width_height[0])
    height = int(width_height[1])
    out_file.write(width_height_line)
    max_color_line = in_file.readline()
    max_color = int(max_color_line.strip())
    out_file.write(max_color_line)
    return width, height, max_color

#calls for a yes or no from user
def options():
    #indexes of this list are useful to call for specific changes in image
    yes_or_no = []
    print('Here are your choices:')
    print('[1] convert to grayscale\n[2] flip horizontally')
    print('[3] negative of red\n[4] negative of green\n[5] negative of blue')
    print('[6] just the reds\n[7] just the greens\n[8] just the blues')
    x = 1
    while x < 9:
        choice = input('Do you want [%d]? (y/n)' % x)
        go = True
        while go: #necessary loop, which is not exited until user inputs y or n
            if choice == 'y':
                go = False
            elif choice == 'n':
                go = False
            else:
                print('Enter y or n')
                choice = input('Do you want [%d]? (y/n)' % x)
        yes_or_no.append(choice)
        x += 1
    return yes_or_no
        
def process(in_file, out_file):
    width, height, max_color = process_header(in_file, out_file)
    yes_or_no = options()
    #loops without horizontal change
    if yes_or_no[1] == 'n':
        for line in in_file:
            values = line.split()
            r = values[0]
            g = values[1]
            b = values[2]
            if yes_or_no[0] == 'y':
                r, g, b = mod.gray_scale(r, g, b, max_color)
            if yes_or_no[2] == 'y':
                r, g, b = mod.flatten_red(r, g, b, max_color)
            if yes_or_no[3] == 'y':
                r, g, b = mod.flatten_green(r, g, b, max_color)
            if yes_or_no[4] == 'y':
                r, g, b = mod.flatten_blue(r, g, b, max_color)
            if yes_or_no[5] == 'y':
                r, g, b = mod.negate_red(r, g, b, max_color)
            if yes_or_no[6] == 'y':
                r, g, b = mod.negate_green(r, g, b, max_color)
            if yes_or_no[7] == 'y':
                r, g, b = mod.negate_blue(r, g, b, max_color)
            out_file.write('%3s, %3s, %3s\n' % (r, g, b))
    #loops with horizontal change (not functioning properly)
    if yes_or_no[1] == 'y':
        reversedlist = mod.flip_horizontal(in_file, width)
        for values in reversedlist:
            r = values[0]
            g = values[1]
            b = values[2]
            if yes_or_no[0] == 'y':
                r, g, b = mod.gray_scale(r, g, b, max_color)
            if yes_or_no[2] == 'y':
                r, g, b = mod.flatten_red(r, g, b, max_color)
            if yes_or_no[3] == 'y':
                r, g, b = mod.flatten_green(r, g, b, max_color)
            if yes_or_no[4] == 'y':
                r, g, b = mod.flatten_blue(r, g, b, max_color)
            if yes_or_no[5] == 'y':
                r, g, b = mod.negate_red(r, g, b, max_color)
            if yes_or_no[6] == 'y':
                r, g, b = mod.negate_green(r, g, b, max_color)
            if yes_or_no[7] == 'y':
                r, g, b = mod.negate_blue(r, g, b, max_color)
            out_file.write('%3s, %3s, %3s\n' % (r, g, b))

def main():
    print('Portable Pixmap (PPM) Image Editor\n')
    in_file_name = input('Enter input file name: ')
    out_file_name = input('Enter output file name: ')
    with open(in_file_name) as in_file:
        with open(out_file_name, 'w') as out_file:
            process(in_file, out_file)

if __name__ == '__main__':
    main()

