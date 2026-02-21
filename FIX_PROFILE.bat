@echo off
echo Fixing SkillSwap Project...
echo.

REM Delete and recreate empty profile.html
del templates\users\profile.html 2>nul

REM Create new profile.html
(
echo ^{% extends 'base.html' %^}
echo.
echo ^{% block title %^}{{ profile_user.username }}'s Profile - SkillSwap^{% endblock %^}
echo.
echo ^{% block content %^}
echo ^<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8"^>
echo     ^<^!-- Profile Header --^>
echo     ^<div class="bg-gray-800 rounded-lg shadow-lg overflow-hidden mb-8"^>
echo         ^<div class="bg-gradient-to-r from-blue-600 to-purple-600 h-32"^>^</div^>
echo         ^<div class="px-8 pb-8"^>
echo             ^<div class="relative -mt-16 mb-4"^>
echo                 ^{% if profile_user.profile_picture %^}
echo                     ^<img src="{{ profile_user.profile_picture.url }}" 
echo                          alt="{{ profile_user.username }}"
echo                          class="w-32 h-32 rounded-full object-cover border-4 border-gray-800"^>
echo                 ^{% else %^}
echo                     ^<div class="w-32 h-32 rounded-full bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center border-4 border-gray-800"^>
echo                         ^<span class="text-white text-5xl font-bold"^>
echo                             {{ profile_user.username^|first^|upper }}
echo                         ^</span^>
echo                     ^</div^>
echo                 ^{% endif %^}
echo             ^</div^>
echo             ^<div class="flex justify-between items-start"^>
echo                 ^<div^>
echo                     ^<h1 class="text-3xl font-bold text-white mb-2"^>
echo                         {{ profile_user.get_full_name^|default:profile_user.username }}
echo                     ^</h1^>
echo                     ^<p class="text-gray-400 text-lg mb-2"^>@{{ profile_user.username }}^</p^>
echo                     ^{% if profile_user.location %^}
echo                     ^<div class="flex items-center text-gray-400 mb-4"^>
echo                         ^<i class="fas fa-map-marker-alt mr-2"^>^</i^>
echo                         ^<span^>{{ profile_user.location }}^</span^>
echo                     ^</div^>
echo                     ^{% endif %^}
echo                     ^{% if profile_user.bio %^}
echo                     ^<p class="text-gray-300 max-w-3xl"^>{{ profile_user.bio }}^</p^>
echo                     ^{% endif %^}
echo                 ^</div^>
echo                 ^{% if profile_user == user %^}
echo                 ^<a href="^{% url 'edit_profile' %^}" 
echo                    class="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition duration-200"^>
echo                     ^<i class="fas fa-edit mr-2"^>^</i^>Edit Profile
echo                 ^</a^>
echo                 ^{% else %^}
echo                 ^<a href="^{% url 'create_exchange' profile_user.username %^}" 
echo                    class="px-6 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition duration-200"^>
echo                     ^<i class="fas fa-handshake mr-2"^>^</i^>Connect
echo                 ^</a^>
echo                 ^{% endif %^}
echo             ^</div^>
echo         ^</div^>
echo     ^</div^>
echo     ^<div class="grid grid-cols-1 md:grid-cols-2 gap-8"^>
echo         ^<^!-- Teaching Skills --^>
echo         ^<div class="bg-gray-800 rounded-lg shadow-lg p-6"^>
echo             ^<h2 class="text-2xl font-bold text-white mb-6 flex items-center"^>
echo                 ^<i class="fas fa-chalkboard-teacher text-green-500 mr-3"^>^</i^>
echo                 Can Teach
echo             ^</h2^>
echo             ^{% if teaching_skills %^}
echo             ^<div class="space-y-4"^>
echo                 ^{% for skill in teaching_skills %^}
echo                 ^<div class="bg-gray-700 rounded-lg p-4 hover:bg-gray-600 transition duration-200"^>
echo                     ^<div class="flex justify-between items-start mb-2"^>
echo                         ^<h3 class="text-lg font-semibold text-white"^>{{ skill.skill_name }}^</h3^>
echo                         ^<span class="px-3 py-1 bg-green-600 text-white text-xs rounded-full"^>
echo                             {{ skill.get_skill_level_display }}
echo                         ^</span^>
echo                     ^</div^>
echo                     ^<p class="text-gray-300 text-sm mb-2"^>{{ skill.description }}^</p^>
echo                     ^<span class="px-2 py-1 ^{% if skill.is_tech %^}bg-blue-600^{% else %^}bg-purple-600^{% endif %^} text-white text-xs rounded-full"^>
echo                         ^{% if skill.is_tech %^}Tech^{% else %^}Non-Tech^{% endif %^}
echo                     ^</span^>
echo                 ^</div^>
echo                 ^{% endfor %^}
echo             ^</div^>
echo             ^{% else %^}
echo             ^<div class="text-center py-12"^>
echo                 ^<i class="fas fa-graduation-cap text-gray-600 text-6xl mb-4"^>^</i^>
echo                 ^<p class="text-gray-400"^>No teaching skills listed yet^</p^>
echo             ^</div^>
echo             ^{% endif %^}
echo         ^</div^>
echo         ^<^!-- Learning Interests --^>
echo         ^<div class="bg-gray-800 rounded-lg shadow-lg p-6"^>
echo             ^<h2 class="text-2xl font-bold text-white mb-6 flex items-center"^>
echo                 ^<i class="fas fa-book-reader text-purple-500 mr-3"^>^</i^>
echo                 Wants to Learn
echo             ^</h2^>
echo             ^{% if learning_interests %^}
echo             ^<div class="space-y-4"^>
echo                 ^{% for interest in learning_interests %^}
echo                 ^<div class="bg-gray-700 rounded-lg p-4 hover:bg-gray-600 transition duration-200"^>
echo                     ^<h3 class="text-lg font-semibold text-white mb-2"^>{{ interest.skill_name }}^</h3^>
echo                     ^{% if interest.description %^}
echo                     ^<p class="text-gray-300 text-sm mb-2"^>{{ interest.description }}^</p^>
echo                     ^{% endif %^}
echo                     ^<span class="px-2 py-1 ^{% if interest.is_tech %^}bg-blue-600^{% else %^}bg-purple-600^{% endif %^} text-white text-xs rounded-full"^>
echo                         ^{% if interest.is_tech %^}Tech^{% else %^}Non-Tech^{% endif %^}
echo                     ^</span^>
echo                 ^</div^>
echo                 ^{% endfor %^}
echo             ^</div^>
echo             ^{% else %^}
echo             ^<div class="text-center py-12"^>
echo                 ^<i class="fas fa-lightbulb text-gray-600 text-6xl mb-4"^>^</i^>
echo                 ^<p class="text-gray-400"^>No learning interests listed yet^</p^>
echo             ^</div^>
echo             ^{% endif %^}
echo         ^</div^>
echo     ^</div^>
echo     ^{% if profile_user == user %^}
echo     ^<div class="mt-8 flex justify-center space-x-4"^>
echo         ^<a href="^{% url 'add_skill' %^}" 
echo            class="px-6 py-3 bg-green-600 text-white rounded-lg hover:bg-green-700 transition duration-200"^>
echo             ^<i class="fas fa-plus mr-2"^>^</i^>Add Teaching Skill
echo         ^</a^>
echo         ^<a href="^{% url 'add_interest' %^}" 
echo            class="px-6 py-3 bg-purple-600 text-white rounded-lg hover:bg-purple-700 transition duration-200"^>
echo             ^<i class="fas fa-plus mr-2"^>^</i^>Add Learning Interest
echo         ^</a^>
echo     ^</div^>
echo     ^{% endif %^}
echo ^</div^>
echo ^{% endblock %^}
) > templates\users\profile.html

echo Profile template created successfully!
echo.
echo Now run: python manage.py runserver
pause
