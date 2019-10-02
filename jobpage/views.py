from django.shortcuts import render
from django.utils import timezone
from jobpage.models import Todo
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

# Create your views here.
def home(request):
    todo_item = Todo.objects.all().order_by("-added_date")

    return render(request,'index.html',{
        "todo_items":todo_item
    })

def add_to(request):
    if request.method == "POST":
        current_date = timezone.now()
        content = request.POST['content']
        todo_obj = Todo.objects.create(added_date=current_date,text=content)
        print(todo_obj)
        print(todo_obj.id)
        return HttpResponseRedirect("/")
    if request.method == "GET":
        return HttpResponseRedirect("/")


def delete_todo(request,todo_id):
    print(todo_id)
    Todo.objects.get(id=todo_id).delete()
    return redirect('/')

