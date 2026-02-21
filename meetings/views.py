from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db import models
from .models import VideoMeeting
from skills.models import SkillExchange
import uuid

@login_required
def meeting_list(request):
    # Get all meetings where user is participant
    user_exchanges = SkillExchange.objects.filter(
        models.Q(requester=request.user) | models.Q(responder=request.user)
    )
    
    upcoming_meetings = VideoMeeting.objects.filter(
        exchange__in=user_exchanges,
        scheduled_time__gte=timezone.now(),
        status='scheduled'
    ).order_by('scheduled_time')
    
    past_meetings = VideoMeeting.objects.filter(
        exchange__in=user_exchanges,
        status__in=['completed', 'cancelled']
    ).order_by('-scheduled_time')
    
    context = {
        'upcoming_meetings': upcoming_meetings,
        'past_meetings': past_meetings,
    }
    return render(request, 'meetings/meeting_list.html', context)

@login_required
def create_meeting(request, exchange_id):
    exchange = get_object_or_404(SkillExchange, id=exchange_id)
    
    if request.user not in [exchange.requester, exchange.responder]:
        messages.error(request, 'You do not have permission.')
        return redirect('meeting_list')
    
    if request.method == 'POST':
        title = request.POST.get('title')
        scheduled_time = request.POST.get('scheduled_time')
        duration = request.POST.get('duration_minutes', 60)
        notes = request.POST.get('notes', '')
        
        room_id = str(uuid.uuid4())
        
        meeting = VideoMeeting.objects.create(
            exchange=exchange,
            title=title,
            scheduled_time=scheduled_time,
            duration_minutes=duration,
            room_id=room_id,
            notes=notes
        )
        messages.success(request, 'Meeting scheduled successfully!')
        return redirect('meeting_detail', pk=meeting.pk)
    
    context = {
        'exchange': exchange,
    }
    return render(request, 'meetings/create_meeting.html', context)

@login_required
def meeting_detail(request, pk):
    meeting = get_object_or_404(VideoMeeting, pk=pk)
    
    if request.user not in meeting.participants:
        messages.error(request, 'You do not have permission.')
        return redirect('meeting_list')
    
    return render(request, 'meetings/meeting_detail.html', {'meeting': meeting})

@login_required
def join_meeting(request, pk):
    meeting = get_object_or_404(VideoMeeting, pk=pk)
    
    if request.user not in meeting.participants:
        messages.error(request, 'You do not have permission.')
        return redirect('meeting_list')
    
    meeting.status = 'ongoing'
    meeting.save()
    
    context = {
        'meeting': meeting,
        'room_id': meeting.room_id,
    }
    return render(request, 'meetings/video_call.html', context)

@login_required
def end_meeting(request, pk):
    meeting = get_object_or_404(VideoMeeting, pk=pk)
    
    if request.user not in meeting.participants:
        messages.error(request, 'You do not have permission.')
        return redirect('meeting_list')
    
    meeting.status = 'completed'
    meeting.save()
    messages.success(request, 'Meeting ended.')
    return redirect('meeting_detail', pk=pk)

@login_required
def cancel_meeting(request, pk):
    meeting = get_object_or_404(VideoMeeting, pk=pk)
    
    if request.user not in meeting.participants:
        messages.error(request, 'You do not have permission.')
        return redirect('meeting_list')
    
    meeting.status = 'cancelled'
    meeting.save()
    messages.success(request, 'Meeting cancelled.')
    return redirect('meeting_list')
