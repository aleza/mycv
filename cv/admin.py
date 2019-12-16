from django.contrib import admin

from .models import Personal
from .models import Resume
from .models import Education
from .models import Courses
from .models import Hobbies


admin.site.register(Personal)
admin.site.register(Resume)
admin.site.register(Education)
admin.site.register(Courses)
admin.site.register(Hobbies)