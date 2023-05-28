import dis


from interpreter import Interpreter
from virtual_machine import VirtualMachine


if __name__ == "__main__":
	what_to_execute = {
        "instructions": [("LOAD_VALUE", 0),
                         ("STORE_NAME", 0),
                         ("LOAD_VALUE", 1),
                         ("STORE_NAME", 1),
                         ("LOAD_NAME", 0),
                         ("LOAD_NAME", 1),
                         ("ADD_TWO_VALUES", None),
                         ("PRINT_ANSWER", None)],
        "numbers": [1, 2],
        "names":   ["a", "b"] }
	interpreter = Interpreter()
	interpreter.run_code(what_to_execute)

	vm = VirtualMachine()
	print(vm.run_code(compile("1+3", "test", "exec")))
	

