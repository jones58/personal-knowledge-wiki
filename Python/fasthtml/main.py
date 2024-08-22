from fasthtml.common import *


def render(todo):
    tid=f'todo-{todo.ROWID}'
    toggle = A(('[x]' if todo.done else '[ ]'), hx_get=f"/toggle/{todo.ROWID}", target_id=f'{tid}')
    delete = A( "Delete", hx_delete=f"/{todo.ROWID}",hx_swap="outerHTML", target_id=f'{tid}')
    return Li(toggle, todo.title, delete, id=tid)


app,rt,todos,Todo = fast_app("todos.db", live=True, ROWID=int, title=str, done=bool, pk='ROWID', render=render)

def mk_input(): return Input(placeholder="add new todo", id="title", hx_swap_oob="true")
@rt("/")
def get():
    frm = Form(Group(mk_input(),
               Button("Add")),
        hx_post="/", target_id="todo-list", hx_swap="beforeend")
    return Titled("Todos",
                  Card(
                    Ul(*todos(), id="todo-list"),
                    header=frm)
                  )

@rt("/{tid}")
def delete(tid:int): todos.delete(tid)

@rt("/")
def post (todo:Todo): return todos.insert(todo), mk_input() # type: ignore


@rt("/toggle/{tid}")
def get(tid:int):
    todo = todos[tid]
    todo.done=not todo.done
    return todos.update(todo)

serve()
