
from crewai.utilities.events import TaskCompletedEvent
from crewai.utilities.events.base_event_listener import BaseEventListener

class StreamlitTaskListener(BaseEventListener):
    def __init__(self, update_callback):
        super().__init__()
        self.update_callback = update_callback

    def setup_listeners(self, crewai_event_bus):
        @crewai_event_bus.on(TaskCompletedEvent)
        def on_task_completed(source, event):
            task_name = event.task.name
            output = event.output
            print(f"Task completed: {task_name} with output: {output}")
            self.update_callback(task_name, output)
