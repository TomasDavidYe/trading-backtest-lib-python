
from datetime import datetime


class PrintLogger:
    def __init__(self, show_debug=True):
        super().__init__()
        self.log_file = ''
        self.show_debug = show_debug

    def prefix(self):
        return datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    def log(self, label, message):
        log_line = f'{self.prefix()} {label}: {message}'
        print(log_line)



    def info(self, message):
        self.log(label='INFO', message=message)

    def error(self, message):
        self.log(label='ERROR', message=message)

    def debug(self, message):
        if self.show_debug:
            self.log(label='DEBUG', message=message)
