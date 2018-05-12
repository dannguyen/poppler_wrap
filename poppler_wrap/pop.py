import subprocess as sb

class Pop():
    def __init__(self, command, *params, stdout_type=sb.PIPE):
        self.command = command
        self.name = self.command
        self.params = params
#        self.output_path = output_path # this should be removed at somepoint
        self.stdout_type = stdout_type # this should be removed at somepoint
        self.process = None
        self.content = None
        self.text = None

    def _makeargs(self):
        return (self.command, *self.params)

    def statement(self):
        return ' '.join(str(a) for a in self._makeargs())

    def run(self):
        if not self.process:
            cmdargs = [str(a) for a in self._makeargs()]
            self.process = sb.Popen(cmdargs, stdout=self.stdout_type)
            # args = ('pdftotext', '-layout', '-f', 1, '-l', 1, 'examples/docs/hellobye.pdf', '-')
            # self.process = sb.Popen(args, stdout=self.stdout_type)
            self.content = self.process.communicate()[0].strip()
            self.text = self.content.decode('utf-8')
        return self.process


    def has_run(self):
        return self.process is not None


    def to_dict(self):
        d = {
            'command': self.command,
            'name': self.name,
            'params': self.params,
            'text': self.text,
            'has_run': self.has_run(),
        }
        return d
