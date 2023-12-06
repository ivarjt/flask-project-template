
# flask-project-template
My flask project template that i use

## Getting Started

### Prerequisites
- Python 3.11.2 (Other versions will most likely work fine if you are using newer libraries as well.)

### Installing (windows)
```
git clone https://github.com/ivarjt/flask-project-template.git
cd flask-project-template
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
python run.py
```

## Deployment
Change `RUN_IN_DEBUG_MODE=True` to `RUN_IN_DEBUG_MODE=False` in [`__init__.py`](https://github.com/ivarjt/flask-project-template/blob/main/app/__init__.py) if you want to run the project in production mode, otherwise leave it as is.

## License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/ivarjt/flask-project-template/blob/main/LICENSE) file for details
