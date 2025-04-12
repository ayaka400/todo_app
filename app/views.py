from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.http import Http404

# todoリスト・新規作成フォーム表示
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'app/index.html', {'tasks': tasks, 'form': form})


# 削除ボタン
def delete_task(request, task_id):    
    try:
        task = Task.objects.get(id=task_id)
        task.delete()
    except Task.DoseNotExist:
        raise Http404("そのタスクは存在しません。")
    return redirect('index')


# 完了ボタン
def complete_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.completed = not task.completed
        task.save()
    except Task.DoseNotExist:
        raise Http404("タスクが存在しません。")
    return redirect('index')
