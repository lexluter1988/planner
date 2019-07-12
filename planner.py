from app import create_app, db
from app.models import User, Task, Note, Project, Milestone, ApplicationStore, Setting, PipelineTask, Pipeline

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Note': Note, 'Task': Task,
            'Project': Project, 'Milestone': Milestone,
            'Setting': Setting, 'PipelineTask': PipelineTask,
            'ApplicationStore': ApplicationStore, 'Pipeline': Pipeline}
