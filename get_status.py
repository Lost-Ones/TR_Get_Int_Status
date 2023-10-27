import re, sys
from dataclasses import dataclass
from collections import defaultdict


#  use https://www.onlinegdb.com/online_python_compiler

@dataclass
class GetSection():
    text : list
    start : str
    stop : str

    def get_sections(self):
        results = defaultdict(list)
        for line in self.text:
            if re.match(f'{self.start}.+', line):
                key = re.match(f'{self.start}.+', line)
                if key:
                    results[key[0]].append(line)
                    go = 1
                    continue
            if results:
                if go == 1:
                    if self.stop not in line:
                        results[key[0]].append(line)
                        continue
                    else:
                        results[key[0]].append(line)
                        go = 0
                        continue
        return results

def get_input():
    """Gets input from the user and saves it to a variable."""
    input_text = sys.stdin.read()
    return input_text


def save_input(input_text):
    """Saves the input text to a variable."""
    global user_inputS
    user_input = input_text


def main():
    """The main function."""
    input_text = get_input()
    save_input(input_text)
    # Convert the user_input into a list with each element a new line.
    lines = re.split("\n", input_text)
    return lines

if __name__ == "__main__":
    print('''\n

##############################################################################
        ############################################################

               DONT NOT paste in any password into the script.

        ############################################################
##############################################################################

''')

    print("\nNext, paste in 'show interface' output: hit <enter> then ctrl + d when done (Windows ctrl + z)\n")
    interface_text = main()
    #you have the dict but need to clean up the key and the variable to have only needed info and short name the interface
    start = 'Gi\S+|Te\S+|Fa\S+|Fi\S+|Twe\S+|Hu\S+'
    stop = 'underruns'
    # involks the dataclass to create the list of interfaces that have had no output.
    data = GetSection(text=interface_text, start=start, stop=stop)
    interface_results = data.get_sections()

    interface_dict = {}
    for k,v in interface_results.items():
        temp = {}
        for item in v:

            status_list = ['connected', 'notconnect', 'monitoring']

            for option in status_list:
                if option in item:
                    status = option
                    temp['status'] = status


        interface_dict[k] = temp


    print('\n\n ---------------------------------------  Data Output --------------------------------------')
    print('\n -------------------------------------------------------------------------------------------\n')
    for k,v in interface_dict.items():
        print(f'{k}, {v["status"]}')
