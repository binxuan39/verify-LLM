import ollama
import os
import argparse

model = "codellama"
messages = []


# The Initial code completion generation
def init_completion(prompt_path):
    try:
        problem_file = os.path.join(prompt_path, "problem.txt")
        with open(problem_file, "r") as f:
            prompt = f.read()
        # print(prompt)

        init_chat()
        result = chat(prompt)
        save_result(prompt_path, result)
        print("output:")
        print(result)
    except FileNotFoundError:
        print("Prompt file not find")


# Iterative generation based on the previous completion and verification tool output
def iter_completion(prompt_path):
    init_chat()
    try:
        problem_file = os.path.join(prompt_path, "problem.txt")
        java_solution_path = os.path.join(prompt_path, "Solution.java")
        infer_output_path = os.path.join(prompt_path, "infer_output.txt")
        with open(problem_file, "r") as f:
            problem = f.read()
        with open(java_solution_path, "r") as f:
            java_solution = f.read()
        with open(infer_output_path, "r") as f:
            infer_output = f.read()

        prompt = (f"This is the problem and the Java solution: \n{problem} \n ``` java \n{java_solution} \n```\n"
                  f"This solution contains the following bugs, fix the given bugs and output the fixed program: \n {infer_output}")

        # print("prompt:")
        # print(prompt)
        result = chat(prompt)
        save_result(prompt_path, result)
        print("output:")
        print(result)

    except FileNotFoundError:
        print("The Solution.java or infer_output.txt file is not found")


# Initial the chat to let the ChatGPT knows write Java program
def init_chat():
    messages.clear()
    messages.append({"role": "system", "content": "You are a helpful assistant designed to output Java."})
    # print(messages)


def chat(prompt):
    messages.append({"role": "user", "content": prompt})
    completion = ollama.chat(
        model=model,
        messages=messages
    )
    print(completion['message']['content'])
    print(messages)
    return completion['message']['content']


def save_result(path, result):
    output_path = os.path.join(path, "completion.txt")
    with open(output_path, "w") as file:
        file.write(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chat with ChatGPT")
    parser.add_argument("--prompt_path", type=str, help="The relative path to the prompt file")
    parser.add_argument("--mode", type=str, help="init or iter", default="init")

    args = parser.parse_args()
    prompt_path = args.prompt_path

    if prompt_path:
        if args.mode == "init":
            print("Initial generation")
            init_completion(prompt_path)
        elif args.mode == "iter":
            print("Iterative generation based on the previous completion and verification tool output")
            iter_completion(prompt_path)
    else:
        print("Please enter the prompt file with argument --prompt_file")
