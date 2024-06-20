
import flet

# window drawing logic
def main(page: flet.Page):
    page.title = "TODO application"
    page.theme_mode = "auto"
    
    # on addnew click -> react
    def add_task(e):
        page.add(
            flet.Checkbox(
                label=new_task.value
                )
            )
        new_task.value = ""
        page.update()
        pass

    # on return key -> react
    def return_add_task(e:flet.KeyboardEvent):
        if e.key == flet.KeyboardEvent.ctrl:
            page.add(
                flet.Checkbox(
                    label=new_task.value
                    )
                )
            new_task.value = ""
            page.update()
        pass

    # setup task-textbox
    new_task:flet.TextField = flet.TextField(
       hint_text="Task, what needs to complete today",
       #key=return_add_task # textbox unfocus D:
       )

    hint_label:flet.Text = flet.Text(
        value="Welcome. This is my first flet-app",
        size=21
        )

    # construct window-columns
    # it looks like:
    #   |====================|
    #   | textfield | button |
    #   |--------------------|
    task_view:flet.Column = flet.Column(
        controls=[
            flet.Row(
                controls=[
                    new_task,
                    flet.FloatingActionButton(
                        icon=flet.icons.ADD,
                        on_click=add_task
                        )
                    ]
                )
            ]
        )

    # draw window elements
    page.add(
        hint_label, 
        task_view
        )
    


flet.app(main)
