import subprocess as sb

class Pop():
    def __init__(self, command, *params, output_path='-', stdout_type=sb.PIPE):
        self.command = command
        self.name = self.command
        self.params = params
        self.output_path = output_path
        self.stdout_type = stdout_type
        self.process = None
        self.content = None
        self.text = None

    def _makeargs(self):
        return (self.command, *self.params, self.output_path)

    def run(self):
        if not self.process:
            self.process = sb.Popen(self._makeargs(), stdout=self.stdout_type)
            self.content = self.process.communicate()[0]
            self.text = self.content.decode('utf-8')
        return self.process


