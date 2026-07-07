import os
import shutil
from datetime import datetime

class LogAnalyzer:
    CRITICAL_WORDS = {'critical', 'error', 'fatal', 'failure', 'failed', 'warning', 'warn', 'exception'}
    
    def __init__(self, log_path):
        self.log_path = log_path.strip('"').strip("'")
        self.backup_dir = None
    
    def analyze(self):
        if not os.path.exists(self.log_path):
            raise FileNotFoundError("Log file not found.")
        
        # Create backup directory first
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.backup_dir = os.path.join(os.getcwd(), f"Backup_{timestamp}")
        os.makedirs(self.backup_dir, exist_ok=True)
        
        # Filter and write directly to backup directory
        output_file = os.path.join(self.backup_dir, "filtered_errors.txt")
        count = 0
        
        with open(self.log_path, "r", encoding="utf-8") as file_in, \
             open(output_file, "w", encoding="utf-8") as file_out:
            
            for line in file_in:
                line_lower = line.lower()
                if any(word in line_lower for word in self.CRITICAL_WORDS):
                    file_out.write(line)
                    count += 1
        
        if count == 0:
            print("[i] No critical lines found.")
            return
        
        print(f"[+] Found {count} critical lines.")
        self._archive()
    
    def _archive(self):
        """Create zip archive of backup directory."""
        zip_path = shutil.make_archive(
            base_name=self.backup_dir,  # Where to save + name
            format="zip",
            root_dir=self.backup_dir    # What to archive
        )
        print(f"[+] Archive created: {zip_path}")

if __name__ == "__main__":
    try:
        path = input("Enter the log file path: ")
        analyzer = LogAnalyzer(path)
        analyzer.analyze()
    except FileNotFoundError as e:
        print(f"[-] Error: {e}")
    except PermissionError:
        print("[-] Error: Permission denied.")