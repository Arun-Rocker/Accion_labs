from collections import defaultdict
import re

class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.error_ips = defaultdict(int)
        self.pattern = re.compile(
            r'^(?P<ip>\d+\.\d+\.\d+\.\d+).*HTTP.*"(?P<status>[4-5]\d{2})'
        )

    def analyze(self):
        """Analyze the log file and count error IPs"""
        with open(self.log_file, 'r') as file:
            for line in file:
                match = self.pattern.match(line)
                if match:
                    ip = match.group('ip')
                    self.error_ips[ip] += 1

    def get_results(self):
        """Get results sorted by frequency"""
        return sorted(
            self.error_ips.items(),
            key=lambda item: item[1],
            reverse=True
        )

# Usage
if __name__ == "__main__":
    analyzer = LogAnalyzer('access.log')
    analyzer.analyze()
    results = analyzer.get_results()
    
    print("IP Address\tError Count")
    print("----------------------------")
    for ip, count in results:
        print(f"{ip}\t{count}")