from django.shortcuts import render, get_object_or_404, redirect
from item.models import Item
from .models import Messages
from .forms import ContactMessagesForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')

    conversations = Messages.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations:
        return redirect("conversation:message_detail",pk=conversations.first().id)
    if request.method == "POST":
        form = ContactMessagesForm(request.POST)

        if form.is_valid():
            conversation = Messages.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_messages = form.save(commit=False)
            conversation_messages.conversation = conversation
            conversation_messages.created_by = request.user
            conversation_messages.save()

            return redirect('item:detail', pk=item_pk)

    else:
        form = ContactMessagesForm()

    return render(request, 'conversation/new_message.html', {
        "form": form,
    })


@login_required
def inbox_messages(request):
    conversations = Messages.objects.filter(members__in=[request.user.id])

    return render(request, 'conversation/inbox.html', {
        "conversations": conversations
    })


@login_required
def message_detail(request, pk):
    conversation = Messages.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = ContactMessagesForm(request.POST)
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation.created_by = request.user
            conversation_message.save()
            conversation.save()

            return redirect('conversation:message_detail')

    else:
        form = ContactMessagesForm()

    return render(request, "conversation/message_detail.html", {
        "conversation": conversation,
        "form": form,
    })
