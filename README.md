# TRowe_assessment

Assumptions:
I assumed that any metacharacters and/or punction would not be counted as part of the length of any given word.
I assumed that users would pass in a string that was not empty to the method. This is type-hinted.
I assumed unit test data was not being passed from file. 

Test Execution Instructions:
1. Make sure pytest is installed on the machine
2. In a terminal, navigate to the top directory of the repository
3. Run "pytest --junitxml=results.xml sentence_parser.py"
    Note: the step above assumes pytest is installed in the repository, or that a virtual environment is activated that contains it in its site-packages directory. 
4. Examine the results.xml file created in the cwd for the test results