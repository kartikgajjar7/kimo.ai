## Installation

Follow these steps to set up **Kimo.ai** on your local machine:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/kartikgajjar7/kimo.ai.git
   cd kimo.ai
   ```

2. **Set Up the Environment**

   It's recommended to use a virtual environment.

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```
## Usage

Provide instructions and examples on how to use your project after installation.
1. Run the load_courses.py file 
 ```bash
cd scripts
python3 load_courses.py 
```

2. run the server 

 ```bash
uvicorn app.main:app --reload
```
