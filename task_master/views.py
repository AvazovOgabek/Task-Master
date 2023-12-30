from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Task

@login_required(login_url='signin')
def reviews(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    tasks = Task.objects.filter(user=user_profile)
    if user_profile.tasks_count > 0:
        done_percentage = (user_profile.done / user_profile.tasks_count) * 100
        
        is_expected_percentage = ((user_profile.tasks_count - user_profile.done) / user_profile.tasks_count) * 100

    else:
        done_percentage = 0
        is_expected_percentage = 0

    
    if request.method == "POST":
        name = request.POST.get('name')
        if name:
            user_profile.tasks_count += 1
            user_profile.save()
            Task.objects.create(user=user_profile, name=name)
        return redirect('reviews')

    return render(request, 'reviews.html', {'user_profile': user_profile, 'tasks': tasks, 'done_percentage': done_percentage, 'is_expected_percentage': is_expected_percentage})

@login_required(login_url='signin')
def delete_task(request, task_id):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    
    task = get_object_or_404(Task, id=task_id, user=user_profile)
    user_profile.tasks_count -= 1
    user_profile.save()
    
    task.delete()
    return redirect('reviews')

@login_required(login_url='signin')
def done_task(request, task_id):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    
    user_profile.done += 1
    user_profile.save()
    
    task = get_object_or_404(Task, id=task_id, user=user_profile)
    task.delete()
    return redirect('reviews')
