
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .forms import NoteForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm, TODOForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView 
from .models import Note, Profile, TODO, StudyMaterials

# Register view
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Registration Successful!')
            return redirect('/login')
        else:
            messages.error(request, "There was an error with your registration.")
    else:
        form = UserRegisterForm()    
    return render(request, 'core/register.html', {'form': form})

# Profile view
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('/profile')
        else:
            messages.error(request, "Please correct the error below.")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'core/profile.html', context)

# ToDo views
@login_required
def todo(request):
    form = TODOForm()
    todos = TODO.objects.filter(user=request.user).order_by('due_date', '-priority')
    context = {
        'form': form,
        'todos': todos
    }
    return render(request, 'core/todo.html', context)

@login_required
def add_todo(request):
    if request.method == 'POST':
        form = TODOForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            messages.success(request, 'ToDo added successfully')
            return redirect("/to-dos")
        else:
            messages.error(request, "There was an error adding your ToDo.")
    else:
        form = TODOForm()

    return render(request, 'core/todo.html', {'form': form})

@login_required
def delete_todo(request, id):
    TODO.objects.get(pk=id).delete()
    messages.success(request, 'ToDo deleted successfully')
    return redirect("/to-dos")

@login_required
def edit_todo(request, pk):
    todo = get_object_or_404(TODO, pk=pk)
    if request.method == 'POST':
        form = TODOForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Changes saved')
            return redirect('to-dos')
        else:
            messages.error(request, "There was an error saving changes.")
    else:
        form = TODOForm(instance=todo)
    
    return render(request, 'core/edit_todo.html', {'form': form})

@login_required
def change_todo(request, id, status):
    todo = TODO.objects.get(pk=id)
    todo.status = status
    todo.save()
    messages.success(request, 'Status changed successfully')
    return redirect("/to-dos")

# Notes views
@login_required
def notes(request):
    user = request.user
    docid = int(request.GET.get('docid', 0))
    documents = Note.objects.filter(user=user)

    if request.method == 'POST':
        docid = int(request.POST.get('docid', 0))
        title = request.POST.get('title')
        content = request.POST.get('content', '')

        if not title:
            messages.error(request, "Please enter a title.")
            return redirect('/notes/?docid=%i' % docid)

        if docid > 0:
            document = get_object_or_404(Note, pk=docid, user=user)
            document.title = title
            document.content = content
            document.save()
            messages.success(request, 'Note updated successfully')
        else:
            document = Note.objects.create(title=title, content=content, user=user)
            messages.success(request, 'Note created successfully')

        return redirect('/notes/?docid=%i' % document.id)

    if docid > 0:
        document = get_object_or_404(Note, pk=docid, user=user)
    else:
        document = None

    context = {
        'docid': docid,
        'documents': documents,
        'document': document
    }
    return render(request, 'core/notes.html', context)

@login_required
def delete_note(request, docid):
    user = request.user
    document = Note.objects.get(pk=docid, user=user)
    document.delete()
    messages.success(request, 'Note deleted successfully')
    return redirect('/notes/?docid=0')

# Updated StudyMaterialListView to handle categories
class StudyMaterialListView(ListView):
    model = StudyMaterials
    template_name = 'core/materials_list.html'
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the list of categories from subject choices
        categories = [choice[0] for choice in StudyMaterials.subject_choices]
        selected_category = self.request.GET.get('category')
        
        # Filter materials by selected category if any
        if selected_category:
            context['object_list'] = StudyMaterials.objects.filter(subject=selected_category)
        else:
            context['object_list'] = StudyMaterials.objects.all()
        
        context['categories'] = categories
        context['selected_category'] = selected_category
        return context

class StudyMaterialDetailView(DetailView):
    model = StudyMaterials
    template_name = 'core/material_detail.html'
    context_object_name = 'studymaterial'
