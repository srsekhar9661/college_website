from django.shortcuts import render
from django.views.generic import TemplateView
import pandas as pd
from student_info.models import Department, StudentProfile
from django.views.generic import ListView
from django.views import View
from auth_app.mixins import StaffLoginRequiredMixin


class IndexPage(TemplateView):
    template_name = 'college/index.html'


class DepartmentList(StaffLoginRequiredMixin,ListView):
    model = Department
    template_name = 'college/departments.html'
    context_object_name = 'depts'


class DepartmentStudentView(StaffLoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        students_list = StudentProfile.objects.filter(application__department__code=kwargs['dept'])
        return render(self.request, 'college/dept_students.html', {'students':students_list})



from django.http import HttpResponse
from auth_app.models import MyUser
import pandas as pd

def download_user_details_csv(request):
    users = MyUser.objects.all()

    data = {
        'Email':[user.email for user in users],
        'Mobile_number' : [user.mobile_number for user in users],
        'Is Student' : [ "Student" if user.is_student else "Staff" for user in users]
    }

    df = pd.DataFrame(data)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="user_details.csv"'

    df.to_csv(response)

    return response


def browse_csv(request):
    # Assuming you have a csv file
    excel_file = r"C:\Users\lenovo\Downloads\Sample - Superstore.xls"
    # import ipdb;ipdb.set_trace(context=15)
    df = pd.read_excel(excel_file)
    data = df.to_dict('records')  # Convert DataFrame to list of dictionaries
    columns = df.columns.tolist()  # Get column names
    return render(request, 'college/browse_csv.html', {'data': data[99:120], 'columns': columns})

    
from .forms import UploadCSVForm

def upload_csv(request):
    if request.method == "POST":
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES)
            
            csv_file = form.cleaned_data['csv_file']

            data = pd.read_excel(csv_file)
            return render(request, 'college/upload_cvs.html', {'data':data})
    else:
        form = UploadCSVForm()
        return render(request, 'college/upload_csv.html', {'form':form})