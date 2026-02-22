from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from django.utils import timezone
from .models import VideoCall
import uuid

@login_required
def video_call_list(request):
    calls = VideoCall.objects.filter(
        Q(caller=request.user) | Q(receiver=request.user)
    ).order_by('-started_at')[:20]
    return render(request, 'video/call_list.html', {'calls': calls})

@login_required
def start_call(request, user_id):
    receiver = get_object_or_404(User, id=user_id)
    if receiver == request.user:
        return redirect('dashboard:home')
    
    room_id = str(uuid.uuid4())
    call = VideoCall.objects.create(
        caller=request.user,
        receiver=receiver,
        room_id=room_id,
        status='calling'
    )
    
    return redirect('video:video_room', room_id=room_id)

@login_required
def video_room(request, room_id):
    call = get_object_or_404(VideoCall, room_id=room_id)
    
    # Check if user is participant
    if call.caller != request.user and call.receiver != request.user:
        return redirect('dashboard:home')
    
    # Don't allow joining ended calls
    if call.status == 'ended':
        return redirect('video:call_list')
    
    if call.status == 'calling':
        call.status = 'active'
        call.save()
    
    context = {
        'call': call,
        'room_id': room_id,
    }
    return render(request, 'video/video_room.html', context)

@login_required
def end_call(request, room_id):
    call = get_object_or_404(VideoCall, room_id=room_id)
    
    # Check if user is participant
    if call.caller != request.user and call.receiver != request.user:
        return JsonResponse({'error': 'Not authorized'}, status=403)
    
    # Only end if not already ended
    if call.status != 'ended':
        call.status = 'ended'
        call.ended_at = timezone.now()
        
        # Calculate duration in seconds
        if call.started_at:
            duration = (call.ended_at - call.started_at).total_seconds()
            call.duration = int(duration)
        
        call.save()
    
    return JsonResponse({'status': 'success'})
