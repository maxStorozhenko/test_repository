from time import time_ns

from students.models import Logger


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time_ns()

        response = self.get_response(request)

        end = time_ns()
        if request.path.startswith('/admin/'):
            diff = (end - start) // 1_000_000

            with open('admin_logs.log', 'a') as f:
                log = Logger.objects.create(method=request.method, path=request.path, execution_time=diff)
                f.write(f'{log.path} | {log.method} | {log.execution_time} ms | {log.created}\n')

        return response
