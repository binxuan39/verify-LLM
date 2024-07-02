## Verify LLM

### Prerequestite

- Java 8+
- Python 3.8+

- Infer : version 1.1.0 [Infer Static Analyzer | Infer | Infer (fbinfer.com)](https://fbinfer.com/)
- Ollama [ollama/ollama (github.com)](https://github.com/ollama/ollama)

Install the required model in Ollama

```
ollama pull codellama
```

### Implementation

#### Initial Generation

required file:

```
prompt path
│   problem.txt         - the problem used to prompt the LLM
```

Steps:

1. Run the Python script with the init mode. The argument ``--prompt_path`` should be the directory of your problem.txt

   ```shell
   python main.py --prompt_path codebase/example --mode init
   ```

After this command the script will create a ``completion.txt`` file in the prompt_path directory which includes the completion of the LLM

2. Extract the code from the `completion.txt` and save it into `Solution.java` file in the prompt_path directory to allow Infer to analyze.

3. Run the command to let infer to analyze the `Solution.java`

   ```shell
   infer run -- javac codebase/example/Solution.java
   ```

4. If the Infer provides the errors , then organize the errors and put them into a file called `infer_output.txt` int the prompt_path directory.



#### Iterative Clean up

required file:

```
prompt path
│   problem.txt         - the problem used to prompt the LLM
│		infer_output.txt    - the errors detected by infer
│		Solution.java       - the java completion from the previous iteration
```

Steps:

1. Run the Python script with the iter mode. The argument ``--prompt_path`` should be the directory of your problem.txt

   ```shell
   python main.py --prompt_path codebase/example --mode iter
   ```

After this command the script will create a ``completion.txt`` file in the prompt_path directory which includes the completion of the LLM

2. Extract the code from the `completion.txt` and save it into `Solution.java` file in the prompt_path directory to allow Infer to analyze.

3. Run the command to let infer to analyze the `Solution.java`

   ```shell
   infer run -- javac codebase/example/Solution.java
   ```

4. If the Infer provides the errors , then organize the errors and put them into a file called `infer_output.txt` int the prompt_path directory.
