from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .forms import CommentForm
from .models import Comment




def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            captcha_response = form.cleaned_data['captcha']
            if captcha_response:
                form.save()
                return redirect('comments:thanks')
            else:
                form.add_error('captcha', 'Invalid CAPTCHA')
        else:
            pass
    else:
        form = CommentForm()
    return render(request, 'comments/add_comment.html', {'form': form})






def thanks(request):
    return render(request, 'comments/thanks.html')



def comments(request):
    
    comments_list = Comment.objects.filter(parent_comment=None)

    sort_by = request.GET.get('sort_by', 'created_at')

    if 'username' in sort_by :
        comments_list = comments_list.order_by('user_name')
    elif 'email' in sort_by:
        comments_list = comments_list.order_by('email')
    else:
        comments_list = comments_list.order_by('-created_at')

    if 'asc' in sort_by:
        comments_list = comments_list.reverse()
    paginator = Paginator(comments_list, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'comments/comments.html', {'page_obj': page_obj})



def add_answer(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        text = request.POST.get('text')
        parent_comment_id = request.POST.get('parent_comment_id')
        parent_comment = None
        print(parent_comment_id)
        if parent_comment_id:
            parent_comment = Comment.objects.get(id=parent_comment_id)
        comment = Comment.objects.create(user_name=user_name, email=email, text=text, parent_comment=parent_comment)
        return redirect('comments:comments')
    return render(request, 'comments/add_answer.html')
