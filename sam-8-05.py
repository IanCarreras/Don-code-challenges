# Print out all of the strings in the following array in alphabetical order, 
# each on a separate line.

array = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']

# The expected output is:
# 'Cha Cha'
# 'Foxtrot'
# 'Jive'
# 'Paso Doble'
# 'Rumba'
# 'Samba'
# 'Tango'
# 'Viennese Waltz'
# 'Waltz'

def alphabetical(arr):
    arr.sort()
    for element in arr:
        print(f'{element}')

alphabetical(array)

def alphabeticalByMiddleLetter(arr):
    pass