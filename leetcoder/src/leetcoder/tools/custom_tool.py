from crewai_tools import BaseTool

class PythonCompiler(BaseTool):
  name: str = "Python code compiler"
  description: str = ("Helps to compiler python code. Accepts the python code as a valid string "
                      "and uses the compile() function to compile it. If the code has syntactical errors,"
                      "this tool returns the error, otherwise it returns None. This tool can be useful for a "
                      "debugging expert to validate whether a given python code has errors or not.")

  def _run(self, argument: str) -> str:
    try:
      compile(argument, '', 'exec')
    except Exception as e:
      return str(e)
    return 'The code is completely CORRECT and has no errors.'
