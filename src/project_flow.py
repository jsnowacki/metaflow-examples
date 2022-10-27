from metaflow import FlowSpec, step, project, current

@project(name='example_project')
class ProjectFlow(FlowSpec):

    @step
    def start(self):
        print('project name:', current.project_name)
        print('project branch:', current.branch_name)
        print('is this a production run?', current.is_production)
        self.next(self.end)

    @step
    def end(self):
        pass

if __name__ == '__main__':
    ProjectFlow()