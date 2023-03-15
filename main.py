import Parser
import SCNFandSDNF


def main():
    function = input()
    table_of_variables = []
    logic_object= Parser.Formula(function)
    output_list, table_of_variables = logic_object.output_logic_list()
    SCNFandSDNF.separator_of_logic_solutions(output_list, table_of_variables)


if __name__ == '__main__':
    main()
