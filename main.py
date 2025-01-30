import os
import subprocess
import sys

def run_rq_script(rq_number):
    main_script_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(
        main_script_dir, 
        "rqs_scripts", 
        f"rq{rq_number}.py"
    )
    
    if not os.path.exists(script_path):
        print(f"Error: RQ script '{script_path}' does not exist.")
        return
    
    try:
        subprocess.run([sys.executable, script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running RQ script: {e}")

def run_count_results():
    main_script_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(
        main_script_dir, 
        "results_rqs", 
        "count_results.py"
    )
    
    if not os.path.exists(script_path):
        print(f"Error: Results script '{script_path}' not found.")
        return
    
    try:
        
        subprocess.run([sys.executable, script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running results script: {e}")

def handle_rq_selection():
    while True:
        print("\nAvailable RQ scripts:")
        print("1. rq1.py\n2. rq2.py\n3. rq3.py\n4. rq4.py\n5. rq5.py")
        choice = input("Enter RQ number (1-5) or 'back': ").strip().lower()
        
        if choice == "back":
            break
        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice. Try again.")
            continue
        
        run_rq_script(choice)

def main():
    while True:
        print("\n=== Main Menu ===")
        print("1. Run RQ scripts")
        print("2. Calculate results")
        print("exit. Quit")
        main_choice = input("Choose an option (1/2/exit): ").strip().lower()
        
        if main_choice == "exit":
            print("Exiting...")
            break
        elif main_choice == "1":
            handle_rq_selection()
        elif main_choice == "2":
            print("\nRunning results calculation...")
            run_count_results()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()