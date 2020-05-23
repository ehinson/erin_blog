import time
from rq import get_current_job
from app import create_app, db
from app.models import Task


# Because this is going to run in a separate process,
# I need to initialize Flask-SQLAlchemy and Flask-Mail,
# which in turn need a Flask application instance from which to get their configuration.
# So I'm going to add a Flask application instance and application context at the top of the app/tasks.py module:
app = create_app()
app.app_context().push()

# def example(seconds):
#     job = get_current_job()
#     print('Starting task')
#     for i in range(seconds):
#         job.meta['progress'] = 100.0 * i / seconds
#         job.save_meta()
#         print(i)
#         time.sleep(1)
#     job.meta['progress'] = 100
#     job.save_meta()
#     print('Task completed')

def _set_task_progress(progress):
    job = get_current_job()
    if job:
        job.meta['progress'] = progress
        job.save_meta()
        task = Task.query.get(job.get_id())
        task.user.add_notification('task_progress', {'task_id': job.get_id(), 'progress': progress})
        if progress >= 100:
            task.complete = True
        # I needed to be very careful in how I designed the parent task (add_notification) to not make any database changes,
        # since this commit call would write those as well
        db.session.commit()