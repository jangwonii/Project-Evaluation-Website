from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Rating

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'projects/project_detail.html', {'project': project})

def rate_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
        score = request.POST.get('score')
        comment = request.POST.get('comment', '')
        
        if score and score.isdigit() and 1 <= int(score) <= 5:
            Rating.objects.create(
                project=project,
                score=int(score),
                comment=comment
            )
            return redirect('projects:project_results')
    
    return redirect('projects:project_detail', project_id=project_id)

def project_results(request):
    projects = Project.objects.all()
    projects = sorted(projects, key=lambda x: x.average_rating, reverse=True)
    return render(request, 'projects/project_results.html', {'projects': projects})
