import subprocess

def install_if_not_exists(package):
    try:
        __import__(package)
    except ImportError:
        print(f"Installing {package}...")
        subprocess.check_call(['pip', 'install', package])

# List your dependencies
dependencies = ['requests', 'numpy', 'pandas', 'matplotlib', 'scikit-learn', 'openpyxl']

# Install missing dependencies
for dependency in dependencies:
    install_if_not_exists(dependency)
    
from ui_element.metricstics_app import MetricsticsApp

if __name__ == "__main__":
    app = MetricsticsApp()
    app.mainloop()
