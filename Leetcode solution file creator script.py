from Lib import textwrap

num = input('Num of file:')
desc = input('Description of problem:')

wrapper = textwrap.TextWrapper(initial_indent=' ', subsequent_indent='# ')

f= open("Problem("+ num +" - Solution.py","w+")

f.write("# Problem "+ num +": ")
f.write("\n")
f.write("\n")
f.write("# " + wrapper.fill(desc) )
f.write("\n")
f.write("\n")
f.write("# Solution:")
f.write("\n")
