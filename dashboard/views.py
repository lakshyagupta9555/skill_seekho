from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from users.models import Skill
from .models import SkillMatch

@login_required
def home(request):
    my_skills = Skill.objects.filter(user=request.user)
    
    # Find matching skills
    teach_skills = my_skills.filter(can_teach=True)
    learn_skills = my_skills.filter(want_to_learn=True)
    
    # Get potential matches
    potential_matches = Skill.objects.filter(
        Q(can_teach=True, name__in=learn_skills.values_list('name', flat=True)) |
        Q(want_to_learn=True, name__in=teach_skills.values_list('name', flat=True))
    ).exclude(user=request.user).select_related('user')[:10]
    
    context = {
        'my_skills': my_skills,
        'potential_matches': potential_matches,
    }
    return render(request, 'dashboard/home.html', context)

@login_required
def browse_skills(request):
    skill_type = request.GET.get('type', '')
    search = request.GET.get('search', '')
    
    skills = Skill.objects.exclude(user=request.user).select_related('user')
    
    if skill_type:
        skills = skills.filter(skill_type=skill_type)
    if search:
        skills = skills.filter(Q(name__icontains=search) | Q(description__icontains=search))
    
    context = {
        'skills': skills,
        'skill_type': skill_type,
        'search': search,
    }
    return render(request, 'dashboard/browse_skills.html', context)

@login_required
def send_match_request(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)
    if skill.user == request.user:
        messages.error(request, 'Cannot send match request to yourself!')
        return redirect('dashboard:home')
    
    # Check if already sent
    existing = SkillMatch.objects.filter(user=request.user, matched_user=skill.user, skill=skill).exists()
    if existing:
        messages.info(request, 'Match request already sent!')
    else:
        SkillMatch.objects.create(user=request.user, matched_user=skill.user, skill=skill)
        messages.success(request, 'Match request sent!')
    
    return redirect('dashboard:browse_skills')

@login_required
def my_matches(request):
    sent = SkillMatch.objects.filter(user=request.user).select_related('matched_user', 'skill')
    received = SkillMatch.objects.filter(matched_user=request.user).select_related('user', 'skill')
    
    context = {
        'sent_matches': sent,
        'received_matches': received,
    }
    return render(request, 'dashboard/my_matches.html', context)

@login_required
def accept_match(request, match_id):
    match = get_object_or_404(SkillMatch, id=match_id, matched_user=request.user)
    match.status = 'accepted'
    match.save()
    messages.success(request, 'Match accepted! You can now chat.')
    return redirect('dashboard:my_matches')

@login_required
def reject_match(request, match_id):
    match = get_object_or_404(SkillMatch, id=match_id, matched_user=request.user)
    match.status = 'rejected'
    match.save()
    messages.info(request, 'Match rejected.')
    return redirect('dashboard:my_matches')
