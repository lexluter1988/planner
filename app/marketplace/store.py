auth = {
    'name': 'auth',
    'description': 'Authentication Module',
    'status': 'installed',
    'settings': [
        {
            'parameter': 'auth_engine',
            'description': 'Default Security Engine for Auth',
            'value': 'flask'
        },
        {
            'parameter': 'password_complexity',
            'description': 'Complexity of Passwords',
            'value': '0'
        },
        {
            'parameter': 'expiration_days',
            'description': 'Password Expiration in days',
            'value': '-1'
        },
    ]
}

notes = {
    'name': 'notes',
    'description': 'Notes application',
    'status': 'installed',
    'settings': [
        {
            'parameter': 'max_notes',
            'description': 'Maximum Notes allowed for user',
            'value': '-1'
        },
    ]
}

projects = {
    'name': 'projects',
    'description': 'Projects Module',
    'status': 'available',
    'settings': [
        {
            'parameter': 'default_project',
            'description': 'Default Project used for tasks with no ordering',
            'value': 'default'
        },
    ]
}


tasks = {
    'name': 'tasks',
    'description': 'Tasks Module',
    'status': 'available',
    'settings': [
        {
            'parameter': 'max_tasks',
            'description': 'Maximum tasks for user',
            'value': '50'
        },
    ]
}


pipelines = {
    'name': 'pipelines',
    'description': 'Pipelines Module',
    'status': 'available',
    'settings': [
        {
            'parameter': 'max_tasks_pipeline',
            'description': 'Maximum tasks in one pipeline',
            'value': '20'
        },
    ]
}

milestones = {
    'name': 'milestones',
    'description': 'Milestones module',
    'status': 'available',
    'settings': [
        {
            'parameter': 'max_milestones',
            'description': 'Maximum milestones',
            'value': '20'
        },
    ]
}

catalog = [
    auth,
    notes,
    tasks,
    projects,
    milestones,
    pipelines
]
