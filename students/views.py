from django.db.models import Q
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from webargs.djangoparser import use_args
from webargs.fields import Str

from .forms import CreateStudentForm
from .models import Student
from .utils import format_list_students


# HttpRequest
# HttpResponse


def index(request):

    return HttpResponse('Welkome to lms')

@use_args(
    {
        'first_name': Str(required=False),
        'last_name': Str(required=False),
    },
    location='query'
)
def get_students(request, args):
    students = Student.objects.all().order_by('birthday')

    # if 'first_name' in args:
    #     students = students.filter(first_name=args['first_name'])
    #
    # if 'last_name' in args:
    #     students = students.filter(last_name=args['last_name'])
    if len(args) and (args.get('first_name') or args.get('last_name')):
        students = students.filter(
            Q(first_name=args.get('first_name', '')) | Q(last_name=args.get('last_name', ''))
        )

    form = '''
    <form method="get">
      <label for="fname">First name:</label>
      <input type="text" id="fname" name="first_name"><br><br>
      <label for="lname">Last name:</label>
      <input type="text" id="lname" name="last_name"><br><br><br>
      <input type="submit" value="Submit"><br>
    </form>'''

    string = form + format_list_students(students)
    response = HttpResponse(string)
    return response

# @csrf_exempt
def create_student_view(request):
    if request.method == 'GET':
        form = CreateStudentForm()
    elif request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')

    token = get_token(request)
    # form = CreateStudentForm()
    html_form = f'''
        <form method="post">
            <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
            <table>
                {form.as_table()}
            </table>
          <input type="submit" value="Submit"><br>
        </form>'''

    return HttpResponse(html_form)
